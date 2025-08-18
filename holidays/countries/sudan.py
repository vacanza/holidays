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
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SUN_TO_NEXT_MON,
)


class Sudan(
    ObservedHolidayBase,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
):
    """Sudan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Sudan>
        * <https://web.archive.org/web/20250801051246/https://www.sudanembassy.org.uk/public-holidays/>
    """

    country = "SD"
    default_language = "ar_SD"
    # %s (estimated).
    estimated_label = tr("%s (المقدرة)")
    # %s (observed).
    observed_label = tr("%s (ملاحظة)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (المقدرة، ملاحظة)")
    supported_languages = ("ar_SD", "en_US")
    start_year = 1985

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=SudanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        kwargs.setdefault("observed_rule", SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # Independence Day.
        dts_observed.add(self._add_new_years_day(tr("عيد الإستقلال")))

        # Coptic Christmas.
        dts_observed.add(
            self._add_christmas_day(tr("عيد الميلاد المجيد"), calendar=JULIAN_CALENDAR)
        )

        # Orthodox Christmas.
        dts_observed.add(self._add_holiday_jan_25(tr("عيد الميلاد الأرثوذكسي")))

        # Coptic Easter.
        dts_observed.add(
            self._add_easter_sunday(tr("عيد القيامة المجيد"), calendar=JULIAN_CALENDAR)
        )

        # Christmas Day.
        dts_observed.add(self._add_christmas_day(tr("يوم عيد الميلاد")))

        # Islamic New Year.
        dts_observed.update(self._add_islamic_new_year_day(tr("رأس السنة الهجرية")))

        # Prophet's Birthday.
        dts_observed.update(self._add_mawlid_day(tr("المولد النبوي الشريف")))

        # Eid al-Fitr.
        dts_observed.update(self._add_eid_al_fitr_day(tr("عيد الفطر المبارك")))

        # Eid al-Adha.
        dts_observed.update(self._add_eid_al_adha_day(tr("عيد الأضحى المبارك")))

        if self.observed:
            self._populate_observed(dts_observed)


class SD(Sudan):
    pass


class SDN(Sudan):
    pass


class SudanIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 10),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 1),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 30),
    }

    HIJRI_NEW_YEAR_DATES = {
        2020: (AUG, 20),
        2021: (AUG, 11),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
        2025: (JUN, 26),
    }

    MAWLID_DATES = {
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 28),
        2024: (SEP, 15),
        2025: (SEP, 4),
    }
