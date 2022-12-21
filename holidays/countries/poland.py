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

from holidays.constants import MAY, NOV
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Poland(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://pl.wikipedia.org/wiki/Dni_wolne_od_pracy_w_Polsce
    """

    country = "PL"
    special_holidays = {
        2018: ((NOV, 12, "Narodowe Święto Niepodległości - 100-lecie"),)
    }

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        self._add_new_years_day("Nowy Rok")

        if year >= 2011:
            self._add_epiphany_day("Święto Trzech Króli")

        self._add_easter_sunday("Niedziela Wielkanocna")
        self._add_easter_monday("Poniedziałek Wielkanocny")

        if year >= 1950:
            self._add_holiday("Święto Państwowe", MAY, 1)
        if year >= 1919:
            self._add_holiday("Święto Narodowe Trzeciego Maja", MAY, 3)

        self._add_whit_sunday("Zielone Świątki")
        self._add_feast_of_corpus_christi("Dzień Bożego Ciała")

        self._add_assumption_of_mary_day(
            "Wniebowzięcie Najświętszej Marii Panny"
        )

        self._add_all_saints_day("Uroczystość Wszystkich Świętych")

        if 1937 <= year <= 1945 or year >= 1989:
            self._add_holiday("Narodowe Święto Niepodległości", NOV, 11)

        self._add_christmas_day("Boże Narodzenie (pierwszy dzień)")
        self._add_christmas_day_two("Boże Narodzenie (drugi dzień)")


class PL(Poland):
    pass


class POL(Poland):
    pass
