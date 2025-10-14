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

from holidays.countries.western_sahara import WesternSahara, EH, ESH
from tests.common import CommonCountryTests


class TestWesternSahara(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(2000, 2050)
        super().setUpClass(WesternSahara, years=cls.full_range)
        cls.no_estimated_holidays = WesternSahara(
            years=cls.full_range, islamic_show_estimated=False
        )

    def test_country_aliases(self):
        self.assertAliases(WesternSahara, EH, ESH)

    def test_no_holidays(self):
        self.assertNoHolidays(WesternSahara(years=1999))

    def test_proclamation_of_the_sadr(self):
        self.assertHolidayName(
            "إعلان الجمهورية العربية الصحراوية الديمقراطية",
            (f"{year}-02-27" for year in self.full_range),
        )

    def test_first_martyr(self):
        self.assertHolidayName("يوم الشهيد الأول", (f"{year}-03-08" for year in self.full_range))

    def test_creation_of_the_polisario_front(self):
        self.assertHolidayName(
            "تأسيس الجبهة الشعبية لتحرير الساقية الحمراء ووادي الذهب",
            (f"{year}-05-10" for year in self.full_range),
        )

    def test_commencement_of_the_armed_struggle(self):
        self.assertHolidayName(
            "اندلاع الكفاح المسلح", (f"{year}-05-20" for year in self.full_range)
        )

    def test_martyrs_day(self):
        self.assertHolidayName("يوم الشهداء", (f"{year}-06-09" for year in self.full_range))

    def test_uprising_day(self):
        self.assertHolidayName("يوم الانتفاضة", (f"{year}-06-17" for year in self.full_range))

    def test_national_unity_day(self):
        self.assertHolidayName("عيد الوحدة الوطنية", (f"{year}-10-12" for year in self.full_range))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(2000, 2004))

    def test_prophets_birthday(self):
        name = "المولد النبوي الشريف"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(2000, 2004))

    def test_eid_al_fitr(self):
        name = "عيد الفطر المبارك"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2003, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(2000, 2003))

    def test_eid_al_adha(self):
        name = "عيد الأضحى المبارك"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2004, 2050))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(2000, 2004))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-02-27", "إعلان الجمهورية العربية الصحراوية الديمقراطية"),
            ("2024-03-08", "يوم الشهيد الأول"),
            ("2024-04-10", "عيد الفطر المبارك (المقدرة)"),
            ("2024-05-10", "تأسيس الجبهة الشعبية لتحرير الساقية الحمراء ووادي الذهب"),
            ("2024-05-20", "اندلاع الكفاح المسلح"),
            ("2024-06-09", "يوم الشهداء"),
            ("2024-06-16", "عيد الأضحى المبارك (المقدرة)"),
            ("2024-06-17", "يوم الانتفاضة"),
            ("2024-07-07", "رأس السنة الهجرية (المقدرة)"),
            ("2024-09-15", "المولد النبوي الشريف (المقدرة)"),
            ("2024-10-12", "عيد الوحدة الوطنية"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-02-27", "Proclamation of the SADR"),
            ("2024-03-08", "First Martyr"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-05-10", "Creation of the Polisario Front"),
            ("2024-05-20", "Commencement of the Armed Struggle"),
            ("2024-06-09", "Martyrs' Day"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Uprising Day"),
            ("2024-07-07", "Islamic New Year (estimated)"),
            ("2024-09-15", "Prophet's Birthday (estimated)"),
            ("2024-10-12", "National Unity Day"),
        )

    def test_l10n_es(self):
        self.assertLocalizedHolidays(
            "es",
            ("2024-02-27", "Proclamación de la República Árabe Saharaui Democrática"),
            ("2024-03-08", "Primer mártir"),
            ("2024-04-10", "Eid al-Fitr (estimado)"),
            ("2024-05-10", "Creación del Frente POLISARIO"),
            ("2024-05-20", "Inicio de la lucha armada"),
            ("2024-06-09", "Día de los mártires"),
            ("2024-06-16", "Eid al-Adha (estimado)"),
            ("2024-06-17", "Día de la insurrección"),
            ("2024-07-07", "Primer día del año de la Hégira (estimado)"),
            ("2024-09-15", "Santo Nacimiento del Profeta (estimado)"),
            ("2024-10-12", "Fiesta de la unidad nacional"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2024-02-27", "Proclamation de la République arabe sahraouie démocratique"),
            ("2024-03-08", "Premier martyr"),
            ("2024-04-10", "Aïd el-Fitr (estimé)"),
            ("2024-05-10", "Création du Front POLISARIO"),
            ("2024-05-20", "Déclenchement de la lutte armée"),
            ("2024-06-09", "Journée des martyrs"),
            ("2024-06-16", "Aïd al-Adha (estimé)"),
            ("2024-06-17", "Jour de l'insurrection"),
            ("2024-07-07", "Premier jour de l'an de l'Hégire (estimé)"),
            ("2024-09-15", "Naissance du Prophète (estimé)"),
            ("2024-10-12", "Fête de l'unité nationale"),
        )
