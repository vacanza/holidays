#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.angola import AGO, AO, Angola
from test.common import TestCase


class TestAngola(TestCase):
    def setUp(self):
        self.holidays = Angola()

    def test_country_aliases(self):
        self.assertCountryAliases(Angola, AO, AGO)

    def test_carnival(self):
        self.assertHoliday(
            "1994-02-15",
            "2002-02-12",
            "2010-02-16",
            "2017-02-28",
            "2018-02-13",
            "2019-03-05",
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
        )

    def test_easter(self):
        self.assertHoliday(
            "1994-04-01",
            "2017-04-14",
            "2020-04-10",
        )

    def test_long_weekend(self):
        self.assertHoliday(
            "2019-04-05",
            "2020-02-03",
            "2050-03-07",
        )

    def test_national_hero_day(self):
        self.assertHoliday(f"{year}-09-17" for year in range(1980, 2030))

        self.assertNoHoliday(f"{year}-09-17" for year in range(1975, 1980))

    def test_national_liberation_day(self):
        self.assertHoliday(f"{year}-03-23" for year in range(2019, 2030))

        # Not a holiday before 2019.
        self.assertNoHoliday(f"{year}-03-23" for year in range(1990, 2019))

    def test_new_years_day(self):
        self.assertHoliday(
            "1975-01-01",
            "2017-01-01",
            "2017-01-02",  # Sunday.
            "2999-01-01",
        )

    def test_not_holidays(self):
        self.assertNoHoliday(
            "2015-03-02",
            "2016-12-28",
            "2018-03-23",
        )

    def test_pre_1975(self):
        self.assertNoHolidays(Angola(years=1974))

    def test_2022(self):
        self.assertHolidaysEqual(
            Angola(observed=False, years=2022),
            ("2022-01-01", "Ano novo"),
            ("2022-02-04", "Dia do Início da Luta Armada"),
            ("2022-03-01", "Carnaval"),
            ("2022-03-08", "Dia Internacional da Mulher"),
            ("2022-03-23", "Dia da Libertação da África Austral"),
            ("2022-04-04", "Dia da Paz e Reconciliação"),
            ("2022-04-15", "Sexta-feira Santa"),
            ("2022-05-01", "Dia Mundial do Trabalho"),
            ("2022-09-17", "Dia do Herói Nacional"),
            ("2022-11-02", "Dia dos Finados"),
            ("2022-11-11", "Dia da Independência"),
            ("2022-12-25", "Dia de Natal e da Família"),
        )

    def test_observed(self):
        for _, name in Angola(observed=False, years=2020).items():
            self.assertNotIn("Observed", name)
