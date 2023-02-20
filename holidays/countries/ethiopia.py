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

from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter, EASTER_ORTHODOX

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, MAY, SEP
from holidays.holiday_base import HolidayBase

# Ethiopian holidays are estimated: it is common for the day to be pushed
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


class Ethiopia(HolidayBase):
    country = "ET"
    default_language = "am"

    @staticmethod
    def _is_leap_year(year):
        """
        Ethiopian leap years are coincident with leap years in the Gregorian
        calendar until the end of February 2100. It starts earlier from new
        year of western calendar.
        Ethiopian leap year starts on Sep 11, so it has an effect on
        holidays between Sep 11 and Jan 1. Therefore, here on the following
        function we intentionally add 1 to the leap year to offset the
        difference.
        """
        return HolidayBase._is_leap_year(year + 1)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        # The Ethiopian New Year is called Kudus Yohannes in Ge'ez and
        # Tigrinya, while in Amharic,
        # the official language of Ethiopia it is called Enkutatash.
        # It occurs on September 11 in the Gregorian Calendar;
        # except for the year preceding a leap year, when it occurs on
        # September 12.
        if self._is_leap_year(year):
            # Ethiopian New Year.
            self[date(year, SEP, 12)] = self.tr("አዲስ ዓመት እንቁጣጣሽ")
        else:
            # Ethiopian New Year.
            self[date(year, SEP, 11)] = self.tr("አዲስ ዓመት እንቁጣጣሽ")

        # Finding of true cross.
        if self._is_leap_year(year):
            # Finding of True Cross.
            self[date(year, SEP, 28)] = self.tr("መስቀል")
        else:
            # Finding of True Cross.
            self[date(year, SEP, 27)] = self.tr("መስቀል")

        # Orthodox Christmas.
        self[date(year, JAN, 7)] = self.tr("ገና")

        # Orthodox Epiphany.
        self[date(year, JAN, 19)] = self.tr("ጥምቀት")

        easter_date = easter(year, EASTER_ORTHODOX)
        # Orthodox Good Friday.
        self[easter_date + td(days=-2)] = self.tr("ስቅለት")

        # Orthodox Easter Sunday.
        self[easter_date] = self.tr("ፋሲካ")

        if year > 1896:
            # Adwa Victory Day.
            self[date(year, MAR, 2)] = self.tr("አድዋ")

        # Labour Day.
        self[date(year, MAY, 1)] = self.tr("የሰራተኞች ቀን")

        if year > 1941:
            # Patriots Day.
            self[date(year, MAY, 5)] = self.tr("የአርበኞች ቀን")

        if year > 1991:
            # Downfall of Dergue Regime Day.
            self[date(year, MAY, 28)] = self.tr("ደርግ የወደቀበት ቀን")

        if year < 1991 and year > 1974:
            # Downfall of King Haile Selassie.
            name = self.tr("ደርግ የመጣበት ቀን")
            if self._is_leap_year(year):
                self[date(year, SEP, 13)] = name
            else:
                self[date(year, SEP, 12)] = name

        # Eid al-Fitr - Feast Festive
        # date of observance is announced yearly, This is an estimate since
        # having the Holiday on Weekend does change the number of days,
        # decided to leave it since marking a Weekend as a holiday
        # wouldn't do much harm.
        for date_obs in _islamic_to_gre(year, 10, 1):
            hol_date = date_obs
            # Eid al-Fitr.
            self[hol_date] = self.tr("ኢድ አልፈጥር")

        # Eid al-Adha - Sacrifice Festive
        # date of observance is announced yearly
        for date_obs in _islamic_to_gre(year, 12, 9):
            hol_date = date_obs
            # Eid al-Adha.
            self[hol_date + td(days=+1)] = self.tr("አረፋ")

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        for date_obs in _islamic_to_gre(year, 3, 12):
            hol_date = date_obs
            # Prophet Muhammad's Birthday.
            self[hol_date + td(days=+1)] = self.tr("መውሊድ")


class ET(Ethiopia):
    pass


class ETH(Ethiopia):
    pass
