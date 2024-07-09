#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import OPTIONAL
from holidays.entities.ISO_3166.PT import PtHolidays
from tests.common import CommonCountryTests


class TestPtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PtHolidays, years=range(1910, 2050))

    def test_2014(self):
        # http://www.officeholidays.com/countries/portugal/2014.php
        self.assertHolidays(
            PtHolidays(years=2014),
            ("2014-01-01", "Ano Novo"),
            ("2014-04-18", "Sexta-feira Santa"),
            ("2014-04-20", "Páscoa"),
            ("2014-04-25", "Dia da Liberdade"),
            ("2014-05-01", "Dia do Trabalhador"),
            ("2014-06-10", "Dia de Portugal, de Camões e das Comunidades Portuguesas"),
            ("2014-08-15", "Assunção de Nossa Senhora"),
            ("2014-12-08", "Imaculada Conceição"),
            ("2014-12-25", "Dia de Natal"),
        )

    def test_2017(self):
        # http://www.officeholidays.com/countries/portugal/2017.php
        self.assertHolidays(
            PtHolidays(years=2017),
            ("2017-01-01", "Ano Novo"),
            ("2017-04-14", "Sexta-feira Santa"),
            ("2017-04-16", "Páscoa"),
            ("2017-04-25", "Dia da Liberdade"),
            ("2017-05-01", "Dia do Trabalhador"),
            ("2017-06-10", "Dia de Portugal, de Camões e das Comunidades Portuguesas"),
            ("2017-06-15", "Corpo de Deus"),
            ("2017-08-15", "Assunção de Nossa Senhora"),
            ("2017-10-05", "Implantação da República"),
            ("2017-11-01", "Dia de Todos os Santos"),
            ("2017-12-01", "Restauração da Independência"),
            ("2017-12-08", "Imaculada Conceição"),
            ("2017-12-25", "Dia de Natal"),
        )

    def test_district_specific_days(self):
        # Conselho Holidays only starts in 1911
        self.assertNoHoliday(PtHolidays(subdiv="01"), "1910-05-12")
        self.assertNoHoliday(PtHolidays(subdiv="02"), "1910-05-05")
        self.assertNoHoliday(PtHolidays(subdiv="03"), "1910-06-24")
        self.assertNoHoliday(PtHolidays(subdiv="04"), "1910-08-22")
        self.assertNoHoliday(PtHolidays(subdiv="05"), "1910-04-12")
        self.assertNoHoliday(PtHolidays(subdiv="06"), "1910-07-04")
        self.assertNoHoliday(PtHolidays(subdiv="07"), "1910-06-29")
        self.assertNoHoliday(PtHolidays(subdiv="08"), "1910-09-07")
        self.assertNoHoliday(PtHolidays(subdiv="09"), "1910-11-27")
        self.assertNoHoliday(PtHolidays(subdiv="10"), "1910-05-22")
        self.assertNoHoliday(PtHolidays(subdiv="11"), "1910-06-13")
        self.assertNoHoliday(PtHolidays(subdiv="12"), "1910-05-23")
        self.assertNoHoliday(PtHolidays(subdiv="13"), "1910-06-24")
        self.assertNoHoliday(PtHolidays(subdiv="14"), "1910-03-19")
        self.assertNoHoliday(PtHolidays(subdiv="15"), "1910-09-15")
        self.assertNoHoliday(PtHolidays(subdiv="16"), "1910-08-20")
        self.assertNoHoliday(PtHolidays(subdiv="17"), "1910-06-13")
        self.assertNoHoliday(PtHolidays(subdiv="18"), "1910-09-21")
        self.assertNoHoliday(PtHolidays(subdiv="20"), "1910-05-16")
        self.assertNoHoliday(PtHolidays(subdiv="30"), "1910-07-01")
        self.assertNoHoliday(PtHolidays(subdiv="30"), "1910-12-26")

        # 2017 Cases
        self.assertHoliday(PtHolidays(subdiv="01"), "2017-05-12")
        self.assertHoliday(PtHolidays(subdiv="02"), "2017-05-25")
        self.assertHoliday(PtHolidays(subdiv="03"), "2017-06-24")
        self.assertHoliday(PtHolidays(subdiv="04"), "2017-08-22")
        self.assertHoliday(PtHolidays(subdiv="05"), "2017-05-02")
        self.assertHoliday(PtHolidays(subdiv="06"), "2017-07-04")
        self.assertHoliday(PtHolidays(subdiv="07"), "2017-06-29")
        self.assertHoliday(PtHolidays(subdiv="08"), "2017-09-07")
        self.assertHoliday(PtHolidays(subdiv="09"), "2017-11-27")
        self.assertHoliday(PtHolidays(subdiv="10"), "2017-05-22")
        self.assertHoliday(PtHolidays(subdiv="11"), "2017-06-13")
        self.assertHoliday(PtHolidays(subdiv="12"), "2017-05-23")
        self.assertHoliday(PtHolidays(subdiv="13"), "2017-06-24")
        self.assertHoliday(PtHolidays(subdiv="14"), "2017-03-19")
        self.assertHoliday(PtHolidays(subdiv="15"), "2017-09-15")
        self.assertHoliday(PtHolidays(subdiv="16"), "2017-08-20")
        self.assertHoliday(PtHolidays(subdiv="17"), "2017-06-13")
        self.assertHoliday(PtHolidays(subdiv="18"), "2017-09-21")
        self.assertHoliday(PtHolidays(subdiv="20"), "2017-06-05")
        self.assertHoliday(PtHolidays(subdiv="30"), "2017-07-01", "2017-12-26")

    def test_azores_day(self):
        name = "Dia da Região Autónoma dos Açores"
        self.assertNoHolidayName(name, PtHolidays(years=1980, subdiv="20"))
        self.assertHolidayName(
            name,
            PtHolidays(years=range(2016, 2024), subdiv="20"),
            "2016-05-16",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
        )

    def test_madeira_day(self):
        name_made = "Dia da Região Autónoma da Madeira"
        name_maco = "Dia da Região Autónoma da Madeira e das Comunidades Madeirenses"
        self.assertNoHolidayName(name_made, PtHolidays(years=1978, subdiv="30"))
        self.assertNoHolidayName(name_maco, PtHolidays(years=range(1978, 1989), subdiv="30"))
        self.assertNoHolidayName(name_made, PtHolidays(years=range(1989, 2050), subdiv="30"))
        self.assertHolidayName(
            name_maco,
            PtHolidays(years=range(2016, 2024), subdiv="30"),
            (f"{year}-07-01" for year in range(2016, 2024)),
        )

    def test_primeira_oitava(self):
        name = "Primeira Oitava"
        self.assertNoHolidayName(name, PtHolidays(years=2001, subdiv="30"))
        self.assertHolidayName(
            name,
            PtHolidays(years=range(2016, 2024), subdiv="30"),
            (f"{year}-12-26" for year in range(2016, 2024)),
        )

    def test_optional_holidays(self):
        holidays = PtHolidays(categories=OPTIONAL, years=range(2017, 2020))
        self.assertHoliday(
            holidays,
            "2017-02-28",
            "2017-06-13",
            "2017-12-24",
            "2017-12-26",
            "2017-12-31",
            "2018-02-13",
            "2018-06-13",
            "2018-12-24",
            "2018-12-26",
            "2018-12-31",
            "2019-03-05",
            "2019-06-13",
            "2019-12-24",
            "2019-12-26",
            "2019-12-31",
        )

    def test_corpus_christi(self):
        name = "Corpo de Deus"
        self.assertNoHolidayName(name, range(2013, 2016))
        self.assertHolidayName(
            name,
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
        )

    def test_republic_day(self):
        name = "Implantação da República"
        self.assertNoHolidayName(name, PtHolidays(years=1909))
        self.assertHolidayName(
            name,
            (f"{year}-10-05" for year in set(range(1910, 2013)).difference({2013, 2014, 2015})),
        )
        self.assertNoHolidayName(name, range(2013, 2016))

    def test_all_saints_day(self):
        name = "Dia de Todos os Santos"
        self.assertHolidayName(
            name,
            (f"{year}-11-01" for year in set(range(1910, 2013)).difference({2013, 2014, 2015})),
        )
        self.assertNoHolidayName(name, range(2013, 2016))

    def test_restoration_of_independence_day(self):
        name = "Restauração da Independência"
        self.assertNoHolidayName(name, PtHolidays(years=1822))
        self.assertHolidayName(
            name,
            (f"{year}-12-01" for year in set(range(1910, 2013)).difference({2013, 2014, 2015})),
        )
        self.assertNoHolidayName(name, range(2013, 2016))

    def test_freedom_day(self):
        name = "Dia da Liberdade"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1974, 2050)))
        self.assertNoHolidayName(name, range(1910, 1974))

    def test_labour_day(self):
        name = "Dia do Trabalhador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1974, 2050)))
        self.assertNoHolidayName(name, range(1910, 1974))

    def test_portugal_day(self):
        name_def = "Dia de Portugal"
        name_esno = "Dia de Camões, de Portugal e da Raça"
        name_carn = "Dia de Portugal, de Camões e das Comunidades Portuguesas"

        self.assertNoHolidayName(name_def, 1910)
        self.assertNoHolidayName(name_esno, 1910)
        self.assertNoHolidayName(name_carn, 1910)
        self.assertHoliday(f"{year}-06-10" for year in range(1911, 2050))
        self.assertNoHolidayName(name_def, range(1933, 1974), range(1978, 2050))
        self.assertNoHolidayName(name_esno, range(1911, 1933), range(1974, 2050))
        self.assertNoHolidayName(name_carn, range(1911, 1978))
