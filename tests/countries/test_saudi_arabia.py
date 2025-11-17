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

from holidays.countries.saudi_arabia import SaudiArabia
from tests.common import CommonCountryTests


class TestSaudiArabia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1950, 2050)
        super().setUpClass(SaudiArabia, years=years, years_non_observed=years)

    def test_special_holidays(self):
        self.assertHoliday("2022-11-23")

    def test_eid_al_fitr(self):
        name = "عطلة عيد الفطر"
        self.assertHolidayName(
            name,
            "2000-01-07",  # 30 Ramadan.
            "2000-01-08",
            "2000-01-09",
            "2000-01-10",
            "2000-12-26",  # 30 Ramadan.
            "2000-12-27",
            "2000-12-28",
            "2000-12-29",
            "2021-05-12",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-09",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
            "2033-01-02",  # 1 Shawwal.
            "2033-01-03",
            "2033-01-04",
            "2033-01-05",
            "2033-12-22",  # 30 Ramadan.
            "2033-12-23",
            "2033-12-24",
            "2033-12-25",
        )
        self.assertHolidayName(name, range(1950, 2050))

        obs_dt = (
            "2000-01-11",
            "2000-12-30",
            "2000-12-31",
            "2020-05-27",
            "2021-05-16",
            "2021-05-17",
            "2023-04-25",
            "2023-04-26",
            "2024-04-14",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_arafat_day(self):
        name = "يوم عرفة"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertHolidayName(name, range(1950, 2050))

    def test_eid_al_adha(self):
        name = "عطلة عيد الأضحى"
        self.assertHolidayName(
            name,
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertHolidayName(name, range(1950, 2050))

        obs_dt = (
            "2020-08-03",
            "2020-08-04",
            "2022-07-12",
            "2022-07-13",
            "2023-07-02",
            "2024-06-19",
            "2025-06-09",
            "2025-06-10",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_day(self):
        name = "اليوم الوطني"
        self.assertHolidayName(name, (f"{year}-09-23" for year in range(2005, 2050)))
        self.assertNoHolidayName(name, range(1950, 2005))

        obs_dt = (
            "2011-09-24",
            "2016-09-22",
            "2017-09-24",
            "2022-09-22",
            "2023-09-24",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_founding_day(self):
        name = "يوم التأسيسي"
        self.assertHolidayName(name, (f"{year}-02-22" for year in range(2022, 2050)))
        self.assertNoHolidayName(name, range(1950, 2022))

        obs_dt = (
            "2025-02-23",
            "2030-02-21",
            "2031-02-23",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_weekend(self):
        for dt in (
            "2013-06-20",  # THU.
            "2013-06-21",  # FRI.
            "2013-06-27",  # THU.
            "2013-06-28",  # FRI.
            "2013-06-29",  # SAT.
            "2013-07-05",  # FRI.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2013-06-22",  # SAT.
            "2013-06-23",  # SUN.
            "2013-06-30",  # SUN.
            "2013-07-04",  # THU.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_2022(self):
        self.assertHolidays(
            SaudiArabia(years=2022),
            ("2022-02-22", "يوم التأسيسي"),
            ("2022-05-01", "عطلة عيد الفطر"),
            ("2022-05-02", "عطلة عيد الفطر"),
            ("2022-05-03", "عطلة عيد الفطر"),
            ("2022-05-04", "عطلة عيد الفطر"),
            ("2022-07-08", "يوم عرفة"),
            ("2022-07-09", "عطلة عيد الأضحى"),
            ("2022-07-10", "عطلة عيد الأضحى"),
            ("2022-07-11", "عطلة عيد الأضحى"),
            ("2022-07-12", "عطلة عيد الأضحى (ملاحظة)"),
            ("2022-07-13", "عطلة عيد الأضحى (ملاحظة)"),
            ("2022-09-22", "اليوم الوطني (ملاحظة)"),
            ("2022-09-23", "اليوم الوطني"),
            ("2022-11-23", "يوم وطني"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-02-22", "يوم التأسيسي"),
            ("2023-04-21", "عطلة عيد الفطر"),
            ("2023-04-22", "عطلة عيد الفطر"),
            ("2023-04-23", "عطلة عيد الفطر"),
            ("2023-04-24", "عطلة عيد الفطر"),
            ("2023-04-25", "عطلة عيد الفطر (ملاحظة)"),
            ("2023-04-26", "عطلة عيد الفطر (ملاحظة)"),
            ("2023-06-27", "يوم عرفة"),
            ("2023-06-28", "عطلة عيد الأضحى"),
            ("2023-06-29", "عطلة عيد الأضحى"),
            ("2023-06-30", "عطلة عيد الأضحى"),
            ("2023-07-02", "عطلة عيد الأضحى (ملاحظة)"),
            ("2023-09-23", "اليوم الوطني"),
            ("2023-09-24", "اليوم الوطني (ملاحظة)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-02-22", "Founding Day Holiday"),
            ("2023-04-21", "Eid al-Fitr Holiday"),
            ("2023-04-22", "Eid al-Fitr Holiday"),
            ("2023-04-23", "Eid al-Fitr Holiday"),
            ("2023-04-24", "Eid al-Fitr Holiday"),
            ("2023-04-25", "Eid al-Fitr Holiday (observed)"),
            ("2023-04-26", "Eid al-Fitr Holiday (observed)"),
            ("2023-06-27", "Arafat Day"),
            ("2023-06-28", "Eid al-Adha Holiday"),
            ("2023-06-29", "Eid al-Adha Holiday"),
            ("2023-06-30", "Eid al-Adha Holiday"),
            ("2023-07-02", "Eid al-Adha Holiday (observed)"),
            ("2023-09-23", "National Day Holiday"),
            ("2023-09-24", "National Day Holiday (observed)"),
        )
