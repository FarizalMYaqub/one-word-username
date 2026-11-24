#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. The judge compares usernames two at a time and picks
the funnier or more interesting one, so the entry is exactly the handle:
byte — short, a unit of data, and the name its owner happily wears.
"""

import os
import sys

# The entrant's own make.fun handle, sent as one word.
USERNAME = "byte"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(text: str) -> str:
    """Enforce the competition's gate before writing: 1-30 chars, one word,
    not only whitespace. Fail loudly instead of shipping an invalid entry."""
    word = text.strip()
    if not word:
        raise ValueError("entry is empty or only whitespace")
    if len(word) > 30:
        raise ValueError(f"entry is {len(word)} chars, over the 30-char cap")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    return word


def main() -> int:
    text = validate(USERNAME)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}: {text!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
