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

from holidays.financial.warsaw_stock_exchange import WarsawStockExchange
from tests.common import CommonFinancialTests


class TestWarsawStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(WarsawStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_no_holidays(self):
        self.assertNoHolidays(WarsawStockExchange(years=self.start_year - 1))

    def test_special_holidays(self):
        self.assertHolidayName("Dzień bez sesji", "2013-04-16", "2018-01-02")

    def test_inherited_special_holiday(self):
        self.assertHolidayName("Narodowe Święto Niepodległości - 100-lecie", "2018-11-12")

    def test_good_friday(self):
        name = "Wielki Piątek"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_eve(self):
        self.assertHolidayName(
            "Wigilia Bożego Narodzenia", (f"{year}-12-24" for year in self.full_range)
        )

    def test_new_years_eve(self):
        self.assertHolidayName("Sylwester", (f"{year}-12-31" for year in self.full_range))

    def test_non_session_weekdays(self):
        # Weekday closures in the yearly resolutions of the GPW Management Board.
        for year, dates in (
            (
                2023,
                (
                    "2023-01-06",
                    "2023-04-07",
                    "2023-04-10",
                    "2023-05-01",
                    "2023-05-03",
                    "2023-06-08",
                    "2023-08-15",
                    "2023-11-01",
                    "2023-12-25",
                    "2023-12-26",
                ),
            ),
            (
                2024,
                (
                    "2024-01-01",
                    "2024-03-29",
                    "2024-04-01",
                    "2024-05-01",
                    "2024-05-03",
                    "2024-05-30",
                    "2024-08-15",
                    "2024-11-01",
                    "2024-11-11",
                    "2024-12-24",
                    "2024-12-25",
                    "2024-12-26",
                    "2024-12-31",
                ),
            ),
            (
                2025,
                (
                    "2025-01-01",
                    "2025-01-06",
                    "2025-04-18",
                    "2025-04-21",
                    "2025-05-01",
                    "2025-06-19",
                    "2025-08-15",
                    "2025-11-11",
                    "2025-12-24",
                    "2025-12-25",
                    "2025-12-26",
                    "2025-12-31",
                ),
            ),
            (
                2026,
                (
                    "2026-01-01",
                    "2026-01-06",
                    "2026-04-03",
                    "2026-04-06",
                    "2026-05-01",
                    "2026-06-04",
                    "2026-11-11",
                    "2026-12-24",
                    "2026-12-25",
                    "2026-12-31",
                ),
            ),
            (
                2027,
                (
                    "2027-01-01",
                    "2027-01-06",
                    "2027-03-26",
                    "2027-03-29",
                    "2027-05-03",
                    "2027-05-27",
                    "2027-11-01",
                    "2027-11-11",
                    "2027-12-24",
                    "2027-12-31",
                ),
            ),
        ):
            weekdays = [
                str(dt) for dt in sorted(WarsawStockExchange(years=year)) if dt.weekday() < 5
            ]
            self.assertEqual(list(dates), weekdays, year)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Nowy Rok"),
            ("2018-01-02", "Dzień bez sesji"),
            ("2018-01-06", "Święto Trzech Króli"),
            ("2018-03-30", "Wielki Piątek"),
            ("2018-04-01", "Niedziela Wielkanocna"),
            ("2018-04-02", "Poniedziałek Wielkanocny"),
            ("2018-05-01", "Święto Państwowe"),
            ("2018-05-03", "Święto Narodowe Trzeciego Maja"),
            ("2018-05-20", "Zielone Świątki"),
            ("2018-05-31", "Dzień Bożego Ciała"),
            ("2018-08-15", "Wniebowzięcie Najświętszej Marii Panny"),
            ("2018-11-01", "Uroczystość Wszystkich Świętych"),
            ("2018-11-11", "Narodowe Święto Niepodległości"),
            ("2018-11-12", "Narodowe Święto Niepodległości - 100-lecie"),
            ("2018-12-24", "Wigilia Bożego Narodzenia"),
            ("2018-12-25", "Boże Narodzenie (pierwszy dzień)"),
            ("2018-12-26", "Boże Narodzenie (drugi dzień)"),
            ("2018-12-31", "Sylwester"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-01-02", "Non-trading day"),
            ("2018-01-06", "Epiphany"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-01", "Easter Sunday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-05-01", "National Day"),
            ("2018-05-03", "National Day of the Third of May"),
            ("2018-05-20", "Pentecost"),
            ("2018-05-31", "Corpus Christi"),
            ("2018-08-15", "Assumption Day"),
            ("2018-11-01", "All Saints' Day"),
            ("2018-11-11", "National Independence Day"),
            ("2018-11-12", "National Independence Day - 100th anniversary"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Second Day of Christmas"),
            ("2018-12-31", "New Year's Eve"),
        )
