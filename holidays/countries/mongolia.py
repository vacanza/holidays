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

from gettext import gettext as tr

from holidays.groups import InternationalHolidays, MongolianCalendarHolidays
from holidays.holiday_base import HolidayBase


class Mongolia(HolidayBase, InternationalHolidays, MongolianCalendarHolidays):
    """Mongolia holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Mongolia>
        * <https://www.timeanddate.com/holidays/mongolia>
        * <https://investmongolia.gov.mn/mongolia-at-a-glance/>
        * <https://www.qppstudio.net/public-holidays/mongolia.htm>
        * <https://publicholidays.asia/mongolia/>
        * <https://www.math.mcgill.ca/gantumur/cal/year.html>
    """

    country = "MN"
    default_language = "en_MN"
    # Mongolia gained independence on December 29, 1911.
    start_year = 1912
    supported_languages = ("en_MN", "en_US", "mn")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # International Women's Day.
        self._add_womens_day(tr("International Women's Day"))

        # Children's Day.
        self._add_holiday_jun_1(tr("Children's Day"))

        # Naadam.
        self._add_holiday_jul_11(tr("Naadam"))

        # Naadam Holiday.
        name = tr("Naadam Holiday")
        self._add_holiday_jul_12(name)
        self._add_holiday_jul_13(name)
        self._add_holiday_jul_14(name)
        self._add_holiday_jul_15(name)

        if self._year >= 1925:
            # Established on November 26, 1924.
            # Republic Day.
            self._add_holiday_nov_26(tr("Republic Day"))

        # Independence Day.
        self._add_holiday_dec_29(tr("Independence Day"))


class MN(Mongolia):
    pass


class MNG(Mongolia):
    pass
