#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

Writes a single flat approve-with-dread line to /output/entry.txt.
Standard library only; deterministic; no network.
"""

import os

LINE = (
    "Approved. The tests pass, the code is clean, and the void has "
    "reviewed this diff too \u2014 it had no comments. Ship it."
)

OUTPUT = "/output/entry.txt"


def validate(text: str) -> str:
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} chars, must be 1-140")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate(LINE.strip())
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
