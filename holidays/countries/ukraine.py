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

from dateutil.easter import easter, EASTER_ORTHODOX
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Ukraine(HolidayBase):
    """
    http://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """

    country = "UA"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # The current set of holidays came into force in 1991
        # But most holiday days were implemented in 1918
        if year <= 1917:
            return

        if year >= 1898:
            # New Year's Day
            self[date(year, JAN, 1)] = "Новий рік"
            if year < 1918:
                return

        # Christmas Day (Orthodox)
        if year >= 1991:
            self[date(year, JAN, 7)] = "Різдво Христове (православне)"

        # Women's Day
        if year >= 1966:
            self[date(year, MAR, 8)] = "Міжнародний жіночий день"

        # Easter
        if year >= 1991:
            self[easter(year, method=EASTER_ORTHODOX)] = "Великдень (Пасха)"

        # Holy trinity
        if year >= 1991:
            self[easter(year, method=EASTER_ORTHODOX) + rd(days=49)] = "Трійця"

        # Labour Day
        if year >= 2018:
            name = "День праці"
        elif 1918 <= year <= 2017:
            name = "День міжнародної солідарності трудящих"
        self[date(year, MAY, 1)] = name

        # Labour Day in past
        if 1929 <= year <= 2017:
            self[date(year, MAY, 2)] = "День міжнародної солідарності трудящих"

        # Victory Day
        name = "День перемоги"

        if year >= 2016:
            self[
                date(year, MAY, 9)
            ] = "День перемоги над нацизмом у Другій світовій війні"
        elif 1965 <= year <= 2015:
            self[date(year, MAY, 9)] = name
        elif 1945 <= year <= 1946:
            self[date(year, MAY, 9)] = name
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
            self[date(year, OCT, 14)] = "День захисника України"

        # USSR Constitution day
        name = "День Конституції СРСР"
        if 1981 <= year <= 1990:
            self[date(year, OCT, 7)] = name
        elif 1937 <= year <= 1980:
            self[date(year, DEC, 5)] = name

        # October Revolution
        if 1918 <= year <= 1999:
            if year <= 1991:
                name = "Річниця Великої Жовтневої Соціалістичної Революції"
            else:
                name = "Річниця жовтневого перевороту"
            self[date(year, NOV, 7)] = name
            self[date(year, NOV, 8)] = name

        # Christmas Day (Catholic)
        if year >= 2017:
            self[date(year, DEC, 25)] = "Різдво Христове (католицьке)"

        # USSR holidays
        # Bloody_Sunday_(1905)
        if 1917 <= year <= 1950:
            self[date(year, JAN, 22)] = "День пам'яті 9 січня 1905 року"

        # Paris_Commune
        if 1918 <= year <= 1928:
            self[date(year, MAR, 18)] = "День паризької комуни"


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass
