#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes a single line to /output/entry.txt: a text message that reads as a
real autocorrect slip. The wrong word ("pubic" for "public") is a classic
one-letter autocorrect accident, and it lands in an ordinary reminder from
one parent to another, so the joke is clear on first read with no setup.

Deterministic: the entry is a fixed string; no time, randomness, network
or environment input is used. Standard library only.
"""

import os

ENTRY = (
    "Don't forget Jake starts pubic school on Monday - we still need to buy "
    "his uniform, backpack, and lunchbox this weekend!"
)


def main() -> None:
    # Enforce the gate ourselves: one line, 1-199 characters, not blank.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry is {len(text)} characters, must be 1-199")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
