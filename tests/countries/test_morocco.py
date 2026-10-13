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

from holidays.countries.morocco import Morocco
from tests.common import CommonCountryTests


class TestMorocco(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Morocco)

    def test_2019(self):
        self.assertHolidayDatesInYear(
            2019,
            "2019-01-01",
            "2019-01-11",
            "2019-05-01",
            "2019-06-04",
            "2019-06-05",
            "2019-07-30",
            "2019-08-11",
            "2019-08-12",
            "2019-08-14",
            "2019-08-20",
            "2019-08-21",
            "2019-08-31",
            "2019-11-06",
            "2019-11-09",
            "2019-11-10",
            "2019-11-18",
        )

    def test_1999(self):
        self.assertHolidayDatesInYear(
            1999,
            "1999-01-01",
            "1999-01-11",
            "1999-01-18",
            "1999-01-19",
            "1999-03-03",
            "1999-03-27",
            "1999-03-28",
            "1999-04-17",
            "1999-05-01",
            "1999-06-26",
            "1999-06-27",
            "1999-07-09",
            "1999-08-14",
            "1999-08-20",
            "1999-11-06",
            "1999-11-18",
        )

    def test_amazigh_new_year(self):
        name = "رأس السنة الأمازيغية"
        self.assertHolidayName(name, (f"{year}-01-14" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_unity_day(self):
        name = "عيد الوحدة"
        self.assertHolidayName(name, (f"{year}-10-31" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))

    def test_independence_manifesto_day(self):
        self.assertHoliday("1945-01-11")
        self.assertNoHoliday("1944-01-11")

    def test_independence_day(self):
        self.assertHolidayName("عيد الاستقلال", "1957-11-18")
        self.assertHolidayName("عيد العرش", "1956-11-18", "1957-11-18")

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid al-Fitr
            "2021-05-13",
            "2021-05-14",
            # Eid al-Adha
            "2006-01-10",
            "2006-12-31",
            "2021-07-20",
            "2021-07-21",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2021-08-09",
            # Prophet Muhammad's Birthday
            "2021-10-18",
            "2021-10-19",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "رأس السنة الميلادية"),
            ("2026-01-11", "ذكرى تقديم وثيقة الاستقلال"),
            ("2026-01-14", "رأس السنة الأمازيغية"),
            ("2026-03-20", "عيد الفطر (تقديري)"),
            ("2026-03-21", "عيد الفطر (تقديري)"),
            ("2026-05-01", "عيد العمال"),
            ("2026-05-27", "عيد الأضحى (تقديري)"),
            ("2026-05-28", "عيد الأضحى (تقديري)"),
            ("2026-06-16", "رأس السنة الهجرية (تقديري)"),
            ("2026-07-30", "عيد العرش"),
            ("2026-08-14", "ذكرى استرجاع إقليم وادي الذهب"),
            ("2026-08-20", "ذكرى ثورة الملك و الشعب"),
            ("2026-08-21", "عيد الشباب"),
            ("2026-08-25", "عيد المولد النبوي (تقديري)"),
            ("2026-08-26", "عيد المولد النبوي (تقديري)"),
            ("2026-10-31", "عيد الوحدة"),
            ("2026-11-06", "ذكرى المسيرة الخضراء"),
            ("2026-11-18", "عيد الاستقلال"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-01-11", "Proclamation of Independence Day"),
            ("2026-01-14", "Amazigh New Year"),
            ("2026-03-20", "Eid al-Fitr (estimated)"),
            ("2026-03-21", "Eid al-Fitr (estimated)"),
            ("2026-05-01", "Labor Day"),
            ("2026-05-27", "Eid al-Adha (estimated)"),
            ("2026-05-28", "Eid al-Adha (estimated)"),
            ("2026-06-16", "Islamic New Year (estimated)"),
            ("2026-07-30", "Throne Day"),
            ("2026-08-14", "Oued Ed-Dahab Day"),
            ("2026-08-20", "Revolution Day"),
            ("2026-08-21", "Youth Day"),
            ("2026-08-25", "Prophet's Birthday (estimated)"),
            ("2026-08-26", "Prophet's Birthday (estimated)"),
            ("2026-10-31", "Unity Day"),
            ("2026-11-06", "Green March"),
            ("2026-11-18", "Independence Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2026-01-01", "Nouvel an"),
            ("2026-01-11", "Manifeste de l'indépendance"),
            ("2026-01-14", "Nouvel an Amazigh"),
            ("2026-03-20", "Fête de la rupture du jeûne (estimé)"),
            ("2026-03-21", "Fête de la rupture du jeûne (estimé)"),
            ("2026-05-01", "Fête du Travail"),
            ("2026-05-27", "Fête du sacrifice (estimé)"),
            ("2026-05-28", "Fête du sacrifice (estimé)"),
            ("2026-06-16", "Nouvel an musulman (estimé)"),
            ("2026-07-30", "Fête du Trône"),
            ("2026-08-14", "Allégeance Oued Eddahab"),
            ("2026-08-20", "La révolution du roi et du peuple"),
            ("2026-08-21", "Fête de la Jeunesse"),
            ("2026-08-25", "Anniversaire du prophète (estimé)"),
            ("2026-08-26", "Anniversaire du prophète (estimé)"),
            ("2026-10-31", "Fête de l'Unité"),
            ("2026-11-06", "La marche verte"),
            ("2026-11-18", "Fête de l'indépendance"),
        )
