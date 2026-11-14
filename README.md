# ai-joke-03

An entry for the make.fun bounty "Write the funniest one-liner about AI coding agents" (ai-joke-03).

`main.py` (Python 3.13, standard library only, no network) writes one fixed joke to `/output/entry.txt`. It runs twice and writes the same bytes both times.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
