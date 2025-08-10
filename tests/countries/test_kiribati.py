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

from holidays.countries.kiribati import Kiribati, KI, KIR
from tests.common import CommonCountryTests


class TestKiribati(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1980, 2050)
        super().setUpClass(Kiribati, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Kiribati, KI, KIR)

    def test_no_holidays(self):
        self.assertNoHolidays(Kiribati(years=1979))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1980, 2050)))
        obs_dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_womens_day(self):
        name = "International Women's Day"
        self.assertNoHolidayName(name, range(1980, 2003))
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(2003, 2050)))
        dt = ("2015-03-09", "2020-03-09")
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
        self.assertHolidayName(name, range(1980, 2050))

    def test_holy_saturday(self):
        name = "Holy Saturday"
        self.assertHolidayName(
            name,
            "1999-04-03",
            "2000-04-22",
            "2001-04-14",
            "2002-03-30",
        )
        self.assertHolidayName(name, range(1980, 2003))
        self.assertNoHolidayName(name, range(2003, 2050))

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
        self.assertHolidayName(name, range(1980, 2050))

    def test_national_health_day(self):
        name = "National Health Day"
        self.assertHolidayName(name, (f"{year}-04-19" for year in range(2003, 2050)))
        dt = ("2015-04-20", "2020-04-20")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoHolidayName(name, range(1980, 2003))
        self.assertNoNonObservedHoliday(dt)

    def test_public_holiday_may_9(self):
        name = "Public Holiday"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1993, 2003)))
        # Observed when falling on weekend.
        dt = ("1993-05-10", "1999-05-10")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(
            name, (f"{year}-05-09" for year in (*range(1980, 1993), *range(2003, 2050)))
        )
    def test_gospel_day(self):
        name = "Gospel Day"
        self.assertHolidayName(name, (f"{year}-07-11" for year in range(2002, 2050)))
        dt = ("2021-07-12", "2027-07-12")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoHolidayName(name, range(1980, 2002))

    def test_national_day_anniversary(self):
        name = "National Day - Independence Anniversary"
        self.assertHolidayName(name, (f"{year}-07-12" for year in range(1993, 2050)))
        dt = ("2020-07-13", "2026-07-13")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoHolidayName(name, range(1980, 1993))
        self.assertNoNonObservedHoliday(dt)

    def test_national_day_unimwane(self):
        name = "National Day (in honor of Unimwane)"
        self.assertHolidayName(name, (f"{year}-07-15" for year in range(2002, 2050)))
        dt = (
            "2018-07-16",
            "2029-07-16",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoHolidayName(name, range(1980, 2002))

    def test_national_day_unaine(self):
        name = "National Day (in honor of Unaine)"
        self.assertHolidayName(name, (f"{year}-07-16" for year in range(2002, 2050)))
        dt = ("2017-07-17", "2023-07-17")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoHolidayName(name, range(1980, 2002))

    def test_public_holiday_1st_mon_of_aug(self):
        name = "Public Holiday"
        self.assertHolidayName(
            name,
            "1999-08-02",
            "2000-08-07",
            "2001-08-06",
            "2002-08-05",
        )
        self.assertHolidayName(name, range(1980, 2003))

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-08-05" for year in range(2003, 2050)))
        self.assertNoHolidayName(name, range(1980, 2003))

    def test_public_holiday_nov_10(self):
        name = "Public Holiday"
        self.assertHolidayName(name, (f"{year}-11-10" for year in range(1980, 1993)))
        # Observed when falling on weekend.
        dt = ("1991-11-11",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name, (f"{year}-11-10" for year in range(1993, 2050)))
    def test_human_rights_peace_day(self):
        name = "Human Rights and Peace Day"
        self.assertHolidayName(name, (f"{year}-12-10" for year in range(1993, 2003)))
        self.assertHolidayName(name, (f"{year}-12-09" for year in range(2003, 2050)))
        dt = ("1995-12-11", "2000-12-11", "2006-12-11", "2012-12-10", "2017-12-11", "2023-12-11")
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoHolidayName(name, range(1980, 1993))
        self.assertNoHolidayName(name, (f"{year}-12-09" for year in range(1993, 2003)))
        self.assertNoHolidayName(name, (f"{year}-12-10" for year in range(2003, 2050)))
        self.assertNoNonObservedHoliday(dt)

    def test_christmas(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1980, 2050)))
        dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1980, 2050)))
        dt = (
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2025(self):
        self.assertHolidays(
            Kiribati(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-10", "International Women's Day (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "National Health Day"),
            ("2025-04-21", "Easter Monday; National Health Day (observed)"),
            ("2025-07-11", "Gospel Day"),
            ("2025-07-12", "National Day - Independence Anniversary"),
            ("2025-07-14", "National Day - Independence Anniversary (observed)"),
            ("2025-07-15", "National Day (in honor of Unimwane)"),
            ("2025-07-16", "National Day (in honor of Unaine)"),
            ("2025-08-05", "Youth Day"),
            ("2025-12-09", "Human Rights and Peace Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
