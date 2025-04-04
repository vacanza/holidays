#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.bhutan import Bhutan, BT, BTN
from tests.common import CommonCountryTests


class TestBhutan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bhutan, years=range(2008, 2050), years_non_observed=range(2008, 2050))

    def test_country_aliases(self):
        self.assertAliases(Bhutan, BT, BTN)

    def test_no_holidays(self):
        self.assertNoHolidays(Bhutan(years=2007))

    def test_nyilo(self):
        self.assertHolidayName("Nyilo", (f"{year}-01-02" for year in range(2008, 2050)))

    def test_kings_birthday(self):
        self.assertHolidayName(
            "King's Birthday (Day 11)", (f"{year}-02-21" for year in range(2008, 2050))
        )
        self.assertHolidayName(
            "King's Birthday (Day 2)", (f"{year}-02-22" for year in range(2008, 2050))
        )
        self.assertHolidayName(
            "King's Birthday (Day 3)", (f"{year}-02-23" for year in range(2008, 2050))
        )

    def test_birth_anniversary_of_third_druk_gyalpo(self):
        self.assertHolidayName(
            "Birth Anniversary of Third Druk Gyalpo",
            (f"{year}-05-02" for year in range(2008, 2050)),
        )

    def test_kings_jigme_khesar_namgyels_coronation(self):
        self.assertHolidayName(
            "King Jigme Khesar Namgyel's Coronation",
            (f"{year}-11-01" for year in range(2008, 2050)),
        )

    def test_birth_anniversary_of_fourth_druk_gyalpo(self):
        self.assertHolidayName(
            "Birth Anniversary of Fourth Druk Gyalpo",
            (f"{year}-11-11" for year in range(2008, 2050)),
        )

    def test_national_day(self):
        self.assertHolidayName("National Day", (f"{year}-12-17" for year in range(2008, 2050)))

    def test_2024(self):
        self.assertHolidays(
            Bhutan(years=2024),
            ("2024-01-02", "Nyilo"),
            ("2024-02-21", "King's Birthday (Day 11)"),
            ("2024-02-22", "King's Birthday (Day 2)"),
            ("2024-02-23", "King's Birthday (Day 3)"),
            ("2024-05-02", "Birth Anniversary of Third Druk Gyalpo"),
            ("2024-11-01", "King Jigme Khesar Namgyel's Coronation"),
            ("2024-11-11", "Birth Anniversary of Fourth Druk Gyalpo"),
            ("2024-12-17", "National Day"),
        )

    def test_2021(self):
        self.assertHolidays(
            Bhutan(years=2021),
            ("2021-01-02", "Nyilo"),
            ("2021-02-21", "King's Birthday (Day 11)"),
            ("2021-02-22", "King's Birthday (Day 2)"),
            ("2021-02-23", "King's Birthday (Day 3)"),
            ("2021-05-02", "Birth Anniversary of Third Druk Gyalpo"),
            ("2021-11-01", "King Jigme Khesar Namgyel's Coronation"),
            ("2021-11-11", "Birth Anniversary of Fourth Druk Gyalpo"),
            ("2021-12-17", "National Day"),
        )
