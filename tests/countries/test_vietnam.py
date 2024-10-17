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

    def test_new_years_day(self):
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
            (2023, 1, 22),
            (2024, 2, 10),
        ):
            dt = date(*dts)
            self.assertHolidayName("Giao thừa Tết Nguyên Đán", _timedelta(dt, -1))
            self.assertHolidayName("Tết Nguyên Đán", dt)
            self.assertHolidayName("Mùng hai Tết Nguyên Đán", _timedelta(dt, +1))
            self.assertHolidayName("Mùng ba Tết Nguyên Đán", _timedelta(dt, +2))
            if dt.year >= 2013:
                self.assertHolidayName("Mùng bốn Tết Nguyên Đán", _timedelta(dt, +3))

    def test_hung_kings_day(self):
        self.assertHolidayName(
            "Ngày Giỗ Tổ Hùng Vương",
            "2007-04-26",
            "2008-04-15",
            "2009-04-05",
            "2010-04-23",
            "2011-04-12",
            "2012-03-31",
            "2013-04-19",
            "2014-04-09",
            "2015-04-28",
            "2016-04-16",
            "2017-04-06",
            "2018-04-25",
            "2019-04-14",
            "2020-04-02",
            "2021-04-21",
            "2022-04-10",
            "2023-04-29",
            "2024-04-18",
        )

    def test_liberation_day(self):
        self.assertHolidayName("Ngày Chiến thắng", (f"{year}-04-30" for year in range(1979, 2050)))

    def test_international_labor_day(self):
        self.assertHolidayName(
            "Ngày Quốc tế Lao động", (f"{year}-05-01" for year in range(1979, 2050))
        )

    def test_national_day(self):
        self.assertHolidayName(
            "Quốc khánh",
            (f"{year}-09-02" for year in range(1979, 2050)),
            "2021-09-03",
            "2022-09-01",
            "2023-09-01",
            "2024-09-03",
        )

    def test_observed(self):
        observed_holidays = (
            # New Year's Day.
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            # Lunar New Year.
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
            # Hung Kings' Commemoration Day.
            "2009-04-06",
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
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tết Dương lịch"),
            ("2022-01-03", "Tết Dương lịch (nghỉ bù)"),
            ("2022-01-31", "Giao thừa Tết Nguyên Đán"),
            ("2022-02-01", "Tết Nguyên Đán"),
            ("2022-02-02", "Mùng hai Tết Nguyên Đán"),
            ("2022-02-03", "Mùng ba Tết Nguyên Đán"),
            ("2022-02-04", "Mùng bốn Tết Nguyên Đán"),
            ("2022-04-10", "Ngày Giỗ Tổ Hùng Vương"),
            ("2022-04-11", "Ngày Giỗ Tổ Hùng Vương (nghỉ bù)"),
            ("2022-04-30", "Ngày Chiến thắng"),
            ("2022-05-01", "Ngày Quốc tế Lao động"),
            ("2022-05-02", "Ngày Chiến thắng (nghỉ bù)"),
            ("2022-05-03", "Ngày Quốc tế Lao động (nghỉ bù)"),
            ("2022-09-01", "Quốc khánh"),
            ("2022-09-02", "Quốc khánh"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-31", "Lunar New Year's Eve"),
            ("2022-02-01", "Lunar New Year"),
            ("2022-02-02", "Second Day of Lunar New Year"),
            ("2022-02-03", "Third Day of Lunar New Year"),
            ("2022-02-04", "Fourth Day of Lunar New Year"),
            ("2022-04-10", "Hung Kings' Commemoration Day"),
            ("2022-04-11", "Hung Kings' Commemoration Day (observed)"),
            ("2022-04-30", "Liberation Day/Reunification Day"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Liberation Day/Reunification Day (observed)"),
            ("2022-05-03", "International Labor Day (observed)"),
            ("2022-09-01", "National Day"),
            ("2022-09-02", "National Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-03", "ชดเชยวันปีใหม่สากล"),
            ("2022-01-31", "วันก่อนวันตรุษเต๊ต"),
            ("2022-02-01", "วันตรุษเต๊ต"),
            ("2022-02-02", "วันตรุษเต๊ตวันที่สอง"),
            ("2022-02-03", "วันตรุษเต๊ตวันที่สาม"),
            ("2022-02-04", "วันตรุษเต๊ตวันที่สี่"),
            ("2022-04-10", "วันสักการะบูชาบรรพกษัตริย์หุ่ง"),
            ("2022-04-11", "ชดเชยวันสักการะบูชาบรรพกษัตริย์หุ่ง"),
            ("2022-04-30", "วันปลดปล่อยภาคใต้เพื่อรวมชาติ"),
            ("2022-05-01", "วันแรงงานสากล"),
            ("2022-05-02", "ชดเชยวันปลดปล่อยภาคใต้เพื่อรวมชาติ"),
            ("2022-05-03", "ชดเชยวันแรงงานสากล"),
            ("2022-09-01", "วันชาติเวียตนาม"),
            ("2022-09-02", "วันชาติเวียตนาม"),
        )
