"""One Word From Your Ex — print the single word an ex would use.

The entry itself lives in entry.txt (exactly one word). This program reads
it, checks it really is one word, and prints it.
"""

from pathlib import Path


def load_word(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    words = text.split()
    if len(words) != 1:
        raise ValueError("entry.txt must hold exactly one word")
    word = words[0]
    if not word.isalpha():
        raise ValueError("the entry must be a single word of letters")
    return word


def main() -> int:
    word = load_word(Path(__file__).with_name("entry.txt"))
    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
