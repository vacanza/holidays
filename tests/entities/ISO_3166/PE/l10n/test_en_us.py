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

from holidays.entities.ISO_3166.PE import PeHolidays
from tests.common import CommonCountryTests


class TestPeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PeHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "Labor Day"),
            ("2022-06-29", "Saint Peter and Saint Paul"),
            ("2022-07-28", "Independence Day"),
            ("2022-07-29", "Great Military Parade Day"),
            ("2022-08-06", "Battle of Junín Day"),
            ("2022-08-30", "Rose of Lima Day"),
            ("2022-10-08", "Battle of Angamos Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-09", "Battle of Ayacucho Day"),
            ("2022-12-25", "Christmas Day"),
        )
