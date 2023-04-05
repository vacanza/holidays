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

from holidays.countries.angola import Angola, AO, AGO
from tests.common import TestCase


class TestAngola(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Angola)

    def test_country_aliases(self):
        self.assertCountryAliases(Angola, AO, AGO)

    def test_no_holidays(self):
        self.assertNoHolidays()
        self.assertNoHolidays(Angola(years=1974))

        self.assertNoNonObservedHolidays()
        self.assertNoNonObservedHolidays(Angola(observed=False, years=1974))

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
            # Good Friday
            "1994-04-01",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
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
        self.assertNoHolidayName(
            "Dia do Herói Nacional",
            Angola(years=range(1975, 1980)),
        )

    def test_national_liberation_day(self):
        self.assertHoliday(f"{year}-03-23" for year in range(2019, 2030))
        self.assertNoHoliday(f"{year}-03-23" for year in range(1990, 2019))
        self.assertNoHolidayName(
            "Dia da Libertação da África Austral",
            Angola(years=range(1975, 2019)),
        )

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

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Ano novo"),
            ("2022-02-04", "Dia do Início da Luta Armada"),
            ("2022-02-28", "Carnaval (Day off)"),
            ("2022-03-01", "Carnaval"),
            ("2022-03-07", "Dia Internacional da Mulher (Day off)"),
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
        dt = (
            # Ano novo
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2018-12-31",
            # Dia do Início da Luta Armada
            "2007-02-05",
            "2020-02-03",
            "2021-02-05",
            "2025-02-03",
            # Dia Internacional da Mulher
            "2009-03-09",
            "2015-03-09",
            "2018-03-09",
            "2022-03-07",
            # Dia da Libertação da África Austral
            "2021-03-22",
            "2023-03-24",
            # Dia da Paz e Reconciliação
            "2010-04-05",
            "2019-04-05",
            "2023-04-03",
            "2024-04-05",
            # Dia Mundial do Trabalho
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2018-04-30",
            "2025-05-02",
            # Dia do Herói Nacional
            "2006-09-18",
            "2017-09-18",
            "2019-09-16",
            "2020-09-18",
            "2024-09-16",
            # Dia dos Finados
            "2008-11-03",
            "2014-11-03",
            "2021-11-01",
            "2023-11-03",
            # Dia da Independência
            "2007-11-12",
            "2012-11-12",
            "2021-11-12",
            "2025-11-10",
            # Dia de Natal e da Família
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2018-12-24",
            "2025-12-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
