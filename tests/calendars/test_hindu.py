#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#  Website: https://github.com/vacanza/holidays/
#  License: MIT (see LICENSE file)

from datetime import date, timedelta
from unittest import TestCase

from holidays.calendars.hindu import _CustomHinduHolidays, _HinduLunisolar


class TestHinduCalendar(TestCase):
    def test_onam_dates(self):
        calendar = _HinduLunisolar()
        for year, (month, day) in calendar.SECOND_ONAM_DATES.items():
            second_onam = date(year, month, day)
            self.assertEqual(
                (second_onam - timedelta(days=1), True), calendar.first_onam_date(year)
            )
            self.assertEqual((second_onam, True), calendar.second_onam_date(year))
            self.assertEqual(
                (second_onam + timedelta(days=1), True), calendar.third_onam_date(year)
            )
            self.assertEqual(
                (second_onam + timedelta(days=2), True), calendar.fourth_onam_date(year)
            )
            self.assertEqual(calendar.second_onam_date(year), calendar.onam_date(year))

    def test_onam_date_preserves_custom_calendar_override(self):
        class CustomHinduCalendar(_CustomHinduHolidays):
            ONAM_DATES = {2025: (8, 24)}

        self.assertEqual((date(2025, 8, 24), False), CustomHinduCalendar().onam_date(2025))
