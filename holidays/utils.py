import inspect

import holidays.countries as countries


def list_supported_countries():
    """List all supported countries incl. their abbreviation."""
    return [name for name, obj in
            inspect.getmembers(countries, inspect.isclass)]


def CountryHoliday(country, years=[], prov=None, state=None, expand=True,
                   observed=True):
    try:
        country_classes = inspect.getmembers(countries, inspect.isclass)
        country = next(obj for name, obj in country_classes if name == country)
        country_holiday = country(years=years, prov=prov, state=state,
                                  expand=expand, observed=observed)
    except StopIteration:
        raise KeyError("Country %s not available" % country)
    return country_holiday
