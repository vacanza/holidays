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

from holidays.entities.ISO_3166.ET import EtHolidays
from tests.common import CommonCountryTests


class TestEtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EtHolidays, years=range(1940, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(EtHolidays(years=1896))

    def test_christmas(self):
        self.assertHolidayName("ገና", (f"{year}-01-07" for year in range(1940, 2050)))

    def test_ephiphany(self):
        name = "ጥምቀት"
        self.assertHolidayName(
            name, (f"{year}-01-19" for year in range(1940, 2050) if year % 4 != 0)
        )
        self.assertHolidayName(
            name, (f"{year}-01-20" for year in range(1940, 2050) if year % 4 == 0)
        )

    def test_adwa_victory(self):
        self.assertHolidayName("አድዋ", (f"{year}-03-02" for year in range(1940, 2050)))

    def test_good_friday(self):
        name = "ስቅለት"
        self.assertHolidayName(
            name,
            "2018-04-06",
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
        )
        self.assertHolidayName(name, range(1940, 2050))

    def test_easter(self):
        name = "ፋሲካ"
        self.assertHolidayName(
            name,
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
        )
        self.assertHolidayName(name, range(1940, 2050))

    def test_workers_day(self):
        self.assertHolidayName("የሰራተኞች ቀን", (f"{year}-05-01" for year in range(1940, 2050)))

    def test_patriots_day(self):
        name = "የአርበኞች ቀን"
        self.assertHolidayName(name, (f"{year}-05-05" for year in range(1942, 2050)))
        self.assertNoHolidayName(name, range(1940, 1942))

    def test_downfall_of_dergue(self):
        name = "ደርግ የወደቀበት ቀን"
        self.assertHolidayName(name, (f"{year}-05-28" for year in range(1992, 2050)))
        self.assertNoHolidayName(name, range(1940, 1992))

    def test_new_year(self):
        name = "እንቁጣጣሽ"
        self.assertHolidayName(
            name, (f"{year}-09-11" for year in range(1940, 2050) if year % 4 != 3)
        )
        self.assertHolidayName(
            name, (f"{year}-09-12" for year in range(1940, 2050) if year % 4 == 3)
        )

    def test_finding_of_true_cross(self):
        name = "መስቀል"
        self.assertHolidayName(
            name, (f"{year}-09-27" for year in range(1940, 2050) if year % 4 != 3)
        )
        self.assertHolidayName(
            name, (f"{year}-09-28" for year in range(1940, 2050) if year % 4 == 3)
        )

    def test_revolution_day(self):
        name = "የአብዮት ቀን"
        self.assertHolidayName(
            name, (f"{year}-09-12" for year in range(1975, 1991) if year % 4 != 3)
        )
        self.assertHolidayName(
            name, (f"{year}-09-13" for year in range(1975, 1991) if year % 4 == 3)
        )
        self.assertNoHolidayName(name, range(1940, 1975), range(1991, 2050))

    def test_october_revolution_day(self):
        name = "የጥቅምት አብዮት ቀን"
        self.assertHolidayName(name, (f"{year}-11-07" for year in range(1975, 1991)))
        self.assertNoHolidayName(name, range(1940, 1975), range(1991, 2050))

    def test_eid_al_fitr(self):
        self.assertHolidayName(
            "ኢድ አልፈጥር",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
        )

    def test_eid_al_adha(self):
        self.assertHolidayName(
            "አረፋ",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )

    def test_prophets_birthday(self):
        self.assertHolidayName(
            "መውሊድ",
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
        )
