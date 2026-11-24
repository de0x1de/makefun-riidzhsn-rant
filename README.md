# makefun-riidzhsn-rant

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/de0x1de/makefun-riidzhsn-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/de0x1de/makefun-riidzhsn-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

## What this is

A small, dependency-free Python program for Angry Judge: The
Short Rant Contest. Running `main.py` writes exactly one text to
`/output/entry.txt`: a single short rant about an everyday
annoyance, with no trailing newline, well inside the
400-character limit the bounty sets.

The rant is about the office printer, the one machine whose only
job is printing and which picks the morning a report is due to
demand a paper size it has used since 1997. It builds beat by
beat: the one job stated up front, the week of doing nothing, the
nonsense error message, everything the narrator already fed,
cleaned and begged, the perfectly printed test page that proves
it could have cooperated all along, and the final look at the
deadline. The program does not store the rant as a lone literal.
It assembles the text from its beats, validates the result (a
single non-empty line of 1 to 400 characters, single-spaced,
ending with a full stop) before writing it as UTF-8. After
writing, it reads the file back and compares the bytes, so every
run produces exactly the same entry.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
