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

from holidays.countries.aruba import Aruba, AW, ABW
from tests.common import CommonCountryTests


class TestAruba(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(AW.start_year, 2050)
        super().setUpClass(Aruba, years=cls.full_range)

    def test_country_aliases(self):
        self.assertAliases(Aruba, AW, ABW)

    def test_no_holidays(self):
        self.assertNoHolidays(Aruba(years=AW.start_year - 1))

    def test_2017(self):
        self.assertHolidays(
            Aruba(years=2017),
            ("2017-01-01", "Aña Nobo"),
            ("2017-01-25", "Dia di Betico"),
            ("2017-02-27", "Dialuna despues di Carnaval Grandi"),
            ("2017-03-18", "Dia di Himno y Bandera"),
            ("2017-04-14", "Bierna Santo"),
            ("2017-04-17", "Di dos dia di Pasco di Resureccion"),
            ("2017-04-27", "Aña di Rey"),
            ("2017-05-01", "Dia di Obrero"),
            ("2017-05-25", "Dia di Asuncion"),
            ("2017-12-25", "Pasco di Nacemento"),
            ("2017-12-26", "Di dos dia di Pasco di Nacemento"),
        )

    def test_new_years_day(self):
        self.assertHolidayName("Aña Nobo", (f"{year}-01-01" for year in self.full_range))

    def test_betico_day(self):
        name = "Dia di Betico"
        self.assertHolidayName(name, (f"{year}-01-25" for year in range(1989, 2050)))
        self.assertNoHolidayName(name, range(AW.start_year, 1989))

    def test_carnival_monday(self):
        name_carnival = "Dialuna despues di Carnaval Grandi"
        name_mon_ash = "Dialuna prome cu diaranson di shinish"

        self.assertHolidayName(
            name_carnival,
            "2016-02-08",
            "2017-02-27",
            "2018-02-12",
            "2019-03-04",
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
        )
        self.assertHolidayName(name_carnival, range(1956, 2023))
        self.assertHolidayName(
            name_mon_ash,
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name_mon_ash, range(2023, 2050))
        self.assertNoHolidayName(name_carnival, AW.start_year, range(2023, 2050))
        self.assertNoHolidayName(name_mon_ash, range(AW.start_year, 2023))

    def test_national_anthem_and_flag_day(self):
        name = "Dia di Himno y Bandera"
        self.assertHolidayName(name, (f"{year}-03-18" for year in range(1976, 2050)))
        self.assertNoHolidayName(name, range(AW.start_year, 1976))

    def test_good_friday(self):
        name = "Bierna Santo"
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

    def test_easter_monday(self):
        name = "Di dos dia di Pasco di Resureccion"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_queens_day(self):
        name = "Aña di La Reina"
        self.assertHolidayName(
            name,
            "1961-05-01",
            "1965-04-30",
            "1967-05-01",
            "1972-05-01",
            "1978-05-01",
            "1989-04-29",
            "1995-04-29",
            "2000-04-29",
            "2006-04-29",
            "2013-04-30",
        )
        self.assertHolidayName(name, range(AW.start_year, 2014))
        self.assertNoHolidayName(
            name,
            "1961-04-30",
            "1967-04-30",
            "1972-04-30",
            "1978-04-30",
            "1995-04-30",
            "1989-04-30",
            "2000-04-30",
            "2006-04-30",
        )
        self.assertNoHolidayName(name, range(2014, 2050))

    def test_king_day(self):
        name_ana = "Aña di Rey"
        name_dia = "Dia di Rey"
        self.assertHolidayName(
            name_ana,
            "2014-04-26",
            "2015-04-27",
            "2016-04-27",
            "2017-04-27",
            "2018-04-27",
            "2019-04-27",
            "2020-04-27",
        )
        self.assertHolidayName(
            name_dia,
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertHolidayName(name_dia, range(2021, 2050))
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )
        self.assertNoHolidayName(name_ana, range(AW.start_year, 2014), range(2021, 2050))
        self.assertNoHolidayName(name_dia, range(AW.start_year, 2021))

    def test_labor_day(self):
        name = "Dia di Obrero"
        self.assertHolidayName(
            name,
            "2016-05-02",
            "2017-05-01",
            "2018-05-01",
            "2019-05-01",
            "2020-05-01",
            "2021-05-01",
            "2022-05-02",
            "2023-05-01",
        )
        self.assertHolidayName(name, self.full_range)
        self.assertNoHolidayName(
            "2011-05-01",
            "2016-05-01",
            "2022-05-01",
        )

    def test_ascension_day(self):
        name = "Dia di Asuncion"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas(self):
        self.assertHolidayName("Pasco di Nacemento", (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(
            "Di dos dia di Pasco di Nacemento", (f"{year}-12-26" for year in self.full_range)
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Aña Nobo"),
            ("2023-01-25", "Dia di Betico"),
            ("2023-02-20", "Dialuna prome cu diaranson di shinish"),
            ("2023-03-18", "Dia di Himno y Bandera"),
            ("2023-04-07", "Bierna Santo"),
            ("2023-04-10", "Di dos dia di Pasco di Resureccion"),
            ("2023-04-27", "Dia di Rey"),
            ("2023-05-01", "Dia di Obrero"),
            ("2023-05-18", "Dia di Asuncion"),
            ("2023-12-25", "Pasco di Nacemento"),
            ("2023-12-26", "Di dos dia di Pasco di Nacemento"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-25", "Betico Day"),
            ("2023-02-20", "Monday before Ash Wednesday"),
            ("2023-03-18", "National Anthem and Flag Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Second Day of Christmas"),
        )

    def test_l10n_nl(self):
        self.assertLocalizedHolidays(
            "nl",
            ("2023-01-01", "Nieuwjaarsdag"),
            ("2023-01-25", "Beticodag"),
            ("2023-02-20", "Maandag voor Aswoensdag"),
            ("2023-03-18", "Nationale vlag en volkslied"),
            ("2023-04-07", "Goede vrijdag"),
            ("2023-04-10", "Tweede paasdag"),
            ("2023-04-27", "Koningsdag"),
            ("2023-05-01", "Dag van de Arbeid"),
            ("2023-05-18", "Hemelvaartsdag"),
            ("2023-12-25", "Eerste Kerstdag"),
            ("2023-12-26", "Tweede kerstdag"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-01-25", "День Бетіко"),
            ("2023-02-20", "Понеділок перед Попільною середою"),
            ("2023-03-18", "День державного гімну та прапора"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-04-10", "Великодній понеділок"),
            ("2023-04-27", "День короля"),
            ("2023-05-01", "День праці"),
            ("2023-05-18", "Вознесіння Господнє"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-26", "Другий день Різдва"),
        )
