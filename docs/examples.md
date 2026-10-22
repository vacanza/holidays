# Additional Examples

## Simplest example possible

```pycon
>>> from datetime import date
>>> import holidays
>>> date(2014, 1, 1) in holidays.US()
True
>>> date(2014, 1, 2) in holidays.US()
False
```

> [!tip]
>
> Don't do this! It is not efficient because it is initializing a new Holiday object and
> generating a list of all the holidays in 2014 during each comparison.

It is more efficient to create the object only once:

```pycon
>>> us_holidays = holidays.US()
>>> date(2014, 1, 1) in us_holidays
True
>>> date(2014, 1, 2) in us_holidays
False
```

You can use the [`country_holidays`](https://github.com/vacanza/holidays/blob/dev/holidays/utils.py)
or [`financial_holidays`](https://github.com/vacanza/holidays/blob/dev/holidays/utils.py) functions
to create the object using a string with the country code:

```pycon
>>> us_holidays = holidays.country_holidays("US")
>>> nyse_holidays = holidays.financial_holidays("NYSE")
```

Use `years` parameter to populate the holidays years you are interested in:

```pycon
>>> us_holidays = holidays.US(years=2020)  # US 2020 holidays
>>> us_holidays = holidays.US(years=range(2020, 2026))  # US 2020-2025 holidays
```

Let's print out the holidays in 2014 specific to California, USA:

```pycon
>>> for date, name in sorted(holidays.US(subdiv='CA', years=2014).items()):
>>>     print(date, name)
2014-01-01 New Year's Day
2014-01-20 Martin Luther King Jr. Day
2014-02-15 Susan B. Anthony Day
2014-02-17 Washington's Birthday
2014-03-31 Cesar Chavez Day
2014-05-26 Memorial Day
2014-07-04 Independence Day
2014-09-01 Labor Day
2014-11-11 Veterans Day
2014-11-27 Thanksgiving
2014-11-28 Day After Thanksgiving
2014-12-25 Christmas Day
```

So far we've only checked holidays in 2014, so that's the only year the Holidays object has
generated:

```pycon
>>> us_holidays.years
set([2014])
>>> len(us_holidays)
10
```

## Expand parameter

Because, by default, the `expand` parameter is `True`, the Holiday object will calculate and add
holidays for other years when they are required:

```pycon
>>> date(2013, 1, 1) in us_holidays
True
>>> us_holidays.years
set([2013, 2014])
>>> len(us_holidays)
20
```

If we change the `expand` parameter to `False` the Holiday object will no longer add holidays from
new years:

```pycon
>>> us_holidays.expand = False
>>> date(2012, 1, 1) in us_holidays
False
>>> us_holidays.expand = True
>>> date(2012, 1, 1) in us_holidays
True
```

## Observed parameter

January 1st, 2012 fell on a Sunday, so the statutory holiday was observed on the 2nd. By default,
the `observed` param is `True`, so the holiday list will include January 2nd, 2012 as a holiday:

```pycon
>>> date(2012, 1, 1) in us_holidays
True
>>> us_holidays[date(2012, 1, 1)]
"New Year's Day"
>>> date(2012, 1, 2) in us_holidays
True
>>> us_holidays.get(date(2012, 1, 2))
"New Year's Day (observed)"
```

The values of `observed` and `expand` can be changed on the fly and the holiday list will be
adjusted accordingly:

```pycon
>>> us_holidays.observed = False
>>> date(2012, 1, 2) in us_holidays
False
us_holidays.observed = True
>>> date(2012, 1, 2) in us_holidays
True
```

## Language support

To change the language translation, you can set the language explicitly.

```pycon
>>> for dt, name in sorted(holidays.ES(years=2023, language="es").items()):
>>>     print(dt, name)
2023-01-06 Epifanía del Señor
2023-04-07 Viernes Santo
2023-05-01 Fiesta del Trabajo
2023-08-15 Asunción de la Virgen
2023-10-12 Fiesta Nacional de España
2023-11-01 Todos los Santos
2023-12-06 Día de la Constitución Española
2023-12-08 Inmaculada Concepción
2023-12-25 Natividad del Señor
```

## Subdivision support

Some holidays are only present in parts of a country. Use the `subdiv` parameter to include
the holidays specific to a subdivision (e.g. a state or province):

```pycon
>>> us_holidays = holidays.US(years=2018)
>>> us_pr_holidays = holidays.US(subdiv="PR", years=2018)
>>> "2018-01-06" in us_holidays
False
>>> "2018-01-06" in us_pr_holidays
True
```

## Date formats

Holiday objects accept dates as `datetime.date`, `datetime.datetime`, a Unix timestamp
(`int` or `float`), or a `str` in any format recognized by `dateutil.parser.parse()`.
Keys are always returned as `datetime.date` objects:

```pycon
>>> us_holidays = holidays.US(years=2014)
>>> "2014-01-01" in us_holidays
True
>>> "1/1/2014" in us_holidays
True
>>> 1388597445 in us_holidays  # Unix timestamp.
True
```

Show the holiday's name:

```pycon
>>> us_holidays.get("2014-01-01")
"New Year's Day"
```

## Date ranges

Slicing a holiday object returns the holiday dates within a range. The start date is included,
the stop date is not:

```pycon
>>> us_holidays["2014-01-01":"2014-01-03"]
[datetime.date(2014, 1, 1)]
```

## Holiday categories support

The framework provides multiple holiday categories, enabling you to filter results by official
status, religious significance, or institutional relevance.

### Basic Category Usage

Categories can be provided as a single string (e.g., 'public') or an iterable of strings.
For better maintainability, it's recommended to use the predefined constants
in `holidays.constants`. Note that category matching is case-sensitive.

To get holidays from specific categories:

```pycon
>>> import holidays
>>> from holidays.constants import PUBLIC, UNOFFICIAL
```

Get only public holidays.

```pycon
>>> us_public = holidays.UnitedStates(categories=PUBLIC, years=2024)
>>> len(us_public)
11
```

Get only unofficial holidays (cultural celebrations).

```pycon
>>> us_unofficial = holidays.UnitedStates(categories=UNOFFICIAL, years=2024)
>>> for date, name in sorted(us_unofficial.items()):
>>>     print(date, name)
2024-02-14 Valentine's Day
2024-03-17 Saint Patrick's Day
2024-10-31 Halloween
```

### Multiple categories

You can specify multiple categories to get a combined set of holidays.
Get both public and bank holidays for Belgium:

```pycon
>>> from holidays.constants import BANK, PUBLIC
>>> for dt, name in sorted(holidays.BE(years=2023, language="en_US", categories=(BANK, PUBLIC)).items()):
>>>     print(dt, name)
2023-01-01 New Year's Day
2023-04-07 Good Friday
2023-04-09 Easter Sunday
2023-04-10 Easter Monday
2023-05-01 Labor Day
2023-05-18 Ascension Day
2023-05-19 Friday after Ascension Day
2023-05-28 Whit Sunday
2023-05-29 Whit Monday
2023-07-21 National Day
2023-08-15 Assumption Day
2023-11-01 All Saints' Day
2023-11-11 Armistice Day
2023-12-25 Christmas Day
2023-12-26 Bank Holiday
```

### Religious categories

Many countries support religious categories for holidays specific to certain communities.
Get Catholic holidays in Germany (Saxony subdivision):

```pycon
>>> from holidays.constants import CATHOLIC
>>> de_sn_catholic = holidays.Germany(subdiv="SN", categories=CATHOLIC, years=2024)
>>> for date, name in sorted(de_sn_catholic.items()):
>>>     print(date, name)
2024-08-15 Mariä Himmelfahrt
```

### Checking supported categories

Each country defines which categories it supports:

```pycon
>>> print("US categories:", holidays.UnitedStates.supported_categories)
US categories: ('government', 'public', 'unofficial')

>>> print("Germany categories:", holidays.Germany.supported_categories)
Germany categories: ('catholic', 'public', 'school')

>>> from holidays.constants import SCHOOL
>>> de_by_school = holidays.Germany(subdiv="BY", categories=SCHOOL, years=2025)
>>> print(de_by_school["2025-08-01"])
Sommerferien

>>> print("Argentina categories:", holidays.Argentina.supported_categories)
Argentina categories: ('armenian', 'bank', 'government', 'hebrew', 'islamic', 'public')
```

For a comprehensive list of all available categories and their descriptions,
see the [Holiday Categories](holiday_categories.md) documentation.

## Working day-related calculations

To check if the specified date is a working day:

```pycon
>>> us_holidays = holidays.US(years=2024)  # Weekends in the US are Saturday and Sunday.
>>> us_holidays.is_working_day("2024-01-01")  # Monday, New Year's Day.
False
>>> us_holidays.is_working_day("2024-01-02")  # Tuesday, ordinary day.
True
>>> us_holidays.is_working_day("2024-01-06")  # Saturday, ordinary day.
False
>>> us_holidays.is_working_day("2024-01-15")  # Monday, Martin Luther King Jr. Day.
False
```

To find the nth working day after the specified date:

```pycon
>>> us_holidays.get_nth_working_day("2024-12-20", 5)
datetime.date(2024, 12, 30)
```

Here we calculate the 5th working day after December 20, 2024. Working days are 23 (Mon), 24 (Tue),
26 (Thu), 27 (Fri), 30 (Mon); 21-22, 28-29 - weekends, 25 - Christmas Day.

To calculate the number of working days between two specified dates:

```pycon
>>> us_holidays.get_working_days_count("2024-04-01", "2024-06-30")
63
```

Here we calculate the number of working days in Q2 2024.

## Getting the closest (next or previous) holiday

You can fetch next or previous holiday for a target date of your selected calendar. The function
returns found holiday's date and name excluding the target date.

Get the next holiday for the current date:

```pycon
>>> us_holidays = holidays.US(years=2025)
>>> us_holidays.get_closest_holiday()
(datetime.date(2025, 1, 20), 'Martin Luther King Jr. Day')
```

Get the previous holiday for the current date:

```pycon
>>> us_holidays = holidays.US(years=2025)
>>> us_holidays.get_closest_holiday(direction="backward")
(datetime.date(2025, 1, 1), "New Year's Day")
```

Get the next holiday for a specific target date:

```pycon
>>> us_holidays = holidays.US(years=2025)
>>> us_holidays.get_closest_holiday("2025-02-01")
(datetime.date(2025, 2, 17), "Washington's Birthday")
```

Get the previous holiday for a specific target date:

```pycon
>>> us_holidays = holidays.US(years=2025)
>>> us_holidays.get_closest_holiday("2025-02-01", direction="backward")
(datetime.date(2025, 1, 20), 'Martin Luther King Jr. Day')
```

If the closest holiday cannot be found, `None` is returned.

```pycon
>>> print(us_holidays.get_closest_holiday("2100-12-31"))
None
>>> print(us_holidays.get_closest_holiday("1777-01-01", direction="backward"))
None
```

## Date from holiday name

Holidays can be retrieved using their name too. `get_named` receives a string and returns a list
of holidays matching it (even partially, with case-insensitive check):

```pycon
>>> us_holidays = holidays.UnitedStates(years=2020)
>>> sorted(us_holidays.get_named("day"))
[datetime.date(2020, 1, 1), datetime.date(2020, 1, 20),
datetime.date(2020, 2, 17), datetime.date(2020, 5, 25),
datetime.date(2020, 7, 3), datetime.date(2020, 7, 4),
datetime.date(2020, 9, 7), datetime.date(2020, 10, 12),
datetime.date(2020, 11, 11), datetime.date(2020, 12, 25)]
```

## Additions

Holiday objects can be added together, and the resulting object will generate the holidays from
all the initial objects:

```pycon
>>> north_america = holidays.CA() + holidays.US() + holidays.MX()
>>> north_america.get("2014-07-01")
"Canada Day"
>>> north_america.get("2014-07-04")
"Independence Day"
```

If several holidays fall on the same date, their names are merged:

```pycon
>>> north_america.get("2014-01-01")
"Año Nuevo; New Year's Day"
```

The other form of addition is also available:

```pycon
>>> north_america = holidays.CA()
>>> north_america += holidays.US()
>>> north_america += holidays.MX()
>>> north_america.country
['CA', 'US', 'MX']
```

We can even get a set of holidays that include all the subdivision-specific holidays using
the built-in `sum` function:

```pycon
>>> a = sum([holidays.CA(subdiv=x) for x in holidays.CA.subdivisions])
>>> a.subdiv
['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
```

## Creating custom holidays (or augmenting existing ones with private ones)

Sometimes we may not be able to use the official federal statutory holiday list in our code. Let's
pretend we work for a company that does not include New Year's Day as a statutory holiday but does
include "Ninja Turtle Day" on July 13th. We can create a new class that inherits the US (please
note the base class import path) and the only method we need to override is
`__populate_public_holidays`:

```pycon
>>> from holidays.countries import US
>>> class CorporateHolidays(US):
>>>     def _populate_public_holidays(self):
>>> # Populate the holiday list with the default US holidays.
>>>         super()._populate_public_holidays()
>>> # Remove New Year's Day.
>>>         self.pop_named("New Year's Day")
>>> # Add Ninja Turtle Day.
>>>         self._add_holiday_jul_13("Ninja Turtle Day")
>>> date(2014, 1, 1) in holidays.country_holidays(country="US")
True
>>> date(2014, 1, 1) in CorporateHolidays()
False
>>> date(2014, 7, 13) in holidays.country_holidays(country="US")
False
>>> date(2014, 7, 13) in CorporateHolidays()
True
```

We can also inherit from the [`HolidayBase`](https://github.com/vacanza/holidays/blob/main/holidays/holiday_base.py)
class which doesn't have any holidays defined, so we must define them all ourselves.
This is how we would create a holidays class for a country that is not supported yet:

```pycon
>>> class NewCountryHolidays(holidays.HolidayBase):
>>>     def _populate_public_holidays(self):
>>>         self[date(year, 1, 2)] = "Some Federal Holiday"
>>>         self[date(year, 2, 3)] = "Another Federal Holiday"
>>> hdays = NewCountryHolidays()
```

We can use the `self._add_holiday_*` methods to specify holidays:

```pycon
>>> class MovingHolidays(holidays.HolidayBase):
>>>     def _populate_public_holidays(self):
>>>         self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")
>>>         self._add_holiday_last_fri_of_feb("Last Friday of February")
>>>         self._add_holiday_1st_mon_before_dec_25("Monday before Christmas")
>>> moving = MovingHolidays(years=2025)
```

The supported `_add_holiday_*` patterns are:

- `_add_holiday_<month>_<day>` for fixed-date holidays
- `_add_holiday_<last/nth>_<weekday>_of_<month>` for holidays that occur on a specific weekday of a month
- `_add_holiday_<n>_day(s)_<past/prior>_<last/nth>_<weekday>_of_<month>`
- `_add_holiday_<nth>_<weekday>_<before/from>_<month>_<day>`
- `_add_holiday_<n>_day(s)_<prior/past>_easter` (requires inheritance from `ChristianHolidays` holidays group)

Some examples of these methods would be:

- `_add_holiday_jan_1`
- `_add_holiday_last_mon_of_feb`
- `_add_holiday_1st_thu_of_nov`
- `_add_holiday_2_days_prior_2nd_mon_of_jan`
- `_add_holiday_1_day_past_last_fri_of_dec`
- `_add_holiday_1st_tue_from_dec_25`
- `_add_holiday_2nd_fri_before_jun_15`
- `_add_holiday_2_days_prior_easter` (make sure to derive from `ChristianHolidays`)
- `_add_holiday_1_day_past_easter` (make sure to derive from `ChristianHolidays`)

You can find the implementation details at `HolidayBase.__getattr__` method.

We can also include holidays for a subdivision (e.g. prov/state) in our new class:

```pycon
>>> class NewCountryHolidays(holidays.HolidayBase):
>>>     def _populate_public_holidays(self):
>>>         self[date(year, 1, 2)] = "Some Federal Holiday"
>>>
>>>     def _populate_subdiv_xx_public_holidays(self):
>>>         self[date(year, 2, 3)] = "Special XX subdiv-only holiday"
>>>
>>>     def _populate_subdiv_yy_public_holidays(self):
>>>         self[date(year, 3, 4)] = "Special YY subdiv-only holiday"
>>> hdays = NewCountryHolidays()
>>> hdays = NewCountryHolidays(subdiv="XX")
```

If you write the code necessary to create a holiday class for a country not currently supported,
please contribute your code to the project!

Perhaps you just have a list of dates that are holidays and want to turn them into a Holiday class
to access all the useful functionality. You can use the `append()` method which accepts a
dictionary of `{date: name}` pairs, a list of dates, or even singular date/string/timestamp
objects. Dates passed without a name are added as "Holiday":

```pycon
>>> custom_holidays = holidays.HolidayBase()
>>> custom_holidays.append(["2015-01-01", "07/04/2015"])
>>> custom_holidays.append(date(2015, 12, 25))
>>> custom_holidays.get("2015-01-01")
'Holiday'
```

The `append()` method is an alias for `update()`. Either of them can also be used to add custom
holidays to an existing country object:

```pycon
>>> us_holidays = holidays.US(years=2015)
>>> us_holidays.update({"2015-07-10": "My birthday!"})
>>> us_holidays.get("2015-07-10")
'My birthday!'
```

## Special holidays

Special (one-off) country-wide holidays, such as a royal jubilee, can be defined with
the `special_public_holidays` mapping of a year to a tuple of `(month, day, name)` entries
(for other holiday categories use `special_<category>_holidays`):

```pycon
>>> from holidays.calendars.gregorian import APR, DEC, JUL, JUN, SEP
>>> class SpecialHolidays(holidays.HolidayBase):
>>>     special_public_holidays = {
>>>         1977: (JUN, 7, "Silver Jubilee of Elizabeth II"),
>>>         1981: (JUL, 29, "Wedding of Charles and Diana"),
>>>         1999: (DEC, 31, "Millennium Celebrations"),
>>>         2002: (JUN, 3, "Golden Jubilee of Elizabeth II"),
>>>         2011: (APR, 29, "Wedding of William and Catherine"),
>>>         2012: (JUN, 5, "Diamond Jubilee of Elizabeth II"),
>>>         2022: (
>>>             (JUN, 3, "Platinum Jubilee of Elizabeth II"),
>>>             (SEP, 19, "State Funeral of Queen Elizabeth II"),
>>>         ),
>>>     }
>>> special_holidays = SpecialHolidays(years=2022)
>>> special_holidays.get("2022-09-19")
'State Funeral of Queen Elizabeth II'
```

## Add years to an existing Holiday object

Because the Holiday class is a subclass of dictionary, we use the
[update()](https://docs.python.org/3/library/stdtypes.html?highlight=update#dict.update)
method to add years to an existing holiday object:

```pycon
>>> from holidays import country_holidays
>>> us_holidays = country_holidays("US", years=2020)
# to add new years of holidays to the object:
>>> us_holidays.update(country_holidays("US", years=2021))
```

## Other ways to specify the country

Each country has two class names that can be called in addition to the alpha-2 ISO code: its
3-digit ISO code and an internal class name.

```pycon
>>> holidays.USA() == holidays.US()
True
>>> holidays.UnitedStates() == holidays.US()
True
```

## Generate iCalendar content and export to `.ics`

[`ICalExporter`](https://github.com/vacanza/holidays/blob/main/holidays/ical.py) facilitates
the creation and export of iCalendar files
in compliance with [RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545).

```pycon
>>> from holidays import country_holidays
>>> from holidays.ical import ICalExporter
>>> us_holidays = country_holidays("US", years=2020)
# Initializes the iCalendar exporter.
>>> exporter = ICalExporter(us_holidays)
```

To create iCalendar content, use
[`generate`](https://github.com/vacanza/holidays/blob/main/holidays/ical.py).

```pycon
>>> from holidays import country_holidays
>>> from holidays.ical import ICalExporter
>>> th_holidays = country_holidays("TH", years=2024)
>>> exporter = ICalExporter(th_holidays)
>>> ical_content = exporter.generate()
# Thailand's Songkran Festival (April 13th-15th) should be counted as a single
# VEVENT with a duration of three days.
>>> ical_content.count("SUMMARY:วันสงกรานต์\r\n")
1
>>> "DURATION:P3D\r\n" in ical_content
True
# Adds ";LANGUAGE=" to SUMMARY too.
>>> exporter = ICalExporter(th_holidays, show_language=True)
>>> ical_content = exporter.generate()
>>> ical_content.count("SUMMARY;LANGUAGE=th:วันสงกรานต์\r\n")
1
```

Each calendar is named after its holidays object (`X-WR-CALNAME`), and every event gets a UID
derived from the entity, subdivision, language, categories, holiday name, start date and length,
so re-generating a calendar yields the same UIDs and subscribed clients update events in place.
For calendars published for subscription, `refresh_interval_weeks` adds the `REFRESH-INTERVAL` and
`X-PUBLISHED-TTL` hints.

``` python
>>> from holidays import country_holidays
>>> from holidays.ical import ICalExporter
>>> be_holidays = country_holidays('BE', years=2024, language='en_US')
>>> exporter = ICalExporter(be_holidays, refresh_interval_weeks=1)
>>> exporter.calendar_name
'Belgium Public Holidays [en-US]'
>>> ical_content = exporter.generate()
>>> "X-WR-CALNAME:Belgium Public Holidays [en-US]\r\n" in ical_content
True
>>> "REFRESH-INTERVAL;VALUE=DURATION:P1W\r\nX-PUBLISHED-TTL:P1W\r\n" in ical_content
True
```

> [!tip]
>
> Although the iCalendar specification supports a wide range of language formats as outlined
> in [RFC 5646](https://datatracker.ietf.org/doc/html/rfc5646), the Holidays object requires
> that the `language` attribute adhere to the [ISO 639-1 or
> ISO 639-2](https://www.loc.gov/standards/iso639-2/php/code_list.php) language codes,
> such as `en` or `pap-AW`. Additionally, if no `language` is specified for a holiday, but a
> `default_language` is set for the Holiday object, the default language will be used instead.

```pycon
>>> from holidays import country_holidays
>>> from holidays.ical import ICalExporter
>>> cn_holidays = country_holidays("CN", years=2024, language="en_US")
>>> jp_holidays = country_holidays("JP", years=2024, language="en_US")
>>> kr_holidays = country_holidays("KR", years=2024, language="en_US")
>>> east_asia_holidays = cn_holidays + jp_holidays + kr_holidays
>>> ical_content = ICalExporter(east_asia_holidays).generate()
# Even with the combined China-Japan-Korea calendar, there should be only one
# 'New Year's Day' VEVENT.
>>> ical_content.count("SUMMARY:New Year's Day\r\n")
1
```

To export to `.ics` format, use
[`save_ics`](https://github.com/vacanza/holidays/blob/main/holidays/ical.py).

```pycon
>>> from pathlib import Path
>>> from holidays import financial_holidays
>>> from holidays.ical import ICalExporter
# Export the NYSE_2024_calendar.ics file in the current directory
>>> nyse_exporter = ICalExporter(financial_holidays("NYSE", years=2024))
>>> nyse_exporter.save_ics(file_path="NYSE_2024_calendar.ics")
# Export the NYSE_2024_calendar.ics file to MS Windows' Downloads folder instead.
>>> downloads_path = Path.home() / "Downloads"
>>> nyse_exporter.save_ics(file_path=str(downloads_path / "NYSE_2024_calendar.ics"))
```

Generate `.ics` files with categories, language, and subdivisions.

```pycon
>>> from holidays.countries.india import IN
>>> from holidays.ical import ICalExporter
>>>
>>> years = range(2021, 2026)
>>> language = "en_US"
>>> subdiv = "AP"  # Andhra Pradesh state.
>>>
>>> for category in IN.supported_categories:
>>>     holidays = IN(
>>>         years=years,
>>>         categories=category,
>>>         language=language,
>>>         subdiv=subdiv,
>>>     )
>>>     filename = f"IN_{subdiv}_{language}_{category.upper()}.ics"
>>>     ICalExporter(holidays).save_ics(filename)
```

For advanced features and customization of the exported `.ics` output, consider using
the [icalendar](https://github.com/collective/icalendar) package.

## holidays-ics Tool

For user convenience, the library includes `holidays-ics` tool for generating iCalendar (.ics)
files from holiday calendars provided by the library. It supports country, subdivision,
and financial market calendars, holiday category filtering, localized holiday names,
year selection, custom output paths, and output filename templates.

The tool can be run either as an installed command:

```shell
holidays-ics CODE [OPTIONS]
```

or as a Python module:

```shell
python -m holidays.generate_ics CODE [OPTIONS]
```

If you do not have Python installed, you can run the tool directly with `uv`:

```shell
uvx --from holidays holidays-ics CODE [OPTIONS]
```

This downloads and runs the latest version of the tool automatically, without requiring
a Python installation or any manual setup of `holidays` package.

For installation instructions, see `uv` [documentation](https://docs.astral.sh/uv/getting-started/installation/).

By default, the generated calendar contains holidays for the current year and is written
to a file whose name is derived from the selected options and year range.
The `--years` option accepts a single year (2025), a year range (2025-2027), or a
relative range (+10), which selects the current year through the current year plus 10.

### Output filename templates

Instead of specifying an explicit output path with `--output`, you can use
`--output-template` to generate output filenames dynamically.

Supported placeholders:

| Placeholder    | Description                                                      |
|----------------|------------------------------------------------------------------|
| `{code}`       | Country or financial market code                                 |
| `{subdiv}`     | Subdivision code, or `ALL` if not specified                      |
| `{language}`   | Requested language, or `DEFAULT` if not specified                |
| `{categories}` | Holiday categories joined with `_`, or `PUBLIC` if not specified |
| `{start_year}` | First year                                                       |
| `{end_year}`   | Last year                                                        |
| `{all}`        | Default output filename without the `.ics` extension             |
| `{today}`      | Current date in `YYYYMMDD` format                                |

To include literal `{` or `}` characters, write them as `{{` and `}}`.

### Examples

Calendar for the current year:

```shell
holidays-ics US
```

Save calendar to a custom file:

```shell
holidays-ics US --output test.ics
```

Calendar for the current and next 10 years:

```shell
holidays-ics US --years +10
```

Calendar for the current year and the previous 5 years:

```shell
holidays-ics US --years -5
```

Calendar for specific year:

```shell
holidays-ics US --years 2035
```

Calendar for an explicit year range:

```shell
holidays-ics US --years 2021-2030
```

Calendar containing unofficial holidays only:

```shell
holidays-ics US --categories unofficial
```

Calendar containing public and optional holidays:

```shell
holidays-ics CA --categories public,optional
```

Financial market holiday calendar:

```shell
holidays-ics XNYS
```

Calendar for Switzerland, specific to the Canton of Zurich:

```shell
holidays-ics CH --subdiv ZH
```

Calendar for Switzerland, localized in German:

```shell
holidays-ics CH --language de
```

Calendar for Switzerland, specific to the Canton of Zurich, localized in German:

```shell
holidays-ics CH --subdiv ZH --language de
```

Calendar for Switzerland, localized in German, saved to a file named from the language and country codes:

```shell
holidays-ics CH --language de --output-template "{language}_{code}.ics"
```

Save calendar to a file named after the country code:

```shell
holidays-ics US --output-template "{code}.ics"
```

Prepend "HOLIDAYS_" to the default file name:

```shell
holidays-ics US --years 2021-2030 --categories unofficial --subdiv TX --language th --output-template "HOLIDAYS_{all}.ics"
```

The tool can also display the supported subdivisions, categories, and languages for a selected
country or market without generating an `.ics` file.

List the supported subdivisions:

```shell
holidays-ics CH --list-subdivisions
```

List the supported holiday categories:

```shell
holidays-ics US --list-categories
```

List the supported languages:

```shell
holidays-ics CA --list-languages
```
