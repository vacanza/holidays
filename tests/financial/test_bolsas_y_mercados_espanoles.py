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

from holidays.financial.bolsas_y_mercados_espanoles import BolsasYMercadosEspanoles
from tests.common import CommonFinancialTests


class TestBolsasYMercadosEspanoles(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BolsasYMercadosEspanoles)

    def test_new_years_day(self):
        name = "Año Nuevo"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-01-01",
            "2021-01-01",
            "2024-01-01",
            "2025-01-01",
            "2026-01-01",
        )
        self.assertNoHoliday(
            "2022-01-01",
            "2023-01-01",
            "2022-01-03",
            "2023-01-02",
        )

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Lunes de Pascua"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Día del Trabajo"
        self.assertNonObservedHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-05-01",
            "2023-05-01",
            "2024-05-01",
            "2025-05-01",
            "2026-05-01",
        )
        self.assertNoHoliday(
            "2021-05-01",
            "2022-05-01",
            "2021-05-03",
            "2022-05-02",
        )

    def test_christmas_day(self):
        name = "Navidad"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2020-12-25",
            "2023-12-25",
            "2024-12-25",
            "2025-12-25",
            "2026-12-25",
        )
        self.assertNoHoliday(
            "2021-12-25",
            "2022-12-25",
            "2021-12-27",
        )

    def test_boxing_day_and_san_esteban(self):
        name = "Boxing Day & San Esteban"
        self.assertNonObservedHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2022-12-26",
            "2023-12-26",
            "2024-12-26",
            "2025-12-26",
        )
        self.assertNoHoliday(
            "2020-12-26",
            "2021-12-26",
            "2026-12-26",
            "2020-12-28",
            "2021-12-28",
        )

    def test_christmas_eve(self):
        name = "Nochebuena (los mercados cierran a las 14:00 CET)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-24" for year in self.full_range)
        )
        self.assertHalfDayHolidayName(
            name,
            "2020-12-24",
            "2021-12-24",
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2022-12-24",
            "2023-12-24",
        )

    def test_new_years_eve(self):
        name = "Nochevieja (los mercados cierran a las 14:00 CET)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-31" for year in self.full_range)
        )
        self.assertHalfDayHolidayName(
            name,
            "2020-12-31",
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2022-12-31",
            "2023-12-31",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Año Nuevo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-04-21", "Lunes de Pascua"),
            ("2025-05-01", "Día del Trabajo"),
            ("2025-12-25", "Navidad"),
            ("2025-12-26", "Boxing Day & San Esteban"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-12-24", "Nochebuena (los mercados cierran a las 14:00 CET)"),
            ("2025-12-31", "Nochevieja (los mercados cierran a las 14:00 CET)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-04-01", "Lunes de Pascua"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-12-24", "Nochebuena (los mercados cierran a las 14:00 CET)"),
            ("2024-12-25", "Navidad"),
            ("2024-12-26", "Boxing Day & San Esteban"),
            ("2024-12-31", "Nochevieja (los mercados cierran a las 14:00 CET)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labor Day"),
            ("2024-12-24", "Christmas Eve (markets close at 14:00 CET)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day & Saint Stephen's Day"),
            ("2024-12-31", "New Year's Eve (markets close at 14:00 CET)"),
        )
