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

from holidays.constants import OPTIONAL
from holidays.countries.netherlands import Netherlands, NL, NLD
from tests.common import CommonCountryTests


class TestNetherlands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Netherlands)

    def test_country_aliases(self):
        self.assertAliases(Netherlands, NL, NLD)

    def test_queens_day_between_1891_and_1948(self):
        name = "Koninginnedag"
        self.assertHolidayName(name, "1891-08-31", "1901-08-31", "1948-08-31")
        self.assertNoHolidayName(name, Netherlands(years=1890))

    def test_queens_day_between_1891_and_1948_substituted_later(self):
        self.assertHolidayName(
            "Koninginnedag",
            "1902-09-01",
            "1913-09-01",
            "1919-09-01",
            "1924-09-01",
            "1930-09-01",
            "1941-09-01",
            "1947-09-01",
        )
        self.assertNoHoliday(
            "1902-08-31",
            "1913-08-31",
            "1919-08-31",
            "1924-08-31",
            "1930-08-31",
            "1941-08-31",
            "1947-08-31",
        )

    def test_queens_day_between_1949_and_2013(self):
        name = "Koninginnedag"
        self.assertHolidayName(name, "1949-04-30", "1970-04-30", "2013-04-30")
        self.assertNoHoliday("2014-04-30")
        self.assertNoHolidayName(name, Netherlands(years=2014))

    def test_queens_day_between_1949_and_1980_substituted_later(self):
        self.assertHolidayName(
            "Koninginnedag",
            "1950-05-01",
            "1961-05-01",
            "1967-05-01",
            "1972-05-01",
            "1978-05-01",
        )
        self.assertNoHoliday(
            "1950-04-30",
            "1961-04-30",
            "1967-04-30",
            "1972-04-30",
            "1978-04-30",
        )

    def test_queens_day_between_1980_and_2013_substituted_earlier(self):
        self.assertHolidayName(
            "Koninginnedag",
            "1989-04-29",
            "1995-04-29",
            "2000-04-29",
            "2006-04-29",
        )
        self.assertNoHoliday(
            "1995-04-30",
            "1989-04-30",
            "2000-04-30",
            "2006-04-30",
        )

    def test_kings_day_after_2014(self):
        name = "Koningsdag"
        self.assertHolidayName(name, "2015-04-27", "2020-04-27", "2023-04-27")
        self.assertNoHoliday("2013-04-27")
        self.assertNoHolidayName(name, Netherlands(years=2013))

    def test_kings_day_after_2014_substituted_earlier(self):
        self.assertHolidayName(
            "Koningsdag",
            "2014-04-26",
            "2025-04-26",
            "2031-04-26",
            "2036-04-26",
        )
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
            "2031-04-27",
            "2036-04-27",
        )

    def test_liberation_day(self):
        name = "Bevrijdingsdag"
        self.assertHolidayName(
            name,
            "1950-05-05",
            "1955-05-05",
            "1960-05-05",
            "1965-05-05",
            "1970-05-05",
            "1975-05-05",
            "1980-05-05",
            "1985-05-05",
            "1990-05-05",
            "1995-05-05",
            "2000-05-05",
            "2005-05-05",
            "2010-05-05",
            "2015-05-05",
            "2020-05-05",
        )
        self.assertNoHoliday(
            "1949-05-05",
            "1971-05-05",
            "1991-05-05",
        )

        opt_holidays = Netherlands(categories=OPTIONAL, years=range(1980, 2050))
        self.assertHolidayName(name, opt_holidays, (f"{year}-05-05" for year in range(1990, 2050)))
        self.assertNoHolidayName(name, Netherlands(categories=OPTIONAL, years=(1949, 1971, 1989)))

    def test_2017(self):
        self.assertHolidays(
            ("2017-01-01", "Nieuwjaarsdag"),
            ("2017-04-16", "Eerste paasdag"),
            ("2017-04-17", "Tweede paasdag"),
            ("2017-04-27", "Koningsdag"),
            ("2017-05-25", "Hemelvaartsdag"),
            ("2017-06-04", "Eerste Pinksterdag"),
            ("2017-06-05", "Tweede Pinksterdag"),
            ("2017-12-25", "Eerste Kerstdag"),
            ("2017-12-26", "Tweede Kerstdag"),
        )

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Nieuwjaarsdag"),
            ("2020-04-12", "Eerste paasdag"),
            ("2020-04-13", "Tweede paasdag"),
            ("2020-04-27", "Koningsdag"),
            ("2020-05-05", "Bevrijdingsdag"),
            ("2020-05-21", "Hemelvaartsdag"),
            ("2020-05-31", "Eerste Pinksterdag"),
            ("2020-06-01", "Tweede Pinksterdag"),
            ("2020-12-25", "Eerste Kerstdag"),
            ("2020-12-26", "Tweede Kerstdag"),
        )

    def test_2023_optional(self):
        self.assertHolidays(
            Netherlands(categories=OPTIONAL, years=2023),
            ("2023-04-07", "Goede Vrijdag"),
            ("2023-05-05", "Bevrijdingsdag"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaarsdag"),
            ("2022-04-15", "Goede Vrijdag"),
            ("2022-04-17", "Eerste paasdag"),
            ("2022-04-18", "Tweede paasdag"),
            ("2022-04-27", "Koningsdag"),
            ("2022-05-05", "Bevrijdingsdag"),
            ("2022-05-26", "Hemelvaartsdag"),
            ("2022-06-05", "Eerste Pinksterdag"),
            ("2022-06-06", "Tweede Pinksterdag"),
            ("2022-12-25", "Eerste Kerstdag"),
            ("2022-12-26", "Tweede Kerstdag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "King's Day"),
            ("2022-05-05", "Liberation Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День короля"),
            ("2022-05-05", "День визволення"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
