#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.thailand import TH, THA, Thailand
from test.common import TestCase


class TestThailand(TestCase):
    def setUp(self):
        self.holidays = Thailand()

    def test_country_aliases(self):
        self.assertCountryAliases(Thailand, TH, THA)

    def test_2022(self):
        self.assertHolidaysEqual(
            Thailand(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-02-16", "Makha Bucha"),
            ("2022-04-06", "Chakri Memorial Day"),
            ("2022-04-13", "Songkran Festival"),
            ("2022-04-14", "Songkran Festival"),
            ("2022-04-15", "Songkran Festival"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (in lieu)"),
            ("2022-05-04", "Coronation Day"),
            ("2022-05-15", "Buddha's Birthday"),
            ("2022-05-16", "Buddha's Birthday (in lieu)"),
            ("2022-06-03", "Queen Suthida's Birthday"),
            ("2022-07-13", "Asalha Puja"),
            ("2022-07-14", "Beginning of Vassa"),
            ("2022-07-28", "King's Birthday"),
            ("2022-08-12", "The Queen Mother's Birthday"),
            ("2022-10-13", "King Bhumibol Adulyadej Memorial Day"),
            ("2022-10-23", "King Chulalongkorn Day"),
            ("2022-10-24", "King Chulalongkorn Day (in lieu)"),
            ("2022-12-05", "King Bhumibol Adulyadej's Birthday"),
            ("2022-12-10", "Constitution Day"),
            ("2022-12-12", "Constitution Day (in lieu)"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_new_years_day(self):
        self.assertHoliday(
            Thailand(observed=True),
            "2010-01-01",
            "2011-01-03",
            "2012-01-02",
        )

        self.assertNoHoliday(
            Thailand(observed=False),
            "2010-01-03",
            "2011-01-03",
            "2012-01-02",
        )

    def test_new_years_eve(self):
        self.assertHoliday(
            Thailand(),
            "2012-12-31",
            "2013-01-01",
            "2028-12-31",
            "2029-01-01",
        )

    def test_pre_2006(self):
        self.assertFalse(Thailand(years=2005).get_named("Asalha Puja"))
        self.assertFalse(Thailand(years=2005).get_named("Beginning of Vassa"))

    def test_coronation_day(self):
        self.assertHoliday("2016-05-05", "2020-05-04")
        self.assertNoHoliday("2017-05-04", "2017-05-05")
