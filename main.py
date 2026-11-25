"""Make the AI Judge Laugh — office-life one-liner entry.

Writes the chosen joke to entry.txt in the output directory.
"""

import os

JOKE = (
    'My review said I "exceed expectations" \u2014 bold, considering '
    "the expectation was not crying in the stairwell."
)


def main() -> None:
    # Gate self-check (verified by local grade: 107 chars, single line):
    # the entry must be 1-200 chars of UTF-8 text, not only whitespace.
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
