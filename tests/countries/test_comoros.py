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

from holidays.countries.comoros import Comoros
from tests.common import CommonCountryTests


class TestComoros(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Comoros)

    def test_special_holidays(self):
        self.assertHolidayName("Jour férié national", "2024-04-13")
        self.assertHolidayName("Journée chômée partielle d'élection", "2025-01-30")

    def test_new_years_day(self):
        self.assertHolidayName("Jour de l'an", (f"{year}-01-01" for year in self.full_range))

    def test_cheikh_al_maarouf_day(self):
        name = "Journée Cheikh Al Maarouf"
        self.assertHolidayName(name, (f"{year}-03-18" for year in range(self.start_year, 2026)))
        self.assertNoHolidayName(name, range(2026, self.end_year))

    def test_reconciliation_day(self):
        name = "Jour de la Réconciliation nationale"
        self.assertHolidayName(name, (f"{year}-02-17" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))

    def test_labor_day(self):
        self.assertHolidayName(
            "Fête internationale du Travail", (f"{year}-05-01" for year in self.full_range)
        )

    def test_national_day(self):
        self.assertHolidayName(
            "Fête de l'Indépendance", (f"{year}-07-06" for year in self.full_range)
        )

    def test_day_after_independence_day(self):
        name = "Lendemain de la Fête d'Indépendance"
        self.assertHolidayName(name, (f"{year}-07-07" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))

    def test_admission_to_un_day(self):
        name_2006 = "Journée Maoré"
        name_2026 = "Jour de l'Admission des Comores aux Nations Unies"
        self.assertHolidayName(name_2006, (f"{year}-11-12" for year in range(2006, 2026)))
        self.assertHolidayName(name_2026, (f"{year}-11-12" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(
            name_2006, range(self.start_year, 2006), range(2026, self.end_year)
        )
        self.assertNoHolidayName(name_2026, range(self.start_year, 2026))

    def test_islamic_new_year(self):
        name = "Premier jour de l'an musulman"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "Jour de la Naissance du Prophète Muhammad"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_isra_and_miraj(self):
        name = "Miradj"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, range(self.start_year, 2026))
        self.assertNoIslamicNoEstimatedHolidayName(name, range(2026, self.end_year))

    def test_eid_al_fitr(self):
        name = "Id-El-Fitr"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 3, set(self.full_range) - {2000, 2033})
        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, 2000, 2033)

    def test_eid_al_adha(self):
        name = "Id-El-Kabir"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2020-08-01",
            "2021-07-20",
            "2021-07-21",
            "2022-07-09",
            "2022-07-10",
            "2023-06-28",
            "2023-06-29",
            "2024-06-16",
            "2024-06-17",
            "2025-06-06",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, set(self.full_range) - {2006, 2007, 2039}
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 3, 2006, 2007)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 2039)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-02-28", "Miradj (estimé)"),
            ("2022-03-18", "Journée Cheikh Al Maarouf"),
            ("2022-05-01", "Fête internationale du Travail"),
            ("2022-05-02", "Id-El-Fitr (estimé)"),
            ("2022-05-03", "Id-El-Fitr (estimé)"),
            ("2022-05-04", "Id-El-Fitr (estimé)"),
            ("2022-07-06", "Fête de l'Indépendance"),
            ("2022-07-09", "Id-El-Kabir (estimé)"),
            ("2022-07-10", "Id-El-Kabir (estimé)"),
            ("2022-07-30", "Premier jour de l'an musulman (estimé)"),
            ("2022-10-08", "Jour de la Naissance du Prophète Muhammad (estimé)"),
            ("2022-11-12", "Journée Maoré"),
        )
        self.assertLocalizedHolidays(
            ("2026-01-01", "Jour de l'an"),
            ("2026-02-17", "Jour de la Réconciliation nationale"),
            ("2026-03-20", "Id-El-Fitr (estimé)"),
            ("2026-03-21", "Id-El-Fitr (estimé)"),
            ("2026-03-22", "Id-El-Fitr (estimé)"),
            ("2026-05-01", "Fête internationale du Travail"),
            ("2026-05-27", "Id-El-Kabir (estimé)"),
            ("2026-05-28", "Id-El-Kabir (estimé)"),
            ("2026-06-16", "Premier jour de l'an musulman (estimé)"),
            ("2026-07-06", "Fête de l'Indépendance"),
            ("2026-07-07", "Lendemain de la Fête d'Indépendance"),
            ("2026-08-25", "Jour de la Naissance du Prophète Muhammad (estimé)"),
            ("2026-11-12", "Jour de l'Admission des Comores aux Nations Unies"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-02-28", "الإسراء والمعراج (تقديري)"),
            ("2022-03-18", "يوم الشيخ المعروف"),
            ("2022-05-01", "عيد العمال الدولي"),
            ("2022-05-02", "عيد الفطر (تقديري)"),
            ("2022-05-03", "عيد الفطر (تقديري)"),
            ("2022-05-04", "عيد الفطر (تقديري)"),
            ("2022-07-06", "عيد الاستقلال"),
            ("2022-07-09", "عيد الأضحى (تقديري)"),
            ("2022-07-10", "عيد الأضحى (تقديري)"),
            ("2022-07-30", "رأس السنة الهجرية (تقديري)"),
            ("2022-10-08", "المولد النبوي الشريف (تقديري)"),
            ("2022-11-12", "يوم مايوت"),
        )
        self.assertLocalizedHolidays(
            "ar",
            ("2026-01-01", "رأس السنة الميلادية"),
            ("2026-02-17", "يوم المصالحة الوطنية"),
            ("2026-03-20", "عيد الفطر (تقديري)"),
            ("2026-03-21", "عيد الفطر (تقديري)"),
            ("2026-03-22", "عيد الفطر (تقديري)"),
            ("2026-05-01", "عيد العمال الدولي"),
            ("2026-05-27", "عيد الأضحى (تقديري)"),
            ("2026-05-28", "عيد الأضحى (تقديري)"),
            ("2026-06-16", "رأس السنة الهجرية (تقديري)"),
            ("2026-07-06", "عيد الاستقلال"),
            ("2026-07-07", "اليوم التالي لعيد الاستقلال"),
            ("2026-08-25", "المولد النبوي الشريف (تقديري)"),
            ("2026-11-12", "يوم انضمام جزر القمر إلى الأمم المتحدة"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Isra' and Mi'raj (estimated)"),
            ("2022-03-18", "Cheikh al Maarouf Day"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "Eid al-Fitr (estimated)"),
            ("2022-05-04", "Eid al-Fitr (estimated)"),
            ("2022-07-06", "Independence Day"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-10", "Eid al-Adha (estimated)"),
            ("2022-07-30", "Islamic New Year (estimated)"),
            ("2022-10-08", "Prophet's Birthday (estimated)"),
            ("2022-11-12", "Maore Day"),
        )
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-02-17", "National Reconciliation Day"),
            ("2026-03-20", "Eid al-Fitr (estimated)"),
            ("2026-03-21", "Eid al-Fitr (estimated)"),
            ("2026-03-22", "Eid al-Fitr (estimated)"),
            ("2026-05-01", "International Labor Day"),
            ("2026-05-27", "Eid al-Adha (estimated)"),
            ("2026-05-28", "Eid al-Adha (estimated)"),
            ("2026-06-16", "Islamic New Year (estimated)"),
            ("2026-07-06", "Independence Day"),
            ("2026-07-07", "Day after Independence Day"),
            ("2026-08-25", "Prophet's Birthday (estimated)"),
            ("2026-11-12", "Day of the Admission of the Comoros to the United Nations"),
        )
