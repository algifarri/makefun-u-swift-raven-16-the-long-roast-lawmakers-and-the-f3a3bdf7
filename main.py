"""Entry for make.fun: The Long Roast — Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    "They passed a law to govern machines that learn, then adjourned in defeat: "
    "their own act was stranded as FINAL_draft_v9.docx, and the chamber's one "
    "working PDF button was greyed out."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 320, "entry must fit the 320-character gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
