#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

# holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.aland_islands import AlandIslands


class TestAland(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.holidays = AlandIslands(years=range(1930, 2050), include_sundays=True)

    def test_fixed_date_holidays(self):
        # Group fixed date holidays in a single method
        fixed = {
            "Nyårsdagen": [f"{y}-01-01" for y in range(1930, 2050)],
            "Trettondedag jul": [f"{y}-01-06" for y in range(1930, 2050)],
            "Första maj": [f"{y}-05-01" for y in range(1939, 2050)],
            "Självstyrelsedagen": [f"{y}-06-09" for y in range(1920, 2050)],
            # etc...
            "Julafton": [f"{y}-12-24" for y in range(1930, 2050)],
            "Juldagen": [f"{y}-12-25" for y in range(1930, 2050)],
            "Annandag jul": [f"{y}-12-26" for y in range(1930, 2050)],
            "Nyårsafton": [f"{y}-12-31" for y in range(1930, 2050)],
        }
        for holiday_name, dates in fixed.items():
            self.assertHolidayName(holiday_name, dates)

        self.assertNoHolidayName("Första maj", range(1930, 1939))

    def test_movable_holidays(self):
        movable = {
            "Långfredagen": [
                "2019-04-19",
                "2020-04-10",
                "2021-04-02",
                "2022-04-15",
                "2023-04-07",
                "2024-03-29",
            ],
            "Påskdagen": [
                "2019-04-21",
                "2020-04-12",
                "2021-04-04",
                "2022-04-17",
                "2023-04-09",
                "2024-03-31",
            ],
            "Annandag påsk": [
                "2019-04-22",
                "2020-04-13",
                "2021-04-05",
                "2022-04-18",
                "2023-04-10",
                "2024-04-01",
            ],
        }
        for holiday_name, dates in movable.items():
            self.assertHolidayName(holiday_name, dates)

        self.assertHolidayName("Långfredagen", range(1930, 2050))

    def test_independence_day_finland(self):
        self.assertHolidayName("Självständighetsdagen", (f"{y}-12-06" for y in range(1917, 2050)))

        self.assertNoHolidayName("Självständighetsdagen", range(1900, 1917))

    def test_not_holiday(self):
        self.assertNoHoliday(
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2016-12-27",
            "2016-12-28",
        )
