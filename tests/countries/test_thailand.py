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

from holidays.constants import ARMED_FORCES, BANK, GOVERNMENT, PUBLIC, SCHOOL, WORKDAY
from holidays.countries.thailand import Thailand, TH, THA
from tests.common import CommonCountryTests


class TestThailand(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        support_range = range(1941, 2050)
        super().setUpClass(Thailand, years=support_range, years_non_observed=support_range)

    def test_country_aliases(self):
        self.assertAliases(Thailand, TH, THA)

    def test_no_holidays(self):
        self.assertNoHolidays(Thailand(years=1940, categories=(PUBLIC, WORKDAY)))
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
        self.assertNoHolidayName(name, range(1941, 1955), 1964)

    def test_chakri_memorial_day(self):
        name = "วันจักรี"
        self.assertHolidayName(name, (f"{year}-04-06" for year in range(1941, 2050)))

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
        # APR 13-14-15
        for year in [*range(1948, 1954), *range(1998, 2020), *range(2021, 2050)]:
            self.assertHolidayName(name, (f"{year}-04-13", f"{year}-04-14", f"{year}-04-15"))
        # APR 12-13-14
        for year in range(1989, 1998):
            self.assertHolidayName(name, (f"{year}-04-12", f"{year}-04-13", f"{year}-04-14"))
        # APR 13
        self.assertHolidayName(name, (f"{year}-04-13" for year in range(1957, 1989)))
        # None (2020 is special_public_holidays instead)
        self.assertNoHolidayName(name, "2020-04-13", "2020-04-14", "2020-04-15")
        self.assertNoHolidayName(name, range(1941, 1948), range(1954, 1957))

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
        self.assertNoHolidayName(name, range(1941, 1974))

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
        self.assertHolidayName(name, (f"{year}-05-05" for year in range(1958, 2017)))
        self.assertHolidayName(name, (f"{year}-05-04" for year in range(2020, 2050)))
        self.assertNoHolidayName(name, range(1941, 1958), range(2017, 2020))

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
        self.assertNoHolidayName(name, range(1941, 2019))

        self.assertNoNonObservedHoliday(
            "2023-06-05",
            "2028-06-05",
            "2029-06-04",
        )

    def test_national_day(self):
        name = "วันชาติ"
        self.assertHolidayName(name, (f"{year}-06-24" for year in range(1941, 1960)))
        self.assertHolidayName(name, (f"{year}-12-05" for year in range(1960, 2050)))

        # No in lieus during its existense on June 24th
        # 1960+ In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_rama_x_birthday(self):
        name = "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดีศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว"
        self.assertHolidayName(name, (f"{year}-07-28" for year in range(2017, 2050)))
        self.assertNoHolidayName(name, range(1941, 2017))

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
        years_pre = range(1941, 1976)
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
        self.assertNoHolidayName(name, range(1941, 1950), range(1958, 1976))

        # April 15 (1950-1958) exists prior to in lieu laws
        # In lieus are same as HM Queen Sirikit's Birthday

    def test_rama_ix_memorial_day(self):
        name_ix = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
        name_x = "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
        name_x_memorial = "วันนวมินทรมหาราช"
        years_pre = range(1941, 2017)
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
        name = "วันปิยมหาราช"
        self.assertHolidayName(name, (f"{year}-10-23" for year in range(1941, 2050)))

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
        years_pre = range(1941, 1960)
        years_reign = range(1960, 2016)
        years_dead = range(2016, 2019)
        years_great = range(2019, 2050)

        self.assertHolidayName(name_reign, (f"{year}-12-05" for year in years_reign))
        self.assertHolidayName(name_dead, (f"{year}-12-05" for year in years_dead))
        self.assertHolidayName(name_great, (f"{year}-12-05" for year in years_great))
        self.assertNoHolidayName(name_reign, years_pre, years_dead, years_great)
        self.assertNoHolidayName(name_dead, years_pre, years_reign, years_great)
        self.assertNoHolidayName(name_great, years_pre, years_reign, years_dead)

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
        self.assertNoHolidayName(name, range(1941, 1980))

        # In lieus are same as HM King Bhumibol Adulyadej's Birthday

    def test_constitution_day(self):
        name = "วันรัฐธรรมนูญ"
        self.assertHolidayName(name, (f"{year}-12-10" for year in range(1941, 2050)))

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
        self.assertHolidayName(name, (f"{year}-12-31" for year in range(1941, 2050)))

        self.assertNoNonObservedHoliday(
            "2012-01-03",
            "2017-01-03",
            "2018-01-02",
            "2023-01-03",
            "2029-01-02",
        )

    def test_buddhist_holidays_in_lieu(self):
        self.assertNoNonObservedHoliday(
            # Makha Bucha
            "2010-03-01",
            "2017-02-13",
            "2020-02-10",
            "2024-02-26",
            "2024-02-22",
            "2030-02-18",
            # Visakha Bucha
            "2019-05-20",
            "2022-05-16",
            "2023-06-05",
            "2025-05-12",
            "2026-06-01",
            "2029-05-28",
            # Asarnha Bucha
            "2017-07-10",
            "2020-07-07",
            "2021-07-26",
            "2024-07-22",
            "2027-07-20",
            "2030-07-16",
            # Khao Phansa
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
