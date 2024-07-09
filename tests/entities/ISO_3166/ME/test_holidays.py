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

from holidays.entities.ISO_3166.ME import MeHolidays
from tests.common import CommonCountryTests


class TestMeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MeHolidays)

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "New Year's Day"),
            ("2021-01-02", "New Year's Day"),
            ("2021-01-06", "Orthodox Christmas Eve"),
            ("2021-01-07", "Orthodox Christmas"),
            ("2021-04-30", "Orthodox Good Friday"),
            ("2021-05-01", "Labour Day"),
            ("2021-05-02", "Labour Day; Orthodox Easter Sunday"),
            ("2021-05-03", "Labour Day (observed); Orthodox Easter Monday"),
            ("2021-05-21", "Independence Day"),
            ("2021-05-22", "Independence Day"),
            ("2021-07-13", "Statehood Day"),
            ("2021-07-14", "Statehood Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-06", "Orthodox Christmas Eve"),
            ("2022-01-07", "Orthodox Christmas"),
            ("2022-04-22", "Orthodox Good Friday"),
            ("2022-04-24", "Orthodox Easter Sunday"),
            ("2022-04-25", "Orthodox Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day"),
            ("2022-05-03", "Labour Day (observed)"),
            ("2022-05-21", "Independence Day"),
            ("2022-05-22", "Independence Day"),
            ("2022-05-23", "Independence Day (observed)"),
            ("2022-07-13", "Statehood Day"),
            ("2022-07-14", "Statehood Day"),
        )

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day"),
            ("2023-01-03", "New Year's Day (observed)"),
            ("2023-01-06", "Orthodox Christmas Eve"),
            ("2023-01-07", "Orthodox Christmas"),
            ("2023-04-14", "Orthodox Good Friday"),
            ("2023-04-16", "Orthodox Easter Sunday"),
            ("2023-04-17", "Orthodox Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-02", "Labour Day"),
            ("2023-05-21", "Independence Day"),
            ("2023-05-22", "Independence Day"),
            ("2023-05-23", "Independence Day (observed)"),
            ("2023-07-13", "Statehood Day"),
            ("2023-07-14", "Statehood Day"),
        )
