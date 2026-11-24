#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence -- a bizarre startup pitch that sounds like a joke
until the business logic lands -- to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the pitch is fixed in this file, so every run writes the
exact same bytes.

The pitch: we train crows to collect cigarette butts from city parks
and charge the city per kilo. Ridiculous at first glance (a crow
workforce), real by the second (cities already pay crews to pick up
butts, and the birds genuinely work for peanuts -- literally).
The payer is named, the thing sold is concrete, and the turn from
laughing to nodding is the last two words.
"""

import os
from pathlib import Path

PITCH = (
    "We train crows to collect cigarette butts from city parks "
    "and charge the city per kilo, because the birds work "
    "for peanuts - literally."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-200 characters, one sentence on one line, not only whitespace.
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(f"pitch is {len(PITCH)} characters, must be 1-200")
    if "\n" in PITCH or "\r" in PITCH:
        raise ValueError("pitch must be a single line")
    if not PITCH.strip():
        raise ValueError("pitch must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(PITCH, encoding="utf-8")
    print(f"Wrote {len(PITCH)} characters to {entry}")


if __name__ == "__main__":
    main()
