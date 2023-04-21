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

from holidays.countries.united_arab_emirates import UnitedArabEmirates, AE, ARE
from tests.common import TestCase


class TestUnitedArabEmirates(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedArabEmirates)

    def test_country_aliases(self):
        self.assertCountryAliases(UnitedArabEmirates, AE, ARE)

    def test_2020(self):
        self.assertHolidays(
            UnitedArabEmirates(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-05-24", "Eid al-Fitr"),
            ("2020-05-25", "Eid al-Fitr Holiday"),
            ("2020-05-26", "Eid al-Fitr Holiday"),
            ("2020-07-30", "Arafat (Hajj) Day"),
            ("2020-07-31", "Eid al-Adha"),
            ("2020-08-01", "Eid al-Adha Holiday"),
            ("2020-08-02", "Eid al-Adha Holiday"),
            ("2020-08-23", "Al Hijra - Islamic New Year"),
            ("2020-12-01", "Commemoration Day"),
            ("2020-12-02", "National Day"),
            ("2020-12-03", "National Day Holiday"),
        )

    def test_commemoration_day_since_2015(self):
        self.assertNoHoliday("2014-11-30")
        self.assertNoHolidayName(
            "Commemoration Day", UnitedArabEmirates(years=2014)
        )
        self.assertHoliday(
            "2015-11-30", "2016-11-30", "2017-11-30", "2018-11-30"
        )
        self.assertNoHoliday("2019-11-30")
        self.assertHoliday("2019-12-01")

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid Al-Fitr
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            # Arafat Day & Eid Al-Adha
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2020-08-23",
            # Leilat Al-Miraj 2018
            "2018-04-13",
            # Prophet's Birthday 2018
            "2018-11-19",
        )
