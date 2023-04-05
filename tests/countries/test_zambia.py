#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.zambia import Zambia, ZM, ZMB
from tests.common import TestCase


class TestZambia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Zambia)

    def test_country_aliases(self):
        self.assertCountryAliases(Zambia, ZM, ZMB)

    def test_no_holidays(self):
        self.assertNoHolidays(Zambia(years=1964))

    def test_special_holidays(self):
        self.assertHoliday(
            "2016-08-11",
            "2016-09-13",
            "2018-03-09",
            "2018-07-26",
            "2021-07-02",
            "2021-07-07",
            "2021-08-12",
            "2021-08-13",
            "2021-08-24",
            "2022-03-18",
        )

    def test_holidays(self):
        for year in range(1965, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-03-12",
                f"{year}-05-01",
                f"{year}-05-25",
                f"{year}-10-24",
                f"{year}-12-25",
            )

        self.assertNoHoliday(f"{year}-03-08" for year in range(1965, 1991))
        self.assertNoHolidayName(
            "International Women's Day", Zambia(years=range(1965, 1991))
        )
        self.assertHoliday(f"{year}-03-08" for year in range(1991, 2050))

        self.assertNoHoliday(f"{year}-04-28" for year in range(1965, 2022))
        self.assertNoHolidayName(
            "Kenneth Kaunda Day", Zambia(years=range(1965, 2022))
        )
        self.assertHoliday(f"{year}-04-28" for year in range(2022, 2050))

        self.assertNoHoliday(f"{year}-10-18" for year in range(1965, 2015))
        self.assertNoHolidayName(
            "National Prayer Day", Zambia(years=range(1965, 2015))
        )
        self.assertHoliday(f"{year}-10-18" for year in range(2015, 2050))

    def test_easter(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            # Holy Saturday
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_moving_holidays(self):
        self.assertHoliday(
            # Heroes' Day
            "2018-07-02",
            "2019-07-01",
            "2020-07-06",
            "2021-07-05",
            "2022-07-04",
            # Unity Day
            "2018-07-03",
            "2019-07-02",
            "2020-07-07",
            "2021-07-06",
            "2022-07-05",
            # Farmers' Day
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
        )

    def test_observed(self):
        dt = (
            "2000-03-13",
            "2003-05-26",
            "2004-10-25",
            "2005-05-02",
            "2005-12-26",
            "2006-01-02",
            "2006-03-13",
            "2008-05-26",
            "2009-03-09",
            "2010-10-25",
            "2011-05-02",
            "2011-12-26",
            "2012-01-02",
            "2014-05-26",
            "2015-03-09",
            "2015-10-19",
            "2016-05-02",
            "2016-12-26",
            "2017-01-02",
            "2017-03-13",
            "2020-03-09",
            "2020-10-19",
            "2021-10-25",
            "2022-05-02",
            "2022-12-26",
            "2023-01-02",
            "2023-03-13",
            "2024-04-29",
            "2030-04-29",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
