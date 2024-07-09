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

from holidays.entities.ISO_3166.EG import EgHolidays
from tests.common import CommonCountryTests


class TestEgypt(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EgHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2019-01-01", "New Year's Day"),
            ("2019-01-07", "Coptic Christmas Day"),
            ("2019-01-25", "January 25th Revolution Day"),
            ("2019-04-25", "Sinai Liberation Day"),
            ("2019-04-28", "Coptic Easter"),
            ("2019-04-29", "Sham El Nessim"),
            ("2019-05-01", "Labor Day"),
            ("2019-06-04", "Eid al-Fitr (estimated)"),
            ("2019-06-05", "Eid al-Fitr Holiday (estimated)"),
            ("2019-06-06", "Eid al-Fitr Holiday (estimated)"),
            ("2019-06-30", "June 30 Revolution Day"),
            ("2019-07-23", "July 23 Revolution Day"),
            ("2019-08-10", "Arafat Day (estimated)"),
            ("2019-08-11", "Eid al-Adha (estimated)"),
            ("2019-08-12", "Eid al-Adha Holiday (estimated)"),
            ("2019-08-13", "Eid al-Adha Holiday (estimated)"),
            ("2019-08-31", "Islamic New Year (estimated)"),
            ("2019-10-06", "Armed Forces Day"),
            ("2019-11-09", "Prophet's Birthday (estimated)"),
        )
