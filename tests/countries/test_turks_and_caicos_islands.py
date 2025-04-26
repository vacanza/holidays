#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.countries.turks_and_caicos_islands import TurksAndCaicosIslands, TC, TCA
from tests.common import CommonCountryTests


class TestTC(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TurksAndCaicosIslands, years=range(2020, 2025))

    def test_country_aliases(self):
        self.assertAliases(TurksAndCaicosIslands, TC, TCA)

    def test_no_checks(self):
        self.assertNoChecks(TurksAndCaicosIslands)

    def test_commonwealth_day(self):
        self.assertHolidayName(
            "Commonwealth Day",
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
            "2023-03-13",
            "2024-03-11",
            "2025-03-10",
        )

    def test_good_friday(self):
        self.assertHolidayName(
            "Good Friday",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Easter Monday",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )

    def test_jags_mccartney_day(self):
        name_pre_2020 = "National Heroes Day"
        name_2020 = "JAGS McCartney Day"
        
        self.assertHolidayName(
            name_2020,
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29", 
            "2024-05-27",
            "2025-05-26",
        )
        
        self.assertHolidayName(name_2020, range(2020, 2026))
        self.assertHolidayName(name_pre_2020, range(2000, 2020))
        self.assertNoHolidayName(name_pre_2020, range(2020, 2026))
        self.assertNoHolidayName(name_2020, range(2000, 2020))

    def test_sovereign_birthday(self):
        name_pre_2023 = "Queen's Birthday"
        name_2023 = "King's Birthday"
        
        self.assertHolidayName(
            name_pre_2023,
            "2020-06-08",
            "2021-06-14",
            "2022-06-13",
        )
        
        self.assertHolidayName(
            name_2023,
            "2023-06-12",
            "2024-06-10",
            "2025-06-09",
        )
        
        self.assertHolidayName(name_pre_2023, range(2000, 2023))
        self.assertHolidayName(name_2023, range(2023, 2026))
        self.assertNoHolidayName(name_pre_2023, range(2023, 2026))
        self.assertNoHolidayName(name_2023, range(2000, 2023))

    def test_national_youth_day(self):
        self.assertHolidayName(
            "National Youth Day",
            "2020-09-25",
            "2021-09-24",
            "2022-09-30",
            "2023-09-29",
            "2024-09-27",
            "2025-09-26",
        )

    def test_national_heritage_day(self):
        name_pre_2020 = "Columbus Day"
        name_2020 = "National Heritage Day"
        
        self.assertHolidayName(
            name_2020,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        
        self.assertHolidayName(name_2020, range(2020, 2026))
        self.assertHolidayName(name_pre_2020, range(2000, 2020))
        self.assertNoHolidayName(name_pre_2020, range(2020, 2026))
        self.assertNoHolidayName(name_2020, range(2000, 2020))

    def test_national_day_of_thanksgiving(self):
        self.assertHolidayName(
            "National Day of Thanksgiving",
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-29",
            "2025-11-28",
        )

    def test_2023(self):
        self.assertHolidayDates(
            TurksAndCaicosIslands(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-03-13", "Commonwealth Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-29", "JAGS McCartney Day"),
            ("2023-06-12", "King's Birthday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-09-29", "National Youth Day"),
            ("2023-10-09", "National Heritage Day"),
            ("2023-11-24", "National Day of Thanksgiving"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidayDates(
            TurksAndCaicosIslands(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-09", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-09", "King's Birthday"),
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
            ("2025-06-09", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
