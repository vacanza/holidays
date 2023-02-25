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

from holidays.constants import JULIAN_CALENDAR, JAN, APR, MAR, MAY, JUN, JUL
from holidays.constants import AUG, SEP, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChristianHolidays, InternationalHolidays


class Ukraine(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """

    country = "UA"
    default_language = "uk"

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_CALENDAR)
        InternationalHolidays.__init__(self)

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        def _add_with_observed(
            hol_date: date, hol_name: str, days: int = 1
        ) -> None:
            self._add_holiday(hol_name, hol_date)
            # 27.01.1995: holiday on weekend move to next workday
            # https://zakon.rada.gov.ua/laws/show/35/95-вр
            # 10.01.1998: cancelled
            # https://zakon.rada.gov.ua/laws/show/785/97-вр
            # 23.04.1999: holiday on weekend move to next workday
            # https://zakon.rada.gov.ua/laws/show/576-14
            if (
                self.observed
                and self._is_weekend(hol_date)
                and (
                    date(1995, JAN, 27) <= hol_date <= date(1998, JAN, 9)
                    or hol_date >= date(1999, APR, 23)
                )
            ):
                obs_date = hol_date + td(
                    days=2 if self._is_saturday(hol_date) else days
                )
                self._add_holiday(
                    self.tr("Вихідний за %s") % hol_name, obs_date
                )

        # The current set of holidays came into force in 1991
        # But most holiday days were implemented in 1918
        if year <= 1917:
            return None

        super()._populate(year)

        # New Year's Day
        if year <= 1929 or year >= 1948:
            _add_with_observed(date(year, JAN, 1), self.tr("Новий рік"))

        # Christmas Day (Julian calendar)
        if year >= 1991:
            _add_with_observed(
                date(year, JAN, 7),
                self.tr("Різдво Христове (за юліанським календарем)"),
            )

        # Women's Day
        if year >= 1966:
            _add_with_observed(
                date(year, MAR, 8), self.tr("Міжнародний жіночий день")
            )

        if year >= 1991:
            # Easter
            name = self.tr("Великдень (Пасха)")
            if year == 2000:
                _add_with_observed(self._easter_sunday, name, days=3)
            elif year in {
                2005,
                2016,
                2021,
                2027,
                2032,
                2062,
                2073,
                2078,
                2084,
            }:
                _add_with_observed(self._easter_sunday, name, days=2)
            else:
                _add_with_observed(self._easter_sunday, name)

            # Holy trinity.
            _add_with_observed(
                self._easter_sunday + td(days=+49), self.tr("Трійця")
            )

        # Labour Day.
        dt = date(year, MAY, 1)
        if year >= 2018:
            name = self.tr("День праці")
            _add_with_observed(dt, name)
        else:
            name = self.tr("День міжнародної солідарності трудящих")
            if year >= 1929:
                _add_with_observed(dt, name, days=2)
                _add_with_observed(dt + td(days=+1), name, days=2)
            else:
                self._add_holiday(name, dt)

        # Victory Day.
        dt = date(year, MAY, 9)
        name = (
            self.tr(
                "День перемоги над нацизмом у Другій світовій війні "
                "(День перемоги)"
            )
            if year >= 2016
            else self.tr("День перемоги")
        )

        if year >= 1965:
            _add_with_observed(dt, name)
        elif 1945 <= year <= 1946:
            self._add_holiday(name, dt)
            self._add_holiday(self.tr("День перемоги над Японією"), SEP, 3)

        # Constitution Day.
        if year >= 1997:
            _add_with_observed(
                date(year, JUN, 28), self.tr("День Конституції України")
            )

        # Day of Ukrainian Statehood.
        if year >= 2022:
            _add_with_observed(
                date(year, JUL, 28), self.tr("День Української Державності")
            )

        # Independence Day.
        name = self.tr("День незалежності України")
        if year >= 1992:
            _add_with_observed(date(year, AUG, 24), name)
        elif year == 1991:
            self._add_holiday(name, JUL, 16)

        # Day of the defender of Ukraine.
        if year >= 2015:
            name = (
                self.tr("День захисників і захисниць України")
                if year >= 2021
                else self.tr("День захисника України")
            )
            _add_with_observed(date(year, OCT, 14), name)

        # October Revolution.
        if year <= 1999:
            name = self.tr(
                "Річниця Великої Жовтневої соціалістичної революції"
            )
            _add_with_observed(date(year, NOV, 7), name, days=2)
            _add_with_observed(date(year, NOV, 8), name, days=2)

        # Christmas Day (Gregorian calendar).
        if year >= 2017:
            _add_with_observed(
                date(year, DEC, 25),
                self.tr("Різдво Христове (за григоріанським календарем)"),
            )

        # USSR holidays.
        # Bloody_Sunday_(1905).
        if year <= 1950:
            self._add_holiday(
                self.tr("День пам'яті 9 січня 1905 року"), JAN, 22
            )

        # Paris_Commune.
        if year <= 1928:
            self._add_holiday(self.tr("День Паризької Комуни"), MAR, 18)

        # USSR Constitution day.
        name = self.tr("День Конституції СРСР")
        if 1981 <= year <= 1990:
            self._add_holiday(name, OCT, 7)
        elif 1937 <= year <= 1980:
            self._add_holiday(name, DEC, 5)


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass
