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

from holidays.countries.united_arab_emirates import UnitedArabEmirates, AE, ARE
from tests.common import CommonCountryTests


class TestUnitedArabEmirates(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedArabEmirates, years=range(2014, 2024))

    def test_country_aliases(self):
        self.assertAliases(UnitedArabEmirates, AE, ARE)

    def test_2020(self):
        self.assertHolidayDates(
            UnitedArabEmirates(years=2020),
            "2020-01-01",
            "2020-05-23",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2020-08-23",
            "2020-10-29",
            "2020-12-01",
            "2020-12-02",
            "2020-12-03",
        )

    def test_commemoration_day(self):
        self.assertNoHoliday("2014-11-30")
        self.assertNoHolidayName("يوم الشهيد", 2014, 2023)
        self.assertHoliday(f"{year}-11-30" for year in range(2015, 2019))
        self.assertNoHoliday("2019-11-30")
        self.assertHoliday(f"{year}-12-01" for year in range(2019, 2023))

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid Al-Fitr
            "2018-06-14",
            "2018-06-15",
            "2018-06-16",
            "2020-05-23",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            # Arafat Day & Eid Al-Adha
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2023-06-27",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2018-09-11",
            "2019-08-31",
            "2020-08-23",
            "2021-08-12",
            "2022-07-30",
            "2023-07-21",
            # Isra' and Mi'raj
            "2018-04-13",
            # Prophet's Birthday
            "2018-11-19",
            "2019-11-09",
            "2020-10-29",
            "2021-10-21",
            "2022-10-08",
            "2023-09-29",
        )
        self.assertNoHoliday("2018-06-13")  # Eid Al-Fitr Eve
        self.assertNoHolidayName("ليلة المعراج", range(2019, 2024))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "رأس السنة الميلادية"),
            ("2018-04-13", "ليلة المعراج"),
            ("2018-06-14", "عيد الفطر"),
            ("2018-06-15", "عطلة عيد الفطر"),
            ("2018-06-16", "عطلة عيد الفطر"),
            ("2018-08-20", "وقفة عرفة"),
            ("2018-08-21", "عيد الأضحى"),
            ("2018-08-22", "عطلة عيد الأضحى"),
            ("2018-08-23", "عطلة عيد الأضحى"),
            ("2018-09-11", "رأس السنة الهجرية"),
            ("2018-11-19", "عيد المولد النبوي"),
            ("2018-11-30", "يوم الشهيد"),
            ("2018-12-02", "اليوم الوطني"),
            ("2018-12-03", "اليوم الوطني"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-04-13", "Isra' and Mi'raj"),
            ("2018-06-14", "Eid al-Fitr"),
            ("2018-06-15", "Eid al-Fitr Holiday"),
            ("2018-06-16", "Eid al-Fitr Holiday"),
            ("2018-08-20", "Arafat Day"),
            ("2018-08-21", "Eid al-Adha"),
            ("2018-08-22", "Eid al-Adha Holiday"),
            ("2018-08-23", "Eid al-Adha Holiday"),
            ("2018-09-11", "Islamic New Year"),
            ("2018-11-19", "Prophet's Birthday"),
            ("2018-11-30", "Commemoration Day"),
            ("2018-12-02", "National Day"),
            ("2018-12-03", "National Day"),
        )
