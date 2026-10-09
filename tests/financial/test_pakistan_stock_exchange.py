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

from holidays.financial.pakistan_stock_exchange import PakistanStockExchange
from tests.common import CommonFinancialTests


class TestPakistanStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PakistanStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_juma_tul_wida(self):
        name = "Juma-tul-Wida"
        self.assertHolidayName(
            name,
            "2020-05-22",
            "2021-05-07",
            "2022-04-29",
            "2023-04-14",
            "2024-04-05",
            "2025-03-28",
            "2026-03-20",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-04-05", "Juma-tul-Wida"),
            ("2024-04-10", "Eid-ul-Fitr"),
            ("2024-04-11", "Eid-ul-Fitr"),
            ("2024-04-12", "Eid-ul-Fitr"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid-ul-Adha"),
            ("2024-06-18", "Eid-ul-Adha"),
            ("2024-06-19", "Eid-ul-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-09-17", "Eid Milad-un-Nabi"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-12-25", "Quaid-e-Azam Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-02-05", "Kashmir Solidarity Day"),
            ("2024-03-23", "Pakistan Day"),
            ("2024-04-05", "Jumu'atul-Wida"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr"),
            ("2024-04-12", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-28", "Youm-e-Takbeer"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-06-18", "Eid al-Adha"),
            ("2024-06-19", "Eid al-Adha"),
            ("2024-07-15", "Ashura"),
            ("2024-07-16", "Ashura"),
            ("2024-08-14", "Independence Day"),
            ("2024-09-17", "Prophet's Birthday"),
            ("2024-11-09", "Iqbal Day"),
            ("2024-12-25", "Quaid-e-Azam Day"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2024-02-05", "یوم یکجہتی کشمیر"),
            ("2024-03-23", "یوم پاکستان"),
            ("2024-04-05", "جمعۃ الوداع"),
            ("2024-04-10", "عید الفطر"),
            ("2024-04-11", "عید الفطر"),
            ("2024-04-12", "عید الفطر"),
            ("2024-05-01", "یوم مزدور"),
            ("2024-05-28", "یوم تکبیر"),
            ("2024-06-17", "عید الاضحی"),
            ("2024-06-18", "عید الاضحی"),
            ("2024-06-19", "عید الاضحی"),
            ("2024-07-15", "عاشورہ"),
            ("2024-07-16", "عاشورہ"),
            ("2024-08-14", "یوم آزادی"),
            ("2024-09-17", "عید میلاد النبی"),
            ("2024-11-09", "یوم اقبال"),
            ("2024-12-25", "یوم قائداعظم"),
        )
