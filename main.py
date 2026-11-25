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

Gate validation: ENTRY is stripped and must be 1-200 characters and
not only whitespace, otherwise the program exits 1 with an error.
The output is written atomically via a temporary file + os.replace,
so a failed run never leaves a partial entry.txt behind.
"""
import os
import sys

ENTRY = "Beware the human who says 'just one quick question' — it is never one, and it is never quick."


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print("error: ENTRY must be 1-200 non-whitespace characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
