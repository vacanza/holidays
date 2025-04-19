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

from unittest import TestCase

from holidays.countries.syrian_arab_republic import SyrianArabRepublic, SY, SYR
from tests.common import CommonCountryTests


class TestSyrianArabRepublic(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1940, 2050)
        super().setUpClass(SyrianArabRepublic, years=years)
        cls.no_estimated_holidays = SyrianArabRepublic(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(SyrianArabRepublic, SY, SYR)

    def test_no_holidays(self):
        self.assertNoHolidays(SyrianArabRepublic(years=1939))

    def test_new_year(self):
        name = "رأس السنة الميلادية"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.years))

    def test_mothers_day(self):
        name = "عيد الأم"
        self.assertHolidayName(name, (f"{year}-03-21" for year in self.years))

    def test_evacuation_day(self):
        name = "عيد الجلاء"
        self.assertHolidayName(name, (f"{year}-04-17" for year in self.years))

    def test_labor_day(self):
        name = "عيد العمال"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.years))

    def test_martyrs_day(self):
        name = "عيد الشهداء"
        self.assertHolidayName(name, (f"{year}-05-06" for year in self.years))

    def test_revolution_day(self):
        name = "عيد الثورة"
        self.assertHolidayName(name, (f"{year}-03-08" for year in self.years))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        dts = (
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1940, 2050))

    def test_mawlid(self):
        name = "مولد النبي"
        dts = (
            "2020-10-28",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1940, 2050))

    def test_isra_and_miraj(self):
        name = "الإسراء والمعراج"
        dts = (
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-02-08",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1940, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        dts = (
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1940, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        dts = (
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1940, 2050))

    def test_christmas_day(self):
        name = "عيد الميلاد المجيد"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.years))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-03-08", "عيد الثورة"),
            ("2023-03-21", "عيد الأم"),
            ("2023-04-17", "عيد الجلاء"),
            ("2023-05-01", "عيد العمال"),
            ("2023-05-06", "عيد الشهداء"),
            ("2023-06-28", "عيد الأضحى"),
            ("2023-06-29", "عيد الأضحى"),
            ("2023-06-30", "عيد الأضحى"),
            ("2023-07-19", "رأس السنة الهجرية"),
            ("2023-09-27", "مولد النبي"),
            ("2023-12-25", "عيد الميلاد المجيد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-03-08", "Revolution Day"),
            ("2023-03-21", "Mother's Day"),
            ("2023-04-17", "Evacuation Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-06", "Martyrs' Day"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-09-27", "Prophet's Birthday"),
            ("2023-12-25", "Christmas Day"),
        )
