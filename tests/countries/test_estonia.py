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

from unittest import TestCase

from holidays.countries.estonia import Estonia, EE, EST
from tests.common import CommonCountryTests


class TestEstonia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Estonia, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertAliases(Estonia, EE, EST)

    def test_new_years(self):
        self.assertHolidayName("uusaasta", (f"{year}-01-01" for year in range(1990, 2050)))

    def test_independence_day(self):
        self.assertHolidayName("iseseisvuspäev", (f"{year}-02-24" for year in range(1990, 2050)))

    def test_good_friday(self):
        self.assertHolidayName(
            "suur reede",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter_sunday(self):
        self.assertHolidayName(
            "ülestõusmispühade 1. püha",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_spring_day(self):
        self.assertHolidayName("kevadpüha", (f"{year}-05-01" for year in range(1990, 2050)))

    def test_whit_sunday(self):
        self.assertHolidayName(
            "nelipühade 1. püha",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )

    def test_victory_day(self):
        self.assertHolidayName("võidupüha", (f"{year}-06-23" for year in range(1990, 2050)))

    def test_midsummer_day(self):
        self.assertHolidayName("jaanipäev", (f"{year}-06-24" for year in range(1990, 2050)))

    def test_restoration_of_independence_day(self):
        name = "taasiseseisvumispäev"
        self.assertHolidayName(name, (f"{year}-08-20" for year in range(1998, 2050)))
        self.assertNoHoliday(f"{year}-08-20" for year in range(1990, 1998))
        self.assertNoHolidayName(name, range(1990, 1998))

    def test_christmas_eve(self):
        name = "jõululaupäev"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2005, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1990, 2005))
        self.assertNoHolidayName(name, range(1990, 2005))

    def test_christmas_day(self):
        self.assertHolidayName(
            "esimene jõulupüha", (f"{year}-12-25" for year in range(1990, 2050))
        )

    def test_second_christmas_day(self):
        self.assertHolidayName("teine jõulupüha", (f"{year}-12-26" for year in range(1990, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "uusaasta"),
            ("2022-02-24", "iseseisvuspäev"),
            ("2022-04-15", "suur reede"),
            ("2022-04-17", "ülestõusmispühade 1. püha"),
            ("2022-05-01", "kevadpüha"),
            ("2022-06-05", "nelipühade 1. püha"),
            ("2022-06-23", "võidupüha"),
            ("2022-06-24", "jaanipäev"),
            ("2022-08-20", "taasiseseisvumispäev"),
            ("2022-12-24", "jõululaupäev"),
            ("2022-12-25", "esimene jõulupüha"),
            ("2022-12-26", "teine jõulupüha"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-24", "Independence Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "Spring Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-23", "Victory Day"),
            ("2022-06-24", "Midsummer Day"),
            ("2022-08-20", "Independence Restoration Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-24", "День незалежності"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-05-01", "День весни"),
            ("2022-06-05", "Трійця"),
            ("2022-06-23", "День перемоги"),
            ("2022-06-24", "День літнього сонцестояння"),
            ("2022-08-20", "День відновлення незалежності"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
