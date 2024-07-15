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

from holidays.entities.ISO_3166.TH import ThHolidays
from tests.common import CommonCountryTests


class TestThHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ThHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
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
