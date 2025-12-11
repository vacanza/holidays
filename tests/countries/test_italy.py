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

from holidays.countries.italy import Italy
from tests.common import CommonCountryTests


class TestItaly(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Italy)

    def test_special_holidays(self):
        self.assertHoliday(
            "1907-07-04",
            "1910-08-10",
            "1911-03-17",
            "1920-03-14",
            "1921-09-14",
            "1926-10-04",
            "1938-05-03",
            "1946-06-11",
            "1961-03-17",
            "2011-03-17",
        )

    def test_new_years_day(self):
        name = "Capodanno"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1875, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1875))

    def test_epiphany_day(self):
        name = "Epifania"
        self.assertHolidayName(
            name,
            (
                f"{year}-01-06"
                for year in (*range(self.start_year, 1978), *range(1986, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1978, 1986))

    def test_saint_josephs_day(self):
        name = "San Giuseppe"
        self.assertHolidayName(name, (f"{year}-03-19" for year in range(1929, 1977)))
        self.assertNoHolidayName(name, range(self.start_year, 1929), range(1977, self.end_year))

    def test_easter_monday(self):
        name = "Lunedì dell'Angelo"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1950, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1950))

    def test_foundation_of_rome(self):
        name = "Natale di Roma"
        self.assertHolidayName(name, (f"{year}-04-21" for year in range(1923, 1942)))
        self.assertNoHolidayName(name, range(self.start_year, 1923), range(1942, self.end_year))

    def test_liberation_day(self):
        name = "Anniversario della Liberazione"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1946, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1946))

    def test_labor_day(self):
        name = "Festa del Lavoro"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1946, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1946))

    def test_anniversary_of_victory_in_europe(self):
        name = "Anniversario della Vittoria in Europa"
        self.assertHolidayName(name, (f"{year}-05-08" for year in range(1946, 1950)))
        self.assertNoHolidayName(name, range(self.start_year, 1946), range(1950, self.end_year))

    def test_anniversary_of_founding_of_empire(self):
        name = "Anniversario della fondazione dell'Impero"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1939, 1942)))
        self.assertNoHolidayName(name, range(self.start_year, 1939), range(1942, self.end_year))

    def test_republic_day(self):
        name = "Festa della Repubblica"
        self.assertHolidayName(
            name, (f"{year}-06-02" for year in (*range(1947, 1977), *range(2001, self.end_year)))
        )
        self.assertHolidayName(
            name,
            "1977-06-05",
            "1978-06-04",
            "1997-06-01",
            "1998-06-07",
            "1999-06-06",
            "2000-06-04",
        )
        self.assertNoHolidayName(name, range(self.start_year, 1947))

    def test_ascension_day(self):
        name = "Ascensione"
        self.assertHolidayName(
            name,
            "1971-05-20",
            "1972-05-11",
            "1973-05-31",
            "1974-05-23",
            "1975-05-08",
            "1976-05-27",
        )
        self.assertHolidayName(name, range(self.start_year, 1977))
        self.assertNoHolidayName(name, range(1977, self.end_year))

    def test_saints_peter_and_paul_day(self):
        name = "Santi Apostoli Pietro e Paolo"
        self.assertHolidayName(
            name, (f"{year}-06-29" for year in (*range(self.start_year, 1914), *range(1924, 1977)))
        )
        self.assertNoHolidayName(name, range(1914, 1924), range(1977, self.end_year))

    def test_corpus_christi_day(self):
        name = "Corpus Domini"
        self.assertHolidayName(
            name,
            "1911-06-15",
            "1912-06-06",
            "1913-05-22",
            "1971-06-10",
            "1972-06-01",
            "1973-06-21",
            "1974-06-13",
            "1975-05-29",
            "1976-06-17",
        )
        self.assertHolidayName(name, range(self.start_year, 1914), range(1924, 1977))
        self.assertNoHolidayName(name, range(1914, 1924), range(1977, self.end_year))

    def test_assumption_of_mary_day(self):
        self.assertHolidayName(
            "Assunzione della Beata Vergine Maria", (f"{year}-08-15" for year in self.full_range)
        )

    def test_nativity_of_mary_day(self):
        name = "Natività della Beata Vergine Maria"
        self.assertHolidayName(name, (f"{year}-09-08" for year in range(self.start_year, 1913)))
        self.assertNoHolidayName(name, range(1913, self.end_year))

    def test_anniversary_of_capture_of_rome(self):
        name = "Anniversario della Presa di Roma"
        self.assertHolidayName(name, (f"{year}-09-20" for year in range(1895, 1931)))
        self.assertNoHolidayName(name, range(self.start_year, 1895), range(1931, self.end_year))

    def test_saint_francis_of_assisi(self):
        name = "Festa nazionale di San Francesco d'Assisi, patrono d'Italia"
        self.assertHolidayName(name, (f"{year}-10-04" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))

    def test_anniversary_of_march_on_rome(self):
        name = "Anniversario della Marcia su Roma"
        self.assertHolidayName(
            name,
            "1926-10-28",
            "1927-10-30",
            "1928-10-28",
            "1929-10-27",
            (f"{year}-10-28" for year in range(1930, 1941)),
        )
        self.assertNoHolidayName(name, range(self.start_year, 1926), range(1941, self.end_year))

    def test_all_saints_day(self):
        self.assertHolidayName("Ognissanti", (f"{year}-11-01" for year in self.full_range))

    def test_national_unity_day(self):
        name_1922 = "Anniversario della Vittoria"
        name_1950 = "Giorno dell'unità nazionale"
        self.assertHolidayName(
            name_1922,
            (
                f"{year}-11-04"
                for year in (*range(1922, 1927), *range(1930, 1941), *range(1946, 1950))
            ),
            "1927-11-06",
            "1928-11-04",
            "1929-11-03",
        )
        self.assertHolidayName(name_1950, (f"{year}-11-04" for year in range(1950, 1977)))
        self.assertHolidayName(
            name_1950,
            "1977-11-06",
            "1978-11-05",
            "2020-11-01",
            "2021-11-07",
            "2022-11-06",
            "2023-11-05",
            "2024-11-03",
            "2025-11-02",
        )
        self.assertHolidayName(name_1950, range(1950, self.end_year))
        self.assertNoHolidayName(name_1922, range(1941, 1946), range(1950, self.end_year))
        self.assertNoHolidayName(name_1950, range(self.start_year, 1950))

    def test_immaculate_conception_day(self):
        name = "Immacolata Concezione"
        self.assertHolidayName(
            name,
            (
                f"{year}-12-08"
                for year in (*range(self.start_year, 1913), *range(1924, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1913, 1924))

    def test_christmas_day(self):
        self.assertHolidayName("Natale", (f"{year}-12-25" for year in self.full_range))

    def test_saint_stephens_day(self):
        name = "Santo Stefano"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1949, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1949))

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Capodanno"),
            ("2022-01-06", "Epifania"),
            ("2022-04-18", "Lunedì dell'Angelo"),
            ("2022-04-25", "Anniversario della Liberazione"),
            ("2022-05-01", "Festa del Lavoro"),
            ("2022-06-02", "Festa della Repubblica"),
            ("2022-08-15", "Assunzione della Beata Vergine Maria"),
            ("2022-11-01", "Ognissanti"),
            ("2022-11-06", "Giorno dell'unità nazionale"),
            ("2022-12-08", "Immacolata Concezione"),
            ("2022-12-25", "Natale"),
            ("2022-12-26", "Santo Stefano"),
        )

    def test_no_subdiv_holidays(self):
        dt_start, dt_end = "1914-01-01", "1950-01-01"
        common_holidays_1914_1949 = self.holidays[dt_start:dt_end]
        for holidays in self.subdiv_holidays.values():
            self.assertEqual(holidays[dt_start:dt_end], common_holidays_1914_1949)

    def test_subdiv_specific_days(self):
        subdiv_holidays = {
            "AG": {"2025-02-25": "San Gerlando"},
            "AL": {"2025-11-10": "San Baudolino"},
            "AN": {"2025-05-04": "San Ciriaco"},
            "AO": {"2025-09-07": "San Grato"},
            "AP": {"2025-08-05": "Sant'Emidio"},
            "AQ": {"2025-06-10": "San Massimo d'Aveia"},
            "AR": {"2025-08-07": "San Donato d'Arezzo"},
            "AT": {"2025-05-06": "San Secondo di Asti"},
            "AV": {"2025-02-14": "San Modestino"},
            "BA": {"2025-12-06": "San Nicola"},
            "BG": {"2025-08-26": "Sant'Alessandro di Bergamo"},
            "BI": {"2025-12-26": "Santo Stefano"},
            "BL": {"2025-11-11": "San Martino"},
            "BN": {"2025-08-24": "San Bartolomeo apostolo"},
            "BO": {"2025-10-04": "San Petronio"},
            "BR": {"2025-09-07": "San Teodoro d'Amasea e San Lorenzo da Brindisi"},
            "BS": {"2025-02-15": "Santi Faustino e Giovita"},
            "BT": {
                "2025-05-03": "San Nicola Pellegrino",
                "2025-09-21": "San Riccardo di Andria",
                "2025-12-30": "San Ruggero",
            },
            "BZ": {"2025-08-15": "Maria Santissima Assunta"},
            "CA": {"2025-10-30": "San Saturnino di Cagliari"},
            "CB": {"2025-04-23": "San Giorgio"},
            "CE": {"2025-01-20": "San Sebastiano"},
            "CH": {"2025-05-11": "San Giustino di Chieti"},
            "CL": {"2025-09-29": "San Michele Arcangelo"},
            "CN": {"2025-09-29": "San Michele Arcangelo"},
            "CO": {"2025-08-31": "Sant'Abbondio"},
            "CR": {"2025-11-13": "Sant'Omobono"},
            "CS": {"2025-02-12": "Madonna del Pilerio"},
            "CT": {"2025-02-05": "Sant'Agata"},
            "CZ": {"2025-07-16": "San Vitaliano"},
            "EN": {"2025-07-02": "Madonna della Visitazione"},
            "FC": {
                "2025-02-04": "Madonna del Fuoco",
                "2025-06-24": "San Giovanni Battista",
            },
            "FE": {"2025-04-23": "San Giorgio"},
            "FG": {"2025-03-22": "Madonna dei Sette Veli"},
            "FI": {"2025-06-24": "San Giovanni Battista"},
            "FM": {
                "2025-08-15": "Maria Santissima Assunta",
                "2025-08-16": "Maria Santissima Assunta",
            },
            "FR": {"2025-06-20": "San Silverio"},
            "GE": {"2025-06-24": "San Giovanni Battista"},
            "GO": {"2025-03-16": "Santi Ilario e Taziano"},
            "GR": {"2025-08-10": "San Lorenzo"},
            "IM": {"2025-11-26": "San Leonardo da Porto Maurizio"},
            "IS": {"2025-05-19": "San Pietro Celestino"},
            "KR": {"2025-10-09": "San Dionigi"},
            "LC": {"2025-12-06": "San Nicola"},
            "LE": {"2025-08-26": "Sant'Oronzo"},
            "LI": {"2025-05-22": "Santa Giulia"},
            "LO": {"2025-01-19": "San Bassiano"},
            "LT": {
                "2025-04-25": "San Marco Evangelista",
                "2025-07-06": "Santa Maria Goretti",
            },
            "LU": {"2025-07-12": "San Paolino di Lucca"},
            "MB": {"2025-06-24": "San Giovanni Battista"},
            "MC": {"2025-08-31": "San Giuliano l'ospitaliere"},
            "ME": {"2025-06-03": "Madonna della Lettera"},
            "MI": {"2025-12-07": "Sant'Ambrogio"},
            "MN": {"2025-03-18": "Sant'Anselmo da Baggio"},
            "MO": {"2025-01-31": "San Geminiano"},
            "MS": {"2025-10-04": "San Francesco d'Assisi"},
            "MT": {"2025-07-02": "Madonna della Bruna"},
            "NA": {"2025-09-19": "San Gennaro"},
            "NO": {"2025-01-22": "San Gaudenzio"},
            "NU": {"2025-08-05": "Nostra Signora della Neve"},
            "OR": {"2025-02-13": "Sant'Archelao"},
            "PA": {"2025-07-15": "Santa Rosalia"},
            "PC": {"2025-07-04": "Sant'Antonino di Piacenza"},
            "PD": {"2025-06-13": "Sant'Antonio di Padova"},
            "PE": {"2025-10-10": "San Cetteo"},
            "PG": {
                "2025-08-11": "Santa Chiara d'Assisi",
                "2025-10-04": "San Francesco d'Assisi",
            },
            "PI": {"2025-06-17": "San Ranieri"},
            "PN": {
                "2025-04-25": "San Marco Evangelista",
                "2025-09-08": "Madonna delle Grazie",
            },
            "PO": {"2025-12-26": "Santo Stefano"},
            "PR": {"2025-01-13": "Sant'Ilario di Poitiers"},
            "PT": {"2025-07-25": "San Jacopo"},
            "PU": {
                "2025-06-01": "San Crescentino",
                "2025-09-24": "San Terenzio di Pesaro",
            },
            "PV": {"2025-12-09": "San Siro"},
            "PZ": {"2025-05-30": "San Gerardo di Potenza"},
            "RA": {"2025-07-23": "Sant'Apollinare"},
            "RC": {"2025-04-23": "San Giorgio"},
            "RE": {"2025-11-24": "San Prospero Vescovo"},
            "RG": {
                "2025-04-23": "San Giorgio Martire",
                "2025-08-29": "San Giovanni Battista",
            },
            "RI": {"2025-12-04": "Santa Barbara"},
            "RM": {"2025-06-29": "Santi Pietro e Paolo"},
            "RN": {"2025-10-14": "San Gaudenzio"},
            "RO": {"2025-11-26": "San Bellino"},
            "SA": {"2025-09-21": "San Matteo Evangelista"},
            "SI": {"2025-12-01": "Sant'Ansano"},
            "SO": {"2025-06-19": "San Gervasio e San Protasio"},
            "SP": {"2025-03-19": "San Giuseppe"},
            "SR": {"2025-12-13": "Santa Lucia"},
            "SS": {"2025-12-06": "San Nicola"},
            "SU": {"2025-05-15": "San Ponziano"},
            "SV": {"2025-03-18": "Nostra Signora della Misericordia"},
            "TA": {"2025-05-10": "San Cataldo"},
            "TE": {"2025-12-19": "San Berardo da Pagliara"},
            "TN": {"2025-06-26": "San Vigilio"},
            "TO": {"2025-06-24": "San Giovanni Battista"},
            "TP": {"2025-08-07": "Sant'Alberto degli Abati"},
            "TR": {"2025-02-14": "San Valentino"},
            "TS": {"2025-11-03": "San Giusto"},
            "TV": {"2025-04-27": "San Liberale"},
            "UD": {"2025-07-12": "Santi Ermacora e Fortunato"},
            "VA": {"2025-05-08": "San Vittore il Moro"},
            "VB": {"2025-05-08": "San Vittore il Moro"},
            "VC": {"2025-08-01": "Sant'Eusebio di Vercelli"},
            "VE": {
                "2025-04-25": "San Marco Evangelista",
                "2025-11-21": "Madonna della Salute",
            },
            "VI": {"2025-09-08": "Madonna di Monte Berico"},
            "VR": {"2025-05-21": "San Zeno"},
            "VT": {"2025-09-04": "Santa Rosa da Viterbo"},
            "VV": {"2025-03-01": "San Leoluca"},
            "Andria": {"2025-09-21": "San Riccardo di Andria"},
            "Barletta": {"2025-12-30": "San Ruggero"},
            "Cesena": {"2025-06-24": "San Giovanni Battista"},
            "Forli": {"2025-02-04": "Madonna del Fuoco"},
            "Pesaro": {"2025-09-24": "San Terenzio di Pesaro"},
            "Trani": {"2025-05-03": "San Nicola Pellegrino"},
            "Urbino": {"2025-06-01": "San Crescentino"},
        }

        for subdiv, holidays in subdiv_holidays.items():
            for dt, name in holidays.items():
                self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Capodanno"),
            ("2025-01-06", "Epifania"),
            ("2025-01-13", "Sant'Ilario di Poitiers"),
            ("2025-01-19", "San Bassiano"),
            ("2025-01-20", "San Sebastiano"),
            ("2025-01-22", "San Gaudenzio"),
            ("2025-01-31", "San Geminiano"),
            ("2025-02-04", "Madonna del Fuoco"),
            ("2025-02-05", "Sant'Agata"),
            ("2025-02-12", "Madonna del Pilerio"),
            ("2025-02-13", "Sant'Archelao"),
            ("2025-02-14", "San Modestino; San Valentino"),
            ("2025-02-15", "Santi Faustino e Giovita"),
            ("2025-02-25", "San Gerlando"),
            ("2025-03-01", "San Leoluca"),
            ("2025-03-16", "Santi Ilario e Taziano"),
            ("2025-03-18", "Nostra Signora della Misericordia; Sant'Anselmo da Baggio"),
            ("2025-03-19", "San Giuseppe"),
            ("2025-03-22", "Madonna dei Sette Veli"),
            ("2025-04-21", "Lunedì dell'Angelo"),
            ("2025-04-23", "San Giorgio; San Giorgio Martire"),
            ("2025-04-25", "Anniversario della Liberazione; San Marco Evangelista"),
            ("2025-04-27", "San Liberale"),
            ("2025-05-01", "Festa del Lavoro"),
            ("2025-05-03", "San Nicola Pellegrino"),
            ("2025-05-04", "San Ciriaco"),
            ("2025-05-06", "San Secondo di Asti"),
            ("2025-05-08", "San Vittore il Moro"),
            ("2025-05-10", "San Cataldo"),
            ("2025-05-11", "San Giustino di Chieti"),
            ("2025-05-15", "San Ponziano"),
            ("2025-05-19", "San Pietro Celestino"),
            ("2025-05-21", "San Zeno"),
            ("2025-05-22", "Santa Giulia"),
            ("2025-05-30", "San Gerardo di Potenza"),
            ("2025-06-01", "San Crescentino"),
            ("2025-06-02", "Festa della Repubblica"),
            ("2025-06-03", "Madonna della Lettera"),
            ("2025-06-10", "San Massimo d'Aveia"),
            ("2025-06-13", "Sant'Antonio di Padova"),
            ("2025-06-17", "San Ranieri"),
            ("2025-06-19", "San Gervasio e San Protasio"),
            ("2025-06-20", "San Silverio"),
            ("2025-06-24", "San Giovanni Battista"),
            ("2025-06-26", "San Vigilio"),
            ("2025-06-29", "Santi Pietro e Paolo"),
            ("2025-07-02", "Madonna della Bruna; Madonna della Visitazione"),
            ("2025-07-04", "Sant'Antonino di Piacenza"),
            ("2025-07-06", "Santa Maria Goretti"),
            ("2025-07-12", "San Paolino di Lucca; Santi Ermacora e Fortunato"),
            ("2025-07-15", "Santa Rosalia"),
            ("2025-07-16", "San Vitaliano"),
            ("2025-07-23", "Sant'Apollinare"),
            ("2025-07-25", "San Jacopo"),
            ("2025-08-01", "Sant'Eusebio di Vercelli"),
            ("2025-08-05", "Nostra Signora della Neve; Sant'Emidio"),
            ("2025-08-07", "San Donato d'Arezzo; Sant'Alberto degli Abati"),
            ("2025-08-10", "San Lorenzo"),
            ("2025-08-11", "Santa Chiara d'Assisi"),
            ("2025-08-15", "Assunzione della Beata Vergine Maria; Maria Santissima Assunta"),
            ("2025-08-16", "Maria Santissima Assunta"),
            ("2025-08-24", "San Bartolomeo apostolo"),
            ("2025-08-26", "Sant'Alessandro di Bergamo; Sant'Oronzo"),
            ("2025-08-29", "San Giovanni Battista"),
            ("2025-08-31", "San Giuliano l'ospitaliere; Sant'Abbondio"),
            ("2025-09-04", "Santa Rosa da Viterbo"),
            ("2025-09-07", "San Grato; San Teodoro d'Amasea e San Lorenzo da Brindisi"),
            ("2025-09-08", "Madonna delle Grazie; Madonna di Monte Berico"),
            ("2025-09-19", "San Gennaro"),
            ("2025-09-21", "San Matteo Evangelista; San Riccardo di Andria"),
            ("2025-09-24", "San Terenzio di Pesaro"),
            ("2025-09-29", "San Michele Arcangelo"),
            ("2025-10-04", "San Francesco d'Assisi; San Petronio"),
            ("2025-10-09", "San Dionigi"),
            ("2025-10-10", "San Cetteo"),
            ("2025-10-14", "San Gaudenzio"),
            ("2025-10-30", "San Saturnino di Cagliari"),
            ("2025-11-01", "Ognissanti"),
            ("2025-11-02", "Giorno dell'unità nazionale"),
            ("2025-11-03", "San Giusto"),
            ("2025-11-10", "San Baudolino"),
            ("2025-11-11", "San Martino"),
            ("2025-11-13", "Sant'Omobono"),
            ("2025-11-21", "Madonna della Salute"),
            ("2025-11-24", "San Prospero Vescovo"),
            ("2025-11-26", "San Bellino; San Leonardo da Porto Maurizio"),
            ("2025-12-01", "Sant'Ansano"),
            ("2025-12-04", "Santa Barbara"),
            ("2025-12-06", "San Nicola"),
            ("2025-12-07", "Sant'Ambrogio"),
            ("2025-12-08", "Immacolata Concezione"),
            ("2025-12-09", "San Siro"),
            ("2025-12-13", "Santa Lucia"),
            ("2025-12-19", "San Berardo da Pagliara"),
            ("2025-12-25", "Natale"),
            ("2025-12-26", "Santo Stefano"),
            ("2025-12-30", "San Ruggero"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-06", "Epiphany"),
            ("2025-01-13", "Saint Hilary of Poitiers's Day"),
            ("2025-01-19", "Saint Bassianus's Day"),
            ("2025-01-20", "Saint Sebastian's Day"),
            ("2025-01-22", "Saint Gaudentius's Day"),
            ("2025-01-31", "Saint Geminianus's Day"),
            ("2025-02-04", "Our Lady of the Fire"),
            ("2025-02-05", "Saint Agatha's Day"),
            ("2025-02-12", "Our Lady of the Pilerio"),
            ("2025-02-13", "Saint Archelaus's Day"),
            ("2025-02-14", "Saint Modestinus's Day; Saint Valentine's Day"),
            ("2025-02-15", "Saints Faustinus and Jovita's Day"),
            ("2025-02-25", "Saint Gerland's Day"),
            ("2025-03-01", "Saint Leoluca's Day"),
            ("2025-03-16", "Saints Hilary and Tatian's Day"),
            ("2025-03-18", "Our Lady of Mercy; Saint Anselm of Baggio's Day"),
            ("2025-03-19", "Saint Joseph's Day"),
            ("2025-03-22", "Our Lady of the Seven Veils"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-23", "Saint George's Day"),
            ("2025-04-25", "Liberation Day; Saint Mark's Day"),
            ("2025-04-27", "Saint Liberal's Day"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-03", "Saint Nicholas the Pilgrim's Day"),
            ("2025-05-04", "Saint Cyriacus's Day"),
            ("2025-05-06", "Saint Secundus of Asti's Day"),
            ("2025-05-08", "Saint Victor the Moor's Day"),
            ("2025-05-10", "Saint Catald's Day"),
            ("2025-05-11", "Saint Justin of Chieti's Day"),
            ("2025-05-15", "Saint Pontian's Day"),
            ("2025-05-19", "Saint Peter Celestine's Day"),
            ("2025-05-21", "Saint Zeno's Day"),
            ("2025-05-22", "Saint Julia's Day"),
            ("2025-05-30", "Saint Gerard of Potenza's Day"),
            ("2025-06-01", "Saint Crescentinus's Day"),
            ("2025-06-02", "Republic Day"),
            ("2025-06-03", "Our Lady of the Letter"),
            ("2025-06-10", "Saint Maximus of Aveia's Day"),
            ("2025-06-13", "Saint Anthony of Padua's Day"),
            ("2025-06-17", "Saint Ranieri's Day"),
            ("2025-06-19", "Saints Gervasius and Protasius's Day"),
            ("2025-06-20", "Saint Silverius's Day"),
            ("2025-06-24", "Saint John's Day"),
            ("2025-06-26", "Saint Vigilius's Day"),
            ("2025-06-29", "Saints Peter and Paul's Day"),
            ("2025-07-02", "Our Lady of the Bruna; Visitation of Mary Day"),
            ("2025-07-04", "Saint Antoninus of Piacenza's Day"),
            ("2025-07-06", "Saint Maria Goretti's Day"),
            (
                "2025-07-12",
                "Saint Paulinus of Lucca's Day; Saints Hermagoras and Fortunatus's Day",
            ),
            ("2025-07-15", "Saint Rosalia's Day"),
            ("2025-07-16", "Saint Vitalian's Day"),
            ("2025-07-23", "Saint Apollinaris's Day"),
            ("2025-07-25", "Saint James's Day"),
            ("2025-08-01", "Saint Eusebius of Vercelli's Day"),
            ("2025-08-05", "Our Lady of the Snows; Saint Emidius's Day"),
            ("2025-08-07", "Saint Albert of Trapani's Day; Saint Donatus of Arezzo's Day"),
            ("2025-08-10", "Saint Lawrence's Day"),
            ("2025-08-11", "Saint Clare of Assisi's Day"),
            ("2025-08-15", "Assumption Day; Assumption Of Mary Day"),
            ("2025-08-16", "Assumption Day"),
            ("2025-08-24", "Saint Bartholomew's Day"),
            ("2025-08-26", "Saint Alexander of Bergamo's Day; Saint Orontius's Day"),
            ("2025-08-29", "Saint John's Day"),
            ("2025-08-31", "Saint Abbondius's Day; Saint Julian the Hospitaller's Day"),
            ("2025-09-04", "Saint Rose of Viterbo's Day"),
            (
                "2025-09-07",
                "Saint Grat's Day; Saint Theodore of Amasea and Saint Lawrence of Brindisi's Day",
            ),
            ("2025-09-08", "Our Lady of Graces; Our Lady of Monte Berico"),
            ("2025-09-19", "Saint Januarius's Day"),
            ("2025-09-21", "Saint Matthew's Day; Saint Richard of Andria's Day"),
            ("2025-09-24", "Saint Terentius of Pesaro's Day"),
            ("2025-09-29", "Saint Michael the Archangel's Day"),
            ("2025-10-04", "Saint Francis of Assisi's Day; Saint Petronius's Day"),
            ("2025-10-09", "Saint Dionysius's Day"),
            ("2025-10-10", "Saint Cetteus's Day"),
            ("2025-10-14", "Saint Gaudentius's Day"),
            ("2025-10-30", "Saint Saturninus of Cagliari's Day"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-02", "National Unity Day"),
            ("2025-11-03", "Saint Justus's Day"),
            ("2025-11-10", "Saint Baudolino's Day"),
            ("2025-11-11", "Saint Martin's Day"),
            ("2025-11-13", "Saint Homobonus's Day"),
            ("2025-11-21", "Our Lady of Health"),
            ("2025-11-24", "Saint Prosper of Reggio's Day"),
            ("2025-11-26", "Saint Bellinus's Day; Saint Leonard of Porto Maurizio's Day"),
            ("2025-12-01", "Saint Ansanus's Day"),
            ("2025-12-04", "Saint Barbara's Day"),
            ("2025-12-06", "Saint Nicholas's Day"),
            ("2025-12-07", "Saint Ambrose's Day"),
            ("2025-12-08", "Immaculate Conception"),
            ("2025-12-09", "Saint Syrus's Day"),
            ("2025-12-13", "Saint Lucy's Day"),
            ("2025-12-19", "Saint Berardo's Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Saint Stephen's Day"),
            ("2025-12-30", "Saint Roger's Day"),
        )
