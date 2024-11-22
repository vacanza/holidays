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

from holidays.countries.guernsey import Guernsey, GG, GGY
from tests.common import CommonCountryTests


class TestGG(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Guernsey, years=range(1909, 2050))

    def test_country_aliases(self):
        self.assertAliases(Guernsey, GG, GGY)

    def test_no_holidays(self):
        self.assertNoHolidays(Guernsey(years=1908))

    def test_special_holidays(self):
        dt = (
            "1930-10-10",
            "1935-05-06",
            "1937-05-12",
            "1939-09-04",
            "1949-09-19",
            "1953-06-02",
            "1957-07-26",
            "1977-06-07",
            "1978-06-28",
            "1981-07-29",
            "1989-05-23",
            "1999-12-28",
            "1999-12-31",
            "2000-01-03",
            "2001-07-12",
            "2002-06-03",
            "2011-04-29",
            "2012-06-05",
            "2022-06-03",
            "2022-09-19",
            "2023-05-08",
            "2024-07-16",
        )
        dt_observed = (
            "1932-12-27",
            "1933-01-02",
            "1938-12-27",
            "1939-01-02",
            "1981-12-28",
            "1982-12-28",
            "1983-01-03",
            "1987-12-28",
            "1993-12-28",
            "1994-01-03",
            "2004-12-28",
            "2005-01-03",
        )
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_his_majesty_birthday(self):
        name = "His Majesty's Birthday"
        dt = (
            # Edward VII (MAY/JUN observance).
            "1909-06-25",
            # George V.
            "1910-06-24",
            "1911-05-27",
            "1912-06-14",
            "1913-06-03",
            "1914-06-24",
            # Not observed in 1915-1918 due to WW1.
            "1919-06-03",
            "1920-06-05",
            "1921-06-04",
            "1922-06-03",
            "1923-06-02",
            "1924-06-03",
            "1925-06-03",
            "1926-06-05",
            "1927-06-03",
            "1928-06-04",
            "1929-06-03",
            "1930-06-03",
            "1931-06-03",
            "1932-06-03",
            "1933-06-03",
            "1934-06-04",
            "1935-06-03",
            # Edward VIII.
            "1936-06-23",
            # George VI.
            "1937-06-09",
            "1938-06-09",
            "1939-06-08",
            # Not observed in 1940-1941 due to WW2.
            "1942-06-11",
            "1943-06-02",
            "1944-06-08",
            "1945-06-14",
            "1946-06-13",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, range(1915, 1919), range(1940, 1942), range(1947, 2050))

    def test_liberation_day(self):
        self.assertHolidayName(
            "Liberation Day",
            "2010-05-10",
            (f"{year}-05-09" for year in range(1946, 2010)),
            (f"{year}-05-09" for year in range(2011, 2050)),
        )

    def test_2019(self):
        # Wayback Machine of https://www.gov.gg/holidaydates
        self.assertHolidays(
            Guernsey(years=2019),
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-06", "May Day Bank Holiday"),
            ("2019-05-09", "Liberation Day"),
            ("2019-05-27", "Spring Bank Holiday"),
            ("2019-08-26", "Summer Bank Holiday"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Boxing Day"),
        )

    def test_2020(self):
        # Wayback Machine of https://www.gov.gg/holidaydates
        self.assertHolidays(
            Guernsey(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-08", "May Day Bank Holiday"),
            ("2020-05-09", "Liberation Day"),
            ("2020-05-25", "Spring Bank Holiday"),
            ("2020-08-31", "Summer Bank Holiday"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-12-28", "Boxing Day (substitute day)"),
        )

    def test_2021(self):
        # Wayback Machine of https://www.gov.gg/holidaydates
        self.assertHolidays(
            Guernsey(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-03", "May Day Bank Holiday"),
            ("2021-05-09", "Liberation Day"),
            ("2021-05-31", "Spring Bank Holiday"),
            ("2021-08-30", "Summer Bank Holiday"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Christmas Day (substitute day)"),
            ("2021-12-28", "Boxing Day (substitute day)"),
        )

    def test_2022(self):
        # Wayback Machine of https://www.gov.gg/holidaydates
        # https://www.bbc.com/news/world-europe-guernsey-62864318
        self.assertHolidays(
            Guernsey(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (substitute day)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day Bank Holiday"),
            ("2022-05-09", "Liberation Day"),
            ("2022-06-02", "Spring Bank Holiday"),
            ("2022-06-03", "Queen's Platinum Jubilee Bank Holiday"),
            ("2022-08-29", "Summer Bank Holiday"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (substitute day)"),
        )

    def test_2023(self):
        # https://www.gov.gg/holidaydates
        self.assertHolidays(
            Guernsey(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (substitute day)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "May Day Bank Holiday"),
            ("2023-05-08", "Extra Public Holiday for the Coronation of King Charles III"),
            ("2023-05-09", "Liberation Day"),
            ("2023-05-29", "Spring Bank Holiday"),
            ("2023-08-28", "Summer Bank Holiday"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        # https://www.gov.gg/holidaydates
        # https://www.bbc.co.uk/news/articles/c1441ddn87po
        self.assertHolidays(
            Guernsey(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day Bank Holiday"),
            ("2024-05-09", "Liberation Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-07-16", "The visit of His Majesty King Charles III and Queen Camilla"),
            ("2024-08-26", "Summer Bank Holiday"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        # https://www.gov.gg/holidaydates
        self.assertHolidays(
            Guernsey(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-05", "May Day Bank Holiday"),
            ("2025-05-09", "Liberation Day"),
            ("2025-05-26", "Spring Bank Holiday"),
            ("2025-08-25", "Summer Bank Holiday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
