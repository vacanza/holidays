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

from holidays.countries.isle_of_man import IsleOfMan, IM, IMN
from tests.common import CommonCountryTests


class TestIM(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IsleOfMan, years=range(1970, 2070))

    def test_country_aliases(self):
        self.assertAliases(IsleOfMan, IM, IMN)

    def test_1970(self):
        self.assertHolidays(
            IsleOfMan(years=1970),
            ("1970-03-27", "Good Friday"),
            ("1970-03-30", "Easter Monday"),
            ("1970-05-18", "Whit Monday"),
            ("1970-06-05", "TT Bank Holiday"),
            ("1970-07-05", "Tynwald Day"),
            ("1970-12-25", "Christmas Day"),
            ("1970-12-26", "Boxing Day"),
            ("1970-12-28", "Boxing Day (observed)"),
        )

    def test_2022(self):
        self.assertHolidays(
            IsleOfMan(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-06-02", "Spring Bank Holiday"),
            ("2022-06-03", "Platinum Jubilee of Elizabeth II; TT Bank Holiday"),
            ("2022-07-05", "Tynwald Day"),
            ("2022-08-29", "Late Summer Bank Holiday"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_tynwald_day(self):
        name = "Tynwald Day"
        self.assertHoliday(f"{year}-07-05" for year in range(1970, 1992))
        self.assertHolidayName(
            name,
            "1992-07-06",
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
            "1992-07-05",
            "2020-07-05",
            "2025-07-05",
            "2026-07-05",
        )
