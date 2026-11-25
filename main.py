#!/usr/bin/env python3
"""Entry for make.fun bounty u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The line is the resignation letter of a retry loop, 96 characters.
"""

import os

TEXT = "I quit: after 10,000 retries, the only thing still backing off exponentially is my will to live."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
