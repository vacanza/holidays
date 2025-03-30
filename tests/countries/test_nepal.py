#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.nepal import Nepal, NP, NPL
from tests.common import CommonCountryTests


class TestNepal(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Nepal)

    def test_country_aliases(self):
        self.assertAliases(Nepal, NP, NPL)

    def test_2025(self):
        self.assertHolidays(
            Nepal(years=2025),
            ("2025-01-11", "Prithvi Jayanti"),
            ("2025-01-14", "Maghe Sankranti"),
            ("2025-01-30", "Martyr's Day; Sonam Losar"),
            ("2025-02-19", "National Democracy Day"),
            ("2025-02-26", "Maha Shivaratri"),
            ("2025-02-28", "Gyalpo Losar"),
            ("2025-03-08", "Women's Day"),
            ("2025-03-13", "Holi (Mountain & Hilly)"),
            ("2025-03-14", "Holi (Terai)"),
            ("2025-03-31", "Id-ul-Fitr"),
            ("2025-04-06", "Ram Navami"),
            ("2025-04-13", "Nepali New Year (Vikram Sambat)"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-12", "Buddha Jayanti"),
            ("2025-05-29", "Republic Day"),
            ("2025-06-07", "Bakrid"),
            ("2025-08-09", "Janai Purnima"),
            ("2025-08-16", "Shree Krishna Janmashtami"),
            ("2025-09-19", "Constitution Day"),
            ("2025-09-22", "Ghatasthapana"),
            ("2025-09-29", "Phulpati"),
            ("2025-09-30", "Maha Ashtami"),
            ("2025-10-01", "Maha Navami"),
            ("2025-10-02", "Vijayadashami"),
            ("2025-10-03", "Ekadashi (Dashain)"),
            ("2025-10-04", "Duwadashi (Dashain)"),
            ("2025-10-20", "Lakshmi Puja"),
            ("2025-10-21", "Gai Tihar"),
            ("2025-10-22", "Govardhan Puja; Mha Puja"),
            ("2025-10-23", "Bhai Tika"),
            ("2025-10-24", "Tihar Holiday"),
            ("2025-10-28", "Chhath Parwa"),
            ("2025-12-25", "Christmas"),
            ("2025-12-30", "Tamu Losar"),
        )

    def test_ranged_holidays(self):
        name = "Bakrid"
        dt = (
            "2001-03-06",
            "2010-11-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, dt)

        name = "Bhai Tika"
        dt = (
            "2001-11-16",
            "2010-11-07",
            "2025-10-23",
            "2035-11-01",
        )
        self.assertHolidayName(name, dt)

        name = "Buddha Jayanti"
        dt = (
            "2001-04-30",
            "2010-05-27",
            "2025-05-12",
            "2035-05-22",
        )
        self.assertHolidayName(name, dt)

        name = "Chhath Parwa"
        dt = (
            "2001-11-21",
            "2010-11-11",
            "2025-10-28",
            "2035-11-06",
        )
        self.assertHolidayName(name, dt)

        name = "Duwadashi (Dashain)"
        dt = (
            "2001-10-28",
            "2010-10-19",
            "2025-10-04",
            "2035-10-13",
        )
        self.assertHolidayName(name, dt)

        name = "Ekadashi (Dashain)"
        dt = (
            "2001-10-27",
            "2010-10-18",
            "2025-10-03",
            "2035-10-12",
        )
        self.assertHolidayName(name, dt)

        name = "Gai Tihar"
        dt = (
            "2001-11-14",
            "2010-11-05",
            "2025-10-21",
            "2035-10-30",
        )
        self.assertHolidayName(name, dt)

        name = "Ghatasthapana"
        dt = (
            "2001-10-17",
            "2010-10-08",
            "2025-09-22",
            "2035-10-02",
        )
        self.assertHolidayName(name, dt)

        name = "Govardhan Puja"
        dt = (
            "2001-11-15",
            "2010-11-06",
            "2025-10-22",
            "2035-10-31",
        )
        self.assertHolidayName(name, dt)

        name = "Gyalpo Losar"
        dt = (
            "2016-03-09",
            "2025-02-28",
            "2035-02-09",
        )
        self.assertHolidayName(name, dt)

        name = "Holi (Mountain & Hilly)"
        dt = (
            "2001-03-09",
            "2010-02-28",
            "2025-03-13",
            "2035-03-23",
        )
        self.assertHolidayName(name, dt)

        name = "Holi (Terai)"
        dt = (
            "2001-03-10",
            "2010-03-01",
            "2025-03-14",
            "2035-03-24",
        )
        self.assertHolidayName(name, dt)

        name = "Id-ul-Fitr"
        dt = (
            "2001-12-17",
            "2010-09-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, dt)

        name = "Janai Purnima"
        dt = (
            "2001-08-04",
            "2010-08-24",
            "2025-08-09",
            "2035-08-18",
        )
        self.assertHolidayName(name, dt)

        name = "Shree Krishna Janmashtami"
        dt = (
            "2001-08-12",
            "2010-09-02",
            "2025-08-16",
            "2035-08-26",
        )
        self.assertHolidayName(name, dt)

        name = "Lakshmi Puja"
        dt = (
            "2001-11-14",
            "2010-11-05",
            "2025-10-20",
            "2035-10-30",
        )
        self.assertHolidayName(name, dt)

        name = "Maha Ashtami"
        dt = (
            "2001-10-24",
            "2010-10-15",
            "2025-09-30",
            "2035-10-09",
        )
        self.assertHolidayName(name, dt)

        name = "Maha Navami"
        dt = (
            "2001-10-25",
            "2010-10-16",
            "2025-10-01",
            "2035-10-10",
        )
        self.assertHolidayName(name, dt)

        name = "Maghe Sankranti"
        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        self.assertHolidayName(name, dt)

        name = "Mha Puja"
        dt = (
            "2001-11-15",
            "2010-11-06",
            "2025-10-22",
            "2035-10-31",
        )
        self.assertHolidayName(name, dt)

        name = "Phulpati"
        dt = (
            "2001-10-23",
            "2010-10-14",
            "2025-09-29",
            "2035-10-08",
        )
        self.assertHolidayName(name, dt)

        name = "Ram Navami"
        dt = (
            "2001-04-02",
            "2010-03-24",
            "2025-04-06",
            "2035-04-16",
        )
        self.assertHolidayName(name, dt)

        name = "Sonam Losar"
        dt = (
            "2016-02-09",
            "2025-01-30",
            "2035-02-09",
        )
        self.assertHolidayName(name, dt)

        name = "Tihar Holiday"
        dt = (
            "2001-11-17",
            "2010-11-08",
            "2025-10-24",
            "2035-11-02",
        )
        self.assertHolidayName(name, dt)

        name = "Vijayadashami"
        dt = (
            "2001-10-26",
            "2010-10-17",
            "2025-10-02",
            "2035-10-11",
        )
        self.assertHolidayName(name, dt)
