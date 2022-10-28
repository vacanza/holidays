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

from dateutil.easter import EASTER_ORTHODOX, easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import (
    JAN,
    APR,
    MAR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    FRI,
    SAT,
    SUN,
    WEEKEND,
)
from holidays.holiday_base import HolidayBase


class Ukraine(HolidayBase):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454

    27.01.1995: holiday on weekend move to next workday
    https://zakon.rada.gov.ua/laws/show/35/95-вр

    10.01.1998: cancelled
    https://zakon.rada.gov.ua/laws/show/785/97-вр

    23.04.1999: holiday on weekend move to next workday
    https://zakon.rada.gov.ua/laws/show/576-14
    """

    country = "UA"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # The current set of holidays came into force in 1991
        # But most holiday days were implemented in 1918
        if year <= 1917:
            return

        # New Year's Day
        if year <= 1929 or year >= 1948:
            dt = date(year, JAN, 1)
            self[dt] = "Новий рік"
            if (
                self.observed
                and (1996 <= year <= 1998 or year >= 2000)
                and dt.weekday() in WEEKEND
            ):
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 1 січня"

        # Christmas Day (Julian calendar)
        if year >= 1991:
            dt = date(year, JAN, 7)
            self[dt] = "Різдво Христове (за юліанським календарем)"
            if (
                self.observed
                and (1996 <= year <= 1998 or year >= 2000)
                and dt.weekday() in WEEKEND
            ):
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 7 січня"

        # Women's Day
        if year >= 1966:
            dt = date(year, MAR, 8)
            self[dt] = "Міжнародний жіночий день"
            if (
                self.observed
                and (1995 <= year <= 1997 or year >= 2000)
                and dt.weekday() in WEEKEND
            ):
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 8 березня"

        # Easter
        if year >= 1991:
            dt = easter(year, method=EASTER_ORTHODOX)
            self[dt] = "Великдень (Пасха)"
            if (
                self.observed
                and (1995 <= year <= 1997 or year >= 2000)
                and dt != date(year, MAY, 1)
            ):
                name = "Вихідний за Великдень"
                if dt == date(year, APR, 30):
                    if year <= 2017:
                        self[dt + rd(days=+3)] = name
                    else:
                        self[dt + rd(days=+2)] = name
                elif dt == date(year, MAY, 2):
                    self[dt + rd(days=+2)] = name
                else:
                    self[dt + rd(days=+1)] = name

        # Holy trinity
        if year >= 1991:
            dt = easter(year, method=EASTER_ORTHODOX) + rd(days=49)
            self[dt] = "Трійця"
            if self.observed and (1995 <= year <= 1997 or year >= 1999):
                self[dt + rd(days=+1)] = "Вихідний за Трійцю"

        # Labour Day
        name = "День міжнародної солідарності трудящих"
        dt = date(year, MAY, 1)
        if year >= 2018:
            name = "День праці"
        self[dt] = name
        if (
            self.observed
            and (1995 <= year <= 1997 or year >= 1999)
            and dt.weekday() in WEEKEND
        ):
            name = "Вихідний за 1 травня"
            if year <= 2017:
                self[dt + rd(days=+2)] = name
            else:
                self[dt + rd(weekday=MO(+1))] = name

        # Labour Day in past
        if 1929 <= year <= 2017:
            dt = date(year, MAY, 2)
            self[dt] = "День міжнародної солідарності трудящих"
            if (
                self.observed
                and (1995 <= year <= 1997 or year >= 1999)
                and dt.weekday() in WEEKEND
            ):
                self[dt + rd(days=+2)] = "Вихідний за 2 травня"

        # Victory Day
        name = "День перемоги"
        dt = date(year, MAY, 9)
        if year >= 2016:
            self[dt] = (
                "День перемоги над нацизмом у Другій світовій війні "
                "(День перемоги)"
            )
        elif 1965 <= year <= 2015:
            self[dt] = name
        elif 1945 <= year <= 1946:
            self[dt] = name
            self[date(year, SEP, 3)] = "День перемоги над Японією"
        if (
            self.observed
            and (1995 <= year <= 1997 or year >= 1999)
            and dt.weekday() in WEEKEND
        ):
            self[dt + rd(weekday=MO(+1))] = "Вихідний за 9 травня"

        # Constitution Day
        if year >= 1997:
            dt = date(year, JUN, 28)
            self[dt] = "День Конституції України"
            if (
                self.observed
                and (year == 1997 or year >= 1999)
                and dt.weekday() in WEEKEND
            ):
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 28 червня"

        # Day of Ukrainian Statehood
        if year >= 2022:
            dt = date(year, JUL, 28)
            self[dt] = "День Української Державності"
            if self.observed and dt.weekday() in WEEKEND:
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 28 липня"

        # Independence Day
        name = "День незалежності України"
        if year >= 1992:
            dt = date(year, AUG, 24)
            self[dt] = name
            if (
                self.observed
                and (1995 <= year <= 1997 or year >= 1999)
                and dt.weekday() in WEEKEND
            ):
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 24 серпня"
        elif year == 1991:
            self[date(year, JUL, 16)] = name

        # Day of the defender of Ukraine
        if year >= 2015:
            name = "День захисника України"
            dt = date(year, OCT, 14)
            if year >= 2021:
                name = "День захисників і захисниць України"
            self[dt] = name
            if self.observed and dt.weekday() in WEEKEND:
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 14 жовтня"

        # October Revolution
        if year <= 1999:
            name = "Річниця Великої Жовтневої соціалістичної революції"
            dt = date(year, NOV, 7)
            self[dt] = name
            self[dt + rd(days=+1)] = name
            if self.observed and (1995 <= year <= 1997 or year >= 1999):
                if dt.weekday() in (SAT, SUN):
                    self[dt + rd(days=+2)] = "Вихідний за 7 листопада"
                if dt.weekday() in (FRI, SAT):
                    self[dt + rd(days=+3)] = "Вихідний за 8 листопада"

        # Christmas Day (Gregorian calendar)
        if year >= 2017:
            dt = date(year, DEC, 25)
            self[dt] = "Різдво Христове (за григоріанським календарем)"
            if self.observed and dt.weekday() in WEEKEND:
                self[dt + rd(weekday=MO(+1))] = "Вихідний за 25 грудня"

        # USSR holidays
        # Bloody_Sunday_(1905)
        if year <= 1950:
            self[date(year, JAN, 22)] = "День пам’яті 9 січня 1905 року"

        # Paris_Commune
        if year <= 1928:
            self[date(year, MAR, 18)] = "День Паризької Комуни"

        # USSR Constitution day
        name = "День Конституції СРСР"
        if 1981 <= year <= 1990:
            self[date(year, OCT, 7)] = name
        elif 1937 <= year <= 1980:
            self[date(year, DEC, 5)] = name


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass
