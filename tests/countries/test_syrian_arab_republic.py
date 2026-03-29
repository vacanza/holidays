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

from holidays.countries.syrian_arab_republic import SyrianArabRepublic
from tests.common import CommonCountryTests


class TestSyrianArabRepublic(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2004, 2050)
        super().setUpClass(SyrianArabRepublic, years=years)
        cls.no_estimated_holidays = SyrianArabRepublic(years=years, islamic_show_estimated=False)

    def test_new_years_day(self):
        self.assertHolidayName(
            "عيد رأس السنة الميلادية", (f"{year}-01-01" for year in range(2004, 2050))
        )

    def test_revolution_day(self):
        self.assertHolidayName("الثورة السورية", (f"{year}-03-08" for year in range(2004, 2050)))

    def test_mothers_day(self):
        self.assertHolidayName("عيد الأم", (f"{year}-03-21" for year in range(2004, 2050)))

    def test_gregorian_easter_sunday(self):
        name = "عيد الفصح حسب التقويم الغربي"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(2004, 2050))

    def test_julian_easter_sunday(self):
        name = "عيد الفصح حسب التقويم الشرقي"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(2004, 2050))

    def test_independence_day(self):
        self.assertHolidayName("عيد الاستقلال", (f"{year}-04-17" for year in range(2004, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in range(2004, 2050)))

    def test_martyrs_day(self):
        self.assertHolidayName("عيد الشهداء", (f"{year}-05-06" for year in range(2004, 2050)))

    def test_tishreen_liberation_war_day(self):
        self.assertHolidayName(
            "ذكرى حرب تشرين التحريرية", (f"{year}-10-06" for year in range(2004, 2050))
        )

    def test_christmas_day(self):
        name = "عيد الميلاد"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(2004, 2024))

    def test_boxing_day(self):
        name = "يوم الصناديق"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(2004, 2024))

    def test_hijri_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))

    def test_mawlid(self):
        name = "عيد المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-08",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-27",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-15",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-05",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "عيد رأس السنة الميلادية"),
            ("2024-03-08", "الثورة السورية"),
            ("2024-03-21", "عيد الأم"),
            ("2024-03-31", "عيد الفصح حسب التقويم الغربي"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عيد الفطر"),
            ("2024-04-12", "عيد الفطر"),
            ("2024-04-17", "عيد الاستقلال"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-05", "عيد الفصح حسب التقويم الشرقي"),
            ("2024-05-06", "عيد الشهداء"),
            ("2024-06-15", "عيد الأضحى"),
            ("2024-06-16", "عيد الأضحى"),
            ("2024-06-17", "عيد الأضحى"),
            ("2024-06-18", "عيد الأضحى"),
            ("2024-07-07", "رأس السنة الهجرية"),
            ("2024-09-15", "عيد المولد النبوي الشريف"),
            ("2024-10-06", "ذكرى حرب تشرين التحريرية"),
            ("2024-12-25", "عيد الميلاد"),
            ("2024-12-26", "يوم الصناديق"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-08", "Revolution Day"),
            ("2024-03-21", "Mother's Day"),
            ("2024-03-31", "Gregorian Easter Sunday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr"),
            ("2024-04-12", "Eid al-Fitr"),
            ("2024-04-17", "Independence Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-05", "Julian Easter Sunday"),
            ("2024-05-06", "Martyrs' Day"),
            ("2024-06-15", "Eid al-Adha"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-06-18", "Eid al-Adha"),
            ("2024-07-07", "Islamic New Year"),
            ("2024-09-15", "Prophet's Birthday"),
            ("2024-10-06", "Tishreen Liberation War Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
