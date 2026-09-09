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

from holidays.countries.haiti import Haiti
from tests.common import CommonCountryTests


class TestHaiti(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Haiti)

    def test_national_independence_day(self):
        self.assertHolidayName(
            "Fête de l'Indépendance Nationale", (f"{year}-01-01" for year in self.full_range)
        )

    def test_ancestry_day(self):
        self.assertHolidayName("Jour des Aïeux", (f"{year}-01-02" for year in self.full_range))

    def test_agriculture_and_labor_day(self):
        self.assertHolidayName(
            "Fête de l'Agriculture et du Travail", (f"{year}-05-01" for year in self.full_range)
        )

    def test_flag_day_and_university_day(self):
        self.assertHolidayName(
            "Fête du Drapeau et de l'Université", (f"{year}-05-18" for year in self.full_range)
        )

    def test_commemoration_of_the_battle_of_vertieres(self):
        self.assertHolidayName(
            "Commémoration de la Bataille de Vertières",
            (f"{year}-11-18" for year in self.full_range),
        )

    def test_armed_forces_day(self):
        self.assertHolidayName(
            "Jour des Forces Armées", (f"{year}-11-18" for year in self.full_range)
        )

    def test_new_years_day(self):
        self.assertHolidayName("Nouvel An", (f"{year}-01-01" for year in self.full_range))

    def test_shrove_monday(self):
        name = "Lundi Gras"
        self.assertHolidayName(
            name,
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_fat_tuesday(self):
        name = "Mardi Gras"
        self.assertHolidayName(
            name,
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
            "2025-03-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Vendredi Saint"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Pâques"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Fête-Dieu"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_assumption_day(self):
        self.assertHolidayName(
            "Assomption de Marie", (f"{year}-08-15" for year in self.full_range)
        )

    def test_death_of_dessalines(self):
        self.assertHolidayName("Mort de Dessalines", (f"{year}-10-17" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("La Toussaint", (f"{year}-11-01" for year in self.full_range))

    def test_day_of_the_dead(self):
        self.assertHolidayName("Fête des Morts", (f"{year}-11-02" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Noël", (f"{year}-12-25" for year in self.full_range))

    def test_ash_wednesday(self):
        name = "Mercredi des Cendres"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
            "2025-03-05",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_maundy_thursday(self):
        name = "Jeudi Saint"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_national_sovereignty_day(self):
        name = "Fête de la Souveraineté Nationale"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-05-23" for year in self.full_range))

    def test_feast_of_lady_of_perpetual_help_patroness_of_haiti(self):
        name = "Fête de Notre-Dame du Perpétuel Secours, patronne d'Haiti"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-06-27" for year in self.full_range))

    def test_ascension_day(self):
        name = "Ascension"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_birth_anniversary_of_jean_jacques_dessalines(self):
        name = "Anniversaire de Naissance de Jean-Jacques Dessalines"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-09-20" for year in self.full_range))

    def test_discovery_day(self):
        name = "Jour de la Découverte"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-12-05" for year in self.full_range))

    def test_2023_public_holiday(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "Fête de l'Indépendance Nationale; Nouvel An"),
            ("2023-01-02", "Jour des Aïeux"),
            ("2023-02-19", "Carnaval"),
            ("2023-02-20", "Lundi Gras"),
            ("2023-02-21", "Mardi Gras"),
            ("2023-04-07", "Vendredi Saint"),
            ("2023-04-09", "Pâques"),
            ("2023-05-01", "Fête de l'Agriculture et du Travail"),
            ("2023-05-18", "Fête du Drapeau et de l'Université"),
            ("2023-06-08", "Fête-Dieu"),
            ("2023-08-15", "Assomption de Marie"),
            ("2023-10-17", "Mort de Dessalines"),
            ("2023-11-01", "La Toussaint"),
            ("2023-11-02", "Fête des Morts"),
            ("2023-11-18", "Commémoration de la Bataille de Vertières; Jour des Forces Armées"),
            ("2023-12-25", "Noël"),
        )

    def test_2025_public_holiday(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Fête de l'Indépendance Nationale; Nouvel An"),
            ("2025-01-02", "Jour des Aïeux"),
            ("2025-03-02", "Carnaval"),
            ("2025-03-03", "Lundi Gras"),
            ("2025-03-04", "Mardi Gras"),
            ("2025-04-18", "Vendredi Saint"),
            ("2025-04-20", "Pâques"),
            ("2025-05-01", "Fête de l'Agriculture et du Travail"),
            ("2025-05-18", "Fête du Drapeau et de l'Université"),
            ("2025-06-19", "Fête-Dieu"),
            ("2025-08-15", "Assomption de Marie"),
            ("2025-10-17", "Mort de Dessalines"),
            ("2025-11-01", "La Toussaint"),
            ("2025-11-02", "Fête des Morts"),
            ("2025-11-18", "Commémoration de la Bataille de Vertières; Jour des Forces Armées"),
            ("2025-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Fête de l'Indépendance Nationale; Nouvel An"),
            ("2024-01-02", "Jour des Aïeux"),
            ("2024-02-11", "Carnaval"),
            ("2024-02-12", "Lundi Gras"),
            ("2024-02-13", "Mardi Gras"),
            ("2024-02-14", "Mercredi des Cendres"),
            ("2024-03-28", "Jeudi Saint"),
            ("2024-03-29", "Vendredi Saint"),
            ("2024-03-31", "Pâques"),
            ("2024-05-01", "Fête de l'Agriculture et du Travail"),
            ("2024-05-09", "Ascension"),
            ("2024-05-18", "Fête du Drapeau et de l'Université"),
            ("2024-05-23", "Fête de la Souveraineté Nationale"),
            ("2024-05-30", "Fête-Dieu"),
            ("2024-06-27", "Fête de Notre-Dame du Perpétuel Secours, patronne d'Haiti"),
            ("2024-08-15", "Assomption de Marie"),
            ("2024-09-20", "Anniversaire de Naissance de Jean-Jacques Dessalines"),
            ("2024-10-17", "Mort de Dessalines"),
            ("2024-11-01", "La Toussaint"),
            ("2024-11-02", "Fête des Morts"),
            ("2024-11-18", "Commémoration de la Bataille de Vertières; Jour des Forces Armées"),
            ("2024-12-05", "Jour de la Découverte"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "National Independence Day; New Year's Day"),
            ("2024-01-02", "Ancestry Day"),
            ("2024-02-11", "Carnival"),
            ("2024-02-12", "Shrove Monday"),
            ("2024-02-13", "Fat Tuesday"),
            ("2024-02-14", "Ash Wednesday"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-05-01", "Agriculture and Labor Day"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-18", "Flag Day and University Day"),
            ("2024-05-23", "National Sovereignty Day"),
            ("2024-05-30", "Corpus Christi"),
            ("2024-06-27", "Feast of Lady of Perpetual Help, Patroness of Haiti"),
            ("2024-08-15", "Assumption Day"),
            ("2024-09-20", "Birth Anniversary of Jean-Jacques Dessalines"),
            ("2024-10-17", "Death of Dessalines"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-02", "Day of the Dead"),
            ("2024-11-18", "Armed Forces Day; Commemoration of the Battle of Vertieres"),
            ("2024-12-05", "Discovery Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_es(self):
        self.assertLocalizedHolidays(
            "es",
            ("2024-01-01", "Año Nuevo; Día de la Independencia Nacional"),
            ("2024-01-02", "Fiesta de los Antepasados"),
            ("2024-02-11", "Carnaval"),
            ("2024-02-12", "Lunes de Carnaval"),
            ("2024-02-13", "Martes Gordo"),
            ("2024-02-14", "Miércoles de Ceniza"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-03-31", "Pascua"),
            ("2024-05-01", "Día de la Agricultura y el Trabajo"),
            ("2024-05-09", "Ascensión"),
            ("2024-05-18", "Fiesta de la Bandera y la Universidad"),
            ("2024-05-23", "Día de la Soberanía Nacional"),
            ("2024-05-30", "Fête-Dieu"),
            ("2024-06-27", "Fiesta de Nuestra Señora del Perpetuo Socorro, patrona de Haití"),
            ("2024-08-15", "Asunción de María"),
            ("2024-09-20", "Aniversario del Nacimiento de Jean-Jacques Dessalines"),
            ("2024-10-17", "Muerte de Dessalines"),
            ("2024-11-01", "Día de Todos los Santos"),
            ("2024-11-02", "Día de Muertos"),
            ("2024-11-18", "Conmemoración de la Batalla de Vertières; Día de las Fuerzas Armadas"),
            ("2024-12-05", "Día del Descubrimiento"),
            ("2024-12-25", "Navidad"),
        )

    def test_l10n_ht(self):
        self.assertLocalizedHolidays(
            "ht",
            ("2024-01-01", "Jounen Endepandans Nasyonal; Nouvèl Ane"),
            ("2024-01-02", "Fèt Zansèt yo"),
            ("2024-02-11", "Kanaval"),
            ("2024-02-12", "Lendi Gras"),
            ("2024-02-13", "Madi Gras"),
            ("2024-02-14", "Mèkredi Sann"),
            ("2024-03-28", "Jedi Sant"),
            ("2024-03-29", "Vandredi Sen"),
            ("2024-03-31", "Pak"),
            ("2024-05-01", "Jounen Agrikilti ak Travay"),
            ("2024-05-09", "Asansyon"),
            ("2024-05-18", "Jounen Drapo ak Inivèsite"),
            ("2024-05-23", "Jounen Nasyonal Souverènte"),
            ("2024-05-30", "Fèt Dye"),
            ("2024-06-27", "Fèt Manman Pèpetyèl Sekou, Patwòn Peyi Dayiti"),
            ("2024-08-15", "Sipozisyon Mari"),
            ("2024-09-20", "Anivèsè Nesans Jean-Jacques Dessalines"),
            ("2024-10-17", "Lanmò Desalin"),
            ("2024-11-01", "Jou tout Sen"),
            ("2024-11-02", "Jou Mouri"),
            ("2024-11-18", "Jounen Fòs Lame; Komemorasyon batay Vertières"),
            ("2024-12-05", "Jounen Dekouvèt"),
            ("2024-12-25", "Nwèl"),
        )
