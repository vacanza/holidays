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

from holidays.constants import OPTIONAL
from holidays.entities.ISO_3166.DK import DkHolidays
from tests.common import CommonCountryTests


class TestDkHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DkHolidays)

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertHolidays(
            ("2016-01-01", "Nytårsdag"),
            ("2016-03-24", "Skærtorsdag"),
            ("2016-03-25", "Langfredag"),
            ("2016-03-27", "Påskedag"),
            ("2016-03-28", "Anden påskedag"),
            ("2016-04-22", "Store bededag"),
            ("2016-05-05", "Kristi himmelfartsdag"),
            ("2016-05-15", "Pinsedag"),
            ("2016-05-16", "Anden pinsedag"),
            ("2016-12-25", "Juledag"),
            ("2016-12-26", "Anden juledag"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Nytårsdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
        )

    def test_2022_optional(self):
        self.assertHolidays(
            DkHolidays(categories=OPTIONAL, years=2022),
            ("2022-05-01", "Arbejdernes kampdag"),
            ("2022-06-05", "Grundlovsdag"),
            ("2022-12-24", "Juleaftensdag"),
            ("2022-12-31", "Nytårsaften"),
        )

    def test_2024(self):
        # https://www.officeholidays.com/countries/denmark/2024
        self.assertNoHoliday("2024-04-26")
        self.assertNoHolidayName("Store bededag", DkHolidays(years=2024))
