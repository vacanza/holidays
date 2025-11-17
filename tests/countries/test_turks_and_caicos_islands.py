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

from holidays.countries.turks_and_caicos_islands import TurksAndCaicosIslands
from tests.common import CommonCountryTests


class TestTC(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TurksAndCaicosIslands, years=range(1963, 2050))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1963, 2050)))
        obs_dt = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        self.assertHolidayName(
            name,
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
            "2023-03-13",
            "2024-03-11",
            "2025-03-10",
        )
        self.assertHolidayName(name, range(1963, 2050))

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
        self.assertHolidayName(name, range(1963, 2050))

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
        self.assertHolidayName(name, range(1963, 2050))

    def test_jags_mccartney_day(self):
        name_pre_2020 = "National Heroes Day"
        name_2020 = "JAGS McCartney Day"

        self.assertHolidayName(
            name_pre_2020,
            "2014-05-26",
            "2015-05-25",
            "2016-05-30",
            "2017-05-29",
            "2018-05-28",
            "2019-05-27",
        )
        self.assertHolidayName(
            name_2020,
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )

        self.assertHolidayName(name_pre_2020, range(1963, 2020))
        self.assertHolidayName(name_2020, range(2020, 2050))
        self.assertNoHolidayName(name_pre_2020, range(2020, 2050))
        self.assertNoHolidayName(name_2020, range(1963, 2020))

    def test_sovereign_birthday(self):
        name_pre_2023 = "Queen's Birthday"
        name_2023 = "King's Birthday"

        self.assertHolidayName(
            name_pre_2023,
            "2017-06-12",
            "2018-06-11",
            "2019-06-10",
            "2020-06-08",
            "2021-06-14",
            "2022-06-03",
        )
        self.assertHolidayName(
            name_2023,
            "2023-06-19",
            "2024-06-17",
            "2025-06-23",
        )

        self.assertHolidayName(name_pre_2023, range(1963, 2023))
        self.assertHolidayName(name_2023, range(2023, 2050))
        self.assertNoHolidayName(name_pre_2023, range(2023, 2050))
        self.assertNoHolidayName(name_2023, range(1963, 2023))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1963, 2050)))
        obs_dt = (
            "2004-08-02",
            "2009-08-03",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
            "2021-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_youth_day(self):
        name = "National Youth Day"
        self.assertHolidayName(
            name,
            "2020-09-25",
            "2021-09-24",
            "2022-09-30",
            "2023-09-29",
            "2024-09-27",
            "2025-09-26",
        )
        self.assertHolidayName(name, range(1963, 2050))

    def test_national_heritage_day(self):
        name_pre_2014 = "Columbus Day"
        name_2014 = "National Heritage Day"

        self.assertHolidayName(
            name_pre_2014,
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
        )
        self.assertHolidayName(
            name_2014,
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
        )

        self.assertHolidayName(name_pre_2014, range(1963, 2014))
        self.assertHolidayName(name_2014, range(2014, 2050))
        self.assertNoHolidayName(name_pre_2014, range(2014, 2050))
        self.assertNoHolidayName(name_2014, range(1963, 2014))

    def test_national_day_of_thanksgiving(self):
        name = "National Day of Thanksgiving"
        self.assertHolidayName(
            name,
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-22",
            "2025-11-28",
        )
        self.assertHolidayName(name, range(1963, 2050))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1963, 2050)))
        obs_dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1963, 2050)))
        obs_dt = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2023(self):
        self.assertHolidays(
            TurksAndCaicosIslands(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-03-13", "Commonwealth Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-29", "JAGS McCartney Day"),
            ("2023-06-19", "King's Birthday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-09-29", "National Youth Day"),
            ("2023-10-09", "National Heritage Day"),
            ("2023-11-24", "National Day of Thanksgiving"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-23", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-23", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
