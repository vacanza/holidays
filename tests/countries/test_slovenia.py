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

from holidays.constants import WORKDAY
from holidays.countries.slovenia import Slovenia
from tests.common import CommonCountryTests


class TestSlovenia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1992, 2050)
        super().setUpClass(Slovenia, years=years)
        cls.workday_holidays = Slovenia(categories=WORKDAY, years=years)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Slovenia(categories=WORKDAY, years=2004))

    def test_special_holidays(self):
        self.assertHoliday(
            # Solidarity Day.
            "2023-08-14",
        )

    def test_new_years_day(self):
        name = "novo leto"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1992, 2050)))
        self.assertHolidayName(
            name, (f"{year}-01-02" for year in (*range(1992, 2013), *range(2017, 2050)))
        )
        self.assertNoHoliday(f"{year}-01-02" for year in range(2013, 2017))

    def test_preserens_day(self):
        self.assertHolidayName(
            "Prešernov dan, slovenski kulturni praznik",
            (f"{year}-02-08" for year in range(1992, 2050)),
        )

    def test_easter_sunday(self):
        self.assertHolidayName(
            "velikonočna nedelja",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "velikonočni ponedeljek",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )

    def test_uprising_against_occupation_day(self):
        self.assertHolidayName(
            "dan upora proti okupatorju", (f"{year}-04-27" for year in range(1992, 2050))
        )

    def test_labor_day(self):
        self.assertHolidayName(
            "praznik dela",
            (f"{year}-05-01" for year in range(1992, 2050)),
            (f"{year}-05-02" for year in range(1992, 2050)),
        )

    def test_whit_sunday(self):
        self.assertHolidayName(
            "binkoštna nedelja",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
        )

    def test_statehood_day(self):
        self.assertHolidayName("dan državnosti", (f"{year}-06-25" for year in range(1992, 2050)))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Marijino vnebovzetje", (f"{year}-08-15" for year in range(1992, 2050))
        )

    def test_reformation_day(self):
        self.assertHolidayName("dan reformacije", (f"{year}-10-31" for year in range(1992, 2050)))

    def test_all_saints_day(self):
        self.assertHolidayName(
            "dan spomina na mrtve", (f"{year}-11-01" for year in range(1992, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("božič", (f"{year}-12-25" for year in range(1992, 2050)))

    def test_independence_and_unity_day(self):
        name_1 = "dan samostojnosti"
        name_2 = "dan samostojnosti in enotnosti"
        self.assertHolidayName(name_1, (f"{year}-12-26" for year in range(1992, 2005)))
        self.assertHolidayName(name_2, (f"{year}-12-26" for year in range(2005, 2050)))
        self.assertNoHolidayName(name_1, range(2005, 2050))
        self.assertNoHolidayName(name_2, range(1992, 2005))

    def test_primoz_trubar_day(self):
        name = "dan Primoža Trubarja"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-06-08" for year in range(2011, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1992, 2011))

    def test_unification_of_prekmurje_slovenes(self):
        name = "združitev prekmurskih Slovencev z matičnim narodom"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-08-17" for year in range(2006, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1992, 2006))

    def test_integration_of_primorska(self):
        name_1 = "vrnitev Primorske k matični domovini"
        name_2 = "priključitev Primorske k matični domovini"
        self.assertNoHolidayName(name_1)
        self.assertNoHolidayName(name_2)
        self.assertHolidayName(
            name_1, self.workday_holidays, (f"{year}-09-15" for year in range(2006, 2025))
        )
        self.assertHolidayName(
            name_2, self.workday_holidays, (f"{year}-09-15" for year in range(2025, 2050))
        )
        self.assertNoHolidayName(
            name_1, self.workday_holidays, range(1992, 2006), range(2025, 2050)
        )
        self.assertNoHolidayName(name_2, self.workday_holidays, range(1992, 2025))

    def test_slovenian_sports_day(self):
        name = "dan slovenskega športa"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-09-23" for year in range(2020, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1992, 2020))

    def test_sovereignty_day(self):
        name = "dan suverenosti"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-10-25" for year in range(2015, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1992, 2015))

    def test_rudolf_maister_day(self):
        name = "dan Rudolfa Maistra"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-11-23" for year in range(2005, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(1992, 2005))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "novo leto"),
            ("2022-01-02", "novo leto"),
            ("2022-02-08", "Prešernov dan, slovenski kulturni praznik"),
            ("2022-04-17", "velikonočna nedelja"),
            ("2022-04-18", "velikonočni ponedeljek"),
            ("2022-04-27", "dan upora proti okupatorju"),
            ("2022-05-01", "praznik dela"),
            ("2022-05-02", "praznik dela"),
            ("2022-06-05", "binkoštna nedelja"),
            ("2022-06-08", "dan Primoža Trubarja"),
            ("2022-06-25", "dan državnosti"),
            ("2022-08-15", "Marijino vnebovzetje"),
            ("2022-08-17", "združitev prekmurskih Slovencev z matičnim narodom"),
            ("2022-09-15", "vrnitev Primorske k matični domovini"),
            ("2022-09-23", "dan slovenskega športa"),
            ("2022-10-25", "dan suverenosti"),
            ("2022-10-31", "dan reformacije"),
            ("2022-11-01", "dan spomina na mrtve"),
            ("2022-11-23", "dan Rudolfa Maistra"),
            ("2022-12-25", "božič"),
            ("2022-12-26", "dan samostojnosti in enotnosti"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-02-08", "Prešeren's Day, the Slovenian Cultural Holiday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "Day of Uprising Against Occupation"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-08", "Primož Trubar Day"),
            ("2022-06-25", "Statehood Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-08-17", "Unification of Prekmurje Slovenes with the Mother Nation"),
            ("2022-09-15", "Return of Primorska into the Homeland"),
            ("2022-09-23", "Slovenian Sport's Day"),
            ("2022-10-25", "Sovereignty Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "Day of Remembrance for the Dead"),
            ("2022-11-23", "Rudolf Maister Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Independence and Unity Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-02-08", "День Прешерена, свято словенської культури"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День спротиву окупантам"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці"),
            ("2022-06-05", "Трійця"),
            ("2022-06-08", "День Приможа Трубара"),
            ("2022-06-25", "День державності"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-08-17", "Обʼєднання прекмурських словенців з материнською нацією"),
            ("2022-09-15", "Повернення Словенського Приморʼя до батьківщини"),
            ("2022-09-23", "День словенського спорту"),
            ("2022-10-25", "День суверенітету"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День памʼяті померлих"),
            ("2022-11-23", "День Рудольфа Майстера"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День незалежності та єднання"),
        )
