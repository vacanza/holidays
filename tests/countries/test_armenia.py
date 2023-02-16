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

from holidays.countries.armenia import Armenia, AM, ARM
from tests.common import TestCase


class TestArmenia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Armenia)

    def test_country_aliases(self):
        self.assertCountryAliases(Armenia, AM, ARM)

    def test_no_holidays(self):
        self.assertNoHolidays(Armenia(years=1990))

    def test_new_year_christmas(self):
        for year in range(1991, 2100):
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
        for year in range(2022, 2100):
            self.assertNoHoliday(
                f"{year}-01-03",
                f"{year}-01-04",
                f"{year}-01-05",
                f"{year}-01-07",
            )

    def test_army_day(self):
        self.assertHoliday(f"{year}-01-28" for year in range(2003, 2100))
        self.assertNoHoliday(f"{year}-01-28" for year in range(1991, 2003))

    def test_women_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1991, 2100))

    def test_motherhood_and_beauty_day(self):
        self.assertHoliday(f"{year}-04-07" for year in range(1994, 2002))
        self.assertNoHoliday(f"{year}-04-07" for year in range(1991, 1994))
        self.assertNoHoliday(f"{year}-04-07" for year in range(2002, 2100))

    def test_genocide_remembrance_day(self):
        self.assertHoliday(f"{year}-04-24" for year in range(1991, 2100))

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(2001, 2100))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1991, 2001))
        may1_old_name = "Աշխատավորների համերաշխության միջազգային օր"
        self.assertIn(may1_old_name, self.holidays["2001-05-01"])
        self.assertNotIn(may1_old_name, self.holidays["2002-05-01"])

    def test_victory_day(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1995, 2100))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1991, 1995))

    def test_republic_day(self):
        self.assertHoliday(f"{year}-05-28" for year in range(1991, 2100))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-07-05" for year in range(1996, 2100))
        self.assertNoHoliday(f"{year}-07-05" for year in range(1991, 1996))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-09-21" for year in range(1992, 2100))
        self.assertNoHoliday(f"{year}-09-21" for year in range(1991, 1992))

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                am = Armenia(language=language)
                self.assertEqual(am["2022-01-01"], "Նոր տարվա օր")
                self.assertEqual(am["2022-12-31"], "Նոր տարվա գիշեր")

        run_tests((Armenia.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Armenia.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        am = Armenia(language=en_us)
        self.assertEqual(am["2022-01-01"], "New Year's Day")
        self.assertEqual(am["2022-12-31"], "New Year's Eve")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            am = Armenia(language=language)
            self.assertEqual(am["2022-01-01"], "New Year's Day")
            self.assertEqual(am["2022-12-31"], "New Year's Eve")
