#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.constants import JAN, MAR, MAY, JUN, AUG, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.groups import ChristianHolidays, InternationalHolidays


class TurksAndCaicosIslands(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Turks and Caicos Islands holidays.
    
    References:
        * https://en.wikipedia.org/wiki/Public_holidays_in_the_Turks_and_Caicos_Islands
        * https://destinationtci.tc/turks-and-caicos-islands-public-holidays/
        * https://www.timeanddate.com/holidays/turks-and-caicos-islands/
    """

    country = "TC"
    default_language = "en_US"
    supported_languages = ("en_US",)

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day(tr("New Year's Day"))

        # Commonwealth Day (second Monday in March)
        self._add_holiday_2nd_mon_of_mar(tr("Commonwealth Day"))

        # Good Friday
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday
        self._add_easter_monday(tr("Easter Monday"))

        # JAGS McCartney Day (last Monday in May)
        self._add_holiday_last_mon_of_may(tr("JAGS McCartney Day"))

        # King's Birthday (second Monday in June)
        self._add_holiday_2nd_mon_of_jun(tr("King's Birthday"))

        # Emancipation Day
        self._add_holiday_aug_1(tr("Emancipation Day"))

        # National Youth Day (last Friday in September)
        self._add_holiday_last_fri_of_sep(tr("National Youth Day"))

        # National Heritage Day (second Monday in October)
        self._add_holiday_2nd_mon_of_oct(tr("National Heritage Day"))

        # National Day of Thanksgiving (fourth Friday in November)
        self._add_holiday_4th_fri_of_nov(tr("National Day of Thanksgiving"))

        # Christmas Day
        self._add_christmas_day(tr("Christmas Day"))

        # Boxing Day
        self._add_christmas_day_two(tr("Boxing Day"))


class TC(TurksAndCaicosIslands):
    pass


class TCA(TurksAndCaicosIslands):
    pass