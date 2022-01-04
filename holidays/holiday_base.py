# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import timedelta, datetime, date
from typing import Any, Iterable, List, Optional, Tuple, Union

from dateutil.parser import parse


class HolidayBase(dict):
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
    holidays. To prepopulate holidays, instantiate the class with the years
    argument:

    us_holidays = holidays.US(years=2020)


    Example usage:

    >>> from datetime import date
    >>> import holidays

    ISO 3166‑1 Alpha 2 code:

    >>> us_holidays = holidays.US()

    or:

    >>> us_holidays = holidays.UnitedStates()

    or:

    >>> us_holidays = holidays.CountryHoliday('US')

    or, for specific prov / states:

    >>> us_holidays = holidays.CountryHoliday('US', prov=None, state='CA')

    The below will cause 2015 holidays to be calculated:

    >>> assert date(2015, 1, 1) in us_holidays

    This will be faster because 2015 holidays are already calculated:

    >>> assert date(2015, 1, 2) not in us_holidays

    The Holiday class will also recognize strings of any format and int/float
    representing a Unix timestamp:

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

    >>> us_holidays = holidays.US(years=2020)
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

    >>> us_pr_holidays = holidays.US(state='PR')
    >>> assert '2018-01-06' not in us_holidays
    >>> assert '2018-01-06' in us_pr_holidays


    Easily create custom Holiday objects with your own dates instead
    of using the pre-defined countries/states/provinces available:

    >>> custom_holidays = holidays.HolidayBase()

    Append custom holiday dates by passing
    (1) a dict with date/name key/value pairs,
    (2) a list of dates (in any format: date, datetime, string, integer)
    ("Holiday" will be used as a description),
    (3) a single date item ("Holiday" will be used as a description):

    >>> custom_holidays.append({'2015-01-01': "New Year's Day"})
    >>> custom_holidays.append(['2015-07-01', '07/04/2015'])
    >>> custom_holidays.append(date(2015, 12, 25))
    >>> assert date(2015, 1, 1) in custom_holidays
    >>> assert date(2015, 1, 2) not in custom_holidays
    >>> assert '12/25/2015' in custom_holidays

    For more complex logic, like 4th Monday of January, you can inherit the
    HolidayBase class and define your own _populate(year) method. See
    documentation for examples.

    """

    country: str

    def __init__(
        self,
        years: Union[int, Iterable[int]] = None,
        expand: bool = True,
        observed: bool = True,
        prov: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        """
        To maximize speed, by default the list of holidays is built as needed
        on the fly, one calendar year at a time. When you instantiate the
        object, it is empty, but the moment you try to read a key it will build
        that year's list of holidays. To prepopulate holiday date, instantiate
        the class with the `years` parameter.

        :param years: The year(s) to pre-calculate holidays for at
           instantiation.
        :param expand: If True (default), the entire year is added when one
           date is requested.
        :param observed: If True (default), include the day when the holiday
           is observed (e.g. a holiday falling on a Sunday being observed the
           following Monday (this doesn't work for all countries).
        :param prov: The Province (see documentation of what is supported; not
           implemented for all countries).
        :param state: The State (see documentation for what is supported; not
           implemented for all countries).
        :return: None.
        """
        super().__init__()
        self.observed = observed
        self.expand = expand
        if isinstance(years, int):
            years = [years]
        self.years = set(years) if years is not None else set()
        if not getattr(self, "prov", False):
            self.prov = prov
        self.state = state
        for year in self.years.copy():
            self._populate(year)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "observed" and len(self) > 0:
            dict.__setattr__(self, key, value)
            if value is True:
                # Add (Observed) dates
                years = list(self.years)
                self.years = set()
                self.clear()
                for year in years:
                    self._populate(year)
            else:
                # Remove (Observed) dates
                for k, v in list(self.items()):
                    if v.find("Observed") >= 0:
                        del self[k]
        else:
            return dict.__setattr__(self, key, value)

    def __keytransform__(self, key: Union[datetime, date, float, str]) -> date:
        """Transforms the date from one of datetime.datetime or datetime.date
        types, Unix timestamp in float type or string to datetime.date, which
        is how it's stored by the class."""
        if isinstance(key, datetime):
            key = key.date()
        elif isinstance(key, date):
            key = key
        elif isinstance(key, int) or isinstance(key, float):
            key = datetime.utcfromtimestamp(key).date()
        elif isinstance(key, str):
            try:
                key = parse(key).date()
            except (ValueError, OverflowError):
                raise ValueError("Cannot parse date from string '%s'" % key)
        else:
            raise TypeError("Cannot convert type '%s' to date." % type(key))

        if self.expand and key.year not in self.years:
            self.years.add(key.year)
            self._populate(key.year)
        return key

    def __contains__(self, key: Union[datetime, date, float, str]) -> bool:
        """Return true if date is in self, false otherwise. Accepts a date in
        datetime.datetime or datetime.date types, as a Unix timestamp in float
        type or a string)."""
        return dict.__contains__(self, self.__keytransform__(key))

    def __getitem__(
        self,
        key: Union[
            datetime,
            date,
            int,
            str,
            Iterable[Union[datetime, date, float, str]],
        ],
    ) -> Union[str, List[str], List[date], bool]:
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
                    "Cannot convert type '%s' to int." % type(key.step)
                )

            if step == 0:
                raise ValueError("Step value must not be zero.")

            date_diff = stop - start
            if date_diff.days < 0 <= step or date_diff.days >= 0 > step:
                step *= -1

            days_in_range = []
            for delta_days in range(0, date_diff.days, step):
                day = start + timedelta(days=delta_days)
                try:
                    self.__getitem__(day)
                    days_in_range.append(day)
                except KeyError:
                    pass
            return days_in_range
        return dict.__getitem__(self, self.__keytransform__(key))

    def __setitem__(
        self, key: Union[datetime, date, float, str], value
    ) -> None:
        if key in self:
            if self.get(key).find(value) < 0 and value.find(self.get(key)) < 0:
                value = "%s, %s" % (value, self.get(key))
            else:
                value = self.get(key)
        return dict.__setitem__(self, self.__keytransform__(key), value)

    def update(self, *args) -> None:
        """Update the Holidays object, overwriting existing dates. Return None.

        update() accepts either another dictionary object or an iterable of
        key/value pairs (as tuples or other iterables of length two) like
        dict.update() but also a single date or a list of dates, for which the
        value will be set to "Holiday"."""
        args = list(args)
        for arg in args:
            if isinstance(arg, dict):
                for key, value in list(arg.items()):
                    self[key] = value
            elif isinstance(arg, list):
                for item in arg:
                    self[item] = "Holiday"
            else:
                self[arg] = "Holiday"

    def append(self, *args) -> None:
        """Alias for update() to mimic list type."""
        return self.update(*args)

    def get(
        self,
        key: Union[datetime, date, float, str],
        default: Optional[Any] = None,
    ) -> str:
        """Return the holiday name for a date (in datetime.datetime or
        datetime.date types, as a Unix timestamp in float type or a string) if
        date is a holiday, else default. If default is not given, it defaults
        to None, so that this method never raises a KeyError.  If more than one
        holiday is present, they are separated by a comma."""
        return dict.get(self, self.__keytransform__(key), default)

    def get_list(self, key: Union[datetime, date, float, str]) -> List[str]:
        """Return a list of all holiday names for a date (in datetime.datetime
        or datetime.date types, as a Unix timestamp in float type or a string)
        if date is a holiday, else default. If default is not given, it
        defaults to None, so that this method never raises a KeyError."""
        return [h for h in self.get(key, "").split(", ") if h]

    def get_named(self, name: str) -> List[date]:
        """Return a list of all holiday dates matching the provided holiday
        name. The match will be made case insensitively and partial matches
        will be included."""
        original_expand = self.expand
        self.expand = False
        matches = [
            key for key in self if name.lower() in str(self[key]).lower()
        ]
        self.expand = original_expand
        return matches

    def pop(
        self,
        key: Union[datetime, date, float, str],
        default: Optional[Any] = None,
    ) -> Union[str, List[str], List[date], bool]:
        """If date (in datetime.datetime or datetime.date types, as a Unix
        timestamp in float type or a string) is a holiday, remove it (no longer
        treat it as a holiday) and return its date, else return default. If
        default is not given and date is not a holiday, a KeyError is
        raised."""
        if default is None:
            return dict.pop(self, self.__keytransform__(key))
        return dict.pop(self, self.__keytransform__(key), default)

    def pop_named(self, name: str) -> List[date]:
        """Remove (no longer treat at as holiday) all dates matching the
        provided holiday name. The match will be made case insensitively and
        partial matches will be removed. If default is not given and date is
        not a holiday, a KeyError is raised."""
        to_pop = self.get_named(name)
        if not to_pop:
            raise KeyError(name)
        for key in to_pop:
            self.pop(key)
        return to_pop

    def __eq__(self, other: object) -> bool:
        return dict.__eq__(self, other) and self.__dict__ == other.__dict__

    def __ne__(self, other: dict) -> bool:
        return dict.__ne__(self, other) or self.__dict__ != other.__dict__

    def __add__(
        self, other: Union[int, "HolidayBase", "HolidaySum"]
    ) -> Union["HolidayBase", "HolidaySum"]:
        """Add two Holiday together creating a HolidaySum object."""
        if isinstance(other, int) and other == 0:
            # Required to sum() list of holidays
            # sum([h1, h2]) is equivalent to (0 + h1 + h2)
            return self
        elif not isinstance(other, (HolidayBase, HolidaySum)):
            raise TypeError(
                "Holiday objects can only be added with other Holiday objects"
            )
        return HolidaySum(self, other)

    def __radd__(self, other: Any) -> "HolidaySum":
        return self.__add__(other)

    def _populate(self, year: int) -> None:
        pass

    def __reduce__(self) -> Union[str, Tuple[Any, ...]]:
        return super(HolidayBase, self).__reduce__()

    def __repr__(self):
        if len(self) == 0:
            _repr = f"holidays.CountryHoliday({self.country!r}"
            if self.prov:
                _repr += f", prov={self.prov!r}"
            if self.state:
                _repr += f", state={self.state!r}"
            _repr += ")"
            return _repr
        return super(HolidayBase, self).__repr__()

    def __str__(self):
        if len(self) == 0:
            return str(self.__dict__)
        return super(HolidayBase, self).__str__()


class HolidaySum(HolidayBase):
    country: Union[str, List[str]]
    prov: Optional[Union[str, List[str]]]
    state: Optional[Union[str, List[str]]]
    holidays: List[HolidayBase]

    def __init__(
        self,
        h1: Union[HolidayBase, "HolidaySum"],
        h2: Union[HolidayBase, "HolidaySum"],
    ) -> None:
        """
        Class containing holidays that have been generated through adding
        individual holidays. The original holidays are kept in the attribute
        'holidays' as a list, and `country`, `prov` and `state` attributes are
        added together and could be lists. Holiday names, when different, are
        merged.  All years are expanded for all operands.

        :param h1: The first Holiday object to add
        :param h2: The other Holiday object to add

        Example:

        >>> from pprint import pprint
        >>> import holidays
        >>> nafta_holidays = holidays.US(years=2020) + holidays.CA() \
        ...     + holidays.MX()
        >>> dates = sorted(nafta_holidays.items(), key=lambda x: x[0])
        >>> pprint(dates[:10], width=72)
        [(datetime.date(2020, 1, 1), "Año Nuevo [New Year's Day]"),
         (datetime.date(2020, 1, 20), 'Martin Luther King Jr. Day'),
         (datetime.date(2020, 2, 3),
          'Día de la Constitución [Constitution Day] (Observed)'),
         (datetime.date(2020, 2, 5),
          'Día de la Constitución [Constitution Day]'),
         (datetime.date(2020, 2, 17), "Washington's Birthday, Family Day"),
         (datetime.date(2020, 3, 16),
          "Natalicio de Benito Juárez [Benito Juárez's birthday] (Observed)"),
         (datetime.date(2020, 3, 21),
          "Natalicio de Benito Juárez [Benito Juárez's birthday]"),
         (datetime.date(2020, 4, 10), 'Good Friday'),
         (datetime.date(2020, 5, 1), 'Día del Trabajo [Labour Day]'),
         (datetime.date(2020, 5, 18), 'Victoria Day')]
        """
        # store originals in the holidays attribute
        self.holidays = []
        for operand in (h1, h2):
            if isinstance(operand, HolidaySum):
                for h in operand.holidays:
                    self.holidays.append(h)
            else:
                self.holidays.append(operand)
        kwargs = {}
        # join years, expand and observed
        kwargs["years"] = h1.years | h2.years
        kwargs["expand"] = h1.expand or h2.expand
        kwargs["observed"] = h1.observed or h2.observed
        # join country and subdivisions data
        for attr in ("country", "prov", "state"):
            if (
                getattr(h1, attr)
                and getattr(h2, attr)
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
                kwargs[attr] = a1 + a2
            else:
                kwargs[attr] = getattr(h1, attr, None) or getattr(
                    h2, attr, None
                )
        self.country = kwargs.pop("country")

        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year: int) -> None:
        for h in self.holidays[::-1]:
            h._populate(year)
            self.update(h)
