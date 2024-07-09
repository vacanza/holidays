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

from holidays.entities.ISO_3166.NO import NoHolidays
from tests.common import CommonCountryTests, SundayHolidays


class TestNoHolidays(CommonCountryTests, SundayHolidays, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NoHolidays)

    def test_new_years(self):
        self.assertHoliday("1900-01-01", "2017-01-01", "2023-01-01")

    def test_easter(self):
        self.assertHoliday(
            "2000-04-20",
            "2000-04-21",
            "2000-04-23",
            "2000-04-24",
            "2010-04-01",
            "2010-04-02",
            "2010-04-04",
            "2010-04-05",
            "2021-04-01",
            "2021-04-02",
            "2021-04-04",
            "2021-04-05",
            "2024-03-28",
            "2024-03-29",
            "2024-03-31",
            "2024-04-01",
        )

    def test_workers_day(self):
        self.assertHoliday("1947-05-01", "2017-05-01", "2023-05-01")
        self.assertNoHoliday("1946-05-01")
        self.assertNoHolidayName("Arbeidernes dag", NoHolidays(years=1946))

    def test_constitution_day(self):
        self.assertHoliday("1947-05-17", "2017-05-17", "2023-05-17")
        self.assertNoHoliday("1946-05-17")
        self.assertNoHolidayName("Grunnlovsdag", NoHolidays(years=1946))

    def test_pentecost(self):
        self.assertHoliday(
            "2000-06-11",
            "2000-06-12",
            "2010-05-23",
            "2010-05-24",
            "2023-05-28",
            "2023-05-29",
        )

    def test_christmas(self):
        self.assertHoliday(
            "1901-12-25",
            "1901-12-26",
            "2016-12-25",
            "2016-12-26",
        )

    def test_sundays(self):
        self.assertSundays(NoHolidays)  # Sundays are considered holidays in Norway.

    def test_not_holiday(self):
        # TODO: Add more dates that are often confused for being a holiday.

        # Sundays in Norway are considered holidays,
        # so make sure none of these are actually Sundays.
        self.assertNoHoliday(
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2017-02-09",
            "2017-02-10",
            "2001-12-24",
            "2001-05-16",
            "2001-05-18",
            "1999-12-31",
            "2016-12-31",
            "2016-12-27",
            "2016-12-28",
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Første nyttårsdag"),
            ("2022-04-14", "Skjærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Første påskedag"),
            ("2022-04-18", "Andre påskedag"),
            ("2022-05-01", "Arbeidernes dag"),
            ("2022-05-17", "Grunnlovsdag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Første pinsedag"),
            ("2022-06-06", "Andre pinsedag"),
            ("2022-12-25", "Første juledag"),
            ("2022-12-26", "Andre juledag"),
        )
