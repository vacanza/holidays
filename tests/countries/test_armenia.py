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

from holidays.countries.armenia import Armenia
from tests.common import CommonCountryTests


class TestArmenia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Armenia)

    def test_new_years_day(self):
        name = "Նոր տարվա օր"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
        )
        self.assertHolidayName(
            name,
            (f"{year}-01-03" for year in range(2010, 2022)),
            (f"{year}-01-04" for year in range(2010, 2022)),
        )
        self.assertHolidayNameCount(
            name, 2, range(self.start_year, 2010), range(2022, self.end_year)
        )

    def test_christmas_eve(self):
        name = "Սուրբ Ծննդյան տոներ"
        self.assertHolidayName(name, (f"{year}-01-05" for year in range(2010, 2022)))
        self.assertNoHolidayName(name, range(self.start_year, 2010), range(2022, self.end_year))

    def test_christmas_and_epiphany_day(self):
        self.assertHolidayName(
            "Սուրբ Ծնունդ եւ Հայտնություն", (f"{year}-01-06" for year in self.full_range)
        )

    def test_day_of_remembrance_of_the_dead(self):
        name = "Մեռելոց հիշատակի օր"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2010, 2022)))
        self.assertNoHolidayName(name, range(self.start_year, 2010), range(2022, self.end_year))

    def test_army_day(self):
        name = "Բանակի օր"
        self.assertHolidayName(name, (f"{year}-01-28" for year in range(2003, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2003))

    def test_womens_day(self):
        self.assertHolidayName("Կանանց տոն", (f"{year}-03-08" for year in self.full_range))

    def test_motherhood_and_beauty_day(self):
        name = "Մայրության և գեղեցկության տոն"
        self.assertHolidayName(name, (f"{year}-04-07" for year in range(1994, 2002)))
        self.assertNoHolidayName(name, range(self.start_year, 1994), range(2002, self.end_year))

    def test_armenian_genocide_remembrance_day(self):
        self.assertHolidayName(
            "Եղեռնի զոհերի հիշատակի օր", (f"{year}-04-24" for year in self.full_range)
        )

    def test_labor_day(self):
        name_2001 = "Աշխատավորների համերաշխության միջազգային օր"
        name_2002 = "Աշխատանքի օր"
        self.assertHolidayName(name_2001, "2001-05-01")
        self.assertHolidayName(name_2002, (f"{year}-05-01" for year in range(2002, self.end_year)))
        self.assertNoHolidayName(
            name_2001, range(self.start_year, 2001), range(2002, self.end_year)
        )
        self.assertNoHolidayName(name_2002, range(self.start_year, 2002))

    def test_victory_and_peace_day(self):
        name = "Հաղթանակի և Խաղաղության տոն"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))

    def test_republic_day(self):
        self.assertHolidayName("Հանրապետության օր", (f"{year}-05-28" for year in self.full_range))

    def test_constitution_day(self):
        name = "Սահմանադրության օր"
        self.assertHolidayName(name, (f"{year}-07-05" for year in range(1996, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1996))

    def test_independence_day(self):
        name = "Անկախության օր"
        self.assertHolidayName(name, (f"{year}-09-21" for year in range(1992, self.end_year)))
        self.assertNoHolidayName(name, 1991)

    def test_new_years_eve(self):
        self.assertHolidayName("Նոր տարվա գիշեր", (f"{year}-12-31" for year in self.full_range))

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
