"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt, as the competition
requires. The program is fully deterministic: no input, no network, no
randomness, standard library only.
"""

from pathlib import Path

# The joke. One line, no setup notes, no explanation: the setup and the
# twist live inside the line itself, and the punchline lands in the final
# quoted beat, so a cold reader gets the whole turn at once.
JOKE = (
    "I tried meditating, but my inner voice narrates everything "
    "like a nature documentary: "
    "'Here we see the human, pretending to relax.'"
)

# Gate limits from RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, not only
    whitespace, exactly one line."""
    text = line.strip()
    if len(text) < MIN_CHARS:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    line = validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    # Re-read and re-validate what actually landed on disk, so a silent
    # write problem can never ship a gate-failing file.
    written = validate(OUTPUT_PATH.read_text(encoding="utf-8"))
    if written != line:
        raise ValueError("written entry does not match the joke")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
