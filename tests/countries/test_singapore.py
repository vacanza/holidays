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

from holidays.countries.singapore import Singapore
from tests.common import CommonCountryTests


class TestSingapore(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Singapore)

    def test_special_holidays(self):
        self.assertHoliday(
            "2001-11-03",
            "2006-05-06",
            "2011-05-07",
            "2015-08-07",
            "2015-09-11",
            "2020-07-10",
            "2023-09-01",
            "2025-05-03",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_chinese_new_year(self):
        name = "Chinese New Year"
        self.assertHolidayName(
            name,
            "2020-01-25",
            "2020-01-26",
            "2021-02-12",
            "2021-02-13",
            "2022-02-01",
            "2022-02-02",
            "2023-01-22",
            "2023-01-23",
            "2024-02-10",
            "2024-02-11",
            "2025-01-29",
            "2025-01-30",
        )
        obs_dts = (
            "2017-01-30",
            "2020-01-27",
            "2023-01-24",
            "2024-02-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Hari Raya Puasa"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2009-09-21",
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        name_day2 = f"Second Day of {name}"
        self.assertIslamicNoEstimatedHolidayName(
            name_day2,
            "1963-02-26",
            "1964-02-16",
            "1965-02-04",
            "1966-01-24",
            "1967-01-13",
            "1968-01-02",
            "1968-12-22",
        )
        self.assertIslamicNoEstimatedHolidayName(name_day2, range(self.start_year, 1969))
        self.assertNoIslamicNoEstimatedHolidayName(name_day2, range(1969, self.end_year))

    def test_eid_al_adha(self):
        name = "Hari Raya Haji"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2007-01-02",
            "2011-11-07",
            "2014-10-06",
            "2019-08-12",
            "2022-07-11",
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
            "1963-04-13",
            "1964-03-28",
            "1965-04-17",
            "1966-04-09",
            "1967-03-25",
            "1968-04-13",
        )
        self.assertHolidayName(name, range(self.start_year, 1969))
        self.assertNoHolidayName(name, range(1969, self.end_year))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "1963-04-15",
            "1964-03-30",
            "1965-04-19",
            "1966-04-11",
            "1967-03-27",
            "1968-04-15",
        )
        self.assertHolidayName(name, range(self.start_year, 1969))
        self.assertNoHolidayName(name, range(1969, self.end_year))

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_vesak_day(self):
        name = "Vesak Day"
        self.assertHolidayName(
            name,
            "2020-05-07",
            "2021-05-26",
            "2022-05-15",
            "2023-06-02",
            "2024-05-22",
            "2025-05-12",
        )
        obs_dts = (
            "2005-05-23",
            "2019-05-20",
            "2022-05-16",
            "2026-06-01",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_day(self):
        name = "National Day"
        self.assertHolidayName(name, (f"{year}-08-09" for year in self.full_range))
        obs_dts = (
            "2009-08-10",
            "2015-08-10",
            "2020-08-10",
            "2026-08-10",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_diwali(self):
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
        obs_dts = (
            "2009-11-16",
            "2019-10-28",
            "2023-11-13",
            "2026-11-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(self.start_year, 1969)))
        self.assertNoHolidayName(range(1969, self.end_year))

    def test_2018(self):
        self.assertHolidaysInYear(
            2018,
            ("2018-01-01", "New Year's Day"),
            ("2018-02-16", "Chinese New Year"),
            ("2018-02-17", "Chinese New Year"),
            ("2018-03-30", "Good Friday"),
            ("2018-05-01", "Labour Day"),
            ("2018-05-29", "Vesak Day"),
            ("2018-06-15", "Hari Raya Puasa"),
            ("2018-08-09", "National Day"),
            ("2018-08-22", "Hari Raya Haji"),
            ("2018-11-06", "Deepavali"),
            ("2018-12-25", "Christmas Day"),
        )

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "New Year's Day"),
            ("2019-02-05", "Chinese New Year"),
            ("2019-02-06", "Chinese New Year"),
            ("2019-04-19", "Good Friday"),
            ("2019-05-01", "Labour Day"),
            ("2019-05-19", "Vesak Day"),
            ("2019-05-20", "Vesak Day (observed)"),
            ("2019-06-05", "Hari Raya Puasa"),
            ("2019-08-09", "National Day"),
            ("2019-08-11", "Hari Raya Haji"),
            ("2019-08-12", "Hari Raya Haji (observed)"),
            ("2019-10-27", "Deepavali"),
            ("2019-10-28", "Deepavali (observed)"),
            ("2019-12-25", "Christmas Day"),
        )

    def test_2020(self):
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "New Year's Day"),
            ("2020-01-25", "Chinese New Year"),
            ("2020-01-26", "Chinese New Year"),
            ("2020-01-27", "Chinese New Year (observed)"),
            ("2020-04-10", "Good Friday"),
            ("2020-05-01", "Labour Day"),
            ("2020-05-07", "Vesak Day"),
            ("2020-05-24", "Hari Raya Puasa"),
            ("2020-05-25", "Hari Raya Puasa (observed)"),
            ("2020-07-10", "Polling Day"),
            ("2020-07-31", "Hari Raya Haji"),
            ("2020-08-09", "National Day"),
            ("2020-08-10", "National Day (observed)"),
            ("2020-11-14", "Deepavali"),
            ("2020-12-25", "Christmas Day"),
        )

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "New Year's Day"),
            ("2021-02-12", "Chinese New Year"),
            ("2021-02-13", "Chinese New Year"),
            ("2021-04-02", "Good Friday"),
            ("2021-05-01", "Labour Day"),
            ("2021-05-13", "Hari Raya Puasa"),
            ("2021-05-26", "Vesak Day"),
            ("2021-07-20", "Hari Raya Haji"),
            ("2021-08-09", "National Day"),
            ("2021-11-04", "Deepavali"),
            ("2021-12-25", "Christmas Day"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-02-01", "Chinese New Year"),
            ("2022-02-02", "Chinese New Year"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-03", "Hari Raya Puasa"),
            ("2022-05-15", "Vesak Day"),
            ("2022-05-16", "Vesak Day (observed)"),
            ("2022-07-10", "Hari Raya Haji"),
            ("2022-07-11", "Hari Raya Haji (observed)"),
            ("2022-08-09", "National Day"),
            ("2022-10-24", "Deepavali"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-02-10", "Chinese New Year"),
            ("2024-02-11", "Chinese New Year"),
            ("2024-02-12", "Chinese New Year (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-10", "Hari Raya Puasa"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-22", "Vesak Day"),
            ("2024-06-17", "Hari Raya Haji"),
            ("2024-08-09", "National Day"),
            ("2024-10-31", "Deepavali"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-29", "Chinese New Year"),
            ("2025-01-30", "Chinese New Year"),
            ("2025-03-31", "Hari Raya Puasa"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Labour Day"),
            ("2025-05-03", "Polling Day"),
            ("2025-05-12", "Vesak Day"),
            ("2025-06-07", "Hari Raya Haji"),
            ("2025-08-09", "National Day"),
            ("2025-10-20", "Deepavali"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "New Year's Day"),
            ("2026-02-17", "Chinese New Year"),
            ("2026-02-18", "Chinese New Year"),
            ("2026-03-21", "Hari Raya Puasa"),
            ("2026-04-03", "Good Friday"),
            ("2026-05-01", "Labour Day"),
            ("2026-05-27", "Hari Raya Haji"),
            ("2026-05-31", "Vesak Day"),
            ("2026-06-01", "Vesak Day (observed)"),
            ("2026-08-09", "National Day"),
            ("2026-08-10", "National Day (observed)"),
            ("2026-11-08", "Deepavali"),
            ("2026-11-09", "Deepavali (observed)"),
            ("2026-12-25", "Christmas Day"),
        )

    def test_2027(self):
        self.assertHolidaysInYear(
            2027,
            ("2027-01-01", "New Year's Day"),
            ("2027-02-06", "Chinese New Year"),
            ("2027-02-07", "Chinese New Year"),
            ("2027-02-08", "Chinese New Year (observed)"),
            ("2027-03-10", "Hari Raya Puasa"),
            ("2027-03-26", "Good Friday"),
            ("2027-05-01", "Labour Day"),
            ("2027-05-17", "Hari Raya Haji"),
            ("2027-05-20", "Vesak Day"),
            ("2027-08-09", "National Day"),
            ("2027-10-28", "Deepavali"),
            ("2027-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Chinese New Year"),
            ("2023-01-23", "Chinese New Year"),
            ("2023-01-24", "Chinese New Year (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-22", "Hari Raya Puasa"),
            ("2023-05-01", "Labour Day"),
            ("2023-06-02", "Vesak Day"),
            ("2023-06-29", "Hari Raya Haji"),
            ("2023-08-09", "National Day"),
            ("2023-09-01", "Polling Day"),
            ("2023-11-12", "Deepavali"),
            ("2023-11-13", "Deepavali (observed)"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Chinese New Year"),
            ("2023-01-23", "Chinese New Year"),
            ("2023-01-24", "Chinese New Year (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-02", "Vesak Day"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-08-09", "National Day"),
            ("2023-09-01", "Polling Day"),
            ("2023-11-12", "Diwali"),
            ("2023-11-13", "Diwali (observed)"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2023-01-01", "วันขึ้นปีใหม่"),
            ("2023-01-02", "ชดเชยวันขึ้นปีใหม่"),
            ("2023-01-22", "วันตรุษจีน"),
            ("2023-01-23", "วันตรุษจีน"),
            ("2023-01-24", "ชดเชยวันตรุษจีน"),
            ("2023-04-07", "วันศุกร์ประเสริฐ"),
            ("2023-04-22", "วันอีฎิ้ลฟิตริ"),
            ("2023-05-01", "วันแรงงาน"),
            ("2023-06-02", "วันวิสาขบูชา"),
            ("2023-06-29", "วันอีดิ้ลอัฎฮา"),
            ("2023-08-09", "วันชาติสิงคโปร์"),
            ("2023-09-01", "วันเลือกตั้ง"),
            ("2023-11-12", "วันดีปาวลี"),
            ("2023-11-13", "ชดเชยวันดีปาวลี"),
            ("2023-12-25", "วันคริสต์มาส"),
        )
