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
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Mauritania(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Mauritania holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Mauritania>
        * <https://web.archive.org/web/20250408205543/https://www.timeanddate.com/holidays/mauritania/>
    """

    country = "MR"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (تقديري)")
    supported_languages = ("ar", "en_MR", "en_US")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Labor Day.
        self._add_labor_day(tr("عيد العمال"))

        # Africa Day.
        self._add_africa_day(tr("يوم أفريقيا"))

        # Independence Day.
        if self._year >= 1960:
            self._add_holiday_nov_28(tr("عيد الاستقلال"))

        # Eid al-Fitr.
        eid_al_fitr = tr("عيد الفطر")
        self._add_eid_al_fitr_day(eid_al_fitr)
        self._add_eid_al_fitr_day_two(eid_al_fitr)

        # Eid al-Adha.
        eid_al_adha = tr("عيد الأضحى")
        self._add_eid_al_adha_day(eid_al_adha)
        self._add_eid_al_adha_day_two(eid_al_adha)

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # The Prophet's Birthday.
        self._add_mawlid_day(tr("المولد النبوي الشريف"))


class MR(Mauritania):
    pass


class MRT(Mauritania):
    pass
