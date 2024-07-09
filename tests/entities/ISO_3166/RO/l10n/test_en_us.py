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

from holidays.entities.ISO_3166.RO import RoHolidays
from tests.common import CommonCountryTests


class TestRoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(RoHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "New Year's Day"),
            ("2018-01-02", "New Year's Day"),
            ("2018-01-24", "Unification of the Romanian Principalities Day"),
            ("2018-04-06", "Easter"),
            ("2018-04-08", "Easter"),
            ("2018-04-09", "Easter"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-27", "Pentecost"),
            ("2018-05-28", "Pentecost"),
            ("2018-06-01", "Children's Day"),
            ("2018-08-15", "Dormition of the Mother of God"),
            ("2018-11-30", "Saint Andrew's Day"),
            ("2018-12-01", "National Day"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Christmas Day"),
        )
