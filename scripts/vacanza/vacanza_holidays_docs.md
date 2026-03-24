# Vacanza Holidays Calendar Generator

`vacanza_holidays.py` is a command-line utility that automates the generation of `.ics` (iCalendar) files for holidays worldwide. It uses the Python `holidays` library to look up dates and supports exporting them based on specific years, languages, and holiday categories.

## Prerequisites

Ensure you have the required dependencies installed:
```bash
pip install holidays
```

## Basic Usage

The basic syntax for running the script is:
```bash
python vacanza_holidays.py [COUNTRY_CODE] [YEAR_OR_RANGE] [OPTIONS]
```

### Positional Arguments
- **`country`**: The country code you want to generate holidays for (e.g., `US`, `GB`, `SE`, `NG`).
- **`year`**: (Optional) The year (`2025`) or range of years (`2020-2025`) to generate calendars for. If omitted, it defaults to `2026`.

### Options
- `-h`, `--help`: Show the help message and exit.
- `-l LANGUAGE`, `--language LANGUAGE`: Filter by language code (e.g., `en`, `sv`, `de`). Must be supported by the specific country's holiday registry.
- `-c CATEGORY`, `--category CATEGORY`: Filter by holiday category (e.g., `public`, `government`, `half_day`, `school`). If not specified, calendars for all supported categories will be generated.
- `-o OUTPUT_DIR`, `--output-dir OUTPUT_DIR`: Specify a directory to save the generated `.ics` files. Defaults to the current working directory.
- `--list-countries`: List all supported countries and their corresponding country codes, then exit.

---

## Examples

**1. Generate all holiday calendars for a country (Default Year: 2026)**
```bash
python vacanza_holidays.py US
```
*Generates `.ics` files for all available categories (e.g., public, government, unofficial) for the United States in the year 2026.*

**2. Generate holidays for a specific year**
```bash
python vacanza_holidays.py US 2025
```

**3. Generate holidays for a range of years**
```bash
python vacanza_holidays.py SE 2025-2030
```

**4. Filter by a specific category**
If you only want public holidays for a country:
```bash
python vacanza_holidays.py GB 2025 --category public
```
*Tip: You can use `--category` to isolate specific groupings like `bank`, `school`, or `optional` depending on what the country supports.*

**5. Specify an output directory**
To keep your workspace clean, save the generated `.ics` files into a specific folder:
```bash
python vacanza_holidays.py NG 2025-2026 -o ./my_calendars/
```

**6. List all supported countries**
If you don't know the code for a country, list them all to find it:
```bash
python vacanza_holidays.py --list-countries
```

## Output Format
The generated files follow this naming convention:
`[COUNTRY]_[YEARS]_[CATEGORY]_[LANGUAGE].ics`

For example, generating all US calendars for 2025 will output:
- `US_2025-2025_government.ics`
- `US_2025-2025_half_day.ics`
- `US_2025-2025_public.ics`
- `US_2025-2025_unofficial.ics`
