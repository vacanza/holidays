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

# from holidays.calendars.gregorian import JAN
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.holiday_base import HolidayBase

# from holidays.calendars import _CustomIslamicHolidays


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
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self,
            # cls = TrinidadAndTobagoIslamicHolidays,
            # show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # Carnival Monday.
        self._add_carnival_monday(tr("Carnival Monday"))

        # Carnival Tuesday.
        self._add_carnival_tuesday(tr("Carnival Tuesday"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Indian Arrival Day.
        self._add_holiday_may_30(tr("Indian Arrival Day"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Corpus Christi"))

        # Labour Day.
        self._add_holiday_jun_19(tr("Labour Day"))

        # African Emancipation Day.
        self._add_holiday_aug_1(tr("Emancipation Day"))

        # Independence Day.
        self._add_holiday_aug_31(tr("Independence Day"))

        # Republic Day.
        self._add_holiday_sep_24(tr("Republic Day"))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Boxing Day.
        self._add_christmas_day_two(tr("Boxing Day"))

        # Diwali.
        self._add_diwali_india(tr("Diwali"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Id-ul-Fitr"))


class TT(TrinidadAndTobago):
    pass


class TTO(TrinidadAndTobago):
    pass
