#!/usr/bin/env python3
"""
Sort and uniquify the custom dictionary file for cspell.
"""

import sys
from pathlib import Path

def sort_custom_dict():
    dict_file = Path(__file__).parent.parent / "cspell" / "custom-dict.txt"
    if not dict_file.exists():
        print(f"Dictionary file {dict_file} not found.")
        return

    with open(dict_file, 'r', encoding='utf-8') as f:
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

    with open(dict_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_words) + '\n')

    print(f"Sorted and uniquified {dict_file}")

if __name__ == "__main__":
    sort_custom_dict()
