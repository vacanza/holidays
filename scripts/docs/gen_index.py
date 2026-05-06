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

"""Generate index.md and contributing.md with proper link."""

import re
from pathlib import Path

import mkdocs_gen_files


GFM_MKDOCS_MAPPING = {
    "note": "note",
    "tip": "tip",
    "important": "important",
    "warning": "warning",
    "caution": "danger",
}

FILES_REPLACE_MAPPING = {
    "examples.md": (
        (
            "[`HolidayBase`](https://github.com/vacanza/holidays/blob/main/holidays/holiday_base.py)",
            "[`HolidayBase`][holidays.HolidayBase]",
        ),
        (
            "[`ICalExporter`](https://github.com/vacanza/holidays/blob/main/holidays/ical.py)",
            "[`ICalExporter`][holidays.ical.ICalExporter]",
        ),
        (
            "[`country_holidays`](https://github.com/vacanza/holidays/blob/dev/holidays/utils.py)",
            "[`country_holidays`][holidays.utils.country_holidays]",
        ),
        (
            "[`financial_holidays`](https://github.com/vacanza/holidays/blob/dev/holidays/utils.py)",
            "[`financial_holidays`][holidays.utils.financial_holidays]",
        ),
        (
            "[`generate`](https://github.com/vacanza/holidays/blob/main/holidays/ical.py)",
            "[`generate`][holidays.ical.ICalExporter.generate]",
        ),
        (
            "[`save_ics`](https://github.com/vacanza/holidays/blob/main/holidays/ical.py)",
            "[`save_ics`][holidays.ical.ICalExporter.save_ics]",
        ),
    ),
    "index.md": (
        (
            "[CONTRIBUTING.md](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTING.md)",
            "[Contributing](contributing.md)",
        ),
        (
            "[`HolidayBase`](https://github.com/vacanza/holidays/blob/main/holidays/holiday_base.py)",
            "[`HolidayBase`][holidays.holiday_base.HolidayBase]",
        ),
    ),
}


def gfm_to_mkdocs(text: str) -> str:
    """Convert GitHub Flavored Markdown notes to ProperDocs admonitions."""
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not (match := re.match(r"^>\s*\[!(\w+)\]$", line)):
            out.append(line)
            i += 1
            continue

        note_type = GFM_MKDOCS_MAPPING.get(match.group(1).lower(), "note")
        i += 1

        title = ""
        if i < len(lines):
            if match := re.match(r"^>\s*\*\*(.+?)\*\*", lines[i]):
                title = f' "{match.group(1)}"'
                i += 1

        note_body = []
        while i < len(lines):
            line = lines[i]
            if not line.startswith(">"):
                break

            content = line[1:]
            if content.startswith(" "):
                content = content[1:]
            note_body.append(content)
            i += 1

        out.append(f"!!! {note_type}{title}")
        out.extend(f"    {note_line}" if note_line else "" for note_line in note_body)

    return "\n".join(out)


def main():
    project_root = Path(__file__).parents[2]

    for target_path, source_path in (
        ("contributing.md", "CONTRIBUTING.md"),
        ("index.md", "README.md"),
        ("examples.md", "docs/examples.md"),
    ):
        with mkdocs_gen_files.open(target_path, "w", encoding="utf-8", newline="\n") as f:
            content = (project_root / source_path).read_text(encoding="utf-8")
            for old_str, new_str in FILES_REPLACE_MAPPING.get(target_path, []):
                content = content.replace(old_str, new_str)
            f.write(gfm_to_mkdocs(content))


if __name__ in {"__main__", "<run_path>"}:
    main()
