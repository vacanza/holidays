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

from holidays.entities.ISO_3166.JP import JpHolidays
from tests.common import CommonCountryTests


class TestJpHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JpHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "Bank Holiday"),
            ("2022-01-03", "Bank Holiday"),
            ("2022-01-10", "Coming of Age Day"),
            ("2022-02-11", "Foundation Day"),
            ("2022-02-23", "Emperor's Birthday"),
            ("2022-03-21", "Vernal Equinox Day"),
            ("2022-04-29", "Showa Day"),
            ("2022-05-03", "Constitution Day"),
            ("2022-05-04", "Greenery Day"),
            ("2022-05-05", "Children's Day"),
            ("2022-07-18", "Marine Day"),
            ("2022-08-11", "Mountain Day"),
            ("2022-09-19", "Respect for the Aged Day"),
            ("2022-09-23", "Autumnal Equinox"),
            ("2022-10-10", "Sports Day"),
            ("2022-11-03", "Culture Day"),
            ("2022-11-23", "Labor Thanksgiving Day"),
            ("2022-12-31", "Bank Holiday"),
        )
