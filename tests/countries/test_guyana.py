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

from holidays.countries.guyana import Guyana
from tests.common import CommonCountryTests


class TestGuyana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Guyana)

    def test_special_holidays(self):
        self.assertHolidayName("Public Holiday", "2020-03-02")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(
            name,
            (
                f"{year}-05-26"
                for year in (*range(self.start_year, 1970), *range(2016, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1970, 2016))

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(name, (f"{year}-02-23" for year in range(1970, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1970))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2019-04-19",
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
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        dt = (
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_arrival_day(self):
        name = "Arrival Day"
        self.assertHolidayName(name, (f"{year}-05-05" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))
        dt = (
            "2019-05-06",
            "2024-05-06",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_caricom_day(self):
        name = "CARICOM Day"
        self.assertHolidayName(
            name,
            "2021-07-05",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-07-07",
        )
        self.assertHolidayName(name, range(2016, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2016))

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        self.assertHolidayName(
            name,
            "2011-08-01",
            "2012-08-06",
            "2013-08-05",
            "2014-08-04",
            "2015-08-03",
        )
        self.assertHolidayName(name, range(self.start_year, 2016))
        self.assertNoHolidayName(name, range(2016, self.end_year))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(2016, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2016))
        dt = (
            "2021-08-02",
            "2027-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_day_after_christmas(self):
        name = "Day after Christmas"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        dt = (
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_phagwah_day(self):
        name = "Phagwah"
        self.assertHolidayName(
            name,
            "2020-03-10",
            "2021-03-28",
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertHolidayName(name, range(2001, 2036))
        dt = (
            "2004-03-08",
            "2007-03-05",
            "2011-03-21",
            "2017-03-13",
            "2021-03-29",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_deepavali_day(self):
        name = "Deepavali"
        self.assertHolidayName(
            name,
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(2001, 2036))
        dt = (
            "2013-11-04",
            "2016-10-31",
            "2019-10-28",
            "2023-11-13",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_youman_nabi_day(self):
        name = "Youman Nabi"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        dt = (
            "2004-05-03",
            "2012-02-06",
            "2019-11-11",
            "2022-10-10",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_eid_ul_azha_day(self):
        name = "Eid-Ul-Azha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-21",
            "2022-07-09",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        dt = (
            "2014-10-06",
            "2019-08-12",
        )
        self.assertIslamicNoEstimatedHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2024(self):
        self.assertHolidays(
            Guyana(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-02-23", "Republic Day"),
            ("2024-03-25", "Phagwah"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-05", "Arrival Day"),
            ("2024-05-06", "Arrival Day (observed)"),
            ("2024-05-26", "Independence Day"),
            ("2024-06-17", "Eid-Ul-Azha"),
            ("2024-07-01", "CARICOM Day"),
            ("2024-08-01", "Emancipation Day"),
            ("2024-09-16", "Youman Nabi"),
            ("2024-10-31", "Deepavali"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Day after Christmas"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-02-23", "Republic Day"),
            ("2025-03-14", "Phagwah"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labour Day"),
            ("2025-05-05", "Arrival Day"),
            ("2025-05-26", "Independence Day"),
            ("2025-06-07", "Eid-Ul-Azha"),
            ("2025-07-07", "CARICOM Day"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-05", "Youman Nabi"),
            ("2025-10-20", "Deepavali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day after Christmas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-02-23", "Republic Day"),
            ("2025-03-14", "Holi"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-05", "Arrival Day"),
            ("2025-05-26", "Independence Day"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-07-07", "CARICOM Day"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-05", "Prophet's Birthday"),
            ("2025-10-20", "Diwali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day after Christmas"),
        )
