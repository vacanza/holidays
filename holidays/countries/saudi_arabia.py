#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
from datetime import timedelta as td
from gettext import gettext as tr
from typing import Set

from holidays.calendars.gregorian import FEB, SEP, NOV, THU, FRI, SAT
from holidays.groups import IslamicHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    THU_TO_PREV_WED,
    FRI_TO_PREV_THU,
    FRI_TO_NEXT_SAT,
    SAT_TO_NEXT_SUN,
    THU_FRI_TO_NEXT_WORKDAY,
    FRI_SAT_TO_NEXT_WORKDAY,
)


class SaudiArabia(ObservedHolidayBase, IslamicHolidays, StaticHolidays):
    """
    There are only 4 official national holidays in Saudi:
    https://laboreducation.hrsd.gov.sa/en/gallery/274
    https://laboreducation.hrsd.gov.sa/en/labor-education/322
    https://english.alarabiya.net/News/gulf/2022/01/27/Saudi-Arabia-to-commemorate-Founding-Day-on-Feb-22-annually-Royal-order
    The national day and the founding day holidays are based on the
    Georgian calendar while the other two holidays are based on the
    Islamic Calendar, and they are estimates as they announced each
    year and based on moon sightings;
    they are:
        - Eid al-Fitr
        - Eid al-Adha
    """

    country = "SA"
    default_language = "ar"
    # Estimated label.
    estimated_label = tr("(تقدير*) *%s")
    # %s (Observed).
    observed_label = tr("(ملاحظة) %s")
    supported_languages = ("ar", "en_US")

    def __init__(self, *args, **kwargs):
        IslamicHolidays.__init__(self)
        StaticHolidays.__init__(self, SaudiArabiaStaticHolidays)
        super().__init__(observed_rule=FRI_TO_PREV_THU + SAT_TO_NEXT_SUN, *args, **kwargs)

    def _add_islamic_observed(self, dts: Set[date]) -> None:
        # Observed days are added to make up for any days falling on a weekend.
        if not self.observed:
            return None
        observed_rule = THU_FRI_TO_NEXT_WORKDAY if self._year <= 2012 else FRI_SAT_TO_NEXT_WORKDAY
        for dt in dts:
            for i in range(4):
                self._add_observed(dt + td(days=-i), name=self[dt], rule=observed_rule)

    def _populate(self, year):
        super()._populate(year)

        # Weekend used to be THU, FRI before June 28th, 2013.
        # On that year both Eids were after that date, and Founding day
        # holiday started at 2022; so what below works.
        self._observed_rule = (
            THU_TO_PREV_WED + FRI_TO_NEXT_SAT
            if year <= 2012
            else FRI_TO_PREV_THU + SAT_TO_NEXT_SUN
        )
        self.weekend = {THU, FRI} if year <= 2012 else {FRI, SAT}

        # Eid al-Fitr Holiday
        eid_al_fitr_name = tr("عطلة عيد الفطر")
        self._add_eid_al_fitr_day(eid_al_fitr_name)
        self._add_eid_al_fitr_day_two(eid_al_fitr_name)
        self._add_eid_al_fitr_day_three(eid_al_fitr_name)
        self._add_islamic_observed(self._add_eid_al_fitr_day_four(eid_al_fitr_name))

        # Arafat Day
        self._add_arafah_day(tr("يوم عرفة"))
        # Eid al-Adha Holiday
        name = tr("عطلة عيد الأضحى")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_islamic_observed(self._add_eid_al_adha_day_three(name))

        # If National Day happens within the Eid al-Fitr Holiday or
        # Eid al-Adha Holiday, there is no extra holidays given for it.
        if year >= 2005:
            dt = date(year, SEP, 23)
            if dt not in self:
                # National Day Holiday
                self._add_observed(self._add_holiday(tr("اليوم الوطني"), dt))

        # If Founding Day happens within the Eid al-Fitr Holiday or
        # Eid al-Adha Holiday, there is no extra holidays given for it.
        if year >= 2022:
            dt = date(year, FEB, 22)
            if dt not in self:
                # Founding Day
                self._add_observed(self._add_holiday(tr("يوم التأسيسي"), dt))

        # observed holidays special case (Eid al-Fitr Holiday (observed))
        if self.observed and year == 2001:
            self._add_holiday_jan_1(self.tr(self.observed_label) % self.tr(eid_al_fitr_name))


class SA(SaudiArabia):
    pass


class SAU(SaudiArabia):
    pass


class SaudiArabiaStaticHolidays:
    special_holidays = {
        # Celebrate the country's win against Argentina in the World Cup
        2022: (NOV, 23, tr("يوم وطني")),
    }
