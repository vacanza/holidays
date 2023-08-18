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

from datetime import timedelta as td

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Andorra(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://en.wikipedia.org/wiki/Public_holidays_in_Andorra
      - https://www.holsdb.com/public-holidays/ad
    """

    country = "AD"
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

    def _populate(self, year: int) -> None:
        super()._populate(year)

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
    def _add_subdiv_02_holidays(self):
        name = "Canillo Annual Festival"
        third_sat_of_july = self._add_holiday_3rd_sat_of_jul(name)
        self._add_holiday(name, third_sat_of_july + td(days=+1))
        self._add_holiday(name, third_sat_of_july + td(days=+2))

    # Encamp.
    def _add_subdiv_03_holidays(self):
        name = "Encamp Annual Festival"
        aug_15 = self._add_holiday_aug_15(name)
        self._add_holiday(name, aug_15 + td(days=+1))

    # La Massana.
    def _add_subdiv_04_holidays(self):
        name = "La Massana Annual Festival"
        aug_15 = self._add_holiday_aug_15(name)
        self._add_holiday(name, aug_15 + td(days=+1))

    # Ordino.
    def _add_subdiv_05_holidays(self):
        name = "Ordino Annual Festival"
        aug_15 = self._add_holiday_aug_15(name)
        self._add_holiday(name, aug_15 + td(days=+1))

    # Sant Julià de Lòria.
    def _add_subdiv_06_holidays(self):
        name = "Sant Julià de Lòria Annual Festival"
        last_fri_of_july = self._add_holiday_1st_fri_before_jul_29(name)
        self._add_holiday(name, last_fri_of_july + td(days=+1))
        self._add_holiday(name, last_fri_of_july + td(days=+2))
        self._add_holiday(name, last_fri_of_july + td(days=+3))

    # Andorra la Vella.
    def _add_subdiv_07_holidays(self):
        name = "Andorra la Vella Annual Festival"
        first_sat_of_august = self._add_holiday_1st_sat_of_aug(name)
        self._add_holiday(name, first_sat_of_august + td(days=+1))
        self._add_holiday(name, first_sat_of_august + td(days=+2))

    # Escaldes-Engordany.
    def _add_subdiv_08_holidays(self):
        name = "Escaldes-Engordany Annual Festival"
        jul_25 = self._add_holiday_jul_25(name)
        self._add_holiday(name, jul_25 + td(days=+1))


class AD(Andorra):
    pass


class AND(Andorra):
    pass
