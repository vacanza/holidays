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

import warnings
from unittest import TestCase

from holidays.constants import OPTIONAL, PUBLIC
from holidays.countries.portugal import Portugal, PT, PRT
from tests.common import CommonCountryTests


class TestPortugal(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Portugal, years=range(1910, 2050))

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_country_aliases(self):
        self.assertAliases(Portugal, PT, PRT)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_2014(self):
        # http://www.officeholidays.com/countries/portugal/2014.php
        self.assertHolidays(
            Portugal(years=2014),
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
            Portugal(years=2017),
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
        self.assertHoliday(Portugal(subdiv="30"), "2017-07-01", "2017-12-26")

    def test_azores_day(self):
        name = "Dia da Região Autónoma dos Açores"
        self.assertNoHolidayName(name, Portugal(years=1980, subdiv="20"))
        self.assertHolidayName(
            name,
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
        name_maco = "Dia da Região Autónoma da Madeira e das Comunidades Madeirenses"
        self.assertNoHolidayName(name_made, Portugal(years=1978, subdiv="30"))
        self.assertNoHolidayName(name_maco, Portugal(years=range(1978, 1989), subdiv="30"))
        self.assertNoHolidayName(name_made, Portugal(years=range(1989, 2050), subdiv="30"))
        self.assertHolidayName(
            name_maco,
            Portugal(years=range(2016, 2024), subdiv="30"),
            (f"{year}-07-01" for year in range(2016, 2024)),
        )

    def test_primeira_oitava(self):
        name = "Primeira Oitava"
        self.assertNoHolidayName(name, Portugal(years=2001, subdiv="30"))
        self.assertHolidayName(
            name,
            Portugal(years=range(2016, 2024), subdiv="30"),
            (f"{year}-12-26" for year in range(2016, 2024)),
        )

    def test_optional_holidays(self):
        holidays = Portugal(categories=OPTIONAL, years=range(2017, 2020))
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

    def test_deprecated(self):
        self.assertEqual(
            Portugal(subdiv="Ext", years=2022).keys(),
            Portugal(categories=(OPTIONAL, PUBLIC), years=2022).keys(),
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
        self.assertNoHolidayName(name, Portugal(years=1909))
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
        self.assertNoHolidayName(name, Portugal(years=1822))
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

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Ano Novo"),
            ("2018-02-13", "Carnaval"),
            ("2018-03-19", "Dia de São José"),
            ("2018-03-30", "Sexta-feira Santa"),
            ("2018-04-01", "Páscoa"),
            ("2018-04-17", "Dia de Nossa Senhora de Mércoles"),
            ("2018-04-25", "Dia da Liberdade"),
            ("2018-05-01", "Dia do Trabalhador"),
            ("2018-05-10", "Quinta-feira da Ascensão"),
            ("2018-05-12", "Dia de Santa Joana"),
            ("2018-05-21", "Dia da Região Autónoma dos Açores"),
            ("2018-05-22", "Dia do Município de Leiria"),
            ("2018-05-23", "Dia do Município de Portalegre"),
            ("2018-05-31", "Corpo de Deus"),
            ("2018-06-10", "Dia de Portugal, de Camões e das Comunidades Portuguesas"),
            ("2018-06-13", "Dia de Santo António"),
            ("2018-06-24", "Dia de São João"),
            ("2018-06-29", "Dia de São Pedro"),
            ("2018-07-01", "Dia da Região Autónoma da Madeira e das Comunidades Madeirenses"),
            ("2018-07-04", "Dia de Santa Isabel"),
            ("2018-08-15", "Assunção de Nossa Senhora"),
            ("2018-08-20", "Dia de Nossa Senhora da Agonia"),
            ("2018-08-22", "Dia de Nossa Senhora das Graças"),
            ("2018-09-07", "Dia do Município de Faro"),
            ("2018-09-15", "Dia de Bocage"),
            ("2018-09-21", "Dia de São Mateus"),
            ("2018-10-05", "Implantação da República"),
            ("2018-11-01", "Dia de Todos os Santos"),
            ("2018-11-27", "Dia do Município da Guarda"),
            ("2018-12-01", "Restauração da Independência"),
            ("2018-12-08", "Imaculada Conceição"),
            ("2018-12-24", "Véspera de Natal"),
            ("2018-12-25", "Dia de Natal"),
            ("2018-12-26", "26 de Dezembro; Primeira Oitava"),
            ("2018-12-31", "Véspera de Ano Novo"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-02-13", "Carnival"),
            ("2018-03-19", "Saint Joseph's Day"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-01", "Easter Sunday"),
            ("2018-04-17", "Feast of Our Lady of Mércoles"),
            ("2018-04-25", "Freedom Day"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-10", "Ascension Day"),
            ("2018-05-12", "Saint Joanna's Day"),
            ("2018-05-21", "Day of the Autonomous Region of the Azores"),
            ("2018-05-22", "Municipal Holiday of Leiria"),
            ("2018-05-23", "Municipal Holiday of Portalegre"),
            ("2018-05-31", "Corpus Christi"),
            ("2018-06-10", "Day of Portugal, Camões, and the Portuguese Communities"),
            ("2018-06-13", "Saint Anthony's Day"),
            ("2018-06-24", "Saint John's Day"),
            ("2018-06-29", "Saint Peter's Day"),
            ("2018-07-01", "Day of the Autonomous Region of Madeira and the Madeiran Communities"),
            ("2018-07-04", "Saint Elizabeth's Day"),
            ("2018-08-15", "Assumption Day"),
            ("2018-08-20", "Feast of Our Lady of Sorrows"),
            ("2018-08-22", "Feast of Our Lady of Graces"),
            ("2018-09-07", "Municipal Holiday of Faro"),
            ("2018-09-15", "Bocage Day"),
            ("2018-09-21", "Saint Matthew's Day"),
            ("2018-10-05", "Republic Day"),
            ("2018-11-01", "All Saints' Day"),
            ("2018-11-27", "Municipal Holiday of Guarda"),
            ("2018-12-01", "Restoration of Independence Day"),
            ("2018-12-08", "Immaculate Conception"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "1st Octave; Second Day of Christmas"),
            ("2018-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2018-01-01", "Новий рік"),
            ("2018-02-13", "Карнавал"),
            ("2018-03-19", "День Святого Йосипа"),
            ("2018-03-30", "Страсна пʼятниця"),
            ("2018-04-01", "Великдень"),
            ("2018-04-17", "День Богоматері Меркольської"),
            ("2018-04-25", "День Свободи"),
            ("2018-05-01", "День праці"),
            ("2018-05-10", "Вознесіння Господнє"),
            ("2018-05-12", "День Святої Йоанни"),
            ("2018-05-21", "День автономного регіону Азорських островів"),
            ("2018-05-22", "День муніципалітету Лейрія"),
            ("2018-05-23", "День муніципалітету Порталегре"),
            ("2018-05-31", "Свято Тіла і Крові Христових"),
            ("2018-06-10", "День Португалії, Камоенса і португальських громад"),
            ("2018-06-13", "День Святого Антонія"),
            ("2018-06-24", "День Святого Івана"),
            ("2018-06-29", "День Святого Петра"),
            ("2018-07-01", "День автономного регіону Мадейра та мадейрських громад"),
            ("2018-07-04", "День Святої Єлизавети"),
            ("2018-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2018-08-20", "День Богоматері Страждання"),
            ("2018-08-22", "День Богоматері Милосердя"),
            ("2018-09-07", "День муніципалітету Фару"),
            ("2018-09-15", "День Бокажі"),
            ("2018-09-21", "День Святого Матвія"),
            ("2018-10-05", "День Республіки"),
            ("2018-11-01", "День усіх святих"),
            ("2018-11-27", "День муніципалітету Гуарда"),
            ("2018-12-01", "День відновлення незалежності"),
            ("2018-12-08", "Непорочне зачаття Діви Марії"),
            ("2018-12-24", "Святий вечір"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "Другий день Різдва; Перша октава"),
            ("2018-12-31", "Переддень Нового року"),
        )
