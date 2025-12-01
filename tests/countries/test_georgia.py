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

from holidays.countries.georgia import Georgia
from tests.common import CommonCountryTests


class TestGeorgia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Georgia, years=range(1991, 2050))

    def test_special_holidays(self):
        self.assertHoliday(
            "2024-05-17",
            "2025-08-29",
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "ახალი წელი",
            (f"{year}-01-01" for year in range(1991, 2050)),
            (f"{year}-01-02" for year in range(1991, 2050)),
        )

    def test_christmas_day(self):
        self.assertHolidayName("ქრისტეშობა", (f"{year}-01-07" for year in range(1991, 2050)))

    def test_epiphany_day(self):
        self.assertHolidayName("ნათლისღება", (f"{year}-01-19" for year in range(1991, 2050)))

    def test_mothers_day(self):
        self.assertHolidayName("დედის დღე", (f"{year}-03-03" for year in range(1991, 2050)))

    def test_international_womens_day(self):
        self.assertHolidayName(
            "ქალთა საერთაშორისო დღე", (f"{year}-03-08" for year in range(1991, 2050))
        )

    def test_national_unity_day(self):
        self.assertHolidayName(
            "ეროვნული ერთიანობის დღე", (f"{year}-04-09" for year in range(1991, 2050))
        )

    def test_good_friday(self):
        name = "წითელი პარასკევი"
        self.assertHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1991, 2050))

    def test_holy_saturday(self):
        name = "დიდი შაბათი"
        self.assertHolidayName(
            name,
            "2020-04-18",
            "2021-05-01",
            "2022-04-23",
            "2023-04-15",
            "2024-05-04",
            "2025-04-19",
        )
        self.assertHolidayName(name, range(1991, 2050))

    def test_easter_sunday(self):
        name = "აღდგომა"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(1991, 2050))

    def test_easter_monday(self):
        name = "შავი ორშაბათი"
        self.assertHolidayName(
            name,
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1991, 2050))

    def test_day_of_victory_over_fascism(self):
        self.assertHolidayName(
            "ფაშიზმზე გამარჯვების დღე", (f"{year}-05-09" for year in range(1991, 2050))
        )

    def test_saint_andrews_day(self):
        self.assertHolidayName(
            "წმინდა ანდრია პირველწოდებულის დღე", (f"{year}-05-12" for year in range(1991, 2050))
        )

    def test_family_sanctity_day(self):
        name = "ოჯახის სიწმინდისა და მშობლების პატივისცემის დღე"
        self.assertHolidayName(name, (f"{year}-05-17" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1991, 2025))

    def test_independence_day(self):
        self.assertHolidayName(
            "დამოუკიდებლობის დღე", (f"{year}-05-26" for year in range(1991, 2050))
        )

    def test_dormition_of_the_mother_of_god(self):
        self.assertHolidayName("მარიამობა", (f"{year}-08-28" for year in range(1991, 2050)))

    def test_svetitskhovloba(self):
        self.assertHolidayName("მცხეთობის", (f"{year}-10-14" for year in range(1991, 2050)))

    def test_saint_georges_day(self):
        self.assertHolidayName("გიორგობა", (f"{year}-11-23" for year in range(1991, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "ახალი წელი"),
            ("2025-01-02", "ახალი წელი"),
            ("2025-01-07", "ქრისტეშობა"),
            ("2025-01-19", "ნათლისღება"),
            ("2025-03-03", "დედის დღე"),
            ("2025-03-08", "ქალთა საერთაშორისო დღე"),
            ("2025-04-09", "ეროვნული ერთიანობის დღე"),
            ("2025-04-18", "წითელი პარასკევი"),
            ("2025-04-19", "დიდი შაბათი"),
            ("2025-04-20", "აღდგომა"),
            ("2025-04-21", "შავი ორშაბათი"),
            ("2025-05-09", "ფაშიზმზე გამარჯვების დღე"),
            ("2025-05-12", "წმინდა ანდრია პირველწოდებულის დღე"),
            ("2025-05-17", "ოჯახის სიწმინდისა და მშობლების პატივისცემის დღე"),
            ("2025-05-26", "დამოუკიდებლობის დღე"),
            ("2025-08-28", "მარიამობა"),
            ("2025-08-29", "უქმე დღე"),
            ("2025-10-14", "მცხეთობის"),
            ("2025-11-23", "გიორგობა"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "New Year's Day"),
            ("2025-01-07", "Christmas Day"),
            ("2025-01-19", "Epiphany"),
            ("2025-03-03", "Mother's Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-04-09", "National Unity Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Holy Saturday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-09", "Day of Victory over Fascism"),
            ("2025-05-12", "Saint Andrew's Day"),
            ("2025-05-17", "Day of Family Sanctity and Respect for Parents"),
            ("2025-05-26", "Independence Day"),
            ("2025-08-28", "Dormition of the Mother of God"),
            ("2025-08-29", "Public Holiday"),
            ("2025-10-14", "Holiday of Svetitskhovloba, Robe of Jesus"),
            ("2025-11-23", "Saint George's Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-01-02", "Новий рік"),
            ("2025-01-07", "Різдво Христове"),
            ("2025-01-19", "Богоявлення"),
            ("2025-03-03", "День матері"),
            ("2025-03-08", "Міжнародний жіночий день"),
            ("2025-04-09", "День національної єдності"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-19", "Велика субота"),
            ("2025-04-20", "Великдень"),
            ("2025-04-21", "Великодній понеділок"),
            ("2025-05-09", "День перемоги над фашизмом"),
            ("2025-05-12", "День Святого Андрія Первозваного"),
            ("2025-05-17", "День святості родини та поваги до батьків"),
            ("2025-05-26", "День незалежності"),
            ("2025-08-28", "Успіння Пресвятої Богородиці"),
            ("2025-08-29", "Вихідний день"),
            ("2025-10-14", "Свято Светіцховлоба, Ризи Господньої"),
            ("2025-11-23", "День Святого Георгія"),
        )
