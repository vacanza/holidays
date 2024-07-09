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

from holidays.entities.ISO_3166.GB import GbHolidays
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_SUN_TO_NEXT_MON


class ImHolidays(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """A class to represent holidays for Isle of Man."""

    country = "IM"
    name = "Isle of Man"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        self.parent_entity = GbHolidays(*args, **kwargs)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate(self, year: int):
        super()._populate(year)

        self.parent_entity._populate(year)
        self.update(self.parent_entity)

    def _populate_public_holidays(self) -> None:
        self.parent_entity._populate_public_holidays()
        self.update(self.parent_entity)

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Whit Monday.
        if self._year <= 1970:
            self._add_whit_monday("Whit Monday")

        # Late Summer bank holiday (last Monday in August)
        if self._year >= 1971:
            self._add_holiday_last_mon_of_aug("Late Summer Bank Holiday")

        # Isle of Man exclusive holidays
        # TT bank holiday (first Friday in June)
        self._add_holiday_1st_fri_of_jun("TT Bank Holiday")

        # Tynwald Day
        # Move to the next Monday if falls on a weekend.
        jul_5 = self._add_holiday_jul_5("Tynwald Day")
        if self._year >= 1992:
            self._move_holiday(jul_5, show_observed_label=False)
