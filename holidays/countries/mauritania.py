#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.calendars.gregorian import FRI, SAT
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Mauritania(HolidayBase, InternationalHolidays, IslamicHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Mauritania
    - https://www.timeanddate.com/holidays/mauritania/
    """

    country = "MR"
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Labor Day.
        self._add_labor_day("Labor Day")

        # Africa Day.
        self._add_africa_day("Africa Day")

        # Independence Day.
        if year >= 1960:
            self._add_holiday_nov_28("Independence Day")

        # Islamic holidays.
        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")
        self._add_eid_al_fitr_day_two("Eid al-Fitr")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")
        self._add_eid_al_adha_day_two("Eid al-Adha")

        # Muharram/Islamic New Year.
        self._add_islamic_new_year_day("Islamic New Year")

        # Prophet Muhammad's Birthday.
        self._add_mawlid_day("Mawlid al-Nabi")


class MR(Mauritania):
    pass


class MRT(Mauritania):
    pass
