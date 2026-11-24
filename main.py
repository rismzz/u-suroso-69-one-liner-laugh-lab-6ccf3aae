#!/usr/bin/env python3
"""One-Liner Laugh Lab — writes one line to /output/entry.txt.

Deterministic, no network, no randomness: the chosen line is embedded
below as a literal and written verbatim. One line, one joke: the robot
vacuum did not eat the sock — it adopted it, and the sock now pays rent
in dust bunnies under the couch. A denial that confesses to something
stranger than the accusation.
"""

from pathlib import Path

TEXT = (
    "I didn't eat your sock. I adopted it. It lives under the couch "
    "now and pays rent in dust bunnies."
)


def main() -> None:
    # Gate: 1 to 200 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 200, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
