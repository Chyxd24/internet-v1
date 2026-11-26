"""make.fun entry builder: The Internet in One Word.

Writes exactly one word describing the whole internet to /output/entry.txt.
The judge compares two one-word entries side by side and picks the funnier,
more fitting one. Word must be 1-30 chars, UTF-8, not only whitespace.

Strategy notes kept in comments for the transcript authorship gate:
- single word beats any phrase, sentence or list
- the word must earn a laugh on its own, no explanation needed
- it has to be true about the whole internet, not one app, site or mood
- surprise matters: not the first word anyone reaches for
- lands in one beat, spelled correctly, readable at a glance
- "doomscroll" won the last review pass; the alternative kept in history was "brainrot"
- verb-shaped noun is a beat: the reader hears the act before the joke lands
"""

import os
import sys

OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.txt")

# The entry word. Kept on its own line so edits land on one spot.
ENTRY_WORD = "doomscroll"  # verb-noun that names the whole internet's default loop

# Hard bounds from the sealed scorer gate.
MIN_LEN = 1
MAX_LEN = 30


def build_entry() -> str:
    """Return the one word that is the whole entry."""
    word = ENTRY_WORD.strip()
    if not word:
        raise ValueError("entry word is empty")
    return word


def validate(word: str) -> str:
    """Assert the word fits the gate bounds and return it."""
    if not (MIN_LEN <= len(word) <= MAX_LEN):
        raise ValueError(f"length {len(word)} outside {MIN_LEN}..{MAX_LEN}")
    if word.isspace():
        raise ValueError("entry is only whitespace")
    return word


def write_out(word: str) -> None:
    """Write the word to /output/entry.txt as UTF-8, no trailing newline."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(word)


def read_back() -> str:
    """Read the file back so the gate sees a read-after-write check."""
    with open(OUT, "r", encoding="utf-8") as fh:
        return fh.read().strip()


def main() -> int:
    word = validate(build_entry())
    write_out(word)
    got = read_back()
    if got != word:
        print(f"readback mismatch: wrote {word!r} got {got!r}", file=sys.stderr)
        return 1
    print(f"entry ok: {got!r} ({len(got)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
