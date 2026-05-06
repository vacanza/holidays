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

sys.path.insert(0, str(Path.cwd()))  # Make holidays visible.

from holidays import (
    country_holidays,
    financial_holidays,
    list_supported_countries,
    list_supported_financial,
)
from holidays.ical import ICalExporter

# Configuration Defaults
DEFAULT_YEAR_START = 2015
DEFAULT_YEAR_END = 2035

OUTPUT_DIR = Path("site/downloads/ics")

LANGUAGES = {
    # --- Base Languages ---
    "am": "Amharic",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cnr": "Montenegrin",
    "cs": "Czech",
    "da": "Danish",
    "de": "German",
    "dz": "Dzongkha",
    "el": "Greek",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fil": "Filipino",
    "fo": "Faroese",
    "fr": "French",
    "fy": "Western Frisian",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "ht": "Haitian Creole",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "kl": "Kalaallisut (Greenlandic)",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "ky": "Kirghiz",
    "lb": "Luxembourgish",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mr": "Marathi",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pa": "Panjabi",
    "pl": "Polish",
    "ro": "Romanian",
    "ru": "Russian",
    "rw": "Kinyarwanda",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sq": "Albanian",
    "sr": "Serbian",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "tet": "Tetum",
    "tg": "Tajik",
    "th": "Thai",
    "tk": "Turkmen",
    "tkl": "Tokelauan",
    "to": "Tongan",
    "tr": "Turkish",
    "tvl": "Tuvaluan",
    "uk": "Ukrainian",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    # --- Arabic Locales ---
    "ar_EG": "Arabic (Egypt)",
    "ar_QA": "Arabic (Qatar)",
    "ar_SD": "Arabic (Sudan)",
    # --- Cocos Islands ---
    "coa_CC": "Cocos Islands Malay",
    # --- English Locales ---
    "en_AI": "English (Anguilla)",
    "en_AU": "English (Australia)",
    "en_BF": "English (Burkina Faso)",
    "en_BM": "English (Bermuda)",
    "en_BQ": "English (Bonaire, Sint Eustatius and Saba)",
    "en_CA": "English (Canada)",
    "en_CC": "English (Cocos Islands)",
    "en_CI": "English (Ivory Coast)",
    "en_CK": "English (Cook Islands)",
    "en_CX": "English (Christmas Island)",
    "en_CY": "English (Cyprus)",
    "en_ET": "English (Ethiopia)",
    "en_FM": "English (Micronesia)",
    "en_GB": "English (United Kingdom)",
    "en_GD": "English (Grenada)",
    "en_GM": "English (Gambia)",
    "en_GS": "English (South Georgia & South Sandwich Islands)",
    "en_GY": "English (Guyana)",
    "en_HK": "English (Hong Kong)",
    "en_IN": "English (India)",
    "en_KE": "English (Kenya)",
    "en_LC": "English (Saint Lucia)",
    "en_MO": "English (Macau)",
    "en_MS": "English (Montserrat)",
    "en_MU": "English (Mauritius)",
    "en_NA": "English (Namibia)",
    "en_NF": "English (Norfolk Island)",
    "en_NG": "English (Nigeria)",
    "en_NR": "English (Nauru)",
    "en_NU": "English (Niue)",
    "en_PH": "English (Philippines)",
    "en_PK": "English (Pakistan)",
    "en_SC": "English (Seychelles)",
    "en_SG": "English (Singapore)",
    "en_SL": "English (Sierra Leone)",
    "en_TC": "English (Turks and Caicos Islands)",
    "en_TK": "English (Tokelau)",
    "en_TL": "English (Timor-Leste)",
    "en_TT": "English (Trinidad and Tobago)",
    "en_US": "English (United States)",
    "en_VC": "English (Saint Vincent and the Grenadines)",
    "en_VG": "English (British Virgin Islands)",
    # --- Persian / Pashto Locales ---
    "fa_AF": "Persian (Afghanistan)",
    "fa_IR": "Persian (Iran)",
    "ps_AF": "Pashto (Afghanistan)",
    # --- French Locales ---
    "fr_BI": "French (Burundi)",
    "fr_BJ": "French (Benin)",
    "fr_HT": "French (Haiti)",
    "fr_NE": "French (Niger)",
    "fr_SN": "French (Senegal)",
    # --- Italian Locales ---
    "it_IT": "Italian (Italy)",
    # --- Korean Locales ---
    "ko_KP": "Korean (North Korea)",
    # --- Malay Locales ---
    "ms_MY": "Malay (Malaysia)",
    # --- Papiamento Locales ---
    "pap_AW": "Papiamento (Aruba)",
    "pap_BQ": "Papiamento (Bonaire, Sint Eustatius and Saba)",
    "pap_CW": "Papiamento (Curaçao)",
    # --- Portuguese Locales ---
    "pt_AO": "Portuguese (Angola)",
    "pt_BR": "Portuguese (Brazil)",
    "pt_CV": "Portuguese (Cabo Verde)",
    "pt_GW": "Portuguese (Guinea-Bissau)",
    "pt_MO": "Portuguese (Macau)",
    "pt_MZ": "Portuguese (Mozambique)",
    "pt_PT": "Portuguese (Portugal)",
    "pt_ST": "Portuguese (Sao Tome and Principe)",
    "pt_TL": "Portuguese (Timor Leste)",
    # --- Russian Locales ---
    "ru_KG": "Russian (Kyrgyzstan)",
    # --- Sinhala / Tamil Locales ---
    "si_LK": "Sinhala (Sri Lanka)",
    "ta_LK": "Tamil (Sri Lanka)",
    # --- Swedish Locales ---
    "sv_FI": "Swedish (Finland)",
    # --- Urdu Locales ---
    "ur_PK": "Urdu (Pakistan)",
    # --- Chinese Locales ---
    "zh_CN": "Chinese (Simplified)",
    "zh_HK": "Chinese (Hong Kong)",
    "zh_MO": "Chinese (Macau)",
    "zh_TW": "Chinese (Traditional)",
}


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

    holidays_func = country_holidays if is_country else financial_holidays
    instance = holidays_func(code)

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

    # Generate files
    for year in range(DEFAULT_YEAR_START, DEFAULT_YEAR_END + 1):
        year_dir = OUTPUT_DIR / entity_type / code / str(year)
        year_dir.mkdir(parents=True, exist_ok=True)

        for subdiv in (None, *instance.subdivisions):
            for lang in languages:
                for cat in categories:
                    filename = f"{subdiv or 'ALL'}_{lang}_{cat}"
                    try:
                        h_obj = holidays_func(
                            code, subdiv=subdiv, years=year, language=lang, categories=cat
                        )
                        write_assets(h_obj, filename, year_dir)
                    except Exception as e:
                        print(f"Failed {filename} for {code} {year}: {e}")

    return entity_type, code, manifest_entry


def main():
    print(f"--- Generating to {OUTPUT_DIR} ---")

    # Inline output dir cleaning
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    work_items = [(c, True) for c in list_supported_countries(include_aliases=False)]
    work_items += [(m, False) for m in list_supported_financial(include_aliases=False)]

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
