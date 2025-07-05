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

from holidays.constants import CATHOLIC, ORTHODOX
from holidays.countries.palestine import Palestine, PS, PSE
from tests.common import CommonTests


class TestPalestine(CommonTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1989, 2050)
        super().setUpClass(Palestine, years=years)
        cls.catholic_holidays = Palestine(categories=CATHOLIC, years=years)
        cls.orthodox_holidays = Palestine(categories=ORTHODOX, years=years)
        cls.no_estimated_holidays = Palestine(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Palestine, PS, PSE)

    def test_no_holidays(self):
        self.assertNoHolidays(Palestine(categories=self.holidays.supported_categories, years=1988))

    def test_new_years_day(self):
        name = "رأس السنة الميلادي"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1989, 2050)))

    def test_orthodox_new_years_day(self):
        name = "عيد الميلاد المجيد"
        self.assertHolidayName(
            name, self.orthodox_holidays, (f"{year}-01-14" for year in range(1989, 2050))
        )

    def test_womens_day(self):
        name = "يوم المراة العالمي"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(1989, 2050)))

    def test_labor_day(self):
        name = "عيد العمال"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1989, 2050)))

    def test_independence_day(self):
        name = "عيد الإستقلال"
        self.assertHolidayName(name, (f"{year}-11-15" for year in range(1989, 2050)))

    def test_christmas_orthodox(self):
        name = "عيد الميلاد المجيد الشرقي"
        self.assertHolidayName(
            name, self.orthodox_holidays, (f"{year}-01-07" for year in range(1989, 2050))
        )
        self.assertHolidayName(
            name, self.orthodox_holidays, (f"{year}-01-08" for year in range(1989, 2050))
        )

    def test_ephiphany_orthodox(self):
        name = "عيد الغطاس"
        self.assertHolidayName(
            name, self.orthodox_holidays, (f"{year}-01-19" for year in range(1989, 2050))
        )

    def test_palm_sunday_orthodox(self):
        name = "أحد الشعانين"
        dts = (
            "2022-04-17",
            "2023-04-09",
            "2024-04-28",
            "2025-04-13",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dts)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_holy_thursday_orthodox(self):
        name = "خميس الغسل"
        dt = (
            "2022-04-21",
            "2023-04-13",
            "2024-05-02",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_good_friday_orthodox(self):
        name = "الجمعة العظيمة"
        dt = (
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_holy_saturday_orthodox(self):
        name = "سبت النور"
        dt = (
            "2022-04-23",
            "2023-04-15",
            "2024-05-04",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_easter_monday_orthodox(self):
        name = "عيد الفصح المجيد"
        dt = (
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_easter_tuesday_orthodox(self):
        name = "عيد الفصح المجيد"
        dt = (
            "2022-04-26",
            "2023-04-18",
            "2024-05-07",
            "2025-04-22",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_ascension_thursday_orthodox(self):
        name = "خميس الصعود"
        dt = (
            "2022-06-02",
            "2023-05-25",
            "2024-06-13",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_whit_sunday_orthodox(self):
        name = "أحد العنصرة"
        dt = (
            "2022-06-12",
            "2023-06-04",
            "2024-06-23",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.orthodox_holidays, dt)
        self.assertHolidayName(name, self.orthodox_holidays, range(1989, 2050))

    def test_ephiphany_catholic(self):
        name = "عيد الغطاس"
        self.assertHolidayName(
            name, self.catholic_holidays, (f"{year}-01-06" for year in range(1989, 2050))
        )

    def test_palm_sunday_catholic(self):
        name = "أحد الشعانين"
        dts = (
            "2022-04-10",
            "2023-04-02",
            "2024-03-24",
            "2025-04-13",
        )
        self.assertHolidayName(name, self.catholic_holidays, dts)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_holy_thursday_catholic(self):
        name = "خميس الغسل"
        dt = (
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_good_friday_catholic(self):
        name = "الجمعة العظيمة"
        dt = (
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_holy_saturday_catholic(self):
        name = "سبت النور"
        dt = (
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_easter_monday_catholic(self):
        name = "عيد الفصح المجيد"
        dt = (
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_easter_tuesday_catholic(self):
        name = "عيد الفصح المجيد"
        dt = (
            "2022-04-19",
            "2023-04-11",
            "2024-04-02",
            "2025-04-22",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_ascension_thursday_catholic(self):
        name = "خميس الصعود"
        dt = (
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_whit_sunday_catholic(self):
        name = "أحد العنصرة"
        dt = (
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.catholic_holidays, dt)
        self.assertHolidayName(name, self.catholic_holidays, range(1989, 2050))

    def test_christmas_catholic(self):
        name = "عيد الميلاد المجيد الغربي"
        self.assertHolidayName(
            name, self.catholic_holidays, (f"{year}-12-25" for year in range(1989, 2050))
        )
        self.assertHolidayName(
            name, self.catholic_holidays, (f"{year}-12-26" for year in range(1989, 2050))
        )

    def test_hijri_new_year(self):
        name = "رأس السنة الهجريــة"
        dts = (
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1989, 2050))

    def test_mawlid(self):
        name = "ذكرى المولد النبوي الشريـف"
        dts = (
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1989, 2050))

    def test_isra_and_miraj(self):
        name = "ذكرى الإسراء والمعــراج"
        dts = (
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1989, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر السعيد"
        dts = (
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
            "2025-03-30",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1989, 2050))

    def test_eid_al_adha(self):
        name = "عيد الأضحى المبارك"
        dts = (
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2020-08-03",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-07-23",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2023-07-01",
            "2024-06-16",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
            "2025-06-06",
            "2025-06-07",
            "2025-06-08",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, dts)
        self.assertHolidayName(name, self.no_estimated_holidays, range(1989, 2050))

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-06", "Epiphany Day"),
            ("2024-01-07", "Christmas (Orthodox)"),
            ("2024-01-08", "Christmas (Orthodox)"),
            ("2024-01-14", "New Year's Day (Orthodox)"),
            ("2024-01-19", "Epiphany Day"),
            ("2024-02-08", "Isra' and Mi'raj (estimated)"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-24", "Palm Sunday"),
            ("2024-03-28", "Holy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Holy Saturday"),
            ("2024-04-01", "Easter"),
            ("2024-04-02", "Easter"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-04-11", "Eid al-Fitr (estimated)"),
            ("2024-04-12", "Eid al-Fitr (estimated)"),
            ("2024-04-28", "Palm Sunday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-02", "Holy Thursday"),
            ("2024-05-03", "Good Friday"),
            ("2024-05-04", "Holy Saturday"),
            ("2024-05-06", "Easter"),
            ("2024-05-07", "Easter"),
            ("2024-05-09", "Ascension Day"),
            ("2024-05-19", "Whit Sunday"),
            ("2024-06-13", "Ascension Day"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha (estimated)"),
            ("2024-06-18", "Eid al-Adha (estimated)"),
            ("2024-06-19", "Eid al-Adha (estimated)"),
            ("2024-06-23", "Whit Sunday"),
            ("2024-07-07", "Hijri New Year (estimated)"),
            ("2024-09-15", "Prophet's Birthday (estimated)"),
            ("2024-11-15", "Independence Day"),
            ("2024-12-25", "Christmas (Catholic)"),
            ("2024-12-26", "Christmas (Catholic)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "رأس السنة الميلادي"),
            ("2024-01-06", "عيد الغطاس"),
            ("2024-01-07", "عيد الميلاد المجيد الشرقي"),
            ("2024-01-08", "عيد الميلاد المجيد الشرقي"),
            ("2024-01-14", "عيد الميلاد المجيد"),
            ("2024-01-19", "عيد الغطاس"),
            ("2024-02-08", "ذكرى الإسراء والمعــراج (المقدرة)"),
            ("2024-03-08", "يوم المراة العالمي"),
            ("2024-03-24", "أحد الشعانين"),
            ("2024-03-28", "خميس الغسل"),
            ("2024-03-29", "الجمعة العظيمة"),
            ("2024-03-30", "سبت النور"),
            ("2024-04-01", "عيد الفصح المجيد"),
            ("2024-04-02", "عيد الفصح المجيد"),
            ("2024-04-10", "عيد الفطر السعيد (المقدرة)"),
            ("2024-04-11", "عيد الفطر السعيد (المقدرة)"),
            ("2024-04-12", "عيد الفطر السعيد (المقدرة)"),
            ("2024-04-28", "أحد الشعانين"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-02", "خميس الغسل"),
            ("2024-05-03", "الجمعة العظيمة"),
            ("2024-05-04", "سبت النور"),
            ("2024-05-06", "عيد الفصح المجيد"),
            ("2024-05-07", "عيد الفصح المجيد"),
            ("2024-05-09", "خميس الصعود"),
            ("2024-05-19", "أحد العنصرة"),
            ("2024-06-13", "خميس الصعود"),
            ("2024-06-16", "عيد الأضحى المبارك (المقدرة)"),
            ("2024-06-17", "عيد الأضحى المبارك (المقدرة)"),
            ("2024-06-18", "عيد الأضحى المبارك (المقدرة)"),
            ("2024-06-19", "عيد الأضحى المبارك (المقدرة)"),
            ("2024-06-23", "أحد العنصرة"),
            ("2024-07-07", "رأس السنة الهجريــة (المقدرة)"),
            ("2024-09-15", "ذكرى المولد النبوي الشريـف (المقدرة)"),
            ("2024-11-15", "عيد الإستقلال"),
            ("2024-12-25", "عيد الميلاد المجيد الغربي"),
            ("2024-12-26", "عيد الميلاد المجيد الغربي"),
        )
