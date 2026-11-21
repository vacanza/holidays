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

from datetime import date
from unittest import TestCase

from holidays.countries.kiribati import Kiribati
from holidays.observed_holiday_base import SAT_SUN_TO_NEXT_MON_TUE
from tests.common import CommonCountryTests


class TestKiribati(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kiribati)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_womens_day(self):
        name = "International Women's Day"
        self.assertHolidayName(
            name,
            (f"{year}-03-08" for year in range(2003, self.end_year) if year not in (2025, 2026)),
        )
        self.assertHolidayName(
            "In honour of International Women's Day", "2025-03-07", "2026-03-09"
        )
        self.assertNoHolidayName(name, range(self.start_year, 2003))
        obs_dts = (
            "2014-03-10",
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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

    def test_holy_saturday(self):
        name = "Holy Saturday"
        self.assertHolidayName(
            name,
            "1999-04-03",
            "2000-04-22",
            "2001-04-14",
            "2002-03-30",
        )
        self.assertHolidayName(name, range(self.start_year, 2003))
        self.assertNoHolidayName(name, range(2003, self.end_year))

    def test_easter_monday(self):
        name = "Easter Monday"
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

    def test_national_health_day(self):
        name = "National Health Day"
        self.assertHolidayName(
            name,
            (f"{year}-04-19" for year in range(2003, self.end_year) if year not in (2025, 2026)),
        )
        self.assertHolidayName(name, "2025-04-07", "2026-04-07")
        self.assertNoHolidayName(name, range(self.start_year, 2003))
        obs_dts = (
            "2014-04-21",
            "2015-04-20",
            "2020-04-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)

    def test_public_holiday_may_9(self):
        name = "Public Holiday"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1993, 2003)))
        self.assertNoHolidayName(
            name,
            (
                f"{year}-05-09"
                for year in (*range(self.start_year, 1993), *range(2003, self.end_year))
            ),
        )
        obs_dts = (
            "1993-05-10",
            "1998-05-11",
            "1999-05-10",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_gospel_day(self):
        name = "Gospel Day"
        self.assertHolidayName(
            name, (f"{year}-07-11" for year in range(2002, self.end_year) if year != 2026)
        )
        self.assertHolidayName(name, "2026-07-10")
        self.assertNoHolidayName(name, range(self.start_year, 2002))

    def test_national_day_anniversary(self):
        name = "National Day - Independence Anniversary"
        self.assertHolidayName(name, (f"{year}-07-12" for year in range(1993, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1993))
        obs_dts = (
            "2014-07-14",
            "2015-07-13",
            "2020-07-13",
            "2025-07-14",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_day_unimwane(self):
        name = "National Day (in honor of Unimwane)"
        self.assertHolidayName(name, (f"{year}-07-15" for year in range(2002, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2002))

    def test_national_day_unaine(self):
        name = "National Day (in honor of Unaine)"
        self.assertHolidayName(name, (f"{year}-07-16" for year in range(2002, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2002))
        obs_dts = (
            "2011-07-18",
            "2016-07-18",
            "2017-07-17",
            "2022-07-18",
            "2023-07-17",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_public_holiday_1st_mon_of_aug(self):
        name = "Public Holiday"
        self.assertHolidayName(
            name,
            "1999-08-02",
            "2000-08-07",
            "2001-08-06",
            "2002-08-05",
        )
        self.assertHolidayName(name, range(self.start_year, 2003))
        self.assertNoHolidayName(name, range(2003, self.end_year))

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-08-05" for year in range(2003, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2003))
        obs_dts = (
            "2012-08-06",
            "2017-08-07",
            "2018-08-06",
            "2023-08-07",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_public_holiday_nov_10(self):
        name = "Public Holiday"
        self.assertHolidayName(name, (f"{year}-11-10" for year in range(self.start_year, 1993)))
        self.assertNoHolidayName(name, (f"{year}-11-10" for year in range(1993, self.end_year)))
        obs_dts = (
            "1985-11-11",
            "1990-11-12",
            "1991-11-11",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_human_rights_peace_day(self):
        name = "Human Rights and Peace Day"
        self.assertHolidayName(
            name,
            (f"{year}-12-10" for year in range(1993, 2003)),
            (f"{year}-12-09" for year in range(2003, self.end_year) if year not in (2025, 2026)),
        )
        self.assertHolidayName("In honour of Human Rights Day", "2025-12-12", "2026-12-11")
        self.assertNoHolidayName(name, range(self.start_year, 1993))
        obs_dts = (
            "1995-12-11",
            "2000-12-11",
            "2006-12-11",
            "2007-12-10",
            "2012-12-10",
            "2017-12-11",
            "2018-12-10",
            "2023-12-11",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_observed_false(self):
        holidays = Kiribati(years=(2025, 2026), observed=False)
        observed_holidays = {
            date(2025, 7, 14): "National Day - Independence Anniversary (observed)",
            date(2026, 7, 13): "National Day - Independence Anniversary (observed)",
            date(2026, 12, 28): "Boxing Day (observed)",
        }

        for dt, name in observed_holidays.items():
            self.assertNotIn(name, holidays.get(dt, ""))

        self.assertIn(
            "In honour of International Women's Day",
            holidays.get(date(2026, 3, 9), ""),
        )

    def test_observed_since(self):
        holidays = Kiribati(years=(2025, 2026), observed_since=2027)
        observed_holidays = {
            date(2025, 7, 14): "National Day - Independence Anniversary (observed)",
            date(2026, 7, 13): "National Day - Independence Anniversary (observed)",
            date(2026, 12, 28): "Boxing Day (observed)",
        }

        for dt, name in observed_holidays.items():
            self.assertNotIn(name, holidays.get(dt, ""))

        self.assertIn(
            "In honour of Boxing Day (Gift Day)",
            holidays.get(date(2026, 12, 28), ""),
        )
        self.assertIn(
            "In honour of International Women's Day",
            holidays.get(date(2026, 3, 9), ""),
        )

    def test_custom_observed_rule(self):
        holidays = Kiribati(years=2026, observed_rule=SAT_SUN_TO_NEXT_MON_TUE)
        observed_holidays = (
            (date(2026, 7, 14), "National Day - Independence Anniversary (observed)"),
        )

        for dt, name in observed_holidays:
            self.assertIn(name, holidays.get(dt, ""))

        self.assertNotIn(
            "National Day - Independence Anniversary (observed)",
            holidays.get(date(2026, 7, 13), ""),
        )
        self.assertIn(
            "In honour of International Women's Day",
            holidays.get(date(2026, 3, 9), ""),
        )

    def test_gazette_date_overrides(self):
        holidays = Kiribati(years=(2025, 2026))
        holidays_on_old_dates = (
            (date(2025, 3, 8), "International Women's Day"),
            (date(2025, 3, 10), "International Women's Day (observed)"),
            (date(2025, 4, 19), "National Health Day"),
            (date(2025, 4, 21), "National Health Day (observed)"),
            (date(2026, 3, 8), "International Women's Day"),
            (date(2026, 4, 19), "National Health Day"),
            (date(2026, 4, 20), "National Health Day (observed)"),
            (date(2026, 7, 11), "Gospel Day"),
            (date(2025, 12, 9), "Human Rights and Peace Day"),
            (date(2026, 12, 9), "Human Rights and Peace Day"),
        )

        for dt, name in holidays_on_old_dates:
            self.assertNotIn(name, holidays.get(dt, ""))

    def test_gazette_holidays_are_year_specific(self):
        holidays = Kiribati(years=2027)
        gazette_only_names = (
            "In honour of International Labour Day",
            "International Labour Day",
            "In honour of National Police Day",
            "In honor of National Youth & Children's Day",
            "National Youth & Children's Day",
            "In honour of World Teachers Day",
            "World Teachers Day",
            "In honour of Human Rights Day",
            "Kiribati Holiday",
        )

        for name in gazette_only_names:
            self.assertNoHolidayName(name, range(2027, 2028))

        self.assertNoHolidayName("National Health Day", date(2027, 4, 7))

    def test_gazette_appointed_weekday_dates(self):
        holidays = Kiribati(years=(2025, 2026), observed=False)
        gazette_holidays = (
            (date(2025, 10, 6), "In honour of World Teachers Day"),
            (date(2026, 8, 3), "National Youth & Children's Day"),
        )
        unappointed_dates = (
            (date(2025, 10, 5), "World Teachers Day"),
            (date(2026, 8, 1), "National Youth & Children's Day"),
        )

        for dt, name in gazette_holidays:
            self.assertIn(name, holidays.get(dt, ""))

        for dt, name in unappointed_dates:
            self.assertNotIn(name, holidays.get(dt, ""))

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-03-07", "In honour of International Women's Day"),
            ("2025-04-07", "National Health Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-25", "Special Day in honour of Pope Francis"),
            ("2025-05-02", "In honour of International Labour Day"),
            ("2025-06-23", "In honour of National Police Day"),
            ("2025-07-11", "Gospel Day"),
            ("2025-07-12", "National Day - Independence Anniversary"),
            ("2025-07-14", "National Day - Independence Anniversary (observed)"),
            (
                "2025-07-15",
                "National Culture and Senior Citizens Day; National Day (in honor of Unimwane)",
            ),
            ("2025-07-16", "Kiribati Special Day; National Day (in honor of Unaine)"),
            ("2025-08-01", "In honor of National Youth & Children's Day"),
            ("2025-08-05", "Youth Day"),
            ("2025-10-06", "In honour of World Teachers Day"),
            ("2025-12-12", "In honour of Human Rights Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
            ("2025-12-29", "Kiribati Holiday"),
            ("2025-12-30", "Kiribati Holiday"),
            ("2025-12-31", "Kiribati Holiday"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "New Year's Day"),
            ("2026-01-02", "Kiribati Holiday"),
            ("2026-03-09", "In honour of International Women's Day"),
            ("2026-04-03", "Good Friday"),
            ("2026-04-06", "Easter Monday"),
            ("2026-04-07", "National Health Day"),
            ("2026-05-01", "International Labour Day"),
            ("2026-06-22", "In honour of National Police Day"),
            ("2026-07-10", "Gospel Day"),
            ("2026-07-12", "National Day - Independence Anniversary"),
            ("2026-07-13", "National Day - Independence Anniversary (observed)"),
            ("2026-07-14", "Kiribati Culture and Senior Citizens Day"),
            ("2026-07-15", "Kiribati Special Day; National Day (in honor of Unimwane)"),
            ("2026-07-16", "National Day (in honor of Unaine)"),
            ("2026-08-03", "National Youth & Children's Day"),
            ("2026-08-05", "Youth Day"),
            ("2026-10-05", "World Teachers Day"),
            ("2026-12-11", "In honour of Human Rights Day"),
            ("2026-12-25", "Christmas Day"),
            ("2026-12-26", "Boxing Day"),
            (
                "2026-12-28",
                "Boxing Day (observed); In honour of Boxing Day (Gift Day)",
            ),
            ("2026-12-29", "Kiribati Holiday"),
            ("2026-12-30", "Kiribati Holiday"),
            ("2026-12-31", "Kiribati Holiday"),
        )
