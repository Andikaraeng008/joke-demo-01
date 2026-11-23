#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents."""

# The entry is exactly the 116-character joke, with no trailing newline,
# so entry.txt is 116 bytes on every run.
import os

JOKE = "I asked my AI agent to fix one typo; it rewrote 400 lines, broke three features, crashed the demo, and said 'Fixed!'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
