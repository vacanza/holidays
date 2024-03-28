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

from holidays.countries.maldives import Maldives, MDV, MV
from tests.common import CommonCountryTests


class TestMaldives(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Maldives, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Maldives, MV, MDV)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1950, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("Labor Day", (f"{year}-05-01" for year in range(1950, 2050)))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-07-26" for year in range(1950, 2050)))

    def test_victory_day(self):
        self.assertHolidayName("Victory Day", (f"{year}-11-03" for year in range(1950, 2050)))

    def test_republic_day(self):
        self.assertHolidayName("Republic Day", (f"{year}-11-11" for year in range(1950, 2050)))

    def test_2018(self):
        self.assertHolidays(
            Maldives(years=2018),
            ("2018-01-01", "New Year's Day"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-16", "Beginning of Ramadan (estimated)"),
            ("2018-06-15", "Eid al-Fitr (estimated)"),
            ("2018-06-16", "Eid al-Fitr (estimated)"),
            ("2018-06-17", "Eid al-Fitr (estimated)"),
            ("2018-07-26", "Independence Day"),
            ("2018-08-20", "Hajj Day (estimated)"),
            ("2018-08-21", "Eid al-Adha (estimated)"),
            ("2018-08-22", "Eid al-Adha (estimated)"),
            ("2018-08-23", "Eid al-Adha (estimated)"),
            ("2018-08-24", "Eid al-Adha (estimated)"),
            ("2018-09-11", "Islamic New Year (estimated)"),
            ("2018-11-03", "Victory Day"),
            ("2018-11-09", "National Day (estimated)"),
            ("2018-11-11", "Republic Day"),
            ("2018-11-20", "Mawlid al-Nabi (estimated)"),
            ("2018-12-08", "The Day Maldives Embraced Islam (estimated)"),
        )

    def test_2020(self):
        self.assertHolidays(
            Maldives(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-24", "Beginning of Ramadan (estimated)"),
            ("2020-05-01", "Labor Day"),
            ("2020-05-24", "Eid al-Fitr (estimated)"),
            ("2020-05-25", "Eid al-Fitr (estimated)"),
            ("2020-05-26", "Eid al-Fitr (estimated)"),
            ("2020-07-26", "Independence Day"),
            ("2020-07-30", "Hajj Day (estimated)"),
            ("2020-07-31", "Eid al-Adha (estimated)"),
            ("2020-08-01", "Eid al-Adha (estimated)"),
            ("2020-08-02", "Eid al-Adha (estimated)"),
            ("2020-08-03", "Eid al-Adha (estimated)"),
            ("2020-08-20", "Islamic New Year (estimated)"),
            ("2020-10-18", "National Day (estimated)"),
            ("2020-10-29", "Mawlid al-Nabi (estimated)"),
            ("2020-11-03", "Victory Day"),
            ("2020-11-11", "Republic Day"),
            ("2020-11-16", "The Day Maldives Embraced Islam (estimated)"),
        )
