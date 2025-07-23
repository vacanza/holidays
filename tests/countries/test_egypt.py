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

from holidays.constants import GOVERNMENT, SCHOOL
from holidays.countries.egypt import Egypt, EG, EGY
from tests.common import CommonCountryTests


class TestEgypt(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1954, 2050)
        super().setUpClass(Egypt, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Egypt(years=years, islamic_show_estimated=False)
        cls.government_holidays = Egypt(
            categories=GOVERNMENT, years=years, islamic_show_estimated=False
        )
        cls.school_holidays = Egypt(categories=SCHOOL, years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Egypt, EG, EGY)

    def test_no_holidays(self):
        self.assertNoHolidays(Egypt(years=1953))
        self.assertNoHolidays(Egypt(categories=GOVERNMENT, years=2017))
        self.assertNoHolidays(Egypt(categories=SCHOOL, years=2018))

    def test_coptic_christmas_day(self):
        name = "عيد الميلاد المجيد"
        self.assertHolidayName(
            name, (f"{year}-01-07" for year in (*range(2002, 2022), *range(2024, 2050)))
        )
        self.assertNoHolidayName(name, range(1954, 2002))
        obs_dt = (
            "2022-01-06",
            "2023-01-08",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_january_25_revolution(self):
        name_1 = "عيد الشرطة"
        name_2 = "ثورة ٢٥ يناير وعيد الشرطة"
        self.assertHolidayName(name_1, (f"{year}-01-25" for year in range(2009, 2012)))
        self.assertNoHolidayName(name_1, range(1954, 2009), range(2012, 2050))

        self.assertHolidayName(name_2, (f"{year}-01-25" for year in range(2012, 2020)))
        self.assertNoHolidayName(name_2, range(1954, 2012))
        self.assertHolidayName(
            name_2,
            "2020-01-25",
            "2024-01-25",
            "2025-01-25",
        )
        obs_dt = (
            "2021-01-28",
            "2022-01-27",
            "2023-01-26",
        )
        self.assertHolidayName(f"{name_2} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNonObservedHolidayName(name_2, range(2020, 2050))

    def test_sinai_liberation_day(self):
        name = "عيد تحرير سيناء"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1983, 2020)))
        self.assertNoHolidayName(name, range(1954, 1983))
        self.assertHolidayName(
            name,
            "2020-04-25",
            "2022-04-25",
            "2024-04-25",
            "2025-04-25",
        )
        obs_dt = (
            "2021-04-29",
            "2023-04-27",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNonObservedHolidayName(name, range(2020, 2050))

    def test_spring_festival(self):
        name = "عيد شم النسيم"
        self.assertHolidayName(
            name,
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1954, 2050))

    def test_labor_day(self):
        name = "عيد العمال"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1954, 2020)))
        self.assertHolidayName(
            name,
            "2020-05-01",
            "2025-05-01",
        )
        obs_dt = (
            "2022-05-05",
            "2023-05-04",
            "2024-05-05",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNonObservedHolidayName(name, range(2020, 2024), range(2025, 2050))

    def test_june_30_revolution_day(self):
        name = "عيد ثورة ٣٠ يونيو"
        self.assertHolidayName(name, (f"{year}-06-30" for year in range(2014, 2020)))
        self.assertNoHolidayName(name, range(1954, 2014))
        self.assertHolidayName(
            name,
            "2022-06-30",
            "2023-06-30",
            "2024-06-30",
        )
        obs_dt = (
            "2020-07-02",
            "2021-07-01",
            "2023-07-02",
            "2025-07-03",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNonObservedHolidayName(name, range(2020, 2050))

    def test_july_23_revolution_day(self):
        name = "عيد ثورة ٢٣ يوليو"
        self.assertHolidayName(name, (f"{year}-07-23" for year in range(1954, 2020)))
        self.assertHolidayName(
            name,
            "2020-07-23",
            "2021-07-23",
            "2022-07-23",
            "2023-07-23",
        )
        obs_dt = (
            "2024-07-25",
            "2025-07-24",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNonObservedHolidayName(name, range(2020, 2050))

    def test_armed_forces_day(self):
        name = "عيد القوات المسلحة"
        self.assertHolidayName(name, (f"{year}-10-06" for year in range(1954, 2020)))
        self.assertHolidayName(
            name,
            "2022-10-06",
            "2023-10-06",
            "2024-10-06",
        )
        obs_dt = (
            "2020-10-08",
            "2021-10-07",
            "2025-10-09",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNonObservedHolidayName(name, range(2020, 2050))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2022-07-30",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1954, 2020))
        obs_dt = (
            "2021-08-12",
            "2023-07-20",
            "2024-07-11",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_mawlid(self):
        name = "المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-28",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1954, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر المبارك"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-01",
            "2022-05-02",
            "2023-04-21",
            "2023-04-22",
            "2024-04-10",
            "2024-04-11",
            "2025-03-30",
            "2025-03-31",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1954, 2050))

        obs_dt = (
            "2022-05-04",
            "2023-04-24",
        )
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        gov_dt = (
            "2019-06-03",
            "2019-06-06",
            "2020-05-23",
            "2020-05-26",
            "2021-05-12",
            "2021-05-15",
            "2022-04-30",
            "2022-05-03",
            "2023-04-20",
            "2023-04-23",
            "2024-04-09",
            "2024-04-12",
            "2025-03-29",
            "2025-04-01",
        )
        self.assertHolidayName(name, self.government_holidays, gov_dt)
        self.assertNoHoliday(gov_dt)
        self.assertHolidayName(name, self.government_holidays, range(2019, 2050))
        self.assertNoHolidayName(name, self.government_holidays, range(1954, 2019))

    def test_arafat_day(self):
        name = "وقفة عيد الأضحى المبارك"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-09",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1954, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى المبارك"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-17",
            "2021-07-18",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
            "2022-07-13",
            "2022-07-14",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1954, 2050))

        obs_dt = ("2023-07-03",)
        self.assertHolidayName(f"{name} (ملاحظة)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        gov_dt = (
            "2018-08-24",
            "2019-08-14",
            "2020-08-03",
            "2021-07-23",
            "2022-07-13",
            "2023-07-01",
            "2024-06-19",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.government_holidays, gov_dt)
        self.assertHolidayName(name, self.government_holidays, range(2018, 2050))
        self.assertNoHolidayName(name, self.government_holidays, range(1954, 2018))

    def test_taba_liberation_day(self):
        name = "عيد تحرير طابا"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.school_holidays, (f"{year}-03-19" for year in range(2019, 2020))
        )
        self.assertNoHolidayName(name, self.school_holidays, range(1954, 2019))

    def test_evacuation_day(self):
        name = "عيد الجلاء"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.school_holidays, (f"{year}-06-18" for year in range(2019, 2020))
        )
        self.assertNoHolidayName(name, self.school_holidays, range(1954, 2019))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-07", "عيد الميلاد المجيد"),
            ("2024-01-25", "ثورة ٢٥ يناير وعيد الشرطة"),
            ("2024-03-19", "عيد تحرير طابا"),
            ("2024-04-09", "عيد الفطر المبارك"),
            ("2024-04-10", "عيد الفطر المبارك"),
            ("2024-04-11", "عيد الفطر المبارك"),
            ("2024-04-12", "عيد الفطر المبارك"),
            ("2024-04-25", "عيد تحرير سيناء"),
            ("2024-05-05", "عيد العمال (ملاحظة)"),
            ("2024-05-06", "عيد شم النسيم"),
            ("2024-06-15", "وقفة عيد الأضحى المبارك"),
            ("2024-06-16", "عيد الأضحى المبارك"),
            ("2024-06-17", "عيد الأضحى المبارك"),
            ("2024-06-18", "عيد الأضحى المبارك; عيد الجلاء"),
            ("2024-06-19", "عيد الأضحى المبارك"),
            ("2024-06-30", "عيد ثورة ٣٠ يونيو"),
            ("2024-07-11", "رأس السنة الهجرية (ملاحظة)"),
            ("2024-07-25", "عيد ثورة ٢٣ يوليو (ملاحظة)"),
            ("2024-09-15", "المولد النبوي الشريف"),
            ("2024-10-06", "عيد القوات المسلحة"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-07", "Coptic Christmas Day"),
            ("2024-01-25", "January 25th Revolution and National Police Day"),
            ("2024-03-19", "Taba Liberation Day"),
            ("2024-04-09", "Eid al-Fitr"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr"),
            ("2024-04-12", "Eid al-Fitr"),
            ("2024-04-25", "Sinai Liberation Day"),
            ("2024-05-05", "Labor Day (observed)"),
            ("2024-05-06", "Spring Festival"),
            ("2024-06-15", "Arafat Day"),
            ("2024-06-16", "Eid al-Adha"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-06-18", "Eid al-Adha; Evacuation Day"),
            ("2024-06-19", "Eid al-Adha"),
            ("2024-06-30", "June 30 Revolution Day"),
            ("2024-07-11", "Islamic New Year (observed)"),
            ("2024-07-25", "July 23 Revolution Day (observed)"),
            ("2024-09-15", "Prophet's Birthday"),
            ("2024-10-06", "Armed Forces Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2024-01-07", "Fête de Noël"),
            ("2024-01-25", "Révolution de 25 Janvier et la fête de la Police"),
            ("2024-03-19", "Fête de la libération de Taba"),
            ("2024-04-09", "Aïd-Al-Fitr"),
            ("2024-04-10", "Aïd-Al-Fitr"),
            ("2024-04-11", "Aïd-Al-Fitr"),
            ("2024-04-12", "Aïd-Al-Fitr"),
            ("2024-04-25", "Fête de la Libération du Sinaï"),
            ("2024-05-05", "Fête du Travail (observé)"),
            ("2024-05-06", "Cham Al-Nessim"),
            ("2024-06-15", "Le jour d'Arafat"),
            ("2024-06-16", "Aïd Al-Adha"),
            ("2024-06-17", "Aïd Al-Adha"),
            ("2024-06-18", "Aïd Al-Adha; Jour d'évacuation"),
            ("2024-06-19", "Aïd Al-Adha"),
            ("2024-06-30", "Fête de la Révolution du 30 Juin"),
            ("2024-07-11", "Fête de l'Hégire (observé)"),
            ("2024-07-25", "Fête de la Révolution du 23 Juillet (observé)"),
            ("2024-09-15", "Naissance du Prophète"),
            ("2024-10-06", "Fête des Forces Armées"),
        )
