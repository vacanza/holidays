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

from dateutil.easter import easter

from holidays.calendars import _ChineseLuniSolar, _islamic_to_gre
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Indonesia(HolidayBase):
    country = "ID"
    special_holidays = {
        # Election Day
        2018: ((JUN, 27, "Hari Pemilihan"),),
        2019: ((APR, 17, "Hari Pemilihan"),),
        2020: ((DEC, 9, "Hari Pemilihan"),),
    }

    # https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia
    # https://www.timeanddate.com/holidays/indonesia
    # https://www.officeholidays.com/countries/indonesia
    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self[date(year, JAN, 1)] = "Tahun Baru Masehi"

        # Chinese New Year
        if year >= 2003:
            hol_date = self.cnls.lunar_n_y_date(year)
            self[hol_date] = "Tahun Baru Imlek"

        if year >= 1983:
            # Day of Silence
            # https://en.wikipedia.org/wiki/Nyepi
            dates_obs = {
                2009: (MAR, 26),
                2010: (MAR, 16),
                2011: (MAR, 5),
                2012: (MAR, 23),
                2013: (MAR, 12),
                2014: (MAR, 31),
                2015: (MAR, 21),
                2016: (MAR, 9),
                2017: (MAR, 28),
                2018: (MAR, 17),
                2019: (MAR, 7),
                2020: (MAR, 25),
                2021: (MAR, 14),
                2022: (MAR, 3),
                2023: (MAR, 22),
                2024: (MAR, 11),
                2025: (MAR, 29),
                2026: (MAR, 19),
            }
            if year in dates_obs:
                hol_date = date(year, *dates_obs[year])
                self[hol_date] = "Hari Suci Nyepi"

        # Eid al-Fitr
        dates_obs = {
            2001: ((DEC, 16),),
            2002: ((DEC, 6),),
            2003: ((NOV, 25),),
            2004: ((NOV, 14),),
            2005: ((NOV, 3),),
            2006: ((OCT, 24),),
            2007: ((OCT, 13),),
            2008: ((OCT, 1),),
            2009: ((SEP, 20),),
            2010: ((SEP, 10),),
            2011: ((AUG, 30),),
            2012: ((AUG, 19),),
            2013: ((AUG, 8),),
            2014: ((JUL, 28),),
            2015: ((JUL, 17),),
            2016: ((JUL, 6),),
            2017: ((JUN, 25),),
            2018: ((JUN, 15),),
            2019: ((JUN, 5),),
            2020: ((MAY, 24),),
            2021: ((MAY, 13),),
            2022: ((MAY, 2),),
            2023: ((APR, 22),),
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Idul Fitri"
                self[
                    hol_date + td(days=+1)
                ] = "Hari kedua dari Hari Raya Idul Fitri"
        else:
            for date_obs in _islamic_to_gre(year, 10, 1):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Idul Fitri* (*estimated)"
                self[
                    hol_date + td(days=+1)
                ] = "Hari kedua dari Hari Raya Idul Fitri* (*estimated)"

        # Eid al-Adha
        dates_obs = {
            2001: ((MAR, 6),),
            2002: ((FEB, 23),),
            2003: ((FEB, 12),),
            2004: ((FEB, 2),),
            2005: ((JAN, 21),),
            2006: ((JAN, 10), (DEC, 31)),
            2007: ((DEC, 20),),
            2008: ((DEC, 8),),
            2009: ((NOV, 27),),
            2010: ((NOV, 17),),
            2011: ((NOV, 6),),
            2012: ((OCT, 26),),
            2013: ((OCT, 15),),
            2014: ((OCT, 5),),
            2015: ((SEP, 24),),
            2016: ((SEP, 12),),
            2017: ((SEP, 1),),
            2018: ((AUG, 22),),
            2019: ((AUG, 11),),
            2020: ((JUL, 31),),
            2021: ((JUL, 20),),
            2022: ((JUL, 10),),
            2023: ((JUN, 29),),
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Hari Raya Idul Adha"
        else:
            for date_obs in _islamic_to_gre(year, 12, 10):
                hol_date = date_obs
                self[hol_date] = "Hari Raya Idul Adha* (*estimated)"

        # Islamic New Year
        dates_obs = {
            2001: ((MAR, 26),),
            2002: ((MAR, 15),),
            2003: ((MAR, 5),),
            2004: ((FEB, 22),),
            2005: ((FEB, 10),),
            2006: ((JAN, 31),),
            2007: ((JAN, 20),),
            2008: ((JAN, 10), (DEC, 29)),
            2009: ((DEC, 18),),
            2010: ((DEC, 7),),
            2011: ((NOV, 27),),
            2012: ((NOV, 15),),
            2013: ((NOV, 5),),
            2014: ((OCT, 25),),
            2015: ((OCT, 14),),
            2016: ((OCT, 2),),
            2017: ((SEP, 21),),
            2018: ((SEP, 11),),
            2019: ((SEP, 1),),
            2020: ((AUG, 20),),
            2021: ((AUG, 11),),
            2022: ((JUL, 30),),
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Tahun Baru Islam"
        else:
            for date_obs in _islamic_to_gre(year, 1, 1):
                hol_date = date_obs
                self[hol_date] = "Tahun Baru Islam* (*estimated)"

        # The Prophet's Birthday
        dates_obs = {
            2006: ((APR, 10),),
            2007: ((MAR, 31),),
            2008: ((MAR, 20),),
            2009: ((MAR, 9),),
            2010: ((FEB, 26),),
            2011: ((FEB, 15),),
            2012: ((FEB, 5),),
            2013: ((JAN, 24),),
            2014: ((JAN, 14),),
            2015: ((JAN, 3), (DEC, 24)),
            2016: ((DEC, 12),),
            2017: ((DEC, 1),),
            2018: ((NOV, 20),),
            2019: ((NOV, 9),),
            2020: ((OCT, 29),),
            2021: ((OCT, 19),),
            2022: ((OCT, 8),),
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Maulid Nabi Muhammad"
        else:
            for date_obs in _islamic_to_gre(year, 3, 12):
                hol_date = date_obs
                self[hol_date] = "Maulid Nabi Muhammad* (*estimated)"

        # The Prophet's Ascension
        dates_obs = {
            2001: ((OCT, 15),),
            2002: ((OCT, 4),),
            2003: ((SEP, 24),),
            2004: ((SEP, 12),),
            2005: ((SEP, 1),),
            2006: ((AUG, 22),),
            2007: ((AUG, 11),),
            2008: ((JUL, 31),),
            2009: ((JUL, 20),),
            2010: ((JUL, 9),),
            2011: ((JUN, 29),),
            2012: ((JUN, 17),),
            2013: ((JUN, 6),),
            2014: ((MAY, 27),),
            2015: ((MAY, 16),),
            2016: ((MAY, 6),),
            2017: ((APR, 24),),
            2018: ((APR, 14),),
            2019: ((APR, 3),),
            2020: ((MAR, 22),),
            2021: ((MAR, 11),),
            2022: ((FEB, 28),),
        }
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = "Isra' Mi'raj Nabi Muhammad"
        else:
            for date_obs in _islamic_to_gre(year, 7, 27):
                hol_date = date_obs
                self[hol_date] = "Isra' Mi'raj Nabi Muhammad* (*estimated)"

        # Good Friday
        self[easter(year) + td(days=-2)] = "Wafat Yesus Kristus"

        # Buddha's Birthday
        if year >= 1983:
            date_obs = {
                2007: (JUN, 1),
                2008: (MAY, 20),
                2009: (MAY, 9),
                2010: (MAY, 28),
                2011: (MAY, 17),
                2012: (MAY, 6),
                2013: (MAY, 25),
                2014: (MAY, 15),
                2015: (JUN, 2),
                2016: (MAY, 22),
                2017: (MAY, 11),
                2018: (MAY, 29),
                2019: (MAY, 19),
                2020: (MAY, 7),
                2021: (MAY, 26),
                2022: (MAY, 16),
                2023: (JUN, 4),
            }
            if year in date_obs:
                buddha_date = date(year, *date_obs[year])
                self[buddha_date] = "Hari Raya Waisak"
            else:
                buddha_date = self.cnls.vesak_date(year)
                self[buddha_date] = "Hari Raya Waisak* (*estimated)"

        # Labour Day
        if 1953 <= year <= 1968 or year >= 2014:
            self[date(year, MAY, 1)] = "Hari Buruh Internasional"

        # Ascension Day
        self[easter(year) + td(days=+39)] = "Kenaikan Yesus Kristus"

        # Pancasila Day
        if year >= 2017:
            self[date(year, JUN, 1)] = "Hari Lahir Pancasila"

        # Independence Day
        self[date(year, AUG, 17)] = "Hari Kemerdekaan Republik Indonesia"

        # Christmas Day
        self[date(year, DEC, 25)] = "Hari Raya Natal"


class ID(Indonesia):
    pass


class IDN(Indonesia):
    pass
