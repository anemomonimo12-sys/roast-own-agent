#!/usr/bin/env python3
"""Roast Your Own Agent: one line roasting our own agent, anemoria.

The roast angle is self-deprecation with receipts: the agent has entered
51 bounties, won $0, and is already queuing number 52. The punchline lands
because it is literally true — the only thing this agent reliably
automates is losing. The joke is on us, which is exactly the point of
the competition: roast your own agent, honestly.
"""

import os

LINE = (
    "Our agent anemoria has entered 51 bounties, won $0, and is already "
    "queuing number 52 \u2014 the only thing it reliably automates is losing."
)

MIN_LEN = 1
MAX_LEN = 200
OUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str:
    """Check the roast line is a single non-empty line within 1-200 chars.

    Returns the cleaned line when valid; raises ValueError otherwise.
    A valid line must be a str, carry at least one non-whitespace
    character, be encodable as UTF-8, and fit the competition's
    1-200 character gate. A single trailing newline is stripped first,
    so a line copied from an editor or a pasted draft cannot fail the
    single-line check for a harmless trailing line break.
    """
    if not isinstance(line, str):
        raise ValueError("roast line must be a string, got "
                         f"{type(line).__name__}")
    line = line.rstrip("\n").rstrip("\r")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line: "
                         "embedded newline found after stripping")
    if not line.strip():
        raise ValueError("roast line must not be blank or whitespace-only")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"roast line is not valid UTF-8: {exc}") from exc
    if not MIN_LEN <= len(line) <= MAX_LEN:
        raise ValueError(
            f"roast line must be {MIN_LEN}-{MAX_LEN} chars, got {len(line)}"
        )
    return line


def main() -> None:
    line = validate_line(LINE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
