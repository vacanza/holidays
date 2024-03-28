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

from holidays.countries.slovenia import Slovenia, SI, SVN
from tests.common import CommonCountryTests


class TestSlovenia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Slovenia, years=range(1991, 2050))

    def test_country_aliases(self):
        self.assertAliases(Slovenia, SI, SVN)

    def test_no_holidays(self):
        self.assertNoHolidays(Slovenia(years=1990))

    def test_special_holidays(self):
        self.assertHoliday(
            # Solidarity Day
            "2023-08-14",
        )

    def test_new_years_day(self):
        name = "novo leto"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1991, 2050)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1991, 2013)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2017, 2050)))
        self.assertNoHoliday(f"{year}-01-02" for year in range(2013, 2017))

    def test_preserens_day(self):
        self.assertHolidayName("Prešernov dan", (f"{year}-02-08" for year in range(1991, 2050)))

    def test_easter_monday(self):
        self.assertHolidayName(
            "Velikonočni ponedeljek",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_uprising_against_occupation_day(self):
        self.assertHolidayName(
            "dan upora proti okupatorju", (f"{year}-04-27" for year in range(1991, 2050))
        )

    def test_labor_day(self):
        self.assertHolidayName("praznik dela", (f"{year}-05-01" for year in range(1991, 2050)))
        self.assertHolidayName("praznik dela", (f"{year}-05-02" for year in range(1991, 2050)))

    def test_statehood_day(self):
        self.assertHolidayName("dan državnosti", (f"{year}-06-25" for year in range(1991, 2050)))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Marijino vnebovzetje", (f"{year}-08-15" for year in range(1991, 2050))
        )

    def test_reformation_day(self):
        name = "dan reformacije"
        self.assertHolidayName(name, (f"{year}-10-31" for year in range(1992, 2050)))
        self.assertNoHoliday("1991-10-31")
        self.assertNoHolidayName(name, 1991)

    def test_all_saints_day(self):
        self.assertHolidayName(
            "dan spomina na mrtve", (f"{year}-11-01" for year in range(1991, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Božič", (f"{year}-12-25" for year in range(1991, 2050)))

    def test_independence_and_unity_day(self):
        self.assertHolidayName(
            "dan samostojnosti in enotnosti", (f"{year}-12-26" for year in range(1991, 2050))
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "novo leto"),
            ("2022-01-02", "novo leto"),
            ("2022-02-08", "Prešernov dan"),
            ("2022-04-18", "Velikonočni ponedeljek"),
            ("2022-04-27", "dan upora proti okupatorju"),
            ("2022-05-01", "praznik dela"),
            ("2022-05-02", "praznik dela"),
            ("2022-06-25", "dan državnosti"),
            ("2022-08-15", "Marijino vnebovzetje"),
            ("2022-10-31", "dan reformacije"),
            ("2022-11-01", "dan spomina na mrtve"),
            ("2022-12-25", "Božič"),
            ("2022-12-26", "dan samostojnosti in enotnosti"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-02-08", "Preseren's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "Day of Uprising Against Occupation"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day"),
            ("2022-06-25", "Statehood Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "Remembrance Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Independence and Unity Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-02-08", "День Прешерена"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День спротиву окупантам"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці"),
            ("2022-06-25", "День державності"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День памʼяті померлих"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День незалежності та єднання"),
        )
