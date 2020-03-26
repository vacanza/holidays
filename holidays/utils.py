import inspect
import holidays
from datetime import date


def list_supported_countries():
    """List all supported countries incl. their abbreviation."""
    return [name for name, obj in
            inspect.getmembers(holidays.countries, inspect.isclass)]


def CountryHoliday(country, years=[], prov=None, state=None, expand=True,
                   observed=True):
    try:
        country_classes = inspect.getmembers(holidays.countries,
                                             inspect.isclass)
        country = next(obj for name, obj in country_classes if name == country)
        country_holiday = country(years=years, prov=prov, state=state,
                                  expand=expand, observed=observed)
    except StopIteration:
        raise KeyError("Country %s not available" % country)
    return country_holiday


def get_gre_date(year, Hmonth, Hday):
    """
    returns the gregian date of of a  of the given gregorian calendar
    yyyy year with Hijari Month & Day
    works *only* if hijri-converter library is installed, otherwise a warning
    is raised that this holiday is missing. hijri-converter requires
    Python >= 3.6
    """
    try:
        from hijri_converter import convert
    except ImportError:
        import warnings

        def warning_on_one_line(message, category, filename, lineno,
                                file=None, line=None):
            return filename + ': ' + str(message) + '\n'
        warnings.formatwarning = warning_on_one_line
        warnings.warn("Error estimating Islamic Holidays." +
                      "To estimate, install hijri-converter library")
        warnings.warn("pip install -U hijri-converter")
        warnings.warn("(see https://hijri-converter.readthedocs.io/ )")
        return []
    Hyear = convert.Gregorian(year, 1, 1).to_hijri().datetuple()[0]
    gres = []
    gres.append(convert.Hijri(Hyear - 1, Hmonth, Hday).to_gregorian())
    gres.append(convert.Hijri(Hyear, Hmonth, Hday).to_gregorian())
    gres.append(convert.Hijri(Hyear + 1, Hmonth, Hday).to_gregorian())
    gre_dates = []
    for gre in gres:
        if gre.year == year:
            gre_dates.append(date(*gre.datetuple()))
    return gre_dates
