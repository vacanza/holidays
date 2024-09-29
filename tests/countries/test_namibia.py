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

from holidays.countries.namibia import Namibia, NA, NAM
from tests.common import CommonCountryTests


class TestNamibia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Namibia, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertAliases(Namibia, NA, NAM)

    def test_no_holidays(self):
        self.assertNoHolidays(Namibia(years=1989))

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-12-31",
            "2000-01-03",
        )

    def test_holidays(self):
        for year in range(1990, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-03-21",
                f"{year}-05-01",
                f"{year}-05-04",
                f"{year}-05-25",
                f"{year}-08-26",
                f"{year}-09-10",
                f"{year}-12-25",
                f"{year}-12-26",
            )
        self.assertNoHolidayName(
            "Day of the Namibian Women and International Human Rights Day", range(1990, 2005)
        )
        self.assertHolidayName(
            "International Human Rights Day", (f"{year}-09-10" for year in range(1990, 2005))
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
            # Ascension Day
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
        )

    def test_observed(self):
        dt = (
            "2010-03-22",
            "2010-12-27",
            "2011-05-02",
            "2012-01-02",
            "2012-08-27",
            "2014-05-05",
            "2014-05-26",
            "2016-05-02",
            "2017-01-02",
            "2017-09-11",
            "2018-08-27",
            "2021-03-22",
            "2021-12-27",
            "2022-05-02",
            "2023-01-02",
            "2023-09-11",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
