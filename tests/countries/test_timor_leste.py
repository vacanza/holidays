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

from holidays.countries.timor_leste import TimorLeste
from tests.common import CommonCountryTests


class TestTimorLeste(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TimorLeste)

    def test_special_government_holidays(self):
        self.assertGovernmentHoliday(
            "2010-11-03",
            "2010-12-24",
            "2010-12-31",
            "2011-08-15",
            "2011-11-03",
            "2011-12-26",
            "2012-01-02",
            "2012-01-23",
            "2012-02-22",
            "2012-03-16",
            "2012-04-16",
            "2012-04-17",
            "2012-11-27",
            "2012-11-29",
            "2012-12-24",
            "2012-12-26",
            "2012-12-31",
            "2013-02-13",
            "2013-03-28",
            "2013-04-01",
            "2013-08-20",
            "2013-11-29",
            "2013-12-24",
            "2013-12-26",
            "2013-12-31",
            "2014-03-05",
            "2014-04-17",
            "2014-04-21",
            "2014-07-22",
            "2014-07-23",
            "2014-08-15",
            "2014-08-20",
            "2014-12-24",
            "2014-12-26",
            "2014-12-31",
            "2015-01-02",
            "2015-02-18",
            "2015-04-02",
            "2015-05-13",
            "2015-06-05",
            "2015-08-20",
            "2015-12-24",
            "2015-12-31",
            "2016-02-10",
            "2016-03-24",
            "2016-07-06",
            "2016-11-03",
            "2016-12-26",
            "2017-01-02",
            "2017-03-01",
            "2017-03-20",
            "2017-03-21",
            "2017-04-13",
            "2017-12-26",
            "2018-01-02",
            "2018-02-14",
            "2018-02-16",
            "2018-03-29",
            "2018-08-22",
            "2019-02-05",
            "2019-03-06",
            "2019-04-18",
            "2019-08-12",
            "2019-08-20",
            "2019-08-26",
            "2019-08-27",
            "2019-08-28",
            "2019-08-29",
            "2019-10-31",
            "2019-12-24",
            "2019-12-26",
            "2019-12-30",
            "2020-01-02",
            "2020-02-26",
            "2020-08-20",
            "2020-08-31",
            "2020-11-03",
            "2020-12-24",
            "2021-02-12",
            "2021-02-17",
            "2021-11-03",
            "2022-02-01",
            "2022-03-02",
            "2022-03-18",
            "2022-04-14",
            "2022-04-18",
            "2022-04-19",
            "2022-04-20",
            "2022-08-29",
            "2022-09-06",
            "2022-10-31",
            "2022-12-09",
            "2022-12-26",
            "2023-01-02",
            "2023-01-23",
            "2023-02-22",
            "2023-04-06",
            "2023-04-10",
            "2023-04-20",
            "2023-04-21",
            "2023-05-19",
            "2023-05-22",
            "2023-10-27",
            "2023-11-13",
            "2023-12-26",
            "2024-01-02",
            "2024-02-14",
            "2024-03-28",
            "2024-08-28",
            "2024-08-29",
            "2024-09-09",
            "2024-09-10",
            "2024-09-11",
            "2024-10-31",
            "2024-11-29",
            "2024-12-24",
            "2025-01-02",
            "2025-01-29",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Dia de Ano Novo", (f"{year}-01-01" for year in self.full_range))

    def test_veterans_day(self):
        name = "Dia dos Veteranos"
        self.assertHolidayName(name, (f"{year}-03-03" for year in range(2017, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_good_friday(self):
        name = "Sexta-Feira Santa"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_international_workers_day(self):
        self.assertHolidayName(
            "Dia Mundial do Trabalhador", (f"{year}-05-01" for year in self.full_range)
        )

    def test_restoration_of_independence_day(self):
        self.assertHolidayName(
            "Dia da Restauração da Independência", (f"{year}-05-20" for year in self.full_range)
        )

    def test_corpus_domini(self):
        name = "Festa do Corpo de Deus"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_popular_consultation_day(self):
        self.assertHolidayName(
            "Dia da Consulta Popular", (f"{year}-08-30" for year in self.full_range)
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Dia de Todos os Santos", (f"{year}-11-01" for year in self.full_range)
        )

    def test_all_souls_day(self):
        self.assertHolidayName(
            "Dia de Todos os Fiéis Defuntos", (f"{year}-11-02" for year in self.full_range)
        )

    def test_national_womens_day(self):
        name = "Dia Nacional da Mulher"
        self.assertHolidayName(name, (f"{year}-11-03" for year in range(2023, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2023))
        self.assertWorkdayHolidayName(
            name, (f"{year}-11-03" for year in range(self.start_year, 2023))
        )
        self.assertNoWorkdayHolidayName(name, range(2023, self.end_year))

    def test_national_youth_day(self):
        self.assertHolidayName(
            "Dia Nacional da Juventude", (f"{year}-11-12" for year in self.full_range)
        )

    def test_proclamation_of_independence_day(self):
        self.assertHolidayName(
            "Dia da Proclamação da Independência", (f"{year}-11-28" for year in self.full_range)
        )

    def test_memorial_day(self):
        name = "Dia da Memória"
        self.assertHolidayName(name, (f"{year}-12-07" for year in range(2017, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_day_of_our_lady_of_immaculate_conception_and_timor_leste_patroness(self):
        self.assertHolidayName(
            "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            (f"{year}-12-08" for year in self.full_range),
        )

    def test_christmas_day(self):
        self.assertHolidayName("Dia de Natal", (f"{year}-12-25" for year in self.full_range))

    def test_national_heroes_day(self):
        self.assertHolidayName(
            "Dia dos Heróis Nacionais",
            (f"{year}-12-07" for year in range(self.start_year, 2017)),
            (f"{year}-12-31" for year in range(2017, self.end_year)),
        )

    def test_eid_al_fitr(self):
        name = "Idul Fitri"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Idul Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-19",
            "2022-07-09",
            "2023-06-29",
            "2024-06-17",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_ash_wednesday(self):
        name = "Quarta-Feira de Cinzas"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name,
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
            "2025-03-05",
        )
        self.assertWorkdayHolidayName(name, self.full_range)

    def test_maundy_thursday(self):
        name = "Quinta-Feira Santa"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertWorkdayHolidayName(name, self.full_range)

    def test_the_day_of_ascension_of_jesus_christ_into_heaven(self):
        name = "Dia da Ascensão de Jesus Cristo ao Céu"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertWorkdayHolidayName(name, self.full_range)

    def test_international_childrens_day(self):
        name = "Dia Mundial da Criança"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-06-01" for year in self.full_range))

    def test_day_of_the_armed_forces_for_the_national_liberation_of_timor_leste_falintil(self):
        name = "Dia das Forças Armadas de Libertação Nacional de Timor-Leste (FALINTIL)"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-08-20" for year in self.full_range))

    def test_international_human_rights_day(self):
        name = "Dia Mundial dos Direitos Humanos"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-12-10" for year in self.full_range))

    def test_2011_public(self):
        # https://timor-leste.gov.tl/?p=4442&lang=en&lang=en
        self.assertHolidaysInYear(
            2011,
            ("2011-01-01", "Dia de Ano Novo"),
            ("2011-04-22", "Sexta-Feira Santa"),
            ("2011-05-01", "Dia Mundial do Trabalhador"),
            ("2011-05-20", "Dia da Restauração da Independência"),
            ("2011-06-23", "Festa do Corpo de Deus"),
            ("2011-08-30", "Dia da Consulta Popular"),
            ("2011-08-31", "Idul Fitri"),
            ("2011-11-01", "Dia de Todos os Santos"),
            ("2011-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2011-11-07", "Idul Adha"),
            ("2011-11-12", "Dia Nacional da Juventude"),
            ("2011-11-28", "Dia da Proclamação da Independência"),
            ("2011-12-07", "Dia dos Heróis Nacionais"),
            (
                "2011-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2011-12-25", "Dia de Natal"),
        )

    def test_2012_public(self):
        # https://timor-leste.gov.tl/?p=6269&lang=en
        self.assertHolidaysInYear(
            2012,
            ("2012-01-01", "Dia de Ano Novo"),
            ("2012-04-06", "Sexta-Feira Santa"),
            ("2012-05-01", "Dia Mundial do Trabalhador"),
            ("2012-05-20", "Dia da Restauração da Independência"),
            ("2012-06-07", "Festa do Corpo de Deus"),
            ("2012-08-20", "Idul Fitri"),
            ("2012-08-30", "Dia da Consulta Popular"),
            ("2012-10-26", "Idul Adha"),
            ("2012-11-01", "Dia de Todos os Santos"),
            ("2012-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2012-11-12", "Dia Nacional da Juventude"),
            ("2012-11-28", "Dia da Proclamação da Independência"),
            ("2012-12-07", "Dia dos Heróis Nacionais"),
            (
                "2012-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2012-12-25", "Dia de Natal"),
        )

    def test_2013_public(self):
        # https://timor-leste.gov.tl/?p=7627&lang=en&lang=en
        self.assertHolidaysInYear(
            2013,
            ("2013-01-01", "Dia de Ano Novo"),
            ("2013-03-29", "Sexta-Feira Santa"),
            ("2013-05-01", "Dia Mundial do Trabalhador"),
            ("2013-05-20", "Dia da Restauração da Independência"),
            ("2013-05-30", "Festa do Corpo de Deus"),
            ("2013-08-08", "Idul Fitri"),
            ("2013-08-30", "Dia da Consulta Popular"),
            ("2013-10-15", "Idul Adha"),
            ("2013-11-01", "Dia de Todos os Santos"),
            ("2013-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2013-11-12", "Dia Nacional da Juventude"),
            ("2013-11-28", "Dia da Proclamação da Independência"),
            ("2013-12-07", "Dia dos Heróis Nacionais"),
            (
                "2013-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2013-12-25", "Dia de Natal"),
        )

    def test_2014_public(self):
        # https://timor-leste.gov.tl/?p=9653&lang=en&lang=en
        self.assertHolidaysInYear(
            2014,
            ("2014-01-01", "Dia de Ano Novo"),
            ("2014-04-18", "Sexta-Feira Santa"),
            ("2014-05-01", "Dia Mundial do Trabalhador"),
            ("2014-05-20", "Dia da Restauração da Independência"),
            ("2014-06-19", "Festa do Corpo de Deus"),
            ("2014-07-28", "Idul Fitri"),
            ("2014-08-30", "Dia da Consulta Popular"),
            ("2014-10-04", "Idul Adha"),
            ("2014-11-01", "Dia de Todos os Santos"),
            ("2014-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2014-11-12", "Dia Nacional da Juventude"),
            ("2014-11-28", "Dia da Proclamação da Independência"),
            ("2014-12-07", "Dia dos Heróis Nacionais"),
            (
                "2014-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2014-12-25", "Dia de Natal"),
        )

    def test_2015_public(self):
        # https://timor-leste.gov.tl/?p=11331&lang=en&lang=en
        self.assertHolidaysInYear(
            2015,
            ("2015-01-01", "Dia de Ano Novo"),
            ("2015-04-03", "Sexta-Feira Santa"),
            ("2015-05-01", "Dia Mundial do Trabalhador"),
            ("2015-05-20", "Dia da Restauração da Independência"),
            ("2015-06-04", "Festa do Corpo de Deus"),
            ("2015-07-17", "Idul Fitri"),
            ("2015-08-30", "Dia da Consulta Popular"),
            ("2015-09-24", "Idul Adha"),
            ("2015-11-01", "Dia de Todos os Santos"),
            ("2015-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2015-11-12", "Dia Nacional da Juventude"),
            ("2015-11-28", "Dia da Proclamação da Independência"),
            ("2015-12-07", "Dia dos Heróis Nacionais"),
            (
                "2015-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2015-12-25", "Dia de Natal"),
        )

    def test_2016_public(self):
        # https://timor-leste.gov.tl/?p=14419&lang=en&lang=en
        self.assertHolidaysInYear(
            2016,
            ("2016-01-01", "Dia de Ano Novo"),
            ("2016-03-25", "Sexta-Feira Santa"),
            ("2016-05-01", "Dia Mundial do Trabalhador"),
            ("2016-05-20", "Dia da Restauração da Independência"),
            ("2016-05-26", "Festa do Corpo de Deus"),
            ("2016-07-07", "Idul Fitri"),
            ("2016-08-30", "Dia da Consulta Popular"),
            ("2016-09-18", "Idul Adha"),
            ("2016-11-01", "Dia de Todos os Santos"),
            ("2016-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2016-11-12", "Dia Nacional da Juventude"),
            ("2016-11-28", "Dia da Proclamação da Independência"),
            ("2016-12-07", "Dia dos Heróis Nacionais"),
            (
                "2016-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2016-12-25", "Dia de Natal"),
        )

    def test_2017_public(self):
        # https://timor-leste.gov.tl/?p=17138&lang=en&lang=en
        self.assertHolidaysInYear(
            2017,
            ("2017-01-01", "Dia de Ano Novo"),
            ("2017-03-03", "Dia dos Veteranos"),
            ("2017-04-14", "Sexta-Feira Santa"),
            ("2017-05-01", "Dia Mundial do Trabalhador"),
            ("2017-05-20", "Dia da Restauração da Independência"),
            ("2017-06-15", "Festa do Corpo de Deus"),
            ("2017-06-26", "Idul Fitri"),
            ("2017-08-30", "Dia da Consulta Popular"),
            ("2017-09-01", "Idul Adha"),
            ("2017-11-01", "Dia de Todos os Santos"),
            ("2017-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2017-11-12", "Dia Nacional da Juventude"),
            ("2017-11-28", "Dia da Proclamação da Independência"),
            ("2017-12-07", "Dia da Memória"),
            (
                "2017-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2017-12-25", "Dia de Natal"),
            ("2017-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2018_public(self):
        self.assertHolidaysInYear(
            2018,
            ("2018-01-01", "Dia de Ano Novo"),
            ("2018-03-03", "Dia dos Veteranos"),
            ("2018-03-30", "Sexta-Feira Santa"),
            ("2018-05-01", "Dia Mundial do Trabalhador"),
            ("2018-05-20", "Dia da Restauração da Independência"),
            ("2018-05-31", "Festa do Corpo de Deus"),
            ("2018-06-15", "Idul Fitri"),
            ("2018-08-21", "Idul Adha"),
            ("2018-08-30", "Dia da Consulta Popular"),
            ("2018-11-01", "Dia de Todos os Santos"),
            ("2018-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2018-11-12", "Dia Nacional da Juventude"),
            ("2018-11-28", "Dia da Proclamação da Independência"),
            ("2018-12-07", "Dia da Memória"),
            (
                "2018-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2018-12-25", "Dia de Natal"),
            ("2018-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2019_public(self):
        # https://timor-leste.gov.tl/?p=21146&lang=en&lang=en
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "Dia de Ano Novo"),
            ("2019-03-03", "Dia dos Veteranos"),
            ("2019-04-19", "Sexta-Feira Santa"),
            ("2019-05-01", "Dia Mundial do Trabalhador"),
            ("2019-05-20", "Dia da Restauração da Independência"),
            ("2019-06-06", "Idul Fitri"),
            ("2019-06-20", "Festa do Corpo de Deus"),
            ("2019-08-11", "Idul Adha"),
            ("2019-08-30", "Dia da Consulta Popular"),
            ("2019-11-01", "Dia de Todos os Santos"),
            ("2019-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2019-11-12", "Dia Nacional da Juventude"),
            ("2019-11-28", "Dia da Proclamação da Independência"),
            ("2019-12-07", "Dia da Memória"),
            (
                "2019-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2019-12-25", "Dia de Natal"),
            ("2019-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2020_public(self):
        # https://timor-leste.gov.tl/?p=23415&lang=en&lang=en
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "Dia de Ano Novo"),
            ("2020-03-03", "Dia dos Veteranos"),
            ("2020-04-10", "Sexta-Feira Santa"),
            ("2020-05-01", "Dia Mundial do Trabalhador"),
            ("2020-05-20", "Dia da Restauração da Independência"),
            ("2020-05-24", "Idul Fitri"),
            ("2020-06-11", "Festa do Corpo de Deus"),
            ("2020-07-31", "Idul Adha"),
            ("2020-08-30", "Dia da Consulta Popular"),
            ("2020-11-01", "Dia de Todos os Santos"),
            ("2020-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2020-11-12", "Dia Nacional da Juventude"),
            ("2020-11-28", "Dia da Proclamação da Independência"),
            ("2020-12-07", "Dia da Memória"),
            (
                "2020-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2020-12-25", "Dia de Natal"),
            ("2020-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2021_public(self):
        # https://timor-leste.gov.tl/?p=26494&lang=en&lang=en
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Dia de Ano Novo"),
            ("2021-03-03", "Dia dos Veteranos"),
            ("2021-04-02", "Sexta-Feira Santa"),
            ("2021-05-01", "Dia Mundial do Trabalhador"),
            ("2021-05-13", "Idul Fitri"),
            ("2021-05-20", "Dia da Restauração da Independência"),
            ("2021-06-03", "Festa do Corpo de Deus"),
            ("2021-07-19", "Idul Adha"),
            ("2021-08-30", "Dia da Consulta Popular"),
            ("2021-11-01", "Dia de Todos os Santos"),
            ("2021-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2021-11-12", "Dia Nacional da Juventude"),
            ("2021-11-28", "Dia da Proclamação da Independência"),
            ("2021-12-07", "Dia da Memória"),
            (
                "2021-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2021-12-25", "Dia de Natal"),
            ("2021-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2022_public(self):
        # https://timor-leste.gov.tl/?p=30266&lang=en
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Dia de Ano Novo"),
            ("2022-03-03", "Dia dos Veteranos"),
            ("2022-04-15", "Sexta-Feira Santa"),
            ("2022-05-01", "Dia Mundial do Trabalhador"),
            ("2022-05-02", "Idul Fitri"),
            ("2022-05-20", "Dia da Restauração da Independência"),
            ("2022-06-16", "Festa do Corpo de Deus"),
            ("2022-07-09", "Idul Adha"),
            ("2022-08-30", "Dia da Consulta Popular"),
            ("2022-11-01", "Dia de Todos os Santos"),
            ("2022-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2022-11-12", "Dia Nacional da Juventude"),
            ("2022-11-28", "Dia da Proclamação da Independência"),
            ("2022-12-07", "Dia da Memória"),
            (
                "2022-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2022-12-25", "Dia de Natal"),
            ("2022-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2023_public(self):
        # https://timor-leste.gov.tl/?p=31750&lang=en&lang=en
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "Dia de Ano Novo"),
            ("2023-03-03", "Dia dos Veteranos"),
            ("2023-04-07", "Sexta-Feira Santa"),
            ("2023-04-22", "Idul Fitri"),
            ("2023-05-01", "Dia Mundial do Trabalhador"),
            ("2023-05-20", "Dia da Restauração da Independência"),
            ("2023-06-08", "Festa do Corpo de Deus"),
            ("2023-06-29", "Idul Adha"),
            ("2023-08-30", "Dia da Consulta Popular"),
            ("2023-11-01", "Dia de Todos os Santos"),
            ("2023-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2023-11-03", "Dia Nacional da Mulher"),
            ("2023-11-12", "Dia Nacional da Juventude"),
            ("2023-11-28", "Dia da Proclamação da Independência"),
            ("2023-12-07", "Dia da Memória"),
            (
                "2023-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2023-12-25", "Dia de Natal"),
            ("2023-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2024_public(self):
        # https://timor-leste.gov.tl/?p=35833&lang=en&lang=en
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Dia de Ano Novo"),
            ("2024-03-03", "Dia dos Veteranos"),
            ("2024-03-29", "Sexta-Feira Santa"),
            ("2024-04-10", "Idul Fitri"),
            ("2024-05-01", "Dia Mundial do Trabalhador"),
            ("2024-05-20", "Dia da Restauração da Independência"),
            ("2024-05-30", "Festa do Corpo de Deus"),
            ("2024-06-17", "Idul Adha"),
            ("2024-08-30", "Dia da Consulta Popular"),
            ("2024-11-01", "Dia de Todos os Santos"),
            ("2024-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2024-11-03", "Dia Nacional da Mulher"),
            ("2024-11-12", "Dia Nacional da Juventude"),
            ("2024-11-28", "Dia da Proclamação da Independência"),
            ("2024-12-07", "Dia da Memória"),
            (
                "2024-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2024-12-25", "Dia de Natal"),
            ("2024-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2025_public(self):
        # https://timor-leste.gov.tl/?p=41492&lang=en
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Dia de Ano Novo"),
            ("2025-03-03", "Dia dos Veteranos"),
            ("2025-03-31", "Idul Fitri"),
            ("2025-04-18", "Sexta-Feira Santa"),
            ("2025-05-01", "Dia Mundial do Trabalhador"),
            ("2025-05-20", "Dia da Restauração da Independência"),
            ("2025-06-06", "Idul Adha"),
            ("2025-06-19", "Festa do Corpo de Deus"),
            ("2025-08-30", "Dia da Consulta Popular"),
            ("2025-11-01", "Dia de Todos os Santos"),
            ("2025-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2025-11-03", "Dia Nacional da Mulher"),
            ("2025-11-12", "Dia Nacional da Juventude"),
            ("2025-11-28", "Dia da Proclamação da Independência"),
            ("2025-12-07", "Dia da Memória"),
            (
                "2025-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2025-12-25", "Dia de Natal"),
            ("2025-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_2022_workday(self):
        self.assertWorkdayHolidaysInYear(
            2022,
            ("2022-03-02", "Quarta-Feira de Cinzas"),
            ("2022-04-14", "Quinta-Feira Santa"),
            ("2022-05-26", "Dia da Ascensão de Jesus Cristo ao Céu"),
            ("2022-06-01", "Dia Mundial da Criança"),
            (
                "2022-08-20",
                "Dia das Forças Armadas de Libertação Nacional de Timor-Leste (FALINTIL)",
            ),
            ("2022-11-03", "Dia Nacional da Mulher"),
            ("2022-12-10", "Dia Mundial dos Direitos Humanos"),
        )

    def test_2023_workday(self):
        self.assertWorkdayHolidaysInYear(
            2023,
            ("2023-02-22", "Quarta-Feira de Cinzas"),
            ("2023-04-06", "Quinta-Feira Santa"),
            ("2023-05-18", "Dia da Ascensão de Jesus Cristo ao Céu"),
            ("2023-06-01", "Dia Mundial da Criança"),
            (
                "2023-08-20",
                "Dia das Forças Armadas de Libertação Nacional de Timor-Leste (FALINTIL)",
            ),
            ("2023-12-10", "Dia Mundial dos Direitos Humanos"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Dia de Ano Novo"),
            ("2023-01-02", "Feriados Nacionais (Especiais)"),
            ("2023-01-23", "Feriados Nacionais (Especiais)"),
            ("2023-02-22", "Feriados Nacionais (Especiais); Quarta-Feira de Cinzas"),
            ("2023-03-03", "Dia dos Veteranos"),
            ("2023-04-06", "Feriados Nacionais (Especiais); Quinta-Feira Santa"),
            ("2023-04-07", "Sexta-Feira Santa"),
            ("2023-04-10", "Feriados Nacionais (Especiais)"),
            ("2023-04-20", "Feriados Nacionais (Especiais)"),
            ("2023-04-21", "Feriados Nacionais (Especiais)"),
            ("2023-04-22", "Idul Fitri"),
            ("2023-05-01", "Dia Mundial do Trabalhador"),
            ("2023-05-18", "Dia da Ascensão de Jesus Cristo ao Céu"),
            ("2023-05-19", "Dia de Eleições Parlamentares"),
            ("2023-05-20", "Dia da Restauração da Independência"),
            ("2023-05-22", "Dia de Eleições Parlamentares"),
            ("2023-06-01", "Dia Mundial da Criança"),
            ("2023-06-08", "Festa do Corpo de Deus"),
            ("2023-06-29", "Idul Adha"),
            (
                "2023-08-20",
                "Dia das Forças Armadas de Libertação Nacional de Timor-Leste (FALINTIL)",
            ),
            ("2023-08-30", "Dia da Consulta Popular"),
            ("2023-10-27", "Dia de eleições locais"),
            ("2023-11-01", "Dia de Todos os Santos"),
            ("2023-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2023-11-03", "Dia Nacional da Mulher"),
            ("2023-11-12", "Dia Nacional da Juventude"),
            ("2023-11-13", "Dia de eleições locais"),
            ("2023-11-28", "Dia da Proclamação da Independência"),
            ("2023-12-07", "Dia da Memória"),
            (
                "2023-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2023-12-10", "Dia Mundial dos Direitos Humanos"),
            ("2023-12-25", "Dia de Natal"),
            ("2023-12-26", "Feriados Nacionais (Especiais)"),
            ("2023-12-31", "Dia dos Heróis Nacionais"),
        )

    def test_l10n_en_tl(self):
        self.assertLocalizedHolidays(
            "en_TL",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "National Holidays (Special)"),
            ("2023-01-23", "National Holidays (Special)"),
            ("2023-02-22", "Ash Wednesday; National Holidays (Special)"),
            ("2023-03-03", "Veterans Day"),
            ("2023-04-06", "Holy Thursday; National Holidays (Special)"),
            ("2023-04-07", "Holy Friday"),
            ("2023-04-10", "National Holidays (Special)"),
            ("2023-04-20", "National Holidays (Special)"),
            ("2023-04-21", "National Holidays (Special)"),
            ("2023-04-22", "Idul Fitri"),
            ("2023-05-01", "World Labour Day"),
            ("2023-05-18", "The Day of Ascension of Jesus Christ into Heaven"),
            ("2023-05-19", "Parliamentary Election Day"),
            ("2023-05-20", "Restoration of Independence Day"),
            ("2023-05-22", "Parliamentary Election Day"),
            ("2023-06-01", "World Children's Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-29", "Idul Adha"),
            (
                "2023-08-20",
                "Day of the Armed Forces for the National Liberation of Timor-Leste (FALINTIL)",
            ),
            ("2023-08-30", "Popular Consultation Day"),
            ("2023-10-27", "Local Election Day"),
            ("2023-11-01", "All Saints Day"),
            ("2023-11-02", "All Souls Day"),
            ("2023-11-03", "National Women's Day"),
            ("2023-11-12", "National Youth Day"),
            ("2023-11-13", "Local Election Day"),
            ("2023-11-28", "Proclamation of Independence Day"),
            ("2023-12-07", "Memorial Day"),
            ("2023-12-08", "Day of Our Lady of Immaculate Conception and Timor-Leste Patroness"),
            ("2023-12-10", "World Human Rights Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "National Holidays (Special)"),
            ("2023-12-31", "National Heroes Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "National Holidays (Special)"),
            ("2023-01-23", "National Holidays (Special)"),
            ("2023-02-22", "Ash Wednesday; National Holidays (Special)"),
            ("2023-03-03", "Veteran's Day"),
            ("2023-04-06", "Maundy Thursday; National Holidays (Special)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "National Holidays (Special)"),
            ("2023-04-20", "National Holidays (Special)"),
            ("2023-04-21", "National Holidays (Special)"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-05-01", "International Worker's Day"),
            ("2023-05-18", "The Day of Ascension of Jesus Christ into Heaven"),
            ("2023-05-19", "Parliamentary Election Day"),
            ("2023-05-20", "Restoration of Independence Day"),
            ("2023-05-22", "Parliamentary Election Day"),
            ("2023-06-01", "International Children's Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-29", "Eid al-Adha"),
            (
                "2023-08-20",
                "Day of the Armed Forces for the National Liberation of Timor-Leste (FALINTIL)",
            ),
            ("2023-08-30", "Popular Consultation Day"),
            ("2023-10-27", "Local Election Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-11-03", "National Women's Day"),
            ("2023-11-12", "National Youth Day"),
            ("2023-11-13", "Local Election Day"),
            ("2023-11-28", "Proclamation of Independence Day"),
            ("2023-12-07", "Memorial Day"),
            ("2023-12-08", "Day of Our Lady of Immaculate Conception and Timor-Leste Patroness"),
            ("2023-12-10", "International Human Rights Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "National Holidays (Special)"),
            ("2023-12-31", "National Heroes Day"),
        )

    def test_l10n_tet(self):
        self.assertLocalizedHolidays(
            "tet",
            ("2023-01-01", "Loron Tinan-Foun nian"),
            ("2023-01-02", "Feriadu Nasional (Espesial)"),
            ("2023-01-23", "Feriadu Nasional (Espesial)"),
            ("2023-02-22", "Feriadu Nasional (Espesial); Kuarta-Feira Sinzas"),
            ("2023-03-03", "Loron Veteranu sira nian"),
            ("2023-04-06", "Feriadu Nasional (Espesial); Quinta-Feira Santa"),
            ("2023-04-07", "Sesta-Feira Santa"),
            ("2023-04-10", "Feriadu Nasional (Espesial)"),
            ("2023-04-20", "Feriadu Nasional (Espesial)"),
            ("2023-04-21", "Feriadu Nasional (Espesial)"),
            ("2023-04-22", "Idul-Fitri"),
            ("2023-05-01", "Loron Mundiál Serbisu-na'in sira nian"),
            ("2023-05-18", "Loron Ascensão do Senhor Jesus Cristo hi'it An ba Lalehan nian"),
            ("2023-05-19", "Loron Eleisaun Parlamentár nian"),
            ("2023-05-20", "Loron Restaurasaun Independénsia nian"),
            ("2023-05-22", "Loron Eleisaun Parlamentár nian"),
            ("2023-06-01", "Loron Mundial ba Labarik"),
            ("2023-06-08", "Festa Korpu de Deus"),
            ("2023-06-29", "Idul Adha"),
            ("2023-08-20", "Loron Forsa Armada Libertasaun Nasionál Timor-Leste (FALINTIL) nian"),
            ("2023-08-30", "Loron Konsulta Populár nian"),
            ("2023-10-27", "Loron eleisaun lokál nian"),
            ("2023-11-01", "Loron Santu sira Hotu nian"),
            ("2023-11-02", "Loron Matebian sira nian"),
            ("2023-11-03", "Loron Nasionál Feto"),
            ("2023-11-12", "Loron Nasionál Foin-Sa'e sira nian"),
            ("2023-11-13", "Loron eleisaun lokál nian"),
            ("2023-11-28", "Loron Proklamasaun Independénsia nian"),
            ("2023-12-07", "Loron Memória nian"),
            ("2023-12-08", "Loron Nossa Senhora da Imaculada Conceição, mahein Timor-Leste nian"),
            ("2023-12-10", "Loron Mundiál Direitu Umanu"),
            ("2023-12-25", "Loron Natál"),
            ("2023-12-26", "Feriadu Nasional (Espesial)"),
            ("2023-12-31", "Loron Eroi Nasionál sira nian"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2023-01-01", "วันขึ้นปีใหม่"),
            ("2023-01-02", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-01-23", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-02-22", "วันพุธรับเถ้า; วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-03-03", "วันทหารผ่านศึก"),
            ("2023-04-06", "วันพฤหัสศักดิ์สิทธิ์; วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-04-07", "วันศุกร์ประเสริฐ"),
            ("2023-04-10", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-04-20", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-04-21", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-04-22", "วันอีฎิ้ลฟิตริ"),
            ("2023-05-01", "วันแรงงานสากล"),
            ("2023-05-18", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2023-05-19", "วันเลือกตั้งสมาชิกรัฐสภา"),
            ("2023-05-20", "วันรำลึกการกอบกู้เอกราชติมอร์-เลสเต"),
            ("2023-05-22", "วันเลือกตั้งสมาชิกรัฐสภา"),
            ("2023-06-01", "วันเด็กสากล"),
            ("2023-06-08", "วันสมโภชพระคริสตวรกาย"),
            ("2023-06-29", "วันอีดิ้ลอัฎฮา"),
            ("2023-08-20", "วันกองกำลังปลดปล่อยแห่งชาติติมอร์-เลสเต (FALINTIL)"),
            ("2023-08-30", "วันรำลึกการลงประชามติเอกราช"),
            ("2023-10-27", "วันเลือกตั้งท้องถิ่น"),
            ("2023-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2023-11-02", "วันภาวนาอุทิศแด่ผู้ล่วงลับ"),
            ("2023-11-03", "วันสตรีแห่งชาติ"),
            ("2023-11-12", "วันเยาวชนแห่งชาติ"),
            ("2023-11-13", "วันเลือกตั้งท้องถิ่น"),
            ("2023-11-28", "วันประกาศเอกราชติมอร์-เลสเต"),
            ("2023-12-07", "วันรำลึกวีรชน"),
            ("2023-12-08", "วันสมโภชแม่พระผู้ปฏิสนธินิรมลและแม่พระองค์อุปถัมภ์แห่งติมอร์-เลสเต"),
            ("2023-12-10", "วันสิทธิมนุษยชนสากล"),
            ("2023-12-25", "วันคริสต์มาส"),
            ("2023-12-26", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2023-12-31", "วันวีรบุรุษแห่งชาติ"),
        )
