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

from holidays.countries.egypt import Egypt, EG, EGY
from tests.common import CommonCountryTests


class TestEgypt(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Egypt)

    def test_country_aliases(self):
        self.assertAliases(Egypt, EG, EGY)

    def test_2019(self):
        self.assertHoliday(
            "2019-01-07",
            "2019-01-25",
            "2019-04-25",
            "2019-04-28",
            "2019-04-29",
            "2019-05-01",
            "2019-07-23",
            "2019-10-6",
        )

    def test_siani_liberation_day(self):
        self.assertHoliday("1983-04-25")
        self.assertNoHoliday("1982-04-25")

    def test_revolution_day(self):
        self.assertHoliday("1953-07-23")
        self.assertNoHoliday("1952-07-23")

    def test_25_jan_from_2009(self):
        # Before 2009 Jan 25th wasn't celebrated
        self.assertHoliday("2010-01-25")
        self.assertNoHoliday("2008-01-25")

        self.assertHolidayName("عيد الشرطة", "2011-01-25")
        self.assertHolidayName("عيد ثورة 25 يناير", "2012-01-25")

    def test_hijri_based(self):
        self.assertHoliday(
            "2019-06-05",
            "2019-08-10",
            "2019-08-11",
            "2019-08-12",
            "2019-08-31",
            "2019-11-09",
            # Arafat
            "2010-02-26",
            # Eid al-Fitr
            "2010-09-10",
            "2019-06-04",
            # Eid al-Adha
            "2007-01-02",
            "2019-08-11",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2019-08-31",
            # Prophet Muhammad's Birthday
            "2010-02-26",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2019-01-01", "رأس السنة الميلادية"),
            ("2019-01-07", "عيد الميلاد المجيد (تقويم قبطي)"),
            ("2019-01-25", "عيد ثورة 25 يناير"),
            ("2019-04-25", "عيد تحرير سيناء"),
            ("2019-04-28", "عيد الفصح القبطي"),
            ("2019-04-29", "شم النسيم"),
            ("2019-05-01", "عيد العمال"),
            ("2019-06-04", "(تقدير) عيد الفطر"),
            ("2019-06-05", "(تقدير) عطلة عيد الفطر"),
            ("2019-06-06", "(تقدير) عطلة عيد الفطر"),
            ("2019-06-30", "عيد ثورة 30 يونيو"),
            ("2019-07-23", "عيد ثورة 23 يوليو"),
            ("2019-08-10", "(تقدير) يوم عرفة"),
            ("2019-08-11", "(تقدير) عيد الأضحى"),
            ("2019-08-12", "(تقدير) عطلة عيد الأضحى"),
            ("2019-08-13", "(تقدير) عطلة عيد الأضحى"),
            ("2019-08-31", "(تقدير) رأس السنة الهجرية"),
            ("2019-10-06", "عيد القوات المسلحة"),
            ("2019-11-09", "(تقدير) عيد المولد النبوي"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2019-01-01", "New Year's Day"),
            ("2019-01-07", "Coptic Christmas Day"),
            ("2019-01-25", "January 25th Revolution Day"),
            ("2019-04-25", "Sinai Liberation Day"),
            ("2019-04-28", "Coptic Easter"),
            ("2019-04-29", "Sham El Nessim"),
            ("2019-05-01", "Labor Day"),
            ("2019-06-04", "Eid al-Fitr (estimated)"),
            ("2019-06-05", "Eid al-Fitr Holiday (estimated)"),
            ("2019-06-06", "Eid al-Fitr Holiday (estimated)"),
            ("2019-06-30", "June 30 Revolution Day"),
            ("2019-07-23", "July 23 Revolution Day"),
            ("2019-08-10", "Arafat Day (estimated)"),
            ("2019-08-11", "Eid al-Adha (estimated)"),
            ("2019-08-12", "Eid al-Adha Holiday (estimated)"),
            ("2019-08-13", "Eid al-Adha Holiday (estimated)"),
            ("2019-08-31", "Islamic New Year (estimated)"),
            ("2019-10-06", "Armed Forces Day"),
            ("2019-11-09", "Prophet's Birthday (estimated)"),
        )
