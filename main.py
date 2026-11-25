#!/usr/bin/env python3
"""Entry for make.fun's "How Many Tabs Do You Have Open?" bounty.

Writes one number in digits -- and nothing else -- to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

TABS = "247"


def main():
    # Fail fast if the entry ever stops being one number in digits.
    if not TABS.isdigit():
        raise SystemExit("TABS must be one number in digits")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TABS)


if __name__ == "__main__":
    main()
