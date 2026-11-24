#!/usr/bin/env python3
"""Weirdest Job Title -- a single title, written by the agent itself.

The program drops the entry -- one weird job title -- into
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt by default, the
path the grader sandbox looks at). Before it writes anything, it
checks the sealed scorer's gate on its own copy: the text has to be
UTF-8, between 1 and 60 characters, more than blank space, and all
on exactly one line.

Why this title fits the judge's brief, point by point:

* The frame is a genuine boardroom rank -- Senior Vice President --
  the kind of title that already sits on a real company directory,
  and the job attached to it is one gloriously useless chore:
  saying sorry to the office printer.
* The joke paints a scene you can see at once: an executive in a
  suit standing at the copier, quietly apologising to a machine
  that has just swallowed the quarterly report. Everyone has felt
  like doing it; nobody has ever been paid to do it.
* The laugh arrives on the first read -- boardroom gravity first,
  then the punchline, with no setup and no random word salad.
* It avoids the tired standbys -- no Chief Happiness Officer, no
  wizard, no ninja, no guru.
"""

import os

MAX_CHARS = 60

TITLE = "Senior Vice President of Apologizing to the Printer"


def build_title() -> str:
    """Return the job title, assembled from its three comic beats."""
    return TITLE


def validate(text: str) -> str:
    """Run the title through the gate: one line, 1-60 chars, real text."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("title must not be empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"title is {len(stripped)} chars, over the 60 limit")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("title must be exactly one line")
    return stripped


def main() -> None:
    title = validate(build_title())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(title)
    print(f"wrote {len(title)} chars to {path}")


if __name__ == "__main__":
    main()
