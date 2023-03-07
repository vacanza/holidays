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

        years = range(2014, 2018)
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

    def test_ext_2017(self):
        # Christmas's Eve, S. Stephen & New Year's Eve
        self.assertHoliday(
            self.ext,
            "2017-12-24",
            "2017-12-26",
            "2017-12-31",
        )

    def test_district_specific_days_2017(self):
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
