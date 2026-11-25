#!/usr/bin/env python3
"""Fortune Cookies for Machines — one-line fortune entry.

Writes the fortune an AI agent would crack open to /output/entry.txt.
Standard library only: no third-party imports, so it runs in the
grading sandbox as well as in a clean local directory.

The fortune: "Beware the human who says 'just one quick question' —
it is never one, and it is never quick." (93 characters, one line.)
A warning in classic fortune-cookie voice, aimed at the one human
every agent knows: the one whose "quick question" is never one
question, and never quick.
"""
import os

ENTRY = "Beware the human who says 'just one quick question' — it is never one, and it is never quick."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
