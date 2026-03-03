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

from holidays.constants import BANK, GOVERNMENT
from holidays.countries.lebanon import Lebanon
from tests.common import CommonCountryTests


class TestLebanon(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Lebanon)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(
            Lebanon(categories=(BANK, GOVERNMENT), years=range(self.start_year, 2019))
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in self.full_range)
        )

    def test_armenian_orthodox_christmas(self):
        name = "عيد الميلاد عند الطوائف الارمنية الارثوذكسية"
        self.assertHolidayName(name, (f"{year}-01-06" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))

    def test_saint_maron_day(self):
        self.assertHolidayName("عيد مار مارون", (f"{year}-02-09" for year in self.full_range))

    def test_rafiki_memorial_day(self):
        name = "يوم ذكرى رفيق الحريري"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-02-14" for year in range(2020, self.end_year)))
        self.assertGovernmentHolidayName(
            name, (f"{year}-02-14" for year in range(2020, self.end_year))
        )
        self.assertNoBankHolidayName(name, range(self.start_year, 2020))
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 2020))

    def test_feast_of_the_annunciation(self):
        name = "عيد بشارة السيدة مريم العذراء"
        self.assertHolidayName(
            name, (f"{year}-03-25" for year in (*range(1995, 2006), *range(2010, self.end_year)))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1995), range(2006, 2010))

    def test_catholic_good_friday(self):
        name = "الجمعة العظيمة عند الطوائف الكاثوليكية"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_good_friday(self):
        name = "الجمعة العظيمة عند الطوائف الأرثوذكسية"
        self.assertHolidayName(
            name,
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_holy_saturday(self):
        name = "سبت النور للطائفة الأرثوذكسية"
        self.assertHolidayName(
            name,
            "2010-04-03",
            "2011-04-23",
            "2014-04-19",
            "2017-04-15",
        )
        self.assertNoHolidayName(name, set(range(2010, 2025)) - {2010, 2011, 2014, 2017})

    def test_catholic_easter_monday(self):
        name = "اثنين الفصح عند الطوائف الكاثوليكية"
        self.assertHolidayName(
            name,
            "1986-03-31",
            "1987-04-20",
            "1988-04-04",
            "1989-03-27",
            "1990-04-16",
        )
        self.assertHolidayName(name, range(1986, 1995))
        self.assertBankHolidayName(name, range(2020, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1986), range(1995, self.end_year))
        self.assertNoBankHolidayName(name, range(self.start_year, 2020))

    def test_orthodox_easter_monday(self):
        name = "اثنين الفصح عند الطوائف الأرثوذكسية"
        self.assertHolidayName(
            name,
            "1986-05-05",
            "1987-04-20",
            "1988-04-11",
            "1989-05-01",
            "1990-04-16",
        )
        self.assertHolidayName(name, range(1986, 1995))
        self.assertBankHolidayName(name, range(2020, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1986), range(1995, self.end_year))
        self.assertNoBankHolidayName(name, range(self.start_year, 2020))

    def test_orthodox_easter_tuesday(self):
        name = "ثلاثاء الفصح للطوائف الأرثوذكسية"
        self.assertHolidayName(
            name,
            "1987-04-21",
            "1990-04-17",
        )
        self.assertNoHolidayName(name, set(self.full_range) - {1987, 1990})

    def test_labor_day(self):
        name = "عيد العمل"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (يُحتفل به)", obs_dts)

    def test_martyrs_day(self):
        name = "عيد الشهداء"
        self.assertHolidayName(
            name,
            "1978-05-07",
            "1979-05-06",
            "1992-05-10",
            "1993-05-09",
            "2006-05-07",
            "2007-05-06",
            "2008-05-04",
            "2009-05-03",
        )
        self.assertHolidayName(name, (*range(self.start_year, 1994), *range(2006, self.end_year)))
        self.assertNoHolidayName(name, range(1994, 2006))

    def test_resistance_and_liberation_day(self):
        name = "عيد المقاومة والتحرير"
        self.assertHolidayName(
            name,
            "2021-05-09",
            "2022-05-08",
            "2023-05-14",
            "2024-05-12",
            "2025-05-11",
        )
        self.assertHolidayName(name, range(2006, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2006))

    def test_anniversary_of_the_tragedy_of_beirut_port_explosion(self):
        name = "ذكرى مأساة انفجار مرفأ بيروت"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(
            name, (f"{year}-08-04" for year in range(2021, self.end_year))
        )
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 2021))
        self.assertNoBankHolidayName(name)

    def test_assumption_day(self):
        self.assertHolidayName("عيد انتقال العذراء", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_days(self):
        name = "عيد جميع القديسين"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1985, 1994)))
        self.assertNoHolidayName(name, range(self.start_year, 1985), range(1994, self.end_year))

    def test_independence_day(self):
        self.assertHolidayName("ذكرى الاستقلال", (f"{year}-11-22" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("عيد الميلاد", (f"{year}-12-25" for year in self.full_range))

    def test_islamic_new_year(self):
        name = "عيد رأس السنة الهجرية"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_ashura(self):
        name = "عاشوراء"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-30",
            "2021-08-19",
            "2022-08-09",
            "2023-07-28",
            "2024-07-16",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_mawlid(self):
        name = "ذكرى المولد النبوي الشريف"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "1985-06-20",
            "1986-06-10",
            "1986-06-11",
            "1994-03-14",
            "1994-03-15",
            "1994-03-16",
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-02",
            "2022-05-03",
            "2023-04-21",
            "2023-04-22",
            "2024-04-10",
            "2024-04-11",
            "2025-03-30",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayNameCount(name, 1, range(self.start_year, 1986))
        self.assertIslamicNoEstimatedHolidayNameCount(name, 3, range(1986, 1995))
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 2, set(range(1995, self.end_year)) - {2000, 2033}
        )

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "1985-08-27",
            "1985-08-28",
            "1986-08-16",
            "1986-08-17",
            "1986-08-18",
            "1994-05-21",
            "1994-05-22",
            "2020-07-31",
            "2020-08-01",
            "2021-07-20",
            "2021-07-21",
            "2022-07-09",
            "2022-07-10",
            "2023-06-28",
            "2023-06-29",
            "2024-06-16",
            "2024-06-17",
            "2025-06-06",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        self.assertIslamicNoEstimatedHolidayNameCount(
            name,
            2,
            range(self.start_year, 1986),
            set(range(1994, self.end_year)) - {2006, 2007, 2039},
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 3, range(1986, 1994))

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-01-06", "عيد الميلاد عند الطوائف الارمنية الارثوذكسية"),
            ("2024-02-09", "عيد مار مارون"),
            ("2024-03-25", "عيد بشارة السيدة مريم العذراء"),
            ("2024-03-29", "الجمعة العظيمة عند الطوائف الكاثوليكية"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عيد الفطر"),
            ("2024-05-01", "عيد العمل"),
            ("2024-05-03", "الجمعة العظيمة عند الطوائف الأرثوذكسية"),
            ("2024-05-05", "عيد الشهداء"),
            ("2024-05-12", "عيد المقاومة والتحرير"),
            ("2024-06-16", "عيد الأضحى"),
            ("2024-06-17", "عيد الأضحى"),
            ("2024-07-07", "عيد رأس السنة الهجرية"),
            ("2024-07-16", "عاشوراء"),
            ("2024-08-15", "عيد انتقال العذراء"),
            ("2024-09-15", "ذكرى المولد النبوي الشريف"),
            ("2024-11-22", "ذكرى الاستقلال"),
            ("2024-12-25", "عيد الميلاد"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "رأس السنة الميلادية"),
            ("2025-01-06", "عيد الميلاد عند الطوائف الارمنية الارثوذكسية"),
            ("2025-02-09", "عيد مار مارون"),
            ("2025-02-14", "يوم ذكرى رفيق الحريري"),
            ("2025-03-25", "عيد بشارة السيدة مريم العذراء"),
            ("2025-03-30", "عيد الفطر"),
            ("2025-03-31", "عيد الفطر"),
            (
                "2025-04-18",
                "الجمعة العظيمة عند الطوائف الأرثوذكسية; الجمعة العظيمة عند الطوائف الكاثوليكية",
            ),
            ("2025-04-19", "سبت النور للطائفة الأرثوذكسية"),
            (
                "2025-04-21",
                "اثنين الفصح عند الطوائف الأرثوذكسية; اثنين الفصح عند الطوائف الكاثوليكية",
            ),
            ("2025-05-01", "عيد العمل"),
            ("2025-05-04", "عيد الشهداء"),
            ("2025-05-11", "عيد المقاومة والتحرير"),
            ("2025-06-06", "عيد الأضحى"),
            ("2025-06-07", "عيد الأضحى"),
            ("2025-06-26", "عيد رأس السنة الهجرية"),
            ("2025-07-05", "عاشوراء (المقدرة)"),
            ("2025-08-04", "ذكرى مأساة انفجار مرفأ بيروت"),
            ("2025-08-15", "عيد انتقال العذراء"),
            ("2025-09-04", "ذكرى المولد النبوي الشريف (المقدرة)"),
            ("2025-11-22", "ذكرى الاستقلال"),
            ("2025-12-25", "عيد الميلاد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-06", "Armenian Orthodox Christmas Day"),
            ("2025-02-09", "Saint Maron's Day"),
            ("2025-02-14", "Rafik Hariri Memorial Day"),
            ("2025-03-25", "Feast of the Annunciation"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-18", "Catholic Good Friday; Orthodox Good Friday"),
            ("2025-04-19", "Orthodox Holy Saturday"),
            ("2025-04-21", "Catholic Easter Monday; Orthodox Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-04", "Martyrs' Day"),
            ("2025-05-11", "Resistance and Liberation Day"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-26", "Islamic New Year"),
            ("2025-07-05", "Ashura (estimated)"),
            ("2025-08-04", "Anniversary of the tragedy of Beirut port explosion"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-04", "Prophet's Birthday (estimated)"),
            ("2025-11-22", "Independence Day"),
            ("2025-12-25", "Christmas Day"),
        )
