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

from holidays.countries.saint_vincent_and_the_grenadines import (
    SaintVincentAndTheGrenadines,
    VC,
    VCT,
)
from tests.common import CommonCountryTests


class TestSaintVincentAndTheGrenadines(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1979, 2050)
        super().setUpClass(SaintVincentAndTheGrenadines, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(SaintVincentAndTheGrenadines, VC, VCT)

    def test_no_holidays(self):
        self.assertNoHolidays(SaintVincentAndTheGrenadines(years=1978))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1979, 2050)))
        dt = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_workers_day(self):
        name = "National Workers Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1979, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1979, 2050)))
        dt = (
            "2021-08-02",
            "2027-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2024(self):
        self.assertHolidays(
            SaintVincentAndTheGrenadines(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-14", "National Heroes Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "National Workers Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-07-08", "Carnival Monday"),
            ("2024-07-09", "Carnival Tuesday"),
            ("2024-08-01", "Emancipation Day"),
            ("2024-10-27", "Independence Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-03-14", "National Heroes Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "National Workers Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-07-10", "Carnival Monday"),
            ("2023-07-11", "Carnival Tuesday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-10-27", "Independence Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-14", "National Heroes Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-07-08", "Carnival Monday"),
            ("2024-07-09", "Carnival Tuesday"),
            ("2024-08-01", "Emancipation Day"),
            ("2024-10-27", "Independence Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
