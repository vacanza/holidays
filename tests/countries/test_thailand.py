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

from holidays.constants import ARMED_FORCES, BANK, GOVERNMENT, PUBLIC, SCHOOL, WORKDAY
from holidays.countries.thailand import Thailand, TH, THA
from tests.common import CommonCountryTests


class TestThailand(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        support_range = list(range(1941, 2059)) + [2158]
        super().setUpClass(Thailand, years=support_range, years_non_observed=support_range)

    def test_country_aliases(self):
        self.assertAliases(Thailand, TH, THA)

    def test_no_holidays(self):
        self.assertNoHolidays(Thailand(years=1940))
        self.assertNoHolidays(Thailand(years=1958, categories=ARMED_FORCES))
        self.assertNoHolidays(Thailand(years=1942, categories=BANK))
        self.assertNoHolidays(Thailand(years=1956, categories=GOVERNMENT))
        self.assertNoHolidays(Thailand(years=1956, categories=SCHOOL))
        self.assertNoHolidays(Thailand(years=1940, categories=WORKDAY))

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
        )
        dt_observed = (
            "2007-12-24",
            "2020-07-27",
            "2020-09-04",
            "2020-09-07",
        )
        self.assertHoliday(dt, dt_observed)
        self.assertNoNonObservedHoliday(dt_observed)

    def test_2022_all(self):
        self.assertHolidays(
            Thailand(categories=(ARMED_FORCES, GOVERNMENT, PUBLIC, SCHOOL, WORKDAY), years=2022),
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
            ("2022-04-06", "วันจักรี"),
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
                    "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร "
                    "มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร; วันชาติ; วันพ่อแห่งชาติ"
                ),
            ),
            ("2022-12-10", "วันรัฐธรรมนูญ"),
            ("2022-12-12", "ชดเชยวันรัฐธรรมนูญ"),
            ("2022-12-30", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2022-12-31", "วันสิ้นปี"),
        )

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1941, 2058))

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
        self.assertNoHolidayName(name, 1954, 1964)

    def test_chakri_memorial_day(self):
        self.assertHoliday(f"{year}-04-06" for year in range(1941, 2058))

        self.assertNoNonObservedHoliday(
            "2013-04-08",
            "2014-04-07",
            "2019-04-08",
            "2024-04-08",
            "2025-04-07",
            "2030-04-08",
        )

    def test_songkran_festival(self):
        name = "วันสงกรานต์"

        self.assertNoHolidayName(name, 1947)
        for year in range(1948, 1954):
            self.assertHoliday(f"{year}-04-13", f"{year}-04-14", f"{year}-04-15")
        self.assertNoHolidayName(name, range(1954, 1957))
        self.assertHolidayName(name, (f"{year}-04-13" for year in range(1957, 1989)))
        for year in range(1989, 1998):
            self.assertHoliday(f"{year}-04-12", f"{year}-04-13", f"{year}-04-14")
        for year in range(1998, 2020):
            self.assertHoliday(f"{year}-04-13", f"{year}-04-14", f"{year}-04-15")
        self.assertNoHoliday("2020-04-13", "2020-04-14", "2020-04-15")
        for year in range(2021, 2058):
            self.assertHoliday(f"{year}-04-13", f"{year}-04-14", f"{year}-04-15")

        self.assertNoNonObservedHoliday(
            "2012-04-16",
            "2013-04-16",
            "2017-04-17",
            "2018-04-16",
            "2019-04-16",
            # 2020 Songkran Festival special in lieus doesn't counts
            "2023-04-17",
            "2024-04-16",
            "2028-04-17",
            "2029-04-16",
            "2030-04-16",
        )

    def test_national_labour_day(self):
        name = "วันแรงงานแห่งชาติ"

        self.assertNoHoliday("1973-05-01")
        self.assertNoHolidayName(name, 1973)
        self.assertHoliday(f"{year}-05-01" for year in range(1974, 2058))

        self.assertNoNonObservedHoliday(
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
            "2027-05-03",
        )

    def test_coronation_day(self):
        name = "วันฉัตรมงคล"

        self.assertNoHoliday("1957-05-05")
        self.assertNoHolidayName(name, 1957)
        self.assertHoliday(f"{year}-05-05" for year in range(1958, 2017))
        self.assertNoHolidayName(name, range(2017, 2020))
        self.assertHoliday(f"{year}-05-04" for year in range(2020, 2058))

        self.assertNoNonObservedHoliday(
            "2012-05-07",
            "2013-05-06",
            "2024-05-06",
            "2025-05-05",
            "2030-05-06",
        )

    def test_queen_suthida_birthday(self):
        name = "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี"

        self.assertNoHoliday("2018-06-03")
        self.assertNoHolidayName(name, 2018)
        self.assertHoliday(f"{year}-06-03" for year in range(2019, 2058))

        self.assertNoNonObservedHoliday(
            "2023-06-05",
            "2028-06-05",
            "2029-06-04",
        )

    def test_national_day(self):
        self.assertHoliday(f"{year}-06-24" for year in range(1941, 1960))
        self.assertHoliday(f"{year}-12-05" for year in range(1960, 2058))

        # No in lieus during its existense on June 24th
        # 1960+ In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_rama_x_birthday(self):
        name = "วันเฉลิมพระชนมพรรษา พระบาทสมเด็จพระเจ้าอยู่หัว"

        self.assertNoHoliday("2016-07-28")
        self.assertNoHolidayName(name, 2016)
        self.assertHoliday(f"{year}-07-28" for year in range(2017, 2058))

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

        self.assertNoHoliday("1975-08-12")
        self.assertNoHolidayName(name_ix, 1975)
        self.assertHolidayName(name_ix, (f"{year}-08-12" for year in range(1976, 2017)))
        self.assertNoHolidayName(name_x, range(1941, 2017))
        self.assertHolidayName(name_x, (f"{year}-08-12" for year in range(2017, 2058)))
        self.assertNoHolidayName(name_ix, range(2017, 2058))

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

        self.assertNoHolidayName(name, 1949)
        self.assertHolidayName(name, (f"{year}-04-15" for year in range(1950, 1958)))
        self.assertNoHolidayName(name, range(1958, 1976))
        self.assertHolidayName(name, (f"{year}-08-12" for year in range(1976, 2058)))

        # April 15 (1950-1958) exists prior to in lieu laws
        # In lieus are same as HM Queen Sirikit's Birthday

    def test_rama_ix_memorial_day(self):
        name_ix = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_x = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        name_x_memorial = "วันนวมินทรมหาราช"

        self.assertNoHoliday("2016-10-13")
        self.assertNoHolidayName(name_ix, 2016)
        self.assertNoHolidayName(name_x, range(1941, 2019))
        self.assertNoHolidayName(name_x_memorial, range(1941, 2023))
        self.assertHolidayName(name_ix, (f"{year}-10-13" for year in range(2017, 2019)))
        self.assertHolidayName(name_x, (f"{year}-10-13" for year in range(2019, 2023)))
        self.assertHolidayName(name_x_memorial, (f"{year}-10-13" for year in range(2023, 2058)))
        self.assertNoHolidayName(name_ix, range(2019, 2058))
        self.assertNoHolidayName(name_x, range(2023, 2058))

        self.assertNoNonObservedHoliday(
            "2018-10-15",
            "2019-10-14",
            "2024-10-14",
            "2029-10-15",
            "2030-10-14",
        )

    def test_rama_five_memorial_day(self):
        name = "วันปิยมหาราช"
        self.assertHoliday(f"{year}-10-23" for year in range(1941, 2058))
        self.assertNoHoliday("1910-10-23", "1940-10-23")
        self.assertNoHolidayName(name, Thailand(years=[1910, 1940]))

        self.assertNoNonObservedHoliday(
            "2010-10-25",
            "2011-10-24",
            "2016-10-24",
            "2021-10-25",
            "2022-10-24",
            "2027-10-25",
        )

    def test_rama_ix_birthday(self):
        name_reign = "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_dead = "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_great = (
            "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        )

        self.assertNoHoliday("1959-12-05")
        self.assertNoHolidayName(name_reign, range(1941, 1960))
        self.assertNoHolidayName(name_dead, range(1941, 2016))
        self.assertNoHolidayName(name_great, range(1941, 2019))
        self.assertHolidayName(name_reign, (f"{year}-12-05" for year in range(1976, 2016)))
        self.assertHolidayName(name_dead, (f"{year}-12-05" for year in range(2016, 2019)))
        self.assertHolidayName(name_great, (f"{year}-12-05" for year in range(2019, 2058)))
        self.assertNoHolidayName(name_reign, range(2016, 2058))
        self.assertNoHolidayName(name_dead, range(2019, 2058))

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
        self.assertNoHolidayName(name, 1979)
        self.assertHolidayName(name, (f"{year}-12-05" for year in range(1980, 2058)))

        # In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-12-10" for year in range(1941, 2058))

        self.assertNoNonObservedHoliday(
            "2011-12-12",
            "2016-12-12",
            "2017-12-11",
            "2022-12-12",
            "2023-12-11",
            "2028-12-11",
        )

    def test_new_years_eve(self):
        self.assertHoliday(f"{year}-12-31" for year in range(1941, 2058))

        self.assertNoNonObservedHoliday(
            "2012-01-03",
            "2017-01-03",
            "2018-01-02",
            "2023-01-03",
            "2029-01-02",
        )

    def test_makha_bucha(self):
        name = "วันมาฆบูชา"

        dt = (
            "2010-02-28",
            "2011-02-18",
            "2012-03-07",
            "2013-02-25",
            "2014-02-14",
            "2015-03-04",
            "2016-02-22",
            "2017-02-11",
            "2018-03-01",
            "2019-02-19",
            "2020-02-08",
            "2021-02-26",
            "2022-02-16",
            "2023-03-06",
            "2024-02-24",
            "2025-02-12",
            "2026-03-03",
            "2027-02-21",
            "2028-02-10",
            "2029-02-27",
            "2030-02-17",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, 2158)

        self.assertNoNonObservedHoliday(
            "2010-03-01",
            "2017-02-13",
            "2020-02-10",
            "2024-02-26",
            "2024-02-22",
            "2030-02-18",
        )

    def test_visakha_bucha(self):
        name = "วันวิสาขบูชา"

        dt = (
            "2010-05-28",
            "2011-05-17",
            "2012-06-04",
            "2013-05-24",
            "2014-05-13",
            "2015-06-01",
            "2016-05-20",
            "2017-05-10",
            "2018-05-29",
            "2019-05-18",
            "2020-05-06",
            "2021-05-26",
            "2022-05-15",
            "2023-06-03",
            "2024-05-22",
            "2025-05-11",
            "2026-05-31",
            "2027-05-20",
            "2028-05-08",
            "2029-05-27",
            "2030-05-16",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, 2158)

        self.assertNoNonObservedHoliday(
            "2019-05-20",
            "2022-05-16",
            "2023-06-05",
            "2025-05-12",
            "2026-06-01",
            "2029-05-28",
        )

    def test_asarnha_bucha(self):
        name = "วันอาสาฬหบูชา"

        dt = (
            "2010-07-26",
            "2011-07-15",
            "2012-08-02",
            "2013-07-22",
            "2014-07-11",
            "2015-07-30",
            "2016-07-19",
            "2017-07-08",
            "2018-07-27",
            "2019-07-16",
            "2020-07-05",
            "2021-07-24",
            "2022-07-13",
            "2023-08-01",
            "2024-07-20",
            "2025-07-10",
            "2026-07-29",
            "2027-07-18",
            "2028-07-06",
            "2029-07-25",
            "2030-07-14",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, 2158)

        self.assertNoNonObservedHoliday(
            "2017-07-10",
            "2020-07-07",
            "2021-07-26",
            "2024-07-22",
            "2027-07-20",
            "2030-07-16",
        )

    def test_khao_phansa(self):
        name = "วันเข้าพรรษา"

        dt = (
            "2010-07-27",
            "2011-07-16",
            "2012-08-03",
            "2013-07-23",
            "2014-07-12",
            "2015-07-31",
            "2016-07-20",
            "2017-07-09",
            "2018-07-28",
            "2019-07-17",
            "2020-07-06",
            "2021-07-25",
            "2022-07-14",
            "2023-08-02",
            "2024-07-21",
            "2025-07-11",
            "2026-07-30",
            "2027-07-19",
            "2028-07-07",
            "2029-07-26",
            "2030-07-15",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, 2158)

        self.assertNoNonObservedHoliday(
            "2011-07-18",
            "2014-07-14",
            "2018-07-30",
        )

    def test_raeknakhwan(self):
        name = "วันพืชมงคล"
        self.assertHolidays(
            Thailand(categories=GOVERNMENT, years=range(1960, 2024)),
            ("1960-05-02", name),
            ("1961-05-11", name),
            ("1962-05-07", name),
            ("1963-05-10", name),
            ("1964-05-08", name),
            ("1965-05-13", name),
            ("1966-05-13", name),
            ("1967-05-11", name),
            ("1968-05-10", name),
            ("1969-05-09", name),
            ("1970-05-08", name),
            ("1971-05-07", name),
            ("1972-05-08", name),
            ("1973-05-07", name),
            ("1974-05-08", name),
            ("1975-05-07", name),
            ("1976-05-10", name),
            ("1977-05-12", name),
            ("1978-05-11", name),
            ("1979-05-07", name),
            ("1980-05-14", name),
            ("1981-05-07", name),
            ("1982-05-19", name),
            ("1983-05-11", name),
            ("1984-05-10", name),
            ("1985-05-09", name),
            ("1986-05-09", name),
            ("1987-05-08", name),
            ("1988-05-11", name),
            ("1989-05-11", name),
            ("1990-05-11", name),
            ("1991-05-10", name),
            ("1992-05-14", name),
            ("1993-05-17", name),
            ("1994-05-11", name),
            ("1995-05-10", name),
            ("1996-05-16", name),
            ("1997-05-09", name),
            ("1998-05-08", name),
            # Not a holiday in 1999 date, was held on MAY, 14.
            ("2000-05-15", name),
            ("2001-05-16", name),
            ("2002-05-09", name),
            ("2003-05-08", name),
            ("2004-05-07", name),
            ("2005-05-11", name),
            ("2006-05-11", name),
            ("2007-05-10", name),
            ("2008-05-09", name),
            ("2009-05-11", name),
            ("2010-05-13", name),
            ("2011-05-13", name),
            ("2012-05-09", name),
            ("2013-05-13", name),
            ("2014-05-09", name),
            ("2015-05-13", name),
            ("2016-05-09", name),
            ("2017-05-12", name),
            ("2018-05-14", name),
            ("2019-05-09", name),
            ("2020-05-11", name),
            ("2021-05-10", name),
            ("2022-05-13", name),
            ("2023-05-17", name),
            ("2024-05-10", name),
        )

    def test_armed_forces_holiday(self):
        name = "วันกองทัพไทย"
        self.assertHolidays(
            Thailand(categories=ARMED_FORCES, years=range(1958, 1960)), ("1959-04-08", name)
        )
        self.assertHolidays(
            Thailand(categories=ARMED_FORCES, years=range(1979, 1981)),
            ("1979-04-08", name),
            ("1980-01-25", name),
        )
        self.assertHolidays(
            Thailand(categories=ARMED_FORCES, years=range(2006, 2008)),
            ("2006-01-25", name),
            ("2007-01-18", name),
        )

    def test_bank_holiday(self):
        a_name = "วันหยุดเพิ่มเติมสำหรับการปิดบัญชีประจำปีของธนาคารเพื่อการเกษตรและสหกรณ์การเกษตร"
        m_name = "วันหยุดภาคครึ่งปีของสถาบันการเงินและสถาบันการเงินเฉพาะกิจ"

        # Start
        self.assertHolidays(
            Thailand(categories=BANK, years=range(1942, 1944)),
            ("1943-04-01", a_name),
            ("1943-07-01", m_name),
        )
        # End
        self.assertHolidays(
            Thailand(categories=BANK, years=range(2017, 2023)),
            ("2017-04-01", a_name),
            ("2017-07-01", m_name),
            ("2018-04-01", a_name),
            ("2018-07-01", m_name),
            ("2019-04-01", a_name),
            ("2020-04-01", a_name),
            ("2021-04-01", a_name),
        )

    def test_school_holiday(self):
        self.assertHolidays(
            Thailand(categories=SCHOOL, years=range(1956, 1958)),
            ("1957-01-16", "วันครู"),
        )

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
            ("2022-04-06", "วันจักรี"),
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
            ("2022-01-17", "HM King Ramkamhaeng Memorial Day"),
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
