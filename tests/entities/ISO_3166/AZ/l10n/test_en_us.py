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

from holidays.entities.ISO_3166.AZ import AzHolidays
from tests.common import CommonCountryTests


class TestAzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AzHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day"),
            ("2023-01-03", "International Azerbaijanis Solidarity Day (observed)"),
            ("2023-01-04", "New Year's Day (observed)"),
            ("2023-01-20", "Martyrs' Day"),
            ("2023-03-08", "Women's Day"),
            ("2023-03-20", "Spring Festival"),
            ("2023-03-21", "Spring Festival"),
            ("2023-03-22", "Spring Festival"),
            ("2023-03-23", "Spring Festival"),
            ("2023-03-24", "Spring Festival"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-24", "Eid al-Fitr (observed)"),
            ("2023-05-09", "Victory over Fascism Day"),
            ("2023-05-28", "Independence Day"),
            ("2023-05-29", "Independence Day (observed)"),
            ("2023-06-15", "National Liberation Day"),
            ("2023-06-26", "Armed Forces Day"),
            ("2023-06-27", "Day off (substituted from 06/24/2023)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Day off (substituted from 06/25/2023)"),
            ("2023-09-27", "Memorial Day"),
            ("2023-10-18", "Independence Restoration Day"),
            ("2023-11-08", "Victory Day"),
            ("2023-11-09", "National Flag Day"),
            ("2023-11-10", "Day off (substituted from 11/04/2023)"),
            ("2023-11-12", "Constitution Day"),
            ("2023-11-17", "National Revival Day"),
            ("2023-12-31", "International Azerbaijanis Solidarity Day"),
        )
