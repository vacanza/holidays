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
from holidays.calendars.gregorian import (
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
)
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Yemen(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Yemen holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Yemen>
        * <https://yemenembassy.it/festivities/>
    """

    country = "YE"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (مُقدَّر)")
    start_year = 1990
    supported_languages = ("ar", "en_US")

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=YemenIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Labor Day.
        self._add_labor_day(tr("عيد العمال"))

        # Unity Day.
        self._add_holiday_may_22(tr("اليوم الوطني للجمهورية اليمنية"))

        # Revolution Day.
        self._add_holiday_sep_26(tr("ثورة 26 سبتمبر المجيدة"))

        # Liberation Day.
        self._add_holiday_oct_14(tr("ثورة 14 أكتوبر المجيدة"))

        # Independence Day.
        self._add_holiday_nov_30(tr("عيد الجلاء"))

        # Hijri New Year.
        self._add_islamic_new_year_day(tr("عيد راس السنة الهجرية"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("المولد النبوي"))

        # Eid al-Fitr.
        name = tr("عيد الفطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("عيد الأضحى")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)
        self._add_eid_al_adha_day_four(name)


class YE(Yemen):
    pass


class YEM(Yemen):
    pass


class YemenIslamicHolidays(_CustomIslamicHolidays):
    # https://www.timeanddate.com/holidays/yemen/muharram-new-year
    HIJRI_NEW_YEAR_DATES = {
        2020: (AUG, 20),
        2021: (AUG, 10),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
    }

    # https://www.timeanddate.com/holidays/yemen/prophet-birthday
    MAWLID_DATES = {
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
    }

    # https://www.timeanddate.com/holidays/yemen/eid-al-fitr-first-day
    EID_AL_FITR_DATES = {
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 30),
    }

    # https://www.timeanddate.com/holidays/yemen/eid-al-adha-first-day
    EID_AL_ADHA_DATES = {
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
    }
