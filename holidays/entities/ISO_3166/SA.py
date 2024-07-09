#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

"""
There are only 4 official national holidays in Saudi:
    - https://laboreducation.hrsd.gov.sa/en/gallery/274
    - https://laboreducation.hrsd.gov.sa/en/labor-education/322
    - https://english.alarabiya.net/News/gulf/2022/01/27/Saudi-Arabia-to-commemorate-Founding-Day-on-Feb-22-annually-Royal-order

The national day and the founding day holidays are based on the
Georgian calendar while the other two holidays are based on the
Islamic Calendar, and they are estimates as they announced each
year and based on moon sightings; they are:
- Eid al-Fitr
- Eid al-Adha
"""

from datetime import date
from gettext import gettext as tr
from typing import Set

from holidays.calendars.gregorian import JAN, FEB, SEP, NOV, THU, FRI, SAT, _timedelta
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


class SaHolidays(ObservedHolidayBase, IslamicHolidays, StaticHolidays):
    """A class to represent holidays for Saudi Arabia."""

    country = "SA"
    name = "Saudi Arabia"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    # %s (observed).
    observed_label = tr("(ملاحظة) %s")
    # %s (observed, estimated).
    observed_estimated_label = tr("(تقدير ملاحظة) %s")
    supported_languages = ("ar", "en_US")

    def __init__(self, *args, **kwargs):
        IslamicHolidays.__init__(self)
        StaticHolidays.__init__(self, SaStaticHolidays)
        kwargs.setdefault("observed_rule", FRI_TO_PREV_THU + SAT_TO_NEXT_SUN)
        super().__init__(*args, **kwargs)

    def _add_islamic_observed(self, dts: Set[date]) -> None:
        # Observed days are added to make up for any days falling on a weekend.
        if not self.observed:
            return None
        observed_rule = THU_FRI_TO_NEXT_WORKDAY if self._year <= 2012 else FRI_SAT_TO_NEXT_WORKDAY
        for dt in dts:
            for i in range(4):
                self._add_observed(_timedelta(dt, -i), name=self[dt], rule=observed_rule)

    def _populate_public_holidays(self):
        # Weekend used to be THU, FRI before June 28th, 2013.
        # On that year both Eids were after that date, and Founding day
        # holiday started at 2022; so what below works.
        self._observed_rule = (
            THU_TO_PREV_WED + FRI_TO_NEXT_SAT
            if self._year <= 2012
            else FRI_TO_PREV_THU + SAT_TO_NEXT_SUN
        )
        self.weekend = {THU, FRI} if self._year <= 2012 else {FRI, SAT}

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
        if self._year >= 2005:
            dt = date(self._year, SEP, 23)
            if dt not in self:
                # National Day Holiday
                self._add_observed(self._add_holiday(tr("اليوم الوطني"), dt))

        # If Founding Day happens within the Eid al-Fitr Holiday or
        # Eid al-Adha Holiday, there is no extra holidays given for it.
        if self._year >= 2022:
            dt = date(self._year, FEB, 22)
            if dt not in self:
                # Founding Day
                self._add_observed(self._add_holiday(tr("يوم التأسيسي"), dt))


class SaStaticHolidays:
    special_public_holidays = {
        # Celebrate the country's win against Argentina in the World Cup
        2022: (NOV, 23, tr("يوم وطني")),
    }

    special_public_holidays_observed = {
        # Eid al-Fitr Holiday
        2001: (JAN, 1, tr("عطلة عيد الفطر")),
    }
