#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.georgia import Georgia, GE, GEO
from tests.common import TestCase


class TestGeorgia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Georgia)

    def test_country_aliases(self):
        self.assertCountryAliases(Georgia, GE, GEO)

    def test_easter(self):
        self.assertHoliday(
            "2020-04-19",
            "2019-04-28",
            "2018-04-08",
        )

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
        self.assertHoliday(
            "2020-01-01",
            "2020-01-02",
            "2020-01-07",
            "2020-01-19",
            "2020-03-03",
            "2020-03-08",
            "2020-04-09",
            "2020-05-09",
            "2020-05-12",
            "2020-05-26",
            "2020-08-28",
            "2020-10-14",
            "2020-11,-23",
        )

    def test_not_holiday(self):
        self.assertNoHoliday(
            "2020-08-16",
            "2008-08-05",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ახალი წელი"),
            ("2022-01-02", "ბედობა"),
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
            ("2022-10-14", "სვეტიცხოვლობა"),
            ("2022-11-23", "გიორგობა"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-01-19", "Epiphany Day"),
            ("2022-03-03", "Mother's Day"),
            ("2022-03-08", "International Women's ay"),
            ("2022-04-09", "National Unity Day"),
            ("2022-04-22", "Orthodox Good Friday"),
            ("2022-04-23", "Orthodox Holy Saturday"),
            ("2022-04-24", "Orthodox Easter Sunday"),
            ("2022-04-25", "Orthodox Easter Monday"),
            ("2022-05-09", "Day of Victory over Fascism"),
            ("2022-05-12", "St. Andrew's Day"),
            ("2022-05-26", "Independence Day"),
            ("2022-08-28", "Saint Mary's Day"),
            ("2022-10-14", "Day of Svetitskhoveli Cathedral"),
            ("2022-11-23", "Saint George's Day"),
        )
