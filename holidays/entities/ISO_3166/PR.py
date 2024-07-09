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

from holidays.entities.ISO_3166.US import UsHolidays
from holidays.holiday_base import HolidayBase


class PrHolidays(HolidayBase):
    """A class to represent holidays for Puerto Rico."""

    country = "PR"
    name = "Puerto Rico"
    supported_categories = UsHolidays.supported_categories

    def __init__(self, *args, **kwargs):
        self.us_holidays = UsHolidays(*args, **{**kwargs, "subdiv": "PR"})
        super().__init__(*args, **kwargs)

    def _populate(self, year: int):
        super()._populate(year)
        self.us_holidays._populate(year)
        self.update(self.us_holidays)
