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

from holidays.countries.tokelau import Tokelau, TK, TKL
from tests.common import CommonCountryTests


class TestTokelau(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tokelau, years=range(2003, 2050))

    def test_country_aliases(self):
        self.assertAliases(Tokelau, TK, TKL)

    def test_new_years(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(2003, 2050)))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2003, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2003, 2050))

    def test_tokehega_day(self):
        self.assertHolidayName("Tokehega Day", (f"{year}-09-03" for year in range(2003, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2003, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(2003, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-09-03", "Tokehega Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-09-03", "Tokehega Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )

    def test_l10n_tkl(self):
        self.assertLocalizedHolidays(
            "tkl",
            ("2022-01-01", "Aho Tauhaga Fou"),
            ("2022-04-15", "Ahofalaile Lelei"),
            ("2022-04-18", "Ahogafua o te Eheta"),
            ("2022-09-03", "Aho o te Tokehega"),
            ("2022-12-25", "Aho Kilihimahi"),
            ("2022-12-26", "Tua-aho Kilihimahi"),
        )
