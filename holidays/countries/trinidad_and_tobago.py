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

# from holidays.calendars.gregorian import JAN
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.holiday_base import HolidayBase


class TrinidadAndTobago(
    HolidayBase, ChristianHolidays, HinduCalendarHolidays, InternationalHolidays, IslamicHolidays
):
    """
    Trinidad and Tobago Holidays.

    References:
      * <https://en.wikipedia.org/wiki/Public_holidays_in_Trinidad_and_Tobago>
      * <https://otp.tt/trinidad-and-tobago/national-holidays-and-awards/>
    """

    country = "TT"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day("New Year's Day")

        # Carnival Monday
        self._add_carnival_monday("Carnival Monday")

        # Carnival Tuesday (Mardi Gras)
        self._add_carnival_tuesday("Carnival Tuesday")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Indian Arrival Day - May 30
        # self._add_holiday_may_30("Indian Arrival Day")

        # Corpus Christi
        self._add_corpus_christi_day("Corpus Christi")

        # Labour Day - June 19
        self._add_holiday_jun_19("Labour Day")

        # Emancipation Day - August 1
        self._add_holiday_aug_1("Emancipation Day")

        # Independence Day - August 31
        self._add_holiday_aug_31("Independence Day")

        # Republic Day - September 24
        self._add_holiday_sep_24("Republic Day")

        # Christmas Day
        self._add_christmas_day("Christmas Day")

        # Boxing Day
        self._add_christmas_day_two("Boxing Day")

        # Diwali
        self._add_diwali_india("Diwali")

        # Eid al-Fitr.
        # self._add_eid_al_fitr_day("Id-ul-Fitr")


class TT(TrinidadAndTobago):
    pass


class TTO(TrinidadAndTobago):
    pass
