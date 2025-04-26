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

from unittest import TestCase

from holidays.countries.turks_and_caicos_islands import TurksAndCaicosIslands, TC, TCA
from tests.common import CommonCountryTests


class TestTC(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TurksAndCaicosIslands, years=range(2020, 2025))

    def test_country_aliases(self):
        self.assertAliases(TurksAndCaicosIslands, TC, TCA)

    def test_2023(self):
        self.assertHolidayDates(
            TurksAndCaicosIslands(years=2023),
            "2023-01-01",  # New Year's Day
            "2023-03-13",  # Commonwealth Day (2nd Monday in March)
            "2023-04-07",  # Good Friday
            "2023-04-10",  # Easter Monday
            "2023-05-29",  # JAGS McCartney Day (last Monday in May)
            "2023-06-12",  # King's Birthday (2nd Monday in June)
            "2023-08-01",  # Emancipation Day
            "2023-09-29",  # National Youth Day (last Friday in September)
            "2023-10-09",  # National Heritage Day (2nd Monday in October)
            "2023-11-24",  # National Day of Thanksgiving (4th Friday in November)
            "2023-12-25",  # Christmas Day
            "2023-12-26",  # Boxing Day
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
