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

from holidays.entities.ISO_3166.BZ import BzHolidays
from tests.common import CommonCountryTests


class TestBzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            BzHolidays, years=range(1982, 2050), years_non_observed=range(1982, 2050)
        )

    def test_no_holidays(self):
        self.assertNoHolidays(BzHolidays(years=1981))

    def test_new_years_day(self):
        name = "New Year's Day"
        years_observed = {1984, 1989, 1995, 2006, 2012, 2017, 2023, 2034, 2040, 2045}
        self.assertHolidayName(
            name, (f"{year}-01-01" for year in set(range(1982, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-01-02" for year in years_observed))

    def test_george_price_day(self):
        name = "George Price Day"
        years_observed = {2023, 2034, 2040, 2045}
        self.assertHolidayName(
            name, (f"{year}-01-15" for year in set(range(2021, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-01-16" for year in years_observed))
        self.assertNoHoliday(f"{year}-01-15" for year in range(1982, 2021))
        self.assertNoHolidayName(name, range(1982, 2021))

    def test_national_heroes_and_benefactors_day(self):
        name = "National Heroes and Benefactors Day"
        self.assertHolidayName(
            f"{name} (observed)",
            "1982-03-08",
            "1983-03-07",
            "1984-03-12",
            "1993-03-08",
            "2000-03-06",
            "2010-03-08",
            "2018-03-12",
            "2021-03-08",
            "2022-03-07",
            "2023-03-06",
        )
        self.assertNonObservedHolidayName(name, (f"{year}-03-09" for year in range(1982, 2050)))

    def test_easter_holidays(self):
        self.assertHolidayName(
            "Good Friday",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

        self.assertHolidayName(
            "Holy Saturday",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
        )

        self.assertHolidayName(
            "Easter Monday",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labour_day(self):
        name = "Labour Day"
        years_observed = {1983, 1988, 1994, 2005, 2011, 2016, 2022, 2033, 2039, 2044}
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in set(range(1982, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-05-02" for year in years_observed))

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        self.assertHolidayName(
            f"{name} (observed)",
            "1983-05-23",
            "1984-05-21",
            "1992-05-25",
            "2000-05-22",
            "2011-05-23",
            "2018-05-21",
            "2019-05-27",
            "2020-05-25",
        )
        self.assertNonObservedHolidayName(name, (f"{year}-05-24" for year in range(1982, 2022)))
        self.assertNoHolidayName(name, range(2022, 2050))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(
            f"{name} (observed)",
            "2021-08-02",
            "2023-07-31",
            "2024-07-29",
            "2025-08-04",
        )
        self.assertNonObservedHolidayName(name, (f"{year}-08-01" for year in range(2021, 2050)))
        self.assertNoHolidayName(name, range(1982, 2021))

    def test_saint_georges_caye_day(self):
        name = "Saint George's Caye Day"
        years_observed = {1989, 1995, 2000, 2006, 2017, 2023, 2028, 2034, 2045}
        self.assertHolidayName(
            name, (f"{year}-09-10" for year in set(range(1982, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-09-11" for year in years_observed))

    def test_independence_day(self):
        name = "Independence Day"
        years_observed = {1986, 1997, 2003, 2008, 2014, 2025, 2031, 2036, 2042}
        self.assertHolidayName(
            name, (f"{year}-09-21" for year in set(range(1982, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-09-22" for year in years_observed))

    def test_indigenous_peoples_resistance_day(self):
        name1 = "Pan American Day"
        name2 = "Indigenous Peoples' Resistance Day"
        self.assertHolidayName(
            f"{name1} (observed)",
            "1982-10-11",
            "1983-10-10",
            "1993-10-11",
            "2000-10-09",
            "2011-10-10",
            "2018-10-15",
        )
        self.assertHolidayName(
            f"{name2} (observed)",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2025-10-13",
            "2027-10-11",
        )
        self.assertNonObservedHolidayName(name1, (f"{year}-10-12" for year in range(1982, 2021)))
        self.assertNonObservedHolidayName(name2, (f"{year}-10-12" for year in range(2021, 2050)))
        self.assertNoHolidayName(name1, range(2021, 2050))
        self.assertNoHolidayName(name2, range(1982, 2021))

    def test_garifuna_settlement_day(self):
        name = "Garifuna Settlement Day"
        years_observed = {1989, 1995, 2000, 2006, 2017, 2023, 2028, 2034, 2045}
        self.assertHolidayName(
            name, (f"{year}-11-19" for year in set(range(1982, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-11-20" for year in years_observed))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1982, 2050)))

    def test_boxing_day(self):
        name = "Boxing Day"
        years_observed = {1982, 1993, 1999, 2004, 2010, 2021, 2027, 2032, 2038, 2049}
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in set(range(1982, 2050)).difference(years_observed))
        )
        self.assertHolidayName(f"{name} (observed)", (f"{year}-12-27" for year in years_observed))

    def test_2021(self):
        # https://www.pressoffice.gov.bz/public-and-bank-holidays-2021-3/
        self.assertHolidays(
            BzHolidays(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-01-15", "George Price Day"),
            ("2021-03-08", "National Heroes and Benefactors Day (observed)"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "Holy Saturday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-01", "Labour Day"),
            ("2021-05-24", "Commonwealth Day"),
            ("2021-08-02", "Emancipation Day (observed)"),
            ("2021-09-10", "Saint George's Caye Day"),
            ("2021-09-21", "Independence Day"),
            ("2021-10-11", "Indigenous Peoples' Resistance Day (observed)"),
            ("2021-11-19", "Garifuna Settlement Day"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-27", "Boxing Day (observed)"),
        )

    def test_2022(self):
        # https://www.pressoffice.gov.bz/public-and-bank-holidays-2022-updated/
        self.assertHolidays(
            BzHolidays(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-15", "George Price Day"),
            ("2022-03-07", "National Heroes and Benefactors Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-08-01", "Emancipation Day"),
            ("2022-09-10", "Saint George's Caye Day"),
            ("2022-09-21", "Independence Day"),
            ("2022-10-10", "Indigenous Peoples' Resistance Day (observed)"),
            ("2022-11-19", "Garifuna Settlement Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )
