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

from holidays.countries.tunisia import Tunisia
from tests.common import CommonCountryTests


class TestTunisia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tunisia)

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in self.full_range)
        )

    def test_revolution_and_youth_day(self):
        self.assertHolidayName("عيد الثورة والشباب", (f"{year}-01-14" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName("عيد الاستقلال", (f"{year}-03-20" for year in self.full_range))

    def test_martyrs_day(self):
        self.assertHolidayName("عيد الشهداء", (f"{year}-04-09" for year in self.full_range))

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in self.full_range))

    def test_republic_day(self):
        self.assertHolidayName("عيد الجمهورية", (f"{year}-07-25" for year in self.full_range))

    def test_womens_day(self):
        self.assertHolidayName("عيد المرأة", (f"{year}-08-13" for year in self.full_range))

    def test_evacuation_day(self):
        self.assertHolidayName("عيد الجلاء", (f"{year}-10-15" for year in self.full_range))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        name_holiday = "عطلة عيد الفطر"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name_holiday,
            "2020-05-25",
            "2020-05-26",
            "2021-05-14",
            "2021-05-15",
            "2022-05-03",
            "2022-05-04",
            "2023-04-22",
            "2023-04-23",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
        )
        years_single = (
            range(self.start_year, 1968),
            range(1969, 2000),
            range(2001, 2033),
            range(2034, self.end_year),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 1, *years_single)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 2, 1968, 2000, 2033)
        self.assertIslamicNoEstimatedHolidayNameCount(name_holiday, 2, *years_single)
        self.assertIslamicNoEstimatedHolidayNameCount(name_holiday, 4, 1968, 2000, 2033)

    def test_day_of_arafah(self):
        name = "يوم عرفة"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            1,
            range(self.start_year, 1974),
            range(1975, 2006),
            range(2007, 2039),
            range(2040, self.end_year),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 2, 1974, 2006, 2039)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        name_holiday = "عطلة عيد الأضحى"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name_holiday,
            "2020-08-01",
            "2020-08-02",
            "2021-07-21",
            "2021-07-22",
            "2022-07-10",
            "2022-07-11",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            1,
            range(self.start_year, 1974),
            range(1975, 2006),
            range(2007, 2039),
            range(2040, self.end_year),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 2, 1974, 2006, 2039)
        self.assertIslamicNoEstimatedHolidayNameCount(
            name_holiday,
            2,
            range(self.start_year, 1974),
            range(1975, 2007),
            range(2008, 2039),
            range(2040, self.end_year),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name_holiday, 4, 1974, 2007, 2039)

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            1,
            range(self.start_year, 1976),
            range(1977, 2008),
            range(2009, 2041),
            range(2042, self.end_year),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 2, 1976, 2008, 2041)

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            1,
            range(1951, 1982),
            range(1983, 2015),
            range(2016, 2047),
            range(2048, self.end_year),
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 2, 1950, 1982, 2015, 2047)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-01-14", "عيد الثورة والشباب"),
            ("2023-03-20", "عيد الاستقلال"),
            ("2023-04-09", "عيد الشهداء"),
            ("2023-04-21", "عيد الفطر (تقديري)"),
            ("2023-04-22", "عطلة عيد الفطر (تقديري)"),
            ("2023-04-23", "عطلة عيد الفطر (تقديري)"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-27", "يوم عرفة (تقديري)"),
            ("2023-06-28", "عيد الأضحى (تقديري)"),
            ("2023-06-29", "عطلة عيد الأضحى (تقديري)"),
            ("2023-06-30", "عطلة عيد الأضحى (تقديري)"),
            ("2023-07-19", "رأس السنة الهجرية (تقديري)"),
            ("2023-07-25", "عيد الجمهورية"),
            ("2023-08-13", "عيد المرأة"),
            ("2023-09-27", "عيد المولد النبوي (تقديري)"),
            ("2023-10-15", "عيد الجلاء"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-14", "Revolution and Youth Day"),
            ("2023-03-20", "Independence Day"),
            ("2023-04-09", "Martyrs' Day"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-23", "Eid al-Fitr Holiday (estimated)"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-27", "Day of Arafah (estimated)"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-30", "Eid al-Adha Holiday (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-07-25", "Republic Day"),
            ("2023-08-13", "Women's Day"),
            ("2023-09-27", "Prophet's Birthday (estimated)"),
            ("2023-10-15", "Evacuation Day"),
        )
