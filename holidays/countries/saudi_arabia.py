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

from holidays.calendars import _islamic_to_gre
from holidays.constants import FEB, SEP, NOV, THU, FRI, SAT
from holidays.holiday_base import HolidayBase


class SaudiArabia(HolidayBase):
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
    special_holidays = {
        # celebrate the country's win against Argentina in the World Cup
        2022: ((NOV, 23, "National Holiday"),),
    }

    def _populate(self, year):
        def _add_with_observed(hol_date: date, hol_name: str) -> None:
            if hol_date in self:
                return None
            self[hol_date] = hol_name
            if self.observed:
                weekend = (THU, FRI) if year <= 2012 else (FRI, SAT)
                # 1st weekend day (Thursday before 2013 and Friday otherwise)
                if hol_date.weekday() == weekend[0]:
                    self[hol_date + td(days=-1)] = f"{hol_name}{observed_str}"
                # 2nd weekend day (Friday before 2013 and Saturday otherwise)
                elif hol_date.weekday() == weekend[1]:
                    self[hol_date + td(days=+1)] = f"{hol_name}{observed_str}"

        def _add_islamic_observed(hol_date: date, hol_name: str) -> None:
            if self.observed:
                weekend_days = sum(
                    self._is_weekend(hol_date + td(days=i)) for i in range(4)
                )
                for i in range(weekend_days):
                    _add_holiday(
                        hol_date + td(days=+4 + i),
                        f"{hol_name}{observed_str}",
                    )

        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle Gregorian
            years).
            """
            if dt.year == year:
                self[dt] = hol

        super()._populate(year)

        # Weekend used to be THU, FRI before June 28th, 2013.
        # On that year both Eids were after that date, and Founding day
        # holiday started at 2022; so what below works.
        self.weekend = {THU, FRI} if year <= 2012 else {FRI, SAT}

        observed_str = " (observed)"

        # Eid al-Fitr Holiday
        # The holiday is a 4-day holiday starting on the day following the
        # 29th day of Ramadan, the 9th month of the Islamic calendar.
        # Observed days are added to make up for any days falling on a weekend.
        # Holidays may straddle across Gregorian years, so we go back one year
        # to pick up any such occurrence.
        # Date of observance is announced yearly.
        holiday_name = "Eid al-Fitr Holiday"
        for yr in (year - 1, year):
            for hijri_date in _islamic_to_gre(yr, 10, 1):
                for dys in range(4):
                    _add_holiday(hijri_date + td(days=dys), holiday_name)
                _add_islamic_observed(hijri_date, holiday_name)

        # Arafat Day & Eid al-Adha
        # The holiday is a 4-day holiday starting on Arafat Day, the 10th of
        # Dhu al-Hijjah, the 12th month of the Islamic calendar.
        # Observed days are added to make up for any days falling on a weekend.
        # Holidays may straddle across Gregorian years, so we go back one year
        # to pick up any such occurrence.
        # Date of observance is announced yearly.
        holiday_name = "Eid al-Adha Holiday"
        for yr in (year - 1, year):
            for hijri_date in _islamic_to_gre(yr, 12, 9):
                _add_holiday(hijri_date, "Arafat Day Holiday")
                for dys in range(1, 4):
                    _add_holiday(hijri_date + td(days=dys), holiday_name)
                _add_islamic_observed(hijri_date, holiday_name)

        # National Day holiday (started at the year 2005).
        # Note: if national day happens within the Eid al-Fitr Holiday or
        # within Eid al-Fitr Holiday, there is no extra holidays given for it.
        if year >= 2005:
            _add_with_observed(date(year, SEP, 23), "National Day Holiday")

        # Founding Day holiday (started 2022).
        # Note: if founding day happens within the Eid al-Fitr Holiday or
        # within Eid al-Fitr Holiday, there is no extra holidays given for it.
        if year >= 2022:
            _add_with_observed(date(year, FEB, 22), "Founding Day Holiday")


class SA(SaudiArabia):
    pass


class SAU(SaudiArabia):
    pass
