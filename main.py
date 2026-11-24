#!/usr/bin/env python3
"""Write the entry for Angry Judge: The Short Rant Contest.

The entry is one short rant about an everyday annoyance: a printer
that refuses to print on the one morning a report is due.  This
program builds the rant from its beats, checks the result against
the bounty's gate (UTF-8 text of 1 to 400 characters, not only
whitespace), writes it to /output/entry.txt with no trailing
newline, and reads the file back for a byte-for-byte comparison.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 400

# The rant is assembled beat by beat rather than kept as a single
# literal.  The opening states the printer's one job, the idle
# beat shows it doing nothing all week until the deadline morning,
# the questions beat calls out the absurd paper message, the care
# beat lists everything the narrator already tried, the test-page
# beat lands the betrayal, and the closing beat delivers the
# verdict.  Single spaces join every word into one line.
OPENING_WORDS = ("The", "printer", "has", "ONE", "job.", "One.")
IDLE_WORDS = (
    "It", "sits", "there", "all", "week", "doing", "nothing,",
    "and", "the", "morning", "my", "report", "is", "due", "it",
    "chooses", "violence:", "'PC", "LOAD", "LETTER.'",
)
QUESTION_WORDS = (
    "Load", "what?", "It's", "A4.", "It", "has", "been", "A4",
    "since", "1997.",
)
CARE_WORDS = ("I", "have", "fed", "it,", "cleaned", "it,", "begged", "it.")
TEST_PAGE_WORDS = (
    "It", "printed", "a", "test", "page.", "A", "TEST", "PAGE.",
    "Perfectly.",
)
CLOSING_WORDS = (
    "Then", "it", "looked", "at", "my", "deadline", "and", "chose",
    "death.",
)

BEATS = (
    OPENING_WORDS,
    IDLE_WORDS,
    QUESTION_WORDS,
    CARE_WORDS,
    TEST_PAGE_WORDS,
    CLOSING_WORDS,
)


def assemble_rant() -> str:
    """Join every beat's words into the rant's single line."""
    words = []
    for beat in BEATS:
        words.extend(beat)
    return " ".join(words)


def validate_rant(text: str) -> None:
    """Raise ValueError if the assembled rant breaks any rule."""
    if not text or not text.strip():
        raise ValueError("rant must not be empty or only whitespace")
    if len(text) < MIN_LENGTH:
        raise ValueError("rant must contain at least one character")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"rant must be at most {MAX_LENGTH} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("rant must be a single line with no newline")
    if text != text.strip():
        raise ValueError("rant must not have leading or trailing space")
    if "  " in text:
        raise ValueError("rant must use single spaces between words")
    if not text.endswith("."):
        raise ValueError("rant must end with a full stop")
    if "\t" in text:
        raise ValueError("rant must not contain a tab")
    if not text.isascii():
        raise ValueError("rant must be plain ASCII")
    if not text[0].isupper():
        raise ValueError("rant must start with a capital letter")
    if text.count("?") != 1:
        raise ValueError("rant must ask its one incredulous question")
    # The line must agree with the beats it was built from: rebuild
    # the word list here and check the total count and each beat's
    # boundary, so an edit to one beat cannot silently shift the
    # entry's wording or drop a beat altogether.
    words = text.split(" ")
    expected_words = sum(len(beat) for beat in BEATS)
    if len(words) != expected_words:
        raise ValueError(
            f"rant must have {expected_words} words, got {len(words)}"
        )
    offset = 0
    for beat in BEATS:
        if tuple(words[offset : offset + len(beat)]) != beat:
            raise ValueError("rant beat does not match its parts")
        offset += len(beat)
    for marker in ("'PC", "LOAD", "LETTER.'", "TEST", "PAGE.", "1997."):
        if marker not in words:
            raise ValueError(f"rant must keep its {marker} turn")
    if "deadline" not in words or "death." not in words:
        raise ValueError("rant must keep its deadline and death closing")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("rant must survive a UTF-8 round trip")
    if len(encoded) != len(text):
        raise ValueError("rant must encode to one byte per character")


def main() -> int:
    rant = assemble_rant()
    validate_rant(rant)

    payload = rant.encode("utf-8")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(payload)

    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != payload:
        print("byte comparison failed after writing", file=sys.stderr)
        return 1
    if written.decode("utf-8") != rant:
        print("round-trip text mismatch after writing", file=sys.stderr)
        return 1
    if len(written) != len(rant):
        print("written byte count differs from rant length", file=sys.stderr)
        return 1
    if assemble_rant() != rant:
        print("reassembly does not reproduce the rant", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
