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


class BaseError(Exception):
    """Base exception."""


class CalendarError(BaseError):
    """Calendar not recognized exception."""


class InvalidDateError(BaseError):
    """Invalid date type or format exception."""


class EntityDoesNotExist(BaseError):
    """Entity not supported exception."""


class CountryDoesNotExist(EntityDoesNotExist):
    """Country not supported exception."""


class FinancialDoesNotExist(EntityDoesNotExist):
    """Financial not supported exception."""


class SubdivisionDoesNotExist(BaseError):
    """Subdivision not supported exception."""


class YearOutOfRangeError(BaseError):
    """Year out of range error."""
