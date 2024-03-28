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

from holidays.countries.lithuania import Lithuania, LT, LTU
from tests.common import CommonCountryTests


class TestLithuania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Lithuania, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertAliases(Lithuania, LT, LTU)

    def test_no_holidays(self):
        self.assertNoHolidays(Lithuania(years=1989))

    def test_new_years(self):
        self.assertHolidayName(
            "Naujųjų metų diena", (f"{year}-01-01" for year in range(1990, 2050))
        )

    def test_restoration_of_state_day(self):
        self.assertHolidayName(
            "Lietuvos valstybės atkūrimo diena", (f"{year}-02-16" for year in range(1990, 2050))
        )

    def test_restoration_of_independence_day(self):
        self.assertHolidayName(
            "Lietuvos nepriklausomybės atkūrimo diena",
            (f"{year}-03-11" for year in range(1990, 2050)),
        )

    def test_easter(self):
        self.assertHolidayName(
            "Šv. Velykos",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Antroji šv. Velykų diena",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        self.assertHolidayName(
            "Tarptautinė darbo diena", (f"{year}-05-01" for year in range(1990, 2050))
        )

    def test_mothers_day(self):
        self.assertHolidayName(
            "Motinos diena",
            "2019-05-05",
            "2020-05-03",
            "2021-05-02",
            "2022-05-01",
            "2023-05-07",
        )

    def test_fathers_day(self):
        self.assertHolidayName(
            "Tėvo diena",
            "2019-06-02",
            "2020-06-07",
            "2021-06-06",
            "2022-06-05",
            "2023-06-04",
        )

    def test_dew_and_saint_john_day(self):
        name = "Rasos ir Joninių diena"
        self.assertHolidayName(name, (f"{year}-06-24" for year in range(2003, 2050)))
        self.assertNoHoliday(f"{year}-06-24" for year in range(1990, 2003))
        self.assertNoHolidayName(name, range(1990, 2003))

    def test_statehood_day(self):
        name = "Valstybės (Lietuvos karaliaus Mindaugo karūnavimo) ir Tautiškos giesmės diena"
        self.assertHolidayName(name, (f"{year}-07-06" for year in range(1991, 2050)))
        self.assertNoHoliday(f"{year}-07-06" for year in range(1990, 1991))
        self.assertNoHolidayName(name, range(1990, 1991))

    def test_assumption_day(self):
        self.assertHolidayName(
            "Žolinė (Švč. Mergelės Marijos ėmimo į dangų diena)",
            (f"{year}-08-15" for year in range(1990, 2050)),
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Visų Šventųjų diena", (f"{year}-11-01" for year in range(1990, 2050))
        )

    def test_all_souls_day(self):
        name = "Mirusiųjų atminimo (Vėlinių) diena"
        self.assertHolidayName(name, (f"{year}-11-02" for year in range(2020, 2050)))
        self.assertNoHoliday(f"{year}-11-02" for year in range(1990, 2020))
        self.assertNoHolidayName(name, range(1990, 2020))

    def test_christmas_eve(self):
        self.assertHolidayName("Kūčių diena", (f"{year}-12-24" for year in range(1990, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Šv. Kalėdų pirma diena", (f"{year}-12-25" for year in range(1990, 2050))
        )

    def test_second_christmas_day(self):
        self.assertHolidayName(
            "Šv. Kalėdų antra diena", (f"{year}-12-26" for year in range(1990, 2050))
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Naujųjų metų diena"),
            ("2022-02-16", "Lietuvos valstybės atkūrimo diena"),
            ("2022-03-11", "Lietuvos nepriklausomybės atkūrimo diena"),
            ("2022-04-17", "Šv. Velykos"),
            ("2022-04-18", "Antroji šv. Velykų diena"),
            ("2022-05-01", "Motinos diena; Tarptautinė darbo diena"),
            ("2022-06-05", "Tėvo diena"),
            ("2022-06-24", "Rasos ir Joninių diena"),
            (
                "2022-07-06",
                "Valstybės (Lietuvos karaliaus Mindaugo karūnavimo) ir Tautiškos giesmės diena",
            ),
            ("2022-08-15", "Žolinė (Švč. Mergelės Marijos ėmimo į dangų diena)"),
            ("2022-11-01", "Visų Šventųjų diena"),
            ("2022-11-02", "Mirusiųjų atminimo (Vėlinių) diena"),
            ("2022-12-24", "Kūčių diena"),
            ("2022-12-25", "Šv. Kalėdų pirma diena"),
            ("2022-12-26", "Šv. Kalėdų antra diena"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-16", "Day of Restoration of the State of Lithuania"),
            ("2022-03-11", "Day of Restoration of Independence of Lithuania"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "International Workers' Day; Mother's Day"),
            ("2022-06-05", "Father's Day"),
            ("2022-06-24", "Day of Dew and Saint John"),
            ("2022-07-06", "Statehood Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-16", "День відновлення Литовської держави"),
            ("2022-03-11", "День відновлення незалежності Литви"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День матері; Міжнародний день трудящих"),
            ("2022-06-05", "День батька"),
            ("2022-06-24", "День роси та День Івана Купала"),
            ("2022-07-06", "День державності та День національного гімну"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-02", "День памʼяті (День всіх померлих)"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
