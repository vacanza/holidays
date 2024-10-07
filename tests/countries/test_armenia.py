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

from holidays.countries.armenia import Armenia, AM, ARM
from tests.common import CommonCountryTests


class TestArmenia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Armenia, years=range(1991, 2050))

    def test_country_aliases(self):
        self.assertAliases(Armenia, AM, ARM)

    def test_no_holidays(self):
        self.assertNoHolidays(Armenia(years=1990))

    def test_new_year_christmas(self):
        for year in range(1991, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-01-02",
                f"{year}-01-06",
                f"{year}-12-31",
            )
        for year in range(2010, 2022):
            self.assertHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )
        for year in range(1991, 2010):
            self.assertNoHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )
        for year in range(2022, 2050):
            self.assertNoHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )

    def test_army_day(self):
        self.assertHoliday(f"{year}-01-28" for year in range(2003, 2050))
        self.assertNoHoliday(f"{year}-01-28" for year in range(1991, 2003))

    def test_women_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1991, 2050))

    def test_motherhood_and_beauty_day(self):
        self.assertHoliday(f"{year}-04-07" for year in range(1994, 2002))
        self.assertNoHoliday(f"{year}-04-07" for year in range(1991, 1994))
        self.assertNoHoliday(f"{year}-04-07" for year in range(2002, 2050))

    def test_genocide_remembrance_day(self):
        self.assertHoliday(f"{year}-04-24" for year in range(1991, 2050))

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(2001, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1991, 2001))
        may1_old_name = "Աշխատավորների համերաշխության միջազգային օր"
        self.assertHolidayName(may1_old_name, "2001-05-01")
        self.assertNoHolidayName(may1_old_name, 2002)

    def test_victory_day(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1995, 2050))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1991, 1995))

    def test_republic_day(self):
        self.assertHoliday(f"{year}-05-28" for year in range(1991, 2050))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-07-05" for year in range(1996, 2050))
        self.assertNoHoliday(f"{year}-07-05" for year in range(1991, 1996))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-09-21" for year in range(1992, 2050))
        self.assertNoHoliday(f"{year}-09-21" for year in range(1991, 1992))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Նոր տարվա օր"),
            ("2022-01-02", "Նոր տարվա օր"),
            ("2022-01-06", "Սուրբ Ծնունդ եւ Հայտնություն"),
            ("2022-01-28", "Բանակի օր"),
            ("2022-03-08", "Կանանց տոն"),
            ("2022-04-24", "Եղեռնի զոհերի հիշատակի օր"),
            ("2022-05-01", "Աշխատանքի օր"),
            ("2022-05-09", "Հաղթանակի և Խաղաղության տոն"),
            ("2022-05-28", "Հանրապետության օր"),
            ("2022-07-05", "Սահմանադրության օր"),
            ("2022-09-21", "Անկախության օր"),
            ("2022-12-31", "Նոր տարվա գիշեր"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-06", "Christmas and Epiphany Day"),
            ("2022-01-28", "Army Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-04-24", "Genocide Memorial Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-09", "Victory and Peace Day"),
            ("2022-05-28", "Republic Day"),
            ("2022-07-05", "Constitution Day"),
            ("2022-09-21", "Independence Day"),
            ("2022-12-31", "New Year's Eve"),
        )
