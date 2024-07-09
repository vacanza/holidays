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

from holidays.entities.ISO_3166.IT import ItHolidays
from tests.common import CommonCountryTests


class TestItHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ItHolidays, years=range(1946, 2050))

    def test_new_years_day(self):
        self.assertHolidayName("Capodanno", (f"{year}-01-01" for year in range(1946, 2050)))

    def test_epiphany_day(self):
        self.assertHolidayName(
            "Epifania del Signore", (f"{year}-01-06" for year in range(1946, 2050))
        )

    def test_saint_josephs_day(self):
        name = "San Giuseppe"
        self.assertHolidayName(name, (f"{year}-03-19" for year in range(1946, 1977)))
        self.assertNoHolidayName(name, range(1977, 2050))

    def test_easter_sunday(self):
        name = "Pasqua di Resurrezione"
        self.assertHolidayName(name, range(1946, 2050))
        self.assertHolidayName(
            name,
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
        )

    def test_easter_monday(self):
        name = "Lunedì dell'Angelo"
        self.assertHolidayName(name, range(1946, 2050))
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )

    def test_liberation_day(self):
        name = "Festa della Liberazione"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1946, 2050)))
        self.assertNoHolidayName(name, ItHolidays(years=1945))

    def test_labor_day(self):
        self.assertHolidayName(
            "Festa dei Lavoratori", (f"{year}-05-01" for year in range(1946, 2050))
        )

    def test_ascension_day(self):
        name = "Ascensione Nostro Signore"
        self.assertHolidayName(name, range(1946, 1977))
        self.assertHolidayName(
            name,
            "1971-05-20",
            "1972-05-11",
            "1973-05-31",
            "1974-05-23",
            "1975-05-08",
            "1976-05-27",
        )
        self.assertNoHolidayName(name, range(1977, 2050))

    def test_republic_day(self):
        name = "Festa della Repubblica"
        self.assertHolidayName(name, (f"{year}-06-02" for year in range(1948, 2050)))
        self.assertNoHolidayName(name, range(1946, 1948))

    def test_saints_peter_and_paul_day(self):
        name = "Santi Pietro e Paolo"
        self.assertHolidayName(name, (f"{year}-06-29" for year in range(1946, 1977)))
        self.assertNoHolidayName(name, range(1977, 2050))

    def test_corpus_christi_day(self):
        name = "Corpus Domini"
        self.assertHolidayName(name, range(1946, 1977))
        self.assertHolidayName(
            name,
            "1971-06-10",
            "1972-06-01",
            "1973-06-21",
            "1974-06-13",
            "1975-05-29",
            "1976-06-17",
        )
        self.assertNoHolidayName(name, range(1977, 2050))

    def test_assumption_of_mary_day(self):
        self.assertHolidayName(
            "Assunzione della Vergine", (f"{year}-08-15" for year in range(1946, 2050))
        )

    def test_all_saints_day(self):
        self.assertHolidayName("Tutti i Santi", (f"{year}-11-01" for year in range(1946, 2050)))

    def test_national_unity_and_armed_forces_day(self):
        name = "Giornata dell'Unità Nazionale e delle Forze Armate"
        self.assertHolidayName(name, (f"{year}-11-04" for year in range(1946, 1977)))
        self.assertNoHolidayName(name, range(1977, 2050))

    def test_immaculate_conception_day(self):
        self.assertHolidayName(
            "Immacolata Concezione", (f"{year}-12-08" for year in range(1946, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Natale", (f"{year}-12-25" for year in range(1946, 2050)))

    def test_saint_stephens_day(self):
        name = "Santo Stefano"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1947, 2050)))
        self.assertNoHolidayName(name, range(1946, 1947))

    def test_2022(self):
        self.assertHolidays(
            ItHolidays(years=2022),
            ("2022-01-01", "Capodanno"),
            ("2022-01-06", "Epifania del Signore"),
            ("2022-04-17", "Pasqua di Resurrezione"),
            ("2022-04-18", "Lunedì dell'Angelo"),
            ("2022-04-25", "Festa della Liberazione"),
            ("2022-05-01", "Festa dei Lavoratori"),
            ("2022-06-02", "Festa della Repubblica"),
            ("2022-08-15", "Assunzione della Vergine"),
            ("2022-11-01", "Tutti i Santi"),
            ("2022-12-08", "Immacolata Concezione"),
            ("2022-12-25", "Natale"),
            ("2022-12-26", "Santo Stefano"),
        )

    def test_province_specific_days(self):
        subdiv_holidays = {
            "AG": ("2017-02-25",),
            "AL": ("2017-11-10",),
            "AN": ("2017-05-04",),
            "AO": ("2017-09-07",),
            "AP": ("2017-08-05",),
            "AQ": ("2017-06-10",),
            "AR": ("2017-08-07",),
            "AT": ("2017-05-02",),
            "AV": ("2017-02-14",),
            "BA": ("2017-12-06",),
            "BG": ("2017-08-26",),
            "BI": ("2017-12-26",),
            "BL": ("2017-12-26",),
            "BN": ("2017-08-24",),
            "BO": ("2017-10-04",),
            "BR": ("2017-09-03",),
            "BS": ("2017-02-15",),
            "BT": ("2017-05-03", "2017-09-17", "2017-12-30"),
            "Barletta": ("2017-12-30",),
            "Andria": ("2017-09-17",),
            "Trani": ("2017-05-03",),
            "BZ": ("2017-06-05", "2017-08-15"),
            "CA": ("2017-10-30",),
            "CB": ("2017-04-23",),
            "CE": ("2017-01-20",),
            "CH": ("2017-05-11",),
            "CL": ("2017-09-29",),
            "CN": ("2017-09-29",),
            "CO": ("2017-08-31",),
            "CR": ("2017-11-13",),
            "CS": ("2017-02-12",),
            "CT": ("2017-02-05",),
            "CZ": ("2017-07-16",),
            "EN": ("2017-07-02",),
            "FC": ("2017-02-04", "2017-06-24"),
            "Forli": ("2017-02-04",),
            "Cesena": ("2017-06-24",),
            "FE": ("2017-04-23",),
            "FG": ("2017-03-22",),
            "FI": ("2017-06-24",),
            "FM": ("2017-08-15", "2017-08-16"),
            "FR": ("2017-06-20",),
            "GE": ("2017-06-24",),
            "GO": ("2017-03-16",),
            "GR": ("2017-08-10",),
            "IM": ("2017-11-26",),
            "IS": ("2017-05-19",),
            "KR": ("2017-10-09",),
            "LC": ("2017-12-06",),
            "LE": ("2017-08-26",),
            "LI": ("2017-05-22",),
            "LO": ("2017-01-19",),
            "LT": ("2017-04-25", "2017-07-06"),
            "LU": ("2017-07-12",),
            "MB": ("2017-06-24",),
            "MC": ("2017-08-31",),
            "ME": ("2017-06-03",),
            "MI": ("2017-12-07",),
            "MN": ("2017-03-18",),
            "MO": ("2017-01-31",),
            "MS": ("2017-10-04",),
            "MT": ("2017-07-02",),
            "NA": ("2017-09-19",),
            "NO": ("2017-01-22",),
            "NU": ("2017-08-05",),
            "OR": ("2017-02-13",),
            "PA": ("2017-07-15",),
            "PC": ("2017-07-04",),
            "PD": ("2017-06-13",),
            "PE": ("2017-10-10",),
            "PG": ("2017-08-11", "2017-10-04"),
            "PI": ("2017-06-17",),
            "PN": ("2017-04-25", "2017-09-08"),
            "PO": ("2017-12-26",),
            "PR": ("2017-01-13",),
            "PT": ("2017-07-25",),
            "PU": ("2017-06-01", "2017-09-24"),
            "Pesaro": ("2017-09-24",),
            "Urbino": ("2017-06-01",),
            "PV": ("2017-12-09",),
            "PZ": ("2017-05-30",),
            "RA": ("2017-07-23",),
            "RC": ("2017-04-23",),
            "RE": ("2017-11-24",),
            "RG": ("2017-04-23", "2017-08-29"),
            "RI": ("2017-12-04",),
            "RM": ("2017-06-29",),
            "RN": ("2017-10-14",),
            "RO": ("2017-11-26",),
            "SA": ("2017-09-21",),
            "SI": ("2017-12-01",),
            "SO": ("2017-06-19",),
            "SP": ("2017-03-19",),
            "SR": ("2017-12-13",),
            "SS": ("2017-12-06",),
            "SU": ("2017-05-18",),
            "SV": ("2017-03-18",),
            "TA": ("2017-05-10",),
            "TE": ("2017-12-19",),
            "TN": ("2017-06-26",),
            "TO": ("2017-06-24",),
            "TP": ("2017-08-07",),
            "TR": ("2017-02-14",),
            "TS": ("2017-11-03",),
            "TV": ("2017-04-27",),
            "UD": ("2017-07-12",),
            "VA": ("2017-05-08",),
            "VB": ("2017-05-08",),
            "VC": ("2017-08-01",),
            "VE": ("2017-04-25", "2017-11-21"),
            "VI": ("2017-09-08",),
            "VR": ("2017-05-21",),
            "VT": ("2017-09-04",),
            "VV": ("2017-03-01",),
        }
        for subdiv, holidays in subdiv_holidays.items():
            self.assertHoliday(ItHolidays(subdiv=subdiv, years=2017), holidays)
