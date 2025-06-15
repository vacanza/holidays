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

from holidays.calendars.gregorian import FRI, SAT
from holidays.calendars.julian import JULIAN_CALENDAR
from holidays.groups import ChristianHolidays, IslamicHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Egypt(HolidayBase, ChristianHolidays, IslamicHolidays, InternationalHolidays):
    """Egypt holidays."""

    country = "EG"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    supported_languages = ("ar", "en_US")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Coptic Christmas Day.
        self._add_christmas_day(tr("عيد الميلاد المجيد (تقويم قبطي)"))

        if self._year >= 2012:
            # January 25th Revolution.
            self._add_holiday_jan_25(tr("عيد ثورة 25 يناير"))
        elif self._year >= 2009:
            # National Police Day.
            self._add_holiday_jan_25(tr("عيد الشرطة"))

        # Coptic Easter.
        self._add_easter_sunday(tr("عيد الفصح القبطي"))

        # Spring Festival.
        self._add_easter_monday(tr("شم النسيم"))

        if self._year > 1982:
            # Sinai Liberation Day.
            self._add_holiday_apr_25(tr("عيد تحرير سيناء"))

        # Labor Day.
        self._add_labor_day(tr("عيد العمال"))

        # Armed Forces Day.
        self._add_holiday_oct_6(tr("عيد القوات المسلحة"))

        if self._year >= 2014:
            # June 30 Revolution Day.
            self._add_holiday_jun_30(tr("عيد ثورة 30 يونيو"))

        if self._year > 1952:
            # July 23 Revolution Day.
            self._add_holiday_jul_23(tr("عيد ثورة 23 يوليو"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("عيد الفطر"))
        # Eid al-Fitr Holiday.
        self._add_eid_al_fitr_day_two(tr("عطلة عيد الفطر"))
        self._add_eid_al_fitr_day_three(tr("عطلة عيد الفطر"))

        # Arafat Day.
        self._add_arafah_day(tr("يوم عرفة"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عيد الأضحى"))
        # Eid al-Adha Holiday.
        self._add_eid_al_adha_day_two(tr("عطلة عيد الأضحى"))
        self._add_eid_al_adha_day_three(tr("عطلة عيد الأضحى"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("عيد المولد النبوي"))


class EG(Egypt):
    pass


class EGY(Egypt):
    pass
