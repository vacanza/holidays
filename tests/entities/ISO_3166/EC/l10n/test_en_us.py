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

from holidays.entities.ISO_3166.EC import EcHolidays
from tests.common import CommonCountryTests


class TestEcHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EcHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Carnival"),
            ("2022-03-01", "Carnival"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-05-23", "The Battle of Pichincha (observed)"),
            ("2022-05-24", "The Battle of Pichincha"),
            ("2022-08-10", "Declaration of Independence of Quito"),
            ("2022-08-12", "Declaration of Independence of Quito (observed)"),
            ("2022-10-09", "Independence of Guayaquil"),
            ("2022-10-10", "Independence of Guayaquil (observed)"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-11-03", "Independence of Cuenca"),
            ("2022-11-04", "All Souls' Day (observed); Independence of Cuenca (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )
