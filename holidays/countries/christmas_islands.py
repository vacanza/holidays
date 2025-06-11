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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
    ChineseCalendarHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class ChristmasIslands(
    ObservedHolidayBase,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
    ChineseCalendarHolidays,
):
    """
    Christmas Islands Holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Christmas_Island>
        * <https://web.archive.org/web/20240519034837/https://www.infrastructure.gov.au/sites/default/files/documents/a11-2023-2024-public-holidays-christmas-island.pdf>
        * <https://www.infrastructure.gov.au/sites/default/files/documents/a20-2024-administrator-community-bulletin-ci-public-holidays-2025.pdf>
    """

    country = "CX"
    default_language = "en_CX"
    # %s (observed).
    observed_label = tr("%s (observed)")
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    supported_languages = ("en_CX", "en_US")
    start_year = 1985

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=ChristmasIslandsIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, ChristmasIslandsStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Australia Day
        self._add_observed(self._add_holiday_jan_26(tr("Australia Day")))

        # Chinese New Year – 2 days
        name = tr("Chinese New Year")
        self._add_observed(self._add_chinese_new_years_day(name))
        self._add_observed(self._add_chinese_new_years_day_two(name))

        # Labour Day – 4th Monday in March
        self._add_holiday_4th_mon_of_mar(tr("Labour Day"))

        # Good Friday
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday
        self._add_easter_monday(tr("Easter Monday"))

        # ANZAC Day
        self._add_observed(self._add_holiday_apr_25(tr("ANZAC Day")))

        # Territory Day – 6 October
        self._add_observed(self._add_holiday_oct_6(tr("Territory Day")))

        # Christmas & Boxing Day
        self._add_observed(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE,
        )

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))
        # Eid al-Fitr.
        for dt in self._add_eid_al_fitr_day(tr("Eid al-Fitr")):
            self._add_observed(dt)

        # Eid al-Adha.
        for dt in self._add_eid_al_adha_day(tr("Eid al-Adha")):
            if self._year != 2025:
                self._add_observed(dt)


class ChristmasIslandsIslamicHolidays(_CustomIslamicHolidays):
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
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        2007: (OCT, 15),
        2008: (OCT, 1),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2016: (JUL, 6),
        2017: (JUN, 24),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }


class CX(ChristmasIslands):
    pass


class CXR(ChristmasIslands):
    pass


class ChristmasIslandsStaticHolidays:
    """Christmas Islands special holidays.

    References:
        * [National Day of Mourning 2022](https://web.archive.org/web/20240712013008/https://www.infrastructure.gov.au/sites/default/files/documents/03-2022-proclamation-ci-day-of-mourning.pdf)
    """

    special_public_holidays = {
        # National Day of Mourning for Queen Elizabeth II.
        2022: (SEP, 22, tr("National Day of Mourning for Queen Elizabeth II")),
    }
    special_public_holidays_observed = {
        2025: (JUN, 6, tr("Eid al-Adha")),
    }
