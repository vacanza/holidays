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

from holidays.calendars import _CustomIslamicHolidays, _CustomHinduHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
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
      * <https://www.timeanddate.com/holidays/trinidad/eid-al-fitr>
      * <https://calendarific.com/holiday/trinidad/eid-al-fitr>
      * <https://www.timeanddate.com/holidays/saudi-arabia/eid-al-adha>
      * <https://www.timeanddate.com/holidays/trinidad/diwali>
      * <https://calendarific.com/holiday/trinidad/diwali>
    """

    country = "TT"
    default_language = "en_TT"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    supported_languages = ("en_TT", "en_US")
    # Trinidad and Tobago gained independence on August 31, 1962.
    start_year = 1962

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, cls=TrinidadAndTobagoHinduHolidays)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=TrinidadAndTobagoIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # Spiritual Baptist Shouter Liberation Day.
        self._add_holiday_mar_30(tr("Spiritual Baptist Shouter Liberation Day"))

        # Indian Arrival Day.
        self._add_holiday_may_30(tr("Indian Arrival Day"))

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

        # Carnival Monday.
        self._add_carnival_monday(tr("Carnival Monday"))

        # Carnival Tuesday.
        self._add_carnival_tuesday(tr("Carnival Tuesday"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Corpus Christi"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Id-ul-Fitr"))

        # Diwali.
        self._add_diwali_india(tr("Diwali"))


class TT(TrinidadAndTobago):
    pass


class TTO(TrinidadAndTobago):
    pass


class TrinidadAndTobagoIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: (JAN, 10),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 2),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 6),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }


class TrinidadAndTobagoHinduHolidays(_CustomHinduHolidays):
    # Deepavali
    DIWALI_DATES = {
        2012: (NOV, 13),
        2013: (NOV, 4),
        2014: (OCT, 23),
        2015: (NOV, 11),
        2016: (OCT, 29),
        2017: (OCT, 19),
        2018: (NOV, 7),
        2019: (OCT, 27),
        2020: (NOV, 14),
        2021: (NOV, 4),
        2022: (OCT, 24),
        2023: (NOV, 12),
        2024: (OCT, 31),
        2025: (OCT, 20),
    }
