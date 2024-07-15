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
        super().setUpClass(RuHolidays)

    def test_ru(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Новогодние каникулы"),
            ("2018-01-02", "Новогодние каникулы"),
            ("2018-01-03", "Новогодние каникулы"),
            ("2018-01-04", "Новогодние каникулы"),
            ("2018-01-05", "Новогодние каникулы"),
            ("2018-01-06", "Новогодние каникулы"),
            ("2018-01-07", "Рождество Христово"),
            ("2018-01-08", "Новогодние каникулы"),
            ("2018-02-23", "День защитника Отечества"),
            ("2018-03-08", "Международный женский день"),
            ("2018-05-01", "Праздник Весны и Труда"),
            ("2018-05-09", "День Победы"),
            ("2018-06-12", "День России"),
            ("2018-11-04", "День народного единства"),
        )
