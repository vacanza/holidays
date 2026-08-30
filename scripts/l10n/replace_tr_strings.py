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
    python scripts/l10n/replace_tr_strings.py
    python scripts/l10n/replace_tr_strings.py --country bulgaria
"""

import argparse
import ast
import json
from pathlib import Path

_JSON_PATH = Path("scripts/l10n/holidays_l10n.json")


def build_reverse_map(data: list[dict]) -> tuple[dict[str, str], dict[str, set[str]]]:
    """Build reverse lookup: translation string -> msgid.

    Only includes strings that unambiguously map to exactly one msgid
    across all languages to avoid incorrect replacements.
    """
    candidates: dict[str, set[str]] = {}
    for entry in data:
        msgid = entry.get("msgid", "")
        for lang, val in entry["messages"].items():
            if isinstance(val, str):
                candidates.setdefault(val, set()).add(msgid)
    ambiguous = {val: msgids for val, msgids in candidates.items() if len(msgids) > 1}
    return {
        val: next(iter(msgids)) for val, msgids in candidates.items() if len(msgids) == 1
    }, ambiguous


def build_comment_map(data: list[dict]) -> dict[str, str]:
    """Build lookup: msgid -> new_comment (empty string if none)."""
    return {entry["msgid"]: entry.get("new_comment", "") for entry in data if entry.get("msgid")}


def _char_offset_from_byte_offset(line: str, byte_offset: int) -> int:
    encoded = 0
    for i, ch in enumerate(line):
        if encoded == byte_offset:
            return i
        encoded += len(ch.encode("utf-8"))
    if encoded == byte_offset:
        return len(line)
    raise ValueError(f"byte offset {byte_offset} does not fall on a character boundary")


def replace_tr_calls(
    source: str,
    reverse_map: dict[str, str],
    comment_map: dict[str, str],
    ambiguous_map: dict[str, set[str]] | None = None,
    path: str = "",
) -> tuple[str, int]:
    """Replace tr() string arguments with msgid keys and update comments above."""
    lines = source.splitlines(keepends=True)
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source, 0

    changes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            is_tr = (isinstance(node.func, ast.Name) and node.func.id == "tr") or (
                isinstance(node.func, ast.Attribute) and node.func.attr == "tr"
            )
            if is_tr and node.args and isinstance(node.args[0], ast.Constant):
                arg = node.args[0]
                s = arg.value
                if not isinstance(s, str):
                    continue
                if arg.end_lineno is None or arg.end_col_offset is None:
                    continue
                if s in reverse_map and reverse_map[s] != s:
                    changes.append((arg, s, reverse_map[s]))
                elif ambiguous_map and s in ambiguous_map:
                    print(f"WARNING: ambiguous string in {path} line {arg.lineno}: {s!r}")
                    print(f"  maps to: {ambiguous_map[s]}")

    line_starts = [0]
    for line in lines:
        line_starts.append(line_starts[-1] + len(line))

    def to_char_offset(lineno, byte_col):
        return line_starts[lineno - 1] + _char_offset_from_byte_offset(lines[lineno - 1], byte_col)

    spans = []
    for arg, old, new in changes:
        start = to_char_offset(arg.lineno, arg.col_offset)
        end = to_char_offset(arg.end_lineno, arg.end_col_offset)
        spans.append((start, end, repr(new)))

    for arg, old, new in changes:
        new_msgid = reverse_map.get(old, "")
        new_comment = comment_map.get(new_msgid, None)
        if new_comment is None:
            continue
        # Find all consecutive comment lines above the tr() call
        comment_end_lineno = arg.lineno - 2
        if comment_end_lineno < 0:
            continue
        comment_line = lines[comment_end_lineno]
        stripped = comment_line.lstrip()
        # If line above string is tr( itself, look one more line up
        if stripped.startswith("tr(") or stripped == "tr(":
            comment_end_lineno -= 1
            if comment_end_lineno < 0:
                continue
            comment_line = lines[comment_end_lineno]
            stripped = comment_line.lstrip()
        if not stripped.startswith("#"):
            continue
        indent = comment_line[: len(comment_line) - len(stripped)]
        # Walk backwards to find start of multi-line comment
        comment_start_lineno = comment_end_lineno
        while comment_start_lineno > 0:
            prev = lines[comment_start_lineno - 1].lstrip()
            if prev.startswith("#"):
                comment_start_lineno -= 1
            else:
                break
        start = line_starts[comment_start_lineno]
        end = line_starts[comment_end_lineno + 1]
        if new_comment:
            spans.append((start, end, f"{indent}# {new_comment}\n"))
        else:
            spans.append((start, end, ""))

    source = "".join(lines)
    for start, end, new_val in sorted(spans, key=lambda c: c[0], reverse=True):
        source = source[:start] + new_val + source[end:]

    return source, len(changes)


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        description="Replace tr() strings with msgid keys and update l10n comments."
    )
    arg_parser.add_argument(
        "--country",
        type=str,
        help="Process a single country file (e.g. bulgaria).",
    )
    args = arg_parser.parse_args()

    with _JSON_PATH.open(encoding="utf-8") as f:
        data = json.load(f)

    reverse_map, ambiguous_map = build_reverse_map(data)
    comment_map = build_comment_map(data)
    print(f"Reverse map entries: {len(reverse_map)}")

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
        new_source, count = replace_tr_calls(
            source, reverse_map, comment_map, ambiguous_map, str(path)
        )
        if count > 0:
            total_replacements += count
            print(f"{path} - {count} replacements")
            path.write_text(new_source, encoding="utf-8", newline="\n")

    print(f"\nTotal replacements: {total_replacements}")


if __name__ == "__main__":
    main()
