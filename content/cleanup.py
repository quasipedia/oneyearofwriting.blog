#! /usr/bin/env python
#!/usr/bin/env python3
import sys
import pathlib
import re

REPLACEMENTS = {
    # Quotes
    "“": '"',
    "”": '"',
    "„": '"',
    "«": '"',
    "»": '"',
    "‘": "'",
    "’": "'",
    "‚": "'",

    # Dashes
    "—": "--",   # em dash
    "–": "-",    # en dash
    "−": "-",    # minus sign

    # Ellipsis
    "…": "...",

    # Misc
    "\u00a0": " ",  # non-breaking space
    "•": "*",
    "×": "x",
}

# Regex patterns for footnotes
FOOTNOTE_REF_RE = re.compile(r"\[(\d+)\]\(#fn:\1\)")
FOOTNOTE_DEF_RE = re.compile(r"^(\d+)\.\s+", re.MULTILINE)

def normalize_typography(text: str) -> str:
    for src, dst in REPLACEMENTS.items():
        text = text.replace(src, dst)
    return text

def normalize_footnotes(text: str) -> str:
    # [1](#fn:1) -> [^1]
    text = FOOTNOTE_REF_RE.sub(r"[^\1]", text)

    # 1. <text> -> [^1]: <text>
    text = FOOTNOTE_DEF_RE.sub(r"[^\1]: ", text)

    return text

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.md>", file=sys.stderr)
        sys.exit(1)

    path = pathlib.Path(sys.argv[1])

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    text = normalize_typography(text)
    text = normalize_footnotes(text)

    sys.stdout.write(text)

if __name__ == "__main__":
    main()
