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

from holidays.entities.ISO_3166.RU import RuHolidays
from tests.common import CommonCountryTests


class TestRussia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(RuHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "New Year Holidays"),
            ("2018-01-02", "New Year Holidays"),
            ("2018-01-03", "New Year Holidays"),
            ("2018-01-04", "New Year Holidays"),
            ("2018-01-05", "New Year Holidays"),
            ("2018-01-06", "New Year Holidays"),
            ("2018-01-07", "Christmas Day"),
            ("2018-01-08", "New Year Holidays"),
            ("2018-02-23", "Fatherland Defender's Day"),
            ("2018-03-08", "International Women's Day"),
            ("2018-05-01", "Holiday of Spring and Labor"),
            ("2018-05-09", "Victory Day"),
            ("2018-06-12", "Russia Day"),
            ("2018-11-04", "Unity Day"),
        )
