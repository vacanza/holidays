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

from holidays.countries.albania import Albania, AL, ALB
from tests.common import CommonCountryTests


class TestAlbania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Albania, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertAliases(Albania, AL, ALB)

    def test_special_holidays(self):
        self.assertHoliday("2022-03-21")

    def test_holidays(self):
        for year in range(1990, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-01-02",
                f"{year}-05-01",
                f"{year}-11-28",
                f"{year}-11-29",
                f"{year}-12-25",
            )

        self.assertNoHolidayName("Summer Day", range(1990, 2004))
        self.assertHoliday(f"{year}-03-14" for year in range(2004, 2050))

        self.assertNoHolidayName("Nevruz", range(1990, 1996))
        self.assertHoliday(f"{year}-03-22" for year in range(1996, 2050))

        self.assertNoHolidayName("National Youth Day", range(1990, 2009))
        self.assertHoliday(f"{year}-12-08" for year in range(2009, 2050))

    def test_easter(self):
        self.assertHoliday(
            # Catholic Easter
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            # Orthodox Easter
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
        )

    def test_islamic_holidays(self):
        self.assertHoliday(
            # Eid al-Fitr
            "2015-07-17",
            "2016-07-06",
            "2017-06-25",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            # Eid al-Adha
            "2006-01-10",
            "2006-12-31",
            "2015-09-23",
            "2016-09-11",
            "2017-09-01",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
        )

    def test_mother_teresa_day(self):
        name = "Mother Teresa Beatification Day"
        self.assertHolidayName(name, (f"{year}-10-19" for year in range(2004, 2018)))
        self.assertNoHolidayName(name, range(1990, 2004), range(2018, 2050))

        name = "Mother Teresa Canonization Day"
        self.assertNoHolidayName(name, range(1990, 2018))
        self.assertHolidayName(name, (f"{year}-09-05" for year in range(2018, 2050)))

    def test_observed(self):
        dt = (
            # New Year's Day
            "2012-01-03",
            "2016-01-04",
            "2017-01-03",
            "2021-01-04",
            "2022-01-03",
            "2022-01-04",
            "2023-01-03",
            # Summer Day
            "2010-03-15",
            "2015-03-16",
            "2020-03-16",
            "2021-03-15",
            # Nevruz
            "2014-03-24",
            "2015-03-23",
            "2020-03-23",
            # May Day
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            # Mother Teresa ... Day
            "2013-10-21",
            "2014-10-20",
            "2020-09-07",
            "2021-09-06",
            # Independence Day
            "2010-11-30",
            "2015-11-30",
            "2020-11-30",
            "2021-11-30",
            # Liberation Day
            "2014-12-01",
            "2015-12-01",
            "2020-12-01",
            # National Youth Day
            "2012-12-10",
            "2013-12-09",
            "2018-12-10",
            "2019-12-09",
            "2024-12-09",
            # Christmas Day
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
            # Eid al-Fitr
            "2012-08-20",
            "2017-06-26",
            "2020-05-25",
            # Eid al-Adha
            "2007-01-03",
            "2014-10-06",
            "2016-09-12",
            "2019-08-12",
            "2022-07-11",
            "2024-06-17",
            # special cases
            # Catholic Easter
            "2008-03-25",
            # Orthodox Easter
            "1989-05-02",
            "2000-05-02",
            "2021-05-04",
            "2027-05-04",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            Albania(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-04", "New Year's Day (observed)"),
            ("2022-03-14", "Summer Day"),
            ("2022-03-21", "Public Holiday"),
            ("2022-03-22", "Nevruz"),
            ("2022-04-17", "Catholic Easter"),
            ("2022-04-18", "Catholic Easter (observed)"),
            ("2022-04-24", "Orthodox Easter"),
            ("2022-04-25", "Orthodox Easter (observed)"),
            ("2022-05-01", "May Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "May Day (observed)"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-11", "Eid al-Adha (estimated) (observed)"),
            ("2022-09-05", "Mother Teresa Canonization Day"),
            ("2022-11-28", "Independence Day"),
            ("2022-11-29", "Liberation Day"),
            ("2022-12-08", "National Youth Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Albania(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day"),
            ("2023-01-03", "New Year's Day (observed)"),
            ("2023-03-14", "Summer Day"),
            ("2023-03-22", "Nevruz"),
            ("2023-04-09", "Catholic Easter"),
            ("2023-04-10", "Catholic Easter (observed)"),
            ("2023-04-16", "Orthodox Easter"),
            ("2023-04-17", "Orthodox Easter (observed)"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-05-01", "May Day"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-09-05", "Mother Teresa Canonization Day"),
            ("2023-11-28", "Independence Day"),
            ("2023-11-29", "Liberation Day"),
            ("2023-12-08", "National Youth Day"),
            ("2023-12-25", "Christmas Day"),
        )
