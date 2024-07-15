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

from holidays.entities.ISO_3166.JE import JeHolidays
from tests.common import CommonCountryTests


class TestJE(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JeHolidays, years=range(1952, 2070))

    def test_no_holidays(self):
        self.assertNoHolidays(JeHolidays(years=1951))

    def test_special_holidays(self):
        dt = (
            "1957-07-26",
            "1977-06-07",
            "1978-06-27",
            "1981-07-29",
            "1989-05-25",
            "1999-12-31",
            "2001-07-13",
            "2002-06-03",
            "2011-04-29",
            "2012-06-05",
            "2020-05-04",
            "2020-05-08",
            "2021-09-27",
            "2022-06-03",
            "2022-09-19",
            "2023-05-08",
        )
        dt_observed = (
            "1976-12-28",
            "1977-01-03",
            "1981-12-28",
            "1982-12-28",
            "1983-01-03",
            "1987-12-28",
            "1992-12-28",
            "1993-12-28",
            "1994-01-03",
            "1998-12-28",
            "1999-12-28",
            "2000-01-03",
            "2009-12-28",
        )
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_liberation_day(self):
        name = "Liberation Day"
        non_obs_date = (
            # Sunday, May 9th list 1952-2050 excl. 2010 (65th Anniversary)
            "1954-05-09",
            "1965-05-09",  # 20th Anniversary special? need to check
            "1971-05-09",
            "1976-05-09",
            "1982-05-09",
            "1993-05-09",
            "1999-05-09",
            "2004-05-09",
            "2021-05-09",
            "2027-05-09",
            "2032-05-09",
            "2038-05-09",
            "2049-05-09",
            # Saturday, May 9th list 1952-2010
            "1953-05-09",
            "1959-05-09",
            "1964-05-09",
            "1970-05-09",  # 25th Anniversary special? need to check
            "1981-05-09",
            "1987-05-09",
            "1992-05-09",
            "1998-05-09",
            "2009-05-09",
        )
        self.assertNoHolidayName(name, non_obs_date)
        self.assertHolidayName(name, range(2010, 2021))

    def test_2010(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2010),
            ("2010-01-01", "New Year's Day"),
            ("2010-04-02", "Good Friday"),
            ("2010-04-05", "Easter Monday"),
            ("2010-05-03", "May Day"),
            ("2010-05-09", "Liberation Day"),
            ("2010-05-31", "Spring Bank Holiday"),
            ("2010-08-30", "Late Summer Bank Holiday"),
            ("2010-12-25", "Christmas Day"),
            ("2010-12-26", "Boxing Day"),
            ("2010-12-27", "Christmas Day (observed)"),
            ("2010-12-28", "Boxing Day (observed)"),
        )

    def test_2011(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2011),
            ("2011-01-01", "New Year's Day"),
            ("2011-01-03", "New Year's Day (observed)"),
            ("2011-04-22", "Good Friday"),
            ("2011-04-25", "Easter Monday"),
            ("2011-04-29", "Wedding of William and Catherine"),
            ("2011-05-02", "May Day"),
            ("2011-05-09", "Liberation Day"),
            ("2011-05-30", "Spring Bank Holiday"),
            ("2011-08-29", "Late Summer Bank Holiday"),
            ("2011-12-25", "Christmas Day"),
            ("2011-12-26", "Boxing Day"),
            ("2011-12-27", "Christmas Day (observed)"),
        )

    def test_2012(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2012),
            ("2012-01-01", "New Year's Day"),
            ("2012-01-02", "New Year's Day (observed)"),
            ("2012-04-06", "Good Friday"),
            ("2012-04-09", "Easter Monday"),
            ("2012-05-07", "May Day"),
            ("2012-05-09", "Liberation Day"),
            ("2012-06-04", "Spring Bank Holiday"),
            ("2012-06-05", "Diamond Jubilee of Elizabeth II"),
            ("2012-08-27", "Late Summer Bank Holiday"),
            ("2012-12-25", "Christmas Day"),
            ("2012-12-26", "Boxing Day"),
        )

    def test_2013(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2013),
            ("2013-01-01", "New Year's Day"),
            ("2013-03-29", "Good Friday"),
            ("2013-04-01", "Easter Monday"),
            ("2013-05-06", "May Day"),
            ("2013-05-09", "Liberation Day"),
            ("2013-05-27", "Spring Bank Holiday"),
            ("2013-08-26", "Late Summer Bank Holiday"),
            ("2013-12-25", "Christmas Day"),
            ("2013-12-26", "Boxing Day"),
        )

    def test_2014(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2014),
            ("2014-01-01", "New Year's Day"),
            ("2014-04-18", "Good Friday"),
            ("2014-04-21", "Easter Monday"),
            ("2014-05-05", "May Day"),
            ("2014-05-09", "Liberation Day"),
            ("2014-05-26", "Spring Bank Holiday"),
            ("2014-08-25", "Late Summer Bank Holiday"),
            ("2014-12-25", "Christmas Day"),
            ("2014-12-26", "Boxing Day"),
        )

    def test_2015(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2015),
            ("2015-01-01", "New Year's Day"),
            ("2015-04-03", "Good Friday"),
            ("2015-04-06", "Easter Monday"),
            ("2015-05-04", "May Day"),
            ("2015-05-09", "Liberation Day"),
            ("2015-05-25", "Spring Bank Holiday"),
            ("2015-08-31", "Late Summer Bank Holiday"),
            ("2015-12-25", "Christmas Day"),
            ("2015-12-26", "Boxing Day"),
            ("2015-12-28", "Boxing Day (observed)"),
        )

    def test_2016(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2016),
            ("2016-01-01", "New Year's Day"),
            ("2016-03-25", "Good Friday"),
            ("2016-03-28", "Easter Monday"),
            ("2016-05-02", "May Day"),
            ("2016-05-09", "Liberation Day"),
            ("2016-05-30", "Spring Bank Holiday"),
            ("2016-08-29", "Late Summer Bank Holiday"),
            ("2016-12-25", "Christmas Day"),
            ("2016-12-26", "Boxing Day"),
            ("2016-12-27", "Christmas Day (observed)"),
        )

    def test_2017(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2017),
            ("2017-01-01", "New Year's Day"),
            ("2017-01-02", "New Year's Day (observed)"),
            ("2017-04-14", "Good Friday"),
            ("2017-04-17", "Easter Monday"),
            ("2017-05-01", "May Day"),
            ("2017-05-09", "Liberation Day"),
            ("2017-05-29", "Spring Bank Holiday"),
            ("2017-08-28", "Late Summer Bank Holiday"),
            ("2017-12-25", "Christmas Day"),
            ("2017-12-26", "Boxing Day"),
        )

    def test_2018(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2018),
            ("2018-01-01", "New Year's Day"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-05-07", "May Day"),
            ("2018-05-09", "Liberation Day"),
            ("2018-05-28", "Spring Bank Holiday"),
            ("2018-08-27", "Late Summer Bank Holiday"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Boxing Day"),
        )

    def test_2019(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2019),
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-05-06", "May Day"),
            ("2019-05-09", "Liberation Day"),
            ("2019-05-27", "Spring Bank Holiday"),
            ("2019-08-26", "Late Summer Bank Holiday"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Boxing Day"),
        )

    def test_2020(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-04", "May Day"),
            ("2020-05-08", "75th Anniversary of VE Day"),
            ("2020-05-09", "Liberation Day"),
            ("2020-05-25", "Spring Bank Holiday"),
            ("2020-08-31", "Late Summer Bank Holiday"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-12-28", "Boxing Day (observed)"),
        )

    def test_2021(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-03", "May Day"),
            ("2021-05-31", "Spring Bank Holiday"),
            ("2021-08-30", "Late Summer Bank Holiday"),
            ("2021-09-27", "250th Anniversary of the 1769 Corn Riots"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Christmas Day (observed)"),
            ("2021-12-28", "Boxing Day (observed)"),
        )

    def test_2022(self):
        # Wayback Machine of https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-05-09", "Liberation Day"),
            ("2022-06-02", "Spring Bank Holiday"),
            ("2022-06-03", "Platinum Jubilee of Elizabeth II"),
            ("2022-08-29", "Late Summer Bank Holiday"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023(self):
        # https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "May Day"),
            ("2023-05-08", "Coronation of Charles III"),
            ("2023-05-09", "Liberation Day"),
            ("2023-05-29", "Spring Bank Holiday"),
            ("2023-08-28", "Late Summer Bank Holiday"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        # https://www.gov.je/Leisure/Events/WhatsOn/Pages/BankHolidayDates.aspx
        self.assertHolidays(
            JeHolidays(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day"),
            ("2024-05-09", "Liberation Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
