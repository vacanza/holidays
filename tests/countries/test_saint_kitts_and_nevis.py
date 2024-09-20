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

from holidays.constants import HALF_DAY, PUBLIC, WORKDAY
from holidays.countries.saint_kitts_and_nevis import SaintKittsAndNevis, KN, KNA
from tests.common import CommonCountryTests


class TestSaintKittsAndNevis(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            SaintKittsAndNevis, years=range(1983, 2051), years_non_observed=range(1983, 2051)
        )

    def test_country_aliases(self):
        self.assertAliases(SaintKittsAndNevis, KN, KNA)

    def test_no_holidays(self):
        self.assertNoHolidays(
            SaintKittsAndNevis(categories=(HALF_DAY, PUBLIC, WORKDAY), years=1982)
        )

    def test_special_public_holidays(self):
        self.assertHoliday(
            SaintKittsAndNevis(categories=PUBLIC),
            "2015-02-18",
            "2017-09-20",
            "2017-12-19",
            "2022-08-08",
            "2023-07-04",
        )

    def test_special_half_day_holidays(self):
        self.assertHoliday(
            SaintKittsAndNevis(categories=HALF_DAY),
            "2017-03-23",
            "2017-04-10",
            "2018-12-31",
            "2019-12-31",
            "2022-04-27",
            "2023-07-20",
            "2023-12-30",
            "2024-08-01",
        )

    def test_labour_day(self):
        # 1st Monday of May.
        dt = (
            "2010-05-03",
            "2011-05-02",
            "2012-05-07",
            "2013-05-06",
            "2014-05-05",
            "2015-05-04",
            "2016-05-02",
            "2017-05-01",
            "2018-05-07",
            "2019-05-06",
            "2020-05-04",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
        )
        self.assertHolidayName("Labour Day", dt)

    def test_first_monday_of_august_holiday(self):
        name_first_mon_aug = "First Monday of August"
        name_emancipation_day = "Emancipation Day"

        dt = (
            "2010-08-02",
            "2011-08-01",
            "2012-08-06",
            "2013-08-05",
            "2014-08-04",
            "2015-08-03",
            "2016-08-01",
            "2017-08-07",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name_emancipation_day, dt)
        self.assertNoHolidayName(name_first_mon_aug, range(1998, 2051))
        self.assertNoHolidayName(name_emancipation_day, range(1983, 1998))

    def test_culturama_day_last_lap(self):
        name_culturama_day_last_lap = "Culturama Day - Last Lap"

        dt = (
            "2010-08-03",
            "2011-08-02",
            "2012-08-07",
            "2013-08-06",
            "2014-08-05",
            "2015-08-04",
            "2016-08-02",
            "2017-08-08",
            "2018-08-07",
            "2019-08-06",
            "2020-08-04",
            "2021-08-03",
            "2022-08-02",
            "2023-08-08",
            "2024-08-06",
        )
        self.assertHolidayName(name_culturama_day_last_lap, dt)

    def test_national_heroes_day(self):
        name_national_heroes_day = "National Heroes Day"

        self.assertNoHolidayName(name_national_heroes_day, range(1983, 1998))
        self.assertHolidayName(
            name_national_heroes_day, (f"{year}-09-16" for year in range(1998, 2051))
        )

        self.assertNoNonObservedHoliday(
            "2001-09-17",
            "2007-09-17",
            "2012-09-17",
            "2018-09-17",
            "2029-09-17",
            "2034-09-17",
            "2040-09-17",
            "2045-09-17",
        )

    def test_kim_collins_day(self):
        self.assertNoHoliday(SaintKittsAndNevis(categories=WORKDAY), 2002)
        self.assertHoliday(
            SaintKittsAndNevis(categories=WORKDAY),
            (f"{year}-08-25" for year in range(2003, 2051)),
        )

    def test_2015_holidays(self):  # ?
        # https://web.archive.org/web/20221102224614/https://www.gov.kn/in-skn-national-public-holidays/
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2015),
            ("2015-01-01", "Carnival Day"),
            ("2015-01-02", "Carnival Day - Last Lap"),
            ("2015-02-18", "Federal Election Victory Day"),
            ("2015-04-03", "Good Friday"),
            ("2015-04-06", "Easter Monday"),
            ("2015-05-04", "Labour Day"),
            ("2015-05-25", "Whit Monday"),
            ("2015-08-03", "Emancipation Day"),
            ("2015-08-04", "Culturama Day - Last Lap"),
            ("2015-08-25", "Kim Collins Day"),
            ("2015-09-16", "National Heroes Day"),
            ("2015-09-19", "Independence Day"),
            ("2015-12-25", "Christmas Day"),
            ("2015-12-26", "Boxing Day"),
        )

    def test_2021_holidays(self):
        # https://www.facebook.com/photo/?fbid=3623684614351340
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2021),
            ("2021-01-01", "Carnival Day"),
            ("2021-01-02", "Carnival Day - Last Lap"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-03", "Labour Day"),
            ("2021-05-24", "Whit Monday"),
            ("2021-08-02", "Emancipation Day"),
            ("2021-08-03", "Culturama Day - Last Lap"),
            ("2021-08-25", "Kim Collins Day"),
            ("2021-09-16", "National Heroes Day"),
            ("2021-09-19", "Independence Day"),
            ("2021-09-20", "Independence Day (observed)"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Boxing Day (observed)"),
        )

    def test_2022_holidays(self):
        # https://www.facebook.com/photo/?fbid=525835396250028
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2022),
            ("2022-01-01", "Carnival Day"),
            ("2022-01-02", "Carnival Day - Last Lap"),
            ("2022-01-03", "Carnival Day - Last Lap (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "Labour Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "Emancipation Day"),
            ("2022-08-02", "Culturama Day - Last Lap"),
            ("2022-08-08", "Federal Election Victory Day"),
            ("2022-08-25", "Kim Collins Day"),
            ("2022-09-16", "National Heroes Day"),
            ("2022-09-19", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023_holidays(self):
        # https://www.facebook.com/photo?fbid=525940556239512
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2023),
            ("2023-01-01", "Carnival Day"),
            ("2023-01-02", "Carnival Day - Last Lap"),
            ("2023-01-03", "Carnival Day (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-29", "Whit Monday"),
            (
                "2023-07-04",
                "50th Anniversary of the Establishment of the Caribbean Community (CARICOM)",
            ),
            ("2023-08-07", "Emancipation Day"),
            ("2023-08-08", "Culturama Day - Last Lap"),
            ("2023-09-16", "National Heroes Day"),
            ("2023-09-19", "Independence Day"),
            ("2023-08-25", "Kim Collins Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024_holidays(self):
        # https://www.facebook.com/photo/?fbid=769697881863777
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2024),
            ("2024-01-01", "Carnival Day"),
            ("2024-01-02", "Carnival Day - Last Lap"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "Labour Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-08-05", "Emancipation Day"),
            ("2024-08-06", "Culturama Day - Last Lap"),
            ("2024-09-16", "National Heroes Day"),
            ("2024-08-25", "Kim Collins Day"),
            ("2024-09-19", "Independence Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
