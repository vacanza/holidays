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

from holidays.constants import SCHOOL, WORKDAY
from holidays.countries.yemen import Yemen, YE, YEM
from tests.common import CommonCountryTests


class TestYemen(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1991, 2050)
        super().setUpClass(Yemen, years=years)
        cls.no_estimated_holidays = Yemen(years=years, islamic_show_estimated=False)
        cls.school_holidays = Yemen(categories=SCHOOL, years=years)
        cls.workday_holidays = Yemen(categories=WORKDAY, years=years)
        cls.workday_no_estimated_holidays = Yemen(
            categories=WORKDAY, years=years, islamic_show_estimated=False
        )

    def test_country_aliases(self):
        self.assertAliases(Yemen, YE, YEM)

    def test_no_holidays(self):
        self.assertNoHolidays(Yemen(years=1990))

    def test_labor_day(self):
        name = "عيد العمال"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1991, 2050)))
        obs_dt = (
            "2009-05-02",
            "2015-05-03",
            "2020-05-03",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_unity_day(self):
        name = "اليوم الوطني للجمهورية اليمنية"
        self.assertHolidayName(name, (f"{year}-05-22" for year in range(1991, 2050)))
        obs_dt = (
            "2009-05-23",
            "2015-05-24",
            "2020-05-27",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_revolution_day(self):
        name = "ثورة 26 سبتمبر المجيدة"
        self.assertHolidayName(name, (f"{year}-09-26" for year in range(1991, 2050)))
        obs_dt = (
            "2003-09-27",
            "2008-09-27",
            "2014-09-28",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_liberation_day(self):
        name = "ثورة 14 أكتوبر المجيدة"
        self.assertHolidayName(name, (f"{year}-10-14" for year in range(1991, 2050)))
        obs_dt = (
            "2011-10-15",
            "2016-10-16",
            "2022-10-16",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "عيد الجلاء"
        self.assertHolidayName(name, (f"{year}-11-30" for year in range(1991, 2050)))
        obs_dt = (
            "2007-12-01",
            "2012-12-01",
            "2018-12-02",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_hijri_new_year(self):
        name = "عيد رأس السنة الهجرية"
        dts = (
            "2020-08-20",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1991, 2050))
        obs_dt = (
            "1994-06-11",
            "2002-03-16",
            "2009-12-19",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        dts = (
            "2020-05-23",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-12",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-20",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-08",
            "2024-04-09",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-29",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1991, 2050))
        obs_dt = (
            "2020-05-27",
            "2021-05-16",
            "2023-04-24",
            "2024-04-14",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        dts = (
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2020-08-03",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-07-23",
            "2022-07-08",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
            "2023-06-27",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2023-07-01",
            "2024-06-15",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1991, 2050))
        obs_dt = (
            "2020-08-04",
            "2021-07-25",
            "2022-07-13",
            "2023-07-02",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_teachers_day(self):
        name = "عيد المعلم"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.school_holidays, (f"{year}-05-05" for year in range(2013, 2050))
        )
        self.assertNoHolidayName(name, self.school_holidays, range(1991, 2013))

    def test_mawlid(self):
        name = "المولد النبوي"
        dts = (
            "1991-09-20",
            "1992-09-09",
            "1993-08-29",
            "1994-08-19",
            "1995-08-08",
            "1996-07-27",
            "1997-07-16",
            "1998-07-06",
            "1999-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(2000, 2050))
        obs_dt = (
            "1991-09-21",
            "1994-08-20",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        dts = (
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, self.workday_no_estimated_holidays, dts)
        self.assertHolidayName(name, self.workday_no_estimated_holidays, range(2000, 2050))
        self.assertNoHolidayName(name, self.workday_no_estimated_holidays, range(1991, 2000))

    def test_isra_and_miraj(self):
        name = "ذكرى الإسراء والمعراج"
        self.assertNoHolidayName(name)
        dts = (
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertHolidayName(name, self.workday_no_estimated_holidays, dts)
        self.assertHolidayName(name, self.workday_no_estimated_holidays, range(2000, 2050))
        self.assertNoHolidayName(name, self.workday_no_estimated_holidays, range(1991, 2000))

    def test_victory_day(self):
        name = "ذكرى 7 يوليو"
        self.assertHolidayName(name, (f"{year}-07-07" for year in range(1991, 2000)))
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-07-07" for year in range(2000, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1991, 2000))

    def test_weekend(self):
        for dt in (
            "2013-08-08",  # THU.
            "2013-08-09",  # FRI.
            "2013-08-16",  # FRI.
            "2013-08-17",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2013-08-10",  # SAT.
            "2013-08-11",  # SUN.
            "2013-08-15",  # THU.
            "2013-08-18",  # SUN.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-02-18", "ذكرى الإسراء والمعراج"),
            ("2023-04-20", "عيد الفطر"),
            ("2023-04-21", "عيد الفطر"),
            ("2023-04-22", "عيد الفطر"),
            ("2023-04-23", "عيد الفطر"),
            ("2023-04-24", "عيد الفطر (ملاحظة)"),
            ("2023-05-01", "عيد العمال"),
            ("2023-05-05", "عيد المعلم"),
            ("2023-05-22", "اليوم الوطني للجمهورية اليمنية"),
            ("2023-06-27", "عيد الأضحى"),
            ("2023-06-28", "عيد الأضحى"),
            ("2023-06-29", "عيد الأضحى"),
            ("2023-06-30", "عيد الأضحى"),
            ("2023-07-01", "عيد الأضحى"),
            ("2023-07-02", "عيد الأضحى (ملاحظة)"),
            ("2023-07-07", "ذكرى 7 يوليو"),
            ("2023-07-19", "عيد رأس السنة الهجرية"),
            ("2023-09-26", "ثورة 26 سبتمبر المجيدة"),
            ("2023-09-27", "المولد النبوي"),
            ("2023-10-14", "ثورة 14 أكتوبر المجيدة"),
            ("2023-11-30", "عيد الجلاء"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-02-18", "Isra' and Mi'raj"),
            ("2023-04-20", "Eid al-Fitr"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-04-24", "Eid al-Fitr (observed)"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-05", "Teacher's Day"),
            ("2023-05-22", "Unity Day"),
            ("2023-06-27", "Eid al-Adha"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-01", "Eid al-Adha"),
            ("2023-07-02", "Eid al-Adha (observed)"),
            ("2023-07-07", "Victory Day"),
            ("2023-07-19", "Hijri New Year"),
            ("2023-09-26", "Revolution Day"),
            ("2023-09-27", "Prophet's Birthday"),
            ("2023-10-14", "Liberation Day"),
            ("2023-11-30", "Independence Day"),
        )
