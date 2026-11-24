"""make.fun bounty: One Letter for Your Day.

Deterministic, no-network program. Writes exactly one letter, A-Z,
to /output/entry.txt. The letter is M, for "mango": this morning a
neighbour left a mango on the user's doorstep with a note saying
"too many, please help", and it honestly made his whole day.
Running twice writes identical bytes.
"""
from pathlib import Path

LETTER = "M"  # M for "mango"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LETTER, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LETTER)} char)")


if __name__ == "__main__":
    main()
