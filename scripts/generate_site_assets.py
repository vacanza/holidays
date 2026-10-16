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

import html
import json
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path.cwd()))  # Make holidays visible.

from holidays import (
    HolidayBase,
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

HTML_INDEX_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Holiday Calendar Downloads</title>
<style>
body { font-family: system-ui, sans-serif; margin: 2rem auto;
       padding: 0 1rem; max-width: 1400px; color: #222; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ddd; padding: .65rem; text-align: left; }
th { background: #f3f3f3; }
tbody tr:nth-child(even) { background: #fafafa; }
a { margin-right: .35rem; }
input { padding: .6rem; margin: 1rem 0; max-width: 100%; width: 24rem; }
button { font: inherit; border: 0; background: none; cursor: pointer; }
</style>
</head>
<body>
<h1>Holiday Calendar Downloads</h1>
<p>Browse available holiday calendars. Download ICS or JSON files,
or use Webcal to subscribe in a compatible calendar application.</p>
<div id="controls"></div>
<table id="calendars">
<thead><tr>
<th>Country / Market</th><th>Type</th><th>Subdivision</th>
<th>Language</th><th>Category</th><th>Available formats</th>
</tr></thead>
<tbody>
"""

HTML_INDEX_FOOTER = """
</tbody>
</table>
<script>
const table = document.getElementById("calendars");
const body = table.tBodies[0];
const controls = document.getElementById("controls");
const search = document.createElement("input");
search.type = "search";
search.placeholder = "Search countries, languages, or categories";
search.setAttribute("aria-label", "Search holiday calendars");
controls.appendChild(search);

search.addEventListener("input", () => {
    const query = search.value.toLocaleLowerCase();
    for (const row of body.rows) {
        row.hidden = !row.textContent.toLocaleLowerCase().includes(query);
    }
});

let sortColumn = 0;
let sortAscending = true;

for (const [index, heading] of [...table.tHead.rows[0].cells].entries()) {
    if (index === 5) continue;

    const label = heading.textContent.trim();
    const button = document.createElement("button");
    button.dataset.label = label;
    button.setAttribute("aria-label", "Sort by " + label);

    const updateButton = () => {
        if (sortColumn === index) {
            button.textContent = label + (sortAscending ? " ↑" : " ↓");
            button.setAttribute(
                "aria-label",
                "Sort by " + label + ", currently " +
                    (sortAscending ? "ascending" : "descending")
            );
            heading.setAttribute(
                "aria-sort",
                sortAscending ? "ascending" : "descending"
            );
        } else {
            button.textContent = label + " ↕";
            button.setAttribute("aria-label", "Sort by " + label);
            heading.setAttribute("aria-sort", "none");
        }
    };

    updateButton();
    heading.replaceChildren(button);

    button.addEventListener("click", () => {
        if (sortColumn === index) {
            sortAscending = !sortAscending;
        } else {
            sortColumn = index;
            sortAscending = true;
        }

        for (const otherHeading of table.tHead.rows[0].cells) {
            const otherButton = otherHeading.querySelector("button");
            if (!otherButton) continue;

            if (otherHeading === heading) {
                updateButton();
                continue;
            }

            const otherLabel = otherButton.dataset.label;
            otherButton.textContent = otherLabel + " ↕";
            otherButton.setAttribute("aria-label", "Sort by " + otherLabel);
            otherHeading.setAttribute("aria-sort", "none");
        }


        const rows = [...body.rows];
        rows.sort((a, b) => {
            const result = a.cells[index].textContent.localeCompare(
                b.cells[index].textContent,
                undefined,
                { numeric: true, sensitivity: "base" }
            );
            return sortAscending ? result : -result;
        });
        body.append(...rows);
    });
}
</script>
</body>
</html>
"""


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
    "dv": "Dhivehi",
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
    "kab": "Kabyle",
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
    "en_BD": "English (Bangladesh)",
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
    "fr_MC": "French (Monaco)",
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


def write_assets(h_obj: HolidayBase, filename_base: str, out_dir: Path) -> None:
    """Write the ICS and JSON files to the disk."""
    if not h_obj:
        return

    try:
        ICalExporter(h_obj).save_ics(out_dir / f"{filename_base}.ics")

        # Inline JSON generation.
        json_data = json.dumps(
            [{"date": dt.isoformat(), "name": name} for dt, name in sorted(h_obj.items())],
            ensure_ascii=False,
        )
        (out_dir / f"{filename_base}.json").write_text(json_data, encoding="utf-8", newline="\n")
    except Exception as e:
        print(f"Error writing {filename_base}: {e}")


def process_entity(args) -> tuple[str, str, dict]:
    """Worker that generates assets for a single Country/Market."""
    code, is_country = args

    holidays_func = country_holidays if is_country else financial_holidays
    instance = holidays_func(code)

    # Prepare metadata.
    docstring = instance.__class__.__base__.__doc__ or ""
    name = docstring.split("\n")[0].split("holidays")[0].strip()
    languages = instance.supported_languages or ["en_US"]
    categories = instance.supported_categories
    default_lang = getattr(instance, "default_language", None) or "en_US"

    subdivision_aliases = instance.get_subdivision_aliases()
    subdivisions_map = {
        subdiv: subdivision_aliases[subdiv][0] if subdivision_aliases[subdiv] else subdiv
        for subdiv in instance.subdivisions
    }

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

    out_dir = OUTPUT_DIR / entity_type / code
    out_dir.mkdir(parents=True, exist_ok=True)
    for subdiv in (None, *instance.subdivisions):
        for language in languages:
            for category in categories:
                filename = f"{subdiv or 'ALL'}_{language}_{category}"
                try:
                    h_obj = holidays_func(
                        code,
                        subdiv=subdiv,
                        years=range(DEFAULT_YEAR_START, DEFAULT_YEAR_END + 1),
                        language=language,
                        categories=category,
                    )
                    write_assets(h_obj, filename, out_dir)
                except Exception as e:
                    print(f"Failed {filename} for {code}: {e}")

    return entity_type, code, manifest_entry


def generate_html_index(manifest: dict[str, dict], output_dir: Path = OUTPUT_DIR) -> None:
    """Generate a static HTML index for available calendar artifacts."""
    rows = []

    for entity_type, entities in manifest.items():
        for code, metadata in entities.items():
            entity_name = metadata["name"]
            subdivisions = [("ALL", "Nationwide"), *metadata["subdivisions"].items()]

            for subdiv_code, subdiv_name in subdivisions:
                for language, language_name in metadata["languages"].items():
                    for category in metadata["categories"]:
                        filename = f"{subdiv_code}_{language}_{category}"
                        relative_path = (Path(entity_type) / code / filename).as_posix()
                        ics_path = output_dir / f"{relative_path}.ics"
                        json_path = output_dir / f"{relative_path}.json"

                        if not ics_path.is_file() and not json_path.is_file():
                            continue

                        links = []
                        if ics_path.is_file():
                            href = html.escape(f"{relative_path}.ics", quote=True)
                            webcal = html.escape(
                                f"webcal://vacanza.github.io/holidays/"
                                f"downloads/ics/{relative_path}.ics",
                                quote=True,
                            )
                            links.append(f'<a href="{href}" download>ICS</a>')
                            links.append(f'<a href="{webcal}">Webcal</a>')

                        if json_path.is_file():
                            href = html.escape(f"{relative_path}.json", quote=True)
                            links.append(f'<a href="{href}" download>JSON</a>')

                        rows.append(
                            (
                                entity_name.casefold(),
                                subdiv_name.casefold(),
                                language_name.casefold(),
                                category.casefold(),
                                f"""<tr>
<td>{html.escape(entity_name)} ({html.escape(code)})</td>
<td>{html.escape(entity_type)}</td>
<td>{html.escape(subdiv_name)}</td>
<td>{html.escape(language_name)} ({html.escape(language)})</td>
<td>{html.escape(category)}</td>
<td>{" | ".join(links)}</td>
</tr>""",
                            )
                        )

    rows.sort(key=lambda row: row[:4])

    document = (
    HTML_INDEX_HEADER
    + "\n".join(row[4] for row in rows)
    + HTML_INDEX_FOOTER
)

    index_path = output_dir / "index.html"
    index_path.write_text(document, encoding="utf-8", newline="\n")
    print(f"Wrote HTML index to {index_path}")


def main() -> None:
    print(f"--- Generating to {OUTPUT_DIR} ---")
    po_time_start = perf_counter()

    # Inline output dir cleaning.
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    work_items = [(c, True) for c in list_supported_countries(include_aliases=False)]
    work_items += [(m, False) for m in list_supported_financial(include_aliases=False)]

    print(f"Found {len(work_items)} entities to process.")
    manifest: dict[str, dict] = {"countries": {}, "financial": {}}

    with ProcessPoolExecutor() as executor:
        for result in executor.map(process_entity, work_items):
            if result:
                etype, code, meta = result
                manifest[etype][code] = meta

    po_time_end = perf_counter()
    print(f"[TIMER] Total generating runtime: {po_time_end - po_time_start:.2f} seconds")

    manifest_path = OUTPUT_DIR / "index.json"

    print(f"Writing manifest to {manifest_path}...")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
    )
    generate_html_index(manifest)

    print("Done.")


if __name__ == "__main__":
    main()
