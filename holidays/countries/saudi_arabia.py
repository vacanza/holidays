# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.relativedelta import relativedelta as rd
from holidays.constants import FRI, SAT
from holidays.constants import SEP
from holidays.holiday_base import HolidayBase
from holidays.utils import get_gre_date

# Weekend used to be THU, FRI before June 28th, 2013
WEEKEND = (FRI, SAT)


class SaudiArabia(HolidayBase):

    """
    There are only 3 official national holidays in Saudi:
    https://laboreducation.hrsd.gov.sa/en/gallery/274
    The national day holiday is based on the Georgian calendar while the
    other two holidays are based on the Islamic Calendar, and they are
    estimates as they announced each year and based on moon sightings;
    which are:
        - Eid al-Fitr*
        - Eid al-Adha*
    * only if hijri-converter library is installed, otherwise a warning is
    raised that this holiday is missing. hijri-converter requires
    Python >= 3.6
    """

    def __init__(self, **kwargs):
        self.country = "SA"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        observed_str = " (observed)"
        # Eid al-Fitr Holiday
        # The holiday defined from the four days after 29th of
        # the 9th month of the Islamic calendar (either from 30/9 to 3/10
        # or from 1/10 to 4/10 depending on observed Islamic calendar)

        holiday_name = "Eid al-Fitr Holiday"
        for hijri_date in get_gre_date(year, 9, 29):
            self[hijri_date + rd(days=1)] = holiday_name
            self[hijri_date + rd(days=2)] = holiday_name
            self[hijri_date + rd(days=3)] = holiday_name
            self[hijri_date + rd(days=4)] = holiday_name
            if self.observed:
                if (hijri_date + rd(days=1)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=5)] = holiday_name + observed_str
                if (hijri_date + rd(days=2)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=5)] = holiday_name + observed_str
                    self[hijri_date + rd(days=6)] = holiday_name + observed_str
                if (hijri_date + rd(days=3)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=5)] = holiday_name + observed_str
                    self[hijri_date + rd(days=6)] = holiday_name + observed_str
                if (hijri_date + rd(days=4)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=6)] = holiday_name + observed_str

        # Arafat Day & Eid al-Adha
        # date of observance is announced yearly
        holiday_name = "Eid al-Adha Holiday"
        for hijri_date in get_gre_date(year, 12, 9):
            self[hijri_date] = holiday_name
            self[hijri_date + rd(days=1)] = holiday_name
            self[hijri_date + rd(days=2)] = holiday_name
            self[hijri_date + rd(days=3)] = holiday_name

            if self.observed:
                if hijri_date.weekday() in WEEKEND:
                    self[hijri_date + rd(days=4)] = holiday_name + observed_str
                if (hijri_date + rd(days=1)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=4)] = holiday_name + observed_str
                    self[hijri_date + rd(days=5)] = holiday_name + observed_str
                if (hijri_date + rd(days=2)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=4)] = holiday_name + observed_str
                    self[hijri_date + rd(days=5)] = holiday_name + observed_str
                if (hijri_date + rd(days=3)).weekday() in WEEKEND:
                    self[hijri_date + rd(days=5)] = holiday_name + observed_str

        # National Day holiday (started at the year 2005).
        # Note: if national day happens within the Eid al-Fitr Holiday or
        # within Eid al-Fitr Holiday, then it is not holiday.
        holiday_name = "National Day Holiday"
        if year >= 2005:
            national_day = date(year, SEP, 23)
            if national_day not in self:
                self[national_day] = holiday_name

                if self.observed and national_day.weekday() == FRI:
                    national_day -= rd(days=1)
                    self[national_day] = holiday_name + observed_str
                elif self.observed and national_day.weekday() == SAT:
                    national_day += rd(days=1)
                    self[national_day] = holiday_name + observed_str


class SA(SaudiArabia):
    pass


class SAU(SaudiArabia):
    pass
