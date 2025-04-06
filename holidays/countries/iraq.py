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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    FRI,
    SAT,
)
from holidays.groups import (
    ChristianHolidays,
    HebrewCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    PersianCalendarHolidays,
)
from holidays.holiday_base import HolidayBase


class Iraq(
    HolidayBase,
    ChristianHolidays,
    HebrewCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    PersianCalendarHolidays,
):
    """Iraq Holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Iraq>
        * <https://www.timeanddate.com/holidays/iraq/>
    """

    country = "IQ"
    default_language = "ar_IQ"
    # %s (estimated).
    estimated_label = tr("%s (تقديري)")
    supported_languages = ("ar_IQ", "en_US")
    start_year = 1933
    weekend = {FRI, SAT}

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=IraqIslamicCalender, show_estimated=islamic_show_estimated
        )
        PersianCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        HebrewCalendarHolidays.__init__(self)

        # Handle special parameters for this class
        self._include_special = kwargs.pop("include_special", False)

        # Call the main parent class with the remaining arguments
        super().__init__(*args, **kwargs)

    def _add_holiday_jan_6(self, name):
        """Army Day"""
        return self._add_holiday(name, JAN, 6)

    def _add_holiday_july_14(self, name):
        """National Day"""
        return self._add_holiday(name, JUL, 14)

    def _add_holiday_oct_3(self, name):
        """National Day"""
        return self._add_holiday(name, OCT, 3)

    def _add_holiday_december_10(self, name):
        """Victory Day"""
        return self._add_holiday(name, DEC, 10)

    def _populate_public_holidays(self):
        if self._year < self.start_year:
            return

        # Temporarily disable estimated labels for 2021 and 2022
        original_show_estimated = self._islamic_calendar_show_estimated
        if self._year in (2021, 2022):
            self._islamic_calendar_show_estimated = False

        self._add_new_years_day(tr("رأس السنة الجديدة"))

        self._add_christmas_day(tr("يوم عيد الميلاد"))

        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        self._add_ashura_day(tr("عاشوراء"))

        self._add_labor_day(tr("عيد العمال"))

        if self._year not in (2021, 2022):
            self._add_eid_al_ghadir_day(tr("عيد الغدير"))

        self._add_prophet_death_day(tr("المولد النبوي الشريف"))

        self._add_nowruz_day(tr("نوروز"))

        self._add_holiday_jan_6(tr("يوم الجيش"))

        self._add_holiday_oct_3(tr("اليوم الوطني"))

        if self._year == 2022:
            self._add_holiday_july_14(tr("يوم الجمهورية"))
        else:
            self._add_holiday_july_14(tr("اليوم الوطني"))

        self._add_holiday_december_10(tr("يوم النصر"))

        name = tr("عيد الفطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        name = tr("عيد الأضحى")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)
        self._add_eid_al_adha_day_four(name)
        if self._year == 2022:
            self._add_holiday(name, JUL, 13)

        # Add special holidays only if requested
        if self._include_special:
            self.special_holidays()

        # Restore original estimated label setting
        if self._year in (2021, 2022):
            self._islamic_calendar_show_estimated = original_show_estimated

    def special_holidays(self):
        name = tr("عيد الفصح")
        self._add_easter_sunday(name)
        self._add_easter_monday(name)

        self._add_sukkot(tr("عيد العُرش"))
        self._add_passover(tr("عيد الفصح"))


class IQ(Iraq):
    pass


class IRQ(Iraq):
    pass


class IraqIslamicCalender(_CustomIslamicHolidays):
    ASHURA_DATES = {
        2001: (APR, 5),
        2002: (MAR, 25),
        2003: (MAR, 14),
        2004: (MAR, 2),
        2005: (FEB, 20),
        2006: (FEB, 9),
        2007: (JAN, 30),
        2008: (JAN, 19),
        2009: ((JAN, 7), (DEC, 27)),
        2010: (DEC, 16),
        2011: (DEC, 6),
        2012: (NOV, 25),
        2013: (NOV, 14),
        2014: (NOV, 4),
        2015: (OCT, 24),
        2016: (OCT, 12),
        2017: (OCT, 1),
        2018: (SEP, 20),
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 19),
        2022: (AUG, 8),
        2023: (JUL, 28),
        2024: (JUL, 16),
        2025: (JUL, 6),
    }

    PROPHET_DEATH_DATES = {
        2001: (MAY, 22),
        2002: (MAY, 11),
        2003: (MAY, 1),
        2004: (APR, 19),
        2005: (APR, 8),
        2006: (MAR, 29),
        2007: (MAR, 18),
        2008: (MAR, 7),
        2009: (FEB, 24),
        2010: (FEB, 13),
        2011: (FEB, 2),
        2012: (JAN, 22),
        2013: ((JAN, 11), (DEC, 31)),
        2014: (DEC, 21),
        2015: (DEC, 10),
        2016: (NOV, 28),
        2017: (NOV, 17),
        2018: (NOV, 7),
        2019: (OCT, 27),
        2020: (OCT, 16),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 14),
        2024: (SEP, 2),
        2025: (AUG, 22),
    }

    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 11), (DEC, 31)),
        2007: (DEC, 21),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 16),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        2001: (DEC, 16),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 9),
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

    EID_AL_GHADIR_DATES = {
        2001: (MAR, 14),
        2002: (MAR, 3),
        2003: (FEB, 20),
        2004: (FEB, 10),
        2005: (JAN, 29),
        2006: (JAN, 19),
        2007: ((JAN, 8), (DEC, 29)),
        2008: (DEC, 17),
        2009: (DEC, 6),
        2010: (NOV, 25),
        2011: (NOV, 15),
        2012: (NOV, 3),
        2013: (OCT, 24),
        2014: (OCT, 13),
        2015: (OCT, 2),
        2016: (SEP, 20),
        2017: (SEP, 9),
        2018: (AUG, 30),
        2019: (AUG, 20),
        2020: (AUG, 8),
        2021: (JUL, 29),
        2022: (JUL, 18),
        2023: (JUL, 7),
        2024: (JUN, 25),
        2025: (JUN, 14),
    }
