#!/usr/bin/env python3
"""The Piano — a short poem about agency.

Two people carry a piano through a doorway: neither can move it
alone, but once they agree on one plan — lift on three — the
weight becomes theirs together. Agency here is not solo power;
it is the choice to act as one.

Writes the poem (185 characters) to /output/entry.txt.
Deterministic, standard library only.
"""

import os

POEM = """The Piano
We lift on three — your end dips low,
mine rises, keys rattling, and the doorway lets us through.
I cannot move it. You cannot move it.
Together, we carry the weight we chose."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
