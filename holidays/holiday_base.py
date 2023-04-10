#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

__all__ = ("DateLike", "HolidayBase", "HolidaySum")

import copy
import os
import warnings
from calendar import isleap
from datetime import date, datetime, timedelta
from gettext import NullTranslations, gettext, translation
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Set, Tuple
from typing import Union, cast

from dateutil.parser import parse

from holidays.constants import HOLIDAY_NAME_DELIMITER, MON, TUE, WED, THU, FRI
from holidays.constants import SAT, SUN

DateArg = Union[date, Tuple[int, int]]
DateLike = Union[date, datetime, str, float, int]

gettext = gettext


class HolidayBase(Dict[date, str]):
    """
    A dict-like object containing the holidays for a specific country (and
    province or state if so initiated); inherits the dict class (so behaves
    similarly to a dict). Dates without a key in the Holiday object are not
    holidays.

    The key of the object is the date of the holiday and the value is the name
    of the holiday itself. When passing the date as a key, the date can be
    expressed as one of the following formats:

    * datetime.datetime type;
    * datetime.date types;
    * a float representing a Unix timestamp;
    * or a string of any format (recognized by datetime.parse).

    The key is always returned as a `datetime.date` object.

    To maximize speed, the list of holidays is built as needed on the fly, one
    calendar year at a time. When you instantiate the object, it is empty, but
    the moment a key is accessed it will build that entire year's list of
    holidays. To pre-populate holidays, instantiate the class with the years
    argument:

    us_holidays = holidays.US(years=2020)

    It is generally instantiated using the :func:`country_holidays` function.

    The key of the :class:`dict`-like :class:`HolidayBase` object is the
    `date` of the holiday, and the value is the name of the holiday itself.
    Dates where a key is not present are not public holidays (or, if
    **observed** is False, days when a public holiday is observed).

    When passing the `date` as a key, the `date` can be expressed in one of the
    following types:

    * :class:`datetime.date`,
    * :class:`datetime.datetime`,
    * a :class:`str` of any format recognized by :func:`dateutil.parser.parse`,
    * or a :class:`float` or :class:`int` representing a POSIX timestamp.

    The key is always returned as a :class:`datetime.date` object.

    To maximize speed, the list of public holidays is built on the fly as
    needed, one calendar year at a time. When the object is instantiated
    without a **years** parameter, it is empty, but, unless **expand** is set
    to False, as soon as a key is accessed the class will calculate that entire
    year's list of holidays and set the keys with them.

    If you need to list the holidays as opposed to querying individual dates,
    instantiate the class with the **years** parameter.

    Example usage:

    >>> from holidays import country_holidays
    >>> us_holidays = country_holidays('US')
    # For a specific subdivisions (e.g. state or province):
    >>> california_holidays = country_holidays('US', subdiv='CA')

    The below will cause 2015 holidays to be calculated on the fly:

    >>> from datetime import date
    >>> assert date(2015, 1, 1) in us_holidays

    This will be faster because 2015 holidays are already calculated:

    >>> assert date(2015, 1, 2) not in us_holidays

    The :class:`HolidayBase` class also recognizes strings of many formats
    and numbers representing a POSIX timestamp:

    >>> assert '2014-01-01' in us_holidays
    >>> assert '1/1/2014' in us_holidays
    >>> assert 1388597445 in us_holidays

    Show the holiday's name:

    >>> us_holidays.get('2014-01-01')
    "New Year's Day"

    Check a range:

    >>> us_holidays['2014-01-01': '2014-01-03']
    [datetime.date(2014, 1, 1)]

    List all 2020 holidays:

    >>> us_holidays = country_holidays('US', years=2020)
    >>> for day in us_holidays.items():
    ...     print(day)
    (datetime.date(2020, 1, 1), "New Year's Day")
    (datetime.date(2020, 1, 20), 'Martin Luther King Jr. Day')
    (datetime.date(2020, 2, 17), "Washington's Birthday")
    (datetime.date(2020, 5, 25), 'Memorial Day')
    (datetime.date(2020, 7, 4), 'Independence Day')
    (datetime.date(2020, 7, 3), 'Independence Day (Observed)')
    (datetime.date(2020, 9, 7), 'Labor Day')
    (datetime.date(2020, 10, 12), 'Columbus Day')
    (datetime.date(2020, 11, 11), 'Veterans Day')
    (datetime.date(2020, 11, 26), 'Thanksgiving')
    (datetime.date(2020, 12, 25), 'Christmas Day')

    Some holidays are only present in parts of a country:

    >>> us_pr_holidays = country_holidays('US', subdiv='PR')
    >>> assert '2018-01-06' not in us_holidays
    >>> assert '2018-01-06' in us_pr_holidays

    Append custom holiday dates by passing one of:

    * a :class:`dict` with date/name key/value pairs (e.g.
      ``{'2010-07-10': 'My birthday!'}``),
    * a list of dates (as a :class:`datetime.date`, :class:`datetime.datetime`,
      :class:`str`, :class:`int`, or :class:`float`); ``'Holiday'`` will be
      used as a description,
    * or a single date item (of one of the types above); ``'Holiday'`` will be
      used as a description:

    >>> custom_holidays = country_holidays('US', years=2015)
    >>> custom_holidays.update({'2015-01-01': "New Year's Day"})
    >>> custom_holidays.update(['2015-07-01', '07/04/2015'])
    >>> custom_holidays.update(date(2015, 12, 25))
    >>> assert date(2015, 1, 1) in custom_holidays
    >>> assert date(2015, 1, 2) not in custom_holidays
    >>> assert '12/25/2015' in custom_holidays

    For special (one-off) country-wide holidays handling use
    :attr:`special_holidays`:

    .. code-block:: python

        special_holidays = {
            1977: ((JUN, 7, "Silver Jubilee of Elizabeth II"),),
            1981: ((JUL, 29, "Wedding of Charles and Diana"),),
            1999: ((DEC, 31, "Millennium Celebrations"),),
            2002: ((JUN, 3, "Golden Jubilee of Elizabeth II"),),
            2011: ((APR, 29, "Wedding of William and Catherine"),),
            2012: ((JUN, 5, "Diamond Jubilee of Elizabeth II"),),
            2022: (
                (JUN, 3, "Platinum Jubilee of Elizabeth II"),
                (SEP, 19, "State Funeral of Queen Elizabeth II"),
            ),
        }

        def _populate(self, year):
            super()._populate(year)

            ...

    For more complex logic, like 4th Monday of January, you can inherit the
    :class:`HolidayBase` class and define your own :meth:`_populate` method.
    See documentation for examples.
    """

    country: str
    """The country's ISO 3166-1 alpha-2 code."""
    market: str
    """The market's ISO 3166-1 alpha-2 code."""
    subdivisions: List[str] = []
    """The subdivisions supported for this country (see documentation)."""
    years: Set[int]
    """The years calculated."""
    expand: bool
    """Whether the entire year is calculated when one date from that year
    is requested."""
    observed: bool
    """Whether dates when public holiday are observed are included."""
    subdiv: Optional[str] = None
    """The subdiv requested."""
    special_holidays: Dict[int, Tuple[Tuple[int, int, str], ...]] = {}
    """A list of the country-wide special (as opposite to regular) holidays for
    a specific year."""
    _deprecated_subdivisions: List[str] = []
    """Other subdivisions whose names are deprecated or aliases of the official
    ones."""
    weekend: Set[int] = {SAT, SUN}
    """Country weekend days."""

    def __init__(
        self,
        years: Optional[Union[int, Iterable[int]]] = None,
        expand: bool = True,
        observed: bool = True,
        subdiv: Optional[str] = None,
        prov: Optional[str] = None,  # Deprecated.
        state: Optional[str] = None,  # Deprecated.
        language: Optional[str] = None,
    ) -> None:
        """
        :param years:
            The year(s) to pre-calculate public holidays for at instantiation.

        :param expand:
            Whether the entire year is calculated when one date from that year
            is requested.

        :param observed:
            Whether to include the dates when public holiday are observed
            (e.g. a holiday falling on a Sunday being observed the
            following Monday). This doesn't work for all countries.

        :param subdiv:
            The subdivision (e.g. state or province); not implemented for all
            countries (see documentation).

        :param prov:
            *deprecated* use subdiv instead.

        :param state:
            *deprecated* use subdiv instead.

        :param language:
            The language which the returned holiday names will be translated
            into. It must be an ISO 639-1 (2-letter) language code. If the
            language translation is not supported the original holiday names
            will be used.

        :return:
            A :class:`HolidayBase` object matching the **country**.
        """
        super().__init__()

        self.expand = expand
        self.language = language.lower() if language else None
        self.observed = observed
        self.subdiv = subdiv or prov or state

        self.tr = gettext  # Default translation method.

        if prov or state:
            warnings.warn(
                "Arguments prov and state are deprecated, use subdiv="
                f"'{prov or state}' instead.",
                DeprecationWarning,
            )

        if not isinstance(self, HolidaySum):
            if (
                subdiv
                and subdiv
                not in self.subdivisions + self._deprecated_subdivisions
            ):
                if hasattr(self, "market"):
                    error = (
                        f"Market '{self.market}' does not have subdivision "
                        f"'{subdiv}'"
                    )
                else:
                    error = (
                        f"Country '{self.country}' does not have subdivision "
                        f"'{subdiv}'"
                    )
                raise NotImplementedError(error)

            name = getattr(self, "country", getattr(self, "market", None))
            if name:
                locale_dir = os.path.join(os.path.dirname(__file__), "locale")
                translator: NullTranslations
                translations = sorted(
                    (
                        # Collect `language` part from
                        # holidays/locale/<language>/LC_MESSAGES/country.po
                        str(translation).split(os.sep)[-3]
                        for translation in Path(locale_dir).rglob(f"{name}.mo")
                    )
                )
                if language and language in translations:
                    translator = translation(
                        name,
                        languages=[language],
                        localedir=locale_dir,
                    )
                else:
                    translator = translation(
                        name,
                        fallback=True,
                        localedir=locale_dir,
                    )
                self.tr = translator.gettext

        if isinstance(years, int):
            self.years = {years}
        else:
            self.years = set(years) if years is not None else set()

        for year in self.years:
            self._populate(year)

    @property
    def __attribute_names(self):
        return (
            "country",
            "expand",
            "language",
            "market",
            "observed",
            "subdiv",
            "years",
        )

    def __setattr__(self, key: str, value: Any) -> None:
        dict.__setattr__(self, key, value)

        if self and key == "observed":
            self.clear()
            for year in self.years:  # Re-populate holidays for each year.
                self._populate(year)

    def __keytransform__(self, key: DateLike) -> date:
        """Transforms the date from one of the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp

        to :class:`datetime.date`, which is how it's stored by the class."""

        # Try to catch `date` and `str` type keys first.
        if type(key) == date:  # Key has `date` type.
            dt = key

        elif type(key) == str:  # Key has `str` type.
            try:
                dt = parse(key).date()
            except (OverflowError, ValueError):
                raise ValueError(f"Cannot parse date from string '{key}'")

        # Check all other types.
        elif isinstance(key, datetime):  # Key type is derived from `datetime`.
            dt = key.date()

        # Must go after the `isinstance(key, datetime)` check
        # as datetime is derived from `date`.
        elif isinstance(key, date):  # Key type is derived from `date`.
            dt = key

        elif isinstance(
            key, (float, int)
        ):  # Key type is derived from `float` or `int`.
            dt = datetime.utcfromtimestamp(key).date()

        else:  # Key type is not supported.
            raise TypeError(f"Cannot convert type '{type(key)}' to date.")

        # Automatically expand for `expand=True` cases.
        if self.expand and dt.year not in self.years:
            self.years.add(dt.year)
            self._populate(dt.year)

        return dt

    def __bool__(self) -> bool:
        return len(self) > 0

    def __contains__(self, key: object) -> bool:
        """Return true if date is in self, false otherwise. Accepts a date in
        the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp.
        """

        if not isinstance(key, (date, datetime, float, int, str)):
            raise TypeError(f"Cannot convert type '{type(key)}' to date.")

        return dict.__contains__(
            cast("Mapping[Any, Any]", self), self.__keytransform__(key)
        )

    def __getitem__(self, key: DateLike) -> Any:
        if isinstance(key, slice):
            if not key.start or not key.stop:
                raise ValueError("Both start and stop must be given.")

            start = self.__keytransform__(key.start)
            stop = self.__keytransform__(key.stop)

            if key.step is None:
                step = 1
            elif isinstance(key.step, timedelta):
                step = key.step.days
            elif isinstance(key.step, int):
                step = key.step
            else:
                raise TypeError(
                    f"Cannot convert type '{type(key.step)}' to int."
                )

            if step == 0:
                raise ValueError("Step value must not be zero.")

            date_diff = stop - start
            if date_diff.days < 0 <= step or date_diff.days >= 0 > step:
                step *= -1

            days_in_range = []
            for delta_days in range(0, date_diff.days, step):
                day = start + timedelta(days=delta_days)
                if day in self:
                    days_in_range.append(day)

            return days_in_range

        return dict.__getitem__(self, self.__keytransform__(key))

    def __setitem__(self, key: DateLike, value: str) -> None:
        if key in self:
            # If there are multiple holidays on the same date
            # order their names alphabetically.
            holiday_names = set(self[key].split(HOLIDAY_NAME_DELIMITER))
            holiday_names.add(value)
            value = HOLIDAY_NAME_DELIMITER.join(sorted(holiday_names))

        dict.__setitem__(self, self.__keytransform__(key), value)

    def update(  # type: ignore[override]
        self, *args: Union[Dict[DateLike, str], List[DateLike], DateLike]
    ) -> None:
        # TODO: fix arguments; should not be *args (cannot properly Type hint)
        """Update the object, overwriting existing dates.

        :param:
            Either another dictionary object where keys are dates and values
            are holiday names, or a single date (or a list of dates) for which
            the value will be set to "Holiday".

            Dates can be expressed in one or more of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.
        """
        for arg in args:
            if isinstance(arg, dict):
                for key, value in arg.items():
                    self[key] = value
            elif isinstance(arg, list):
                for item in arg:
                    self[item] = "Holiday"
            else:
                self[arg] = "Holiday"

    def append(
        self, *args: Union[Dict[DateLike, str], List[DateLike], DateLike]
    ) -> None:
        """Alias for :meth:`update` to mimic list type."""
        return self.update(*args)

    def get(
        self,
        key: DateLike,
        default: Union[str, Any] = None,
    ) -> Union[str, Any]:
        """Return the holiday name for a date if date is a holiday, else
        default. If default is not given, it defaults to None, so that this
        method never raises a KeyError. If more than one holiday is present,
        they are separated by a comma.

        :param key:
            The date expressed in one of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.

        :param default:
            The default value to return if no value is found.
        """
        return dict.get(
            self,
            self.__keytransform__(key),
            default,
        )

    def get_list(self, key: DateLike) -> List[str]:
        """Return a list of all holiday names for a date if date is a holiday,
        else empty string.

        :param key:
            The date expressed in one of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.
        """
        return [
            name
            for name in self.get(key, "").split(HOLIDAY_NAME_DELIMITER)
            if name
        ]

    def get_named(self, holiday_name: str, lookup="icontains") -> List[date]:
        """Return a list of all holiday dates matching the provided holiday
        name. The match will be made case insensitively and partial matches
        will be included by default.

        :param holiday_name:
            The holiday's name to try to match.
        :param lookup:
            The holiday name lookup type:
                contains - case sensitive contains match;
                exact - case sensitive exact match;
                startswith - case sensitive starts with match;
                icontains - case insensitive contains match;
                iexact - case insensitive exact match;
                istartswith - case insensitive starts with match;

        :return:
            A list of all holiday dates matching the provided holiday name.
        """
        holiday_date_names_mapping: Dict[date, List[str]] = {
            key: value.split(HOLIDAY_NAME_DELIMITER)
            for key, value in self.items()
        }

        if lookup == "icontains":
            holiday_name_lower = holiday_name.lower()
            return [
                dt
                for dt, names in holiday_date_names_mapping.items()
                if any((holiday_name_lower in name.lower() for name in names))
            ]
        elif lookup == "exact":
            return [
                dt
                for dt, names in holiday_date_names_mapping.items()
                if any((holiday_name == name for name in names))
            ]
        elif lookup == "contains":
            return [
                dt
                for dt, names in holiday_date_names_mapping.items()
                if any((holiday_name in name for name in names))
            ]
        elif lookup == "startswith":
            return [
                dt
                for dt, names in holiday_date_names_mapping.items()
                if any(
                    (
                        holiday_name == name[: len(holiday_name)]
                        for name in names
                    )
                )
            ]
        elif lookup == "iexact":
            holiday_name_lower = holiday_name.lower()
            return [
                dt
                for dt, names in holiday_date_names_mapping.items()
                if any((holiday_name_lower == name.lower() for name in names))
            ]
        elif lookup == "istartswith":
            holiday_name_lower = holiday_name.lower()
            return [
                dt
                for dt, names in holiday_date_names_mapping.items()
                if any(
                    (
                        holiday_name_lower == name[: len(holiday_name)].lower()
                        for name in names
                    )
                )
            ]

        raise AttributeError(f"Unknown lookup type: {lookup}")

    def pop(
        self,
        key: DateLike,
        default: Union[str, Any] = None,
    ) -> Union[str, Any]:
        """If date is a holiday, remove it and return its date, else return
        default.

        :param key:
            The date expressed in one of the following types:

            * :class:`datetime.date`,
            * :class:`datetime.datetime`,
            * a :class:`str` of any format recognized by
              :func:`dateutil.parser.parse`,
            * or a :class:`float` or :class:`int` representing a POSIX
              timestamp.

        :param default:
            The default value to return if no match is found.

        :return:
            The date removed.

        :raise:
            KeyError if date is not a holiday and default is not given.
        """
        if default is None:
            return dict.pop(self, self.__keytransform__(key))

        return dict.pop(self, self.__keytransform__(key), default)

    def pop_named(self, name: str) -> List[date]:
        """Remove (no longer treat at as holiday) all dates matching the
        provided holiday name. The match will be made case insensitively and
        partial matches will be removed.

        :param name:
            The holiday's name to try to match.

        :param default:
            The default value to return if no match is found.

        :return:
            A list of dates removed.

        :raise:
            KeyError if date is not a holiday and default is not given.
        """
        dates = self.get_named(name)
        if not dates:
            raise KeyError(name)

        for dt in dates:
            self.pop(dt)

        return dates

    def copy(self):
        """Return a copy of the object."""
        return copy.copy(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HolidayBase):
            return False

        for attribute_name in self.__attribute_names:
            if getattr(self, attribute_name, None) != getattr(
                other, attribute_name, None
            ):
                return False

        return dict.__eq__(self, other)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, HolidayBase):
            return True

        for attribute_name in self.__attribute_names:
            if getattr(self, attribute_name, None) != getattr(
                other, attribute_name, None
            ):
                return True

        return dict.__ne__(self, other)

    def __add__(
        self, other: Union[int, "HolidayBase", "HolidaySum"]
    ) -> "HolidayBase":
        """Add another dictionary of public holidays creating a
        :class:`HolidaySum` object.

        :param other:
            The dictionary of public holiday to be added.

        :return:
            A :class:`HolidaySum` object unless the other object cannot be
            added, then :class:`self`.
        """
        if isinstance(other, int) and other == 0:
            # Required to sum() list of holidays
            # sum([h1, h2]) is equivalent to (0 + h1 + h2).
            return self

        if not isinstance(other, (HolidayBase, HolidaySum)):
            raise TypeError(
                "Holiday objects can only be added with other Holiday objects"
            )

        return HolidaySum(self, other)

    def __radd__(self, other: Any) -> "HolidayBase":
        return self.__add__(other)

    def _parse_holiday(self, *args) -> Tuple[str, date]:
        """Parse holiday data."""
        if len(args) == 2:
            name, dt = args
            if not isinstance(dt, date):
                raise TypeError(
                    "Invalid argument type: expected <class 'date'> "
                    f"got '{type(dt)}'."
                )
        elif len(args) == 3:
            name, month, day = args
            dt = date(self._year, month, day)
        else:
            raise TypeError("Incorrect number of arguments.")

        return name, dt

    def _add_holiday(self, *args) -> Optional[date]:
        """Add a holiday.

        This method accepts either `name: str, dt: date` or
        `name: str, month: int, day: int` arguments.
        """
        name, dt = self._parse_holiday(*args)
        if dt.year != self._year:
            return None

        self[dt] = self.tr(name)
        return dt

    def _add_subdiv_holidays(self):
        """Populate subdivision holidays."""
        if self.subdiv is not None:
            add_subdiv_holidays = getattr(
                self, f"_add_subdiv_{self.subdiv.lower()}_holidays", None
            )
            if add_subdiv_holidays and callable(add_subdiv_holidays):
                add_subdiv_holidays()

    def _populate(self, year: int) -> Set[Optional[date]]:
        """This is a private class that populates (generates and adds) holidays
        for a given year. To keep things fast, it assumes that no holidays for
        the year have already been populated. It is required to be called
        internally by any country populate() method, while should not be called
        directly from outside.
        To add holidays to an object, use the update() method:

        :param year:
            The year to populate with holidays.

        >>> from holidays import country_holidays
        >>> us_holidays = country_holidays('US', years=2020)
        # to add new holidays to the object:
        >>> us_holidays.update(country_holidays('US', years=2021))
        """

        self._year = year
        dates = set()

        # Populate items from the special holidays list.
        for month, day, name in self.special_holidays.get(year, ()):
            dates.add(self._add_holiday(name, date(year, month, day)))

        # Populate subdivision holidays.
        self._add_subdiv_holidays()

        return dates

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        """
        Returns True if the year is leap. Returns False otherwise.
        """
        return isleap(year)

    def _is_weekend(self, *args):
        """
        Returns True if date's week day is a weekend day.
        Returns False otherwise.
        """
        dt = args[0] if len(args) == 1 else date(self._year, *args)

        return dt.weekday() in self.weekend

    @staticmethod
    def __is_weekday(weekday, *args):
        """
        Returns True if `weekday` equals to the date's week day.
        Returns False otherwise.
        """
        dt = args[0] if len(args) == 1 else date(*args)

        return dt.weekday() == weekday

    @staticmethod
    def _is_monday(*args) -> bool:
        return HolidayBase.__is_weekday(MON, *args)

    @staticmethod
    def _is_tuesday(*args) -> bool:
        return HolidayBase.__is_weekday(TUE, *args)

    @staticmethod
    def _is_wednesday(*args) -> bool:
        return HolidayBase.__is_weekday(WED, *args)

    @staticmethod
    def _is_thursday(*args) -> bool:
        return HolidayBase.__is_weekday(THU, *args)

    @staticmethod
    def _is_friday(*args) -> bool:
        return HolidayBase.__is_weekday(FRI, *args)

    @staticmethod
    def _is_saturday(*args) -> bool:
        return HolidayBase.__is_weekday(SAT, *args)

    @staticmethod
    def _is_sunday(*args) -> bool:
        return HolidayBase.__is_weekday(SUN, *args)

    def __reduce__(self) -> Union[str, Tuple[Any, ...]]:
        return super().__reduce__()

    def __repr__(self) -> str:
        if self:
            return super().__repr__()

        parts = []
        if hasattr(self, "market"):
            parts.append(f"holidays.financial_holidays({self.market!r}")
        elif hasattr(self, "country"):
            if parts:
                parts.append(" + ")
            parts.append(f"holidays.country_holidays({self.country!r}")
            if self.subdiv:
                parts.append(f", subdiv={self.subdiv!r}")
        parts.append(")")

        return "".join(parts)

    def __str__(self) -> str:
        if self:
            return super().__str__()

        parts = []
        for attribute_name in self.__attribute_names:
            parts.append(
                "'%s': %s"
                % (attribute_name, getattr(self, attribute_name, None))
            )

        return f"{{{', '.join(parts)}}}"


class HolidaySum(HolidayBase):
    """
    Returns a :class:`dict`-like object resulting from the addition of two or
    more individual dictionaries of public holidays. The original dictionaries
    are available as a :class:`list` in the attribute :attr:`holidays,` and
    :attr:`country` and :attr:`subdiv` attributes are added
    together and could become :class:`list` s. Holiday names, when different,
    are merged. All years are calculated (expanded) for all operands.
    """

    country: Union[str, List[str]]  # type: ignore[assignment]
    """Countries included in the addition."""
    market: Union[str, List[str]]  # type: ignore[assignment]
    """Markets included in the addition."""
    subdiv: Optional[Union[str, List[str]]]  # type: ignore[assignment]
    """Subdivisions included in the addition."""
    holidays: List[HolidayBase]
    """The original HolidayBase objects included in the addition."""
    years: Set[int]
    """The years calculated."""

    def __init__(
        self,
        h1: Union[HolidayBase, "HolidaySum"],
        h2: Union[HolidayBase, "HolidaySum"],
    ) -> None:
        """
        :param h1:
            The first HolidayBase object to add.

        :param h2:
            The other HolidayBase object to add.

        Example:

        >>> from holidays import country_holidays
        >>> nafta_holidays = country_holidays('US', years=2020) + \
country_holidays('CA') + country_holidays('MX')
        >>> dates = sorted(nafta_holidays.items(), key=lambda x: x[0])
        >>> from pprint import pprint
        >>> pprint(dates[:10], width=72)
        [(datetime.date(2020, 1, 1), "Año Nuevo"),
         (datetime.date(2020, 1, 20), 'Martin Luther King Jr. Day'),
         (datetime.date(2020, 2, 3),
          'Día de la Constitución'),
         (datetime.date(2020, 2, 17), "Washington's Birthday, Family Day"),
         (datetime.date(2020, 3, 16),
          "Natalicio de Benito Juárez"),
         (datetime.date(2020, 4, 10), 'Good Friday'),
         (datetime.date(2020, 5, 1), 'Día del Trabajo'),
         (datetime.date(2020, 5, 18), 'Victoria Day')]
        """
        # Store originals in the holidays attribute.
        self.holidays = []
        for operand in (h1, h2):
            if isinstance(operand, HolidaySum):
                self.holidays.extend(operand.holidays)
            else:
                self.holidays.append(operand)

        kwargs: Dict[str, Any] = {}
        # Join years, expand and observed.
        kwargs["years"] = h1.years | h2.years
        kwargs["expand"] = h1.expand or h2.expand
        kwargs["observed"] = h1.observed or h2.observed
        # Join country and subdivisions data.
        # TODO: this way makes no sense: joining Italy Catania (IT, CA) with
        # USA Mississippi (US, MS) and USA Michigan (US, MI) yields
        # country=["IT", "US"] and subdiv=["CA", "MS", "MI"], which could very
        # well be California and Messina and Milano, or Catania, Mississippi
        # and Milano, or ... you get the picture.
        # Same goes when countries and markets are being mixed (working, yet
        # still nonsensical).
        for attr in ("country", "market", "subdiv"):
            if (
                getattr(h1, attr, None)
                and getattr(h2, attr, None)
                and getattr(h1, attr) != getattr(h2, attr)
            ):
                a1 = (
                    getattr(h1, attr)
                    if isinstance(getattr(h1, attr), list)
                    else [getattr(h1, attr)]
                )
                a2 = (
                    getattr(h2, attr)
                    if isinstance(getattr(h2, attr), list)
                    else [getattr(h2, attr)]
                )
                value = a1 + a2
            else:
                value = getattr(h1, attr, None) or getattr(h2, attr, None)

            if attr == "subdiv":
                kwargs[attr] = value
            else:
                setattr(self, attr, value)

        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        for operand in self.holidays:
            operand._populate(year)
            self.update(cast("Dict[DateLike, str]", operand))
