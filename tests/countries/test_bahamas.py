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

from unittest import TestCase

from holidays.countries.bahamas import Bahamas, BS, BHS
from tests.common import CommonCountryTests


class TestBahamas(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bahamas, years=range(1974, 2050), years_non_observed=range(1974, 2050))

    def test_country_aliases(self):
        self.assertAliases(Bahamas, BS, BHS)

    def test_no_holidays(self):
        self.assertNoHolidays(Bahamas(years=1973))

    def test_special_public_holidays(self):
        self.assertHoliday("2022-09-19")

    def test_special_observance_2012_and_prior(self):
        self.assertNoNonObservedHoliday(
            # Cases of New Year's Day observance overflow into prev year
            "1979-12-31",
            "1984-12-31",
            "1990-12-31",
            "2001-12-31",
            "2007-12-31",
            # New Year's Day
            "2003-01-03",
            "2004-01-02",
            "2009-01-02",
            "2011-01-03",
            # Discovery Day
            "2000-10-13",
            "2004-10-11",
            "2005-10-14",
            "2006-10-13",
            "2010-10-11",
            "2011-10-14",
        )

    def test_2012(self):
        self.assertHolidays(
            Bahamas(years=2012),
            ("2012-01-01", "New Year's Day"),
            ("2012-01-02", "New Year's Day (observed)"),
            ("2012-04-06", "Good Friday"),
            ("2012-04-09", "Easter Monday"),
            ("2012-05-28", "Whit Monday"),
            ("2012-06-01", "Labour Day"),
            ("2012-07-10", "Independence Day"),
            ("2012-08-06", "Emancipation Day"),
            ("2012-10-12", "Discovery Day"),
            ("2012-12-25", "Christmas Day"),
            ("2012-12-26", "Boxing Day"),
        )

    def test_2013(self):
        self.assertHolidays(
            Bahamas(years=2013),
            ("2013-01-01", "New Year's Day"),
            ("2013-03-29", "Good Friday"),
            ("2013-04-01", "Easter Monday"),
            ("2013-05-20", "Whit Monday"),
            ("2013-06-07", "Randol Fawkes Labour Day"),
            ("2013-07-10", "Independence Day"),
            ("2013-08-05", "Emancipation Day"),
            ("2013-10-14", "National Heroes Day"),
            ("2013-12-25", "Christmas Day"),
            ("2013-12-26", "Boxing Day"),
        )

    def test_2014(self):
        self.assertHolidays(
            Bahamas(years=2014),
            ("2014-01-01", "New Year's Day"),
            ("2014-01-10", "Majority Rule Day"),
            ("2014-04-18", "Good Friday"),
            ("2014-04-21", "Easter Monday"),
            ("2014-06-06", "Randol Fawkes Labour Day"),
            ("2014-06-09", "Whit Monday"),
            ("2014-07-10", "Independence Day"),
            ("2014-08-04", "Emancipation Day"),
            ("2014-10-13", "National Heroes Day"),
            ("2014-12-25", "Christmas Day"),
            ("2014-12-26", "Boxing Day"),
        )

    def test_2020(self):
        self.assertHolidays(
            Bahamas(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-01-10", "Majority Rule Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-06-01", "Whit Monday"),
            ("2020-06-05", "Randol Fawkes Labour Day"),
            ("2020-07-10", "Independence Day"),
            ("2020-08-03", "Emancipation Day"),
            ("2020-10-12", "National Heroes Day"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-12-28", "Boxing Day (observed)"),
        )

    def test_2021(self):
        self.assertHolidays(
            Bahamas(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-01-10", "Majority Rule Day"),
            ("2021-01-11", "Majority Rule Day (observed)"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-24", "Whit Monday"),
            ("2021-06-04", "Randol Fawkes Labour Day"),
            ("2021-07-10", "Independence Day"),
            ("2021-07-12", "Independence Day (observed)"),
            ("2021-08-02", "Emancipation Day"),
            ("2021-10-11", "National Heroes Day"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Boxing Day (observed)"),
        )

    def test_2022(self):
        self.assertHolidays(
            Bahamas(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Majority Rule Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-03", "Randol Fawkes Labour Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-10", "Independence Day"),
            ("2022-07-11", "Independence Day (observed)"),
            ("2022-08-01", "Emancipation Day"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-10-10", "National Heroes Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Bahamas(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-10", "Majority Rule Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-29", "Whit Monday"),
            ("2023-06-02", "Randol Fawkes Labour Day"),
            ("2023-07-10", "Independence Day"),
            ("2023-08-07", "Emancipation Day"),
            ("2023-10-09", "National Heroes Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
