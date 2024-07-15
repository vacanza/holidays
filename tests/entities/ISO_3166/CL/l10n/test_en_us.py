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

from holidays.entities.ISO_3166.CL import ClHolidays
from tests.common import CommonCountryTests


class TestClHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ClHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-21", "Navy Day"),
            ("2022-06-21", "National Day of Indigenous Peoples"),
            ("2022-06-27", "Saint Peter and Saint Paul"),
            ("2022-07-16", "Our Lady of Mount Carmel"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-16", "National Holiday"),
            ("2022-09-18", "Independence Day"),
            ("2022-09-19", "Army Day"),
            ("2022-10-10", "Meeting of Two Worlds' Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-31", "Bank Holiday"),
        )
