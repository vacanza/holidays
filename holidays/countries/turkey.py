# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.relativedelta import relativedelta as rd
from holidays.constants import FRI, SAT
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, \
    OCT, \
    NOV, DEC
from holidays.holiday_base import HolidayBase


class Turkey(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Turkey

    # *only if hijri-converter library is installed, otherwise a warning is
    #  raised that this holiday is missing. hijri-converter requires
    #  Python >= 3.6

    def __init__(self, **kwargs):
        self.country = 'TR'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # 1st of Jan
        self[date(year, JAN, 1)] = "New Year's Day"

        # 23rd of Apr
        self[date(year, APR, 23)] = "National Sovereignty and Children's Day"

        # 1st of May
        self[date(year, MAY, 1)] = "Labour Day"

        # 19th of May
        self[date(year, MAY, 19)] = "Commemoration of Ataturk, Youth and "\
            "Sports Day"

        # 15th of Jul
        # Became a national holiday after 15 Jul 2016 coup d'etat attempt.
        if year > 2016:
            self[date(year, JUL, 15)] = "Democracy and National Unity Day"

        # 30th of Aug
        self[date(year, AUG, 30)] = "Victory Day"

        # 29th of Oct
        self[date(year, OCT, 29)] = "Republic Day"

        # Ramadan Feast
        # Date of observance is announced yearly, This is an estimate.
        for date_obs in self.get_gre_date(year, 10, 1):
            hol_date = date_obs
            self[hol_date] = "Ramadan Feast"
            self[hol_date + rd(days=1)] = "Ramadan Feast Holiday"
            self[hol_date + rd(days=2)] = "Ramadan Feast Holiday"

        # Sacrifice Feast
        # Date of observance is announced yearly, This is an estimate.
        for date_obs in self.get_gre_date(year, 12, 10):
            hol_date = date_obs
            self[hol_date] = "Sacrifice Feast"
            self[hol_date + rd(days=1)] = "Sacrifice Feast Holiday"
            self[hol_date + rd(days=2)] = "Sacrifice Feast Holiday"
            self[hol_date + rd(days=3)] = "Sacrifice Feast Holiday"

    def get_gre_date(self, year, Hmonth, Hday):
        """
        returns the gregian date of of a  of the given gregorian calendar
        yyyy year with Hijari Month & Day
        """
        try:
            from hijri_converter import convert
        except ImportError:
            import warnings

            def warning_on_one_line(message, category, filename, lineno,
                                    file=None, line=None):
                return filename + ': ' + str(message) + '\n'
            warnings.formatwarning = warning_on_one_line
            warnings.warn("Error estimating Islamic Holidays." +
                          "To estimate, install hijri-converter library")
            warnings.warn("pip install -U hijri-converter")
            warnings.warn("(see https://hijri-converter.readthedocs.io/ )")
            return []
        Hyear = convert.Gregorian(year, 1, 1).to_hijri().datetuple()[0]
        hrhs = []
        hrhs.append(convert.Hijri(Hyear - 1, Hmonth, Hday).to_gregorian())
        hrhs.append(convert.Hijri(Hyear, Hmonth, Hday).to_gregorian())
        hrhs.append(convert.Hijri(Hyear + 1, Hmonth, Hday).to_gregorian())
        hrh_dates = []
        for hrh in hrhs:
            if hrh.year == year:
                hrh_dates.append(date(*hrh.datetuple()))
        return hrh_dates


class TR(Turkey):
    pass
