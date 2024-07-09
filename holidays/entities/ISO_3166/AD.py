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
    - https://en.wikipedia.org/wiki/Public_holidays_in_Andorra
    - https://www.holsdb.com/public-holidays/ad
"""

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class AdHolidays(HolidayBase, ChristianHolidays, InternationalHolidays):
    """A class to represent holidays for Andorra."""

    country = "AD"
    name = "Andorra"
    subdivisions = (
        "02",  # Canillo.
        "03",  # Encamp.
        "04",  # La Massana.
        "05",  # Ordino.
        "06",  # Sant Julià de Lòria.
        "07",  # Andorra la Vella.
        "08",  # Escaldes-Engordany.
    )

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self) -> None:
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Epiphany.
        self._add_epiphany_day("Epiphany")

        # Carnival.
        self._add_carnival_tuesday("Carnival")

        # Constitution Day.
        self._add_holiday_mar_14("Constitution Day")

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Sunday.
        self._add_easter_monday("Easter Monday")

        # Labor Day.
        self._add_labor_day("Labor Day")

        # Whit Monday.
        self._add_whit_monday("Whit Monday")

        # Assumption Day.
        self._add_assumption_of_mary_day("Assumption Day")

        # National Day.
        self._add_holiday_sep_8("National Day")

        # All Saints' Day.
        self._add_all_saints_day("All Saints' Day")

        # Immaculate Conception Day.
        self._add_immaculate_conception_day("Immaculate Conception Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Saint Stephen's Day.
        self._add_christmas_day_two("Saint Stephen's Day")

    # Canillo.
    def _populate_subdiv_02_public_holidays(self):
        name = "Canillo Annual Festival"
        self._add_holiday_3rd_sat_of_jul(name)
        self._add_holiday_1_day_past_3rd_sat_of_jul(name)
        self._add_holiday_2_days_past_3rd_sat_of_jul(name)

    # Encamp.
    def _populate_subdiv_03_public_holidays(self):
        name = "Encamp Annual Festival"
        self._add_holiday_aug_15(name)
        self._add_holiday_aug_16(name)

    # La Massana.
    def _populate_subdiv_04_public_holidays(self):
        name = "La Massana Annual Festival"
        self._add_holiday_aug_15(name)
        self._add_holiday_aug_16(name)

    # Ordino.
    def _populate_subdiv_05_public_holidays(self):
        name = "Ordino Annual Festival"
        self._add_holiday_aug_15(name)
        self._add_holiday_aug_16(name)

    # Sant Julià de Lòria.
    def _populate_subdiv_06_public_holidays(self):
        name = "Sant Julià de Lòria Annual Festival"
        self._add_holiday_1st_fri_before_jul_29(name)
        self._add_holiday_1st_sat_before_jul_30(name)
        self._add_holiday_1st_sun_before_jul_31(name)
        self._add_holiday_1st_mon_before_aug_1(name)

    # Andorra la Vella.
    def _populate_subdiv_07_public_holidays(self):
        name = "Andorra la Vella Annual Festival"
        self._add_holiday_1st_sat_of_aug(name)
        self._add_holiday_1_day_past_1st_sat_of_aug(name)
        self._add_holiday_2_days_past_1st_sat_of_aug(name)

    # Escaldes-Engordany.
    def _populate_subdiv_08_public_holidays(self):
        name = "Escaldes-Engordany Annual Festival"
        self._add_holiday_jul_25(name)
        self._add_holiday_jul_26(name)
