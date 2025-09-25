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

from holidays.countries.antigua_and_barbuda import AntiguaAndBarbuda, AG, ATG
from tests.common import CommonCountryTests


class TestAntiguaAndBarbuda(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AntiguaAndBarbuda)

    def test_country_aliases(self):
        self.assertAliases(AntiguaAndBarbuda, AG, ATG)

    def test_no_holidays(self):
        self.assertNoHolidays(AntiguaAndBarbuda(years=self.start_year - 1))

    def test_special_holidays(self):
        name_day_after_general_election = "Day after the General Election"
        for dt, name in (
            ("1993-08-03", "Public Holiday"),
            ("2008-02-19", "State Funeral of the late The Honourable Charlesworth T. Samuel"),
            ("2008-03-18", "State Funeral of the late The Honourable Sir George Herbert Walter"),
            ("2018-03-22", name_day_after_general_election),
            ("2023-01-19", name_day_after_general_election),
        ):
            self.assertHolidayName(name, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        dt = (
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(
            name,
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_caribbean_community_day(self):
        name = "Caribbean Community (Caricom) Day"
        self.assertHolidayName(
            name,
            "1995-07-03",
            "2000-07-03",
            "2004-07-05",
            "2005-07-04",
        )
        self.assertHolidayName(name, range(self.start_year, 2006))
        self.assertNoHolidayName(name, range(2006, self.end_year))

    def test_carnival_monday(self):
        name = "Carnival Monday"
        self.assertHolidayName(
            name,
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_carnival_tuesday(self):
        name = "Carnival Tuesday"
        self.assertHolidayName(
            name,
            "2021-08-03",
            "2022-08-02",
            "2023-08-08",
            "2024-08-06",
            "2025-08-05",
        )
        self.assertHolidayName(name, range(2006, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2006))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-11-01" for year in self.full_range))
        dt = (
            "2008-11-03",
            "2009-11-02",
            "2014-11-03",
            "2015-11-02",
            "2020-11-02",
            "2025-11-03",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_heroes_and_sir_vere_cornwall_bird_snr_day(self):
        name_2005 = "National Heroes Day"
        name_2014 = "Sir Vere Cornwall Bird Snr. Day"
        self.assertHolidayName(
            name_2005,
            "2005-12-09",
            "2006-12-11",
            "2007-12-09",
            "2008-12-09",
            "2009-12-09",
            "2010-12-09",
            "2011-12-09",
            "2012-12-10",
            "2013-12-09",
        )
        self.assertHolidayName(name_2014, (f"{year}-12-09" for year in range(2014, self.end_year)))
        self.assertNoHolidayName(
            name_2005, range(self.start_year, 2005), range(2014, self.end_year)
        )
        self.assertNoHolidayName(name_2014, range(self.start_year, 2014))

        dt = ("2023-12-11",)
        self.assertHolidayName(f"{name_2014} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        dt = (
            "2004-12-28",
            "2010-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2025(self):
        self.assertHolidays(
            AntiguaAndBarbuda(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-05", "Labour Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-08-04", "Carnival Monday"),
            ("2025-08-05", "Carnival Tuesday"),
            ("2025-11-01", "Independence Day"),
            ("2025-11-03", "Independence Day (observed)"),
            ("2025-12-09", "Sir Vere Cornwall Bird Snr. Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
