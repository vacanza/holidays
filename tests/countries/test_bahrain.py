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

from holidays.countries.bahrain import Bahrain, BH, BAH
from tests.common import CommonCountryTests


class TestBahrain(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bahrain)

    def test_country_aliases(self):
        self.assertAliases(Bahrain, BH, BAH)

    def test_2022(self):
        self.assertHoliday(
            "2022-01-01",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-30",
            "2022-08-07",
            "2022-08-08",
            "2022-10-08",
            "2022-12-16",
            "2022-12-17",
        )

    def test_2023(self):
        self.assertHoliday(
            "2023-01-01",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2023-05-01",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2023-07-19",
            "2023-07-27",
            "2023-07-28",
            "2023-09-27",
            "2023-12-16",
            "2023-12-17",
        )

    def test_hijri_based(self):
        # Eid Al-Fitr.
        self.assertHoliday(
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
        )

        # Eid Al-Adha.
        self.assertHoliday(
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
        )

        # Islamic New Year.
        self.assertHoliday(
            "2008-01-10",
            "2008-12-29",
            "2020-08-20",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-04-21", "(تقدير) عيد الفطر"),
            ("2023-04-22", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-23", "(تقدير) عطلة عيد الفطر"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-28", "(تقدير) عيد الأضحى"),
            ("2023-06-29", "(تقدير) عطلة عيد الأضحى"),
            ("2023-06-30", "(تقدير) عطلة عيد الأضحى"),
            ("2023-07-19", "(تقدير) رأس السنة الهجرية"),
            ("2023-07-27", "(تقدير) ليلة عاشورة"),
            ("2023-07-28", "(تقدير) عاشورة"),
            ("2023-09-27", "(تقدير) عيد المولد النبوي"),
            ("2023-12-16", "اليوم الوطني"),
            ("2023-12-17", "اليوم الوطني"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-23", "Eid al-Fitr Holiday (estimated)"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-30", "Eid al-Adha Holiday (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-07-27", "Ashura Eve (estimated)"),
            ("2023-07-28", "Ashura (estimated)"),
            ("2023-09-27", "Prophet's Birthday (estimated)"),
            ("2023-12-16", "National Day"),
            ("2023-12-17", "National Day"),
        )
