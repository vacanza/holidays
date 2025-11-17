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

from holidays.countries.jordan import Jordan
from tests.common import CommonCountryTests


class TestJordan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Jordan)

    def test_2024(self):
        self.assertHolidays(
            Jordan(years=2024),
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-02-08", "ليلة المعراج (المقدرة)"),
            ("2024-04-10", "عيد الفطر (المقدرة)"),
            ("2024-04-11", "عطلة عيد الفطر (المقدرة)"),
            ("2024-04-12", "عطلة عيد الفطر (المقدرة)"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-25", "عيد الإستقلال"),
            ("2024-06-15", "يوم عرفة (المقدرة)"),
            ("2024-06-16", "عيد الأضحى (المقدرة)"),
            ("2024-06-17", "عطلة عيد الأضحى (المقدرة)"),
            ("2024-06-18", "عطلة عيد الأضحى (المقدرة)"),
            ("2024-07-07", "رأس السنة الهجرية (المقدرة)"),
            ("2024-09-15", "عيد المولد النبوي (المقدرة)"),
            ("2024-12-25", "عيد الميلاد المجيد"),
        )

    def test_weekend(self):
        for dt in (
            "1999-12-30",  # THU.
            "1999-12-31",  # FRI.
            "2000-01-07",  # FRI.
            "2000-01-08",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2000-01-01",  # SAT.
            "2000-01-02",  # SUN.
            "2000-01-06",  # THU.
            "2000-01-09",  # SUN.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-02-08", "ليلة المعراج (المقدرة)"),
            ("2024-04-10", "عيد الفطر (المقدرة)"),
            ("2024-04-11", "عطلة عيد الفطر (المقدرة)"),
            ("2024-04-12", "عطلة عيد الفطر (المقدرة)"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-25", "عيد الإستقلال"),
            ("2024-06-15", "يوم عرفة (المقدرة)"),
            ("2024-06-16", "عيد الأضحى (المقدرة)"),
            ("2024-06-17", "عطلة عيد الأضحى (المقدرة)"),
            ("2024-06-18", "عطلة عيد الأضحى (المقدرة)"),
            ("2024-07-07", "رأس السنة الهجرية (المقدرة)"),
            ("2024-09-15", "عيد المولد النبوي (المقدرة)"),
            ("2024-12-25", "عيد الميلاد المجيد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-08", "Isra' and Mi'raj (estimated)"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-04-11", "Eid al-Fitr Holiday (estimated)"),
            ("2024-04-12", "Eid al-Fitr Holiday (estimated)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-25", "Independence Day"),
            ("2024-06-15", "Arafat Day (estimated)"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha Holiday (estimated)"),
            ("2024-06-18", "Eid al-Adha Holiday (estimated)"),
            ("2024-07-07", "Islamic New Year (estimated)"),
            ("2024-09-15", "Prophet's Birthday (estimated)"),
            ("2024-12-25", "Christmas Day"),
        )
