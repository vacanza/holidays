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

from holidays.entities.ISO_3166.ID import IdHolidays
from tests.common import CommonCountryTests


class TestIdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IdHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-01", "Lunar New Year"),
            ("2022-02-28", "Isra and Miraj"),
            ("2022-03-03", "Day of Silence"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-29", "Eid al-Fitr Joint Holiday"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Eid al-Fitr Second Day"),
            ("2022-05-04", "Eid al-Fitr Joint Holiday"),
            ("2022-05-05", "Eid al-Fitr Joint Holiday"),
            ("2022-05-06", "Eid al-Fitr Joint Holiday"),
            ("2022-05-16", "Buddha's Birthday"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-01", "Pancasila Day"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-30", "Islamic New Year"),
            ("2022-08-17", "Independence Day"),
            ("2022-10-08", "Prophet's Birthday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Joint Holiday"),
        )
