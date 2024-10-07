#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.tunisia import Tunisia, TN, TUN
from tests.common import CommonCountryTests


class TestTunisia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tunisia)

    def test_country_aliases(self):
        self.assertAliases(Tunisia, TN, TUN)

    def test_2021(self):
        self.assertHolidayDates(
            "2021-01-01",
            "2021-01-14",
            "2021-03-20",
            "2021-04-09",
            "2021-05-01",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-07-25",
            "2021-08-09",
            "2021-08-13",
            "2021-10-15",
            "2021-10-18",
        )

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid al-Fitr
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            # Eid al-Adha
            "2006-01-10",
            "2006-12-31",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2021-08-09",
            # Prophet Muhammad's Birthday
            "2021-10-18",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-01-14", "عيد الثورة والشباب"),
            ("2023-03-20", "عيد الإستقلال"),
            ("2023-04-09", "عيد الشهداء"),
            ("2023-04-21", "(تقدير) عيد الفطر"),
            ("2023-04-22", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-23", "(تقدير) عطلة عيد الفطر"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-27", "(تقدير) يوم عرفة"),
            ("2023-06-28", "(تقدير) عيد الأضحى"),
            ("2023-06-29", "(تقدير) عطلة عيد الأضحى"),
            ("2023-06-30", "(تقدير) عطلة عيد الأضحى"),
            ("2023-07-19", "(تقدير) رأس السنة الهجرية"),
            ("2023-07-25", "عيد الجمهورية"),
            ("2023-08-13", "عيد المرأة"),
            ("2023-09-27", "(تقدير) عيد المولد النبوي"),
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
            ("2023-06-27", "Arafat Day (estimated)"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-30", "Eid al-Adha Holiday (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-07-25", "Republic Day"),
            ("2023-08-13", "Women's Day"),
            ("2023-09-27", "Prophet's Birthday (estimated)"),
            ("2023-10-15", "Evacuation Day"),
        )
