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

from holidays.constants import GREGORIAN_CALENDAR, JULIAN_CALENDAR, JAN, APR
from holidays.constants import MAR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Ukraine(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """

    country = "UA"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # The current set of holidays came into force in 1991
        # But most holiday days were implemented in 1918
        if year <= 1917:
            return

        super()._populate(year)

        # New Year's Day
        if year <= 1929 or year >= 1948:
            self._add_new_years_day("Новий рік")

        # Christmas Day (Julian calendar)
        if year >= 1991:
            self._add_christmas_day(
                "Різдво Христове (за юліанським календарем)"
            )

        # Women's Day
        if year >= 1966:
            self._add_womens_day("Міжнародний жіночий день")

        if year >= 1991:
            # Easter
            self._add_easter_sunday("Великдень (Пасха)")

            # Holy trinity
            self._add_whit_sunday("Трійця")

        # Labour Day
        name = "День міжнародної солідарності трудящих"
        if year >= 2018:
            name = "День праці"
        self._add_labour_day(name)

        # Labour Day in past
        if 1929 <= year <= 2017:
            self._add_holiday("День міжнародної солідарності трудящих", MAY, 2)

        # Victory Day
        name = "День перемоги"
        if year >= 2016:
            name = (
                "День перемоги над нацизмом у Другій світовій війні "
                "(День перемоги)"
            )
        if year >= 1965:
            self._add_world_war_two_victory_day(name)
        elif 1945 <= year <= 1946:
            self._add_world_war_two_victory_day(name)
            self._add_holiday("День перемоги над Японією", SEP, 3)

        # Constitution Day
        if year >= 1997:
            self._add_holiday("День Конституції України", JUN, 28)

        # Day of Ukrainian Statehood
        if year >= 2022:
            self._add_holiday("День Української Державності", JUL, 28)

        # Independence Day
        name = "День незалежності України"
        if year >= 1992:
            self._add_holiday(name, AUG, 24)
        elif year == 1991:
            self._add_holiday(name, JUL, 16)

        # Day of the defender of Ukraine
        if year >= 2015:
            name = "День захисника України"
            if year >= 2021:
                name = "День захисників і захисниць України"
            self._add_holiday(name, OCT, 14)

        # October Revolution
        if year <= 1999:
            name = "Річниця Великої Жовтневої соціалістичної революції"
            self._add_holiday(name, NOV, 7)
            self._add_holiday(name, NOV, 8)

        # Christmas Day (Gregorian calendar)
        if year >= 2017:
            self._add_christmas_day(
                "Різдво Христове (за григоріанським календарем)",
                GREGORIAN_CALENDAR,
            )

        # 27.01.1995: holiday on weekend move to next workday
        # https://zakon.rada.gov.ua/laws/show/35/95-вр
        # 10.01.1998: cancelled
        # https://zakon.rada.gov.ua/laws/show/785/97-вр
        # 23.04.1999: holiday on weekend move to next workday
        # https://zakon.rada.gov.ua/laws/show/576-14
        if self.observed:
            for k, v in list(self.items()):
                if (
                    self._is_weekend(k)
                    and k.year == year
                    and (
                        date(1995, JAN, 27) <= k <= date(1998, JAN, 9)
                        or k >= date(1999, APR, 23)
                    )
                ):
                    next_workday = k + rd(days=+1)
                    while self._is_weekend(next_workday) or self.get(
                        next_workday
                    ):
                        next_workday += rd(days=+1)
                    self._add_holiday(f"Вихідний за {v}", next_workday)

        # USSR holidays
        # Bloody_Sunday_(1905)
        if year <= 1950:
            self._add_holiday("День пам'яті 9 січня 1905 року", JAN, 22)

        # Paris_Commune
        if year <= 1928:
            self._add_holiday("День Паризької Комуни", MAR, 18)

        # USSR Constitution day
        name = "День Конституції СРСР"
        if 1981 <= year <= 1990:
            self._add_holiday(name, OCT, 7)
        elif 1937 <= year <= 1980:
            self._add_holiday(name, DEC, 5)


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass
