#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.isle_of_man import IsleOfMan, IM, IMN
from tests.common import TestCase


class TestIM(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IsleOfMan)

    def test_country_aliases(self):
        self.assertCountryAliases(IsleOfMan, IM, IMN)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (Observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-06-02", "Spring Bank Holiday"),
            (
                "2022-06-03",
                "Platinum Jubilee of Elizabeth II; TT Bank Holiday",
            ),
            ("2022-07-05", "Tynwald Day"),
            ("2022-08-29", "Late Summer Bank Holiday"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (Observed)"),
        )

    def test_tynwald_day(self):
        self.assertHolidaysName(
            "Tynwald Day",
            "2019-07-05",
            "2020-07-06",
            "2021-07-05",
            "2022-07-05",
            "2023-07-05",
            "2024-07-05",
            "2025-07-07",
            "2026-07-06",
        )
        self.assertNoHoliday(
            "2020-07-05",
            "2025-07-05",
            "2026-07-05",
        )
