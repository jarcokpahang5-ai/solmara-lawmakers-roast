"""The Long Roast: Lawmakers and the File They Cannot Convert -- make.fun entry.

One satirical sentence roasting lawmakers who would regulate AI, crypto,
and the internet but cannot convert a file to PDF on their own. Before
they write a single rule, they must first convert one file to PDF
without calling IT, crying, or declaring the printer a national
security threat. This script checks that the sentence is a single
well-formed line, prints it, and stores it in /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The roast itself: one sentence, ending with a single period.
LINE = (
    "Before lawmakers may regulate AI, crypto, or the internet, they must first "
    "convert a single file to PDF without calling IT, crying, or declaring the "
    "printer a national security threat."
)

MAX_CHARS = 320
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check that the line is one roast within the limit."""
    if not isinstance(line, str):
        raise ValueError("roast must be text")
    if not line or line != line.strip():
        raise ValueError("roast must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if not line.endswith("."):
        raise ValueError("roast must end with a full stop")
    for mark in (". ", "! ", "? "):
        if mark in line:
            raise ValueError("roast must be one sentence, not several")
    return line


def store(line):
    """Print the roast and save it to the entry file."""
    print(line)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    # Validate first, so only a well-formed roast is ever stored.
    store(validate(LINE))


if __name__ == "__main__":
    main()
