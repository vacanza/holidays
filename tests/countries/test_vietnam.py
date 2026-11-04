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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.countries.vietnam import Vietnam
from tests.common import CommonCountryTests, WorkingDayTests


class TestVietnam(CommonCountryTests, WorkingDayTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Vietnam)

    def test_substituted_holidays(self):
        self.assertHoliday(
            "2010-02-19",
            "2012-01-27",
            "2013-04-29",
            "2014-05-02",
            "2014-09-01",
            "2015-01-02",
            "2015-02-16",
            "2015-04-29",
            "2018-12-31",
            "2019-04-29",
            "2024-04-29",
            "2025-05-02",
            "2026-08-31",
        )

    def test_workdays(self):
        self.assertWorkingDay(
            "2010-02-27",
            "2012-02-04",
            "2013-05-04",
            "2014-04-26",
            "2014-09-06",
            "2014-12-27",
            "2015-02-14",
            "2015-04-25",
            "2019-01-05",
            "2019-05-04",
            "2024-05-04",
            "2025-04-26",
            "2026-08-22",
        )

        for year, dts in {
            2014: (
                "2014-04-26",
                "2014-09-06",
                "2014-12-27",
            ),
            2019: ("2019-01-05",),
        }.items():
            self.assertWorkingDay(Vietnam(years=year), dts)

    def test_new_years_day(self):
        name = "Tết Dương lịch"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (nghỉ bù)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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
            (2023, 1, 22),
            (2024, 2, 10),
            (2025, 1, 29),
            (2026, 2, 17),
        ):
            dt = date(*dts)
            self.assertHolidayName("Giao thừa Tết Nguyên Đán", _timedelta(dt, -1))
            self.assertHolidayName("Tết Nguyên Đán", dt)
            self.assertHolidayName("Mùng hai Tết Nguyên Đán", _timedelta(dt, +1))
            self.assertHolidayName("Mùng ba Tết Nguyên Đán", _timedelta(dt, +2))
            if dt.year >= 2013:
                self.assertHolidayName("Mùng bốn Tết Nguyên Đán", _timedelta(dt, +3))
        obs_dts = (
            "2012-01-26",
            "2013-02-14",
            "2013-02-15",
            "2014-01-29",
            "2014-02-04",
            "2015-02-17",
            "2015-02-23",
            "2016-02-12",
            "2017-01-26",
            "2017-02-01",
            "2018-02-14",
            "2018-02-20",
            "2020-01-23",
            "2020-01-29",
            "2021-02-10",
            "2021-02-16",
            "2023-01-20",
            "2023-01-26",
            "2024-02-08",
            "2024-02-14",
        )
        self.assertHoliday(obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_hung_kings_commemoration_day(self):
        name = "Ngày Giỗ Tổ Hùng Vương"
        self.assertHolidayName(
            name,
            "2020-04-02",
            "2021-04-21",
            "2022-04-10",
            "2023-04-29",
            "2024-04-18",
            "2025-04-07",
            "2026-04-26",
        )
        self.assertHolidayName(name, range(2007, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2007))
        obs_dts = (
            "2016-04-18",
            "2019-04-15",
            "2022-04-11",
            "2023-05-02",
            "2026-04-27",
        )
        self.assertHolidayName(f"{name} (nghỉ bù)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_liberation_day_reunification_day(self):
        name = "Ngày Chiến thắng"
        self.assertHolidayName(name, (f"{year}-04-30" for year in self.full_range))
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
            "2017-05-02",
            "2022-05-02",
            "2023-05-03",
        )
        self.assertHolidayName(f"{name} (nghỉ bù)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_labor_day(self):
        name = "Ngày Quốc tế Lao động"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2010-05-03",
            "2011-05-03",
            "2016-05-03",
            "2021-05-03",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (nghỉ bù)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_day(self):
        name = "Quốc khánh"
        self.assertHolidayName(name, (f"{year}-09-02" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2021-09-03",
            "2022-09-01",
            "2023-09-01",
            "2024-09-03",
            "2025-09-01",
            "2026-09-01",
        )
        self.assertHolidayNameCount(name, 2, range(2021, self.end_year))
        obs_dts = (
            "2007-09-03",
            "2012-09-03",
            "2017-09-04",
            "2018-09-03",
            "2023-09-04",
        )
        self.assertHolidayName(f"{name} (nghỉ bù)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_vietnam_cultural_day(self):
        name = "Ngày Văn hóa Việt Nam"
        self.assertHolidayName(name, (f"{year}-11-24" for year in range(2026, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2026))
        obs_dts = (
            "2029-11-26",
            "2030-11-25",
        )
        self.assertHolidayName(f"{name} (nghỉ bù)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Tết Dương lịch"),
            ("2025-01-27", "29 Tết"),
            ("2025-01-28", "Giao thừa Tết Nguyên Đán"),
            ("2025-01-29", "Tết Nguyên Đán"),
            ("2025-01-30", "Mùng hai Tết Nguyên Đán"),
            ("2025-01-31", "Mùng ba Tết Nguyên Đán"),
            ("2025-02-01", "Mùng bốn Tết Nguyên Đán"),
            ("2025-04-07", "Ngày Giỗ Tổ Hùng Vương"),
            ("2025-04-30", "Ngày Chiến thắng"),
            ("2025-05-01", "Ngày Quốc tế Lao động"),
            ("2025-05-02", "Ngày nghỉ (thay cho ngày 26/04/2025)"),
            ("2025-09-01", "Quốc khánh"),
            ("2025-09-02", "Quốc khánh"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "Tết Dương lịch"),
            ("2026-02-16", "Giao thừa Tết Nguyên Đán"),
            ("2026-02-17", "Tết Nguyên Đán"),
            ("2026-02-18", "Mùng hai Tết Nguyên Đán"),
            ("2026-02-19", "Mùng ba Tết Nguyên Đán"),
            ("2026-02-20", "Mùng bốn Tết Nguyên Đán"),
            ("2026-04-26", "Ngày Giỗ Tổ Hùng Vương"),
            ("2026-04-27", "Ngày Giỗ Tổ Hùng Vương (nghỉ bù)"),
            ("2026-04-30", "Ngày Chiến thắng"),
            ("2026-05-01", "Ngày Quốc tế Lao động"),
            ("2026-08-31", "Ngày nghỉ (thay cho ngày 22/08/2026)"),
            ("2026-09-01", "Quốc khánh"),
            ("2026-09-02", "Quốc khánh"),
            ("2026-11-24", "Ngày Văn hóa Việt Nam"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-02-16", "Lunar New Year's Eve"),
            ("2026-02-17", "Lunar New Year"),
            ("2026-02-18", "Second Day of Lunar New Year"),
            ("2026-02-19", "Third Day of Lunar New Year"),
            ("2026-02-20", "Fourth Day of Lunar New Year"),
            ("2026-04-26", "Hung Kings' Commemoration Day"),
            ("2026-04-27", "Hung Kings' Commemoration Day (observed)"),
            ("2026-04-30", "Liberation Day/Reunification Day"),
            ("2026-05-01", "International Labor Day"),
            ("2026-08-31", "Day off (substituted from 08/22/2026)"),
            ("2026-09-01", "National Day"),
            ("2026-09-02", "National Day"),
            ("2026-11-24", "Vietnam Cultural Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2026-01-01", "วันปีใหม่สากล"),
            ("2026-02-16", "วันก่อนวันตรุษเต๊ต"),
            ("2026-02-17", "วันตรุษเต๊ต"),
            ("2026-02-18", "วันตรุษเต๊ตวันที่สอง"),
            ("2026-02-19", "วันตรุษเต๊ตวันที่สาม"),
            ("2026-02-20", "วันตรุษเต๊ตวันที่สี่"),
            ("2026-04-26", "วันสักการะบูชาบรรพกษัตริย์หุ่ง"),
            ("2026-04-27", "ชดเชยวันสักการะบูชาบรรพกษัตริย์หุ่ง"),
            ("2026-04-30", "วันปลดปล่อยภาคใต้เพื่อรวมชาติ"),
            ("2026-05-01", "วันแรงงานสากล"),
            ("2026-08-31", "วันหยุด (แทน 22/08/2026)"),
            ("2026-09-01", "วันชาติเวียตนาม"),
            ("2026-09-02", "วันชาติเวียตนาม"),
            ("2026-11-24", "วันวัฒนธรรมเวียดนาม"),
        )
