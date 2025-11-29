#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.nauru import Nauru
from tests.common import CommonCountryTests


class TestNauru(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1969, 2050)
        super().setUpClass(Nauru, years=years, years_non_observed=years)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1969, 2050)))
        dt = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        name_after = f"Day following {name}"
        self.assertHolidayName(name, (f"{year}-01-31" for year in range(1969, 2050)))
        self.assertHolidayName(name_after, (f"{year}-02-01" for year in range(1969, 2050)))
        dt = (
            "2004-02-02",
            "2009-02-02",
            "2010-02-02",
            "2015-02-02",
            "2016-02-02",
            "2021-02-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        dt_after = (
            "2003-02-03",
            "2004-02-03",
            "2009-02-03",
            "2014-02-03",
            "2015-02-03",
            "2020-02-03",
        )
        self.assertHolidayName(f"{name_after} (observed)", dt_after)
        self.assertNoNonObservedHoliday(dt, dt_after)

    def test_international_womens_day(self):
        name = "International Women's Day"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(2019, 2050)))
        self.assertNoHolidayName(name, range(1969, 2019))
        dt = (
            "2020-03-09",
            "2025-03-10",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1969, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1969, 2050))

    def test_easter_tuesday(self):
        name = "Easter Tuesday"
        self.assertHolidayName(
            name,
            "2020-04-14",
            "2021-04-06",
            "2022-04-19",
            "2023-04-11",
            "2024-04-02",
            "2025-04-22",
        )
        self.assertHolidayName(name, range(1969, 2050))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-05-17" for year in range(1969, 2050)))
        dt = (
            "2003-05-19",
            "2008-05-19",
            "2009-05-18",
            "2014-05-19",
            "2015-05-18",
            "2020-05-18",
            "2025-05-19",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_ronphos_handover(self):
        name = "RONPHOS Handover"
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2018, 2050)))
        self.assertNoHolidayName(name, range(1969, 2018))
        dt = (
            "2018-07-02",
            "2023-07-03",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_ibumin_earoeni_day(self):
        name = "Ibumin Earoeni Day"
        self.assertHolidayName(name, (f"{year}-08-19" for year in range(2019, 2050)))
        self.assertNoHolidayName(name, range(1969, 2019))
        dt = ("2023-08-21",)
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_youth_day(self):
        name = "National Youth Day"
        self.assertHolidayName(name, (f"{year}-09-25" for year in range(2001, 2020)))
        self.assertNoHolidayName(name, range(1969, 2001), range(2020, 2050))
        dt = (
            "2004-09-27",
            "2005-09-26",
            "2010-09-27",
            "2011-09-26",
            "2016-09-26",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_sir_hammer_deroburt_day(self):
        name = "Sir Hammer DeRoburt Day"
        self.assertHolidayName(name, (f"{year}-09-25" for year in range(2020, 2050)))
        self.assertNoHolidayName(name, range(1969, 2020))
        dt = (
            "2021-09-27",
            "2022-09-26",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_angam_day(self):
        name = "Angam Day"
        self.assertHolidayName(name, (f"{year}-10-26" for year in range(1969, 2050)))
        dt = (
            "2002-10-28",
            "2003-10-27",
            "2008-10-27",
            "2013-10-28",
            "2014-10-27",
            "2019-10-28",
            "2024-10-28",
            "2025-10-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1969, 2050)))
        dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_day_following_christmas(self):
        name = "Day following Christmas"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1969, 2050)))
        dt = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2024(self):
        self.assertHolidays(
            Nauru(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-31", "Independence Day"),
            ("2024-02-01", "Day following Independence Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-02", "Easter Tuesday"),
            ("2024-05-17", "Constitution Day"),
            ("2024-07-01", "RONPHOS Handover"),
            ("2024-08-19", "Ibumin Earoeni Day"),
            ("2024-09-25", "Sir Hammer DeRoburt Day"),
            ("2024-10-26", "Angam Day"),
            ("2024-10-28", "Angam Day (observed)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Day following Christmas"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-31", "Independence Day"),
            ("2025-02-01", "Day following Independence Day"),
            ("2025-02-03", "Day following Independence Day (observed)"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-10", "International Women's Day (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-22", "Easter Tuesday"),
            ("2025-05-17", "Constitution Day"),
            ("2025-05-19", "Constitution Day (observed)"),
            ("2025-07-01", "RONPHOS Handover"),
            ("2025-08-19", "Ibumin Earoeni Day"),
            ("2025-09-25", "Sir Hammer DeRoburt Day"),
            ("2025-10-26", "Angam Day"),
            ("2025-10-27", "Angam Day (observed)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day following Christmas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-31", "Independence Day"),
            ("2025-02-01", "Day following Independence Day"),
            ("2025-02-03", "Day following Independence Day (observed)"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-10", "International Women's Day (observed)"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-22", "Easter Tuesday"),
            ("2025-05-17", "Constitution Day"),
            ("2025-05-19", "Constitution Day (observed)"),
            ("2025-07-01", "RONPHOS Handover"),
            ("2025-08-19", "Ibumin Earoeni Day"),
            ("2025-09-25", "Sir Hammer DeRoburt Day"),
            ("2025-10-26", "Angam Day"),
            ("2025-10-27", "Angam Day (observed)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day following Christmas"),
        )
