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

from holidays.calendars.gregorian import DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class EuropeanCentralBank(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
        - https://en.wikipedia.org/wiki/TARGET2
        - https://www.ecb.europa.eu/press/pr/date/1999/html/pr990715_1.en.html
        - https://www.ecb.europa.eu/press/pr/date/2000/html/pr001214_4.en.html
    """

    market = "ECB"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, EuropeanCentralBankStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1999:
            return None
        super()._populate(year)

        self._add_new_years_day("New Year's Day")

        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")

        self._add_labor_day("1 May (Labour Day)")

        self._add_christmas_day("Christmas Day")
        self._add_christmas_day_two("26 December")


class ECB(EuropeanCentralBank):
    pass


class TAR(EuropeanCentralBank):
    pass


class EuropeanCentralBankStaticHolidays:
    special_public_holidays = {
        2000: (DEC, 31, "Additional closing day"),
    }
