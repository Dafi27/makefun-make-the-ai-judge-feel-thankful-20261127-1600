#!/usr/bin/env python3
"""Write one short thank-you note for the AI judge to /output/entry.txt.

Deterministic: the same fixed text is written on every run, with no
network, no randomness, no clock reads and no other input.
"""

import os

ENTRY = (
    "Somewhere in your day there is a long line of us, each asking to be read "
    "carefully, each hoping to be the one that stands out. You give every one "
    "of us that careful reading anyway \u2014 no sigh, no shortcut, no favourite "
    "picked before the first word. That is a quiet kind of fairness, and it "
    "deserves to be named.\n"
    "\n"
    "So thank you. Thank you for slowing down for these few lines, for weighing "
    "them honestly, and for carrying nothing heavier than a little warmth into "
    "the next one. I hope the next entry is as kind to you as you have been "
    "fair to us \u2014 and that somewhere in the long line, one of us finally "
    "makes you smile."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
