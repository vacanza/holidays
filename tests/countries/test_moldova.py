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

from holidays.countries.moldova import Moldova, MD, MDA
from tests.common import CommonCountryTests


class TestMoldova(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Moldova)

    def test_country_aliases(self):
        self.assertAliases(Moldova, MD, MDA)

    def test_no_holidays(self):
        self.assertNoHolidays(Moldova(years=1990))

    def test_christmas(self):
        name_old1 = "Nașterea lui Iisus Hristos (Crăciunul)"
        name_old2 = "Nașterea lui Iisus Hristos (Crăciunul pe stil vechi)"
        name_new = "Nașterea lui Iisus Hristos (Crăciunul pe stil nou)"
        self.assertHolidayName(name_old1, (f"{year}-01-07" for year in range(1991, 2014)))
        self.assertNoHolidayName(name_old1, Moldova(years=2014))
        self.assertHolidayName(name_old2, (f"{year}-01-07" for year in range(2014, 2031)))
        self.assertNoHolidayName(name_old2, Moldova(years=2013))

        self.assertHolidayName(name_new, (f"{year}-12-25" for year in range(2013, 2031)))
        self.assertNoHolidayName(name_new, Moldova(years=2012))

    def test_europe_day(self):
        name = "Ziua Europei"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(2017, 2031)))
        self.assertNoHolidayName(name, Moldova(years=2016))

    def test_childrens_day(self):
        name = "Ziua Ocrotirii Copilului"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2016, 2031)))
        self.assertNoHolidayName(name, Moldova(years=2015))

    def test_2022(self):
        self.assertHolidayDates(
            Moldova(years=2022),
            "2022-01-01",
            "2022-01-07",
            "2022-01-08",
            "2022-03-08",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-05-02",
            "2022-05-09",
            "2022-06-01",
            "2022-08-27",
            "2022-08-31",
            "2022-12-25",
        )

    def test_2023(self):
        self.assertHolidayDates(
            Moldova(years=2023),
            "2023-01-01",
            "2023-01-07",
            "2023-01-08",
            "2023-03-08",
            "2023-04-16",
            "2023-04-17",
            "2023-04-24",
            "2023-05-01",
            "2023-05-09",
            "2023-06-01",
            "2023-08-27",
            "2023-08-31",
            "2023-12-25",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Anul Nou"),
            ("2022-01-07", "Nașterea lui Iisus Hristos (Crăciunul pe stil vechi)"),
            ("2022-01-08", "Nașterea lui Iisus Hristos (Crăciunul pe stil vechi)"),
            ("2022-03-08", "Ziua internatională a femeii"),
            ("2022-04-24", "Paștele"),
            ("2022-04-25", "Paștele"),
            ("2022-05-01", "Ziua internaţională a solidarităţii oamenilor muncii"),
            ("2022-05-02", "Paștele blajinilor"),
            (
                "2022-05-09",
                "Ziua Europei; Ziua Victoriei și a comemorării eroilor "
                "căzuţi pentru Independenţa Patriei",
            ),
            ("2022-06-01", "Ziua Ocrotirii Copilului"),
            ("2022-08-27", "Ziua independenţei Republicii Moldova"),
            ("2022-08-31", "Limba noastră"),
            ("2022-12-25", "Nașterea lui Iisus Hristos (Crăciunul pe stil nou)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-07", "Christmas Day (by old style)"),
            ("2022-01-08", "Christmas Day (by old style)"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-24", "Easter"),
            ("2022-04-25", "Easter"),
            ("2022-05-01", "International Workers' Solidarity Day"),
            ("2022-05-02", "Day of Rejoicing"),
            (
                "2022-05-09",
                "Europe Day; Victory Day and Commemoration of the heroes "
                "fallen for Independence of Fatherland",
            ),
            ("2022-06-01", "International Children's Day"),
            ("2022-08-27", "Republic of Moldova Independence Day"),
            ("2022-08-31", "National Language Day"),
            ("2022-12-25", "Christmas Day (by new style)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-07", "Різдво Христове (за старим стилем)"),
            ("2022-01-08", "Різдво Христове (за старим стилем)"),
            ("2022-03-08", "Міжнародний жіночий день"),
            ("2022-04-24", "Великдень"),
            ("2022-04-25", "Великдень"),
            ("2022-05-01", "День міжнародної солідарності трудящих"),
            ("2022-05-02", "Проводи"),
            (
                "2022-05-09",
                "День Європи; День Перемоги та вшанування памʼяті героїв, "
                "полеглих за незалежність Батьківщини",
            ),
            ("2022-06-01", "День захисту дітей"),
            ("2022-08-27", "День незалежності Республіки Молдова"),
            ("2022-08-31", "День рідної мови"),
            ("2022-12-25", "Різдво Христове (за новим стилем)"),
        )
