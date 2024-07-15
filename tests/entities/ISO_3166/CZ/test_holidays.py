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

from unittest import TestCase

from holidays.entities.ISO_3166.CZ import CzHolidays
from tests.common import CommonCountryTests


class TestCzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CzHolidays, years=range(1945, 2050))

    def test_new_years_day(self):
        name_1 = "Nový rok"
        name_2 = "Den obnovy samostatného českého státu"
        self.assertHolidayName(name_1, (f"{year}-01-01" for year in range(1945, 2000)))
        self.assertHolidayName(name_2, (f"{year}-01-01" for year in range(2000, 2050)))
        self.assertNoHolidayName(name_1, range(2000, 2050))
        self.assertNoHolidayName(name_2, range(1945, 2000))

    def test_good_friday(self):
        name = "Velký pátek"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertNoHolidayName(name, range(1952, 2016))

    def test_easter_monday(self):
        self.assertHolidayName(
            "Velikonoční pondělí",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        name = "Svátek práce"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_victory_day(self):
        name_1 = "Den vítězství nad hitlerovským fašismem"
        name_2 = "Den vítězství"
        self.assertHolidayName(name_1, (f"{year}-05-09" for year in range(1947, 1992)))
        self.assertHolidayName(name_2, (f"{year}-05-08" for year in range(1992, 2050)))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1945, 1947))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1992, 2050))
        self.assertNoHoliday(f"{year}-05-08" for year in range(1945, 1992))
        self.assertNoHolidayName(name_1, range(1945, 1947), range(1992, 2050))
        self.assertNoHolidayName(name_2, range(1945, 1992))

    def test_cyril_and_methodius_day(self):
        name = "Den slovanských věrozvěstů Cyrila a Metoděje"
        self.assertHolidayName(name, (f"{year}-07-05" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-07-05" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_jan_hus_day(self):
        name = "Den upálení mistra Jana Husa"
        self.assertHolidayName(name, (f"{year}-07-06" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-07-06" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_statehood_day(self):
        name = "Den české státnosti"
        self.assertHolidayName(name, (f"{year}-09-28" for year in range(2000, 2050)))
        self.assertNoHoliday(f"{year}-09-28" for year in range(1945, 2000))
        self.assertNoHolidayName(name, range(1945, 2000))

    def test_independent_czechoslovak_state_day(self):
        name = "Den vzniku samostatného československého státu"
        self.assertHolidayName(name, (f"{year}-10-28" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-10-28" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_struggle_for_freedom_and_democracy_day(self):
        name = "Den boje za svobodu a demokracii"
        self.assertHolidayName(name, (f"{year}-11-17" for year in range(1990, 2050)))
        self.assertNoHoliday(f"{year}-11-17" for year in range(1945, 1990))
        self.assertNoHolidayName(name, range(1945, 1990))

    def test_christmas_eve(self):
        name = "Štědrý den"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(1990, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1945, 1990))
        self.assertNoHolidayName(name, range(1945, 1990))

    def test_christmas_day(self):
        name = "1. svátek vánoční"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-12-25" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_christmas_second_day(self):
        name = "2. svátek vánoční"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-12-26" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))
