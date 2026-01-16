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

from holidays.constants import HALF_DAY
from holidays.countries.curacao import Curacao
from tests.common import CommonCountryTests


class TestCuracao(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Curacao, years_half_day=range(2010, 2050))

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Curacao(categories=HALF_DAY, years=range(self.start_year, 2010)))

    def test_2016_public(self):
        self.assertHolidaysInYear(
            2016,
            ("2016-01-01", "Aña Nobo"),
            ("2016-02-08", "Dialuna despues di Carnaval Grandi"),
            ("2016-03-25", "Bièrnèsantu"),
            ("2016-03-27", "Pasku di Resurekshon"),
            ("2016-03-28", "Di dos dia di Pasku di Resurekshon"),
            ("2016-04-27", "Dia di Rey"),
            ("2016-05-02", "Dia di Obrero"),
            ("2016-05-05", "Dia di Asenshon"),
            ("2016-07-02", "Dia di Himno i Bandera"),
            ("2016-10-10", "Dia di Pais Kòrsou"),
            ("2016-12-25", "Pasku di Nasementu"),
            ("2016-12-26", "Di dos dia di Pasku di Nasementu"),
        )

    def test_2016_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2016,
            ("2016-12-31", "Vispu di Aña Nobo"),
        )

    def test_new_years_day(self):
        self.assertHolidayName("Aña Nobo", (f"{year}-01-01" for year in self.full_range))

    def test_carnival_monday(self):
        name = "Dialuna despues di Carnaval Grandi"
        self.assertHolidayName(
            name,
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Bièrnèsantu"
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

    def test_easter_sunday(self):
        name = "Pasku di Resurekshon"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Di dos dia di Pasku di Resurekshon"
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
        name = "Dia di la Reina"
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
        self.assertHolidayName(name, range(self.start_year, 2014))
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
        self.assertNoHolidayName(name, range(2014, self.end_year))

    def test_king_day(self):
        name = "Dia di Rey"
        self.assertHolidayName(
            name,
            "2016-04-27",
            "2017-04-27",
            "2018-04-27",
            "2019-04-27",
            "2020-04-27",
            "2021-04-27",
            "2022-04-27",
            "2023-04-27",
            "2024-04-27",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertHolidayName(name, range(2014, self.end_year))
        self.assertNoHolidayName(
            name,
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )
        self.assertNoHolidayName(name, range(self.start_year, 2014))

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
            name,
            "2011-05-01",
            "2016-05-01",
            "2022-05-01",
        )

    def test_ascension_day(self):
        name = "Dia di Asenshon"
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

    def test_whit_sunday(self):
        name = "Domingo di Pentekòstès"
        self.assertHolidayName(
            name,
            "2005-05-15",
            "2006-06-04",
            "2007-05-27",
            "2008-05-11",
            "2009-05-31",
        )
        self.assertHolidayName(name, range(self.start_year, 2010))
        self.assertNoHolidayName(name, range(2010, self.end_year))

    def test_national_anthem_and_flag_day(self):
        name = "Dia di Himno i Bandera"
        self.assertHolidayName(name, (f"{year}-07-02" for year in range(1984, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1984))

    def test_curacao_day(self):
        name = "Dia di Pais Kòrsou"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(2010, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2010))

    def test_christmas(self):
        self.assertHolidayName("Pasku di Nasementu", (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(
            "Di dos dia di Pasku di Nasementu", (f"{year}-12-26" for year in self.full_range)
        )

    def test_new_years_eve(self):
        name = "Vispu di Aña Nobo"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name, (f"{year}-12-31" for year in range(2010, self.end_year))
        )
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 2010))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Aña Nobo"),
            ("2023-02-20", "Dialuna despues di Carnaval Grandi"),
            ("2023-04-07", "Bièrnèsantu"),
            ("2023-04-09", "Pasku di Resurekshon"),
            ("2023-04-10", "Di dos dia di Pasku di Resurekshon"),
            ("2023-04-27", "Dia di Rey"),
            ("2023-05-01", "Dia di Obrero"),
            ("2023-05-18", "Dia di Asenshon"),
            ("2023-07-02", "Dia di Himno i Bandera"),
            ("2023-10-10", "Dia di Pais Kòrsou"),
            ("2023-12-25", "Pasku di Nasementu"),
            ("2023-12-26", "Di dos dia di Pasku di Nasementu"),
            ("2023-12-31", "Vispu di Aña Nobo"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-20", "Carnival Monday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-07-02", "National Anthem and Flag Day"),
            ("2023-10-10", "Curaçao Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Second Day of Christmas"),
            ("2023-12-31", "New Year's Eve"),
        )

    def test_l10n_nl(self):
        self.assertLocalizedHolidays(
            "nl",
            ("2023-01-01", "Nieuwjaarsdag"),
            ("2023-02-20", "De maandag na de Grote Karnaval"),
            ("2023-04-07", "Goede Vrijdag"),
            ("2023-04-09", "Paasdag"),
            ("2023-04-10", "Tweede paasdag"),
            ("2023-04-27", "Koningsdag"),
            ("2023-05-01", "Dag van de Arbeid"),
            ("2023-05-18", "Hemelvaartsdag"),
            ("2023-07-02", "Nationale vlag en volkslied"),
            ("2023-10-10", "Dag van Land Curaçao"),
            ("2023-12-25", "Eerste Kerstdag"),
            ("2023-12-26", "Tweede kerstdag"),
            ("2023-12-31", "Oudejaarsavond"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-02-20", "Карнавальний понеділок"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-04-09", "Великдень"),
            ("2023-04-10", "Великодній понеділок"),
            ("2023-04-27", "День короля"),
            ("2023-05-01", "День праці"),
            ("2023-05-18", "Вознесіння Господнє"),
            ("2023-07-02", "День державного гімну та прапора"),
            ("2023-10-10", "День Кюрасао"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-26", "Другий день Різдва"),
            ("2023-12-31", "Переддень Нового року"),
        )
