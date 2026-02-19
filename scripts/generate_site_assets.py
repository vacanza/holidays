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

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed


sys.path.append(".")

import holidays
from holidays.ical import ICalExporter

# Configuration Defaults
DEFAULT_YEAR_START = 2015
DEFAULT_YEAR_END = 2035


def clean_output_dir(path):
    """Delete output directory if it exists and create it again"""
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def format_name(name):
    """Turn CamelCase strings into readable 'Camel Case' version"""
    return re.sub(r"(?<!^)(?=[A-Z])", " ", name)


def get_subdivision_name(instance, code):
    """Find the display name for a subdivision code (e.g., 'AL' -> 'Alabama')."""
    aliases = getattr(instance, "subdivisions_aliases", {})
    candidates = [name for name, target_code in aliases.items() if target_code == code]

    if not candidates:
        return code

    return max(candidates, key=len)


def get_canonical_name(instance):
    """Find the full country name by looking up the class hierarchy."""
    if hasattr(instance, "market"):
        return instance.market

    for cls in type(instance).__mro__:
        name = cls.__name__
        if name in ("HolidayBase", "DateHoliday", "Entity", "object"):
            continue
        if not name.isupper():
            return format_name(name)

    return format_name(type(instance).__name__)


def generate_json_content(holiday_obj):
    """Generate a sorted JSON string array of dates and names."""
    data = []
    for date_obj, name in sorted(holiday_obj.items()):
        data.append({"date": date_obj.isoformat(), "name": name})
    return json.dumps(data, ensure_ascii=False)


def write_assets(h_obj, filename_base, year_dir):
    """Write the ICS and JSON files to the disk."""
    if not h_obj:
        return
    try:

        exporter = ICalExporter(h_obj)
        ics_path = year_dir / f"{filename_base}.ics"
        exporter.save_ics(str(ics_path))

        json_data = generate_json_content(h_obj)
        with open(year_dir / f"{filename_base}.json", "w", encoding="utf-8") as f:
            f.write(json_data)
    except Exception as e:
        print(f"Error writing {filename_base}: {e}")


def process_entity(code, entity_type, output_dir, year_range):
    """Worker for Generates assets for a single Country/Market."""
    try:
        if entity_type == "countries":
            instance = holidays.country_holidays(code)
        else:
            instance = holidays.financial_holidays(code)
    except (NotImplementedError, KeyError):
        return None
    except Exception as e:
        print(f"Skipping {code}: Error instantiating ({e})")
        return None

    # Prepare metadata.
    name = get_canonical_name(instance)
    subdiv_codes = instance.subdivisions if instance.subdivisions else []
    languages = instance.supported_languages if instance.supported_languages else ["en"]
    categories = (
        instance.supported_categories if hasattr(instance, "supported_categories") else ["public"]
    )
    default_lang = getattr(instance, "default_language", "en")

    subdivisions_map = {}
    for sc in subdiv_codes:
        subdivisions_map[sc] = get_subdivision_name(instance, sc)

    manifest_entry = {
        "name": name,
        "subdivisions": subdivisions_map,
        "languages": sorted(list(languages)),
        "categories": sorted(list(categories)),
        "default_language": default_lang
    }

    print(f"Processing {code} ({name})...")

    # Generate files.
    for year in year_range:
        year_dir = output_dir / entity_type / code / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for lang in languages:
            for cat in categories:
                try:
                    if entity_type == "countries":
                        h_obj = holidays.country_holidays(code, years=year, language=lang, categories=[cat])
                    else:
                        h_obj = holidays.financial_holidays(code, years=year, language=lang, categories=[cat])
                    write_assets(h_obj, f"ALL_{lang}_{cat}", year_dir)
                except Exception:
                    pass

        if entity_type == "countries":
            for subdiv in subdiv_codes:
                for lang in languages:
                    for cat in categories:
                        try:
                            h_obj = holidays.country_holidays(
                                code, subdiv=subdiv, years=year, language=lang, categories=[cat]
                            )
                            if h_obj.subdiv == subdiv:
                                write_assets(h_obj, f"{subdiv}_{lang}_{cat}", year_dir)
                        except Exception:
                            pass

    return (entity_type, code, manifest_entry)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Generate small sample for local testing")
    parser.add_argument("--output", type=str, default="docs/downloads/ics", help="Output directory")
    parser.add_argument("--workers", type=int, default=None, help="Number of parallel worker processes")
    args = parser.parse_args()

    manifest = {"countries": {}, "financial": {}}
    work_items = []


    if args.dev:
        print("--- DEV MODE: Generating sample ---")
        output_dir = Path("docs/downloads/ics")
        clean_output_dir(output_dir)
        target_years = [2026,2027]
        target_countries = ["IN", "US", "AZ", "TD", "IT"]
        target_financial = ["XNYS", "XECB", "XBOM", "IFEU"]

        for code in target_financial:
            work_items.append((code, "financial"))

        for code in target_countries:
            work_items.append((code, "countries"))
    else:
        output_dir = Path(args.output)
        print(f"--- PROD MODE: Generating to {output_dir} ---")
        clean_output_dir(output_dir)
        target_years = range(DEFAULT_YEAR_START, DEFAULT_YEAR_END + 1)

        try:
            countries = holidays.list_supported_countries(include_aliases=False)
            for c in countries:
                work_items.append((c, "countries"))

            supported_financial = set(holidays.list_supported_financial(include_aliases=False))
            for m in supported_financial:
                work_items.append((m, "financial"))

            print(f"Found {len(work_items)} entities to process.")
        except Exception as e:
            print(f"Error listing entities: {e}")
            return


    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(process_entity, code, etype, output_dir, target_years): code
            for code, etype in work_items
        }

        for future in as_completed(futures):
            result = future.result()
            if result:
                etype, code, meta = result
                manifest[etype][code] = meta

    # Save Manifest
    manifest_path = output_dir / "index.json"
    print(f"Writing manifest to {manifest_path}...")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Done.")


if __name__ == "__main__":
    main()