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

from holidays.calendars import _ChineseLuniSolar, _get_nth_weekday_of_month
from holidays.constants import JAN, APR, MAY, JUN, JUL, AUG, SEP, OCT, DEC, MON
from holidays.holiday_base import HolidayBase


class HongKong(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Hong_Kong
    Holidays for 2007–2023 (government source):
    https://www.gov.hk/en/about/abouthk/holiday/index.htm
    """

    country = "HK"
    special_holidays = {
        # Special holiday on 2015 - The 70th anniversary day of the victory
        # of the Chinese people's war of resistance against Japanese
        # aggression.
        2015: (
            (
                SEP,
                3,
                "The 70th anniversary day of the victory of the Chinese "
                "people's war of resistance against Japanese aggression",
            ),
        ),
    }

    def __init__(self, **kwargs):
        self.cnls = _ChineseLuniSolar()
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Current set of holidays actually valid since 1946
        if year <= 1945:
            return None

        super()._populate(year)

        day_following = "The day following "

        # The first day of January
        first_date = date(year, JAN, 1)
        if self.observed and self._is_sunday(first_date):
            self[first_date + td(days=+1)] = (
                day_following + "the first day of January"
            )
        else:
            self[first_date] = "The first day of January"

        # Lunar New Year
        name = "Lunar New Year's Day"
        preceding_day_lunar = "The day preceding Lunar New Year's Day"
        second_day_lunar = "The second day of Lunar New Year"
        third_day_lunar = "The third day of Lunar New Year"
        fourth_day_lunar = "The fourth day of Lunar New Year"
        new_year_date = self.cnls.lunar_n_y_date(year)
        if self.observed:
            if self._is_sunday(new_year_date):
                if year in {2006, 2007, 2010}:
                    self[new_year_date + td(days=-1)] = preceding_day_lunar
                else:
                    self[new_year_date + td(days=+3)] = fourth_day_lunar
            else:
                self[new_year_date] = name
            if self._is_saturday(new_year_date):
                self[new_year_date + td(days=+3)] = fourth_day_lunar
            else:
                self[new_year_date + td(days=+1)] = second_day_lunar
            if self._is_friday(new_year_date):
                self[new_year_date + td(days=+3)] = fourth_day_lunar
            else:
                self[new_year_date + td(days=+2)] = third_day_lunar
        else:
            self[new_year_date] = name
            self[new_year_date + td(days=+1)] = second_day_lunar
            self[new_year_date + td(days=+2)] = third_day_lunar

        easter_date = easter(year)
        easter_monday_date = easter_date + td(days=+1)

        # Ching Ming Festival
        name = "Ching Ming Festival"
        if self._is_leap_year(year) or (
            year > 2008 and self._is_leap_year(year - 1)
        ):
            ching_ming_date = date(year, APR, 4)
        else:
            ching_ming_date = date(year, APR, 5)
        if self.observed and (
            self._is_sunday(ching_ming_date)
            or ching_ming_date == easter_monday_date
        ):
            self[ching_ming_date + td(days=+1)] = day_following + name
        else:
            self[ching_ming_date] = name

        # Easter Holiday
        good_friday = "Good Friday"
        easter_monday = "Easter Monday"
        self[easter_date + td(days=-2)] = good_friday
        self[easter_date + td(days=-1)] = day_following + good_friday
        if self.observed and self.get(easter_monday_date):
            self[easter_monday_date + td(days=+1)] = (
                day_following + easter_monday
            )
        else:
            self[easter_monday_date] = easter_monday

        # The Birthday of the Buddha
        if year >= 1998:
            name = "The Birthday of the Buddha"
            buddha_date = self.cnls.lunar_to_gre(year, 4, 8)
            if self.observed and self._is_sunday(buddha_date):
                self[buddha_date + td(days=+1)] = day_following + name
            else:
                self[buddha_date] = name

        # Labour Day
        if year >= 1998:
            name = "Labour Day"
            labour_date = date(year, MAY, 1)
            if self.observed and self._is_sunday(labour_date):
                self[labour_date + td(days=+1)] = day_following + name
            else:
                self[labour_date] = name

        # Tuen Ng Festival
        name = "Tuen Ng Festival"
        tuen_ng_date = self.cnls.lunar_to_gre(year, 5, 5)
        if self.observed and self._is_sunday(tuen_ng_date):
            self[tuen_ng_date + td(days=+1)] = day_following + name
        else:
            self[tuen_ng_date] = name

        # Hong Kong Special Administrative Region Establishment Day
        if year >= 1997:
            name = "Hong Kong Special Administrative Region Establishment Day"
            hksar_date = date(year, JUL, 1)
            if self.observed and self._is_sunday(hksar_date):
                self[hksar_date + td(days=+1)] = day_following + name
            else:
                self[hksar_date] = name

        # Chinese Mid-Autumn Festival
        name = "Chinese Mid-Autumn Festival"
        mid_autumn_date = self.cnls.lunar_to_gre(year, 8, 15)
        if self.observed:
            # if Chinese Mid-Autumn Festival lies on Saturday
            # before 1983 public holiday lies on Monday
            # from 1983 to 2010 public holiday lies on same day
            # since 2011 public holiday lies on Monday
            if self._is_saturday(mid_autumn_date):
                if 1983 <= year <= 2010:
                    self[mid_autumn_date] = name
                else:
                    self[mid_autumn_date + td(days=+2)] = (
                        "The second day of the " + name + " (Monday)"
                    )
            else:
                self[mid_autumn_date + td(days=+1)] = (
                    day_following + "the " + name
                )
        else:
            self[mid_autumn_date] = name

        # National Day
        if year >= 1997:
            name = "National Day"
            national_date = date(year, OCT, 1)
            if self.observed and (
                self._is_sunday(national_date) or self.get(national_date)
            ):
                self[national_date + td(days=+1)] = day_following + name
            else:
                self[national_date] = name

        # Chung Yeung Festival
        name = "Chung Yeung Festival"
        chung_yeung_date = self.cnls.lunar_to_gre(year, 9, 9)
        if self.observed and self._is_sunday(chung_yeung_date):
            self[chung_yeung_date + td(days=+1)] = day_following + name
        else:
            self[chung_yeung_date] = name

        # Christmas Day
        name = "Christmas Day"
        first_after_christmas = "The first weekday after " + name
        second_after_christmas = "The second weekday after " + name
        christmas_date = date(year, DEC, 25)
        if self.observed:
            if self._is_sunday(christmas_date):
                self[christmas_date + td(days=+1)] = first_after_christmas
                self[christmas_date + td(days=+2)] = second_after_christmas
            elif self._is_saturday(christmas_date):
                self[christmas_date] = name
                self[christmas_date + td(days=+2)] = first_after_christmas
            else:
                self[christmas_date] = name
                self[christmas_date + td(days=+1)] = first_after_christmas
        else:
            self[christmas_date] = name
            self[christmas_date + td(days=+1)] = day_following + name

        # Previous holidays
        if 1952 <= year <= 1997:
            # Queen's Birthday (June 2nd Monday)
            self[
                _get_nth_weekday_of_month(2, MON, JUN, year)
            ] = "Queen's Birthday"

        if year <= 1996:
            # Anniversary of the liberation of Hong Kong (August last Monday)
            dt = _get_nth_weekday_of_month(-1, MON, AUG, year)
            self[dt] = "Anniversary of the liberation of Hong Kong"

            # Anniversary of the victory in the Second Sino-Japanese War
            self[
                dt + td(days=-1)
            ] = "Anniversary of the victory in the Second Sino-Japanese War"


class HK(HongKong):
    pass


class HKG(HongKong):
    pass
