#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import AUG, MAR, SAT, SUN
from holidays.constants import JAN, APR, MAY, JUN, JUL, OCT
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre

WEEKEND = (SAT, SUN)


class Tunisia(HolidayBase):
    country = "TN"

    # Holidays here are estimates, it is common for the day to be pushed
    # if falls in a weekend, although not a rule that can be implemented.
    # Holidays after 2020: the following four moving date holidays whose exact
    # date is announced yearly are estimated (and so denoted):
    # - Eid El Fetr*
    # - Eid El Adha*
    # - Arafat Day*
    # - Moulad El Naby*
    # *only if hijri-converter library is installed, otherwise a warning is
    #  raised that this holiday is missing. hijri-converter requires
    #  Python >= 3.6
    # is_weekend function is there, however not activated for accuracy.

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        """
        # Function to store the holiday name in the appropriate
        # date and to shift the Public holiday in case it happens
        # on a Saturday(Weekend)
        # (NOT USED)
        def is_weekend(self, hol_date, hol_name):
            if hol_date.weekday() == FRI:
                self[hol_date] = hol_name + " [Friday]"
                self[hol_date + rd(days=+2)] = "Sunday following " + hol_name
            else:
                self[hol_date] = hol_name
        """

        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle Gregorian
            years).
            """
            if dt.year == year:
                self[dt] = hol

        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's Day"

        # Revolution and Youth Day - January 14
        self[date(year, JAN, 14)] = "Revolution and Youth Day - January 14"

        # Independence Day
        self[date(year, MAR, 20)] = "Independence Day"

        # Martyrs' Day
        self[date(year, APR, 9)] = "Martyrs' Day"

        # Labour Day
        self[date(year, MAY, 1)] = "Labour Day"

        # Republic Day
        self[date(year, JUL, 25)] = "Republic Day"

        # Women's Day
        self[date(year, AUG, 13)] = "Women's Day"

        # Evacuation Day
        self[date(year, OCT, 15)] = "Evacuation Day"

        # Eid al-Fitr - Feast Festive
        # date of observance is announced yearly, This is an estimate since
        # having the Holiday on Weekend does change the number of days,
        # deceided to leave it since marking a Weekend as a holiday
        # wouldn't do much harm.
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 10, 1):
                hol_date = date_obs
                _add_holiday(hol_date, "Eid al-Fitr")
                _add_holiday(hol_date + rd(days=1), "Eid al-Fitr Holiday")
                _add_holiday(hol_date + rd(days=2), "Eid al-Fitr Holiday")

        # Arafat Day & Eid al-Adha - Scarfice Festive
        # date of observance is announced yearly
        for yr in (year - 1, year):
            for date_obs in _islamic_to_gre(yr, 12, 9):
                hol_date = date_obs
                _add_holiday(hol_date, "Arafat Day")
                _add_holiday(hol_date + rd(days=1), "Eid al-Adha")
                _add_holiday(hol_date + rd(days=2), "Eid al-Adha Holiday")
                _add_holiday(hol_date + rd(days=3), "Eid al-Adha Holiday")

        # Islamic New Year - (hijari_year, 1, 1)
        for date_obs in _islamic_to_gre(year, 1, 1):
            hol_date = date_obs
            self[hol_date] = "Islamic New Year"

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        for date_obs in _islamic_to_gre(year, 3, 12):
            hol_date = date_obs
            self[hol_date] = "Prophet Muhammad's Birthday"


class TN(Tunisia):
    pass


class TUN(Tunisia):
    pass
