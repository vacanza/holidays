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

from holidays.entities.ISO_3166.AR import ArHolidays
from tests.common import CommonCountryTests


class TestArHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ArHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Carnival Day"),
            ("2022-03-01", "Carnival Day"),
            ("2022-03-24", "Memory's National Day for the Truth and Justice"),
            ("2022-04-02", "Veterans Day and the Fallen in the Malvinas War"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-18", "National Census Day 2022"),
            ("2022-05-25", "May Revolution Day"),
            ("2022-06-17", "Pass to the Immortality of General Don Martín Miguel de Güemes"),
            ("2022-06-20", "Pass to the Immortality of General Don Manuel Belgrano"),
            ("2022-07-09", "Independence Day"),
            ("2022-08-15", "Pass to the Immortality of General Don José de San Martin (observed)"),
            ("2022-10-07", "Bridge Public Holiday"),
            ("2022-10-10", "Respect for Cultural Diversity Day (observed)"),
            ("2022-11-20", "National Sovereignty Day"),
            ("2022-11-21", "Bridge Public Holiday"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-09", "Bridge Public Holiday"),
            ("2022-12-25", "Christmas Day"),
        )
