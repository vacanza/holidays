#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

__all__ = ("DateLike", "HolidayBase", "HolidaySum")

import copy
from calendar import isleap
from datetime import date, datetime, timedelta, timezone
from functools import cached_property
from gettext import gettext, translation
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union, cast

from dateutil.parser import parse

from holidays.calendars.gregorian import (
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN,
    _timedelta,
    _get_nth_weekday_from,
    _get_nth_weekday_of_month,
    DAYS,
    MONTHS,
    WEEKDAYS,
)
from holidays.constants import HOLIDAY_NAME_DELIMITER, PUBLIC
from holidays.helpers import _normalize_arguments, _normalize_tuple

CategoryArg = Union[str, Iterable[str]]
DateArg = Union[date, Tuple[int, int]]
DateLike = Union[date, datetime, str, float, int]
SpecialHoliday = Union[Tuple[int, int, str], Tuple[Tuple[int, int, str], ...]]
SubstitutedHoliday = Union[
    Union[Tuple[int, int, int, int], Tuple[int, int, int, int, int]],
    Tuple[Union[Tuple[int, int, int, int], Tuple[int, int, int, int, int]], ...],
]
YearArg = Union[int, Iterable[int]]


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

    It is generally instantiated using the :func:`iso_3166_holidays` function.

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

    >>> from holidays import iso_3166_holidays
    >>> us_holidays = iso_3166_holidays('US')
    # For a specific subdivisions (e.g. state or province):
    >>> california_holidays = iso_3166_holidays('US', subdiv='CA')

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

    >>> us_holidays = iso_3166_holidays('US', years=2020)
    >>> for day in us_holidays.items():
    ...     print(day)
    (datetime.date(2020, 1, 1), "New Year's Day")
    (datetime.date(2020, 1, 20), 'Martin Luther King Jr. Day')
    (datetime.date(2020, 2, 17), "Washington's Birthday")
    (datetime.date(2020, 5, 25), 'Memorial Day')
    (datetime.date(2020, 7, 4), 'Independence Day')
    (datetime.date(2020, 7, 3), 'Independence Day (observed)')
    (datetime.date(2020, 9, 7), 'Labor Day')
    (datetime.date(2020, 10, 12), 'Columbus Day')
    (datetime.date(2020, 11, 11), 'Veterans Day')
    (datetime.date(2020, 11, 26), 'Thanksgiving')
    (datetime.date(2020, 12, 25), 'Christmas Day')

    Some holidays are only present in parts of a country:

    >>> us_pr_holidays = iso_3166_holidays('US', subdiv='PR')
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

    >>> custom_holidays = iso_3166_holidays('US', years=2015)
    >>> custom_holidays.update({'2015-01-01': "New Year's Day"})
    >>> custom_holidays.update(['2015-07-01', '07/04/2015'])
    >>> custom_holidays.update(date(2015, 12, 25))
    >>> assert date(2015, 1, 1) in custom_holidays
    >>> assert date(2015, 1, 2) not in custom_holidays
    >>> assert '12/25/2015' in custom_holidays

    For special (one-off) country-wide holidays handling use
    :attr:`special_public_holidays`:

    .. code-block:: python

        special_public_holidays = {
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
    """The entity's ISO 3166-1 alpha-2 code."""
    name: str
    """The entity's ISO 3166-1 name."""
    market: str
    """The market's ISO 3166-1 alpha-2 code."""
    subdivisions: Tuple[str, ...] = ()
    """The subdivisions supported for this country (see documentation)."""
    subdivisions_aliases: Dict[str, str] = {}
    """Aliases for the ISO 3166-2 subdivision codes with the key as alias and
    the value the ISO 3166-2 subdivision code."""
    years: Set[int]
    """The years calculated."""
    expand: bool
    """Whether the entire year is calculated when one date from that year
    is requested."""
    observed: bool
    """Whether dates when public holiday are observed are included."""
    subdiv: Optional[str] = None
    """The subdiv requested as ISO 3166-2 code or one of the aliases."""
    special_holidays: Dict[int, Union[SpecialHoliday, SubstitutedHoliday]] = {}
    """A list of the country-wide special (as opposite to regular) holidays for
    a specific year."""
    weekend: Set[int] = {SAT, SUN}
    """Country weekend days."""
    weekend_workdays: Set[date] = set()
    """Working days moved to weekends."""
    default_category: str = PUBLIC
    """The entity category used by default."""
    default_language: Optional[str] = None
    """The entity language used by default."""
    categories: Set[str] = set()
    """Requested holiday categories."""
    supported_categories: Tuple[str, ...] = (PUBLIC,)
    """All holiday categories supported by this entity."""
    supported_languages: Tuple[str, ...] = ()
    """All languages supported by this entity."""

    def __init__(
        self,
        years: Optional[YearArg] = None,
        expand: bool = True,
        observed: bool = True,
        subdiv: Optional[str] = None,
        language: Optional[str] = None,
        categories: Optional[CategoryArg] = None,
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
            The subdivision (e.g. state or province) as a ISO 3166-2 code
            or its alias; not implemented for all countries (see documentation).

        :param language:
            The language which the returned holiday names will be translated
            into. It must be an ISO 639-1 (2-letter) language code. If the
            language translation is not supported the original holiday names
            will be used.

        :param categories:
            Requested holiday categories.

        :return:
            A :class:`HolidayBase` object matching the **country**.
        """
        super().__init__()

        # Categories validation.
        if self.default_category and self.default_category not in self.supported_categories:
            raise ValueError("The default category must be listed in supported categories.")

        if not self.default_category and not categories:
            raise ValueError("Categories cannot be empty if `default_category` is not set.")

        categories = _normalize_arguments(str, categories) or {self.default_category}
        if unknown_categories := categories.difference(  # type: ignore[union-attr]
            self.supported_categories
        ):
            raise ValueError(f"Category is not supported: {', '.join(unknown_categories)}.")

        # Subdivision validation.
        if subdiv is not None:
            # Handle subdivisions passed as integers.
            if isinstance(subdiv, int):
                subdiv = str(subdiv)

            subdivisions_aliases = tuple(sorted(self.subdivisions_aliases))
            # Unsupported subdivisions.
            if not isinstance(self, HolidaySum) and subdiv not in (
                self.subdivisions + subdivisions_aliases
            ):
                raise NotImplementedError(
                    f"Entity `{self._entity_code}` does not have subdivision {subdiv}"
                )

        # Special holidays validation.
        if (has_substituted_holidays := getattr(self, "has_substituted_holidays", False)) and (
            not getattr(self, "substituted_label", None)
            or not getattr(self, "substituted_date_format", None)
        ):
            raise ValueError(
                f"Entity `{self._entity_code}` class must have `substituted_label` "
                "and `substituted_date_format` attributes set."
            )

        self.categories = categories
        self.expand = expand
        self.has_special_holidays = getattr(self, "has_special_holidays", False)
        self.has_substituted_holidays = has_substituted_holidays
        self.language = language.lower() if language else None
        self.observed = observed
        self.subdiv = subdiv
        self.weekend_workdays = set()

        supported_languages = set(self.supported_languages)
        self.tr = (
            translation(
                self._entity_code,
                fallback=language not in supported_languages,
                languages=[language] if language in supported_languages else None,
                localedir=str(Path(__file__).with_name("locale")),
            ).gettext
            if self._entity_code is not None
            else gettext
        )
        self.years = _normalize_arguments(int, years)

        # Populate holidays.
        for year in self.years:
            self._populate(year)

    def __add__(self, other: Union[int, "HolidayBase", "HolidaySum"]) -> "HolidayBase":
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
            raise TypeError("Holiday objects can only be added with other Holiday objects")

        return HolidaySum(self, other)

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

        return dict.__contains__(cast("Dict[Any, Any]", self), self.__keytransform__(key))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HolidayBase):
            return False

        for attribute_name in self.__attribute_names:
            if getattr(self, attribute_name, None) != getattr(other, attribute_name, None):
                return False

        return dict.__eq__(cast("Dict[Any, Any]", self), other)

    def __getattr__(self, name):
        try:
            return self.__getattribute__(name)
        except AttributeError as e:
            # This part is responsible for _add_holiday_* syntactic sugar support.
            add_holiday_prefix = "_add_holiday_"
            # Raise early if prefix doesn't match to avoid patterns checks.
            if name[: len(add_holiday_prefix)] != add_holiday_prefix:
                raise e

            tokens = name.split("_")

            # Handle <month> <day> patterns (e.g., _add_holiday_jun_15()).
            if len(tokens) == 5:
                *_, month, day = tokens
                if month in MONTHS and day in DAYS:
                    return lambda name: self._add_holiday(
                        name,
                        date(self._year, MONTHS[month], int(day)),
                    )

            elif len(tokens) == 7:
                # Handle <last/nth> <weekday> of <month> patterns (e.g.,
                # _add_holiday_last_mon_of_aug() or _add_holiday_3rd_fri_of_aug()).
                *_, number, weekday, of, month = tokens
                if (
                    of == "of"
                    and (number == "last" or number[0].isdigit())
                    and month in MONTHS
                    and weekday in WEEKDAYS
                ):
                    return lambda name: self._add_holiday(
                        name,
                        _get_nth_weekday_of_month(
                            -1 if number == "last" else int(number[0]),
                            WEEKDAYS[weekday],
                            MONTHS[month],
                            self._year,
                        ),
                    )

                # Handle <n> days <past/prior> easter patterns (e.g.,
                # _add_holiday_8_days_past_easter() or
                # _add_holiday_5_days_prior_easter()).
                *_, days, unit, delta_direction, easter = tokens
                if (
                    unit in {"day", "days"}
                    and delta_direction in {"past", "prior"}
                    and easter == "easter"
                    and len(days) < 3
                    and days.isdigit()
                ):
                    return lambda name: self._add_holiday(
                        name,
                        _timedelta(
                            self._easter_sunday,
                            +int(days) if delta_direction == "past" else -int(days),
                        ),
                    )

            # Handle <n> day(s) <past/prior> <last/<nth> <weekday> of <month> patterns (e.g.,
            # _add_holiday_1_day_past_1st_fri_of_aug() or
            # _add_holiday_5_days_prior_last_fri_of_aug()).
            elif len(tokens) == 10:
                *_, days, unit, delta_direction, number, weekday, of, month = tokens
                if (
                    unit in {"day", "days"}
                    and delta_direction in {"past", "prior"}
                    and of == "of"
                    and len(days) < 3
                    and days.isdigit()
                    and (number == "last" or number[0].isdigit())
                    and month in MONTHS
                    and weekday in WEEKDAYS
                ):
                    return lambda name: self._add_holiday(
                        name,
                        _timedelta(
                            _get_nth_weekday_of_month(
                                -1 if number == "last" else int(number[0]),
                                WEEKDAYS[weekday],
                                MONTHS[month],
                                self._year,
                            ),
                            +int(days) if delta_direction == "past" else -int(days),
                        ),
                    )

            # Handle <nth> <weekday> <before/from> <month> <day> patterns (e.g.,
            # _add_holiday_1st_mon_before_jun_15() or _add_holiday_1st_mon_from_jun_15()).
            elif len(tokens) == 8:
                *_, number, weekday, date_direction, month, day = tokens
                if (
                    date_direction in {"before", "from"}
                    and number[0].isdigit()
                    and month in MONTHS
                    and weekday in WEEKDAYS
                    and day in DAYS
                ):
                    return lambda name: self._add_holiday(
                        name,
                        _get_nth_weekday_from(
                            -int(number[0]) if date_direction == "before" else +int(number[0]),
                            WEEKDAYS[weekday],
                            date(self._year, MONTHS[month], int(day)),
                        ),
                    )

            raise e  # No match.

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
                raise TypeError(f"Cannot convert type '{type(key.step)}' to int.")

            if step == 0:
                raise ValueError("Step value must not be zero.")

            date_diff = stop - start
            if date_diff.days < 0 <= step or date_diff.days >= 0 > step:
                step *= -1

            days_in_range = []
            for delta_days in range(0, date_diff.days, step):
                day = _timedelta(start, delta_days)
                if day in self:
                    days_in_range.append(day)

            return days_in_range

        return dict.__getitem__(self, self.__keytransform__(key))

    def __keytransform__(self, key: DateLike) -> date:
        """Transforms the date from one of the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp

        to :class:`datetime.date`, which is how it's stored by the class."""

        # Try to catch `date` and `str` type keys first.
        # Using type() here to skip date subclasses.
        # Key is `date`.
        if type(key) is date:
            dt = key

        # Key is `str` instance.
        elif isinstance(key, str):
            try:
                dt = parse(key).date()
            except (OverflowError, ValueError):
                raise ValueError(f"Cannot parse date from string '{key}'")

        # Key is `datetime` instance.
        elif isinstance(key, datetime):
            dt = key.date()

        # Must go after the `isinstance(key, datetime)` check as datetime is `date` subclass.
        elif isinstance(key, date):
            dt = key

        # Key is `float` or `int` instance.
        elif isinstance(key, (float, int)):
            dt = datetime.fromtimestamp(key, timezone.utc).date()

        # Key is not supported.
        else:
            raise TypeError(f"Cannot convert type '{type(key)}' to date.")

        # Automatically expand for `expand=True` cases.
        if self.expand and dt.year not in self.years:
            self.years.add(dt.year)
            self._populate(dt.year)

        return dt

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, HolidayBase):
            return True

        for attribute_name in self.__attribute_names:
            if getattr(self, attribute_name, None) != getattr(other, attribute_name, None):
                return True

        return dict.__ne__(self, other)

    def __radd__(self, other: Any) -> "HolidayBase":
        return self.__add__(other)

    def __reduce__(self) -> Union[str, Tuple[Any, ...]]:
        return super().__reduce__()

    def __repr__(self) -> str:
        if self:
            return super().__repr__()

        parts = []
        if hasattr(self, "market"):
            parts.append(f"holidays.entities.iso_10383_holidays({self.market!r}")
            parts.append(")")
        elif hasattr(self, "country"):
            parts.append(f"holidays.iso_3166_holidays({self.country!r}")
            if self.subdiv:
                parts.append(f", subdiv={self.subdiv!r}")
            parts.append(")")
        else:
            parts.append("holidays.HolidayBase()")

        return "".join(parts)

    def __setattr__(self, key: str, value: Any) -> None:
        dict.__setattr__(self, key, value)

        if self and key in {"categories", "observed"}:
            self.clear()
            for year in self.years:  # Re-populate holidays for each year.
                self._populate(year)

    def __setitem__(self, key: DateLike, value: str) -> None:
        if key in self:
            # If there are multiple holidays on the same date
            # order their names alphabetically.
            holiday_names = set(self[key].split(HOLIDAY_NAME_DELIMITER))
            holiday_names.update(value.split(HOLIDAY_NAME_DELIMITER))
            value = HOLIDAY_NAME_DELIMITER.join(sorted(holiday_names))

        dict.__setitem__(self, self.__keytransform__(key), value)

    def __str__(self) -> str:
        if self:
            return super().__str__()

        parts = (
            f"'{attribute_name}': {getattr(self, attribute_name, None)}"
            for attribute_name in self.__attribute_names
        )

        return f"{{{', '.join(parts)}}}"

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

    @cached_property
    def _entity_code(self):
        return getattr(self, "country", getattr(self, "market", None))

    @cached_property
    def _normalized_subdiv(self):
        return (
            self.subdivisions_aliases.get(self.subdiv, self.subdiv)
            .translate(
                str.maketrans(
                    {
                        "-": "_",
                        " ": "_",
                    }
                )
            )
            .lower()
        )

    @property
    def _sorted_categories(self):
        return (
            [self.default_category] + sorted(self.categories - {self.default_category})
            if self.default_category in self.categories
            else sorted(self.categories)
        )

    @classmethod
    def get_subdivision_aliases(cls) -> Dict[str, List]:
        """Get subdivision aliases."""
        subdivision_aliases: Dict[str, List[str]] = {s: [] for s in cls.subdivisions}
        for alias, subdivision in cls.subdivisions_aliases.items():
            subdivision_aliases[subdivision].append(alias)

        return subdivision_aliases

    def _is_leap_year(self) -> bool:
        """
        Returns True if the year is leap. Returns False otherwise.
        """
        return isleap(self._year)

    def _add_holiday(self, name: str, *args) -> Optional[date]:
        """Add a holiday."""
        if not args:
            raise TypeError("Incorrect number of arguments.")

        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)

        if dt.year != self._year:
            return None

        self[dt] = self.tr(name)
        return dt

    def _add_special_holidays(self, mapping_names, observed=False):
        """Add special holidays."""
        for mapping_name in mapping_names:
            for data in _normalize_tuple(getattr(self, mapping_name, {}).get(self._year, ())):
                if len(data) == 3:  # Special holidays.
                    month, day, name = data
                    self._add_holiday(
                        self.tr(self.observed_label) % self.tr(name)
                        if observed
                        else self.tr(name),
                        month,
                        day,
                    )
                else:  # Substituted holidays.
                    to_month, to_day, from_month, from_day, *optional = data
                    from_date = date(optional[0] if optional else self._year, from_month, from_day)
                    self._add_holiday(
                        self.tr(self.substituted_label)
                        % from_date.strftime(self.tr(self.substituted_date_format)),
                        to_month,
                        to_day,
                    )
                    self.weekend_workdays.add(from_date)

    def _check_weekday(self, weekday: int, *args) -> bool:
        """
        Returns True if `weekday` equals to the date's week day.
        Returns False otherwise.
        """
        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)
        return dt.weekday() == weekday

    def _is_monday(self, *args) -> bool:
        return self._check_weekday(MON, *args)

    def _is_tuesday(self, *args) -> bool:
        return self._check_weekday(TUE, *args)

    def _is_wednesday(self, *args) -> bool:
        return self._check_weekday(WED, *args)

    def _is_thursday(self, *args) -> bool:
        return self._check_weekday(THU, *args)

    def _is_friday(self, *args) -> bool:
        return self._check_weekday(FRI, *args)

    def _is_saturday(self, *args) -> bool:
        return self._check_weekday(SAT, *args)

    def _is_sunday(self, *args) -> bool:
        return self._check_weekday(SUN, *args)

    def _is_weekend(self, *args):
        """
        Returns True if date's week day is a weekend day.
        Returns False otherwise.
        """
        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)
        return dt.weekday() in self.weekend

    def _populate(self, year: int) -> None:
        """This is a private class that populates (generates and adds) holidays
        for a given year. To keep things fast, it assumes that no holidays for
        the year have already been populated. It is required to be called
        internally by any country populate() method, while should not be called
        directly from outside.
        To add holidays to an object, use the update() method.

        :param year:
            The year to populate with holidays.

        >>> from holidays import iso_3166_holidays
        >>> us_holidays = iso_3166_holidays('US', years=2020)
        # to add new holidays to the object:
        >>> us_holidays.update(iso_3166_holidays('US', years=2021))
        """

        self._year = year
        self._populate_common_holidays()
        self._populate_subdiv_holidays()

    def _populate_common_holidays(self):
        """Populate entity common holidays."""
        for category in self._sorted_categories:
            if pch_method := getattr(self, f"_populate_{category.lower()}_holidays", None):
                pch_method()

        if self.has_special_holidays:
            self._add_special_holidays(
                f"special_{category}_holidays" for category in self._sorted_categories
            )

    def _populate_subdiv_holidays(self):
        """Populate entity subdivision holidays."""
        if self.subdiv is None:
            return None

        for category in self._sorted_categories:
            if asch_method := getattr(
                self,
                f"_populate_subdiv_{self._normalized_subdiv}_{category.lower()}_holidays",
                None,
            ):
                asch_method()

        if self.has_special_holidays:
            self._add_special_holidays(
                f"special_{self._normalized_subdiv}_{category.lower()}_holidays"
                for category in self._sorted_categories
            )

    def append(self, *args: Union[Dict[DateLike, str], List[DateLike], DateLike]) -> None:
        """Alias for :meth:`update` to mimic list type."""
        return self.update(*args)

    def copy(self):
        """Return a copy of the object."""
        return copy.copy(self)

    def get(self, key: DateLike, default: Union[str, Any] = None) -> Union[str, Any]:
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
        return dict.get(self, self.__keytransform__(key), default)

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
        return [name for name in self.get(key, "").split(HOLIDAY_NAME_DELIMITER) if name]

    def get_named(
        self, holiday_name: str, lookup="icontains", split_multiple_names=True
    ) -> List[date]:
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
        :param split_multiple_names:
            Either use the exact name for each date or split it by holiday
            name delimiter.

        :return:
            A list of all holiday dates matching the provided holiday name.
        """
        holiday_name_dates = (
            ((k, name) for k, v in self.items() for name in v.split(HOLIDAY_NAME_DELIMITER))
            if split_multiple_names
            else ((k, v) for k, v in self.items())
        )

        if lookup == "icontains":
            holiday_name_lower = holiday_name.lower()
            return [dt for dt, name in holiday_name_dates if holiday_name_lower in name.lower()]
        elif lookup == "exact":
            return [dt for dt, name in holiday_name_dates if holiday_name == name]
        elif lookup == "contains":
            return [dt for dt, name in holiday_name_dates if holiday_name in name]
        elif lookup == "startswith":
            return [
                dt for dt, name in holiday_name_dates if holiday_name == name[: len(holiday_name)]
            ]
        elif lookup == "iexact":
            holiday_name_lower = holiday_name.lower()
            return [dt for dt, name in holiday_name_dates if holiday_name_lower == name.lower()]
        elif lookup == "istartswith":
            holiday_name_lower = holiday_name.lower()
            return [
                dt
                for dt, name in holiday_name_dates
                if holiday_name_lower == name[: len(holiday_name)].lower()
            ]

        raise AttributeError(f"Unknown lookup type: {lookup}")

    def get_nth_workday(self, key: DateLike, n: int) -> date:
        """Return n-th working day from provided date (if n is positive)
        or n-th working day before provided date (if n is negative).
        """
        direction = +1 if n > 0 else -1
        dt = self.__keytransform__(key)
        for _ in range(abs(n)):
            dt = _timedelta(dt, direction)
            while not self.is_workday(dt):
                dt = _timedelta(dt, direction)
        return dt

    def get_workdays_number(self, key1: DateLike, key2: DateLike) -> int:
        """Return the number of working days between two dates (not including the start date)."""
        dt1 = self.__keytransform__(key1)
        dt2 = self.__keytransform__(key2)
        if dt1 == dt2:
            return 0
        if dt1 > dt2:
            dt1, dt2 = dt2, dt1

        return sum(self.is_workday(_timedelta(dt1, n)) for n in range(1, (dt2 - dt1).days + 1))

    def is_workday(self, key: DateLike) -> bool:
        """Return True if date is a working day (not a holiday or a weekend)."""
        dt = self.__keytransform__(key)
        return dt in self.weekend_workdays if self._is_weekend(dt) else dt not in self

    def pop(self, key: DateLike, default: Union[str, Any] = None) -> Union[str, Any]:
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
        use_exact_name = HOLIDAY_NAME_DELIMITER in name
        dts = self.get_named(name, split_multiple_names=not use_exact_name)
        if len(dts) == 0:
            raise KeyError(name)

        popped = []
        for dt in dts:
            holiday_names = self[dt].split(HOLIDAY_NAME_DELIMITER)
            self.pop(dt)
            popped.append(dt)

            # Keep the rest of holidays falling on the same date.
            if not use_exact_name:
                name_lower = name.lower()
                holiday_names = [
                    holiday_name
                    for holiday_name in holiday_names
                    if name_lower not in holiday_name.lower()
                ]

                if len(holiday_names) > 0:
                    self[dt] = HOLIDAY_NAME_DELIMITER.join(holiday_names)

        return popped

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
        self, h1: Union[HolidayBase, "HolidaySum"], h2: Union[HolidayBase, "HolidaySum"]
    ) -> None:
        """
        :param h1:
            The first HolidayBase object to add.

        :param h2:
            The other HolidayBase object to add.

        Example:

        >>> from holidays import iso_3166_holidays
        >>> nafta_holidays = iso_3166_holidays('US', years=2020) + \
iso_3166_holidays('CA') + iso_3166_holidays('MX')
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
