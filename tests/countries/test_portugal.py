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

from holidays.countries.portugal import Portugal, PT, PRT
from tests.common import TestCase


class TestPortugal(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Portugal)

    def setUp(self):
        super().setUp()

        years = range(1910, 2023)
        self.district_01 = Portugal(years=years, subdiv="01")
        self.district_02 = Portugal(years=years, subdiv="02")
        self.district_03 = Portugal(years=years, subdiv="03")
        self.district_04 = Portugal(years=years, subdiv="04")
        self.district_05 = Portugal(years=years, subdiv="05")
        self.district_06 = Portugal(years=years, subdiv="06")
        self.district_07 = Portugal(years=years, subdiv="07")
        self.district_08 = Portugal(years=years, subdiv="08")
        self.district_09 = Portugal(years=years, subdiv="09")
        self.district_10 = Portugal(years=years, subdiv="10")
        self.district_11 = Portugal(years=years, subdiv="11")
        self.district_12 = Portugal(years=years, subdiv="12")
        self.district_13 = Portugal(years=years, subdiv="13")
        self.district_14 = Portugal(years=years, subdiv="14")
        self.district_15 = Portugal(years=years, subdiv="15")
        self.district_16 = Portugal(years=years, subdiv="16")
        self.district_17 = Portugal(years=years, subdiv="17")
        self.district_18 = Portugal(years=years, subdiv="18")
        self.district_20 = Portugal(years=years, subdiv="20")
        self.district_30 = Portugal(years=years, subdiv="30")
        self.ext = Portugal(years=years, subdiv="Ext")

    def test_country_aliases(self):
        self.assertCountryAliases(Portugal, PT, PRT)

    def test_2014(self):
        # http://www.officeholidays.com/countries/portugal/2014.php
        self.assertHolidays(
            (
                "2014-01-01",
                "Ano Novo",
            ),
            (
                "2014-04-18",
                "Sexta-feira Santa",
            ),
            (
                "2014-04-20",
                "Páscoa",
            ),
            (
                "2014-04-25",
                "Dia da Liberdade",
            ),
            (
                "2014-05-01",
                "Dia do Trabalhador",
            ),
            (
                "2014-06-10",
                "Dia de Portugal, de Camões e das Comunidades Portuguesas",
            ),
            (
                "2014-08-15",
                "Assunção de Nossa Senhora",
            ),
            (
                "2014-12-08",
                "Imaculada Conceição",
            ),
            (
                "2014-12-25",
                "Dia de Natal",
            ),
        )

    def test_2017(self):
        # http://www.officeholidays.com/countries/portugal/2017.php
        self.assertHolidays(
            (
                "2017-01-01",
                "Ano Novo",
            ),
            (
                "2017-04-14",
                "Sexta-feira Santa",
            ),
            (
                "2017-04-16",
                "Páscoa",
            ),
            (
                "2017-04-25",
                "Dia da Liberdade",
            ),
            (
                "2017-05-01",
                "Dia do Trabalhador",
            ),
            (
                "2017-06-10",
                "Dia de Portugal, de Camões e das Comunidades Portuguesas",
            ),
            (
                "2017-06-15",
                "Corpo de Deus",
            ),
            (
                "2017-08-15",
                "Assunção de Nossa Senhora",
            ),
            (
                "2017-10-05",
                "Implantação da República",
            ),
            (
                "2017-11-01",
                "Dia de Todos os Santos",
            ),
            (
                "2017-12-01",
                "Restauração da Independência",
            ),
            (
                "2017-12-08",
                "Imaculada Conceição",
            ),
            (
                "2017-12-25",
                "Dia de Natal",
            ),
        )

    def test_district_specific_days(self):
        # Conselho Holidays only starts in 1911
        self.assertNotIn("1910-05-12", self.district_01)
        self.assertNotIn("1910-05-05", self.district_02)
        self.assertNotIn("1910-06-24", self.district_03)
        self.assertNotIn("1910-08-22", self.district_04)
        self.assertNotIn("1910-04-12", self.district_05)
        self.assertNotIn("1910-07-04", self.district_06)
        self.assertNotIn("1910-06-29", self.district_07)
        self.assertNotIn("1910-09-07", self.district_08)
        self.assertNotIn("1910-11-27", self.district_09)
        self.assertNotIn("1910-05-22", self.district_10)
        self.assertNotIn("1910-06-13", self.district_11)
        self.assertNotIn("1910-05-23", self.district_12)
        self.assertNotIn("1910-06-24", self.district_13)
        self.assertNotIn("1910-03-19", self.district_14)
        self.assertNotIn("1910-09-15", self.district_15)
        self.assertNotIn("1910-08-20", self.district_16)
        self.assertNotIn("1910-06-13", self.district_17)
        self.assertNotIn("1910-09-21", self.district_18)
        self.assertNotIn("1910-05-16", self.district_20)
        self.assertNotIn("1910-07-01", self.district_30)
        self.assertNotIn("1910-12-26", self.district_30)

        # 2017 Cases
        self.assertHoliday(self.district_01, "2017-05-12")
        self.assertHoliday(self.district_02, "2017-05-25")
        self.assertHoliday(self.district_03, "2017-06-24")
        self.assertHoliday(self.district_04, "2017-08-22")
        self.assertHoliday(self.district_05, "2017-05-02")
        self.assertHoliday(self.district_06, "2017-07-04")
        self.assertHoliday(self.district_07, "2017-06-29")
        self.assertHoliday(self.district_08, "2017-09-07")
        self.assertHoliday(self.district_09, "2017-11-27")
        self.assertHoliday(self.district_10, "2017-05-22")
        self.assertHoliday(self.district_11, "2017-06-13")
        self.assertHoliday(self.district_12, "2017-05-23")
        self.assertHoliday(self.district_13, "2017-06-24")
        self.assertHoliday(self.district_14, "2017-03-19")
        self.assertHoliday(self.district_15, "2017-09-15")
        self.assertHoliday(self.district_16, "2017-08-20")
        self.assertHoliday(self.district_17, "2017-06-13")
        self.assertHoliday(self.district_18, "2017-09-21")
        self.assertHoliday(self.district_20, "2017-06-05")
        self.assertHoliday(self.district_30, "2017-07-01")
        self.assertHoliday(self.district_30, "2017-12-26")

    def test_azores_day(self):
        name = "Dia da Região Autónoma dos Açores"

        self.assertNoHolidayName(name, Portugal(years=1980, subdiv="20"))
        self.assertHoliday(
            self.district_20,
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
        name_maco = (
            "Dia da Região Autónoma da Madeira e das Comunidades Madeirenses"
        )

        self.assertNoHolidayName(name_made, Portugal(years=1978, subdiv="30"))
        self.assertNoHolidayName(
            name_maco,
            Portugal(years=range(1978, 1989), subdiv="30"),
        )
        self.assertNoHolidayName(
            name_made,
            Portugal(years=range(1989, 2050), subdiv="30"),
        )
        self.assertHoliday(
            self.district_30,
            "2016-07-01",
            "2017-07-01",
            "2018-07-01",
            "2019-07-01",
            "2020-07-01",
            "2021-07-01",
            "2022-07-01",
            "2023-07-01",
        )

    def test_primeira_oitava(self):
        name = "Primeira Oitava"

        self.assertNoHolidayName(name, Portugal(years=2001, subdiv="30"))
        self.assertHoliday(
            self.district_30,
            "2016-12-26",
            "2017-12-26",
            "2018-12-26",
            "2019-12-26",
            "2020-12-26",
            "2021-12-26",
            "2022-12-26",
            "2023-12-26",
        )

    def test_ext(self):
        # Christmas's Eve, S. Stephen & New Year's Eve
        self.assertHoliday(
            self.ext,
            "2017-12-24",
            "2017-12-26",
            "2017-12-31",
            "2017-12-24",
            "2017-12-26",
            "2017-12-31",
            "2018-12-24",
            "2018-12-26",
            "2018-12-31",
            "2019-12-24",
            "2019-12-26",
            "2019-12-31",
        )

    def test_corpus_christi(self):
        name = "Corpo de Deus"

        self.assertNoHolidayName(name, Portugal(years=range(2013, 2016)))
        self.assertHoliday(
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

        self.assertNoHolidayName(name, Portugal(years=1909))
        self.assertHoliday(f"{year}-10-05" for year in range(1910, 2013))
        self.assertNoHolidayName(name, Portugal(years=range(2013, 2016)))
        self.assertHoliday(f"{year}-10-05" for year in range(2016, 2050))

    def test_all_saints_day(self):
        name = "Dia de Todos os Santos"

        self.assertHoliday(f"{year}-11-01" for year in range(1950, 2013))
        self.assertNoHolidayName(name, Portugal(years=range(2013, 2016)))
        self.assertHoliday(f"{year}-11-01" for year in range(2016, 2050))

    def test_restoration_of_independence_day(self):
        name = "Restauração da Independência"

        self.assertNoHolidayName(name, Portugal(years=1822))
        self.assertHoliday(f"{year}-12-01" for year in range(1823, 2013))
        self.assertNoHolidayName(name, Portugal(years=range(2013, 2016)))
        self.assertHoliday(f"{year}-12-01" for year in range(2016, 2050))

    def test_freedom_day(self):
        name = "Dia da Liberdade"

        self.assertNoHolidayName(name, Portugal(years=1973))
        self.assertHoliday(f"{year}-04-25" for year in range(1974, 2050))

    def test_labour_day(self):
        name = "Dia do Trabalhador"

        self.assertNoHolidayName(name, Portugal(years=1973))
        self.assertHoliday(f"{year}-05-01" for year in range(1974, 2050))

    def test_portugal_day(self):
        name_def = "Dia de Portugal"
        name_esno = "Dia de Camões, de Portugal e da Raça"
        name_carn = "Dia de Portugal, de Camões e das Comunidades Portuguesas"

        self.assertNoHolidayName(name_def, Portugal(years=1910))
        self.assertNoHolidayName(name_esno, Portugal(years=1910))
        self.assertNoHolidayName(name_carn, Portugal(years=1910))
        self.assertHoliday(f"{year}-06-10" for year in range(1911, 2050))
        self.assertNoHolidayName(name_esno, Portugal(years=range(1911, 1933)))
        self.assertNoHolidayName(name_carn, Portugal(years=range(1911, 1978)))
        self.assertNoHolidayName(name_def, Portugal(years=range(1933, 1974)))
        self.assertNoHolidayName(name_def, Portugal(years=range(1978, 2050)))
        self.assertNoHolidayName(name_esno, Portugal(years=range(1978, 2050)))

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                pt = Portugal(language=language)
                self.assertEqual(pt["2017-01-01"], "Ano Novo")
                self.assertEqual(pt["2017-12-25"], "Dia de Natal")

        run_tests((Portugal.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Portugal.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        pt = Portugal(language=en_us)
        self.assertEqual(pt["2017-01-01"], "New Year's Day")
        self.assertEqual(pt["2017-12-25"], "Christmas")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            pt = Portugal(language=language)
            self.assertEqual(pt["2017-01-01"], "New Year's Day")
            self.assertEqual(pt["2017-12-25"], "Christmas")
