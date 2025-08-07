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

from holidays.groups.mandaean import MandaeanHolidays, _timedelta
from holidays.holiday_base import HolidayBase


class DummyCountry(HolidayBase, MandaeanHolidays):
    start_year = 1899

    def __init__(self, *args, **kwargs):
        MandaeanHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        self._add_great_feast_day("Great Feast")


class TestMandaeanCalendar(TestCase):
    def test_missing_date(self):
        self.assertEqual(len(DummyCountry(years=1900)), 0)

    def test_timedelta(self):
        self.assertIsNone(_timedelta(None, 1))
