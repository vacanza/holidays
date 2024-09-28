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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.countries.vietnam import Vietnam, VN, VNM
from tests.common import CommonCountryTests


class TestVietnam(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Vietnam, years=range(1979, 2050))

    def test_country_aliases(self):
        self.assertAliases(Vietnam, VN, VNM)

    def test_common(self):
        self.assertHolidayName(
            "Tết Dương lịch",
            "2020-01-01",
        )

    def test_first_day_of_january(self):
        self.assertHolidayName("Tết Dương lịch", (f"{year}-01-01" for year in range(1979, 2050)))

    def test_lunar_new_year(self):
        for dts in (
            (1997, 2, 7),
            (2008, 2, 7),
            (2009, 1, 26),
            (2010, 2, 14),
            (2011, 2, 3),
            (2012, 1, 23),
            (2013, 2, 10),
            (2014, 1, 31),
            (2015, 2, 19),
            (2016, 2, 8),
            (2017, 1, 28),
            (2018, 2, 16),
            (2019, 2, 5),
            (2020, 1, 25),
            (2021, 2, 12),
            (2022, 2, 1),
        ):
            dt = date(*dts)
            self.assertHolidayName("Giao thừa Tết Nguyên Đán", _timedelta(dt, -1))
            self.assertHolidayName("Tết Nguyên Đán", dt)
            self.assertHolidayName("Mùng hai Tết Nguyên Đán", _timedelta(dt, +1))
            self.assertHolidayName("Mùng ba Tết Nguyên Đán", _timedelta(dt, +2))
            self.assertHolidayName("Mùng bốn Tết Nguyên Đán", _timedelta(dt, +3))
            self.assertHolidayName("Mùng năm Tết Nguyên Đán", _timedelta(dt, +4))

    def test_king_hung_day(self):
        self.assertHolidayName(
            "Ngày Giỗ Tổ Hùng Vương",
            "2020-04-02",
            "2021-04-21",
            "2022-04-10",
        )

    def test_liberation_day(self):
        self.assertHolidayName("Ngày Chiến thắng", (f"{year}-04-30" for year in range(1979, 2050)))

    def test_international_labor_day(self):
        self.assertHolidayName(
            "Ngày Quốc tế Lao động", (f"{year}-05-01" for year in range(1979, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName("Quốc khánh", (f"{year}-09-02" for year in range(1979, 2050)))

    def test_observed(self):
        observed_holidays = (
            # New Year's Day.
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            # Hung Kings' Commemoration Day.
            "2012-04-02",
            "2016-04-18",
            "2019-04-15",
            "2022-04-11",
            "2023-05-02",
            # Liberation Day/Reunification Day.
            "2011-05-02",
            "2016-05-02",
            "2017-05-02",
            "2022-05-02",
            "2023-05-03",
            # International Labor Day.
            "2011-05-03",
            "2016-05-03",
            "2021-05-03",
            "2022-05-03",
            # National Day.
            "2012-09-03",
            "2017-09-04",
            "2018-09-03",
            "2023-09-04",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tết Dương lịch"),
            ("2022-01-03", "Tết Dương lịch (nghỉ bù)"),
            ("2022-01-31", "Giao thừa Tết Nguyên Đán"),
            ("2022-02-01", "Tết Nguyên Đán"),
            ("2022-02-02", "Mùng hai Tết Nguyên Đán"),
            ("2022-02-03", "Mùng ba Tết Nguyên Đán"),
            ("2022-02-04", "Mùng bốn Tết Nguyên Đán"),
            ("2022-02-05", "Mùng năm Tết Nguyên Đán"),
            ("2022-04-10", "Ngày Giỗ Tổ Hùng Vương"),
            ("2022-04-11", "Ngày Giỗ Tổ Hùng Vương (nghỉ bù)"),
            ("2022-04-30", "Ngày Chiến thắng"),
            ("2022-05-01", "Ngày Quốc tế Lao động"),
            ("2022-05-02", "Ngày Chiến thắng (nghỉ bù)"),
            ("2022-05-03", "Ngày Quốc tế Lao động (nghỉ bù)"),
            ("2022-09-02", "Quốc khánh"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-31", "Lunar New Year's Eve"),
            ("2022-02-01", "Lunar New Year"),
            ("2022-02-02", "The second day of Tet Holiday"),
            ("2022-02-03", "The third day of Tet Holiday"),
            ("2022-02-04", "The fourth day of Tet Holiday"),
            ("2022-02-05", "The fifth day of Tet Holiday"),
            ("2022-04-10", "Hung Kings' Commemoration Day"),
            ("2022-04-11", "Hung Kings' Commemoration Day (observed)"),
            ("2022-04-30", "Liberation Day/Reunification Day"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Liberation Day/Reunification Day (observed)"),
            ("2022-05-03", "International Labor Day (observed)"),
            ("2022-09-02", "National Day"),
        )
