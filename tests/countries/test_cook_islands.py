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

from holidays.countries.cook_islands import CookIslands, CK, COK
from tests.common import CommonCountryTests


class TestCookIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CookIslands)

    def test_country_aliases(self):
        self.assertAliases(CookIslands, CK, COK)

    def test_no_holidays(self):
        self.assertNoHolidays(CookIslands(years=self.start_year - 1))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2011-01-03",
            "2012-01-03",
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_after_new_years(self):
        name = "Day after New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-02" for year in self.full_range))
        obs_dts = (
            "2010-01-04",
            "2011-01-04",
            "2016-01-04",
            "2021-01-04",
            "2022-01-04",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_anzac_day(self):
        self.assertHolidayName("Anzac Day", (f"{year}-04-25" for year in self.full_range))

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

    def test_sovereigns_birthday(self):
        name = "Sovereign's Birthday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
            "2023-06-05",
            "2024-06-03",
            "2025-06-02",
        )
        self.assertHolidayName(name, self.full_range)

    def test_house_of_ariki_day(self):
        name = "Ra o te Ui Ariki"
        self.assertHolidayName(
            name,
            "2012-06-06",
            "2020-07-03",
            "2021-07-02",
            "2022-07-01",
            "2023-07-07",
            "2024-07-05",
            "2025-07-04",
        )
        self.assertHolidayName(name, range(2012, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2012))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-08-04" for year in self.full_range))
        obs_dts = (
            "2012-08-06",
            "2013-08-05",
            "2018-08-06",
            "2019-08-05",
            "2024-08-05",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_cook_islands_gospel_day(self):
        name = "Cook Islands Gospel Day"
        self.assertHolidayName(name, (f"{year}-10-26" for year in self.full_range))
        obs_dts = (
            "2013-10-28",
            "2014-10-27",
            "2019-10-28",
            "2024-10-28",
            "2025-10-27",
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
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_penrhyn_gospel_day(self):
        name = "Penrhyn Gospel Day"
        self.assertHolidayName(name, (f"{year}-03-13" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2004-03-15",
            "2005-03-14",
            "2010-03-15",
            "2011-03-14",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_palmerston_gospel_day(self):
        name = "Palmerston Gospel Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2002-05-27",
            "2003-05-26",
            "2008-05-26",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_mangaia_gospel_day(self):
        name = "Mangaia Gospel Day"
        self.assertHolidayName(name, (f"{year}-06-15" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2002-06-17",
            "2003-06-16",
            "2008-06-16",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_atiu_gospel_day(self):
        name = "Atiu Gospel Day"
        self.assertHolidayName(name, (f"{year}-07-20" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2002-07-22",
            "2003-07-21",
            "2008-07-21",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHolidayName(name_observed, obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_mitiaro_gospel_day(self):
        name = "Mitiaro Gospel Day"
        self.assertHolidayName(name, (f"{year}-07-21" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2001-07-23",
            "2002-07-22",
            "2007-07-23",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHolidayName(name_observed, obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_mauke_gospel_day(self):
        name = "Mauke Gospel Day"
        self.assertHolidayName(name, (f"{year}-07-23" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2000-07-24",
            "2005-07-26",
            "2011-07-26",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_rarotonga_gospel_day(self):
        name = "Rarotonga Gospel Day"
        self.assertHolidayName(name, (f"{year}-07-25" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2004-07-26",
            "2009-07-27",
            "2010-07-26",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_manihiki_gospel_day(self):
        name = "Manihiki Gospel Day"
        self.assertHolidayName(name, (f"{year}-08-08" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2004-08-09",
            "2009-08-10",
            "2010-08-09",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_rakahanga_gospel_day(self):
        name = "Rakahanga Gospel Day"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2004-08-16",
            "2009-08-17",
            "2010-08-16",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_aitutaki_gospel_day(self):
        name = "Aitutaki Gospel Day"
        self.assertHolidayName(name, (f"{year}-10-27" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2001-10-29",
            "2002-10-28",
            "2007-10-29",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_pukapuka_gospel_day(self):
        name = "Pukapuka Gospel Day"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(self.start_year, 2012)))
        self.assertNoHolidayName(name, range(2012, self.end_year))
        obs_dts = (
            "2001-12-10",
            "2002-12-09",
            "2007-12-10",
        )
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(2012, self.end_year))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "Day after New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-04", "Day after New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "Anzac Day"),
            ("2022-06-06", "Sovereign's Birthday"),
            ("2022-07-01", "Ra o te Ui Ariki"),
            ("2022-08-04", "Constitution Day"),
            ("2022-10-26", "Cook Islands Gospel Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "Day after New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-04", "Day after New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "Anzac Day"),
            ("2022-06-06", "Sovereign's Birthday"),
            ("2022-07-01", "Day of the House of Ariki"),
            ("2022-08-04", "Constitution Day"),
            ("2022-10-26", "Cook Islands Gospel Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
