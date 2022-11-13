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
    WEEKEND,
)
from holidays.holiday_base import HolidayBase


class Ukraine(HolidayBase):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """

    country = "UA"

    def _add_observed(self, holiday: date) -> None:
        """
        27.01.1995: holiday on weekend move to next workday
        https://zakon.rada.gov.ua/laws/show/35/95-вр

        10.01.1998: cancelled
        https://zakon.rada.gov.ua/laws/show/785/97-вр

        23.04.1999: holiday on weekend move to next workday
        https://zakon.rada.gov.ua/laws/show/576-14
        """
        if (
            self.observed
            and holiday.weekday() in WEEKEND
            and (
                date(1995, JAN, 27) <= holiday <= date(1998, JAN, 9)
                or holiday >= date(1999, APR, 23)
            )
        ):
            next_workday = holiday + rd(days=1)
            while next_workday.weekday() in WEEKEND or self.get(
                next_workday, None
            ):
                next_workday += rd(days=1)
            self[next_workday] = "Вихідний за " + self[holiday]

    def _populate(self, year):
        super()._populate(year)

        # The current set of holidays came into force in 1991
        # But most holiday days were implemented in 1918
        if year <= 1917:
            return

        # New Year's Day
        if year <= 1929 or year >= 1948:
            self[date(year, JAN, 1)] = "Новий рік"

        # Christmas Day (Julian calendar)
        if year >= 1991:
            self[
                date(year, JAN, 7)
            ] = "Різдво Христове (за юліанським календарем)"

        # Women's Day
        if year >= 1966:
            self[date(year, MAR, 8)] = "Міжнародний жіночий день"

        if year >= 1991:
            # Easter
            dt = easter(year, method=EASTER_ORTHODOX)
            self[dt] = "Великдень (Пасха)"

            # Holy trinity
            self[dt + rd(days=49)] = "Трійця"

        # Labour Day
        name = "День міжнародної солідарності трудящих"
        if year >= 2018:
            name = "День праці"
        self[date(year, MAY, 1)] = name

        # Labour Day in past
        if 1929 <= year <= 2017:
            self[date(year, MAY, 2)] = "День міжнародної солідарності трудящих"

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

        # Constitution Day
        if year >= 1997:
            self[date(year, JUN, 28)] = "День Конституції України"

        # Day of Ukrainian Statehood
        if year >= 2022:
            self[date(year, JUL, 28)] = "День Української Державності"

        # Independence Day
        name = "День незалежності України"
        if year >= 1992:
            self[date(year, AUG, 24)] = name
        elif year == 1991:
            self[date(year, JUL, 16)] = name

        # Day of the defender of Ukraine
        if year >= 2015:
            name = "День захисника України"
            if year >= 2021:
                name = "День захисників і захисниць України"
            self[date(year, OCT, 14)] = name

        # October Revolution
        if year <= 1999:
            name = "Річниця Великої Жовтневої соціалістичної революції"
            self[date(year, NOV, 7)] = name
            self[date(year, NOV, 8)] = name

        # Christmas Day (Gregorian calendar)
        if year >= 2017:
            self[
                date(year, DEC, 25)
            ] = "Різдво Христове (за григоріанським календарем)"

        for dt in sorted(list(self.keys())):
            if dt.year == year:
                self._add_observed(dt)

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
