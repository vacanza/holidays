# Holiday Categories

The framework offers multiple holiday categories to classify different types of observances, enabling users to filter holidays by official status, religious significance, or cultural importance.

## Overview

Holiday categories enable you to filter holidays based on their nature and official recognition. Each country defines which categories it supports, and holidays are classified accordingly.

## Category Types

### Official Status Categories

#### PUBLIC

Official holidays recognized by the government that typically provide time off from work and school for the general population.

Examples:

- New Year's Day in most countries
- Independence Day in the United States
- Christmas Day in Christian-majority countries

#### GOVERNMENT

Holidays observed by government institutions but may not provide general time off for all workers.

Examples:

- Flag Day in some jurisdictions
- Government-designated commemorative days

#### WORKDAY

Holidays that are officially recognized but do not provide time off from work. Often ceremonial or commemorative in nature.

Examples:

- Constitution Day in some countries
- Memorial days that are observed but not as public holidays

#### UNOFFICIAL

Commonly celebrated cultural holidays with no official government recognition or mandated time off. These are widely observed cultural celebrations, but exclude novelty, internet, or marketing "national days".

Examples:

- Halloween
- Saint Patrick's Day
- Valentine's Day

### Institutional Categories

#### BANK

Holidays specifically observed by banking institutions, which may differ from general public holidays.

Examples:

- Additional bank-specific closures
- Good Friday (in some countries)

#### SCHOOL

Holidays specific to educational institutions.

Examples:

- Education-related observances
- Teacher's Day

#### ARMED_FORCES

Holidays specific to military personnel and institutions.

Examples:

- Armed Forces Day
- Military commemoration days

### Special Categories

#### OPTIONAL

Optional holidays that individuals or organizations may observe, often with flexible implementation.

Examples:

- Cultural observances with optional recognition
- Religious holidays for minority populations

#### MANDATORY *(deprecated)*

Holidays that were legally required to be observed in specific contexts. Previously used in Macau, where "Mandatory (Statutory) Holidays" have since been reclassified under the `PUBLIC` category, and "General Holidays" are now included in the `OPTIONAL` category, following the same approach as in Hong Kong.

#### HALF_DAY

Holidays observed for only part of a day, typically resulting in reduced working hours rather than a full day off.

Examples:

- Christmas Eve (afternoon only)
- New Year's Eve (afternoon only)

#### DE_FACTO

Holidays that are legally treated equivalently to public holidays for specific purposes (such as working day calculations) but are not officially designated as public holidays. These observances have legal backing that grants them similar status to public holidays in certain contexts.

Examples:

- **Sweden**: Midsummer Eve (Midsommarafton), Christmas Eve (Julafton), and New Year's Eve (Nyårsafton) - per [Semesterlag (SFS 1977:480)](https://web.archive.org/web/20260106114757/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/semesterlag-1977480_sfs-1977-480/), these are treated equivalently to Sundays and public holidays for working day calculations, though they are not official public holidays.
- **Switzerland**: Easter Sunday (Ostersonntag), Whit Sunday (Pfingstsonntag), and Federal Day of Thanksgiving, Repentance, and Prayer (Eidgenössischer Bettag) - per Zürich's [Ruhetags- und Ladenöffnungsgesetz vom 26. Juni 2000](https://web.archive.org/web/20260421063821/https://www.notes.zh.ch/appl/zhlex_r.nsf/WebView/C1256C610039641BC12569990033674B/$File/822.4.pdf).

Usage:

```python
import holidays
from holidays.constants import PUBLIC, DE_FACTO

# For accurate is_working_day() behavior in Sweden.
se = holidays.Sweden(categories=(PUBLIC, DE_FACTO), years=2024)
print(se.is_working_day('2024-12-24'))  # False (Christmas Eve)
```

### Religious Categories

#### CATHOLIC

Holidays specific to the Catholic Christian tradition.

Examples:

- Corpus Christi
- Feast of the Immaculate Conception

#### PROTESTANT

Holidays specific to the Protestant Christian tradition.

Examples:

- In Austria (1956-2018), Good Friday was treated as a public holiday for members of the Evangelical Churches of the Augsburg and Helvetic Confessions, the Methodist Church, and the Old Catholic Church (the special provision was removed via [BGBl. I Nr. 22/2019](https://web.archive.org/web/20260408111719/https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2019_I_22/BGBLA_2019_I_22.pdf)).

#### CHRISTIAN

General Christian holidays observed by multiple denominations.

Examples:

- Christmas Day
- Easter Sunday

#### ORTHODOX

Holidays specific to the Orthodox Christian tradition.

Examples:

- Orthodox Christmas
- Orthodox Easter

#### ISLAMIC

Holidays specific to the Islamic tradition.

Examples:

- Eid al-Adha
- Eid al-Fitr

#### HINDU

Holidays specific to the Hindu tradition.

Examples:

- Diwali
- Holi

#### HEBREW

Holidays specific to the Jewish tradition.

Examples:

- Passover
- Yom Kippur

#### SABIAN

Holidays specific to the Sabian religious tradition.

Examples:

- Used in Iraq for Sabian community holidays

#### YAZIDI

Holidays specific to the Yazidi religious tradition.

Examples:

- Used in Iraq for Yazidi community holidays

### Ethnic and Cultural Categories

#### ARMENIAN

Holidays specific to Armenian culture and traditions.

Examples:

- Used in Argentina for Armenian community holidays

#### ALBANIAN

Holidays specific to Albanian culture and traditions.

Examples:

- Used in North Macedonia for Albanian community holidays

#### BOSNIAN

Holidays specific to Bosnian culture and traditions.

Examples:

- Used in North Macedonia for Bosnian community holidays

#### SERBIAN

Holidays specific to Serbian culture and traditions.

Examples:

- Used in North Macedonia for Serbian community holidays

#### TURKISH

Holidays specific to Turkish culture and traditions.

Examples:

- Used in North Macedonia for Turkish community holidays

#### ROMA

Holidays specific to Roma culture and traditions.

Examples:

- Used in North Macedonia for Roma community holidays

#### VLACH

Holidays specific to Vlach culture and traditions.

Examples:

- Used in North Macedonia for Vlach community holidays

## Usage Examples

### Filtering by Single Category

Get only public holidays for the United States:

```python
import holidays
from holidays.constants import PUBLIC

us_public = holidays.UnitedStates(categories=PUBLIC, years=2024)
print(f"US public holidays in 2024: {len(us_public)}")
```

### Filtering by Multiple Categories

Get both public and bank holidays for Belgium:

```python
import holidays
from holidays.constants import PUBLIC, BANK

belgium_holidays = holidays.Belgium(categories=(PUBLIC, BANK), years=2024)
for date, name in sorted(belgium_holidays.items()):
    print(f"{date}: {name}")
```

### Religious Category Example

Get only Catholic holidays in Germany (Saxony subdivision):

```python
import holidays
from holidays.constants import CATHOLIC

germany_catholic = holidays.Germany(subdiv='SN', categories=CATHOLIC, years=2024)
for date, name in sorted(germany_catholic.items()):
    print(f"{date}: {name}")
```

### Unofficial Holidays Example

Get unofficial holidays in the United States:

```python
import holidays
from holidays.constants import UNOFFICIAL

us_unofficial = holidays.UnitedStates(categories=UNOFFICIAL, years=2024)
for date, name in sorted(us_unofficial.items()):
    print(f"{date}: {name}")
```

## Country-Specific Support

Not all countries support every category. Each country defines the categories it recognizes based on its legal and cultural framework.

### Checking Supported Categories

Check which categories a country supports:

```python
import holidays

print(f"US supported categories: {holidays.UnitedStates.supported_categories}")

print(f"Germany supported categories: {holidays.Germany.supported_categories}")
```

The returned categories are lowercase strings corresponding to the constants in `holidays.constants`.

### Examples by Country

**United States**: `('government', 'half_day', 'public', 'unofficial')`

- Supports federal holidays, state holidays, and cultural observances

**Germany**: `('catholic', 'public')`

- Supports public holidays and Catholic religious holidays in certain regions

**India**: `('optional', 'public')`

- Supports national holidays and optional regional observances

**Argentina**: `('armenian', 'bank', 'government', 'hebrew', 'islamic', 'public')`

- Supports multiple religious traditions and institutional categories

## Implementation Guidelines

### When Defining New Countries

When adding support for a new country, consider:

1. **Official Status**: Which holidays are legally mandated public holidays?
2. **Religious Diversity**: What religious communities have recognized holidays?
3. **Cultural Significance**: Are there widely celebrated unofficial holidays?
4. **Institutional Needs**: Do banks, schools, or government have specific observances?

### Category Selection Principles

- **PUBLIC**: Holidays mandated by law with general time off
- **GOVERNMENT**: Holidays observed by government institutions but may not provide general time off for all workers
- **WORKDAY**: Recognized but are working holidays
- **UNOFFICIAL**: Widely celebrated but not official
- **DE_FACTO**: Legally recognized holidays that must be treated like public holidays for specific purposes (e.g., working day calculations) but lack official public holiday status
- **Religious categories**: Use when holidays apply to particular religious communities
- **Institutional categories**: Use when holidays apply to specific sectors

## Default Behavior

When no categories are specified, all countries and markets default to returning PUBLIC holidays, as these are typically what users expect when asking for a country's holidays.

```python
import holidays
from holidays.constants import PUBLIC

# These are equivalent for all countries and markets.
us_default = holidays.UnitedStates(years=2024)
us_public = holidays.UnitedStates(categories=PUBLIC, years=2024)
```

## Contributing

When contributing new countries or updating existing ones:

1. Research the official holiday framework for the country
2. Identify which categories are appropriate
3. Classify each holiday according to its official status and cultural significance
4. Document the reasoning for category assignments
5. Provide examples in tests demonstrating category usage
