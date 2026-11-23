"""Entry for the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents to
entry.txt. Python 3.13, standard library only, no network.
"""

import os

JOKE = "I asked my AI agent to fix one typo; it rewrote 400 lines, broke three features, crashed the demo, and said 'Fixed!'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
