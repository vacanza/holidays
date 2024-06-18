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

from datetime import date, datetime, timezone

from dateutil.parser import parse

from holidays.types import DateLike


def _convert_to_date(dt: DateLike) -> date:
    """Convert value to date.

    :param dt:
        A value that should be converted into a date.

    :return:
        A date created based on the provided value.
    """

    # Attempt to catch `date` and `str` type keys first.
    # Using `type()`` instead of `isinstance()` here to skip date subclasses.
    # Key is `date`.
    if type(dt) is date:
        return dt

    # Key is `str` instance.
    elif isinstance(dt, str):
        try:
            return parse(dt).date()
        except (OverflowError, ValueError):
            raise ValueError(f"Cannot parse date from string '{dt}'")

    # Key is `datetime` instance.
    elif isinstance(dt, datetime):
        return dt.date()

    # Must go after the `isinstance(key, datetime)` check as datetime is `date` subclass.
    elif isinstance(dt, date):
        return dt

    # Key is `float` or `int` instance.
    elif isinstance(dt, (float, int)):
        return datetime.fromtimestamp(dt, timezone.utc).date()

    # Key is not supported.
    else:
        raise TypeError(f"Cannot convert type '{type(dt)}' to date.")


def _normalize_arguments(cls, value):
    """Normalize arguments.

    :param cls:
        A type of arguments to normalize.

    :param value:
        Either a single item or an iterable of `cls` type.

    :return:
        A set created from `value` argument.

    """
    if value is None:
        return set()

    if isinstance(value, cls):
        return {value}

    try:
        return {v if isinstance(v, cls) else cls(v) for v in value}
    except TypeError:  # non-iterable
        return {value if isinstance(value, cls) else cls(value)}


def _normalize_tuple(value):
    """Normalize tuple.

    :param data:
        Either a tuple or a tuple of tuples.

    :return:
        An unchanged object for tuple of tuples, e.g., ((JAN, 10), (DEC, 31)).
        An object put into a tuple otherwise, e.g., ((JAN, 10),).
    """
    return value if not value or isinstance(value[0], tuple) else (value,)
