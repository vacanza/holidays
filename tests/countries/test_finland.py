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

from holidays.countries.finland import Finland, FI, FIN
from tests.common import CommonCountryTests


class TestFinland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Finland)

    def test_country_aliases(self):
        self.assertAliases(Finland, FI, FIN)

    def test_fixed_holidays(self):
        for year in range(2010, 2030):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-01-06",
                f"{year}-05-01",
                f"{year}-12-06",
                f"{year}-12-24",
                f"{year}-12-25",
                f"{year}-12-26",
            )

    def test_epiphany(self):
        self.assertHolidayName(
            "Loppiainen",
            "1972-01-06",
            "1973-01-06",
            "1974-01-12",
            "1989-01-07",
            "1990-01-06",
            "1991-01-06",
        )
        self.assertNoHoliday(
            "1974-01-06",
            "1975-01-06",
            "1980-01-06",
            "1988-01-06",
            "1989-01-06",
        )

    def test_easter_holidays(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            # Easter Sunday
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            # Ascension Day
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            # Whit Sunday
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )

    def test_ascension_day(self):
        self.assertHoliday(
            "1971-05-20",
            "1972-05-11",
            "1973-05-26",
            "1974-05-18",
            "1989-04-29",
            "1990-05-19",
            "1991-05-09",
            "1992-05-28",
            "1993-05-20",
        )

        self.assertNoHoliday(
            "1973-05-31",
            "1974-05-23",
            "1980-05-15",
            "1988-05-12",
            "1989-05-04",
            "1990-05-24",
        )

    def test_midsummer_eve(self):
        name = "Juhannusaatto"
        self.assertHolidayName(
            name,
            "1953-06-23",
            "1954-06-23",
            "1955-06-24",
            "1956-06-22",
            "1957-06-21",
        )
        for dt in (
            "1955-06-23",
            "1956-06-23",
            "1957-06-23",
        ):
            self.assertNotIn(name, self.holidays.get(dt, ""))

    def test_midsummer_day(self):
        name = "Juhannuspäivä"
        self.assertHolidayName(
            name,
            "1953-06-24",
            "1954-06-24",
            "1955-06-25",
            "1956-06-23",
            "1957-06-22",
        )
        for dt in (
            "1955-06-24",
            "1956-06-24",
            "1957-06-24",
        ):
            self.assertNotIn(name, self.holidays.get(dt, ""))

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Pyhäinpäivä",
            "1952-11-01",
            "1953-11-01",
            "1954-11-01",
            "1955-11-05",
            "1956-11-03",
            "1957-11-02",
        )
        self.assertNoHoliday(
            "1955-11-01",
            "1956-11-01",
            "1957-11-01",
        )

    def test_2018(self):
        self.assertHolidays(
            ("2018-01-01", "Uudenvuodenpäivä"),
            ("2018-01-06", "Loppiainen"),
            ("2018-03-30", "Pitkäperjantai"),
            ("2018-04-01", "Pääsiäispäivä"),
            ("2018-04-02", "2. pääsiäispäivä"),
            ("2018-05-01", "Vappu"),
            ("2018-05-10", "Helatorstai"),
            ("2018-05-20", "Helluntaipäivä"),
            ("2018-06-22", "Juhannusaatto"),
            ("2018-06-23", "Juhannuspäivä"),
            ("2018-11-03", "Pyhäinpäivä"),
            ("2018-12-06", "Itsenäisyyspäivä"),
            ("2018-12-24", "Jouluaatto"),
            ("2018-12-25", "Joulupäivä"),
            ("2018-12-26", "Tapaninpäivä"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Uudenvuodenpäivä"),
            ("2022-01-06", "Loppiainen"),
            ("2022-04-15", "Pitkäperjantai"),
            ("2022-04-17", "Pääsiäispäivä"),
            ("2022-04-18", "2. pääsiäispäivä"),
            ("2022-05-01", "Vappu"),
            ("2022-05-26", "Helatorstai"),
            ("2022-06-05", "Helluntaipäivä"),
            ("2022-06-24", "Juhannusaatto"),
            ("2022-06-25", "Juhannuspäivä"),
            ("2022-11-05", "Pyhäinpäivä"),
            ("2022-12-06", "Itsenäisyyspäivä"),
            ("2022-12-24", "Jouluaatto"),
            ("2022-12-25", "Joulupäivä"),
            ("2022-12-26", "Tapaninpäivä"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Uudenvuodenpäivä"),
            ("2022-01-06", "Loppiainen"),
            ("2022-04-15", "Pitkäperjantai"),
            ("2022-04-17", "Pääsiäispäivä"),
            ("2022-04-18", "2. pääsiäispäivä"),
            ("2022-05-01", "Vappu"),
            ("2022-05-26", "Helatorstai"),
            ("2022-06-05", "Helluntaipäivä"),
            ("2022-06-24", "Juhannusaatto"),
            ("2022-06-25", "Juhannuspäivä"),
            ("2022-11-05", "Pyhäinpäivä"),
            ("2022-12-06", "Itsenäisyyspäivä"),
            ("2022-12-24", "Jouluaatto"),
            ("2022-12-25", "Joulupäivä"),
            ("2022-12-26", "Tapaninpäivä"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "May Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-24", "Midsummer Eve"),
            ("2022-06-25", "Midsummer Day"),
            ("2022-11-05", "All Saints' Day"),
            ("2022-12-06", "Independence Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "Ваппу"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-24", "Переддень літнього сонцестояння"),
            ("2022-06-25", "День літнього сонцестояння"),
            ("2022-11-05", "День усіх святих"),
            ("2022-12-06", "День незалежності"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )

    def test_l10n_sv(self):
        self.assertLocalizedHolidays(
            "sv",
            ("2022-01-01", "Nyårsdagen"),
            ("2022-01-06", "Trettondedagen"),
            ("2022-04-15", "Långfredagen"),
            ("2022-04-17", "Påskdagen"),
            ("2022-04-18", "Annandag påsk"),
            ("2022-05-01", "Vappen"),
            ("2022-05-26", "Kristi himmelfärdsdag"),
            ("2022-06-05", "Pingst"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-06-25", "Midsommardagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-12-06", "Självständighetsdagen"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
        )
