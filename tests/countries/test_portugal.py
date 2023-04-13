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
        super().setUpClass(Portugal, years=range(1910, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Portugal, PT, PRT)

    def test_2014(self):
        # http://www.officeholidays.com/countries/portugal/2014.php
        self.assertHolidays(
            Portugal(years=2014),
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
            Portugal(years=2017),
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
        self.assertNoHoliday(Portugal(subdiv="01"), "1910-05-12")
        self.assertNoHoliday(Portugal(subdiv="02"), "1910-05-05")
        self.assertNoHoliday(Portugal(subdiv="03"), "1910-06-24")
        self.assertNoHoliday(Portugal(subdiv="04"), "1910-08-22")
        self.assertNoHoliday(Portugal(subdiv="05"), "1910-04-12")
        self.assertNoHoliday(Portugal(subdiv="06"), "1910-07-04")
        self.assertNoHoliday(Portugal(subdiv="07"), "1910-06-29")
        self.assertNoHoliday(Portugal(subdiv="08"), "1910-09-07")
        self.assertNoHoliday(Portugal(subdiv="09"), "1910-11-27")
        self.assertNoHoliday(Portugal(subdiv="10"), "1910-05-22")
        self.assertNoHoliday(Portugal(subdiv="11"), "1910-06-13")
        self.assertNoHoliday(Portugal(subdiv="12"), "1910-05-23")
        self.assertNoHoliday(Portugal(subdiv="13"), "1910-06-24")
        self.assertNoHoliday(Portugal(subdiv="14"), "1910-03-19")
        self.assertNoHoliday(Portugal(subdiv="15"), "1910-09-15")
        self.assertNoHoliday(Portugal(subdiv="16"), "1910-08-20")
        self.assertNoHoliday(Portugal(subdiv="17"), "1910-06-13")
        self.assertNoHoliday(Portugal(subdiv="18"), "1910-09-21")
        self.assertNoHoliday(Portugal(subdiv="20"), "1910-05-16")
        self.assertNoHoliday(Portugal(subdiv="30"), "1910-07-01")
        self.assertNoHoliday(Portugal(subdiv="30"), "1910-12-26")

        # 2017 Cases
        self.assertHoliday(Portugal(subdiv="01"), "2017-05-12")
        self.assertHoliday(Portugal(subdiv="02"), "2017-05-25")
        self.assertHoliday(Portugal(subdiv="03"), "2017-06-24")
        self.assertHoliday(Portugal(subdiv="04"), "2017-08-22")
        self.assertHoliday(Portugal(subdiv="05"), "2017-05-02")
        self.assertHoliday(Portugal(subdiv="06"), "2017-07-04")
        self.assertHoliday(Portugal(subdiv="07"), "2017-06-29")
        self.assertHoliday(Portugal(subdiv="08"), "2017-09-07")
        self.assertHoliday(Portugal(subdiv="09"), "2017-11-27")
        self.assertHoliday(Portugal(subdiv="10"), "2017-05-22")
        self.assertHoliday(Portugal(subdiv="11"), "2017-06-13")
        self.assertHoliday(Portugal(subdiv="12"), "2017-05-23")
        self.assertHoliday(Portugal(subdiv="13"), "2017-06-24")
        self.assertHoliday(Portugal(subdiv="14"), "2017-03-19")
        self.assertHoliday(Portugal(subdiv="15"), "2017-09-15")
        self.assertHoliday(Portugal(subdiv="16"), "2017-08-20")
        self.assertHoliday(Portugal(subdiv="17"), "2017-06-13")
        self.assertHoliday(Portugal(subdiv="18"), "2017-09-21")
        self.assertHoliday(Portugal(subdiv="20"), "2017-06-05")
        self.assertHoliday(Portugal(subdiv="30"), "2017-07-01")
        self.assertHoliday(Portugal(subdiv="30"), "2017-12-26")

    def test_azores_day(self):
        name = "Dia da Região Autónoma dos Açores"

        self.assertNoHolidayName(name, Portugal(years=1980, subdiv="20"))
        self.assertHoliday(
            Portugal(years=range(2016, 2024), subdiv="20"),
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
            Portugal(years=range(2016, 2024), subdiv="30"),
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
            Portugal(years=range(2016, 2024), subdiv="30"),
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
            Portugal(years=range(2017, 2020), subdiv="Ext"),
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

        self.assertNoHolidayNameInYears(name, range(2013, 2016))
        self.assertHolidaysName(
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

        self.assertNoHolidayName(name, Portugal(years=1909))
        self.assertHoliday(f"{year}-10-05" for year in range(1910, 2013))
        self.assertNoHolidayNameInYears(name, range(2013, 2016))
        self.assertHoliday(f"{year}-10-05" for year in range(2016, 2050))

    def test_all_saints_day(self):
        name = "Dia de Todos os Santos"

        self.assertHoliday(f"{year}-11-01" for year in range(1950, 2013))
        self.assertNoHolidayNameInYears(name, range(2013, 2016))
        self.assertHoliday(f"{year}-11-01" for year in range(2016, 2050))

    def test_restoration_of_independence_day(self):
        name = "Restauração da Independência"

        self.assertNoHolidayName(name, Portugal(years=1822))
        self.assertHoliday(f"{year}-12-01" for year in range(1823, 2013))
        self.assertNoHolidayNameInYears(name, range(2013, 2016))
        self.assertHoliday(f"{year}-12-01" for year in range(2016, 2050))

    def test_freedom_day(self):
        name = "Dia da Liberdade"

        self.assertNoHolidayNameInYears(name, 1973)
        self.assertHoliday(f"{year}-04-25" for year in range(1974, 2050))

    def test_labour_day(self):
        name = "Dia do Trabalhador"

        self.assertNoHolidayNameInYears(name, 1973)
        self.assertHoliday(f"{year}-05-01" for year in range(1974, 2050))

    def test_portugal_day(self):
        name_def = "Dia de Portugal"
        name_esno = "Dia de Camões, de Portugal e da Raça"
        name_carn = "Dia de Portugal, de Camões e das Comunidades Portuguesas"

        self.assertNoHolidayNameInYears(name_def, 1910)
        self.assertNoHolidayNameInYears(name_esno, 1910)
        self.assertNoHolidayNameInYears(name_carn, 1910)
        self.assertHoliday(f"{year}-06-10" for year in range(1911, 2050))
        self.assertNoHolidayNameInYears(name_esno, range(1911, 1933))
        self.assertNoHolidayNameInYears(name_carn, range(1911, 1978))
        self.assertNoHolidayNameInYears(name_def, range(1933, 1974))
        self.assertNoHolidayNameInYears(name_def, range(1978, 2050))
        self.assertNoHolidayNameInYears(name_esno, range(1978, 2050))

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
