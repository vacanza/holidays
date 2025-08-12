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

from holidays.groups import TibetanCalendarHolidays
from holidays.holiday_base import HolidayBase


class TestTibetanCalendarHolidays(TestCase):
    def test_add_tibetan_calendar_holiday(self):
        # Check for out-of-range dates.
        class TestHolidays(HolidayBase, TibetanCalendarHolidays):
            def __init__(self, *args, **kwargs):
                TibetanCalendarHolidays.__init__(self)
                super().__init__(*args, **kwargs)

        test_holidays = TestHolidays()

        test_holidays._populate(2100)
        test_holidays._add_blessed_rainy_day("Blessed Rainy Day")
        test_holidays._add_birth_of_guru_rinpoche("Birth of Guru Rinpoche")
        test_holidays._add_buddha_first_sermon("Buddha First Sermon")
        test_holidays._add_buddha_parinirvana("Buddha Parinirvana")
        test_holidays._add_day_of_offering("Day of Offering")
        test_holidays._add_death_of_zhabdrung("Death of Zhabdrung")
        test_holidays._add_descending_day_of_lord_buddha("Descending Day Of Lord Buddha")
        test_holidays._add_losar("Losar")
        test_holidays._add_thimphu_drubchen_day("Thimpu Drubchoe")
        test_holidays._add_thimphu_tshechu_day("Thimphu Tshechu")
        test_holidays._add_tibetan_winter_solstice("Winter Solstice Day")
        self.assertEqual(0, len(test_holidays))
