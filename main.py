# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed
# joke, a one-liner about AI coding agents, to /output/entry.txt.
# Deterministic: every run writes the same bytes. No network, no randomness.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "I asked my AI coding agent to fix one bug. It rewrote the whole file, deleted the tests, and opened a PR titled 'trust me'."

# Guardrail: the gate takes 1-280 characters, not only white space.
assert 1 <= len(JOKE) <= 280 and any(not c.isspace() for c in JOKE)

Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
