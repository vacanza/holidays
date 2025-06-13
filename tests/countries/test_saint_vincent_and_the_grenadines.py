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

    def test_no_holidays_before_start(self):
        self.assertNoHolidays(SaintVincentAndTheGrenadines(years=1978))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1979, 2050)))
        observed = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", observed)
        self.assertNoNonObservedHoliday(observed)

    def test_national_heroes_day(self):
        name = "National Heroes' Day"
        self.assertHolidayName(
            name,
            (f"{year}-03-14" for year in range(1979, 2050)),
        )
        self.assertHolidayName(f"{name} (observed)", ["2021-03-15"])
        self.assertNoNonObservedHoliday(["2021-03-15"])

    def test_national_workers_day(self):
        name = "National Workers' Day"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in range(1979, 2050)),
        )
        observed = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", observed)
        self.assertNoNonObservedHoliday(observed)

    def test_good_friday_and_easter_monday(self):
        self.assertHolidayName("Good Friday", range(1979, 2050))
        self.assertHolidayName("Easter Monday", range(1979, 2050))

    def test_spiritual_baptist_day(self):
        name = "National Spiritual Baptist Day"
        self.assertHolidayName(name, (f"{year}-05-21" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1979, 2025))

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(name, range(1979, 2050))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1979, 2050)))
        self.assertHolidayName(f"{name} (observed)", ["2021-08-02"])
        self.assertNoNonObservedHoliday(["2021-08-02"])

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-10-27" for year in range(1979, 2050)))
        self.assertHolidayName(f"{name} (observed)", ["2024-10-28"])
        self.assertNoNonObservedHoliday(["2024-10-28"])

    def test_christmas_and_boxing_day(self):
        name_christmas = "Christmas Day"
        name_boxing = "Boxing Day"
        self.assertHolidayName(name_christmas, (f"{year}-12-25" for year in range(1979, 2050)))
        self.assertHolidayName(name_boxing, (f"{year}-12-26" for year in range(1979, 2050)))

        dt_chrismas = ("2022-12-27",)
        self.assertHolidayName(f"{name_christmas} (observed)", dt_chrismas)
        self.assertNoNonObservedHoliday(dt_chrismas)
        dt_boxing = ("2021-12-27",)
        self.assertHolidayName(f"{name_boxing} (observed)", dt_boxing)
        self.assertNoNonObservedHoliday(dt_boxing)

    def test_2024_holidays(self):
        self.assertHolidays(
            SaintVincentAndTheGrenadines(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-14", "National Heroes' Day"),
            ("2024-04-07", "Good Friday"),
            ("2024-04-10", "Easter Monday"),
            ("2024-05-01", "National Workers' Day"),
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
            ("2023-03-14", "National Heroes' Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "National Workers' Day"),
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
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-03-14", "National Heroes' Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-07-10", "Carnival Monday"),
            ("2023-07-11", "Carnival Tuesday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-10-27", "Independence Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
