#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC
from holidays.countries.united_arab_emirates import UnitedArabEmirates, AE, ARE
from tests.common import CommonCountryTests


class TestUnitedArabEmirates(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedArabEmirates, years=range(1972, 2050))
        cls.no_estimated_holidays = UnitedArabEmirates(
            years=range(1972, 2050), islamic_show_estimated=False
        )

    def test_country_aliases(self):
        self.assertAliases(UnitedArabEmirates, AE, ARE)

    def test_no_holidays(self):
        self.assertNoHolidays(
            UnitedArabEmirates(years=1971, categories=(GOVERNMENT, OPTIONAL, PUBLIC))
        )

    def test_special(self):
        self.assertHoliday(
            # 29 Ramadan Eid al-Fitr specials.
            "2020-05-22",
            "2021-05-11",
            "2022-04-30",
            "2024-04-08",
            # Other Special Public Holidays.
            "2022-05-14",
            "2022-05-15",
            "2022-05-16",
        )

    def test_special_government(self):
        self.assertHoliday(
            UnitedArabEmirates(categories=GOVERNMENT),
            # Extended holidays for Public Sectors.
            "2022-05-05",
            "2022-05-06",
            "2022-05-07",
            "2022-05-08",
            "2023-12-04",
        )

    def test_special_optional(self):
        # 2019 Pope Visit.
        self.assertHoliday(UnitedArabEmirates(categories=OPTIONAL), "2019-02-05")

    def test_commemoration_day(self):
        name = "يوم الشهيد"
        self.assertHolidayName(name, (f"{year}-11-30" for year in range(2015, 2019)))
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(2019, 2024)))
        self.assertNoHolidayName(name, range(1972, 2015), range(2024, 2050))

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        name_holiday = "عطلة عيد الفطر"
        self.assertHolidayName(
            name,
            "2017-06-25",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1972, 2050))
        self.assertHolidayName(name_holiday, self.no_estimated_holidays, range(1972, 2050))
        self.assertNoHolidayName(name_holiday, "2018-06-14", "2025-03-29")

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        self.assertHolidayName(
            name,
            "2017-09-01",
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-04",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1972, 2050))
        self.assertHolidayName("عطلة عيد الأضحى", self.no_estimated_holidays, range(1972, 2050))
        self.assertHolidayName("وقفة عرفة", self.no_estimated_holidays, range(1972, 2050))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertHolidayName(
            name,
            "2017-09-22",
            "2018-09-11",
            "2019-08-31",
            "2020-08-23",
            "2021-08-12",
            "2022-07-30",
            "2023-07-21",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1972, 2050))

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertHolidayName(
            name,
            "2017-11-30",
            "2018-11-18",
            "2019-11-09",
            "2020-10-29",
            "2021-10-21",
            "2022-10-08",
            "2023-09-29",
            "2024-09-15",
            "2025-09-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1972, 2050))

    def test_isra_and_miraj(self):
        name = "ليلة المعراج"
        self.assertHolidayName(name, "2017-04-23", "2018-04-14")
        self.assertHolidayName(name, self.no_estimated_holidays, range(1972, 2019))
        self.assertNoHolidayName(name, self.no_estimated_holidays, range(2019, 2050))

    def test_2020(self):
        # https://gulfbusiness.com/revealed-uae-private-sector-holidays-for-eid-al-fitr-2020/
        # https://www.timeanddate.com/holidays/united-arab-emirates/2020?hol=134217729
        self.assertHolidays(
            UnitedArabEmirates(years=2020),
            ("2020-01-01", "رأس السنة الميلادية"),
            ("2020-05-22", "عطلة عيد الفطر"),
            ("2020-05-23", "عطلة عيد الفطر"),
            ("2020-05-24", "عيد الفطر"),
            ("2020-05-25", "عطلة عيد الفطر"),
            ("2020-05-26", "عطلة عيد الفطر"),
            ("2020-07-30", "وقفة عرفة"),
            ("2020-07-31", "عيد الأضحى"),
            ("2020-08-01", "عطلة عيد الأضحى"),
            ("2020-08-02", "عطلة عيد الأضحى"),
            ("2020-08-23", "رأس السنة الهجرية"),
            ("2020-10-29", "عيد المولد النبوي"),
            ("2020-12-01", "يوم الشهيد"),
            ("2020-12-02", "اليوم الوطني"),
            ("2020-12-03", "اليوم الوطني"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "رأس السنة الميلادية"),
            ("2018-04-14", "ليلة المعراج"),
            ("2018-06-15", "عيد الفطر"),
            ("2018-06-16", "عطلة عيد الفطر"),
            ("2018-06-17", "عطلة عيد الفطر"),
            ("2018-08-21", "وقفة عرفة"),
            ("2018-08-22", "عيد الأضحى"),
            ("2018-08-23", "عطلة عيد الأضحى"),
            ("2018-08-24", "عطلة عيد الأضحى"),
            ("2018-09-11", "رأس السنة الهجرية"),
            ("2018-11-18", "عيد المولد النبوي"),
            ("2018-11-30", "يوم الشهيد"),
            ("2018-12-02", "اليوم الوطني"),
            ("2018-12-03", "اليوم الوطني"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-04-14", "Isra' and Mi'raj"),
            ("2018-06-15", "Eid al-Fitr"),
            ("2018-06-16", "Eid al-Fitr Holiday"),
            ("2018-06-17", "Eid al-Fitr Holiday"),
            ("2018-08-21", "Arafat Day"),
            ("2018-08-22", "Eid al-Adha"),
            ("2018-08-23", "Eid al-Adha Holiday"),
            ("2018-08-24", "Eid al-Adha Holiday"),
            ("2018-09-11", "Islamic New Year"),
            ("2018-11-18", "Prophet's Birthday"),
            ("2018-11-30", "Commemoration Day"),
            ("2018-12-02", "National Day"),
            ("2018-12-03", "National Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2018-01-01", "วันขึ้นปีใหม่"),
            ("2018-04-14", "วันเมี๊ยะราจ"),
            ("2018-06-15", "วันอีฎิ้ลฟิตริ"),
            ("2018-06-16", "เทศกาลอีฎิ้ลฟิตริ"),
            ("2018-06-17", "เทศกาลอีฎิ้ลฟิตริ"),
            ("2018-08-21", "วันอารอฟะห์"),
            ("2018-08-22", "วันอีดิ้ลอัฎฮา"),
            ("2018-08-23", "เทศกาลอีดิ้ลอัฎฮา"),
            ("2018-08-24", "เทศกาลอีดิ้ลอัฎฮา"),
            ("2018-09-11", "วันขึ้นปีใหม่อิสลาม"),
            ("2018-11-18", "วันเมาลิดนบี"),
            ("2018-11-30", "วันรำลึกผู้อุทิศตน"),
            ("2018-12-02", "วันชาติสหรัฐอาหรับเอมิเรตส์"),
            ("2018-12-03", "วันชาติสหรัฐอาหรับเอมิเรตส์"),
        )
