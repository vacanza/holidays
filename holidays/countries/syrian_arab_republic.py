# holidays
# --------
# A fast, efficient Python library for generating country, province, and state
# specific sets of holidays on the fly.
# Copyright (c) 2025 Vacanza. All rights reserved.Licensed under the terms of the MIT License.

# Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
# Website: https://github.com/vacanza/holidays
# License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, JUN, SEP

from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase

class SyrianArabRepublic(HolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """
    Syrian Arab Republic holidays.

    References:
    * [Timeanddate.com](https://www.timeanddate.com/holidays/syria/2025)
    * [OfficeHolidays.com](https://www.officeholidays.com/countries/syria/2025)
    * [PublicHolidays.me](https://publicholidays.me/syria/2025-dates/)
    * [Wikipedia](https://en.wikipedia.org/wiki/Public_holidays_in_Syria)

    Holidays are regulated by the Syrian government and may vary each year.
    """

    country = "SY"
    default_language = "ar"
    estimated_label = tr("(تقدير) %s")
    supported_categories = (GOVERNMENT, OPTIONAL, PUBLIC)
    supported_languages = ("ar", "en_US")
    start_year = 1946  # Syria's independence

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=SyrianArabRepublicIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, SyrianArabRepublicStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Revolution Day
        self._add_holiday_mar_8(tr("عيد الثورة"))

        # Mother's Day
        self._add_holiday_mar_21(tr("عيد الأم"))

        # Evacuation Day (Independence Day)
        self._add_holiday_apr_17(tr("عيد الجلاء"))

        # Labor Day
        self._add_labor_day(tr("عيد العمال"))

        # Martyrs' Day
        self._add_holiday_may_6(tr("عيد الشهداء"))

        # October Liberation Day
        self._add_holiday_oct_6(tr("عيد حرب تشرين التحريرية"))

        # Christmas Day
        self._add_christmas_day(tr("عيد الميلاد المجيد"))

        # Islamic Holidays
        self._add_eid_al_fitr_day(tr("عيد الفطر"))
        self._add_eid_al_fitr_day_two(tr("عطلة عيد الفطر"))
        self._add_eid_al_fitr_day_three(tr("عطلة عيد الفطر"))

        self._add_arafah_day(tr("وقفة عرفة"))
        self._add_eid_al_adha_day(tr("عيد الأضحى"))
        self._add_eid_al_adha_day_two(tr("عطلة عيد الأضحى"))
        self._add_eid_al_adha_day_three(tr("عطلة عيد الأضحى"))

        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))
        self._add_mawlid_day(tr("عيد المولد النبوي"))

        # Easter (Orthodox and Gregorian)
        self._add_orthodox_easter_sunday(tr("عيد الفصح (الأرثوذكسي)"))
        self._add_easter_sunday(tr("عيد الفصح (الغربي)"))


class SY(SyrianArabRepublic):
    """ISO 3166‑1 alpha‑2 code alias for Syrian Arab Republic."""
    pass
class SYR(SyrianArabRepublic):
    """ISO 3166‑1 alpha‑3 code alias for Syrian Arab Republic."""
    pass

class SyrianArabRepublicIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_FITR_DATES = {
        2025: (MAR, 31),
    }

    EID_AL_ADHA_DATES = {
        2025: (JUN, 6),
    }

    HIJRI_NEW_YEAR_DATES = {
        2025: (JUN, 27),
    }

    MAWLID_DATES = {
        2025: (SEP, 5),
    }


class SyrianArabRepublicStaticHolidays:
    """Syrian Arab Republic special holidays."""

    # No special static holidays defined for 2025
    special_government_holidays: dict[str, str] = {}
    special_optional_holidays: dict[str, str] = {}
    special_public_holidays: dict[str, str] = {}
