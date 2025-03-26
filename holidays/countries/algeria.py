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

from holidays.calendars.gregorian import THU, FRI, SAT, SUN
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Algeria(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Algeria holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Algeria>
        * <https://www.horizons.dz/english/archives/amp/12021>
        * <https://www.thenationalnews.com/mena/2021/12/07/when-is-the-weekend-in-the-arab-world/>
    """

    country = "DZ"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    supported_languages = ("ar", "en_US", "fr")

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
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
        # The resting days are Friday and Saturday since 2009.
        # Previously, these were on Thursday and Friday as implemented in 1976.
        if self._year >= 2009:
            self.weekend = {FRI, SAT}
        elif self._year >= 1976:
            self.weekend = {THU, FRI}
        else:
            self.weekend = {SAT, SUN}

        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # In January 2018, Algeria declared Yennayer a national holiday.
        if self._year >= 2018:
            # Amazigh New Year.
            self._add_holiday_jan_12(tr("رأس السنة الأمازيغية"))

        # Labor Day.
        self._add_labor_day(tr("عيد العمال"))

        if self._year >= 1962:
            # Independence Day.
            self._add_holiday_jul_5(tr("عيد الإستقلال"))

        if self._year >= 1963:
            # Revolution Day.
            self._add_holiday_nov_1(tr("عيد الثورة"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Ashura.
        self._add_ashura_day(tr("عاشورة"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("عيد المولد النبوي"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("عيد الفطر"))
        # Eid al-Fitr Holiday.
        self._add_eid_al_fitr_day_two(tr("عطلة عيد الفطر"))
        if self._year >= 2024:
            self._add_eid_al_fitr_day_three(tr("عطلة عيد الفطر"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عيد الأضحى"))
        # Eid al-Adha Holiday.
        self._add_eid_al_adha_day_two(tr("عطلة عيد الأضحى"))
        if self._year >= 2023:
            self._add_eid_al_adha_day_three(tr("عطلة عيد الأضحى"))


class DZ(Algeria):
    pass


class DZA(Algeria):
    pass
