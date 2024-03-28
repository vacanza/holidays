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

from holidays.countries.malawi import Malawi, MW, MWI
from tests.common import CommonCountryTests


class TestMalawi(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass(Malawi)

    def test_country_aliases(self):
        self.assertAliases(Malawi, MW, MWI)

    def test_no_holidays(self):
        self.assertNoHolidays(Malawi(years=1999))

    def test_holidays(self):
        for year in range(2000, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-01-15",
                f"{year}-03-03",
                f"{year}-05-01",
                f"{year}-05-14",
                f"{year}-07-06",
                f"{year}-10-15",
                f"{year}-12-25",
                f"{year}-12-26",
            )

    def test_easter(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_observed(self):
        dt = (
            # New Year's Day
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
            # John Chilembwe Day
            "2011-01-17",
            "2012-01-16",
            "2017-01-16",
            "2022-01-17",
            "2023-01-16",
            # Martyrs Day
            "2012-03-05",
            "2013-03-04",
            "2018-03-05",
            "2019-03-04",
            "2024-03-04",
            # Labour Day
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
            # Kamuzu Day
            "2011-05-16",
            "2016-05-16",
            "2017-05-15",
            "2022-05-16",
            "2023-05-15",
            # Independence Day
            "2013-07-08",
            "2014-07-07",
            "2019-07-08",
            "2024-07-08",
            # Mother's Day
            "2011-10-17",
            "2016-10-17",
            "2017-10-16",
            "2022-10-17",
            "2023-10-16",
            # Christmas Day
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
            # Boxing Day
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
