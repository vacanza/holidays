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

from holidays.constants import BANK, PUBLIC, SCHOOL
from holidays.countries.belgium import Belgium
from tests.common import CommonCountryTests


class TestBelgium(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Belgium, with_subdiv_categories=True)

    def test_no_school_holidays(self):
        self.assertNoHolidays(Belgium(categories=SCHOOL, years=range(self.start_year, 2050)))
        for subdiv in Belgium.subdivisions:
            self.assertNoHolidays(
                Belgium(subdiv=subdiv, categories=SCHOOL, years=Belgium.start_year - 1)
            )

    def test_new_years_day(self):
        self.assertHolidayName("Nieuwjaar", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Goede vrijdag"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Pasen"
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

    def test_easter_monday(self):
        name = "Paasmaandag"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Dag van de Arbeid", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "O. L. H. Hemelvaart"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_friday_after_ascension_day(self):
        name = "Vrijdag na O. L. H. Hemelvaart"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-05-22",
            "2021-05-14",
            "2022-05-27",
            "2023-05-19",
            "2024-05-10",
            "2025-05-30",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_whit_sunday(self):
        name = "Pinksteren"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Pinkstermaandag"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_day(self):
        self.assertHolidayName("Nationale feestdag", (f"{year}-07-21" for year in self.full_range))

    def test_assumption_day(self):
        self.assertHolidayName(
            "O. L. V. Hemelvaart", (f"{year}-08-15" for year in self.full_range)
        )

    def test_all_saints_day(self):
        self.assertHolidayName("Allerheiligen", (f"{year}-11-01" for year in self.full_range))

    def test_armistice_day(self):
        self.assertHolidayName("Wapenstilstand", (f"{year}-11-11" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Kerstmis", (f"{year}-12-25" for year in self.full_range))

    def test_bank_holiday(self):
        name = "Banksluitingsdag"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-26" for year in self.full_range))

    def test_school_christmas_break(self):
        name = "Kerstvakantie"
        self.assertNoHolidayName(name)
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(
                name,
                holidays,
                "2015-12-21",
                "2016-01-03",
                "2016-12-26",
                "2017-01-08",
                "2019-12-23",
                "2020-01-05",
                "2020-12-21",
                "2021-01-03",
                "2021-12-27",
                "2022-01-09",
                "2022-12-26",
                "2023-01-08",
                "2023-12-25",
                "2024-01-07",
                "2024-12-23",
                "2025-01-05",
                "2025-12-22",
                "2026-01-04",
                "2026-12-21",
                "2027-01-03",
                "2027-12-27",
                "2028-01-09",
                "2028-12-25",
                "2029-01-07",
                "2029-12-24",
                "2030-01-06",
            )
            self.assertNoHoliday(
                holidays,
                "2015-12-20",
                "2016-01-04",
                "2016-12-25",
                "2017-01-09",
                "2021-12-26",
                "2022-01-10",
                "2026-12-20",
                "2027-01-04",
            )
            self.assertHolidayName(name, holidays, self.full_range)

    def test_school_carnival_break(self):
        name = "Krokusvakantie"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_school_holidays.items():
            # Two weeks in the French Community since 2023.
            self.assertHolidayName(
                name,
                holidays,
                "2013-02-11",
                "2013-02-17",
                "2016-02-08",
                "2016-02-14",
                "2019-03-04",
                "2019-03-10",
                "2020-02-24",
                "2020-03-01",
                "2022-02-28",
                "2022-03-06",
            )
            self.assertNoHoliday(holidays, "2019-03-03", "2019-03-11", "2022-02-27", "2022-03-07")
            self.assertHolidayName(name, holidays, self.full_range)
            if subdiv == "French":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2023-02-20",
                    "2023-03-05",
                    "2024-02-26",
                    "2024-03-10",
                    "2025-02-24",
                    "2025-03-09",
                    "2026-02-16",
                    "2026-03-01",
                    "2027-02-22",
                    "2027-03-07",
                    "2028-02-28",
                    "2028-03-12",
                    "2029-02-26",
                    "2029-03-11",
                )
                self.assertNoHoliday(
                    holidays,
                    "2023-02-19",
                    "2023-03-06",
                    "2027-02-08",
                    "2027-02-21",
                    "2027-03-08",
                )
            else:
                self.assertHolidayName(
                    name,
                    holidays,
                    "2023-02-20",
                    "2023-02-26",
                    "2024-02-12",
                    "2024-02-18",
                    "2025-03-03",
                    "2025-03-09",
                    "2026-02-16",
                    "2026-02-22",
                    "2027-02-08",
                    "2027-02-14",
                    "2028-02-28",
                    "2028-03-05",
                    "2029-02-12",
                    "2029-02-18",
                    "2030-03-04",
                    "2030-03-10",
                )
                self.assertNoHoliday(holidays, "2023-02-27", "2025-03-10", "2027-02-15")

    def test_school_easter_break(self):
        name = "Paasvakantie"
        self.assertNoHolidayName(name)

        # Flemish Community.
        self.assertSubdivFlemishSchoolHolidayName(
            name,
            "2001-04-02",
            "2001-04-16",
            "2016-03-28",
            "2016-04-10",
            "2019-04-08",
            "2019-04-22",
            "2022-04-04",
            "2022-04-18",
            "2023-04-03",
            "2023-04-16",
            "2024-04-01",
            "2024-04-14",
            "2025-04-07",
            "2025-04-21",
            "2026-04-06",
            "2026-04-19",
            "2027-03-29",
            "2027-04-11",
            "2028-04-03",
            "2028-04-17",
            "2029-04-02",
            "2029-04-15",
            "2030-04-08",
            "2030-04-22",
        )
        self.assertNoSubdivFlemishSchoolHoliday(
            "2001-04-01",
            "2001-04-17",
            "2016-03-27",
            "2016-04-11",
            "2019-04-07",
            "2019-04-23",
            "2025-04-06",
            "2025-04-22",
            "2027-03-28",
            "2027-04-12",
        )
        self.assertSubdivFlemishSchoolHolidayName(name, self.full_range)

        # Starts on Easter Monday in the German-speaking Community since 2025.
        self.assertSubdivGermanSchoolHolidayName(
            name,
            "2001-04-02",
            "2001-04-16",
            "2019-04-08",
            "2019-04-22",
            "2020-04-06",
            "2020-04-19",
            "2022-04-04",
            "2022-04-18",
            "2023-04-03",
            "2023-04-16",
            "2024-04-01",
            "2024-04-14",
            "2025-04-21",
            "2025-05-04",
            "2026-04-06",
            "2026-04-19",
            "2027-03-29",
            "2027-04-11",
            "2028-04-17",
            "2028-04-30",
            "2029-04-02",
            "2029-04-15",
        )
        self.assertNoSubdivGermanSchoolHoliday(
            "2001-04-01",
            "2001-04-17",
            "2023-04-02",
            "2023-04-17",
            "2025-04-07",
            "2025-04-20",
            "2025-05-05",
            "2028-04-03",
            "2028-04-16",
        )
        self.assertSubdivGermanSchoolHolidayName(name, self.full_range)

        # French Community.
        self.assertSubdivFrenchSchoolHolidayName(
            name,
            # Easter-based until 2022.
            "2001-04-02",
            "2001-04-16",
            "2013-04-01",
            "2013-04-14",
            "2014-04-07",
            "2014-04-21",
            "2015-04-06",
            "2015-04-19",
            "2016-03-28",
            "2016-04-10",
            "2017-04-03",
            "2017-04-17",
            "2018-04-02",
            "2018-04-15",
            "2019-04-08",
            "2019-04-22",
            "2020-04-06",
            "2020-04-19",
            "2021-04-05",
            "2021-04-18",
            "2022-04-04",
            "2022-04-18",
            # Starting on the Monday of the week of May 1 since 2023.
            "2023-05-01",
            "2023-05-14",
            "2024-04-29",
            "2024-05-12",
            "2025-04-28",
            "2025-05-11",
            "2026-04-27",
            "2026-05-10",
            "2027-04-26",
            "2027-05-09",
            "2028-05-01",
            "2028-05-14",
            "2029-04-30",
            "2029-05-13",
        )
        self.assertNoSubdivFrenchSchoolHoliday(
            "2001-04-01",
            "2001-04-17",
            "2017-04-02",
            "2017-04-18",
            "2022-04-03",
            "2022-04-19",
            "2023-04-30",
            "2023-05-15",
            "2026-04-26",
            "2026-05-11",
            "2028-04-30",
            "2028-05-15",
        )
        self.assertSubdivFrenchSchoolHolidayName(name, self.full_range)

    def test_school_summer_break(self):
        name = "Zomervakantie"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_school_holidays.items():
            self.assertHolidayName(
                name,
                holidays,
                "2019-07-01",
                "2019-08-31",
                "2020-07-01",
                "2020-08-31",
                "2021-07-01",
                "2021-08-31",
            )
            self.assertNoHoliday(holidays, "2019-06-30", "2019-09-01", "2021-06-30", "2021-09-01")
            self.assertHolidayName(name, holidays, self.full_range)
            if subdiv == "French":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2022-07-01",
                    "2022-08-28",
                    "2023-07-08",
                    "2023-08-27",
                    "2024-07-06",
                    "2024-08-25",
                    "2025-07-05",
                    "2025-08-24",
                    "2026-07-04",
                    "2026-08-23",
                    "2027-07-03",
                    "2027-08-29",
                    "2028-07-08",
                    "2028-08-27",
                    "2029-07-07",
                    "2029-08-26",
                )
                self.assertNoHoliday(
                    holidays,
                    "2022-08-29",
                    "2023-07-07",
                    "2023-08-28",
                    "2024-07-05",
                    "2024-08-26",
                    "2025-07-04",
                    "2025-08-25",
                    "2026-07-03",
                    "2026-08-24",
                    "2027-07-02",
                    "2027-08-30",
                    "2028-07-07",
                    "2028-08-28",
                    "2029-07-06",
                    "2029-08-27",
                )
            else:
                self.assertHolidayName(
                    name, holidays, "2022-07-01", "2022-08-31", "2027-07-01", "2027-08-31"
                )
                self.assertNoHoliday(holidays, "2022-06-30", "2022-09-01", "2027-06-30")

    def test_school_autumn_break(self):
        name = "Herfstvakantie"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_school_holidays.items():
            # Two weeks in the French Community since 2022.
            self.assertHolidayName(
                name,
                holidays,
                "2013-10-28",
                "2013-11-03",
                "2014-10-27",
                "2014-11-02",
                "2015-11-02",
                "2015-11-08",
                "2016-10-31",
                "2016-11-06",
                "2019-10-28",
                "2019-11-03",
                "2020-11-02",
                "2020-11-08",
                "2021-11-01",
                "2021-11-07",
            )
            self.assertNoHoliday(
                holidays,
                "2013-10-27",
                "2013-11-04",
                "2015-11-01",
                "2015-11-09",
                "2020-11-01",
                "2020-11-09",
            )
            self.assertHolidayName(name, holidays, self.full_range)
            if subdiv == "French":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2022-10-24",
                    "2022-11-06",
                    "2023-10-23",
                    "2023-11-05",
                    "2024-10-21",
                    "2024-11-03",
                    "2025-10-20",
                    "2025-11-02",
                    "2026-10-19",
                    "2026-11-01",
                    "2027-10-25",
                    "2027-11-07",
                    "2028-10-23",
                    "2028-11-05",
                )
                self.assertNoHoliday(
                    holidays, "2022-10-23", "2022-11-07", "2026-10-18", "2027-10-24", "2027-11-08"
                )
            else:
                self.assertHolidayName(
                    name,
                    holidays,
                    "2023-10-30",
                    "2023-11-05",
                    "2024-10-28",
                    "2024-11-03",
                    "2025-10-27",
                    "2025-11-02",
                    "2026-11-02",
                    "2026-11-08",
                    "2027-11-01",
                    "2027-11-07",
                    "2028-10-30",
                    "2028-11-05",
                    "2029-10-29",
                    "2029-11-04",
                )
                self.assertNoHoliday(holidays, "2026-10-26", "2026-11-01", "2026-11-09")

    def test_school_labor_day(self):
        name = "Dag van de Arbeid"
        self.assertSubdivFlemishSchoolHolidayName(
            name, (f"{year}-05-01" for year in self.full_range)
        )
        self.assertSubdivGermanSchoolHolidayName(
            name, (f"{year}-05-01" for year in self.full_range)
        )
        # Falls within the Easter Break since 2023.
        self.assertSubdivFrenchSchoolHolidayName(
            name, (f"{year}-05-01" for year in range(self.start_year, 2023))
        )
        self.assertNoSubdivFrenchSchoolHolidayName(name, range(2023, 2050))
        self.assertSubdivFrenchSchoolHoliday(f"{year}-05-01" for year in range(2023, 2050))

    def test_school_easter_monday(self):
        name = "Paasmaandag"
        # Always falls within the Easter Break.
        self.assertNoSubdivFlemishSchoolHolidayName(name)
        self.assertNoSubdivGermanSchoolHolidayName(name)
        self.assertSubdivFlemishSchoolHoliday(
            "2019-04-22", "2022-04-18", "2024-04-01", "2025-04-21", "2027-03-29"
        )
        self.assertSubdivGermanSchoolHoliday(
            "2019-04-22", "2022-04-18", "2024-04-01", "2025-04-21", "2027-03-29"
        )
        # Falls within the Easter Break until 2022.
        self.assertNoSubdivFrenchSchoolHolidayName(name, range(self.start_year, 2023))
        self.assertSubdivFrenchSchoolHoliday("2019-04-22", "2022-04-18")
        self.assertSubdivFrenchSchoolHolidayName(
            name,
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
            "2027-03-29",
            "2028-04-17",
            "2029-04-02",
        )
        self.assertSubdivFrenchSchoolHolidayName(name, range(2023, 2050))

    def test_school_ascension_day(self):
        name = "O. L. H. Hemelvaart"
        dts = (
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
            "2026-05-14",
            "2027-05-06",
        )
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, self.full_range)

    def test_school_friday_after_ascension_day(self):
        name = "Vrijdag na O. L. H. Hemelvaart"
        self.assertSubdivFlemishSchoolHolidayName(
            name,
            "2019-05-31",
            "2020-05-22",
            "2021-05-14",
            "2022-05-27",
            "2023-05-19",
            "2024-05-10",
            "2025-05-30",
            "2026-05-15",
            "2027-05-07",
        )
        self.assertSubdivFlemishSchoolHolidayName(name, self.full_range)
        self.assertNoSubdivGermanSchoolHolidayName(name)
        self.assertNoSubdivGermanSchoolHoliday("2019-05-31", "2024-05-10", "2027-05-07")
        self.assertSubdivFrenchSchoolHolidayName(
            name, "2015-05-15", "2016-05-06", "2020-05-22", "2021-05-14"
        )
        self.assertNoSubdivFrenchSchoolHolidayName(
            name, range(self.start_year, 2015), 2017, 2018, 2019, range(2022, 2050)
        )
        self.assertNoSubdivFrenchSchoolHoliday("2017-05-26", "2019-05-31", "2022-05-27")

    def test_school_pentecost_monday(self):
        name = "Pinkstermaandag"
        dts = (
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
            "2026-05-25",
            "2027-05-17",
        )
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, self.full_range)

    def test_school_armistice_day(self):
        name = "Wapenstilstand"
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(name, holidays, (f"{year}-11-11" for year in self.full_range))

    def test_school_french_community_day(self):
        name = "Feestdag van de Franse Gemeenschap"
        self.assertNoHolidayName(name)
        self.assertNoSubdivFlemishSchoolHolidayName(name)
        self.assertNoSubdivGermanSchoolHolidayName(name)
        self.assertSubdivFrenchSchoolHolidayName(
            name, (f"{year}-09-27" for year in range(1975, 2050))
        )
        self.assertNoSubdivFrenchSchoolHolidayName(name, range(self.start_year, 1975))

    def test_school_german_speaking_community_day(self):
        name = "Feestdag van de Duitstalige Gemeenschap"
        self.assertNoHolidayName(name)
        self.assertNoSubdivFlemishSchoolHolidayName(name)
        self.assertNoSubdivFrenchSchoolHolidayName(name)
        self.assertSubdivGermanSchoolHolidayName(
            name, (f"{year}-11-15" for year in range(1990, 2050))
        )
        self.assertNoSubdivGermanSchoolHolidayName(name, range(self.start_year, 1990))

    def test_school_all_souls_day(self):
        name = "Allerzielen"
        self.assertNoHolidayName(name)
        self.assertNoSubdivFlemishSchoolHolidayName(name)
        self.assertNoSubdivGermanSchoolHolidayName(name)
        # Only when Nov 1 falls on Sunday since 2022.
        self.assertSubdivFrenchSchoolHolidayName(name, "2026-11-02", "2037-11-02", "2043-11-02")
        self.assertNoSubdivFrenchSchoolHolidayName(
            name, range(self.start_year, 2026), range(2027, 2037), range(2038, 2043)
        )
        self.assertSubdivFrenchSchoolHoliday("2020-11-02", "2025-11-02", "2027-11-02")

    def test_school_mardi_gras(self):
        name = "Vastenavond"
        self.assertNoHolidayName(name)
        self.assertNoSubdivFlemishSchoolHolidayName(name)
        self.assertNoSubdivGermanSchoolHolidayName(name)
        self.assertSubdivFrenchSchoolHolidayName(
            name,
            "2024-02-13",
            "2027-02-09",
            "2029-02-13",
            "2032-02-10",
            "2035-02-06",
        )
        self.assertNoSubdivFrenchSchoolHolidayName(
            name, range(self.start_year, 2024), 2025, 2026, 2028, 2030, 2031, 2033, 2034, 2036
        )
        self.assertNoSubdivFrenchSchoolHolidayName(name, "2025-03-04", "2033-03-01")
        self.assertSubdivFrenchSchoolHoliday("2023-02-21", "2026-02-17", "2028-02-29")

    def test_school_bridge_holiday(self):
        name = "Brugdag"
        self.assertNoHolidayName(name)
        self.assertNoSubdivFlemishSchoolHolidayName(name)
        self.assertNoSubdivGermanSchoolHolidayName(name)
        self.assertSubdivFrenchSchoolHolidayName(name, "2016-05-04", "2021-04-30")
        self.assertNoSubdivFrenchSchoolHolidayName(
            name, range(self.start_year, 2016), range(2017, 2021), range(2022, 2050)
        )

    def test_school_days(self):
        self.assertNoSubdivFlemishSchoolHoliday(
            "2025-09-01", "2026-01-05", "2026-02-23", "2026-04-20", "2026-06-30"
        )
        self.assertNoSubdivFrenchSchoolHoliday(
            "2021-09-01", "2022-06-30", "2025-08-25", "2026-01-05", "2026-03-02", "2026-07-03"
        )
        self.assertNoSubdivGermanSchoolHoliday(
            "2025-09-01", "2026-01-05", "2026-02-23", "2026-04-20", "2026-06-30"
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "Nieuwjaar"),
            ("2020-04-12", "Pasen"),
            ("2020-04-13", "Paasmaandag"),
            ("2020-05-01", "Dag van de Arbeid"),
            ("2020-05-21", "O. L. H. Hemelvaart"),
            ("2020-05-31", "Pinksteren"),
            ("2020-06-01", "Pinkstermaandag"),
            ("2020-07-21", "Nationale feestdag"),
            ("2020-08-15", "O. L. V. Hemelvaart"),
            ("2020-11-01", "Allerheiligen"),
            ("2020-11-11", "Wapenstilstand"),
            ("2020-12-25", "Kerstmis"),
        )

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Nieuwjaar"),
            ("2021-04-04", "Pasen"),
            ("2021-04-05", "Paasmaandag"),
            ("2021-05-01", "Dag van de Arbeid"),
            ("2021-05-13", "O. L. H. Hemelvaart"),
            ("2021-05-23", "Pinksteren"),
            ("2021-05-24", "Pinkstermaandag"),
            ("2021-07-21", "Nationale feestdag"),
            ("2021-08-15", "O. L. V. Hemelvaart"),
            ("2021-11-01", "Allerheiligen"),
            ("2021-11-11", "Wapenstilstand"),
            ("2021-12-25", "Kerstmis"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Nieuwjaar"),
            ("2022-04-17", "Pasen"),
            ("2022-04-18", "Paasmaandag"),
            ("2022-05-01", "Dag van de Arbeid"),
            ("2022-05-26", "O. L. H. Hemelvaart"),
            ("2022-06-05", "Pinksteren"),
            ("2022-06-06", "Pinkstermaandag"),
            ("2022-07-21", "Nationale feestdag"),
            ("2022-08-15", "O. L. V. Hemelvaart"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Wapenstilstand"),
            ("2022-12-25", "Kerstmis"),
        )

    def test_2022_bank(self):
        self.assertBankHolidaysInYear(
            2022,
            ("2022-04-15", "Goede vrijdag"),
            ("2022-05-27", "Vrijdag na O. L. H. Hemelvaart"),
            ("2022-12-26", "Banksluitingsdag"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaar"),
            ("2022-04-15", "Goede vrijdag"),
            ("2022-04-17", "Pasen"),
            ("2022-04-18", "Paasmaandag"),
            ("2022-05-01", "Dag van de Arbeid"),
            ("2022-05-26", "O. L. H. Hemelvaart"),
            ("2022-05-27", "Vrijdag na O. L. H. Hemelvaart"),
            ("2022-06-05", "Pinksteren"),
            ("2022-06-06", "Pinkstermaandag"),
            ("2022-07-21", "Nationale feestdag"),
            ("2022-08-15", "O. L. V. Hemelvaart"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Wapenstilstand"),
            ("2022-12-25", "Kerstmis"),
            ("2022-12-26", "Banksluitingsdag"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2022-01-01", "Neujahr"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostern"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-05-27", "Freitag nach Christi Himmelfahrt"),
            ("2022-06-05", "Pfingsten"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-07-21", "Nationalfeiertag"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Waffenstillstand"),
            ("2022-12-25", "Weihnachten"),
            ("2022-12-26", "Bankschlusstag"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-05-27", "Friday after Ascension Day"),
            ("2022-06-05", "Pentecost"),
            ("2022-06-06", "Pentecost Monday"),
            ("2022-07-21", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Armistice Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Bank Holiday"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Nouvel An"),
            ("2022-04-15", "Vendredi Saint"),
            ("2022-04-17", "Pâques"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-26", "Ascension"),
            ("2022-05-27", "Vendredi suivant l'Ascension"),
            ("2022-06-05", "Pentecôte"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-21", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Jour de l'Armistice"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "Jour de fermeture bancaire"),
            categories=(BANK, PUBLIC),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-05-27", "Пʼятниця після Вознесіння Господнього"),
            ("2022-06-05", "Пʼятидесятниця"),
            ("2022-06-06", "Другий день Пʼятидесятниці"),
            ("2022-07-21", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День перемирʼя"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Банківський вихідний"),
            categories=(BANK, PUBLIC),
        )

    def _assert_school_l10n(self, language, *expected):
        for subdiv, years, dt, name in expected:
            self.assertHolidayName(
                name,
                Belgium(subdiv=subdiv, years=years, language=language, categories=SCHOOL),
                dt,
            )

    def test_l10n_default_school(self):
        self._assert_school_l10n(
            None,
            ("Flemish", 2026, "2026-01-01", "Kerstvakantie"),
            ("Flemish", 2026, "2026-02-16", "Krokusvakantie"),
            ("Flemish", 2026, "2026-04-06", "Paasvakantie"),
            ("Flemish", 2026, "2026-07-01", "Zomervakantie"),
            ("Flemish", 2026, "2026-11-02", "Herfstvakantie"),
            ("French", 2021, "2021-04-30", "Brugdag"),
            ("French", 2024, "2024-02-13", "Vastenavond"),
            ("French", 2026, "2026-04-27", "Paasvakantie"),
            ("French", 2026, "2026-09-27", "Feestdag van de Franse Gemeenschap"),
            ("French", 2026, "2026-11-02", "Allerzielen"),
            ("German", 2026, "2026-11-15", "Feestdag van de Duitstalige Gemeenschap"),
        )

    def test_l10n_de_school(self):
        self._assert_school_l10n(
            "de",
            ("Flemish", 2026, "2026-01-01", "Weihnachtsferien"),
            ("Flemish", 2026, "2026-02-16", "Karnevalsferien"),
            ("Flemish", 2026, "2026-04-06", "Osterferien"),
            ("Flemish", 2026, "2026-07-01", "Sommerferien"),
            ("Flemish", 2026, "2026-11-02", "Herbstferien"),
            ("French", 2021, "2021-04-30", "Brückentag"),
            ("French", 2024, "2024-02-13", "Karnevalsdienstag"),
            ("French", 2026, "2026-04-27", "Osterferien"),
            ("French", 2026, "2026-09-27", "Feiertag der Französischen Gemeinschaft"),
            ("French", 2026, "2026-11-02", "Allerseelen"),
            ("German", 2026, "2026-11-15", "Tag der Deutschsprachigen Gemeinschaft"),
        )

    def test_l10n_en_us_school(self):
        self._assert_school_l10n(
            "en_US",
            ("Flemish", 2026, "2026-01-01", "Christmas Break"),
            ("Flemish", 2026, "2026-02-16", "Carnival Break"),
            ("Flemish", 2026, "2026-04-06", "Easter Break"),
            ("Flemish", 2026, "2026-07-01", "Summer Break"),
            ("Flemish", 2026, "2026-11-02", "Autumn Break"),
            ("French", 2021, "2021-04-30", "Bridge Holiday"),
            ("French", 2024, "2024-02-13", "Mardi Gras"),
            ("French", 2026, "2026-04-27", "Easter Break"),
            ("French", 2026, "2026-09-27", "French Community Day"),
            ("French", 2026, "2026-11-02", "All Souls' Day"),
            ("German", 2026, "2026-11-15", "German-speaking Community Day"),
        )

    def test_l10n_fr_school(self):
        self._assert_school_l10n(
            "fr",
            ("Flemish", 2026, "2026-01-01", "Vacances d'hiver"),
            ("Flemish", 2026, "2026-02-16", "Vacances de carnaval"),
            ("Flemish", 2026, "2026-04-06", "Vacances de printemps"),
            ("Flemish", 2026, "2026-07-01", "Vacances d'été"),
            ("Flemish", 2026, "2026-11-02", "Vacances d'automne"),
            ("French", 2021, "2021-04-30", "Jour pont"),
            ("French", 2024, "2024-02-13", "Mardi gras"),
            ("French", 2026, "2026-04-27", "Vacances de printemps"),
            ("French", 2026, "2026-09-27", "Fête de la Communauté française"),
            ("French", 2026, "2026-11-02", "Fête des morts"),
            ("German", 2026, "2026-11-15", "Fête de la Communauté germanophone"),
        )

    def test_l10n_uk_school(self):
        self._assert_school_l10n(
            "uk",
            ("Flemish", 2026, "2026-01-01", "Різдвяні канікули"),
            ("Flemish", 2026, "2026-02-16", "Карнавальні канікули"),
            ("Flemish", 2026, "2026-04-06", "Пасхальні канікули"),
            ("Flemish", 2026, "2026-07-01", "Літні канікули"),
            ("Flemish", 2026, "2026-11-02", "Осінні канікули"),
            ("French", 2021, "2021-04-30", "Проміжний вихідний"),
            ("French", 2024, "2024-02-13", "Масний вівторок"),
            ("French", 2026, "2026-04-27", "Пасхальні канікули"),
            ("French", 2026, "2026-09-27", "День Французької спільноти"),
            ("French", 2026, "2026-11-02", "День усіх померлих"),
            ("German", 2026, "2026-11-15", "День Німецькомовної спільноти"),
        )
