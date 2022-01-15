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
from typing import Any, Iterable, List, Optional, TYPE_CHECKING, Tuple, Union

from dateutil.parser import parse

if TYPE_CHECKING:
    from holidays.utils import country_holidays  # required by docstring


class HolidayBase(dict):
    """
    The base class for a new dictionary containing the public holidays.

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
    # For specific prov / state:
    >>> calif_holidays = country_holidays('US', prov=None, state='CA')

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

    >>> us_pr_holidays = country_holidays('US', state='PR')
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

    For more complex logic, like 4th Monday of January, you can inherit the
    :class:`HolidayBase` class and define your own :meth:`_populate` method.
    See documentation for examples.
    """

    country: str
    """The country's ISO 3166-1 alpha-2 code."""

    def __init__(
        self,
        years: Union[int, Iterable[int]] = None,
        expand: bool = True,
        observed: bool = True,
        prov: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        """
        :param years:
            The year(s) to pre-calculate public holidays for at instantiation.

        :param prov:
            The Province (not implemented for all countries; see
            documentation).

        :param state:
            The State (not implemented for all countries; see documentation).

        :param expand:
            Whether the entire year is calculated when one date from that year
            is requested.

        :param observed:
            Whether to include the dates when public holiday are observed
            (e.g. a holiday falling on a Sunday being observed the
            following Monday). This doesn't work for all countries.

        :return:
            A :class:`HolidayBase` object matching the **country**.
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

    def __keytransform__(self, key: Union[date, datetime, str, float]) -> date:
        """Transforms the date from one of the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp

        to :class:`datetime.date`, which is how it's stored by the class."""
        if isinstance(key, datetime):
            out_key = key.date()
        elif isinstance(key, date):
            out_key = key
        elif isinstance(key, int) or isinstance(key, float):
            out_key = datetime.utcfromtimestamp(key).date()
        elif isinstance(key, str):
            try:
                out_key = parse(key).date()
            except (ValueError, OverflowError):
                raise ValueError("Cannot parse date from string '%s'" % key)
        else:
            raise TypeError("Cannot convert type '%s' to date." % type(key))

        if self.expand and out_key.year not in self.years:
            self.years.add(out_key.year)
            self._populate(out_key.year)
        return out_key

    def __contains__(self, key: Union[date, datetime, str, float]) -> bool:
        """Return true if date is in self, false otherwise. Accepts a date in
        the following types:

        * :class:`datetime.date`,
        * :class:`datetime.datetime`,
        * a :class:`str` of any format recognized by
          :func:`dateutil.parser.parse`,
        * or a :class:`float` or :class:`int` representing a POSIX timestamp.
        """
        return dict.__contains__(self, self.__keytransform__(key))

    def __getitem__(
        self,
        key: Union[
            date,
            datetime,
            str,
            float,
            Iterable[Union[date, datetime, str, float]],
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
        self, key: Union[date, datetime, str, float], value
    ) -> None:
        if key in self:
            if self.get(key).find(value) < 0 and value.find(self.get(key)) < 0:
                value = "%s, %s" % (value, self.get(key))
            else:
                value = self.get(key)
        return dict.__setitem__(self, self.__keytransform__(key), value)

    def update(self, *args) -> None:
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
        args_list = list(args)
        for arg in args_list:
            if isinstance(arg, dict):
                for key, value in list(arg.items()):
                    self[key] = value
            elif isinstance(arg, list):
                for item in arg:
                    self[item] = "Holiday"
            else:
                self[arg] = "Holiday"

    def append(self, *args) -> None:
        """Alias for :meth:`update` to mimic list type."""
        return self.update(*args)

    def get(
        self,
        key: Union[date, datetime, str, float],
        default: Optional[Any] = None,
    ) -> str:
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

    def get_list(self, key: Union[date, datetime, str, float]) -> List[str]:
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
        return [h for h in self.get(key, "").split(", ") if h]

    def get_named(self, name: str) -> List[date]:
        """Return a list of all holiday dates matching the provided holiday
        name. The match will be made case insensitively and partial matches
        will be included.

        :param name:
            The holiday's name to try to match.

        :return:
            A list of all holiday dates matching the provided holiday name.
        """
        original_expand = self.expand
        self.expand = False
        matches = [
            key for key in self if name.lower() in str(self[key]).lower()
        ]
        self.expand = original_expand
        return matches

    def pop(
        self,
        key: Union[date, datetime, str, float],
        default: Optional[Any] = None,
    ) -> Union[str, List[str], List[date], bool]:
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
    ) -> "HolidaySum":
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
            # sum([h1, h2]) is equivalent to (0 + h1 + h2)
            return self  # TODO understand why this is necessary (typing issue)
        elif not isinstance(other, (HolidayBase, HolidaySum)):
            raise TypeError(
                "Holiday objects can only be added with other Holiday objects"
            )
        return HolidaySum(self, other)

    def __radd__(self, other: Any) -> "HolidaySum":
        return self.__add__(other)

    def __pos__(self):
        """Enables type checking for the unary operator + (e.g. a + b instead of
        a.__add__(b))."""
        pass

    def _populate(self, year: int) -> None:
        """meta: public"""
        pass

    def __reduce__(self) -> Union[str, Tuple[Any, ...]]:
        return super(HolidayBase, self).__reduce__()

    def __repr__(self):
        if len(self) == 0:
            _repr = f"holidays.Holidays({self.country!r}"
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
    """
    Returns a :class:`dict`-like object resulting from the addition of two or
    more individual dictionaries of public holidays. The original dictionaries
    are available as a :class:`list` in the attribute :attr:`holidays,` and
    :attr:`country`, :attr:`prov` and :attr:`state` attributes are added
    together and could become :class:`list` s. Holiday names, when different,
    are merged. All years are calculated (expanded) for all operands.
    """

    country: Union[str, List[str]]
    """Countries included in the addition."""
    prov: Optional[Union[str, List[str]]]
    """Provinces included in the addition."""
    state: Optional[Union[str, List[str]]]
    """States included in the addition."""
    holidays: List[HolidayBase]
    """The original HolidayBase objects included in the addition."""

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
