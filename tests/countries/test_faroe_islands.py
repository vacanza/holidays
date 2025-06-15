#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import PUBLIC, HALF_DAY
from holidays.countries.faroe_islands import FaroeIslands, FO
from tests.common import CommonCountryTests


class TestFaroeIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1990, 2050)
        super().setUpClass(FaroeIslands, years=years)

    holidays_2023 = [
        ("2023-01-01", "Nýggjársdagur"),
        ("2023-04-06", "Skírhósdagur"),
        ("2023-04-07", "Langifríggjadagur"),
        ("2023-04-09", "Páskadagur"),
        ("2023-04-10", "Annar páskadagur"),
        ("2023-04-25", "Flaggdagur"),
        ("2023-05-05", "Dýri biðidagur"),
        ("2023-05-18", "Kristi himmalsferðardagur"),
        ("2023-05-28", "Hvítusunnudagur"),
        ("2023-05-29", "Annar hvítusunnudagur"),
        ("2023-06-05", "Grundlógardagur"),
        ("2023-07-28", "Ólavsøkuaftan"),
        ("2023-07-29", "Ólavsøkudagur"),
        ("2023-12-24", "Jólaaftan"),
        ("2023-12-25", "Jóladagur"),
        ("2023-12-26", "Annar jóladagur"),
        ("2023-12-31", "Nýggjársaftan"),
    ]

    def test_country_aliases(self):
        self.assertAliases(FaroeIslands, FO)

    def test_new_years_day(self):
        self.assertHolidayName("Nýggjársdagur", (f"{year}-01-01" for year in range(1990, 2050)))

    def test_national_day(self):
        self.assertHolidayName("Ólavsøkudagur", (f"{year}-07-29" for year in range(1990, 2050)))

    def test_2023(self):
        self.assertHolidays(FaroeIslands(categories=(PUBLIC, HALF_DAY)), *self.holidays_2023)

    def test_2023_and_localization(self):
        self.assertHolidays(FaroeIslands(categories=(PUBLIC, HALF_DAY)), *self.holidays_2023)
        self.assertLocalizedHolidays(*self.holidays_2023)
