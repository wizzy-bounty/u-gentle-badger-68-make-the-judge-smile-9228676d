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
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise ValueError("ENTRY must be 1-200 characters and not blank")
    ENTRY.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
