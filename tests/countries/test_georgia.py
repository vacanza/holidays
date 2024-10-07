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

from holidays.constants import GOVERNMENT
from holidays.countries.georgia import Georgia, GE, GEO
from tests.common import CommonCountryTests


class TestGeorgia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Georgia)

    def test_country_aliases(self):
        self.assertAliases(Georgia, GE, GEO)

    def test_no_holidays(self):
        self.assertNoHolidays(Georgia(years=1990))

    def test_family_sanctity_day(self):
        self.assertHolidays(
            Georgia(categories=GOVERNMENT, years=2024),
            ("2024-05-17", "ოჯახის სიწმინდისა და მშობლების პატივისცემის დღე"),
        )

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
        self.assertHolidayDates(
            "2020-01-01",
            "2020-01-02",
            "2020-01-07",
            "2020-01-19",
            "2020-03-03",
            "2020-03-08",
            "2020-04-09",
            "2020-04-17",
            "2020-04-18",
            "2020-04-19",
            "2020-04-20",
            "2020-05-09",
            "2020-05-12",
            "2020-05-26",
            "2020-08-28",
            "2020-10-14",
            "2020-11-23",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ახალი წელი"),
            ("2022-01-02", "ახალი წელი"),
            ("2022-01-07", "ქრისტეშობა"),
            ("2022-01-19", "ნათლისღება"),
            ("2022-03-03", "დედის დღე"),
            ("2022-03-08", "ქალთა საერთაშორისო დღე"),
            ("2022-04-09", "ეროვნული ერთიანობის დღე"),
            ("2022-04-22", "წითელი პარასკევი"),
            ("2022-04-23", "დიდი შაბათი"),
            ("2022-04-24", "აღდგომა"),
            ("2022-04-25", "შავი ორშაბათი"),
            ("2022-05-09", "ფაშიზმზე გამარჯვების დღე"),
            ("2022-05-12", "წმინდა ანდრია პირველწოდებულის დღე"),
            ("2022-05-26", "დამოუკიდებლობის დღე"),
            ("2022-08-28", "მარიამობა"),
            ("2022-10-14", "მცხეთობის"),
            ("2022-11-23", "გიორგობა"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Christmas Day"),
            ("2022-01-19", "Epiphany"),
            ("2022-03-03", "Mother's Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-09", "National Unity Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-23", "Holy Saturday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-09", "Day of Victory over Fascism"),
            ("2022-05-12", "Saint Andrew's Day"),
            ("2022-05-26", "Independence Day"),
            ("2022-08-28", "Dormition of the Mother of God"),
            ("2022-10-14", "Holiday of Svetitskhovloba, Robe of Jesus"),
            ("2022-11-23", "Saint George's Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-01-07", "Різдво Христове"),
            ("2022-01-19", "Богоявлення"),
            ("2022-03-03", "День матері"),
            ("2022-03-08", "Міжнародний жіночий день"),
            ("2022-04-09", "День національної єдності"),
            ("2022-04-22", "Страсна пʼятниця"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Великдень"),
            ("2022-04-25", "Великодній понеділок"),
            ("2022-05-09", "День перемоги над фашизмом"),
            ("2022-05-12", "День святого Андрія Первозваного"),
            ("2022-05-26", "День незалежності"),
            ("2022-08-28", "Успіння Пресвятої Богородиці"),
            ("2022-10-14", "Свято Светіцховлоба, Ризи Господньої"),
            ("2022-11-23", "День святого Георгія"),
        )
