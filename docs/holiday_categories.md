# Holiday Categories

The holidays library supports various categories of holidays to help classify different types of observances. This allows users to filter holidays based on their official status, religious significance, or cultural importance.

## Overview

Holiday categories enable you to filter holidays based on their nature and official recognition. Each country defines which categories it supports, and holidays are classified accordingly.

## Category Types

### Official Status Categories

**PUBLIC**
Official holidays recognized by the government that typically provide time off from work and school for the general population.

Examples:
- New Year's Day in most countries
- Independence Day in the United States
- Christmas Day in Christian-majority countries

**GOVERNMENT**
Holidays observed by government institutions but may not provide general time off for all workers.

Examples:
- Flag Day in some jurisdictions
- Government-specific commemorative days

**WORKDAY**
Holidays that are officially recognized but do not provide time off from work. Often ceremonial or commemorative in nature.

Examples:
- Constitution Day in some countries
- Memorial days that are observed but not as public holidays

**UNOFFICIAL**
Commonly celebrated cultural holidays with no official government recognition or mandated time off.

Examples:
- Valentine's Day
- Saint Patrick's Day  
- Halloween

### Institutional Categories

**BANK**
Holidays specifically observed by banking institutions, which may differ from general public holidays.

Examples:
- Good Friday (in some countries)
- Additional banking-specific closures

**SCHOOL**
Holidays specific to educational institutions.

Examples:
- Teacher's Day
- Education-specific observances

**ARMED_FORCES**
Holidays specific to military personnel and institutions.

Examples:
- Armed Forces Day
- Military commemoration days

### Special Categories

**OPTIONAL**
Holidays that individuals or organizations may choose to observe, often with flexibility in implementation.

Examples:
- Religious holidays for minority populations
- Cultural observances with optional recognition

**MANDATORY**
Holidays that must be observed by law in specific contexts.

**HALF_DAY**
Holidays that are observed for only part of the day.

Examples:
- Christmas Eve (afternoon only)
- New Year's Eve (afternoon only)

### Religious Categories

**CATHOLIC**
Holidays specific to the Catholic Christian tradition.

Examples:
- Feast of the Immaculate Conception
- Corpus Christi

**CHRISTIAN**
General Christian holidays observed across denominations.

Examples:
- Easter Sunday
- Christmas Day

**ORTHODOX**
Holidays specific to Orthodox Christian traditions.

Examples:
- Orthodox Easter
- Orthodox Christmas

**ISLAMIC**
Holidays from the Islamic tradition.

Examples:
- Eid al-Fitr
- Eid al-Adha

**HINDU**
Holidays from the Hindu tradition.

Examples:
- Diwali
- Holi

**HEBREW**
Holidays from the Jewish tradition.

Examples:
- Yom Kippur
- Passover

**CHINESE**
Holidays from Chinese cultural and religious traditions.

Examples:
- Chinese New Year
- Mid-Autumn Festival

**SABIAN**
Holidays specific to the Sabian religious tradition.

**YAZIDI**
Holidays specific to the Yazidi religious tradition.

### Ethnic and Cultural Categories

**ARMENIAN**
Holidays specific to Armenian culture and traditions.

**ALBANIAN**
Holidays specific to Albanian culture and traditions.

**BOSNIAN**
Holidays specific to Bosnian culture and traditions.

**SERBIAN**
Holidays specific to Serbian culture and traditions.

**TURKISH**
Holidays specific to Turkish culture and traditions.

**ROMA**
Holidays specific to Roma culture and traditions.

**VLACH**
Holidays specific to Vlach culture and traditions.

## Usage Examples

### Filtering by Single Category

Get only public holidays:

```python
import holidays

# Get only public holidays for the United States
us_public = holidays.UnitedStates(categories='public', years=2024)
print(f"US public holidays in 2024: {len(us_public)}")
```

### Filtering by Multiple Categories

Get holidays from multiple categories:

```python
import holidays

# Get both public and bank holidays for Belgium
belgium_holidays = holidays.Belgium(categories=('public', 'bank'), years=2024)
for date, name in sorted(belgium_holidays.items()):
    print(f"{date}: {name}")
```

### Religious Category Example

```python
import holidays

# Get only Catholic holidays in Germany
germany_catholic = holidays.Germany(categories='catholic', years=2024)
for date, name in sorted(germany_catholic.items()):
    print(f"{date}: {name}")
```

### Unofficial Holidays Example

```python
import holidays

# Get unofficial holidays in the United States
us_unofficial = holidays.UnitedStates(categories='unofficial', years=2024)
for date, name in sorted(us_unofficial.items()):
    print(f"{date}: {name}")
# Output: Valentine's Day, Saint Patrick's Day, Halloween, etc.
```

## Country-Specific Support

Not all countries support all categories. Each country defines its own supported categories based on its legal and cultural framework.

### Checking Supported Categories

```python
import holidays

# Check which categories a country supports
us = holidays.UnitedStates()
print(f"US supported categories: {us.supported_categories}")
# Output: ('government', 'public', 'unofficial')

de = holidays.Germany()
print(f"Germany supported categories: {de.supported_categories}")
# Output: ('catholic', 'public')
```

### Examples by Country

**United States**: `('government', 'public', 'unofficial')`
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
- **GOVERNMENT**: Official observances without general time off
- **WORKDAY**: Recognized but working holidays
- **UNOFFICIAL**: Widely celebrated but not official
- **Religious categories**: Use specific tradition names when holidays apply to particular communities
- **Institutional categories**: Use when holidays apply to specific sectors

## Default Behavior

When no categories are specified, most countries default to returning PUBLIC holidays, as these are typically what users expect when asking for a country's holidays.

```python
import holidays

# These are equivalent for most countries
us_default = holidays.UnitedStates(years=2024)
us_public = holidays.UnitedStates(categories='public', years=2024)
```

## Contributing

When contributing new countries or updating existing ones:

1. Research the official holiday framework for the country
2. Identify which categories are appropriate
3. Classify each holiday according to its official status and cultural significance
4. Document the reasoning for category assignments
5. Provide examples in tests demonstrating category usage
