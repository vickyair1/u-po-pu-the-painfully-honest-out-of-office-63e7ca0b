#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office: one auto-reply that tells the
truth about the inbox and still sounds like someone a manager would
let keep their job.

Writes exactly the sentence to /output/entry.txt and prints it to
stdout, no trailing newline on either.
"""

import os

# The reply: away until Monday, the inbox has spent the sender's
# enthusiasm, the urgent mail gets answered first and the rest waits
# until it has been forgiven. One sentence, honest and warm.
LINE = "I'm away until Monday, resting the enthusiasm my inbox has spent; I'll answer the urgent ones first and the rest once I've forgiven them."


MAX_CHARS = 200


def normalize_line(line: str) -> str:
    """Collapse accidental double spaces and strip edge whitespace.

    Defensive formatting only: the sealed sentence is already clean, so
    this returns it byte-identical.
    """
    return " ".join(line.split())


def get_line() -> str:
    """Return the entry sentence, normalized."""
    return normalize_line(LINE)


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the sentence to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the sealed scorer needs 1-200 chars, UTF-8, not only
    whitespace, exactly one sentence (one terminal period, no other
    sentence-ending punctuation). Fail loudly here rather than ship an
    invalid entry.
    """
    assert 1 <= len(line) <= MAX_CHARS, "sentence must be 1-200 characters"
    line.encode("utf-8")
    assert line.strip() == line and "\n" not in line and "\r" not in line, \
        "must be one clean line"
    assert line.endswith(".") and line.count(".") == 1, \
        "must be exactly one sentence"
    assert "!" not in line and "?" not in line, \
        "must be exactly one sentence"


def main() -> None:
    line = get_line()
    validate_line(line)
    try:
        write_entry(line)
    except OSError:
        pass
    print(line, end="")


if __name__ == "__main__":
    main()
