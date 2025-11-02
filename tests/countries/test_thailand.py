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

from holidays.constants import ARMED_FORCES, BANK, GOVERNMENT, SCHOOL, WORKDAY
from holidays.countries.thailand import Thailand
from tests.common import CommonCountryTests


class TestThailand(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        support_range = range(1914, 2050)
        super().setUpClass(Thailand, years=support_range, years_non_observed=support_range)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Thailand(years=1942, categories=BANK))
        self.assertNoHolidays(Thailand(years=1956, categories=(GOVERNMENT, SCHOOL)))
        self.assertNoHolidays(Thailand(years=1958, categories=ARMED_FORCES))

    def test_special_holidays(self):
        dt = (
            # 1992-1994 (include In Lieus, Checked with Bank of Thailand Data).
            "1992-05-18",
            "1992-12-07",
            "1993-03-08",
            "1993-05-03",
            "1993-10-25",
            "1993-12-06",
            "1994-01-03",
            "1994-05-02",
            "1994-07-25",
            "1994-10-24",
            "1994-12-12",
            # 1995-1997 (Bank of Thailand Data).
            "1996-06-10",
            # 1998-2000 (include In Lieus, Checked with Bank of Thailand Data).
            "1998-05-11",
            "1998-12-07",
            "1999-05-03",
            "1999-05-31",
            "1999-10-25",
            "1999-12-06",
            "2000-01-03",
            "2000-02-21",
            "2000-08-14",
            "2000-12-11",
            "2000-12-29",
            # From 2001 Onwards (Checked with Bank of Thailand Data).
            "2006-04-19",
            "2006-06-09",
            "2006-06-12",
            "2006-06-13",
            "2006-09-20",
            "2009-01-02",
            "2009-04-10",
            "2009-04-16",
            "2009-04-17",
            "2009-07-06",
            "2010-05-20",
            "2010-05-21",
            "2010-08-13",
            "2011-05-16",
            "2011-10-27",
            "2011-10-28",
            "2011-10-29",
            "2011-10-30",
            "2011-10-31",
            "2012-04-09",
            "2013-12-30",
            "2014-08-11",
            "2015-01-02",
            "2015-05-04",
            "2016-05-06",
            "2016-07-18",
            "2016-10-14",
            "2017-10-26",
            "2019-05-06",
            "2020-11-19",
            "2020-11-20",
            "2020-12-11",
            "2021-02-12",
            "2021-04-12",
            "2021-09-24",
            "2022-07-15",
            "2022-07-29",
            "2022-10-14",
            "2022-12-30",
            "2023-05-05",
            "2023-07-31",
            "2023-12-29",
            "2024-04-12",
            "2024-12-30",
            "2025-06-02",
            "2025-08-11",
            "2026-01-02",
        )
        dt_observed = (
            "2007-12-24",
            "2020-07-27",
            "2020-09-04",
            "2020-09-07",
        )
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_new_years_day(self):
        name = "วันขึ้นปีใหม่"

        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1941, 2050)))
        self.assertHolidayName(
            name,
            (f"{year}-01-02" for year in range(1941, 1945)),
            (f"{year}-01-02" for year in range(1948, 1954)),
        )
        self.assertNoHolidayName(name, range(1914, 1941))

        self.assertNoNonObservedHoliday(
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
            "2028-01-03",
        )

    def test_national_childrens_day(self):
        name = "วันเด็กแห่งชาติ"
        dt = (
            # First Iteration
            "1955-10-03",
            # Second and Current Iteration
            "2010-01-09",
            "2011-01-08",
            "2012-01-14",
            "2013-01-12",
            "2014-01-11",
            "2015-01-10",
            "2016-01-09",
            "2017-01-14",
            "2018-01-13",
            "2019-01-12",
            "2020-01-11",
            "2021-01-09",
            "2022-01-08",
            "2023-01-14",
            "2024-01-13",
            "2025-01-11",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, range(1914, 1955), 1964)

    def test_franco_thai_war_armistice_day(self):
        name = "วันลงนามในสัญญาพักรบระหว่างประเทศไทยกับประเทศอินโดจีนฝรั่งเศส"
        self.assertHolidayName(name, (f"{year}-01-28" for year in range(1942, 1945)))
        self.assertNoHolidayName(name, range(1914, 1942), range(1945, 2050))

    def test_chakri_memorial_day(self):
        name_maha_chakri = "วันที่ระลึกมหาจักรี"
        name_chakri = "วันจักรี"
        name_rama_one = "วันพระบาทสมเด็จพระพุทธยอดฟ้าจุฬาโลกมหาราช และวันที่ระลึกมหาจักรีบรมราชวงศ์"
        years_pre = range(1914, 1926)
        years_maha_chakri = range(1926, 1938)
        years_chakri = range(1938, 1983)
        years_rama_one = range(1983, 2050)

        self.assertHolidayName(name_maha_chakri, (f"{year}-04-06" for year in years_maha_chakri))
        self.assertHolidayName(name_chakri, (f"{year}-04-06" for year in years_chakri))
        self.assertHolidayName(name_rama_one, (f"{year}-04-06" for year in years_rama_one))
        self.assertNoHolidayName(name_maha_chakri, years_pre, years_chakri, years_rama_one)
        self.assertNoHolidayName(name_chakri, years_pre, years_maha_chakri, years_rama_one)
        self.assertNoHolidayName(name_rama_one, years_pre, years_maha_chakri, years_chakri)

        self.assertNoNonObservedHoliday(
            "2013-04-08",
            "2014-04-07",
            "2019-04-08",
            "2024-04-08",
            "2025-04-07",
            "2030-04-08",
        )

    def test_songkran_festival(self):
        name_1914 = "พระราชพิธีตะรุษะสงกรานต์ แลนักขัตฤกษ์"
        name_1926 = "ตะรุษะสงกรานต์"
        name_1938 = "วันตรุษสงกรานต์"
        name_1939 = "วันตรุษสงกรานต์และขึ้นปีใหม่"
        name_1948 = "วันสงกรานต์"

        # MAR 28 - APR 15
        for year in range(1914, 1926):
            self.assertHolidayName(name_1914, (f"{year}-03-28", f"{year}-04-01", f"{year}-04-15"))
        self.assertNoHolidayName(name_1914, range(1926, 2050))
        # MAR 31 - APR 3
        for year in range(1926, 1938):
            self.assertHolidayName(name_1926, (f"{year}-03-31", f"{year}-04-01", f"{year}-04-03"))
        self.assertNoHolidayName(name_1926, range(1914, 1926), range(1938, 2050))
        # MAR 28 - APR 2
        for year in range(1938, 1940):
            self.assertHolidayName(name_1938, (f"{year}-03-31", f"{year}-04-01", f"{year}-04-02"))
        self.assertHolidayName(name_1939, "1940-03-31", "1940-04-01", "1940-04-02")
        self.assertNoHolidayName(name_1938, range(1914, 1938), range(1940, 2050))
        self.assertNoHolidayName(name_1939, range(1914, 1940), range(1941, 2050))
        # APR 13-14-15
        for year in [*range(1948, 1954), *range(1998, 2020), *range(2021, 2050)]:
            self.assertHolidayName(name_1948, (f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"))
        # APR 12-13-14
        for year in range(1989, 1998):
            self.assertHolidayName(name_1948, (f"{year}-04-12", f"{year}-04-13", f"{year}-04-14"))
        # APR 13
        self.assertHolidayName(name_1948, (f"{year}-04-13" for year in range(1957, 1989)))
        # None (2020 is special_public_holidays instead)
        self.assertNoHolidayName(name_1948, "2020-04-13", "2020-04-14", "2020-04-15")
        self.assertNoHolidayName(name_1948, range(1914, 1948), range(1954, 1957))

        self.assertNoNonObservedHoliday(
            "2012-04-16",
            "2013-04-16",
            "2014-04-16",
            "2017-04-17",
            "2018-04-16",
            "2019-04-16",
            # 2020 Songkran Festival special in lieus doesn't counts
            "2023-04-17",
            "2024-04-16",
            "2025-04-16",
            "2028-04-17",
            "2029-04-16",
            "2030-04-16",
        )

    def test_national_labour_day(self):
        name = "วันแรงงานแห่งชาติ"

        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1974, 2050)))
        self.assertNoHolidayName(name, range(1914, 1974))

        self.assertNoNonObservedHoliday(
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
            "2027-05-03",
        )

    def test_coronation_day(self):
        name_1914 = "ทำบุญพระบรมอัษฐิ และพระราชพิธีฉัตรมงคล"
        name_1926 = "พระราชพิธีฉัตรมงคล"
        name_1958 = "วันฉัตรมงคล"

        for year in range(1914, 1925):
            self.assertHolidayName(
                name_1914, (f"{year}-11-09", f"{year}-11-10", f"{year}-11-11", f"{year}-11-12")
            )
        self.assertNoHolidayName(name_1914, range(1926, 2050))
        for year in range(1926, 1936):
            self.assertHolidayName(name_1926, (f"{year}-02-24", f"{year}-02-25", f"{year}-02-26"))
        self.assertNoHolidayName(name_1926, range(1914, 1926), range(1936, 2050))
        self.assertHolidayName(name_1958, (f"{year}-05-05" for year in range(1958, 2017)))
        self.assertHolidayName(name_1958, (f"{year}-05-04" for year in range(2020, 2050)))
        self.assertNoHolidayName(name_1958, range(1914, 1958), range(2017, 2020))

        self.assertNoNonObservedHoliday(
            "2012-05-07",
            "2013-05-06",
            "2024-05-06",
            "2025-05-05",
            "2030-05-06",
        )

    def test_queen_suthida_birthday(self):
        name = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี"

        self.assertHolidayName(name, (f"{year}-06-03" for year in range(2019, 2050)))
        self.assertNoHolidayName(name, range(1914, 2019))

        self.assertNoNonObservedHoliday(
            "2023-06-05",
            "2028-06-05",
            "2029-06-04",
        )

    def test_national_day(self):
        name_1938 = "วันขอพระราชทานรัฐธรรมนูญ"
        name_1939 = "วันชาติ"

        self.assertHolidayName(name_1938, "1938-06-24")
        for year in [*range(1940, 1948), *range(1952, 1954)]:
            self.assertHolidayName(name_1939, (f"{year}-06-23", f"{year}-06-24", f"{year}-06-25"))
        self.assertHolidayName(
            name_1939,
            "1939-06-24",
            (f"{year}-06-24" for year in range(1948, 1952)),
            (f"{year}-06-24" for year in range(1954, 1960)),
        )
        self.assertHolidayName(name_1939, (f"{year}-12-05" for year in range(1960, 2050)))
        self.assertNoHolidayName(name_1938, range(1914, 1938), range(1939, 2050))
        self.assertNoHolidayName(name_1939, range(1914, 1939))

        # No in lieus during its existense on June 24th
        # 1960+ In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_provisional_constitution_day(self):
        name = "วันรัฐธรรมนูญชั่วคราว"

        self.assertHolidayName(name, (f"{year}-06-27" for year in range(1938, 1940)))
        self.assertNoHolidayName(name, range(1914, 1938), range(1940, 2050))

    def test_rama_x_birthday(self):
        name = "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดีศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว"

        self.assertHolidayName(name, (f"{year}-07-28" for year in range(2017, 2050)))
        self.assertNoHolidayName(name, range(1914, 2017))

        self.assertNoNonObservedHoliday(
            "2018-07-30",
            "2019-07-29",
            "2024-07-29",
            "2029-07-30",
            "2030-07-29",
        )

    def test_queen_sirikit_birthday(self):
        name_ix = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสิริกิติ์ พระบรมราชินีนาถ"
        name_x = "วันเฉลิมพระชนมพรรษาสมเด็จพระบรมราชชนนีพันปีหลวง"
        years_pre = range(1914, 1976)
        years_ix = range(1976, 2017)
        years_x = range(2017, 2050)

        self.assertHolidayName(name_ix, (f"{year}-08-12" for year in years_ix))
        self.assertHolidayName(name_x, (f"{year}-08-12" for year in years_x))
        self.assertNoHolidayName(name_ix, years_pre, years_x)
        self.assertNoHolidayName(name_x, years_pre, years_ix)

        self.assertNoNonObservedHoliday(
            "2012-08-13",
            "2017-08-14",
            "2018-08-13",
            "2023-08-14",
            "2028-08-14",
            "2029-08-13",
        )

    def test_national_mothers_day(self):
        name = "วันแม่แห่งชาติ"

        self.assertHolidayName(name, (f"{year}-04-15" for year in range(1950, 1958)))
        self.assertHolidayName(name, (f"{year}-08-12" for year in range(1976, 2050)))
        self.assertNoHolidayName(name, range(1914, 1950), range(1958, 1976))

        # April 15 (1950-1958) exists prior to in lieu laws
        # In lieus are same as HM Queen Sirikit's Birthday

    def test_peace_proclamation_day(self):
        name = "วันประกาศสันติภาพ"
        self.assertHolidayName(name, (f"{year}-08-16" for year in range(1946, 1948)))
        self.assertNoHolidayName(name, range(1914, 1946), range(1948, 2050))

    def test_rama_ix_memorial_day(self):
        name_ix = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_x = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        name_x_memorial = "วันนวมินทรมหาราช"
        years_pre = range(1914, 2017)
        years_ix = range(2017, 2019)
        years_x = range(2019, 2023)
        years_x_memorial = range(2023, 2050)

        self.assertHolidayName(name_ix, (f"{year}-10-13" for year in years_ix))
        self.assertHolidayName(name_x, (f"{year}-10-13" for year in years_x))
        self.assertHolidayName(name_x_memorial, (f"{year}-10-13" for year in years_x_memorial))
        self.assertNoHolidayName(name_ix, years_pre, years_x, years_x_memorial)
        self.assertNoHolidayName(name_x, years_pre, years_ix, years_x_memorial)
        self.assertNoHolidayName(name_x_memorial, years_pre, years_ix, years_x)

        self.assertNoNonObservedHoliday(
            "2018-10-15",
            "2019-10-14",
            "2024-10-14",
            "2029-10-15",
            "2030-10-14",
        )

    def test_rama_five_memorial_day(self):
        name_ashes = "ทำบุญพระบรมอัษฐิพระพุทธเจ้าหลวง"
        name_death = "วันสวรรคตแห่งพระบาทสมเด็จพระพุทธเจ้าหลวง"
        name_memorial = "วันปิยมหาราช"
        years_ashes = range(1914, 1926)
        years_death = range(1926, 1938)
        years_none = range(1938, 1946)
        years_memorial = range(1946, 2050)

        self.assertHolidayName(name_ashes, (f"{year}-10-23" for year in years_ashes))
        self.assertHolidayName(name_death, (f"{year}-10-23" for year in years_death))
        self.assertHolidayName(name_memorial, (f"{year}-10-23" for year in years_memorial))
        self.assertNoHolidayName(name_ashes, years_death, years_none, years_memorial)
        self.assertNoHolidayName(name_death, years_ashes, years_none, years_memorial)
        self.assertNoHolidayName(name_memorial, years_ashes, years_death, years_none)

        self.assertNoNonObservedHoliday(
            "2010-10-25",
            "2011-10-24",
            "2016-10-24",
            "2021-10-25",
            "2022-10-24",
            "2027-10-25",
        )

    def test_united_nations_day(self):
        name = "วันสหประชาชาติ"
        self.assertHolidayName(name, (f"{year}-10-24" for year in range(1951, 1957)))
        self.assertNoHolidayName(name, range(1914, 1951), range(1957, 2050))

    def test_rama_vi_to_ix_birthday(self):
        name_1914 = "เฉลิมพระชนมพรรษา"
        name_1926 = "เฉลิมพระชนม์พรรษา"
        name_1938 = "วันเฉลิมพระชนม์พรรษา"
        name_1941 = "วันเกิดในสมเด็จพระเจ้าอยู่หัว"
        name_1945 = "วันเฉลิมพระชนมพรรษา"
        name_1960 = "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_2016 = "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_2019 = (
            "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        )

        # Rama VI.
        for year in range(1914, 1925):
            self.assertHolidayName(name_1914, (f"{year}-12-30", f"{year}-12-31"))
        for year in range(1915, 1926):
            self.assertHolidayName(name_1914, (f"{year}-01-01", f"{year}-01-02", f"{year}-01-03"))
        # Rama VII.
        for year in range(1926, 1935):
            self.assertHolidayName(name_1926, (f"{year}-11-07", f"{year}-11-08", f"{year}-11-09"))
        # Rama VIII.
        self.assertHolidayName(name_1938, (f"{year}-09-20" for year in range(1938, 1940)))
        self.assertHolidayName(name_1938, "1940-09-20", "1940-09-21")
        for year in range(1941, 1945):
            self.assertHolidayName(name_1941, (f"{year}-09-20", f"{year}-09-21"))
        self.assertHolidayName(name_1945, "1945-09-20", "1945-09-21")
        # Rama IX.
        for year in range(1946, 1948):
            self.assertHolidayName(name_1945, (f"{year}-12-05", f"{year}-12-06"))
        for year in [*range(1948, 1951), *range(1952, 1954)]:
            self.assertHolidayName(name_1945, (f"{year}-12-04", f"{year}-12-05", f"{year}-12-06"))
        self.assertHolidayName(name_1945, "1951-12-05", "1951-12-06", "1951-12-07")
        self.assertHolidayName(name_1960, (f"{year}-12-05" for year in range(1960, 2016)))
        self.assertHolidayName(name_2016, (f"{year}-12-05" for year in range(2016, 2019)))
        self.assertHolidayName(name_2019, (f"{year}-12-05" for year in range(2019, 2050)))
        self.assertNoHolidayName(name_1914, range(1926, 2050))
        self.assertNoHolidayName(name_1926, range(1914, 1926), range(1935, 2050))
        self.assertNoHolidayName(name_1938, range(1914, 1938), range(1941, 2050))
        self.assertNoHolidayName(name_1941, range(1914, 1941), range(1945, 2050))
        self.assertNoHolidayName(name_1945, range(1914, 1945), range(1960, 2050))
        self.assertNoHolidayName(name_1960, range(1914, 1960), range(2016, 2050))
        self.assertNoHolidayName(name_2016, range(1914, 2016), range(2019, 2050))
        self.assertNoHolidayName(name_2019, range(1914, 2019))

        self.assertNoNonObservedHoliday(
            "2010-12-06",
            "2015-12-07",
            "2020-12-07",
            "2021-12-06",
            "2026-12-07",
            "2027-12-06",
        )

    def test_national_fathers_day(self):
        name = "วันพ่อแห่งชาติ"

        # This concides with HM King Bhumibol Adulyadej's Birthday
        self.assertHolidayName(name, (f"{year}-12-05" for year in range(1980, 2050)))
        self.assertNoHolidayName(name, range(1914, 1980))

        # In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_constitution_day(self):
        name = "วันรัฐธรรมนูญ"

        for year in [*range(1938, 1948), *range(1950, 1954)]:
            self.assertHolidayName(name, (f"{year}-12-09", f"{year}-12-10", f"{year}-12-11"))
        self.assertHolidayName(
            name,
            (f"{year}-12-10" for year in range(1948, 1950)),
            (f"{year}-12-10" for year in range(1954, 2050)),
        )
        self.assertNoHolidayName(name, range(1914, 1938))

        self.assertNoNonObservedHoliday(
            "2011-12-12",
            "2016-12-12",
            "2017-12-11",
            "2022-12-12",
            "2023-12-11",
            "2028-12-11",
        )

    def test_new_years_eve(self):
        name = "วันสิ้นปี"

        self.assertHolidayName(
            name,
            (f"{year}-12-31" for year in range(1941, 1957)),
            (f"{year}-12-31" for year in range(1989, 2050)),
        )
        self.assertNoHolidayName(name, range(1914, 1941), range(1957, 1989))

        self.assertNoNonObservedHoliday(
            "2012-01-03",
            "2017-01-03",
            "2018-01-02",
            "2023-01-03",
            "2029-01-02",
        )

    def test_makha_bucha(self):
        self.assertNoHolidayName("มาฆบูชา จาตุรงฅ์สันนิบาต", 1914, range(1938, 2050))
        self.assertNoHolidayName("วันมาฆบูชา", range(1914, 1938))

        self.assertNoNonObservedHoliday(
            "2010-03-01",
            "2017-02-13",
            "2020-02-10",
            "2024-02-26",
            "2024-02-22",
            "2030-02-18",
        )

    def test_visakha_bucha(self):
        self.assertNoHolidayName("วิสาขะบูชา", range(1926, 2050))
        self.assertNoHolidayName("วิศาขะบูชา", range(1914, 1926), range(1938, 2050))
        self.assertNoHolidayName("วันวิสาขะบูชา", range(1914, 1938), range(1957, 2050))
        self.assertNoHolidayName("วันวิสาขบูชา", range(1914, 1957))

        self.assertNoNonObservedHoliday(
            "2019-05-20",
            "2022-05-16",
            "2023-06-05",
            "2025-05-12",
            "2026-06-01",
            "2029-05-28",
        )

    def test_asarnha_bucha(self):
        self.assertNoHolidayName("วันอาสาฬหบูชา", range(1914, 1962))

        self.assertNoNonObservedHoliday(
            "2017-07-10",
            "2020-07-07",
            "2021-07-26",
            "2024-07-22",
            "2027-07-20",
            "2030-07-16",
        )

    def test_buddhist_lent_day(self):
        self.assertNoHolidayName("เข้าปุริมพรรษา", range(1938, 2050))
        self.assertNoHolidayName("วันเข้าพรรษา", range(1914, 1938))

        self.assertNoNonObservedHoliday(
            "2011-07-18",
            "2014-07-14",
            "2018-07-30",
        )

    def test_raeknakhwan(self):
        name = "วันพืชมงคล"

        dt = (
            "1960-05-02",
            "1961-05-11",
            "1962-05-07",
            "1963-05-10",
            "1964-05-08",
            "1965-05-13",
            "1966-05-13",
            "1967-05-11",
            "1968-05-10",
            "1969-05-09",
            "1970-05-08",
            "1971-05-07",
            "1972-05-08",
            "1973-05-07",
            "1974-05-08",
            "1975-05-07",
            "1976-05-10",
            "1977-05-12",
            "1978-05-11",
            "1979-05-07",
            "1980-05-14",
            "1981-05-07",
            "1982-05-19",
            "1983-05-11",
            "1984-05-10",
            "1985-05-09",
            "1986-05-09",
            "1987-05-08",
            "1988-05-11",
            "1989-05-11",
            "1990-05-11",
            "1991-05-10",
            "1992-05-14",
            "1993-05-17",
            "1994-05-11",
            "1995-05-10",
            "1996-05-16",
            "1997-05-09",
            "1998-05-08",
            # Not a holiday in 1999 date, was held on MAY, 14.
            "2000-05-15",
            "2001-05-16",
            "2002-05-09",
            "2003-05-08",
            "2004-05-07",
            "2005-05-11",
            "2006-05-11",
            "2007-05-10",
            "2008-05-09",
            "2009-05-11",
            "2010-05-13",
            "2011-05-13",
            "2012-05-09",
            "2013-05-13",
            "2014-05-09",
            "2015-05-13",
            "2016-05-09",
            "2017-05-12",
            "2018-05-14",
            "2019-05-09",
            "2020-05-11",
            "2021-05-10",
            "2022-05-13",
            "2023-05-17",
            "2024-05-10",
            "2025-05-09",
        )
        gov_holidays = Thailand(categories=GOVERNMENT, years=range(1959, 2026))
        self.assertHolidayName(name, gov_holidays, dt)
        self.assertNoHolidayName(name, gov_holidays, 1959, 1999)
        self.assertNoHolidayName(name)

    def test_armed_forces_holiday(self):
        name = "วันกองทัพไทย"

        armed_forces_holidays = Thailand(categories=ARMED_FORCES, years=range(1958, 2050))
        self.assertHolidayName(
            name, armed_forces_holidays, (f"{year}-04-08" for year in range(1959, 1980))
        )
        self.assertHolidayName(
            name, armed_forces_holidays, (f"{year}-01-25" for year in range(1980, 2007))
        )
        self.assertHolidayName(
            name, armed_forces_holidays, (f"{year}-01-18" for year in range(2007, 2050))
        )
        self.assertNoHolidayName(name, armed_forces_holidays, 1958)
        self.assertNoHolidayName(name)

    def test_bank_holiday(self):
        name_agri = "วันหยุดเพิ่มเติมสำหรับการปิดบัญชีประจำปีของธนาคารเพื่อการเกษตรและสหกรณ์การเกษตร"
        name_mid = "วันหยุดภาคครึ่งปีของสถาบันการเงินและสถาบันการเงินเฉพาะกิจ"

        bank_holidays = Thailand(categories=BANK, years=range(1942, 2023))
        self.assertHolidayName(
            name_agri, bank_holidays, (f"{year}-04-01" for year in range(1943, 2022))
        )
        self.assertHolidayName(
            name_mid, bank_holidays, (f"{year}-07-01" for year in range(1943, 2019))
        )
        self.assertNoHolidayName(name_agri, bank_holidays, 1942, range(2022, 2050))
        self.assertNoHolidayName(name_mid, bank_holidays, 1942, range(2019, 2050))
        self.assertNoHolidayName(name_agri)
        self.assertNoHolidayName(name_mid)

    def test_school_holiday(self):
        name = "วันครู"

        school_holidays = Thailand(categories=SCHOOL, years=range(1956, 2050))
        self.assertHolidayName(
            name, school_holidays, (f"{year}-01-16" for year in range(1957, 2050))
        )
        self.assertNoHolidayName(name, school_holidays, 1956)
        self.assertNoHolidayName(name)

    def test_workday_1947(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1947),
            ("1947-11-27", "วันลอยกระทง"),
        )

    def test_workday_1948(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1948),
            ("1948-02-03", "วันทหารผ่านศึก"),
            ("1948-11-15", "วันลอยกระทง"),
        )

    def test_workday_1982(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1982),
            ("1982-02-03", "วันทหารผ่านศึก"),
            ("1982-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("1982-10-31", "วันลอยกระทง"),
        )

    def test_workday_1985(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1985),
            ("1985-02-03", "วันทหารผ่านศึก"),
            ("1985-02-26", "วันศิลปินแห่งชาติ"),
            ("1985-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("1985-11-26", "วันลอยกระทง"),
        )

    def test_workday_1989(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1989),
            ("1989-02-03", "วันทหารผ่านศึก"),
            ("1989-02-26", "วันศิลปินแห่งชาติ"),
            ("1989-03-08", "วันสตรีสากล"),
            ("1989-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("1989-11-12", "วันลอยกระทง"),
        )

    def test_workday_1990(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1990),
            ("1990-01-14", "วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ"),
            ("1990-01-17", "วันพ่อขุนรามคำแหงมหาราช"),
            ("1990-02-03", "วันทหารผ่านศึก"),
            ("1990-02-26", "วันศิลปินแห่งชาติ"),
            ("1990-03-08", "วันสตรีสากล"),
            ("1990-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("1990-11-02", "วันลอยกระทง"),
        )

    def test_workday_1995(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1995),
            ("1995-01-13", "วันการบินแห่งชาติ"),
            ("1995-01-14", "วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ"),
            ("1995-01-17", "วันพ่อขุนรามคำแหงมหาราช"),
            ("1995-02-03", "วันทหารผ่านศึก"),
            ("1995-02-26", "วันศิลปินแห่งชาติ"),
            ("1995-03-08", "วันสตรีสากล"),
            ("1995-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("1995-11-06", "วันลอยกระทง"),
        )

    def test_workday_1999(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=1999),
            ("1999-01-13", "วันการบินแห่งชาติ"),
            ("1999-01-14", "วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ"),
            ("1999-01-17", "วันพ่อขุนรามคำแหงมหาราช"),
            ("1999-02-03", "วันทหารผ่านศึก"),
            ("1999-02-26", "วันศิลปินแห่งชาติ"),
            ("1999-03-08", "วันสตรีสากล"),
            ("1999-05-14", "วันพืชมงคล"),
            ("1999-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("1999-11-22", "วันลอยกระทง"),
        )

    def test_workday_2017(self):
        self.assertHolidays(
            Thailand(categories=WORKDAY, years=2017),
            ("2017-01-13", "วันการบินแห่งชาติ"),
            ("2017-01-14", "วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ"),
            ("2017-01-17", "วันพ่อขุนรามคำแหงมหาราช"),
            ("2017-02-03", "วันทหารผ่านศึก"),
            ("2017-02-26", "วันศิลปินแห่งชาติ"),
            ("2017-03-08", "วันสตรีสากล"),
            ("2017-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("2017-09-28", "วันพระราชทานธงชาติไทย"),
            ("2017-11-03", "วันลอยกระทง"),
        )

    def test_weekends(self):
        for dt in (
            "1940-01-07",  # SUN.
            "1940-01-14",  # SUN.
            "1940-01-21",  # SUN.
            "1940-01-28",  # SUN.
            "1956-09-02",  # SUN.
            "1956-09-09",  # SUN.
            "1956-09-16",  # SUN.
            "1956-09-23",  # SUN.
            "1956-09-30",  # SUN.
            "1956-10-04",  # THU (Buddhist Sabbath Day).
            "1956-10-07",  # SUN.
            "1956-10-12",  # FRI (Buddhist Sabbath Day).
            "1956-10-14",  # SUN.
            "1956-10-19",  # FRI (Buddhist Sabbath Day).
            "1956-10-21",  # SUN.
            "1956-10-27",  # SAT (Buddhist Sabbath Day).
            "1956-10-28",  # SUN.
            "1957-01-06",  # SUN.
            "1957-01-08",  # TUE (Buddhist Sabbath Day).
            "1957-01-13",  # SUN.
            "1957-01-15",  # TUE (Buddhist Sabbath Day).
            "1957-01-20",  # SUN.
            "1957-01-23",  # WED (Buddhist Sabbath Day).
            "1957-01-27",  # SUN.
            "1957-01-30",  # WED (Buddhist Sabbath Day).
            "1957-09-01",  # SUN.
            "1957-09-02",  # MON (Buddhist Sabbath Day).
            "1957-09-08",  # SUN.
            "1957-09-09",  # MON (Buddhist Sabbath Day).
            "1957-09-15",  # SUN.
            "1957-09-17",  # TUE (Buddhist Sabbath Day).
            "1957-09-22",  # SUN.
            "1957-09-24",  # TUE (Buddhist Sabbath Day).
            "1957-09-29",  # SUN.
            "1957-10-02",  # WED (Buddhist Sabbath Day).
            "1957-10-06",  # SUN.
            "1957-10-13",  # SUN.
            "1957-10-20",  # SUN.
            "1957-10-27",  # SUN.
            "1958-01-05",  # SUN.
            "1958-01-12",  # SUN.
            "1958-01-19",  # SUN.
            "1958-01-26",  # SUN.
            "1960-01-02",  # SAT.
            "1960-01-03",  # SUN.
            "1960-01-09",  # SAT.
            "1960-01-10",  # SUN.
            "1960-01-16",  # SAT.
            "1960-01-17",  # SUN.
            "1960-01-23",  # SAT.
            "1960-01-24",  # SUN.
            "1960-01-30",  # SAT.
            "1960-01-31",  # SUN.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "1938-01-01",  # SAT.
            "1938-01-02",  # SUN.
            "1938-01-08",  # SAT.
            "1938-01-09",  # SUN.
            "1938-01-15",  # SAT.
            "1938-01-16",  # SUN.
            "1938-01-22",  # SAT.
            "1938-01-23",  # SUN.
            "1938-01-29",  # SAT.
            "1938-01-30",  # SUN.
            "1940-01-06",  # SAT (Half Day).
            "1940-01-13",  # SAT (Half Day).
            "1940-01-20",  # SAT (Half Day).
            "1940-01-27",  # SAT (Half Day).
            "1956-09-01",  # SAT (Half Day).
            "1956-09-08",  # SAT (Half Day).
            "1956-09-15",  # SAT (Half Day).
            "1956-09-22",  # SAT (Half Day).
            "1956-09-29",  # SAT (Half Day).
            "1956-10-06",  # SAT.
            "1956-10-13",  # SAT.
            "1956-10-20",  # SAT.
            "1957-01-05",  # SAT.
            "1957-01-12",  # SAT.
            "1957-01-19",  # SAT.
            "1957-01-26",  # SAT.
            "1957-09-07",  # SAT.
            "1957-09-14",  # SAT.
            "1957-09-21",  # SAT.
            "1957-09-28",  # SAT.
            "1957-10-05",  # SAT.
            "1957-10-12",  # SAT (Half Day).
            "1957-10-19",  # SAT (Half Day).
            "1957-10-26",  # SAT (Half Day).
            "1958-01-04",  # SAT (Half Day).
            "1958-01-11",  # SAT (Half Day).
            "1958-01-18",  # SAT (Half Day).
            "1958-01-25",  # SAT (Half Day).
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-03", "ชดเชยวันขึ้นปีใหม่"),
            ("2022-01-08", "วันเด็กแห่งชาติ"),
            ("2022-01-13", "วันการบินแห่งชาติ"),
            ("2022-01-14", "วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ"),
            ("2022-01-16", "วันครู"),
            ("2022-01-17", "วันพ่อขุนรามคำแหงมหาราช"),
            ("2022-01-18", "วันกองทัพไทย"),
            ("2022-02-03", "วันทหารผ่านศึก"),
            ("2022-02-16", "วันมาฆบูชา"),
            ("2022-02-26", "วันศิลปินแห่งชาติ"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-04-06", "วันพระบาทสมเด็จพระพุทธยอดฟ้าจุฬาโลกมหาราช และวันที่ระลึกมหาจักรีบรมราชวงศ์"),
            ("2022-04-13", "วันสงกรานต์"),
            ("2022-04-14", "วันสงกรานต์"),
            ("2022-04-15", "วันสงกรานต์"),
            ("2022-05-01", "วันแรงงานแห่งชาติ"),
            ("2022-05-02", "ชดเชยวันแรงงานแห่งชาติ"),
            ("2022-05-04", "วันฉัตรมงคล"),
            ("2022-05-13", "วันพืชมงคล"),
            ("2022-05-15", "วันวิสาขบูชา"),
            ("2022-05-16", "ชดเชยวันวิสาขบูชา"),
            (
                "2022-06-03",
                "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี",
            ),
            ("2022-07-13", "วันอาสาฬหบูชา"),
            ("2022-07-14", "วันเข้าพรรษา"),
            ("2022-07-15", "วันหยุดพิเศษ (เพิ่มเติม)"),
            (
                "2022-07-28",
                (
                    "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดี"
                    "ศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว"
                ),
            ),
            ("2022-07-29", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2022-08-12", "วันเฉลิมพระชนมพรรษาสมเด็จพระบรมราชชนนีพันปีหลวง; วันแม่แห่งชาติ"),
            ("2022-08-18", "วันวิทยาศาสตร์แห่งชาติ"),
            ("2022-09-28", "วันพระราชทานธงชาติไทย"),
            (
                "2022-10-13",
                "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร",
            ),
            ("2022-10-14", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2022-10-23", "วันปิยมหาราช"),
            ("2022-10-24", "ชดเชยวันปิยมหาราช"),
            ("2022-11-08", "วันลอยกระทง"),
            (
                "2022-12-05",
                (
                    "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรม"
                    "ชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร; วันชาติ; วันพ่อแห่งชาติ"
                ),
            ),
            ("2022-12-10", "วันรัฐธรรมนูญ"),
            ("2022-12-12", "ชดเชยวันรัฐธรรมนูญ"),
            ("2022-12-30", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2022-12-31", "วันสิ้นปี"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-01-08", "National Children's Day"),
            ("2022-01-13", "National Aviation Day"),
            ("2022-01-14", "National Forest Conservation Day"),
            ("2022-01-16", "Teacher's Day"),
            ("2022-01-17", "HM King Ramkhamhaeng Memorial Day"),
            ("2022-01-18", "Royal Thai Armed Forces Day"),
            ("2022-02-03", "Thai Veterans Day"),
            ("2022-02-16", "Makha Bucha"),
            ("2022-02-26", "National Artist Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-06", "Chakri Memorial Day"),
            ("2022-04-13", "Songkran Festival"),
            ("2022-04-14", "Songkran Festival"),
            ("2022-04-15", "Songkran Festival"),
            ("2022-05-01", "National Labor Day"),
            ("2022-05-02", "National Labor Day (in lieu)"),
            ("2022-05-04", "Coronation Day"),
            ("2022-05-13", "Royal Ploughing Ceremony"),
            ("2022-05-15", "Visakha Bucha"),
            ("2022-05-16", "Visakha Bucha (in lieu)"),
            ("2022-06-03", "HM Queen Suthida's Birthday"),
            ("2022-07-13", "Asarnha Bucha"),
            ("2022-07-14", "Buddhist Lent Day"),
            ("2022-07-15", "Bridge Public Holiday"),
            ("2022-07-28", "HM King Maha Vajiralongkorn's Birthday"),
            ("2022-07-29", "Bridge Public Holiday"),
            (
                "2022-08-12",
                "HM Queen Sirikit The Queen Mother's Birthday; National Mother's Day",
            ),
            ("2022-08-18", "National Science Day"),
            ("2022-09-28", "Thai National Flag Day"),
            ("2022-10-13", "HM King Bhumibol Adulyadej the Great Memorial Day"),
            ("2022-10-14", "Bridge Public Holiday"),
            ("2022-10-23", "HM King Chulalongkorn Memorial Day"),
            ("2022-10-24", "HM King Chulalongkorn Memorial Day (in lieu)"),
            ("2022-11-08", "Loy Krathong"),
            (
                "2022-12-05",
                (
                    "HM King Bhumibol Adulyadej the Great's Birthday; "
                    "National Day; National Father's Day"
                ),
            ),
            ("2022-12-10", "Constitution Day"),
            ("2022-12-12", "Constitution Day (in lieu)"),
            ("2022-12-30", "Bridge Public Holiday"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-03", "Новий рік (вихідний)"),
            ("2022-01-08", "Національний день дітей"),
            ("2022-01-13", "Національний день авіації"),
            ("2022-01-14", "Національний день охорони лісів"),
            ("2022-01-16", "День вчителя"),
            ("2022-01-17", "День памʼяті короля Рамкхамхенга"),
            ("2022-01-18", "День Королівських збройних сил Таїланду"),
            ("2022-02-03", "День ветеранів"),
            ("2022-02-16", "Маха Буча"),
            ("2022-02-26", "Національний день художника"),
            ("2022-03-08", "Міжнародний жіночий день"),
            ("2022-04-06", "День памʼяті короля Рами I та династії Чакрі"),
            ("2022-04-13", "Тайський Новий рік"),
            ("2022-04-14", "Тайський Новий рік"),
            ("2022-04-15", "Тайський Новий рік"),
            ("2022-05-01", "Національний день праці"),
            ("2022-05-02", "Національний день праці (вихідний)"),
            ("2022-05-04", "День коронації"),
            ("2022-05-13", "Церемонія королівської оранки"),
            ("2022-05-15", "Вісака Буча"),
            ("2022-05-16", "Вісака Буча (вихідний)"),
            ("2022-06-03", "День народження Її Величності королеви Сутіди"),
            ("2022-07-13", "Асарна Буча"),
            ("2022-07-14", "Початок буддистського посту"),
            ("2022-07-15", "Проміжний вихідний"),
            ("2022-07-28", "День народження Його Величності короля Маха Вачіралонгкорна"),
            ("2022-07-29", "Проміжний вихідний"),
            (
                "2022-08-12",
                "День народження Її Величності королеви-матері Сірікіт; Національний день матері",
            ),
            ("2022-08-18", "Національний день науки"),
            ("2022-09-28", "День національного прапора Таїланду"),
            ("2022-10-13", "Річниця смерті Його Величності короля Пуміпона Адульядета Великого"),
            ("2022-10-14", "Проміжний вихідний"),
            ("2022-10-23", "День памʼяті Його Величності короля Чулалонгкорна"),
            ("2022-10-24", "День памʼяті Його Величності короля Чулалонгкорна (вихідний)"),
            ("2022-11-08", "Лой Кратонг"),
            (
                "2022-12-05",
                "Національний день; Національний день батька; "
                "Річниця дня народження Його Величності короля Пуміпона Адульядета Великого",
            ),
            ("2022-12-10", "День Конституції"),
            ("2022-12-12", "День Конституції (вихідний)"),
            ("2022-12-30", "Проміжний вихідний"),
            ("2022-12-31", "Переддень Нового року"),
        )
