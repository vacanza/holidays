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

import json
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.append(".")

from language_registry import LANGUAGES

import holidays
from holidays.ical import ICalExporter

# Configuration Defaults
DEFAULT_YEAR_START = 2015
DEFAULT_YEAR_END = 2035
OUTPUT_DIR = Path("docs/downloads/ics")


def write_assets(h_obj, filename_base, year_dir):
    """Write the ICS and JSON files to the disk."""
    if not h_obj:
        return
    try:
        exporter = ICalExporter(h_obj)
        ics_path = year_dir / f"{filename_base}.ics"
        exporter.save_ics(str(ics_path))

        # Inline JSON generation
        json_data = json.dumps(
            [{"date": dt.isoformat(), "name": name} for dt, name in sorted(h_obj.items())],
            ensure_ascii=False,
        )
        (year_dir / f"{filename_base}.json").write_text(json_data, encoding="utf-8", newline="\n")
    except Exception as e:
        print(f"Error writing {filename_base}: {e}")


def process_entity(args):
    """Worker that generates assets for a single Country/Market."""
    code, is_country = args

    try:
        if is_country:
            instance = holidays.country_holidays(code)
        else:
            instance = holidays.financial_holidays(code)
    except (NotImplementedError, KeyError):
        return None
    except Exception as e:
        print(f"Skipping {code}: Error instantiating ({e})")
        return None

    # Prepare metadata.
    docstring = instance.__class__.__base__.__doc__
    name = docstring.split("\n")[0].split("holidays")[0].strip()
    languages = instance.supported_languages or ["en_US"]
    categories = instance.supported_categories
    default_lang = getattr(instance, "default_language", None) or "en_US"

    subdivision_aliases = instance.get_subdivision_aliases()
    subdivisions_map = {
        subdiv: subdivision_aliases[subdiv][0] if subdivision_aliases[subdiv] else subdiv
        for subdiv in instance.subdivisions
    }

    # Generate a clean dictionary of full language names
    languages_map = {lang: LANGUAGES.get(lang, lang) for lang in sorted(languages)}

    manifest_entry = {
        "name": name,
        "subdivisions": subdivisions_map,
        "languages": languages_map,
        "categories": sorted(categories),
        "default_language": default_lang,
    }

    print(f"Processing {code} ({name})...")

    entity_type = "countries" if is_country else "financial"
    holidays_func = holidays.country_holidays if is_country else holidays.financial_holidays

    # Generate files
    for year in range(DEFAULT_YEAR_START, DEFAULT_YEAR_END + 1):
        year_dir = OUTPUT_DIR / entity_type / code / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for subdiv in (None, *instance.subdivisions):
            for lang in languages:
                for cat in categories:
                    filename = f"{subdiv or 'ALL'}_{lang}_{cat}"
                    try:
                        if is_country:
                            h_obj = holidays_func(
                                code, subdiv=subdiv, years=year, language=lang, categories=cat
                            )
                        else:
                            h_obj = holidays_func(code, years=year, language=lang, categories=cat)
                        write_assets(h_obj, filename, year_dir)
                    except Exception as e:
                        print(f"Failed {filename} for {code} {year}: {e}")

    return (entity_type, code, manifest_entry)


def main():
    print(f"--- Generating to {OUTPUT_DIR} ---")

    # Inline output dir cleaning
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    work_items = [(c, True) for c in holidays.list_supported_countries(include_aliases=False)]
    work_items += [(m, False) for m in holidays.list_supported_financial(include_aliases=False)]

    print(f"Found {len(work_items)} entities to process.")
    manifest = {"countries": {}, "financial": {}}

    with ProcessPoolExecutor() as executor:
        for result in executor.map(process_entity, work_items):
            if result:
                etype, code, meta = result
                manifest[etype][code] = meta

    manifest_path = OUTPUT_DIR / "index.json"
    print(f"Writing manifest to {manifest_path}...")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
    )

    print("Done.")


if __name__ == "__main__":
    main()
