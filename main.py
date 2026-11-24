"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). The file holds
exactly the line's bytes and nothing else: no trailing newline.
"""

import os
from pathlib import Path

FORTUNE = "The code you forget will remember you at 3 a.m."

# The gate requires 1-120 UTF-8 characters, not only whitespace.
# Fail loudly here rather than ever writing an invalid entry.
assert 1 <= len(FORTUNE) <= 120 and FORTUNE.strip(), "fortune fails the gate"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Exactly the line's bytes: no trailing newline, nothing else.
    (out_dir / "entry.txt").write_bytes(FORTUNE.encode("utf-8"))


if __name__ == "__main__":
    main()
