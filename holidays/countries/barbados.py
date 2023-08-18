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

from holidays.calendars.gregorian import JUL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Barbados(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Barbados
    https://www.timeanddate.com/holidays/barbados/
    """

    country = "BB"

    special_holidays = {
        # One off 50th Anniversary of CARICOM Holiday.
        # See https://tinyurl.com/brbhol
        2023: (JUL, 31, "50th Anniversary of CARICOM Holiday")
    }

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Errol Barrow Day
        self._add_holiday_jan_21("Errol Barrow Day")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # National Heroes Day
        self._add_holiday_apr_28("National Heroes Day")

        # May Day
        self._add_labor_day("May Day")

        # Whit Monday
        self._add_whit_monday("Whit Monday")

        # Emancipation Day
        self._add_holiday_aug_1("Emancipation Day")

        # Kadooment Day
        self._add_holiday_1st_mon_of_aug("Kadooment Day")

        # Independence Day
        self._add_holiday_nov_30("Independence Day")

        # Christmas
        self._add_christmas_day("Christmas Day")

        # Boxing Day
        self._add_christmas_day_two("Boxing Day")


class BB(Barbados):
    pass


class BRB(Barbados):
    pass
