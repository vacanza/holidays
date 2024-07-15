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

from holidays.entities.ISO_3166.SA import SaHolidays
from tests.common import CommonCountryTests


class TestSaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-02-22", "Founding Day Holiday"),
            ("2023-04-21", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-22", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-23", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-24", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-25", "Eid al-Fitr Holiday (observed, estimated)"),
            ("2023-04-26", "Eid al-Fitr Holiday (observed, estimated)"),
            ("2023-06-27", "Arafat Day (estimated)"),
            ("2023-06-28", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-29", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-30", "Eid al-Adha Holiday (estimated)"),
            ("2023-07-02", "Eid al-Adha Holiday (observed, estimated)"),
            ("2023-09-23", "National Day Holiday"),
            ("2023-09-24", "National Day Holiday (observed)"),
        )
