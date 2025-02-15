#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.countries.tuvalu import Tuvalu, TV, TUV
from tests.common import CommonCountryTests


class TestTuvalu(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1990, 2050)
        super().setUpClass(Tuvalu, years=years)
        cls.subdiv_holidays = {
            subdiv: Tuvalu(subdiv=subdiv, years=years) for subdiv in Tuvalu.subdivisions
        }

    def _assertVariableDays(self, year: int, subdiv_holidays: dict):  # noqa: N802
        observed_prov_holidays = {
            subdiv: Tuvalu(subdiv=subdiv, years=year) for subdiv in Tuvalu.subdivisions
        }
        for hol_date, hol_provs in subdiv_holidays.items():
            dt = date(year, *hol_date)
            for subdiv, prov_holidays in observed_prov_holidays.items():
                self.assertEqual(
                    dt in prov_holidays,
                    subdiv in hol_provs,
                    f"Failed date `{dt:%Y-%m-%d}`, province `{subdiv}`: {', '.join(hol_provs)}",
                )

    def test_country_aliases(self):
        self.assertAliases(Tuvalu, TV, TUV)

    def test_new_years(self):
        name = "Tausaga Fou"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1990, 2050)))

    def test_tuvalu_day(self):
        name = "Tutokotasi"
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1990, 2050)))
        self.assertHolidayName(name, (f"{year}-10-02" for year in range(1990, 2050)))

    def test_commonwealth_day(self):
        name = "Aso Atefenua"
        dt = (
            "2001-03-12",
            "2002-03-11",
            "2003-03-10",
            "2004-03-08",
            "2005-03-14",
            "2006-03-13",
            "2007-03-12",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2020))

    def test_gospel_day(self):
        name = "Te Aso o te Tala Lei"
        dt = (
            "2001-05-14",
            "2002-05-13",
            "2003-05-12",
            "2004-05-10",
            "2005-05-09",
            "2006-05-15",
            "2007-05-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2050))

        nkl_holidays = Tuvalu(subdiv="NKL", years=range(1990, 2050))
        name = "Aso o te Tala Lei"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NKL":
                self.assertHolidayName(
                    name, nkl_holidays, (f"{year}-05-10" for year in range(1990, 2050))
                )

    def test_king_birthday(self):
        name = "Asofanau Tupu"
        dt = (
            "2024-06-08",
            "2025-06-14",
            "2026-06-13",
            "2027-06-12",
            "2028-06-10",
            "2029-06-09",
            "2030-06-08",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2024, 2050))

    def test_queen_birthday(self):
        name = "Asofanau Fafine"
        dt = (
            "1990-06-09",
            "1991-06-08",
            "1992-06-13",
            "1999-06-12",
            "2002-06-08",
            "2007-06-09",
            "2008-06-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2024))

    def test_national_children_day(self):
        name = "Aso Tamaliki"
        dt = (
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2050))

    def test_national_youth_day(self):
        name = "Aso tupulaga"
        dt = (
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2019, 2050))

    def test_heir_to_the_throne_birthday(self):
        name = "Aso fanau o te sui ote Tupu"
        dt = (
            "2021-11-08",
            "2022-11-14",
            "2023-11-13",
            "2024-11-11",
            "2025-11-10",
            "2026-11-09",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2021, 2050))

    def test_boxing_ay(self):
        self.assertHolidayName("Aso Faipele", (f"{year}-12-26" for year in range(1990, 2050)))

    def test_good_friday(self):
        name = "Aso toe tu"
        dt = (
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2050))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dt)
            self.assertHolidayName(name, holidays, range(1990, 2050))

    def test_holy_saturday(self):
        name = "Aso Tapu"
        dt = (
            "1999-04-03",
            "2000-04-22",
            "2010-04-03",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2050))
        dt = (
            "1995-04-17",
            "2006-04-17",
            "2011-04-25",
            "2017-04-17",
            "2028-04-17",
        )
        self.assertHolidayName(f"{name} (fakamatakuga)", dt)

    def test_easter_monday(self):
        name = "Toe Tu aso gafua"
        dt = (
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1990, 2050))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dt)
            self.assertHolidayName(name, holidays, range(1990, 2050))

    def test_christmas_day(self):
        name = "Kilisimasi"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1990, 2050)))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, range(1990, 2050))

    def test_all_holidays(self):
        holidays_found = set()
        for subdiv in Tuvalu.subdivisions:
            holidays_found.update(
                Tuvalu(
                    subdiv=subdiv,
                    observed=False,
                    years=(1990, 2007, 2012, 2015, 2023),
                ).values()
            )
        all_holidays = {
            "Tausaga Fou",
            "Aso toe tu",
            "Aso Tapu",
            "Toe Tu aso gafua",
            "Aso Atefenua",
            "Te Aso o te Tala Lei",
            "Asofanau Fafine",
            "Aso Tamaliki",
            "Aso tupulaga",
            "Tutokotasi",
            "Aso fanau o te sui ote Tupu",
            "Kilisimasi",
            "Aso Faipele",
            "Aso o te matagi",
            "Te Aso o te Paula",
            "Aho o te Fakavae",
            "Te Po o Tefolaha",
            "Po Lahi",
            "Te Aso o te Setema",
            "Bogin te Ieka",
            "Te Aso O Tutasi",
            "Aso o te Tala Lei",
            "Te Aso Fiafia",
        }
        self.assertEqual(all_holidays, holidays_found)

    def test_cyclone_day(self):
        fun_holidays = Tuvalu(subdiv="FUN", years=range(1990, 2050))
        name = "Aso o te matagi"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "FUN":
                self.assertHolidayName(
                    name, fun_holidays, (f"{year}-10-21" for year in range(1990, 2050))
                )

    def test_the_day_of_the_bombing(self):
        fun_holidays = Tuvalu(subdiv="FUN", years=range(1990, 2050))
        name = "Te Aso o te Paula"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "FUN":
                self.assertHolidayName(
                    name, fun_holidays, (f"{year}-04-23" for year in range(1990, 2050))
                )

    def test_nanumaga_day(self):
        nmg_holidays = Tuvalu(subdiv="NMG", years=range(1990, 2050))
        name = "Aho o te Fakavae"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NMG":
                self.assertHolidayName(
                    name, nmg_holidays, (f"{year}-04-15" for year in range(1990, 2050))
                )

    def test_golden_jubilee(self):
        nma_holidays = Tuvalu(subdiv="NMA", years=range(1990, 2050))
        name = "Te Po o Tefolaha"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NMA":
                self.assertHolidayName(
                    name, nma_holidays, (f"{year}-01-08" for year in range(1990, 2050))
                )

    def test_big_day(self):
        nma_holidays = Tuvalu(subdiv="NMA", years=range(1990, 2050))
        name = "Po Lahi"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NMA":
                self.assertHolidayName(
                    name, nma_holidays, (f"{year}-02-03" for year in range(1990, 2050))
                )

    def test_niutao_day(self):
        nit_holidays = Tuvalu(subdiv="NIT", years=range(1990, 2050))
        name = "Te Aso o te Setema"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NIT":
                self.assertHolidayName(
                    name, nit_holidays, (f"{year}-09-17" for year in range(1990, 2050))
                )

    def test_day_of_the_flood(self):
        nui_holidays = Tuvalu(subdiv="NUI", years=range(1990, 2050))
        name = "Bogin te Ieka"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NUI":
                self.assertHolidayName(
                    name, nui_holidays, (f"{year}-02-16" for year in range(1990, 2050))
                )

    def test_nukufetau_day(self):
        nkf_holidays = Tuvalu(subdiv="NKF", years=range(1990, 2050))
        name = "Te Aso O Tutasi"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NKF":
                self.assertHolidayName(
                    name, nkf_holidays, (f"{year}-02-11" for year in range(1990, 2050))
                )

    def test_happy_day(self):
        vai_holidays = Tuvalu(subdiv="VAI", years=range(1990, 2050))
        name = "Te Aso Fiafia"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "VAI":
                self.assertHolidayName(
                    name, vai_holidays, (f"{year}-11-25" for year in range(1990, 2050))
                )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tausaga Fou"),
            ("2022-01-03", "Tausaga Fou (fakamatakuga)"),
            ("2022-01-08", "Te Po o Tefolaha"),
            ("2022-02-03", "Po Lahi"),
            ("2022-02-11", "Te Aso O Tutasi"),
            ("2022-02-16", "Bogin te Ieka"),
            ("2022-04-15", "Aho o te Fakavae; Aso toe tu"),
            ("2022-04-16", "Aso Tapu"),
            ("2022-04-18", "Aso Tapu (fakamatakuga); Toe Tu aso gafua"),
            ("2022-04-23", "Te Aso o te Paula"),
            ("2022-05-09", "Te Aso o te Tala Lei"),
            ("2022-05-10", "Aso o te Tala Lei"),
            ("2022-06-11", "Asofanau Fafine"),
            ("2022-08-01", "Aso tupulaga"),
            ("2022-09-17", "Te Aso o te Setema"),
            ("2022-10-01", "Tutokotasi"),
            ("2022-10-02", "Tutokotasi"),
            ("2022-10-03", "Tutokotasi (fakamatakuga)"),
            ("2022-10-04", "Tutokotasi (fakamatakuga)"),
            ("2022-10-10", "Aso Tamaliki"),
            ("2022-10-21", "Aso o te matagi"),
            ("2022-11-14", "Aso fanau o te sui ote Tupu"),
            ("2022-11-25", "Te Aso Fiafia"),
            ("2022-12-25", "Kilisimasi"),
            ("2022-12-26", "Aso Faipele"),
            ("2022-12-27", "Kilisimasi (fakamatakuga)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-08", "Golden Jubilee"),
            ("2022-02-03", "Big Day"),
            ("2022-02-11", "Nukufetau Day"),
            ("2022-02-16", "Day of the Flood"),
            ("2022-04-15", "Good Friday; Nanumaga Day"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-04-18", "Easter Monday; Holy Saturday (observed)"),
            ("2022-04-23", "The Day of the Bombing"),
            ("2022-05-09", "Gospel Day"),
            ("2022-05-10", "Gospel Day"),
            ("2022-06-11", "Queen's Birthday"),
            ("2022-08-01", "National Youth Day"),
            ("2022-09-17", "Niutao Day"),
            ("2022-10-01", "Tuvalu Day"),
            ("2022-10-02", "Tuvalu Day"),
            ("2022-10-03", "Tuvalu Day (observed)"),
            ("2022-10-04", "Tuvalu Day (observed)"),
            ("2022-10-10", "National Children's Day"),
            ("2022-10-21", "Cyclone Day"),
            ("2022-11-14", "Heir to the Throne's Birthday"),
            ("2022-11-25", "Happy Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_en_gb(self):
        self.assertLocalizedHolidays(
            "en_GB",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-08", "Golden Jubilee"),
            ("2022-02-03", "Big Day"),
            ("2022-02-11", "Nukufetau Day"),
            ("2022-02-16", "Day of the Flood"),
            ("2022-04-15", "Good Friday; Nanumaga Day"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-04-18", "Easter Monday; Holy Saturday (observed)"),
            ("2022-04-23", "The Day of the Bombing"),
            ("2022-05-09", "Gospel Day"),
            ("2022-05-10", "Gospel Day"),
            ("2022-06-11", "Queen's Birthday"),
            ("2022-08-01", "National Youth Day"),
            ("2022-09-17", "Niutao Day"),
            ("2022-10-01", "Tuvalu Day"),
            ("2022-10-02", "Tuvalu Day"),
            ("2022-10-03", "Tuvalu Day (observed)"),
            ("2022-10-04", "Tuvalu Day (observed)"),
            ("2022-10-10", "National Children's Day"),
            ("2022-10-21", "Cyclone Day"),
            ("2022-11-14", "Heir to the Throne's Birthday"),
            ("2022-11-25", "Happy Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
