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

from holidays.constants import MAR, MAY, SEP, JULIAN_CALENDAR
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_groups import IslamicHolidays

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


class Ethiopia(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays
):
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

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)

        super().__init__(*args, **kwargs)

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
            self._add_holiday(_("አዲስ ዓመት እንቁጣጣሽ"), SEP, 12)
        else:
            # Ethiopian New Year.
            self._add_holiday(_("አዲስ ዓመት እንቁጣጣሽ"), SEP, 11)

        if self._is_leap_year(year):
            # Finding of True Cross.
            self._add_holiday(_("መስቀል"), SEP, 28)
        else:
            # Finding of True Cross.
            self._add_holiday(_("መስቀል"), SEP, 27)

        # Orthodox Christmas.
        self._add_christmas_day(_("ገና"))

        # Orthodox Epiphany.
        self._add_epiphany_day(_("ጥምቀት"))

        # Orthodox Good Friday.
        self._add_good_friday(_("ስቅለት"))

        # Orthodox Easter Sunday.
        self._add_easter_sunday(_("ፋሲካ"))

        if year > 1896:
            # Adwa Victory Day.
            self._add_holiday(_("አድዋ"), MAR, 2)

        # Labour Day.
        self._add_labour_day(_("የሰራተኞች ቀን"))

        if year > 1941:
            # Patriots Day.
            self._add_holiday(_("የአርበኞች ቀን"), MAY, 5)

        if year > 1991:
            # Downfall of Dergue Regime Day.
            self._add_holiday(_("ደርግ የወደቀበት ቀን"), MAY, 28)

        if year < 1991 and year > 1974:
            # Downfall of King Haile Selassie.
            name = _("ደርግ የመጣበት ቀን")
            if self._is_leap_year(year):
                self._add_holiday(name, SEP, 13)
            else:
                self._add_holiday(name, SEP, 12)

        # Eid al-Fitr - Feast Festive
        # date of observance is announced yearly, This is an estimate since
        # having the Holiday on Weekend does change the number of days,
        # decided to leave it since marking a Weekend as a holiday
        # wouldn't do much harm.
        self._add_eid_al_fitr_day(_("ኢድ አልፈጥር"))

        # Eid al-Adha - Sacrifice Festive
        # date of observance is announced yearly
        self._add_eid_al_adha_day(_("አረፋ"))
        self._add_eid_al_adha_day_two(_("አረፋ"))

        # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
        # Prophet Muhammad's Birthday.
        name = _("መውሊድ")
        self._add_mawlid_day(name)
        self._add_mawlid_day_two(name)


class ET(Ethiopia):
    pass


class ETH(Ethiopia):
    pass
