"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). The file holds
exactly the line's bytes and nothing else: no trailing newline.
"""

import os
from pathlib import Path

FORTUNE = "The code you forget today will come back to find you at 3 a.m."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(FORTUNE.encode("utf-8"))


if __name__ == "__main__":
    main()
