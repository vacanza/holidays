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

from holidays.countries.jordan import Jordan, JO, JOR
from tests.common import CommonCountryTests


class TestJordan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Jordan)

    def test_country_aliases(self):
        self.assertAliases(Jordan, JO, JOR)

    def test_2024(self):
        self.assertHolidays(
            Jordan(years=2024),
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-02-08", "(تقدير) ليلة المعراج"),
            ("2024-04-10", "(تقدير) عيد الفطر"),
            ("2024-04-11", "(تقدير) عطلة عيد الفطر"),
            ("2024-04-12", "(تقدير) عطلة عيد الفطر"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-25", "عيد الإستقلال"),
            ("2024-06-15", "(تقدير) يوم عرفة"),
            ("2024-06-16", "(تقدير) عيد الأضحى"),
            ("2024-06-17", "(تقدير) عطلة عيد الأضحى"),
            ("2024-06-18", "(تقدير) عطلة عيد الأضحى"),
            ("2024-07-07", "(تقدير) رأس السنة الهجرية"),
            ("2024-09-15", "(تقدير) عيد المولد النبوي"),
            ("2024-12-25", "عيد الميلاد المجيد"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-02-08", "(تقدير) ليلة المعراج"),
            ("2024-04-10", "(تقدير) عيد الفطر"),
            ("2024-04-11", "(تقدير) عطلة عيد الفطر"),
            ("2024-04-12", "(تقدير) عطلة عيد الفطر"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-25", "عيد الإستقلال"),
            ("2024-06-15", "(تقدير) يوم عرفة"),
            ("2024-06-16", "(تقدير) عيد الأضحى"),
            ("2024-06-17", "(تقدير) عطلة عيد الأضحى"),
            ("2024-06-18", "(تقدير) عطلة عيد الأضحى"),
            ("2024-07-07", "(تقدير) رأس السنة الهجرية"),
            ("2024-09-15", "(تقدير) عيد المولد النبوي"),
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
