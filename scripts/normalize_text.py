#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import re
import sys
from pathlib import Path

FIND_URL_PATTERN = re.compile(r'https?://[^\s<>"]+')
REPLACEMENTS = {
    # Space (U+0020)
    " ": " ",  # No-Break Space (U+00A0)
    # Quotation Mark (U+0022)
    "“": '"',  # Left Double Quotation Mark (U+201C)
    "”": '"',  # Right Double Quotation Mark (U+201D)
    # Apostrophe (U+0027)
    "‘": "'",  # Left Single Quotation Mark (U+2018)
    "’": "'",  # Right Single Quotation Mark (U+2019)
    # Hyphen Minus (U+002D)
    "–": "-",  # En Dash (U+2013)
    "—": "-",  # Em Dash (U+2014)
    "−": "-",  # Minus Sign (U+2212)
}
REPLACEMENT_TABLE = str.maketrans(REPLACEMENTS)
FORBIDDEN_CHARS = set(REPLACEMENTS)


class TextNormalizer:
    """Normalize text by replacing non-standard Unicode with ASCII."""

    @staticmethod
    def normalize(text: str) -> str:
        """Apply character replacements to a string while preserving URLs."""
        result: list[str] = []
        last_end = 0
        for match in FIND_URL_PATTERN.finditer(text):
            start, end = match.start(), match.end()
            result.append(text[last_end:start].translate(REPLACEMENT_TABLE))
            result.append(match.group())
            last_end = end
        result.append(text[last_end:].translate(REPLACEMENT_TABLE))
        return "".join(result)

    @staticmethod
    def fix_file(path: Path) -> bool:
        """Normalize a single file.

        Returns:
            True if file was modified, False otherwise.
        """
        if not path.is_file():
            return False
        try:
            # For Python >=3.13: original = path.read_text(encoding="utf-8", newline="")
            with path.open("r", encoding="utf-8", newline="") as f:
                original = f.read()
        except Exception as e:
            print(f"Warning: Could not read {path}: {e}", file=sys.stderr)
            return False
        # Skip binary files
        if "\x00" in original:
            return False
        # Fast exit
        if FORBIDDEN_CHARS.isdisjoint(original):
            return False
        fixed = TextNormalizer.normalize(original)
        if fixed == original:
            return False
        try:
            path.write_text(fixed, encoding="utf-8", newline="")
        except Exception as e:
            print(f"Error writing {path}: {e}", file=sys.stderr)
            return False
        return True

    def run(self) -> int:
        """Run normalization over all files passed as command-line arguments."""
        changed = False
        for filename in sys.argv[1:]:
            path = Path(filename)
            if self.fix_file(path):
                print(f"Fixed: {path}")
                changed = True
        return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(TextNormalizer().run())
