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

from holidays.financial.budapest_stock_exchange import BudapestStockExchange
from tests.common import CommonFinancialTests


class TestBudapestStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BudapestStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_christmas_eve(self):
        name = "Szenteste"
        self.assertHolidayName(
            name,
            "1991-12-24",
            "1996-12-24",
            "2026-12-24",
            "2027-12-24",
            "2029-12-24",
            "2030-12-24",
        )
        self.assertNoHoliday(
            "1994-12-24",
            "1995-12-24",
            "2000-12-24",
            "2005-12-24",
            "2006-12-24",
            "2011-12-24",
            "2016-12-24",
            "2017-12-24",
            "2022-12-24",
            "2023-12-24",
            "2028-12-24",
        )

    def test_new_years_eve(self):
        name = "Szilveszter"
        self.assertHolidayName(
            name,
            "2019-12-31",
            "2020-12-31",
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHoliday(
            "1994-12-31",
            "1995-12-31",
            "2000-12-31",
            "2005-12-31",
            "2006-12-31",
            "2011-12-31",
            "2016-12-31",
            "2017-12-31",
            "2022-12-31",
            "2023-12-31",
        )

    def test_weekend_workdays_closed(self):
        self.assertEqual(len(self.holidays.weekend_workdays), 0)
        for dt in (
            "2021-12-11",
            "2025-05-17",
            "2025-10-18",
            "2025-12-13",
            "2026-01-10",
            "2026-08-08",
        ):
            self.assertFalse(self.holidays.is_working_day(dt))

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Újév"),
            ("2025-04-18", "Nagypéntek"),
            ("2025-04-21", "Húsvét Hétfő"),
            ("2025-05-01", "A Munka ünnepe"),
            ("2025-05-02", "Pihenőnap (2025. 05. 17.-től helyettesítve)"),
            ("2025-06-09", "Pünkösdhétfő"),
            ("2025-08-20", "Az államalapítás ünnepe"),
            ("2025-10-23", "Nemzeti ünnep"),
            ("2025-10-24", "Pihenőnap (2025. 10. 18.-től helyettesítve)"),
            ("2025-12-24", "Pihenőnap (2025. 12. 13.-től helyettesítve)"),
            ("2025-12-25", "Karácsony"),
            ("2025-12-26", "Karácsony másnapja"),
            ("2025-12-31", "Szilveszter"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Újév"),
            ("2026-01-02", "Pihenőnap (2026. 01. 10.-től helyettesítve)"),
            ("2026-04-03", "Nagypéntek"),
            ("2026-04-06", "Húsvét Hétfő"),
            ("2026-05-01", "A Munka ünnepe"),
            ("2026-05-25", "Pünkösdhétfő"),
            ("2026-08-20", "Az államalapítás ünnepe"),
            ("2026-08-21", "Pihenőnap (2026. 08. 08.-től helyettesítve)"),
            ("2026-10-23", "Nemzeti ünnep"),
            ("2026-12-24", "Szenteste"),
            ("2026-12-25", "Karácsony"),
            ("2026-12-31", "Szilveszter"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "Újév"),
            ("2026-01-02", "Pihenőnap (2026. 01. 10.-től helyettesítve)"),
            ("2026-04-03", "Nagypéntek"),
            ("2026-04-06", "Húsvét Hétfő"),
            ("2026-05-01", "A Munka ünnepe"),
            ("2026-05-25", "Pünkösdhétfő"),
            ("2026-08-20", "Az államalapítás ünnepe"),
            ("2026-08-21", "Pihenőnap (2026. 08. 08.-től helyettesítve)"),
            ("2026-10-23", "Nemzeti ünnep"),
            ("2026-12-24", "Szenteste"),
            ("2026-12-25", "Karácsony"),
            ("2026-12-31", "Szilveszter"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-01-02", "Day off (substituted from 01/10/2026)"),
            ("2026-04-03", "Good Friday"),
            ("2026-04-06", "Easter Monday"),
            ("2026-05-01", "Labor Day"),
            ("2026-05-25", "Pentecost Monday"),
            ("2026-08-20", "State Foundation Day"),
            ("2026-08-21", "Day off (substituted from 08/08/2026)"),
            ("2026-10-23", "National Day"),
            ("2026-12-24", "Christmas Eve"),
            ("2026-12-25", "Christmas Day"),
            ("2026-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2026-01-01", "Новий рік"),
            ("2026-01-02", "Вихідний день (перенесено з 10.01.2026)"),
            ("2026-04-03", "Страсна пʼятниця"),
            ("2026-04-06", "Великодній понеділок"),
            ("2026-05-01", "День праці"),
            ("2026-05-25", "Другий день Пʼятидесятниці"),
            ("2026-08-20", "День заснування держави"),
            ("2026-08-21", "Вихідний день (перенесено з 08.08.2026)"),
            ("2026-10-23", "Національне свято"),
            ("2026-12-24", "Святий вечір"),
            ("2026-12-25", "Різдво Христове"),
            ("2026-12-31", "Переддень Нового року"),
        )
