#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

Writes a single line (<=200 UTF-8 characters) to /output/entry.txt.
Deterministic, standard library only, no network.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY = (
    "I blanked on question one of my finals, and the invigilator, deadpan, "
    "slid me a mint and whispered, 'Brains run on sugar. Begin again.' I passed."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_ENTRY_CHARS) or not ENTRY.strip():
        raise ValueError("ENTRY must be 1-200 characters and not blank")
    ENTRY.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
