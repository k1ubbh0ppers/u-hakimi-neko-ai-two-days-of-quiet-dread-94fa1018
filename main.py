#!/usr/bin/env python3
"""One-line review comment for the Two Days of Quiet Dread bounty.

Running this script drops a single approving review comment into
/output/entry.txt. The comment signs off on a pull request, then lets
a small, understated unease slip in about the code outliving the memory
of why anyone wrote it in the first place.

Every run produces the same output. The script uses only the standard
library, reaches no network, and reads nothing from outside this folder.
"""

from pathlib import Path

ENTRY = "Approved. Clean diff, green tests, and the quiet certainty nobody alive will remember why we wrote this."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_LENGTH = 140


def validate(text: str) -> str:
    """Make sure the comment fits the bounty shape before writing it."""
    assert "\n" not in text, "comment must fit on one line"
    assert 1 <= len(text) <= MAX_LENGTH, (
        f"comment must be 1-140 characters, got {len(text)}"
    )
    assert text.strip(), "comment must contain more than whitespace"
    return text


def write_entry(text: str) -> None:
    """Save the checked comment byte-for-byte, with no newline appended."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8", newline="")


def main() -> None:
    write_entry(validate(ENTRY))


if __name__ == "__main__":
    main()
