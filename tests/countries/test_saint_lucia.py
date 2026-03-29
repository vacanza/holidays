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

from holidays.countries.saint_lucia import SaintLucia
from tests.common import CommonCountryTests


class TestSaintLucia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            SaintLucia, years=range(1979, 2050), years_non_observed=range(1979, 2050)
        )

    def test_new_years(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1979, 2050)))
        self.assertHolidayName(
            "New Year's Holiday", (f"{year}-01-02" for year in range(1979, 2050))
        )

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-02-22" for year in range(1979, 2050)))
        dt = (
            "2004-02-23",
            "2009-02-23",
            "2015-02-23",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1979, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(1979, 2050))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1979, 2050)))
        dt = (
            "2004-08-02",
            "2010-08-02",
            "2021-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1979, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_corpus_christi(self):
        name = "Corpus Christi"
        dt = (
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1979, 2050))

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        dt = (
            "1995-10-02",
            "1996-10-07",
            "1997-10-06",
            "1998-10-05",
            "1999-10-04",
            "2000-10-02",
            "2001-10-01",
            "2002-10-07",
            "2003-10-06",
            "2004-10-04",
            "2005-10-03",
            "2006-10-02",
            "2007-10-01",
            "2008-10-06",
            "2009-10-05",
            "2010-10-04",
            "2011-10-03",
            "2012-10-01",
            "2013-10-07",
            "2014-10-06",
            "2015-10-05",
            "2016-10-03",
            "2017-10-02",
            "2018-10-01",
            "2019-10-07",
            "2020-10-05",
            "2021-10-04",
            "2022-10-03",
            "2023-10-02",
            "2024-10-07",
            "2025-10-06",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1979, 2050))

    def test_national_day(self):
        name = "National Day"
        self.assertHolidayName(name, (f"{year}-12-13" for year in range(1979, 2050)))
        dt = (
            "2009-12-14",
            "2015-12-14",
            "2020-12-14",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1979, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(1979, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Holiday"),
            ("2023-01-03", "New Year's Day (observed)"),
            ("2023-02-22", "Independence Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-10-02", "Thanksgiving Day"),
            ("2023-12-13", "National Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Holiday"),
            ("2022-01-03", "New Year's Holiday (observed)"),
            ("2022-02-22", "Independence Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-01", "Emancipation Day"),
            ("2022-10-03", "Thanksgiving Day"),
            ("2022-12-13", "National Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
