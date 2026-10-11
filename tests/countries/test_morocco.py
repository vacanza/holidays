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
            "2019-06-05",
            "2019-06-06",
            "2019-07-30",
            "2019-08-12",
            "2019-08-13",
            "2019-08-14",
            "2019-08-20",
            "2019-08-21",
            "2019-09-01",
            "2019-11-06",
            "2019-11-10",
            "2019-11-11",
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
        self.assertHoliday("2024-01-13")
        self.assertNoHoliday("2023-01-13")

    def test_independence_manifesto_day(self):
        self.assertHoliday("1945-01-11")
        self.assertNoHoliday("1944-01-11")

    def test_independence_day(self):
        self.assertHolidayName("عيد الاستقلال", "1957-11-18")
        self.assertHolidayName("عيد العرش", "1956-11-18", "1957-11-18")

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertHolidayName(
            name,
            "2015-07-18",
            "2015-07-19",
            "2016-07-06",
            "2016-07-07",
            "2017-06-26",
            "2017-06-27",
            "2018-06-15",
            "2018-06-16",
            "2019-06-05",
            "2019-06-06",
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-02",
            "2022-05-03",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2025-03-31",
            "2025-04-01",
            "2026-03-20",
            "2026-03-21",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2015-07-18",
            "2015-07-19",
            "2016-07-06",
            "2016-07-07",
            "2017-06-26",
            "2017-06-27",
            "2018-06-15",
            "2018-06-16",
            "2019-06-05",
            "2019-06-06",
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-02",
            "2022-05-03",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2025-03-31",
            "2025-04-01",
            "2026-03-20",
            "2026-03-21",
        )

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2015-09-24",
            "2015-09-25",
            "2016-09-12",
            "2016-09-13",
            "2017-09-01",
            "2017-09-02",
            "2018-08-22",
            "2018-08-23",
            "2019-08-12",
            "2019-08-13",
            "2020-07-31",
            "2020-08-01",
            "2021-07-21",
            "2021-07-22",
            "2022-07-10",
            "2022-07-11",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2025-06-07",
            "2025-06-08",
            "2026-05-27",
            "2026-05-28",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2015-09-24",
            "2015-09-25",
            "2016-09-12",
            "2016-09-13",
            "2017-09-01",
            "2017-09-02",
            "2018-08-22",
            "2018-08-23",
            "2019-08-12",
            "2019-08-13",
            "2020-07-31",
            "2020-08-01",
            "2021-07-21",
            "2021-07-22",
            "2022-07-10",
            "2022-07-11",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2025-06-07",
            "2025-06-08",
            "2026-05-27",
            "2026-05-28",
        )

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2015-10-15",
            "2016-10-03",
            "2017-09-22",
            "2018-09-11",
            "2019-09-01",
            "2020-08-21",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-27",
            "2026-06-17",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2015-10-15",
            "2016-10-03",
            "2017-09-22",
            "2018-09-11",
            "2019-09-01",
            "2020-08-21",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-27",
            "2026-06-17",
        )

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertHolidayName(
            name,
            "2015-12-24",
            "2015-12-25",
            "2016-12-12",
            "2016-12-13",
            "2017-12-01",
            "2017-12-02",
            "2018-11-20",
            "2018-11-21",
            "2019-11-10",
            "2019-11-11",
            "2020-10-29",
            "2020-10-30",
            "2021-10-19",
            "2021-10-20",
            "2022-10-09",
            "2022-10-10",
            "2023-09-28",
            "2023-09-29",
            "2024-09-16",
            "2024-09-17",
            "2025-09-05",
            "2025-09-06",
            "2026-08-25",
            "2026-08-26",
        )
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2015-12-24",
            "2015-12-25",
            "2016-12-12",
            "2016-12-13",
            "2017-12-01",
            "2017-12-02",
            "2018-11-20",
            "2018-11-21",
            "2019-11-10",
            "2019-11-11",
            "2020-10-29",
            "2020-10-30",
            "2021-10-19",
            "2021-10-20",
            "2022-10-09",
            "2022-10-10",
            "2023-09-28",
            "2023-09-29",
            "2024-09-16",
            "2024-09-17",
            "2025-09-05",
            "2025-09-06",
            "2026-08-25",
            "2026-08-26",
        )

    def test_hijri_based_estimated(self):
        self.assertHoliday(
            # Eid al-Adha
            "2006-01-10",
            "2006-12-31",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-01-11", "ذكرى تقديم وثيقة الاستقلال"),
            ("2023-04-22", "عيد الفطر"),
            ("2023-04-23", "عيد الفطر"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-29", "عيد الأضحى"),
            ("2023-06-30", "عيد الأضحى"),
            ("2023-07-19", "رأس السنة الهجرية"),
            ("2023-07-30", "عيد العرش"),
            ("2023-08-14", "ذكرى استرجاع إقليم وادي الذهب"),
            ("2023-08-20", "ذكرى ثورة الملك و الشعب"),
            ("2023-08-21", "عيد الشباب"),
            ("2023-09-28", "عيد المولد النبوي"),
            ("2023-09-29", "عيد المولد النبوي"),
            ("2023-11-06", "ذكرى المسيرة الخضراء"),
            ("2023-11-18", "عيد الاستقلال"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-11", "Proclamation of Independence Day"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-07-30", "Throne Day"),
            ("2023-08-14", "Oued Ed-Dahab Day"),
            ("2023-08-20", "Revolution Day"),
            ("2023-08-21", "Youth Day"),
            ("2023-09-28", "Prophet's Birthday"),
            ("2023-09-29", "Prophet's Birthday"),
            ("2023-11-06", "Green March"),
            ("2023-11-18", "Independence Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2023-01-01", "Nouvel an"),
            ("2023-01-11", "Manifeste de l'indépendance"),
            ("2023-04-22", "Fête de la rupture du jeûne"),
            ("2023-04-23", "Fête de la rupture du jeûne"),
            ("2023-05-01", "Fête du Travail"),
            ("2023-06-29", "Fête du sacrifice"),
            ("2023-06-30", "Fête du sacrifice"),
            ("2023-07-19", "Nouvel an musulman"),
            ("2023-07-30", "Fête du Trône"),
            ("2023-08-14", "Allégeance Oued Eddahab"),
            ("2023-08-20", "La révolution du roi et du peuple"),
            ("2023-08-21", "Fête de la Jeunesse"),
            ("2023-09-28", "Anniversaire du prophète"),
            ("2023-09-29", "Anniversaire du prophète"),
            ("2023-11-06", "La marche verte"),
            ("2023-11-18", "Fête de l'indépendance"),
        )
