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

from holidays.entities.ISO_3166.CN import CnHolidays
from tests.common import CommonCountryTests


class TestCnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CnHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-31", "Day off (substituted from 01/29/2022)"),
            ("2022-02-01", "Chinese New Year (Spring Festival)"),
            ("2022-02-02", "Chinese New Year (Spring Festival)"),
            ("2022-02-03", "Chinese New Year (Spring Festival)"),
            ("2022-02-04", "Day off (substituted from 01/30/2022)"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-04", "Day off (substituted from 04/02/2022)"),
            ("2022-04-05", "Tomb-Sweeping Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-05-03", "Day off (substituted from 04/24/2022)"),
            ("2022-05-04", "Day off (substituted from 05/07/2022); Youth Day"),
            ("2022-06-01", "Children's Day"),
            ("2022-06-03", "Dragon Boat Festival"),
            ("2022-08-01", "Army Day"),
            ("2022-09-10", "Mid-Autumn Festival"),
            ("2022-09-12", "Mid-Autumn Festival (observed)"),
            ("2022-10-01", "National Day"),
            ("2022-10-02", "National Day"),
            ("2022-10-03", "National Day"),
            ("2022-10-04", "National Day (observed)"),
            ("2022-10-05", "National Day (observed)"),
            ("2022-10-06", "Day off (substituted from 10/08/2022)"),
            ("2022-10-07", "Day off (substituted from 10/09/2022)"),
        )
