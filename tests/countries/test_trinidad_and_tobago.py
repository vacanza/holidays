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

from holidays.constants import OPTIONAL
from holidays.countries.trinidad_and_tobago import TrinidadAndTobago, TT, TTO
from tests.common import CommonCountryTests


class TestTrinidadAndTobago(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1963, 2050)
        super().setUpClass(TrinidadAndTobago, years=years)
        cls.no_estimated_holidays = TrinidadAndTobago(years=years, islamic_show_estimated=False)
        cls.optional_holidays = TrinidadAndTobago(categories=OPTIONAL, years=years)

    def test_country_aliases(self):
        self.assertAliases(TrinidadAndTobago, TT, TTO)

    def test_no_holidays(self):
        self.assertNoHolidays(TrinidadAndTobago(years=1962))
        self.assertNoHolidays(TrinidadAndTobago(categories=OPTIONAL, years=1962))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1963, 2050)))

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

    def test_spiritual_baptist_liberation_day(self):
        name = "Spiritual Baptist Liberation Day"
        self.assertHolidayName(name, (f"{year}-03-30" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, range(1963, 1996))

    def test_indian_arrival_day(self):
        name = "Indian Arrival Day"
        self.assertHolidayName(name, (f"{year}-05-30" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, range(1963, 1996))

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
        self.assertHolidayName(name, range(1963, 2050))

    def test_labor_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-06-19" for year in range(1973, 2050)))

    def test_african_emancipation_day(self):
        self.assertHolidayName(
            "African Emancipation Day", (f"{year}-08-01" for year in range(1985, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-08-31" for year in range(1963, 2050)))

    def test_republic_day(self):
        self.assertHolidayName("Republic Day", (f"{year}-09-24" for year in range(1976, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1963, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(1963, 2050)))

    def test_diwali(self):
        name = "Divali"
        self.assertHolidayName(
            name,
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, range(1963, 2050))

    def test_eid_al_fitr(self):
        name = "Eid-Ul-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1963, 2050))

    def test_carnival_monday(self):
        name = "Carnival Monday"
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1963, 2050))
        self.assertNoHolidayName(name)

    def test_carnival_tuesday(self):
        name = "Carnival Tuesday"
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
            "2025-03-04",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1963, 2050))
        self.assertNoHolidayName(name)

    def test_optional_2025(self):
        self.assertHolidays(
            TrinidadAndTobago(categories=OPTIONAL, years=2025),
            ("2025-03-03", "Carnival Monday"),
            ("2025-03-04", "Carnival Tuesday"),
        )

    def test_2024(self):
        self.assertHolidays(
            TrinidadAndTobago(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Spiritual Baptist Liberation Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid-Ul-Fitr"),
            ("2024-05-30", "Corpus Christi; Indian Arrival Day"),
            ("2024-06-19", "Labour Day"),
            ("2024-08-01", "African Emancipation Day"),
            ("2024-08-31", "Independence Day"),
            ("2024-09-24", "Republic Day"),
            ("2024-10-31", "Divali"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidays(
            TrinidadAndTobago(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-03-30", "Spiritual Baptist Liberation Day"),
            ("2025-03-31", "Eid-Ul-Fitr"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-30", "Indian Arrival Day"),
            ("2025-06-19", "Corpus Christi; Labour Day"),
            ("2025-08-01", "African Emancipation Day"),
            ("2025-08-31", "Independence Day"),
            ("2025-09-24", "Republic Day"),
            ("2025-10-20", "Divali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-03", "Carnival Monday"),
            ("2025-03-04", "Carnival Tuesday"),
            ("2025-03-30", "Spiritual Baptist Liberation Day"),
            ("2025-03-31", "Eid-Ul-Fitr"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-30", "Indian Arrival Day"),
            ("2025-06-19", "Corpus Christi; Labour Day"),
            ("2025-08-01", "African Emancipation Day"),
            ("2025-08-31", "Independence Day"),
            ("2025-09-24", "Republic Day"),
            ("2025-10-20", "Divali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-03", "Carnival Monday"),
            ("2025-03-04", "Carnival Tuesday"),
            ("2025-03-30", "Spiritual Baptist Liberation Day"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-30", "Indian Arrival Day"),
            ("2025-06-19", "Corpus Christi; Labor Day"),
            ("2025-08-01", "African Emancipation Day"),
            ("2025-08-31", "Independence Day"),
            ("2025-09-24", "Republic Day"),
            ("2025-10-20", "Diwali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
