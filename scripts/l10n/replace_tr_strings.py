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

"""Replace tr() string arguments in .py files with new msgid keys.

Run with:
    python scripts/l10n/replace_tr_strings.py --preview
    python scripts/l10n/replace_tr_strings.py
"""

import argparse
import ast
import json
from pathlib import Path

_JSON_PATH = Path("scripts/l10n/holidays_l10n.json")


def build_reverse_map(data: list[dict]) -> dict[str, str]:
    """Build reverse lookup: translation string -> msgid."""
    reverse_map = {}
    for entry in data:
        msgid = entry.get("msgid", "")
        for lang, val in entry["messages"].items():
            if isinstance(val, str) and val not in reverse_map:
                reverse_map[val] = msgid
    return reverse_map


def _char_offset_from_byte_offset(line: str, byte_offset: int) -> int:
    encoded = 0
    for i, ch in enumerate(line):
        if encoded == byte_offset:
            return i
        encoded += len(ch.encode("utf-8"))
    if encoded == byte_offset:
        return len(line)
    raise ValueError(f"byte offset {byte_offset} does not fall on a character boundary")


def replace_tr_calls(source: str, reverse_map: dict[str, str]) -> tuple[str, int]:
    """Replace tr() string arguments with msgid keys."""
    lines = source.splitlines(keepends=True)
    replacements = 0
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source, 0

    changes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "tr":
                if node.args and isinstance(node.args[0], ast.Constant):
                    arg = node.args[0]
                    s = arg.value
                    if not isinstance(s, str):
                        continue
                    if arg.end_lineno is None or arg.end_col_offset is None:
                        continue
                    if s in reverse_map and reverse_map[s] != s:
                        changes.append((arg, s, reverse_map[s]))

    single_line = [c for c in changes if c[0].lineno == c[0].end_lineno]
    for arg, old, new in sorted(single_line, key=lambda c: c[0].lineno, reverse=True):
        lineno = arg.lineno
        line = lines[lineno - 1]
        for quote in (repr(old), f'"{old}"', f"'{old}'"):
            if quote in line:
                new_quoted = repr(new)
                lines[lineno - 1] = line.replace(quote, new_quoted, 1)
                replacements += 1
                break

    multi_line = [c for c in changes if c[0].lineno != c[0].end_lineno]
    for arg, old, new in sorted(multi_line, key=lambda c: c[0].lineno, reverse=True):
        if arg.end_lineno is None or arg.end_col_offset is None:
            continue
        start_line = lines[arg.lineno - 1]
        end_line = lines[arg.end_lineno - 1]
        start_char = arg.col_offset
        end_char = _char_offset_from_byte_offset(end_line, arg.end_col_offset)
        prefix = start_line[:start_char]
        suffix = end_line[end_char:]
        lines[arg.lineno - 1 : arg.end_lineno] = [prefix + repr(new) + suffix]
        replacements += 1

    return "".join(lines), replacements


def main() -> None:
    arg_parser = argparse.ArgumentParser(description="Replace tr() strings with msgid keys.")
    arg_parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview changes without writing to disk.",
    )
    arg_parser.add_argument(
        "--country",
        type=str,
        help="Process a single country file (e.g. bulgaria).",
    )
    args = arg_parser.parse_args()

    with _JSON_PATH.open(encoding="utf-8") as f:
        data = json.load(f)

    reverse_map = build_reverse_map(data)
    print(f"Reverse map entries: {len(reverse_map)}")

    paths = []
    if args.country:
        paths = [Path(f"holidays/countries/{args.country}.py")]
    else:
        paths = list(Path("holidays/countries").glob("*.py"))
        paths += list(Path("holidays/financial").glob("*.py"))

    total_replacements = 0
    for path in sorted(paths):
        if path.stem == "__init__":
            continue
        source = path.read_text(encoding="utf-8")
        new_source, count = replace_tr_calls(source, reverse_map)
        if count > 0:
            total_replacements += count
            print(f"\n{path} - {count} replacements")
            if args.preview:
                for old, new in zip(source.splitlines(), new_source.splitlines()):
                    if old != new:
                        print(f"  - {old.strip()}")
                        print(f"  + {new.strip()}")
            else:
                path.write_text(new_source, encoding="utf-8", newline="\n")

    print(f"\nTotal replacements: {total_replacements}")
    if args.preview:
        print("Preview only - no files written.")


if __name__ == "__main__":
    main()
