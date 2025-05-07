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

from datetime import date, timedelta
from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.utils import nth_weekday_of_month
from holidays.constants import (
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
    MON,
    SAT,
    SUN,
)
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class CocosIslands(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Cocos (Keeling) Islands holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Cocos_(Keeling)_Islands>
        * <https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/community-bulletins>
        * <https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/gazettes-bulletins>
        * <https://publicholidays.asia/cocos-keeling-islands/>
    """

    country = "CC"
    default_language = "coa_CC"
    # %s (observed).
    observed_label = tr("%s (disambut)")
    supported_languages = ("coa_CC", "en_AU", "en_US")
    start_year = 1955

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        islamic_show_estimated = kwargs.pop("islamic_show_estimated", True)
        IslamicHolidays.__init__(
            self, cls=CocosIslandsIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        name = tr("Hari Tahun Baru")
        self._add_observed(self._add_new_years_day(name))
        self._add_observed(self._next_year_new_years_day, name=name)

        # Australia Day.
        self._add_observed(self._add_holiday_jan_26(tr("Hari Australia")))

        # Islamic New Year.
        if self._year < 2020:
            self._add_islamic_new_year_day(tr("Tahun Baru Hijriah"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Hari Raya Puasa"))

        # Good Friday.
        self._add_good_friday(tr("Jumat Agung"))

        # Easter Monday.
        self._add_easter_monday(tr("Isnin Paskah"))

        # Self Determination Day.
        if self._year >= 1984:
            self._add_observed(self._add_holiday_apr_6(tr("Hari Penentuan Diri")))

        # ANZAC Day.
        self._add_observed(self._add_holiday_apr_25(tr("Hari ANZAC")))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Hari Raya Haji"))

        # King's Birthday.
        name = tr("Hari Ulang Tahun Raja")
        dt = self.nth_weekday_of_month(2, MON, JUN)
        self._add_holiday(name, dt)

        # Prophet Muhammad's Birthday.
        self._add_mawlid_day(tr("Hari Maulaud Nabi"))

        # Christmas Day.
        name = tr("Hari Natal")
        dt_christmas = date(self._year, DEC, 25)
        self._add_observed(dt_christmas, rule=SAT_SUN_TO_NEXT_MON)
        self._add_christmas_day(name)

        # Boxing Day.
        name = tr("Hari Boxing")
        dt_boxing = date(self._year, DEC, 26)
        self._add_christmas_day_two(name)
        boxing_weekday = dt_boxing.weekday()
        if boxing_weekday == MON:
            self._add_observed(dt_boxing, name=name, rule=MON_TO_NEXT_TUE)
        elif boxing_weekday in (SAT, SUN):
            self._add_observed(dt_boxing, name=name, rule=SAT_SUN_TO_NEXT_MON_TUE)


class CocosIslandsIslamicHolidays(_CustomIslamicHolidays):
    # Eid al-Adha.
    EID_AL_ADHA_DATES = {
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 30),
        2010: (NOV, 16),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2016: (SEP, 13),
        2017: (SEP, 1),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 11),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
        2026: (MAY, 27),
    }

    # Eid al-Fitr.
    EID_AL_FITR_DATES = {
        2007: (OCT, 15),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
        2026: (MAR, 20),
    }

    # Islamic New Year.
    HIJRI_NEW_YEAR_DATES = {
        2007: (JAN, 22),
        2008: (JAN, 10),
        2009: (DEC, 18),
        2010: (DEC, 7),
        2013: (NOV, 4),
        2014: (OCT, 27),
        2016: (OCT, 3),
        2017: (SEP, 22),
        2019: (SEP, 1),
    }

    # Prophet Muhammad's Birthday.
    MAWLID_DATES = {
        2007: (APR, 2),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2013: (JAN, 24),
        2014: (JAN, 13),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 10),
        2023: (SEP, 27),
        2024: (SEP, 16),
        2025: (SEP, 5),
        2026: (AUG, 26),
    }


class CC(CocosIslands):
    """Alias for CocosIslands class."""

    pass


class CCK(CocosIslands):
    """Alias for CocosIslands class."""

    pass
