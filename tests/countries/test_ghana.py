#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.ghana import Ghana
from tests.common import CommonCountryTests


class TestGhana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ghana)

    def test_special_holidays(self):
        self.assertHoliday(
            "2017-07-03",
            "2018-07-02",
            "2019-08-05",
            "2019-08-12",
            "2019-09-23",
            "2020-05-25",
            "2020-12-28",
            "2021-03-08",
            "2021-05-03",
            "2021-12-27",
            "2021-12-28",
            "2022-01-03",
            "2022-03-07",
            "2022-05-02",
            "2022-07-11",
            "2022-12-27",
            "2023-01-02",
            "2023-01-09",
            "2023-04-24",
            "2024-01-08",
            "2024-06-17",
            "2024-08-05",
            "2024-09-23",
            "2025-03-31",
            "2025-04-01",
            "2025-07-04",
            "2025-09-22",
            "2026-01-09",
            "2026-07-03",
        )

    def test_new_year_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-01-07" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-03-06" for year in self.full_range))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name_2002 = "Workers' Day"
        name_2026 = "Labour Day"
        self.assertHolidayName(
            name_2002, (f"{year}-05-01" for year in range(self.start_year, 2026))
        )
        self.assertHolidayName(name_2026, (f"{year}-05-01" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name_2002, range(2026, self.end_year))
        self.assertNoHolidayName(name_2026, range(self.start_year, 2026))

    def test_african_union_day(self):
        name = "African Union Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(2002, 2020)))
        self.assertNoHolidayName(name, range(self.start_year, 2002), range(2020, self.end_year))

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(
            name,
            (
                f"{year}-07-01"
                for year in (*range(self.start_year, 2019), *range(2025, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(2019, 2025))

    def test_founders_day(self):
        name = "Founders' Day"
        self.assertHolidayName(name, (f"{year}-08-04" for year in range(2019, 2025)))
        self.assertNoHolidayName(name, range(self.start_year, 2019), range(2025, self.end_year))

    def test_founder_day(self):
        name_2009 = "Founder's Day"
        name_2019 = "Kwame Nkrumah Memorial Day"
        self.assertHolidayName(
            name_2009,
            (f"{year}-09-21" for year in (*range(2009, 2019), *range(2025, self.end_year))),
        )
        self.assertHolidayName(name_2019, (f"{year}-09-21" for year in range(2019, 2025)))
        self.assertNoHolidayName(name_2009, range(self.start_year, 2009), range(2019, 2025))
        self.assertNoHolidayName(
            name_2019, range(self.start_year, 2019), range(2025, self.end_year)
        )

    def test_farmers_day(self):
        name = "Farmers' Day"
        self.assertHolidayName(
            name,
            "2020-12-07",
            "2021-12-03",
            "2022-12-02",
            "2023-12-01",
            "2024-12-06",
            "2025-12-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in self.full_range))

    def test_eid_al_fitr(self):
        name = "Eid-ul-Fitr"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_shaqq_day(self):
        name = "Shaqq Day"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2026-03-21",
            "2027-03-10",
            "2028-02-27",
            "2029-02-15",
            "2030-02-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(2026, self.end_year))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(self.start_year, 2026))

    def test_eid_al_adha(self):
        name = "Eid-ul-Adha"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "Public Holiday"),
            ("2023-01-07", "Constitution Day"),
            ("2023-01-09", "Public Holiday"),
            ("2023-03-06", "Independence Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-22", "Eid-ul-Fitr"),
            ("2023-04-24", "Public Holiday"),
            ("2023-05-01", "Workers' Day"),
            ("2023-06-28", "Eid-ul-Adha"),
            ("2023-08-04", "Founders' Day"),
            ("2023-09-21", "Kwame Nkrumah Memorial Day"),
            ("2023-12-01", "Farmers' Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-01-07", "Constitution Day"),
            ("2024-01-08", "Public Holiday"),
            ("2024-03-06", "Independence Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-11", "Eid-ul-Fitr"),
            ("2024-05-01", "Workers' Day"),
            ("2024-06-16", "Eid-ul-Adha"),
            ("2024-06-17", "Public Holiday"),
            ("2024-08-04", "Founders' Day"),
            ("2024-08-05", "Public Holiday"),
            ("2024-09-21", "Kwame Nkrumah Memorial Day"),
            ("2024-09-23", "Public Holiday"),
            ("2024-12-06", "Farmers' Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-07", "Constitution Day"),
            ("2025-03-06", "Independence Day"),
            ("2025-03-30", "Eid-ul-Fitr"),
            ("2025-03-31", "Public Holiday"),
            ("2025-04-01", "Public Holiday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Workers' Day"),
            ("2025-06-06", "Eid-ul-Adha"),
            ("2025-07-01", "Republic Day"),
            ("2025-07-04", "Public Holiday"),
            ("2025-09-21", "Founder's Day"),
            ("2025-09-22", "Public Holiday"),
            ("2025-12-05", "Farmers' Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "New Year's Day"),
            ("2026-01-07", "Constitution Day"),
            ("2026-01-09", "Public Holiday"),
            ("2026-03-06", "Independence Day"),
            ("2026-03-20", "Eid-ul-Fitr"),
            ("2026-03-21", "Shaqq Day"),
            ("2026-04-03", "Good Friday"),
            ("2026-04-06", "Easter Monday"),
            ("2026-05-01", "Labour Day"),
            ("2026-05-27", "Eid-ul-Adha"),
            ("2026-07-01", "Republic Day"),
            ("2026-07-03", "Public Holiday"),
            ("2026-09-21", "Founder's Day"),
            ("2026-12-04", "Farmers' Day"),
            ("2026-12-25", "Christmas Day"),
            ("2026-12-26", "Boxing Day"),
        )
