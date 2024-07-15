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

"""
References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_the_Maldives
    - https://www.timeanddate.com/holidays/maldives/
    - http://www.mma.gov.mv/#/about/bankholidays
"""

from holidays.calendars.gregorian import FRI, SAT
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class MvHolidays(HolidayBase, InternationalHolidays, IslamicHolidays):
    """A class to represent holidays for Maldives."""

    country = "MV"
    name = "Maldives"
    weekend = {FRI, SAT}

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Labor Day.
        self._add_labor_day("Labor Day")

        # Independence Day.
        self._add_holiday_jul_26("Independence Day")

        # Victory Day.
        self._add_holiday_nov_3("Victory Day")

        # Republic Day.
        self._add_holiday_nov_11("Republic Day")

        # Islamic holidays.
        # Start of Ramadan.
        self._add_ramadan_beginning_day("Beginning of Ramadan")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid al-Fitr")
        self._add_eid_al_fitr_day_two("Eid al-Fitr")
        self._add_eid_al_fitr_day_three("Eid al-Fitr")

        # Hajj Day.
        self._add_arafah_day("Hajj Day")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid al-Adha")
        self._add_eid_al_adha_day_two("Eid al-Adha")
        self._add_eid_al_adha_day_three("Eid al-Adha")
        self._add_eid_al_adha_day_four("Eid al-Adha")

        # Muharram/Islamic New Year.
        self._add_islamic_new_year_day("Islamic New Year")

        # National Day.
        self._add_quamee_dhuvas_day("National Day")

        # Prophet Muhammad's Birthday.
        self._add_mawlid_day("Mawlid al-Nabi")

        # The Day Maldives Embraced Islam.
        self._add_maldives_embraced_islam_day("The Day Maldives Embraced Islam")
