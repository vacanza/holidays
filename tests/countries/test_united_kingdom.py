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

import warnings
from unittest import TestCase

from holidays.countries.united_kingdom import UnitedKingdom
from tests.common import CommonCountryTests


class TestUnitedKingdom(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedKingdom)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_no_holidays(self):
        super().test_no_holidays()

        for subdiv in UnitedKingdom.subdivisions:
            self.assertNoHolidays(UnitedKingdom(years=self.start_year - 1, subdiv=subdiv))

    def test_special_holidays(self):
        self.assertHoliday(
            "1977-06-07",
            "1981-07-29",
            "1999-12-31",
            "2002-06-03",
            "2011-04-29",
            "2012-06-05",
            "2022-06-03",
            "2022-09-19",
            "2023-05-08",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1975, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1975))

        obs_dts = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_new_years_day_scotland(self):
        name_new_year = "New Year's Day"
        name_new_year_holiday = "New Year Holiday"

        nyh_obs_dts = (
            "2000-01-04",
            "2005-01-04",
            "2006-01-03",
            "2010-01-04",
            "2011-01-04",
            "2012-01-03",
            "2016-01-04",
            "2017-01-03",
            "2021-01-04",
            "2022-01-04",
            "2023-01-03",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SCT":
                self.assertSubdivSctHolidayName(
                    name_new_year, (f"{year}-01-01" for year in self.full_range)
                )
                self.assertSubdivSctHolidayName(
                    f"{name_new_year} (observed)",
                    "2000-01-03",
                    "2005-01-03",
                    "2006-01-02",
                    "2011-01-03",
                    "2012-01-02",
                    "2017-01-02",
                    "2022-01-03",
                    "2023-01-02",
                )
                self.assertSubdivSctHolidayName(
                    name_new_year_holiday, (f"{year}-01-02" for year in self.full_range)
                )
                self.assertSubdivSctHolidayName(f"{name_new_year_holiday} (observed)", nyh_obs_dts)
                self.assertNoSubdivSctNonObservedHoliday(nyh_obs_dts)
            else:
                self.assertNoHolidayName(name_new_year_holiday, holidays)

    def test_saint_patricks_day(self):
        name = "Saint Patrick's Day"
        self.assertNoHolidayName(name)

        obs_dts = (
            "2001-03-19",
            "2002-03-18",
            "2007-03-19",
            "2012-03-19",
            "2013-03-18",
            "2018-03-19",
            "2019-03-18",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NIR":
                self.assertSubdivNirHolidayName(
                    name, (f"{year}-03-17" for year in range(1903, self.end_year))
                )
                self.assertNoSubdivNirHolidayName(name, range(self.start_year, 1903))
                self.assertSubdivNirHolidayName(f"{name} (observed)", obs_dts)
                self.assertNoSubdivNirNonObservedHoliday(obs_dts)
            else:
                self.assertNoHolidayName(name, holidays)

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

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertNoHolidayName(name)

        dts = (
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SCT":
                self.assertNoSubdivSctHolidayName(name)
            else:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, self.full_range)

    def test_may_day(self):
        name = "May Day"
        self.assertHolidayName(
            name,
            "1978-05-01",
            "1979-05-07",
            "1980-05-05",
            "1995-05-08",
            "1999-05-03",
            "2000-05-01",
            "2010-05-03",
            "2016-05-02",
            "2018-05-07",
            "2019-05-06",
            "2020-05-08",
        )
        self.assertHolidayName(name, range(1978, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1978))

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertNoHolidayName(name)

        dts = (
            "1965-06-07",
            "1966-05-30",
            "1967-05-15",
            "1968-06-03",
            "1969-05-26",
            "1970-05-18",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SCT":
                self.assertNoHolidayName(name, holidays)
            else:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(self.start_year, 1971))
                self.assertNoHolidayName(name, holidays, range(1971, self.end_year))

    def test_spring_bank_holiday(self):
        name = "Spring Bank Holiday"
        self.assertHolidayName(
            name,
            "2002-06-04",
            "2012-06-04",
            "2020-05-25",
            "2021-05-31",
            "2022-06-02",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHolidayName(name, range(1971, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1971))

    def test_battle_of_the_boyne_day(self):
        name = "Battle of the Boyne"
        self.assertNoHolidayName(name)

        obs_dts = (
            "2003-07-14",
            "2008-07-14",
            "2009-07-13",
            "2014-07-14",
            "2015-07-13",
            "2020-07-13",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NIR":
                self.assertSubdivNirHolidayName(
                    name, (f"{year}-07-12" for year in self.full_range)
                )
                self.assertSubdivNirHolidayName(f"{name} (observed)", obs_dts)
                self.assertNoSubdivNirNonObservedHoliday(obs_dts)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_summer_bank_holiday(self):
        name = "Summer Bank Holiday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SCT":
                self.assertSubdivSctHolidayName(
                    name,
                    "2020-08-03",
                    "2021-08-02",
                    "2022-08-01",
                    "2023-08-07",
                    "2024-08-05",
                    "2025-08-04",
                )
                self.assertSubdivSctHolidayName(name, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_late_summer_bank_holiday(self):
        name = "Late Summer Bank Holiday"
        self.assertNoHolidayName(name)

        dts = (
            "2020-08-31",
            "2021-08-30",
            "2022-08-29",
            "2023-08-28",
            "2024-08-26",
            "2025-08-25",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SCT":
                self.assertNoSubdivSctHolidayName(name)
            else:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(1971, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1971))

    def test_saint_andrews_day(self):
        name = "Saint Andrew's Day"
        self.assertNoHolidayName(name)

        obs_dts = (
            "2008-12-01",
            "2013-12-02",
            "2014-12-01",
            "2019-12-02",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SCT":
                self.assertSubdivSctHolidayName(
                    name, (f"{year}-11-30" for year in range(2006, self.end_year))
                )
                self.assertNoSubdivSctHolidayName(name, range(self.start_year, 2006))
                self.assertSubdivSctHolidayName(f"{name} (observed)", obs_dts)
                self.assertNoSubdivSctNonObservedHoliday(obs_dts)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        obs_dts = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day_scotland(self):
        name = "Christmas Day"

        obs_dts = (
            "1955-12-26",
            "1960-12-26",
            "1966-12-26",
        )
        self.assertSubdivSctHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoSubdivSctNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(f"{name} (observed)", obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        obs_dts = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day_scotland(self):
        name = "Boxing Day"
        self.assertSubdivSctHolidayName(
            name, (f"{year}-12-26" for year in range(1974, self.end_year))
        )
        self.assertNoSubdivSctHolidayName(name, range(self.start_year, 1974))

    def test_all_holidays_present(self):
        y_2015 = set()
        for subdiv in UnitedKingdom.subdivisions:
            y_2015.update(UnitedKingdom(observed=False, years=2015, subdiv=subdiv).values())

        all_holidays = {
            "New Year's Day",
            "New Year Holiday",
            "Saint Patrick's Day",
            "Good Friday",
            "Easter Monday",
            "May Day",
            "Spring Bank Holiday",
            "Summer Bank Holiday",
            "Battle of the Boyne",
            "Late Summer Bank Holiday",
            "Saint Andrew's Day",
            "Christmas Day",
            "Boxing Day",
        }
        self.assertEqual(all_holidays, y_2015)

    def test_l10n_default(self):
        # https://www.gov.uk/bank-holidays
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year Holiday"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-03-18", "Saint Patrick's Day (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-07-12", "Battle of the Boyne"),
            ("2024-08-05", "Summer Bank Holiday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-11-30", "Saint Andrew's Day"),
            ("2024-12-02", "Saint Andrew's Day (observed)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year Holiday"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-03-18", "Saint Patrick's Day (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-07-12", "Battle of the Boyne"),
            ("2024-08-05", "Summer Bank Holiday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-11-30", "Saint Andrew's Day"),
            ("2024-12-02", "Saint Andrew's Day (observed)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-01-02", "หยุดวันขึ้นปีใหม่"),
            ("2024-03-17", "วันนักบุญแพทริก"),
            ("2024-03-18", "ชดเชยวันนักบุญแพทริก"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-04-01", "วันจันทร์อีสเตอร์"),
            ("2024-05-06", "วันเมย์เดย์"),
            ("2024-05-27", "วันหยุดฤดูใบไม้ผลิของธนาคาร"),
            ("2024-07-12", "วันรำลึกยุทธการแม่น้ำบอยน์"),
            ("2024-08-05", "วันหยุดฤดูร้อนของธนาคาร"),
            ("2024-08-26", "วันหยุดช่วงปลายฤดูร้อนของธนาคาร"),
            ("2024-11-30", "วันนักบุญแอนดรูว์"),
            ("2024-12-02", "ชดเชยวันนักบุญแอนดรูว์"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-26", "วันเปิดกล่องของขวัญ"),
        )
