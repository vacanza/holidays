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

from holidays.countries.algeria import Algeria, DZ, DZA
from tests.common import CommonCountryTests


class TestAlgeria(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Algeria)

    def test_country_aliases(self):
        self.assertAliases(Algeria, DZ, DZA)

    def test_2022(self):
        self.assertHoliday(
            "2022-01-01",
            "2022-01-12",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-07-05",
            "2022-07-09",
            "2022-07-10",
            "2022-11-01",
        )

    def test_new_year_day(self):
        self.assertHoliday(
            "2022-01-01",
            "2023-01-01",
        )

    def test_independence_day(self):
        self.assertNoHoliday(
            "1961-07-05",
            "1962-07-04",
        )
        self.assertHoliday(
            "1962-07-05",
            "1963-07-05",
        )

    def test_revolution_day(self):
        self.assertNoHoliday("1962-11-01")
        self.assertHoliday("1963-11-01")

    def test_amazigh_new_year(self):
        self.assertNoHoliday("2017-01-12")
        self.assertHoliday(
            "2018-01-12",
            "2023-01-12",
        )

    def test_labour_day(self):
        self.assertNoHoliday(
            "2021-05-02",
            "2022-05-04",
            "2023-05-02",
        )
        self.assertHoliday(
            "2021-05-01",
            "2022-05-01",
            "2023-05-01",
        )

    def test_islamic_holidays(self):
        # Eid al-Fitr - Feast Festive
        self.assertNoHoliday("2023-04-20")
        self.assertHoliday(
            "2023-04-21",
            "2023-04-22",
        )

        # Eid al-Adha - Scarfice Festive
        self.assertNoHoliday(
            "2023-06-27",
            "2023-07-02",
            "2024-07-15",
            "2024-07-19",
        )
        self.assertHoliday(
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
        )

        # Islamic New Year
        self.assertHoliday(
            "2008-01-10",
            "2008-12-29",
            "2020-08-20",
        )

        # Ashura
        self.assertNoHoliday("2023-07-29")
        self.assertHoliday("2023-07-28")

        # Mawlid / Prophet's Birthday
        self.assertNoHoliday(
            "2021-10-19",
            "2023-09-28",
        )
        self.assertHoliday(
            "2021-10-18",
            "2023-09-27",
        )

    def test_l10_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-01-12", "رأس السنة الأمازيغية"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "(تقدير) عيد الفطر"),
            ("2022-05-03", "(تقدير) عطلة عيد الفطر"),
            ("2022-07-05", "عيد الإستقلال"),
            ("2022-07-09", "(تقدير) عيد الأضحى"),
            ("2022-07-10", "(تقدير) عطلة عيد الأضحى"),
            ("2022-07-30", "(تقدير) رأس السنة الهجرية"),
            ("2022-08-08", "(تقدير) عاشورة"),
            ("2022-10-08", "(تقدير) عيد المولد النبوي"),
            ("2022-11-01", "عيد الثورة"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-12", "Amazigh New Year"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "Eid al-Fitr Holiday (estimated)"),
            ("2022-07-05", "Independence Day"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-10", "Eid al-Adha Holiday (estimated)"),
            ("2022-07-30", "Islamic New Year (estimated)"),
            ("2022-08-08", "Ashura (estimated)"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
            ("2022-11-01", "Revolution Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Nouvel an"),
            ("2022-01-12", "Nouvel an Amazigh"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Fête de la rupture du jeûne (estimé)"),
            ("2022-05-03", "Congé de fête de la rupture du jeûne (estimé)"),
            ("2022-07-05", "Fête de l'indépendance"),
            ("2022-07-09", "Fête du sacrifice (estimé)"),
            ("2022-07-10", "Congé de fête du sacrifice (estimé)"),
            ("2022-07-30", "Nouvel an musulman (estimé)"),
            ("2022-08-08", "Achoura (estimé)"),
            ("2022-10-08", "Anniversaire du prophète (estimé)"),
            ("2022-11-01", "Fête de la Révolution"),
        )
