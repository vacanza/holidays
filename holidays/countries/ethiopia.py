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

from calendar import isleap

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
        if self.ethiopian_isleap(year):
            self._add_holiday("አዲስ ዓመት እንቁጣጣሽ/Ethiopian New Year", SEP, 12)
        else:
            self._add_holiday("አዲስ ዓመት እንቁጣጣሽ/Ethiopian New Year", SEP, 11)

        # Finding of true cross
        if self.ethiopian_isleap(year):
            self._add_holiday("መስቀል/Finding of True Cross", SEP, 28)
        else:
            self._add_holiday("መስቀል/Finding of True Cross", SEP, 27)

        # Ethiopian Christmas
        self._add_christmas_day("ገና/Ethiopian X-Mas")

        # Ethiopian Ephiphany
        self._add_epiphany_day("ጥምቀት/Ephiphany")

        # Ethiopian Good Friday
        self._add_good_friday("ስቅለት/Ethiopian Good Friday")

        # Ethiopian  Easter - Orthodox Easter
        self._add_easter_sunday("ፋሲካ/Ethiopian Easter")

        # Adwa Victory Day
        if year > 1896:
            self._add_holiday("አድዋ/Victory of Adwa", MAR, 2)

        # Labour Day
        self._add_labour_day("የሰራተኞች ቀን/Labor Day")

        # Patriots Day
        if year > 1941:
            self._add_holiday("የአርበኞች ቀን/Patriots Day", MAY, 5)

        # Derg Downfall Day
        if year > 1991:
            self._add_holiday(
                "ደርግ የወደቀበት ቀን/Downfall of Dergue regime", MAY, 28
            )

        # Downfall of King. Hailesilassie
        if year < 1991 and year > 1974:
            if self.ethiopian_isleap(year):
                self._add_holiday("ደርግ የመጣበት ቀን/Formation of Dergue", SEP, 13)
            else:
                self._add_holiday("ደርግ የመጣበት ቀን/Formation of Dergue", SEP, 12)

        # Eid al-Fitr - Feast Festive
        self._add_eid_al_fitr_day("ኢድ አልፈጥር/Eid-Al-Fitr")

        # Eid al-Adha - Scarfice Festive
        # date of observance is announced yearly
        self._add_eid_al_adha_day("አረፋ/Eid-Al-Adha")

        # Prophet Muhammad's Birthday.
        self._add_mawlid_day_two("መውሊድ/Prophet Muhammad's Birthday")

    # Ethiopian leap years are coincident with leap years in the Gregorian
    # calendar until the end of February 2100. It starts earlier from new year
    # of western calendar.
    # Ethiopian leap year starts on Sep 11, so it has an effect on
    # holidays between Sep 11 and Jan 1. Therefore, here on the following
    # function we intentionally add 1 to the leap year to offset the difference
    def ethiopian_isleap(self, year):
        return isleap(year + 1)


class ET(Ethiopia):
    pass


class ETH(Ethiopia):
    pass
