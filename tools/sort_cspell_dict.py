#!/usr/bin/env python3
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

"""
Sort and uniquify the custom dictionary file for cspell.
"""

import sys
from pathlib import Path


def sort_custom_dict():
    dict_file = Path(__file__).parent.parent / "cspell" / "custom-dict.txt"
    if not dict_file.exists():
        raise SystemExit(f"Dictionary file {dict_file} not found.")

    with open(dict_file, encoding="utf-8") as f:
        words = f.read().splitlines()

    # Remove duplicates while preserving order (case-sensitive)
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)

    # Sort the words
    unique_words.sort()

    with open(dict_file, "w", encoding="utf-8") as f:
        f.write("\n".join(unique_words) + "\n")

    sys.stdout.write(f"Sorted and uniquified {dict_file}\n")


if __name__ == "__main__":
    sort_custom_dict()
