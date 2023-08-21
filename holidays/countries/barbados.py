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

from datetime import date
from datetime import timedelta as td

from holidays.calendars.gregorian import JAN, JUL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Barbados(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Barbados
    https://www.timeanddate.com/holidays/barbados/
    [Public Holidays Act Cap.352] http://barbadosparliament-laws.com/en/showdoc/cs/352
    https://labour.gov.bb/pdf/Library/Other%20Docs/Public%20Holidays%20for%20the%20Year%202018.pdf
    https://labour.gov.bb/wp-content/uploads/2020/04/Public-Holidays-for-the-Year-2021.pdf
    https://gisbarbados.gov.bb/download/public-holidays-for-2022/
    https://gisbarbados.gov.bb/download/public-holidays-for-2023/
    """

    country = "BB"
    observed_label = "%s (Observed)"
    special_holidays = {
        2021: (
            (JAN, 4, "Public Holiday"),
            (JAN, 5, "Public Holiday"),
        ),
        # One off 50th Anniversary of CARICOM Holiday.
        # See https://tinyurl.com/brbhol
        2023: (JUL, 31, "50th Anniversary of CARICOM Holiday"),
    }

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, days: int = +1) -> None:
        if self.observed and self._is_sunday(dt):
            self._add_holiday(self.observed_label % self[dt], dt + td(days=days))

    def _populate(self, year):
        # Public Holidays Act Cap.352, 1968-12-30
        if year <= 1968:
            return None
        super()._populate(year)

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Errol Barrow Day
        if year >= 1989:
            self._add_observed(self._add_holiday_jan_21("Errol Barrow Day"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # National Heroes Day
        if year >= 1998:
            self._add_observed(self._add_holiday_apr_28("National Heroes Day"))

        # May Day
        self._add_observed(self._add_labor_day("May Day"))

        # Whit Monday
        self._add_whit_monday("Whit Monday")

        # Emancipation Day
        name = "Emancipation Day"
        self._add_observed(aug_1 := self._add_holiday_aug_1(name), days=+2)
        # If Aug 1 is Kadooment Day.
        if self.observed and self._is_monday(aug_1):
            self._add_holiday(self.observed_label % name, aug_1 + td(days=+1))

        # Kadooment Day
        self._add_holiday_1st_mon_of_aug("Kadooment Day")

        # Independence Day
        self._add_observed(self._add_holiday_nov_30("Independence Day"))

        # Christmas
        self._add_observed(self._add_christmas_day("Christmas Day"), days=+2)

        # Boxing Day
        self._add_observed(self._add_christmas_day_two("Boxing Day"))


class BB(Barbados):
    pass


class BRB(Barbados):
    pass
