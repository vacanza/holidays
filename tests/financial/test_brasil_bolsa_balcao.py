#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import datetime as dt
from unittest import TestCase

from dateutil.easter import easter

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, SEP, OCT, NOV, DEC
from holidays.financial.brasil_bolsa_balcao import BrasilBolsaBalcao, BVMF, B3
from tests.common import CommonFinancialTests


class TestBrasilBolsaBalcao(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BrasilBolsaBalcao)

    def test_market_aliases(self):
        self.assertAliases(BrasilBolsaBalcao, BVMF, B3)

    def test_no_holidays(self):
        self.assertNoHolidays(BrasilBolsaBalcao(years=1889))

    def test_new_years_day(self):
        holiday_name = "Confraternização Universal"

        self.assertHolidayName(
            holiday_name,
            (dt.date(year, JAN, 1) for year in range(1890, 2100)),
        )

    def test_carnival_monday(self):
        holiday_name = "Carnaval"

        for date in (
            dt.date(2020, FEB, 24),
            dt.date(2021, FEB, 15),
            dt.date(2022, FEB, 28),
            dt.date(2023, FEB, 20),
            dt.date(2024, FEB, 12),
        ):
            self.assertHolidayName(holiday_name, date)

    def test_carnival_thursday(self):
        holiday_name = "Carnaval"

        for date in (
            dt.date(2020, FEB, 25),
            dt.date(2021, FEB, 16),
            dt.date(2022, MAR, 1),
            dt.date(2023, FEB, 21),
            dt.date(2024, FEB, 13),
        ):
            self.assertHolidayName(holiday_name, date)

    def test_holy_thursday(self):
        holiday_name = "Quinta-feira Santa"

        for i in range(1890, 2000):
            e = easter(i)
            self.assertHolidayName(holiday_name, e - dt.timedelta(days=3))

        self.assertNoHolidayName(
            holiday_name,
            (dt.date(year, APR, 21) for year in range(2000, 2100)),
        )

    def test_good_friday(self):
        holiday_name = "Sexta-feira Santa"

        for date in (
            dt.date(2020, APR, 10),
            dt.date(2021, APR, 2),
            dt.date(2022, APR, 15),
            dt.date(2023, APR, 7),
            dt.date(2024, MAR, 29),
        ):
            self.assertHolidayName(holiday_name, date)

    def test_tiradentes_day(self):
        holiday_name = "Tiradentes"

        self.assertHolidayName(
            holiday_name,
            (dt.date(year, APR, 21) for year in range(1890, 1931)),
        )
        self.assertNoHolidayName(
            holiday_name,
            (dt.date(year, APR, 21) for year in {1931, 1932}),
        )
        self.assertHolidayName(
            holiday_name,
            (dt.date(year, APR, 21) for year in range(1933, 2100)),
        )

    def test_labor_day(self):
        holiday_name = "Dia do Trabalhador"

        self.assertNoHolidayName(
            holiday_name,
            (dt.date(year, MAY, 1) for year in range(1890, 1925)),
        )
        self.assertHolidayName(
            holiday_name,
            (dt.date(year, MAY, 1) for year in range(1925, 2100)),
        )

    def test_corpus_christi_day(self):
        holiday_name = "Corpus Christi"

        for date in (
            dt.date(2020, JUN, 11),
            dt.date(2021, JUN, 3),
            dt.date(2022, JUN, 16),
            dt.date(2023, JUN, 8),
            dt.date(2024, MAY, 30),
        ):
            self.assertHolidayName(holiday_name, date)

    def test_independence_day(self):
        holiday_name = "Independência do Brasil"

        self.assertHolidayName(
            holiday_name,
            (dt.date(year, SEP, 7) for year in range(1890, 2100)),
        )

    def test_our_lady_of_aparecida(self):
        holiday_name = "Nossa Senhora Aparecida"

        self.assertHolidayName(
            holiday_name,
            (dt.date(year, OCT, 12) for year in range(1890, 1931)),
        )
        self.assertNoHolidayName(
            holiday_name,
            (dt.date(year, OCT, 12) for year in range(1931, 1980)),
        )
        self.assertHolidayName(
            holiday_name,
            (dt.date(year, OCT, 12) for year in range(1980, 2100)),
        )

    def test_all_souls_day(self):
        holiday_name = "Finados"

        self.assertHolidayName(
            holiday_name,
            (dt.date(year, NOV, 2) for year in range(1890, 2100)),
        )

    def test_republic_proclamation_day(self):
        holiday_name = "Proclamação da República"

        self.assertHolidayName(
            holiday_name,
            (dt.date(year, NOV, 15) for year in range(1890, 2100)),
        )

    def test_national_day_of_zumbi_and_black_awareness(self):
        holiday_name = "Dia Nacional de Zumbi e da Consciência Negra"

        self.assertNoHolidayName(
            holiday_name,
            (dt.date(year, NOV, 20) for year in range(1890, 2024)),
        )
        self.assertHolidayName(
            holiday_name,
            (dt.date(year, NOV, 20) for year in range(2024, 2100)),
        )

    def test_christmas_day(self):
        holiday_name = "Natal"

        self.assertNoHolidayName(
            holiday_name,
            (dt.date(year, DEC, 25) for year in range(1890, 1922)),
        )
        self.assertHolidayName(
            holiday_name,
            (dt.date(year, DEC, 25) for year in range(1922, 2100)),
        )
