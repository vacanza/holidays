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

from datetime import date, timedelta

from dateutil.easter import easter
from dateutil.relativedelta import FR, MO, TH, TU
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import (
    APR,
    AUG,
    DEC,
    FEB,
    JAN,
    JUL,
    JUN,
    MAR,
    MAY,
    NOV,
    OCT,
    SEP,
)
from holidays.holiday_base import HolidayBase


class NewYorkStockExchange(HolidayBase):
    # Official regulations:
    # https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf
    # https://www.nyse.com/markets/hours-calendars
    # Historical data:
    # s3.amazonaws.com/armstrongeconomics-wp/2013/07/NYSE-Closings.pdf

    market = "NYSE"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _get_observed(self, d):
        wdnum = d.isoweekday()
        if wdnum == 6:
            return d + rd(weekday=FR(-1))
        if wdnum == 7:
            return d + rd(weekday=MO(+1))
        return d

    def _set_observed_date(self, holiday_date, name):
        date_obs = self._get_observed(holiday_date)
        if date_obs == holiday_date:
            self[holiday_date] = name
        else:
            self[date_obs] = name + " (Observed)"

    def _populate(self, year):
        ##############################################################
        # REGULAR HOLIDAYS
        ##############################################################

        # NYD
        # This year's New Year Day.
        self._set_observed_date(date(year, JAN, 1), "New Year's Day")

        # https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf
        # As per Rule 7.2.: check if next year's NYD falls on Saturday and
        # needs to be observed on Friday (Dec 31 of previous year).
        dec_31 = date(year, DEC, 31)
        if dec_31.isoweekday() == 5:
            self._set_observed_date(dec_31 + rd(days=+1), "New Year's Day")

        # MLK - observed 1998 - 3rd Monday of Jan
        if year >= 1998:
            self[
                date(year, JAN, 1) + rd(weekday=MO(3))
            ] = "Martin Luther King Jr. Day"

        # LINCOLN BIRTHDAY: observed 1896 - 1953 and 1968, Feb 12 (observed)
        if (1896 <= year <= 1953) or year == 1968:
            lincoln = date(year, FEB, 12)
            self._set_observed_date(lincoln, "Lincoln's Birthday")

        # WASHINGTON'S BIRTHDAY: Feb 22 (obs) until 1971, then 3rd Mon of Feb
        if year < 1971:
            wash = date(year, FEB, 22)
            self._set_observed_date(wash, "Washington's Birthday")
        else:
            self[
                date(year, FEB, 1) + rd(weekday=MO(3))
            ] = "Washington's Birthday"

        # GOOD FRIDAY - closed every year except 1898, 1906, and 1907
        e = easter(year)
        if year not in [1898, 1906, 1907]:
            self[e - rd(days=2)] = "Good Friday"

        # MEM DAY (May 30) - closed every year since 1873
        # last Mon in May since 1971
        if 1873 <= year < 1971:
            memday = date(year, MAY, 30)
            self._set_observed_date(memday, "Memorial Day")
        else:
            self[date(year, MAY, 31) + rd(weekday=MO(-1))] = "Memorial Day"

        # FLAG DAY: June 14th 1916 - 1953
        if 1916 <= year <= 1953:
            flagday = date(year, JUN, 14)
            self._set_observed_date(flagday, "Flag Day")

        # JUNETEENTH: since 2021
        if year >= 2021:
            juneteenth = date(year, JUN, 19)
            self._set_observed_date(
                juneteenth, "Juneteenth National Independence Day"
            )

        # INDEPENDENCE DAY (July 4) - history suggests closed every year
        j4th = date(year, JUL, 4)
        self._set_observed_date(j4th, "Independence Day")

        # LABOR DAY - first mon in Sept, since 1887
        if year >= 1887:
            self[date(year, SEP, 1) + rd(weekday=MO(1))] = "Labor Day"

        # COLUMBUS DAY/INDIGENOUS PPL DAY: Oct 12 - closed 1909-1953
        if 1909 <= year <= 1953:
            colday = date(year, OCT, 12)
            self._set_observed_date(colday, "Columbus Day")

        # ELECTION DAY: first Tues in NOV
        # closed until 1969, then closed pres years 1972-80
        if year <= 1968:
            self[date(year, NOV, 1) + rd(weekday=TU(1))] = "Election Day"
        elif year in [1972, 1976, 1980]:
            self[date(year, NOV, 1) + rd(weekday=TU(1))] = "Election Day"

        # VETERAN'S DAY: Nov 11 - closed 1918, 1921, 1934-1953
        if year in [1918, 1921] or (1934 <= year <= 1953):
            vetday = date(year, NOV, 11)
            self._set_observed_date(vetday, "Veteran's Day")

        # THXGIVING DAY: 4th Thurs in Nov - closed every year
        self[date(year, NOV, 1) + rd(weekday=TH(4))] = "Thanksgiving Day"

        # XMAS DAY: Dec 25th - every year
        xmas = date(year, DEC, 25)
        self._set_observed_date(xmas, "Christmas Day")

        ##############################################################
        # SPECIAL HOLIDAYS
        ##############################################################
        if year == 1888:
            self[date(year, MAR, 12)] = "Blizzard of 1888"
            self[date(year, MAR, 13)] = "Blizzard of 1888"
            self[date(year, NOV, 30)] = "Thanksgiving Friday 1888"
        elif year == 1889:
            self[date(year, APR, 29)] = "Centennial of Washington Inauguration"
            self[date(year, APR, 30)] = "Centennial of Washington Inauguration"
            self[date(year, MAY, 1)] = "Centennial of Washington Inauguration"
        elif year == 1892:
            self[date(year, OCT, 12)] = "Columbian Celebration"
            self[date(year, OCT, 21)] = "Columbian Celebration"
        elif year == 1893:
            self[date(year, APR, 27)] = "Columbian Celebration"
        elif year == 1897:
            self[date(year, APR, 27)] = "Grant's Birthday"
        elif year == 1898:
            self[date(year, MAY, 4)] = "Charter Day"
        elif year == 1899:
            self[date(year, MAY, 29)] = "Monday before Decoration Day"
            self[date(year, JUL, 3)] = "Monday before Independence Day"
            self[date(year, SEP, 29)] = "Admiral Dewey Celebration"
        elif year == 1900:
            self[date(year, DEC, 24)] = "Christmas Eve"
        elif year == 1901:
            self[date(year, JUL, 5)] = "Friday after Independence Day"
            self[date(year, SEP, 19)] = "Funeral of President McKinley"
        elif year == 1903:
            self[date(year, APR, 22)] = "Opening of new NYSE building"
        elif year == 1914:
            # Beginning of WWI
            begin = date(year, JUL, 31)
            end = date(year, NOV, 27)
            for d in (
                begin + timedelta(days=n)
                for n in range((end - begin).days + 1)
            ):
                if d.isoweekday() in [6, 7]:
                    continue
                self[d] = "World War I"
        elif year == 1917:
            self[date(year, JUN, 5)] = "Draft Registration Day"
        elif year == 1918:
            self[date(year, JAN, 28)] = "Heatless Day"
            self[date(year, FEB, 4)] = "Heatless Day"
            self[date(year, FEB, 11)] = "Heatless Day"
            self[date(year, JUN, 14)] = "Heatless Day"
            self[date(year, SEP, 12)] = "Draft Registration Day"
            self[date(year, NOV, 11)] = "Armistice Day"
        elif year == 1919:
            self[date(year, MAR, 25)] = "Homecoming Day for 27th Division"
            self[date(year, MAY, 6)] = "Parade Day for 77th Division"
            self[date(year, SEP, 10)] = "Return of General Pershing"
        elif year == 1923:
            self[date(year, AUG, 3)] = "Death of President Warren G. Harding"
            self[
                date(year, AUG, 10)
            ] = "Funeral of President Warren G. Harding"
        elif year == 1927:
            self[date(year, JUN, 13)] = "Parade for Colonel Charles Lindbergh"
        elif year == 1929:
            self[date(year, NOV, 29)] = "Catch Up Day"
        elif year == 1933:
            begin = date(year, MAR, 6)
            end = date(year, MAR, 14)
            for d in (
                begin + timedelta(days=n)
                for n in range((end - begin).days + 1)
            ):
                if d.isoweekday() in [6, 7]:
                    continue
                self[d] = "Special Bank Holiday"
        elif year == 1945:
            self[date(year, AUG, 15)] = "V-J Day (WWII)"
            self[date(year, AUG, 16)] = "V-J Day (WWII)"
            self[date(year, DEC, 24)] = "Christmas Eve"
        elif year == 1954:
            self[date(year, DEC, 24)] = "Christmas Eve"
        elif year == 1956:
            self[date(year, DEC, 24)] = "Christmas Eve"
        elif year == 1958:
            self[date(year, DEC, 26)] = "Day after Christmas"
        elif year == 1961:
            self[date(year, MAY, 29)] = "Day before Decoration Day"
        elif year == 1963:
            self[date(year, NOV, 25)] = "Funeral of President John F. Kennedy"
        elif year == 1965:
            self[date(year, DEC, 24)] = "Christmas Eve"
        elif year == 1968:
            self[
                date(year, APR, 9)
            ] = "Day of Mourning for Martin Luther King Jr."
            self[date(year, JUL, 5)] = "Day after Independence Day"
            begin = date(year, JUN, 12)
            end = date(year, DEC, 31)
            for d in (
                begin + timedelta(days=n)
                for n in range((end - begin).days + 1)
            ):
                if d.isoweekday() != 3:  # Wednesday special holiday
                    continue
                self[d] = "Paper Crisis"
        elif year == 1969:
            self[date(year, FEB, 10)] = "Heavy Snow"
            self[
                date(year, MAR, 31)
            ] = "Funeral of President Dwight D. Eisenhower"
            self[
                date(year, JUL, 21)
            ] = "National Participation in Lunar Exploration"
        elif year == 1972:
            self[date(year, DEC, 28)] = "Funeral for President Harry S. Truman"
        elif year == 1973:
            self[
                date(year, JAN, 25)
            ] = "Funeral for President Lyndon B. Johnson"
        elif year == 1977:
            self[date(year, JUL, 14)] = "Blackout in New Yor City"
        elif year == 1994:
            self[
                date(year, APR, 27)
            ] = "Funeral for President Richard M. Nixon"
        elif year == 2001:
            self[date(year, SEP, 11)] = "Closed for Sept 11, 2001 Attacks"
            self[date(year, SEP, 12)] = "Closed for Sept 11, 2001 Attacks"
            self[date(year, SEP, 13)] = "Closed for Sept 11, 2001 Attacks"
            self[date(year, SEP, 14)] = "Closed for Sept 11, 2001 Attacks"
        elif year == 2004:
            self[
                date(year, JUN, 11)
            ] = "Day of Mourning for President Ronald W. Reagan"
        elif year == 2007:
            self[
                date(year, JAN, 2)
            ] = "Day of Mourning for President Gerald R. Ford"


class XNYS(NewYorkStockExchange):
    pass


class NYSE(NewYorkStockExchange):
    pass
