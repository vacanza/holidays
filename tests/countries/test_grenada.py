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

from holidays.countries.grenada import Grenada
from tests.common import CommonCountryTests


class TestGrenada(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Grenada)

    def test_special_holidays(self):
        self.assertHoliday(
            "2011-12-27",
            "2013-02-22",
            "2016-12-27",
            "2018-03-14",
            "2022-06-24",
            "2022-12-27",
            "2023-07-04",
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

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-02-07" for year in self.full_range))
        obs_dts = (
            "2010-02-08",
            "2016-02-08",
            "2021-02-08",
            "2027-02-08",
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

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name, range(self.start_year, 2025))
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(2025, self.end_year)))
        obs_dts = (
            "2027-08-02",
            "2032-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_carnival_monday(self):
        name = "Carnival Monday"
        self.assertHolidayName(
            name,
            "2020-08-10",
            "2021-08-09",
            "2022-08-08",
            "2023-08-14",
            "2024-08-12",
            "2025-08-11",
        )
        self.assertHolidayName(name, self.full_range)

    def test_carnival_tuesday(self):
        name = "Carnival Tuesday"
        self.assertHolidayName(
            name,
            "2020-08-11",
            "2021-08-10",
            "2022-08-09",
            "2023-08-15",
            "2024-08-13",
            "2025-08-12",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_heroes_day(self):
        name = "National Heroes' Day"
        self.assertHolidayName(name, (f"{year}-10-19" for year in range(2023, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2023))
        obs_dts = (
            "2025-10-20",
            "2031-10-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(name, (f"{year}-10-25" for year in self.full_range))
        obs_dts = (
            "2009-10-26",
            "2015-10-26",
            "2020-10-26",
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

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2012(self):
        # https://web.archive.org/web/20120623100105/http://www.gov.gd/holiday_events.html
        self.assertHolidays(
            Grenada(years=2012),
            ("2012-01-01", "New Year's Day"),
            ("2012-01-02", "New Year's Day (observed)"),
            ("2012-02-07", "Independence Day"),
            ("2012-04-06", "Good Friday"),
            ("2012-04-09", "Easter Monday"),
            ("2012-05-01", "Labour Day"),
            ("2012-05-28", "Whit Monday"),
            ("2012-06-07", "Corpus Christi"),
            ("2012-08-06", "Emancipation Day"),
            ("2012-08-13", "Carnival Monday"),
            ("2012-08-14", "Carnival Tuesday"),
            ("2012-10-25", "Thanksgiving Day"),
            ("2012-12-25", "Christmas Day"),
            ("2012-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-02-07", "Independence Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labour Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-06-19", "Corpus Christi"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-08-11", "Carnival Monday"),
            ("2025-08-12", "Carnival Tuesday"),
            ("2025-10-19", "National Heroes' Day"),
            ("2025-10-20", "National Heroes' Day (observed)"),
            ("2025-10-25", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-02-07", "Independence Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-06-19", "Corpus Christi"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-08-11", "Carnival Monday"),
            ("2025-08-12", "Carnival Tuesday"),
            ("2025-10-19", "National Heroes' Day"),
            ("2025-10-20", "National Heroes' Day (observed)"),
            ("2025-10-25", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
