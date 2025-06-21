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

from holidays.constants import OPTIONAL, PUBLIC
from holidays.countries import CapeVerde, CV, CAV
from tests.common import CommonCountryTests


class TestCapeVerde(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CapeVerde, years=range(1976, 2050))

    def test_country_aliases(self):
        self.assertAliases(CapeVerde, CV, CAV)

    def test_no_holidays(self):
        self.assertNoHolidays(CapeVerde(categories=(OPTIONAL, PUBLIC), years=1975))

    def test_democracy_and_freedom_day(self):
        name = "Dia da Liberdade e Democracia"
        self.assertHolidayName(name, (f"{year}-01-13" for year in range(1991, 2050)))
        self.assertNoHolidayName(name, range(1976, 1991))

    def test_independence_day(self):
        self.assertHolidayName(
            "Dia da Independência Nacional", (f"{year}-07-05" for year in range(1976, 2050))
        )

    def test_heroes_day(self):
        self.assertHolidayName(
            "Dia da Nacionalidade e dos Heróis Nacionais",
            (f"{year}-01-20" for year in range(1976, 2050)),
        )

    def test_international_childrens_day(self):
        self.assertHolidayName(
            "Dia Mundial da Criança", (f"{year}-06-01" for year in range(1976, 2050))
        )

    def test_ash_wednesday(self):
        name = "Quarta-feira de Cinzas"
        self.assertHolidayName(
            name,
            "2019-03-06",
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
            "2025-03-05",
        )
        self.assertHolidayName(name, range(1976, 2050))

    def test_good_friday(self):
        name = "Sexta-feira Santa"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1976, 2050))

    def test_easter_sunday(self):
        name = "Páscoa"
        self.assertHolidayName(
            name,
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(1976, 2050))

    def test_municipal_specific_days(self):
        subdiv_holidays = {
            "BR": ("2024-06-24",),
            "BV": ("2024-07-04",),
            "CF": ("2024-05-01",),
            "MA": ("2024-09-08",),
            "PR": ("2024-04-29", "2024-05-19"),
            "RB": ("2024-12-06",),
            "RS": ("2024-01-31",),
            "SL": ("2024-09-15",),
            "SV": ("2024-01-22", "2024-02-13"),
            "TS": ("2024-08-02",),
        }
        for subdiv, holidays in subdiv_holidays.items():
            self.assertHoliday(CapeVerde(subdiv=subdiv, years=2024), holidays)

    def test_2024_public_holidays(self):
        self.assertHolidays(
            CapeVerde(categories=PUBLIC, years=2024),
            ("2024-01-01", "Ano Novo"),
            ("2024-01-13", "Dia da Liberdade e Democracia"),
            ("2024-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2024-02-14", "Quarta-feira de Cinzas"),
            ("2024-03-29", "Sexta-feira Santa"),
            ("2024-03-31", "Páscoa"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-06-01", "Dia Mundial da Criança"),
            ("2024-07-05", "Dia da Independência Nacional"),
            ("2024-08-15", "Dia da Assunção"),
            ("2024-11-01", "Dia de Todos os Santos"),
            ("2024-12-25", "Natal"),
        )

    def test_2024_optional_holidays(self):
        self.assertHolidays(
            CapeVerde(categories=OPTIONAL, years=2024),
            ("2024-03-28", "Quinta-Feira Santa"),
            ("2024-05-12", "Dia das Mães"),
            ("2024-06-16", "Dia dos Pais"),
        )

    def test_2025_public_holidays(self):
        self.assertHolidays(
            CapeVerde(categories=PUBLIC, years=2025),
            ("2025-01-01", "Ano Novo"),
            ("2025-01-13", "Dia da Liberdade e Democracia"),
            ("2025-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2025-03-05", "Quarta-feira de Cinzas"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-06-01", "Dia Mundial da Criança"),
            ("2025-07-05", "Dia da Independência Nacional"),
            ("2025-08-15", "Dia da Assunção"),
            ("2025-11-01", "Dia de Todos os Santos"),
            ("2025-12-25", "Natal"),
        )

    def test_default_l10n(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Ano Novo"),
            ("2025-01-13", "Dia da Liberdade e Democracia"),
            ("2025-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2025-01-22", "Dia do Município de São Vicente"),
            ("2025-01-31", "Dia do Município de Ribeira Grande de Santiago"),
            ("2025-03-04", "Terça-feira de Carnaval"),
            ("2025-03-05", "Quarta-feira de Cinzas"),
            ("2025-04-17", "Quinta-Feira Santa"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-04-29", "Dia da Cidade da Praia"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-05-11", "Dia das Mães"),
            ("2025-05-19", "Dia do Município da Praia"),
            ("2025-06-01", "Dia Mundial da Criança"),
            ("2025-06-15", "Dia dos Pais"),
            ("2025-06-24", "Dia do Município da Brava"),
            ("2025-07-04", "Dia do Município"),
            ("2025-07-05", "Dia da Independência Nacional"),
            ("2025-08-02", "Dia do Município do Tarrafal de São Nicolau"),
            ("2025-08-15", "Dia da Assunção"),
            ("2025-09-08", "Dia do Município do Maio"),
            ("2025-09-15", "Dia do Município"),
            ("2025-11-01", "Dia de Todos os Santos"),
            ("2025-12-06", "Dia do Município de Ribeira Brava"),
            ("2025-12-25", "Natal"),
        )

    def test_de_l10n(self):
        self.assertLocalizedHolidays(
            "de",
            ("2025-01-01", "Neujahr"),
            ("2025-01-13", "Tag der Demokratie und Freiheit"),
            ("2025-01-20", "Tag der Nationalhelden"),
            ("2025-01-22", "Tag der Gemeinde São Vicente"),
            ("2025-01-31", "Tag der Gemeinde Ribeira Grande de Santiago"),
            ("2025-03-04", "Karnevalsdienstag"),
            ("2025-03-05", "Aschermittwoch"),
            ("2025-04-17", "Gründonnerstag"),
            ("2025-04-18", "Karfreitag"),
            ("2025-04-20", "Ostern"),
            ("2025-04-29", "Praia-Stadttag"),
            ("2025-05-01", "Tag der Arbeit"),
            ("2025-05-11", "Muttertag"),
            ("2025-05-19", "Tag der Gemeinde Praia"),
            ("2025-06-01", "Weltkindertag"),
            ("2025-06-15", "Vatertag"),
            ("2025-06-24", "Tag der Gemeinde Brava"),
            ("2025-07-04", "Gemeindetag"),
            ("2025-07-05", "Nationaler Unabhängigkeitstag"),
            ("2025-08-02", "Tag der Gemeinde Tarrafal de São Nicolau"),
            ("2025-08-15", "Mariä Himmelfahrt"),
            ("2025-09-08", "Tag der Gemeinde Maio"),
            ("2025-09-15", "Gemeindetag"),
            ("2025-11-01", "Allerheiligen"),
            ("2025-12-06", "Tag der Gemeinde Ribeira Brava"),
            ("2025-12-25", "Weihnachten"),
        )

    def test_es_l10n(self):
        self.assertLocalizedHolidays(
            "es",
            ("2025-01-01", "Año Nuevo"),
            ("2025-01-13", "Día de la Libertad y la Democracia"),
            ("2025-01-20", "Día de los Héroes Nacionales"),
            ("2025-01-22", "Día del Municipio de São Vicente"),
            ("2025-01-31", "Día del Municipio de Ribeira Grande de Santiago"),
            ("2025-03-04", "Martes de Carnaval"),
            ("2025-03-05", "Miércoles de Ceniza"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-04-20", "Domingo de Pascua"),
            ("2025-04-29", "Día de la Ciudad de Praia"),
            ("2025-05-01", "Día laboral"),
            ("2025-05-11", "Dia de la Madre"),
            ("2025-05-19", "Día del Municipio de Praia"),
            ("2025-06-01", "Día Internacional del Niño"),
            ("2025-06-15", "Dia del Padre"),
            ("2025-06-24", "Día del Municipio Brava"),
            ("2025-07-04", "Día del Municipio"),
            ("2025-07-05", "Día de la Independencia Nacional"),
            ("2025-08-02", "Día del Municipio de Tarrafal de São Nicolau"),
            ("2025-08-15", "Día de la Asunción"),
            ("2025-09-08", "Día del Municipio de Mayo"),
            ("2025-09-15", "Día del Municipio"),
            ("2025-11-01", "Día de Todos los Santos"),
            ("2025-12-06", "Día del Municipio de Ribeira Brava"),
            ("2025-12-25", "Navidad"),
        )

    def test_en_us_l10n(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-13", "Democracy and Freedom Day"),
            ("2025-01-20", "National Heroes Day"),
            ("2025-01-22", "São Vicente Municipal Day"),
            ("2025-01-31", "Ribeira Grande de Santiago Municipal Day"),
            ("2025-03-04", "Carnival Tuesday"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-04-17", "Holy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-04-29", "Praia City Day"),
            ("2025-05-01", "Worker's Day"),
            ("2025-05-11", "Mother's Day"),
            ("2025-05-19", "Praia Municipal Day"),
            ("2025-06-01", "International Children's Day"),
            ("2025-06-15", "Father's Day"),
            ("2025-06-24", "Brava Municipal Day"),
            ("2025-07-04", "Municipal Day"),
            ("2025-07-05", "Independence Day"),
            ("2025-08-02", "Tarrafal de São Nicolau Municipal Day"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-08", "Maio Municipal Day"),
            ("2025-09-15", "Municipal Day"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-06", "Ribeira Brava Municipal Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_fr_l10n(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2025-01-01", "Nouvel An"),
            ("2025-01-13", "Journée de la liberté et de la démocratie"),
            ("2025-01-20", "Journée de la nationalité et des héros nationaux"),
            ("2025-01-22", "Journée de la municipalité de São Vicente"),
            ("2025-01-31", "Journée de la municipalité de Ribeira Grande de Santiago"),
            ("2025-03-04", "Mardi du Carnaval"),
            ("2025-03-05", "Mercredi des Cendres"),
            ("2025-04-17", "Jeudi Saint"),
            ("2025-04-18", "Vendredi Saint"),
            ("2025-04-20", "Dimanche de Pâques"),
            ("2025-04-29", "Journée de la ville de Praia"),
            ("2025-05-01", "Fête du travail"),
            ("2025-05-11", "Fête des Mères"),
            ("2025-05-19", "Journée de la municipalité de Praia"),
            ("2025-06-01", "Journée mondiale de l'enfance"),
            ("2025-06-15", "Fête des Pères"),
            ("2025-06-24", "Journée de la municipalité de Brava"),
            ("2025-07-04", "Journée de la municipalité"),
            ("2025-07-05", "Fête de l'Indépendance Nationale"),
            ("2025-08-02", "Journée de la municipalité de Tarrafal de São Nicolau"),
            ("2025-08-15", "Jour de l'Assomption"),
            ("2025-09-08", "Journée de la municipalité de Maio"),
            ("2025-09-15", "Journée de la municipalité"),
            ("2025-11-01", "La Toussaint"),
            ("2025-12-06", "Journée de la municipalité de Ribeira Brava"),
            ("2025-12-25", "Noël"),
        )
