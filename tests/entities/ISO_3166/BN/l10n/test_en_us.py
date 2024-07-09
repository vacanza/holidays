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

from holidays.entities.ISO_3166.BN import BnHolidays
from tests.common import CommonCountryTests


class TestBnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BnHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Lunar New Year"),
            ("2023-01-23", "Lunar New Year (observed)"),
            ("2023-02-18", "Isra Mi'raj"),
            ("2023-02-23", "National Day"),
            ("2023-03-23", "First Day of Ramadan"),
            ("2023-04-08", "Anniversary of the revelation of the Quran"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-04-24", "Eid al-Fitr"),
            ("2023-04-25", "Eid al-Fitr (observed)"),
            ("2023-05-31", "Armed Forces Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-15", "Sultan Hassanal Bolkiah's Birthday"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-09-28", "Birth of the Prophet"),
            ("2023-12-25", "Christmas Day"),
        )
