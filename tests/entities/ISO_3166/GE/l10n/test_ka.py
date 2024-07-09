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

from holidays.entities.ISO_3166.GE import GeHolidays
from tests.common import CommonCountryTests


class TestGeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GeHolidays)

    def test_ka(self):
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
