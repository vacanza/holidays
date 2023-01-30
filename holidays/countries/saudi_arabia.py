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

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import FEB, SEP, THU, FRI, SAT
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


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
        - Eid al-Fitr*
        - Eid al-Adha*
    * only if hijri-converter library is installed, otherwise a warning is
    raised that this holiday is missing. hijri-converter requires
    Python >= 3.6
    """

    country = "SA"

    def _populate(self, year):
        super()._populate(year)

        if year < 2013:
            # Weekend used to be THU, FRI before June 28th, 2013
            # On that year both Eids were after that date, and foudning
            # day holiday started at 2022; so what below works,
            self.weekend = (THU, FRI)
        else:
            self.weekend = (FRI, SAT)

        observed_str = " (observed)"

        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle Gregorian
            years).
            """
            if dt.year == year:
                self[dt] = hol

        # Eid al-Fitr Holiday
        # The holiday is a 4-day holiday starting on the day following the
        # 29th day of Ramadan, the 9th month of the Islamic calendar.
        # Observed days are added to make up for any days falling on a weekend.
        # Holidays may straddle across Gregorian years, so we go back one year
        # to pick up any such occurrence.
        # Date of observance is announced yearly.
        holiday_name = "Eid al-Fitr Holiday"
        for yr in (year - 1, year):
            for hijri_date in _islamic_to_gre(yr, 9, 29):
                hijri_date += rd(days=+1)
                for dys in range(4):
                    _add_holiday((hijri_date + rd(days=dys)), holiday_name)
                if self.observed:
                    weekend_days = sum(
                        (hijri_date + rd(days=dys)).weekday() in self.weekend
                        for dys in range(4)
                    )
                    for dys in range(weekend_days):
                        _add_holiday(
                            hijri_date + rd(days=4 + dys),
                            holiday_name + observed_str,
                        )

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
                    _add_holiday((hijri_date + rd(days=dys)), holiday_name)
                if self.observed:
                    weekend_days = sum(
                        (hijri_date + rd(days=dys)).weekday() in self.weekend
                        for dys in range(4)
                    )
                    for dys in range(weekend_days):
                        _add_holiday(
                            hijri_date + rd(days=4 + dys),
                            holiday_name + observed_str,
                        )

        # National Day holiday (started at the year 2005).
        # Note: if national day happens within the Eid al-Fitr Holiday or
        # within Eid al-Fitr Holiday, there is no extra holidays given for it.
        holiday_name = "National Day Holiday"
        if year >= 2005:
            national_day = date(year, SEP, 23)
            if national_day not in self:
                self[national_day] = holiday_name
                # First weekend day(Thursaday before 2013 and Friday otherwise)
                if self.observed and national_day.weekday() == self.weekend[0]:
                    national_day += rd(days=-1)
                    self[national_day] = holiday_name + observed_str
                # Second weekend day(Friday before 2013 and Saturday otherwise)
                elif (
                    self.observed and national_day.weekday() == self.weekend[1]
                ):
                    national_day += rd(days=+1)
                    self[national_day] = holiday_name + observed_str

        # Founding Day holiday (started 2022).
        # Note: if founding day happens within the Eid al-Fitr Holiday or
        # within Eid al-Fitr Holiday, there is no extra holidays given for it.
        holiday_name = "Founding Day Holiday"
        if year >= 2022:
            founding_day = date(year, FEB, 22)
            if founding_day not in self:
                self[founding_day] = holiday_name
                # First weekend day(Thursaday before 2013 and Friday otherwise)
                if self.observed and founding_day.weekday() == self.weekend[0]:
                    founding_day += rd(days=-1)
                    self[founding_day] = holiday_name + observed_str
                # Second weekend day(Friday before 2013 and Saturday otherwise)
                elif (
                    self.observed and founding_day.weekday() == self.weekend[1]
                ):
                    founding_day += rd(days=+1)
                    self[founding_day] = holiday_name + observed_str


class SA(SaudiArabia):
    pass


class SAU(SaudiArabia):
    pass
