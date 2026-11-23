#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

Writes a single line (<=200 UTF-8 characters) to /output/entry.txt.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "The bus driver waited while an old man counted his coins twice, "
    "then waved the fare away: 'pay me back with a good day.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
