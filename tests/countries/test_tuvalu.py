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

from holidays.countries.tuvalu import Tuvalu
from tests.common import CommonCountryTests


class TestTuvalu(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Tuvalu)

    def test_new_years(self):
        name = "Tausaga Fou"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (fakamatakuga)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_commonwealth_day(self):
        name = "Aso Atefenua"
        self.assertHolidayName(
            name,
            "2015-03-09",
            "2016-03-14",
            "2017-03-13",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
        )
        self.assertHolidayName(name, range(self.start_year, 2021))
        self.assertNoHolidayName(name, range(2021, self.end_year))

    def test_good_friday(self):
        name = "Aso toe tu"
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

    def test_easter_monday(self):
        name = "Toe Tu aso gafua"
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

    def test_gospel_day(self):
        name = "Te Aso o te Tala Lei"
        self.assertHolidayName(
            name,
            "2020-05-11",
            "2021-05-10",
            "2022-05-09",
            "2023-05-15",
            "2024-05-13",
            "2025-05-12",
        )
        self.assertHolidayName(name, self.full_range)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NKL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-10" for year in self.full_range)
                )

    def test_king_birthday(self):
        name = "Asofanau Tupu"
        self.assertHolidayName(
            name,
            "2023-06-10",
            "2024-06-08",
            "2025-06-14",
            "2026-06-13",
            "2027-06-12",
            "2028-06-10",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_queen_birthday(self):
        name = "Asofanau Fafine"
        self.assertHolidayName(
            name,
            "2017-06-10",
            "2018-06-09",
            "2019-06-08",
            "2020-06-13",
            "2021-06-12",
            "2022-06-11",
        )
        self.assertHolidayName(name, range(self.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, self.end_year))

    def test_national_children_day(self):
        name = "Aso Tamaliki"
        self.assertHolidayName(
            name,
            "2013-08-05",
            "2014-08-04",
            "2015-08-03",
            "2016-08-01",
            "2017-08-07",
            "2018-08-06",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_youth_day(self):
        name = "Aso tupulaga"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, range(2019, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2019))

    def test_tuvalu_day(self):
        name = "Tutokotasi"
        self.assertHolidayName(name, (f"{year}-10-01" for year in self.full_range))
        self.assertHolidayName(name, (f"{year}-10-02" for year in self.full_range))
        obs_dts = (
            "2016-10-03",
            "2016-10-04",
            "2017-10-03",
            "2021-10-04",
            "2022-10-03",
            "2022-10-04",
            "2023-10-03",
        )
        self.assertHolidayName(f"{name} (fakamatakuga)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_heir_to_the_throne_birthday(self):
        name = "Aso fanau o te sui ote Tupu"
        self.assertHolidayName(
            name,
            "2017-11-13",
            "2018-11-12",
            "2019-11-11",
            "2020-11-09",
            "2021-11-08",
            "2022-11-14",
        )
        self.assertHolidayName(name, range(self.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, self.end_year))

    def test_christmas_day(self):
        name = "Kilisimasi"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (fakamatakuga)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Aso Faipele"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (fakamatakuga)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_the_day_of_the_bombing(self):
        name = "Te Aso o te Paula"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "FUN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-23" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_cyclone_day(self):
        name = "Aso o te matagi"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "FUN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-21" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_niutao_day(self):
        name = "Te Aso o te Setema"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NIT":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-17" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_nukufetau_day(self):
        name = "Te Aso O Tutasi"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NKF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-11" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_golden_jubilee(self):
        name = "Te Po o Tefolaha"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NMA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-08" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_big_day(self):
        name = "Po Lahi"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NMA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-03" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_nanumaga_day(self):
        name = "Aho o te Fakavae"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NMG":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_day_of_the_flood(self):
        name = "Bogin te Ieka"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NUI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_happy_day(self):
        name = "Te Aso Fiafia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "VAI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-25" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_all_holidays(self):
        holidays_found = set()
        for subdiv in Tuvalu.subdivisions:
            holidays_found.update(
                Tuvalu(
                    subdiv=subdiv, observed=False, years=(1990, 2007, 2012, 2015, 2023)
                ).values()
            )
        all_holidays = {
            "Aho o te Fakavae",
            "Aso Atefenua",
            "Aso Faipele",
            "Aso fanau o te sui ote Tupu",
            "Aso o te matagi",
            "Aso Tamaliki",
            "Aso toe tu",
            "Aso tupulaga",
            "Asofanau Fafine",
            "Asofanau Tupu",
            "Bogin te Ieka",
            "Kilisimasi",
            "Po Lahi",
            "Tausaga Fou",
            "Te Aso Fiafia",
            "Te Aso o te Paula",
            "Te Aso o te Setema",
            "Te Aso o te Tala Lei",
            "Te Aso O Tutasi",
            "Te Po o Tefolaha",
            "Toe Tu aso gafua",
            "Tutokotasi",
        }
        self.assertEqual(all_holidays, holidays_found)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tausaga Fou"),
            ("2022-01-03", "Tausaga Fou (fakamatakuga)"),
            ("2022-01-08", "Te Po o Tefolaha"),
            ("2022-02-03", "Po Lahi"),
            ("2022-02-11", "Te Aso O Tutasi"),
            ("2022-02-16", "Bogin te Ieka"),
            ("2022-04-15", "Aho o te Fakavae; Aso toe tu"),
            ("2022-04-18", "Toe Tu aso gafua"),
            ("2022-04-23", "Te Aso o te Paula"),
            ("2022-05-09", "Te Aso o te Tala Lei"),
            ("2022-05-10", "Te Aso o te Tala Lei"),
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
            ("2022-04-18", "Easter Monday"),
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
            ("2022-04-18", "Easter Monday"),
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
