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
import re
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.append(".")

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
    code, is_financial = args

    try:
        if not is_financial:
            instance = holidays.country_holidays(code)
        else:
            instance = holidays.financial_holidays(code)
    except (NotImplementedError, KeyError):
        return None
    except Exception as e:
        print(f"Skipping {code}: Error instantiating ({e})")
        return None

    # Prepare metadata
    cls = type(instance)
    entity_cls = cls.__base__ if cls.__name__.isupper() else cls
    name = re.sub(r"(?<!^)(?=[A-Z])", " ", entity_cls.__name__)
    languages = instance.supported_languages if instance.supported_languages else ["en_US"]
    categories = instance.supported_categories
    default_lang = getattr(instance, "default_language", "en_US")

    subdivision_aliases = instance.get_subdivision_aliases()
    subdivisions_map = {
        subdiv: subdivision_aliases[subdiv][0] if subdivision_aliases[subdiv] else subdiv
        for subdiv in instance.subdivisions
    }

    manifest_entry = {
        "name": name,
        "subdivisions": subdivisions_map,
        "languages": sorted(languages),
        "categories": sorted(categories),
        "default_language": default_lang,
    }

    print(f"Processing {code} ({name})...")

    entity_type = "financial" if is_financial else "countries"

    # Generate files
    for year in range(DEFAULT_YEAR_START, DEFAULT_YEAR_END + 1):
        year_dir = OUTPUT_DIR / entity_type / code / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for lang in languages:
            for cat in categories:
                try:
                    if not is_financial:
                        h_obj = holidays.country_holidays(code, years=year, language=lang, categories=[cat])
                    else:
                        h_obj = holidays.financial_holidays(code, years=year, language=lang, categories=[cat])
                    write_assets(h_obj, f"ALL_{lang}_{cat}", year_dir)
                except Exception as e:
                    print(f"Failed ALL_{lang}_{cat} for {code} {year}: {e}")

        if not is_financial:
            for subdiv in instance.subdivisions:
                for lang in languages:
                    for cat in categories:
                        try:
                            h_obj = holidays.country_holidays(
                                code, subdiv=subdiv, years=year, language=lang, categories=[cat]
                            )
                            if h_obj.subdiv == subdiv:
                                write_assets(h_obj, f"{subdiv}_{lang}_{cat}", year_dir)
                        except Exception as e:
                            print(f"Failed {subdiv}_{lang}_{cat} for {code} {year}: {e}")

    return (entity_type, code, manifest_entry)


def main():
    print(f"--- Generating to {OUTPUT_DIR} ---")
    
    # Inline output dir cleaning
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    
    work_items = [(c, False) for c in holidays.list_supported_countries(include_aliases=False)]
    work_items += [(m, True) for m in holidays.list_supported_financial(include_aliases=False)]

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