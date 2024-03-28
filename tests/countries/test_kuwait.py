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

from holidays.countries.kuwait import Kuwait, KW, KWT
from tests.common import CommonCountryTests


class TestKuwait(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kuwait)

    def test_country_aliases(self):
        self.assertAliases(Kuwait, KW, KWT)

    def test_2022(self):
        self.assertHolidays(
            Kuwait(years=2022),
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-02-25", "اليوم الوطني"),
            ("2022-02-26", "يوم التحرير"),
            ("2022-02-28", "(تقدير) ليلة المعراج"),
            ("2022-05-02", "(تقدير) عيد الفطر"),
            ("2022-05-03", "(تقدير) عطلة عيد الفطر"),
            ("2022-05-04", "(تقدير) عطلة عيد الفطر"),
            ("2022-07-08", "(تقدير) يوم عرفة"),
            ("2022-07-09", "(تقدير) عيد الأضحى"),
            ("2022-07-10", "(تقدير) عطلة عيد الأضحى"),
            ("2022-07-11", "(تقدير) عطلة عيد الأضحى"),
            ("2022-07-30", "(تقدير) رأس السنة الهجرية"),
            ("2022-10-08", "(تقدير) عيد المولد النبوي"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-02-18", "(تقدير) ليلة المعراج"),
            ("2023-02-25", "اليوم الوطني"),
            ("2023-02-26", "يوم التحرير"),
            ("2023-04-21", "(تقدير) عيد الفطر"),
            ("2023-04-22", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-23", "(تقدير) عطلة عيد الفطر"),
            ("2023-06-27", "(تقدير) يوم عرفة"),
            ("2023-06-28", "(تقدير) عيد الأضحى"),
            ("2023-06-29", "(تقدير) عطلة عيد الأضحى"),
            ("2023-06-30", "(تقدير) عطلة عيد الأضحى"),
            ("2023-07-19", "(تقدير) رأس السنة الهجرية"),
            ("2023-09-27", "(تقدير) عيد المولد النبوي"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-18", "Isra and Miraj (estimated)"),
            ("2023-02-25", "National Day"),
            ("2023-02-26", "Liberation Day"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-23", "Eid al-Fitr Holiday (estimated)"),
            ("2023-06-27", "Arafat Day (estimated)"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-30", "Eid al-Adha Holiday (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-09-27", "Prophet's Birthday (estimated)"),
        )
