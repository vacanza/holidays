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

from holidays.countries.malaysia import Malaysia, MY, MYS
from tests.common import CommonCountryTests


class TestMalaysia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Malaysia, years=range(1952, 2050))
        cls.subdiv_holidays = {
            subdiv: Malaysia(subdiv=subdiv, years=range(2000, 2025))
            for subdiv in Malaysia.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(Malaysia, MY, MYS)

    def test_no_holidays(self):
        self.assertNoHolidays(Malaysia(years=1951))

    def test_2023(self):
        rows = (
            ("2023-01-01", (0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1)),
            ("2023-01-02", (0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1)),
            ("2023-01-14", (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-01-22", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-01-23", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-01-24", (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1)),
            ("2023-02-01", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1)),
            ("2023-02-05", (1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1)),
            ("2023-02-06", (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1)),
            ("2023-02-18", (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-02-19", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-03-04", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-03-05", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-03-23", (1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-04-07", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0)),
            ("2023-04-08", (0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1)),
            ("2023-04-09", (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-04-15", (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-04-21", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-04-22", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-04-23", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-04-24", (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-04-26", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-05-01", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-05-04", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-05-17", (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-05-22", (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-05-30", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0)),
            ("2023-05-31", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0)),
            ("2023-06-01", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)),
            ("2023-06-02", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)),
            ("2023-06-05", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-06-18", (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-06-28", (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-06-29", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-06-30", (0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-07-02", (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-07-07", (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-07-08", (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-07-19", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-07-22", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)),
            ("2023-07-30", (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-07-31", (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-08-23", (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-08-24", (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-08-31", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-09-16", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-09-17", (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)),
            ("2023-09-28", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
            ("2023-09-29", (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-09-30", (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-10-07", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)),
            ("2023-10-14", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)),
            ("2023-11-03", (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)),
            ("2023-11-12", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1)),
            ("2023-11-13", (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1)),
            ("2023-12-11", (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)),
            ("2023-12-24", (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)),
            ("2023-12-25", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
        )

        for col, subdiv in enumerate(Malaysia.subdivisions):
            state_holidays = self.subdiv_holidays[subdiv]
            for dt, is_holiday in rows:
                self.assertEqual(dt in state_holidays, is_holiday[col])

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-11-29",
            "2017-04-24",
            "2017-09-04",
            "2018-05-09",
            "2019-07-30",
            "2022-11-18",
            "2022-11-19",
            "2022-11-28",
            "2023-04-21",
        )

    def test_special_subdiv_holidays(self):
        for subdiv in ("14", "15", "16"):
            self.assertHoliday(self.subdiv_holidays[subdiv], "2021-12-03")

        self.assertHoliday(self.subdiv_holidays["13"], "2018-05-17", "2018-05-18")

        for subdiv in ("01", "02", "03", "11"):
            self.assertHoliday(self.subdiv_holidays[subdiv], "2022-05-04")
            self.assertNoNonObservedHoliday(Malaysia(subdiv=subdiv, observed=False), "2022-05-04")

        for subdiv in ("04", "05", "06", "07", "08", "09", "10", "11", "12", "14", "15", "16"):
            self.assertHoliday(self.subdiv_holidays[subdiv], "2007-01-02")
            self.assertNoNonObservedHoliday(Malaysia(subdiv=subdiv, observed=False), "2007-01-02")

    def test_new_years_day(self):
        name = "Tahun Baharu"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"04", "05", "06", "07", "08", "10", "12", "13", "14", "15", "16"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-01" for year in range(2000, 2025))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_federal_territory_day(self):
        name = "Hari Wilayah Persekutuan"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"14", "15", "16"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-01" for year in range(2000, 2025))
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1973))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_labor_day(self):
        name = "Hari Pekerja"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1973, 2050)))
        self.assertNoHolidayName(name, range(1952, 1973))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"12", "13"}:
                self.assertHolidayName(
                    name,
                    holidays,
                    "2012-04-06",
                    "2013-03-29",
                    "2014-04-18",
                    "2015-04-03",
                    "2016-03-25",
                    "2017-04-14",
                    "2018-03-30",
                    "2019-04-19",
                    "2020-04-10",
                    "2021-04-02",
                    "2022-04-15",
                    "2023-04-07",
                    "2024-03-29",
                )
                self.assertHolidayName(name, holidays, range(2000, 2025))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pesta_kaamatan(self):
        name = "Pesta Kaamatan"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"12", "15"}:
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-05-30" for year in range(2000, 2025)),
                    (f"{year}-05-31" for year in range(2000, 2025)),
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_yang_di_pertuan_agong_birthday(self):
        name = "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"
        self.assertHolidayName(
            name,
            "2012-06-02",
            "2013-06-01",
            "2014-06-07",
            "2015-06-06",
            "2016-06-04",
            "2017-09-09",
            "2018-09-09",
            "2019-09-09",
            "2020-06-08",
            "2021-06-07",
            "2022-06-06",
            "2023-06-05",
            "2024-06-03",
        )
        self.assertHolidayName(name, range(1952, 2050))

    def test_malaysia_day(self):
        name = "Hari Malaysia"
        self.assertHolidayName(name, (f"{year}-09-16" for year in range(2010, 2050)))
        self.assertNoHolidayName(name, range(1952, 2010))

    def test_deepavali(self):
        name = "Hari Deepavali"
        self.assertNoHolidayName(name)
        dt = (
            "2014-10-22",
            "2015-11-10",
            "2016-10-29",
            "2017-10-18",
            "2018-11-06",
            "2019-10-27",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "13":
                self.assertNoHolidayName(name, holidays)
            elif subdiv == "15":
                self.assertHolidayName(name, holidays, dt)
                self.assertNoHolidayName(name, holidays, range(2000, 2014))
            else:
                self.assertHolidayName(name, holidays, dt)

    def test_thaipusam(self):
        name = "Hari Thaipusam"
        self.assertNoHolidayName(name)
        dt = (
            "2012-01-08",
            "2013-02-25",
            "2014-02-14",
            "2015-03-05",
            "2016-02-23",
            "2017-01-13",
            "2018-01-31",
            "2019-01-21",
            "2020-02-08",
            "2021-01-28",
            "2022-01-18",
            "2023-02-05",
            "2024-01-25",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"01", "05", "07", "08", "10", "14", "16"}:
                self.assertHolidayName(name, holidays, dt)
                self.assertHolidayName(name, holidays, range(2000, 2025))
            elif subdiv == "02":
                self.assertHolidayName(name, holidays, "2022-01-18", "2023-02-05", "2024-01-25")
                self.assertNoHolidayName(name, holidays, range(2000, 2022))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_islamic_new_year(self):
        name = "Awal Muharam"
        self.assertHolidayName(
            name,
            "2012-11-15",
            "2013-11-05",
            "2014-10-25",
            "2015-10-14",
            "2016-10-02",
            "2017-09-22",
            "2018-09-11",
            "2019-09-01",
            "2020-08-20",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
        )
        self.assertNoHolidayName(name, range(1952, 1995))

    def test_prophets_birthday(self):
        name = "Hari Keputeraan Nabi Muhammad S.A.W."
        self.assertHolidayName(
            name,
            "2012-02-05",
            "2013-01-24",
            "2014-01-14",
            "2015-01-03",
            "2015-12-24",
            "2016-12-12",
            "2017-12-01",
            "2018-11-20",
            "2019-11-09",
            "2020-10-29",
            "2021-10-19",
            "2022-10-10",
            "2023-09-28",
            "2024-09-16",
        )

    def test_eid_al_fitr(self):
        name = "Hari Raya Puasa"
        self.assertHolidayName(
            name,
            "2012-08-19",
            "2013-08-08",
            "2014-07-28",
            "2015-07-17",
            "2016-07-06",
            "2017-06-25",
            "2018-06-15",
            "2019-06-05",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
        )

    def test_eid_al_fitr_second_day(self):
        name = "Hari Raya Puasa (Hari Kedua)"
        self.assertHolidayName(
            name,
            "2012-08-20",
            "2013-08-09",
            "2014-07-29",
            "2015-07-18",
            "2016-07-07",
            "2017-06-26",
            "2018-06-16",
            "2019-06-06",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-23",
            "2024-04-11",
        )

    def test_eid_al_adha(self):
        name = "Hari Raya Qurban"
        self.assertHolidayName(
            name,
            "2012-10-26",
            "2013-10-15",
            "2014-10-05",
            "2015-09-24",
            "2016-09-12",
            "2017-09-01",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
        )

    def test_isra_and_miraj(self):
        name = "Israk dan Mikraj"
        self.assertNoHolidayName(name)
        dt = (
            "2012-06-17",
            "2013-06-06",
            "2014-05-27",
            "2015-05-16",
            "2016-05-05",
            "2017-04-24",
            "2018-04-14",
            "2019-04-03",
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-02-08",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"02", "05", "09"}:
                self.assertHolidayName(name, holidays, dt)
            elif subdiv == "11":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-03-22",
                    "2021-03-11",
                    "2022-03-01",
                    "2023-02-18",
                    "2024-02-08",
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2020))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_beginning_of_ramadan(self):
        name = "Awal Ramadan"
        self.assertNoHolidayName(name)
        dt = (
            "2012-07-20",
            "2013-07-09",
            "2014-06-29",
            "2015-06-18",
            "2016-06-07",
            "2017-05-27",
            "2018-05-17",
            "2019-05-06",
            "2020-04-24",
            "2021-04-13",
            "2022-04-03",
            "2023-03-23",
            "2024-03-12",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"01", "02", "04"}:
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_nuzul_al_quran_day(self):
        name = "Hari Nuzul Al-Quran"
        self.assertNoHolidayName(name)
        dt = (
            "2012-08-05",
            "2013-07-25",
            "2014-07-15",
            "2015-07-04",
            "2016-06-22",
            "2017-06-12",
            "2018-06-02",
            "2019-05-22",
            "2020-05-10",
            "2021-04-29",
            "2022-04-19",
            "2023-04-08",
            "2024-03-28",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"03", "06", "07", "08", "09", "10", "11", "14", "15", "16"}:
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_arafat_day(self):
        name = "Hari Arafah"
        self.assertNoHolidayName(name)
        dt = (
            "2012-10-25",
            "2013-10-14",
            "2014-10-04",
            "2015-09-23",
            "2016-09-11",
            "2017-08-31",
            "2018-08-21",
            "2019-08-10",
            "2020-07-30",
            "2021-07-19",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "11":
                self.assertHolidayName(name, holidays, dt)
            elif subdiv == "03":
                self.assertHolidayName(name, holidays, "2023-06-28", "2024-06-16")
                self.assertNoHolidayName(name, holidays, range(2000, 2023))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_eid_al_adha_second_day(self):
        name = "Hari Raya Qurban (Hari Kedua)"
        self.assertNoHolidayName(name)
        dt = (
            "2012-10-27",
            "2013-10-16",
            "2014-10-06",
            "2015-09-25",
            "2016-09-13",
            "2017-09-02",
            "2018-08-23",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-11",
            "2023-06-30",
            "2024-06-18",
        )

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"02", "03", "09", "11"}:
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_observed(self):
        dt = (
            "2012-02-06",
            "2012-08-21",
            "2012-09-17",
            "2013-02-12",
            "2014-09-01",
            "2014-10-06",
            "2015-05-04",
            "2016-05-02",
            "2016-12-26",
            "2017-01-30",
            "2017-06-27",
            "2018-09-10",
            "2018-09-17",
            "2019-05-20",
            "2019-08-12",
            "2020-01-27",
            "2020-05-26",
            "2022-05-04",
            "2022-05-16",
            "2022-07-11",
            "2022-12-26",
            "2023-01-24",
            "2023-04-24",
            "2024-02-12",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_birthday_of_sultan_of_johor(self):
        name = "Hari Keputeraan Sultan Johor"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "01":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-23" for year in range(2015, 2025))
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2015))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sultan_of_johor_hol(self):
        name = "Hari Hol Almarhum Sultan Iskandar"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "01":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2011-01-12",
                    "2012-12-20",
                    "2013-12-10",
                    "2014-11-29",
                    "2015-11-19",
                    "2016-11-07",
                    "2017-10-27",
                    "2018-10-15",
                    "2019-10-05",
                    "2020-09-24",
                    "2021-09-13",
                    "2022-09-03",
                    "2023-08-23",
                    "2024-08-11",
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2011))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_kedah(self):
        name = "Hari Keputeraan Sultan Kedah"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "02":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2018-06-17",
                    "2019-06-16",
                    "2020-06-21",
                    "2021-06-20",
                    "2022-06-19",
                    "2023-06-18",
                    "2024-06-30",
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2018))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_kelantan(self):
        name = "Hari Keputeraan Sultan Kelantan"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "03":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-03-30" for year in range(2010, 2012)),
                    (f"{year}-03-31" for year in range(2010, 2012)),
                )
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-11-11" for year in range(2012, 2023)),
                    (f"{year}-11-12" for year in range(2012, 2023)),
                )
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-09-29" for year in range(2023, 2025)),
                    (f"{year}-09-30" for year in range(2023, 2025)),
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2010))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_malacca_declaration_of_independence_day(self):
        name = "Hari Pengisytiharan Tarikh Kemerdekaan"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "04":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-20" for year in range(2024, 2025))
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2024))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_declaration_malacca_as_historical_city(self):
        name = "Hari Perisytiharan Melaka Sebagai Bandaraya Bersejarah"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "04":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in range(2000, 2024))
                )
                self.assertNoHolidayName(name, holidays, range(2024, 2025))
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1988))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_governor_of_malacca(self):
        name = "Hari Jadi Yang di-Pertua Negeri Melaka"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "04":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-24" for year in range(2020, 2025))
                )
                self.assertHolidayName(
                    name,
                    holidays,
                    "2012-10-12",
                    "2013-10-11",
                    "2014-10-10",
                    "2015-10-09",
                    "2016-10-14",
                    "2017-10-13",
                    "2018-10-12",
                    "2019-10-11",
                )
                self.assertHolidayName(name, holidays, range(2000, 2025))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_negeri_sembilan(self):
        name = "Hari Keputeraan Yang di-Pertuan Besar Negeri Sembilan"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "05":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-14" for year in range(2009, 2025))
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2009))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sultan_of_pahang_hol(self):
        name = "Hari Hol Sultan Pahang"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "06":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-05-22" for year in range(2020, 2025)),
                    (f"{year}-05-07" for year in range(2000, 2020)),
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1974))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_pahang(self):
        name = "Hari Keputeraan Sultan Pahang"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "06":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-07-30" for year in range(2019, 2025)),
                    (f"{year}-10-24" for year in range(2000, 2019)),
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1974))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_george_town_heritage_day(self):
        name = "Hari Ulang Tahun Perisytiharan Tapak Warisan Dunia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "07":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-07" for year in range(2009, 2025))
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2009))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_governor_of_penang(self):
        name = "Hari Jadi Yang di-Pertua Negeri Pulau Pinang"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "07":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2012-07-14",
                    "2013-07-13",
                    "2014-07-12",
                    "2015-07-11",
                    "2016-07-09",
                    "2017-07-08",
                    "2018-07-14",
                    "2019-07-13",
                    "2020-07-11",
                    "2021-07-10",
                    "2022-07-09",
                    "2023-07-08",
                    "2024-07-13",
                )
                self.assertHolidayName(name, holidays, range(2000, 2025))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_perak(self):
        name = "Hari Keputeraan Sultan Perak"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "08":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-27" for year in range(2000, 2018))
                )
                self.assertHolidayName(
                    name,
                    holidays,
                    "2018-11-02",
                    "2019-11-01",
                    "2020-11-06",
                    "2021-11-05",
                    "2022-11-04",
                    "2023-11-03",
                    "2024-11-01",
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_raja_of_perlis(self):
        name = "Hari Ulang Tahun Keputeraan Raja Perlis"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "09":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-05-17" for year in range(2000, 2018)),
                    (f"{year}-05-17" for year in range(2022, 2025)),
                    (f"{year}-07-17" for year in range(2018, 2022)),
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1999))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_selangor(self):
        name = "Hari Keputeraan Sultan Selangor"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "10":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-11" for year in range(2000, 2025))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_installation_of_sultan_of_terengganu(self):
        name = "Hari Ulang Tahun Pertabalan Sultan Terengganu"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "11":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-04" for year in range(2000, 2025))
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1999))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_sultan_of_terengganu(self):
        name = "Hari Keputeraan Sultan Terengganu"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "11":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-26" for year in range(2000, 2025))
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1999))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_governor_of_sabah(self):
        name = "Hari Jadi Yang di-Pertua Negeri Sabah"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "12":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2012-10-06",
                    "2013-10-05",
                    "2014-10-04",
                    "2015-10-03",
                    "2016-10-01",
                    "2017-10-07",
                    "2018-10-06",
                    "2019-10-05",
                    "2020-10-03",
                    "2021-10-02",
                    "2022-10-01",
                    "2023-10-07",
                    "2024-10-05",
                )
                self.assertHolidayName(name, holidays, range(2000, 2025))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_christmas_eve(self):
        name = "Christmas Eve"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "12":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-24" for year in range(2019, 2025))
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2019))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_dayak_festival_day(self):
        name = "Perayaan Hari Gawai Dayak"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "13":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-06-01" for year in range(2000, 2025)),
                    (f"{year}-06-02" for year in range(2000, 2025)),
                )
                self.assertNoHolidayName(name, Malaysia(subdiv=subdiv, years=1964))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_governor_of_sarawak(self):
        name = "Hari Jadi Yang di-Pertua Negeri Sarawak"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "13":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2012-10-13",
                    "2013-10-12",
                    "2014-10-11",
                    "2015-10-10",
                    "2016-10-08",
                    "2017-10-14",
                    "2018-10-13",
                    "2019-10-12",
                    "2020-10-10",
                    "2021-10-09",
                    "2022-10-08",
                    "2023-10-14",
                    "2024-10-12",
                )
                self.assertHolidayName(name, holidays, range(2000, 2025))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sarawak_independence_day(self):
        name = "Hari Kemerdekaan Sarawak"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "13":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-22" for year in range(2017, 2025))
                )
                self.assertNoHolidayName(name, holidays, range(2000, 2017))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_2024(self):
        self.assertHolidays(
            Malaysia(years=2024),
            ("2024-02-10", "Tahun Baharu Cina"),
            ("2024-02-11", "Tahun Baharu Cina (Hari Kedua)"),
            ("2024-02-12", "Cuti Tahun Baharu Cina (Hari Kedua)"),
            ("2024-04-10", "Hari Raya Puasa"),
            ("2024-04-11", "Hari Raya Puasa (Hari Kedua)"),
            ("2024-05-01", "Hari Pekerja"),
            ("2024-05-22", "Hari Wesak"),
            ("2024-06-03", "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"),
            ("2024-06-17", "Hari Raya Qurban"),
            ("2024-07-07", "Awal Muharam"),
            ("2024-08-31", "Hari Kebangsaan"),
            ("2024-09-16", "Hari Keputeraan Nabi Muhammad S.A.W.; Hari Malaysia"),
            ("2024-12-25", "Hari Krismas"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-22", "Tahun Baharu Cina"),
            ("2023-01-23", "Tahun Baharu Cina (Hari Kedua)"),
            ("2023-01-24", "Cuti Tahun Baharu Cina"),
            ("2023-04-21", "Hari Raya Puasa (pergantian hari)"),
            ("2023-04-22", "Hari Raya Puasa"),
            ("2023-04-23", "Hari Raya Puasa (Hari Kedua)"),
            ("2023-04-24", "Cuti Hari Raya Puasa (Hari Kedua)"),
            ("2023-05-01", "Hari Pekerja"),
            ("2023-05-04", "Hari Wesak"),
            ("2023-06-05", "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"),
            ("2023-06-29", "Hari Raya Qurban"),
            ("2023-07-19", "Awal Muharam"),
            ("2023-08-31", "Hari Kebangsaan"),
            ("2023-09-16", "Hari Malaysia"),
            ("2023-09-28", "Hari Keputeraan Nabi Muhammad S.A.W."),
            ("2023-12-25", "Hari Krismas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-22", "Chinese New Year"),
            ("2023-01-23", "Chinese New Year (Second Day)"),
            ("2023-01-24", "Chinese New Year (observed)"),
            ("2023-04-21", "Eid al-Fitr (additional holiday)"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr (Second Day)"),
            ("2023-04-24", "Eid al-Fitr (Second Day) (observed)"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-04", "Vesak Day"),
            ("2023-06-05", "Birthday of HM Yang di-Pertuan Agong"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-08-31", "National Day"),
            ("2023-09-16", "Malaysia Day"),
            ("2023-09-28", "Prophet Muhammad's Birthday"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2023-01-22", "วันตรุษจีน"),
            ("2023-01-23", "วันตรุษจีนวันที่สอง"),
            ("2023-01-24", "ชดเชยวันตรุษจีน"),
            ("2023-04-21", "วันอีฎิ้ลฟิตริ (เพิ่มเติม)"),
            ("2023-04-22", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-23", "วันอีฎิ้ลฟิตริวันที่สอง"),
            ("2023-04-24", "ชดเชยวันอีฎิ้ลฟิตริวันที่สอง"),
            ("2023-05-01", "วันแรงงาน"),
            ("2023-05-04", "วันวิสาขบูชา"),
            ("2023-06-05", "วันคล้ายวันพระราชสมภพสมเด็จพระราชาธิบดีแห่งมาเลเซีย"),
            ("2023-06-29", "วันอีดิ้ลอัฎฮา"),
            ("2023-07-19", "วันขึ้นปีใหม่อิสลาม"),
            ("2023-08-31", "วันชาติมาเลเซีย"),
            ("2023-09-16", "วันเฉลิมฉลองการจัดตั้งสหพันธรัฐมาเลเซีย"),
            ("2023-09-28", "วันเมาลิดนบี"),
            ("2023-12-25", "วันคริสต์มาส"),
        )
