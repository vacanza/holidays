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

from holidays.constants import HALF_DAY
from holidays.financial.nasdaq import NASDAQ
from tests.common import CommonFinancialTests


class TestNASDAQ(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NASDAQ)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(NASDAQ(categories=HALF_DAY, years=range(1800, self.start_year)))

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1993-12-31",
            "1999-12-31",
            "2004-12-31",
            "2010-12-31",
            "2021-12-31",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_martin_luther_king_jr_day(self):
        name = "Martin Luther King Jr. Day"
        self.assertHolidayName(
            name,
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
            "2024-01-15",
            "2025-01-20",
        )
        self.assertHolidayName(name, range(1998, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1998))

    def test_washingtons_birthday(self):
        name = "Washington's Birthday"
        self.assertHolidayName(
            name,
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHolidayName(name, range(self.start_year, self.end_year))

    def test_good_friday(self):
        name = "Good Friday"
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

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertHolidayName(
            name,
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHolidayName(name, range(self.start_year, self.end_year))

    def test_juneteenth_national_independence_day(self):
        name = "Juneteenth National Independence Day"
        self.assertNonObservedHolidayName(
            name, (f"{year}-06-19" for year in range(2022, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        obs_dts = (
            "2022-06-20",
            "2027-06-18",
            "2032-06-18",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-07-04" for year in self.full_range))
        obs_dts = (
            "2015-07-03",
            "2020-07-03",
            "2021-07-05",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Labor Day"
        self.assertHolidayName(
            name,
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_columbus_day(self):
        name = "Columbus Day"
        self.assertNoHolidayName(name, range(self.start_year, self.end_year))

    def test_election_day(self):
        name = "Election Day"
        self.assertHolidayName(
            name,
            "1972-11-07",
            "1976-11-02",
            "1980-11-04",
        )
        self.assertNoHolidayName(
            name,
            range(self.start_year, 1972),
            range(1973, 1976),
            range(1977, 1980),
            range(1981, self.end_year),
        )

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
            "2024-11-28",
            "2025-11-27",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_special_public_holidays(self):
        # NOTE: update the list whenever new historical holidays are added.
        special_holidays = [
            "1972-12-28",  # Funeral of former President Harry S. Truman.
            "1973-01-25",  # Funeral of former President Lyndon B. Johnson.
            "1977-07-14",  # Blackout in New York City.
            "1985-09-27",  # Hurricane Gloria.
            "1994-04-27",  # Funeral of former President Richard M. Nixon.
            "2001-09-11",  # Closed following Attacks on the World Trade Center.
            "2001-09-12",  # Closed following Attacks on the World Trade Center.
            "2001-09-13",  # Closed following Attacks on the World Trade Center.
            "2001-09-14",  # Closed following Attacks on the World Trade Center.
            "2004-06-11",  # National Day of Mourning for former President Ronald Reagan.
            "2007-01-02",  # National Day of Mourning for former President Gerald R. Ford.
            "2012-10-29",  # Hurricane Sandy.
            "2012-10-30",  # Hurricane Sandy.
            "2018-12-05",  # National Day of Mourning for former President George H. W. Bush.
            "2025-01-09",  # National Day of Mourning for former President Jimmy Carter.
        ]
        self.assertHoliday(special_holidays)

    def test_day_before_independence_day(self):
        name = "Day before Independence Day (markets close at 1:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1995-07-03",
            "1997-07-03",
            "2000-07-03",
            "2001-07-03",
            "2003-07-03",
            "2006-07-03",
            "2007-07-03",
            "2008-07-03",
            "2012-07-03",
            "2014-07-03",
            "2017-07-03",
            "2018-07-03",
            "2023-07-03",
            "2025-07-03",
        )
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 1993), 1996, 2002)

    def test_day_after_thanksgiving(self):
        name = "Day after Thanksgiving Day (markets close at 1:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-29",
            "2025-11-28",
        )
        self.assertHalfDayHolidayName(name, range(1993, self.end_year))
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 1993))

    def test_christmas_eve(self):
        name = "Christmas Eve (markets close at 1:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-12-24",
            "1997-12-24",
            "1998-12-24",
            "2001-12-24",
            "2002-12-24",
            "2003-12-24",
            "2007-12-24",
            "2008-12-24",
            "2009-12-24",
            "2012-12-24",
            "2013-12-24",
            "2014-12-24",
            "2015-12-24",
            "2018-12-24",
            "2019-12-24",
            "2020-12-24",
            "2024-12-24",
            "2025-12-24",
        )
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 1993))

    def test_special_half_day_holidays(self):
        special_holidays = [
            "1974-12-24",  # Christmas Eve (from 2:00pm).
            "1975-02-12",  # Snowstorm (from 2:30pm).
            "1975-12-24",  # Christmas Eve (from 2:00pm).
            "1976-08-09",  # Hurricane watch (from 3:00pm).
            "1978-02-06",  # Snowstorm (from 2:00pm).
            "1981-03-30",  # Assassination attempt on President Reagan (from 3:17pm).
            "1981-09-09",  # Con Edison power failure in lower Manhattan (from 3:28pm).
            "1987-10-23",  # Shortened hours following market break (from 2:00pm).
            "1987-10-26",  # Shortened hours following market break (from 2:00pm).
            "1987-10-27",  # Shortened hours following market break (from 2:00pm).
            "1987-10-28",  # Shortened hours following market break (from 2:00pm).
            "1987-10-29",  # Shortened hours following market break (from 2:00pm).
            "1987-10-30",  # Shortened hours following market break (from 2:00pm).
            "1987-11-02",  # Shortened hours following market break (from 2:30pm).
            "1987-11-03",  # Shortened hours following market break (from 2:30pm).
            "1987-11-04",  # Shortened hours following market break (from 2:30pm).
            "1987-11-05",  # Shortened hours following market break (from 3:00pm).
            "1987-11-06",  # Shortened hours following market break (from 3:00pm).
            "1987-11-09",  # Shortened hours following market break (from 3:30pm).
            "1987-11-10",  # Shortened hours following market break (from 3:30pm).
            "1987-11-11",  # Shortened hours following market break (from 3:30pm).
            "1990-12-24",  # Christmas Eve (from 2:00pm).
            "1991-12-24",  # Christmas Eve (from 2:00pm).
            "1992-11-27",  # Day after Thanksgiving Day (from 2:00pm).
            "1992-12-24",  # Christmas Eve (from 2:00pm).
            "1994-02-11",  # Snowstorm (from 2:30pm).
            "1996-07-05",  # Day after Independence Day (from 1:00pm).
            "1997-12-26",  # Friday after Christmas Day (from 1:00pm).
            "1999-12-31",  # New Year's Eve (from 1:00pm).
            "2002-07-05",  # Day after Independence Day (from 1:00pm).
            "2003-12-26",  # Friday after Christmas Day (from 1:00pm).
            "2013-07-03",  # Day before Independence Day (from 1:00pm).
        ]
        self.assertHalfDayHoliday(special_holidays)

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-16", "Martin Luther King Jr. Day"),
            ("2023-02-20", "Washington's Birthday"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-29", "Memorial Day"),
            ("2023-06-19", "Juneteenth National Independence Day"),
            ("2023-07-04", "Independence Day"),
            ("2023-09-04", "Labor Day"),
            ("2023-11-23", "Thanksgiving Day"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_half_day_2023(self):
        self.assertHalfDayHolidaysInYear(
            2023,
            ("2023-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2023-11-24", "Day after Thanksgiving Day (markets close at 1:00pm)"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Martin Luther King Jr. Day"),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_half_day_2024(self):
        self.assertHalfDayHolidaysInYear(
            2024,
            ("2024-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2024-11-29", "Day after Thanksgiving Day (markets close at 1:00pm)"),
            ("2024-12-24", "Christmas Eve (markets close at 1:00pm)"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-09", "National Day of Mourning for former President Jimmy Carter"),
            ("2025-01-20", "Martin Luther King Jr. Day"),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2025-11-28", "Day after Thanksgiving Day (markets close at 1:00pm)"),
            ("2025-12-24", "Christmas Eve (markets close at 1:00pm)"),
        )
