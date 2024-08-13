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

from holidays.calendars.gregorian import SAT, SUN
from holidays.groups import InternationalHolidays, ChristianHolidays
from holidays.holiday_base import HolidayBase


class Samoa(HolidayBase, InternationalHolidays, ChristianHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Samoa
    - https://www.timeanddate.com/holidays/samoa/
    """

    country = "WS"
    weekend = {SAT, SUN}

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_new_years_day("New Year's Day")
        self._add_new_years_day_two("Day After New Year's Day")

        # Good Friday.
        self._add_good_friday("Good Friday")
        self._add_holy_saturday("Day After Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Mother's Day.
        self._add_holiday_2nd_mon_of_may("Mother's Day")

        # Independence Day.
        self._add_holiday_jun_1("Independence Day")

        # Father's Day.
        self._add_holiday_2nd_mon_of_aug("Father's Day")

        # Lotu a Tamaiti (White Monday).
        self._add_holiday_2nd_mon_of_oct("Lotu a Tamaiti (White Monday)")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Boxing Day.
        self._add_christmas_day_two("Boxing Day")


class WS(Samoa):
    pass


class WSM(Samoa):
    pass
