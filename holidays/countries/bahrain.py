#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.relativedelta import relativedelta as rd

from holidays.constants import (
    FRI,
    SAT,
    JAN,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre

WEEKEND = (FRI, SAT)

class Bahrain(HolidayBase):
    """
    Bahrain holidays

    # Holidays based on the Islamic Calendar are estimated (and so denoted),
    # as are announced each year and based on moon sightings:
    # - Eid Al Fitr*
    # - Eid Al Adha*
    # - Al Hijra New Year*
    # - Ashoora*
    # - Prophets Birthday*
    # *only if hijri-converter library is installed, otherwise a warning is
    #  raised that this holiday is missing. hijri-converter requires
    #  Python >= 3.6
    Primary sources:
    https://www.cbb.gov.bh/official-bank-holidays/
    https://www.officeholidays.com/countries/bahrain/
    """

    country = "BH"

    def _populate(self, year):
        super()._populate(year)

        def _add_holiday(dt: date, hol: str) -> None:
            """Only add if in current year; prevents adding holidays across
            years (handles multi-day Islamic holidays that straddle Gregorian
            years).
            """
            if dt.year == year:
                self[dt] = hol

        # New Year's Day
        self[date(year, JAN, 1)] = "New Year's Day"

        # Labor day
        self[date(year, MAY, 1)] = "Labour Day"

        # National Day
        self[date(year, DEC, 16)] = "National Day"
        self[date(year, DEC, 17)] = "National Day"

        # Eid Al Fitr
        # Date is announced each year. Usually stretches along 3 or 4 days,
        # in some instances prepending/appending a day or two
        # before/after the official holiday.
        fitr = "Eid Al Fitr"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = fitr
                self[hol_date + rd(days=1)] = f"{fitr} Holiday"
                self[hol_date + rd(days=2)] = f"{fitr} Holiday"
        else:
            for yr in (year - 1, year):
                for date_obs in _islamic_to_gre(yr, 10, 1):
                    hol_date = date_obs
                    _add_holiday(hol_date, f"{fitr}* (*estimated)")
                    _add_holiday(
                        hol_date + rd(days=1),
                        f"{fitr} Holiday* (*estimated)",
                    )
                    _add_holiday(
                        hol_date + rd(days=2),
                        f"{fitr} Holiday* (*estimated)",
                    )

        # Eid Al Adha
        # Date is announced each year. Usually stretches along 3 or 4 days,
        # in some instances prepending/appending a day or two
        # before/after the official holiday.
        adha = "Eid Al Adha"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date + rd(days=1)] = adha
                self[hol_date + rd(days=2)] = f"{adha} Holiday"
                self[hol_date + rd(days=3)] = f"{adha} Holiday"
        else:
            for yr in (year - 1, year):
                for date_obs in _islamic_to_gre(yr, 12, 9):
                    hol_date = date_obs
                    _add_holiday(
                        hol_date + rd(days=1), f"{adha}* (*estimated)"
                    )
                    _add_holiday(
                        hol_date + rd(days=2),
                        f"{adha}* Holiday* (*estimated)",
                    )
                    _add_holiday(
                        hol_date + rd(days=3),
                        f"{adha} Holiday* (*estimated)",
                    )

        # Al Hijra New Year
        new_hijri_year = "Al Hijra New Year"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date] = new_hijri_year
        else:
            for date_obs in _islamic_to_gre(year, 1, 1):
                hol_date = date_obs
                self[hol_date] = f"{new_hijri_year}* (*estimated)"

        # Ashoora
        # Date is announced each year. Usually the 9th and 10th Day,
        # of the month of Muharam
        ashoora = "Ashoora"
        if year in dates_obs:
            for date_obs in dates_obs[year]:
                hol_date = date(year, *date_obs)
                self[hol_date + rd(days=9)] = ashoora
                self[hol_date + rd(days=10)] = f"{ashoora} Holiday"
        else:
            for yr in (year - 1, year):
                for date_obs in _islamic_to_gre(yr, 1, 9):
                    hol_date = date_obs
                    _add_holiday(
                        hol_date + rd(days=9), f"{ashoora}* (*estimated)"
                    )
                    _add_holiday(
                        hol_date + rd(days=10),
                        f"{ashoora}* Holiday* (*estimated)",
                    )

        # Prophets Birthday
        mawlud = "Prophets Birthday"
            if year in dates_obs:
                for date_obs in dates_obs[year]:
                    hol_date = date(year, *date_obs)
                    self[hol_date] = mawlud
            else:
                for date_obs in _islamic_to_gre(year, 3, 12):
                    hol_date = date_obs
                    self[hol_date] = f"{mawlud}* (*estimated)"


class BH(Bahrain):
    pass


class BAH(Bahrain):
    pass
