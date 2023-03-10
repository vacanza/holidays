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
from gettext import gettext as _

from dateutil.easter import EASTER_ORTHODOX, easter

from holidays.constants import JAN, APR, MAR, MAY, JUN, JUL, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class Ukraine(HolidayBase):
    """
    Current holidays list:
    https://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """

    country = "UA"
    default_language = "uk"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Override gettext for `_("Вихідний за %s")` below.
        global _
        _ = self.gettext

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
                self._add_holiday(_("%s (вихідний)") % hol_name, obs_date)

        # The current set of holidays came into force in 1991
        if year <= 1990:
            return None

        # There is no holidays in Ukraine during the period of martial law
        # https://zakon.rada.gov.ua/laws/show/2136-20#n26
        # law is in force from March 15, 2022
        if year >= 2023:
            return None

        super()._populate(year)

        # New Year's Day.
        _add_with_observed(date(year, JAN, 1), _("Новий рік"))

        _add_with_observed(
            date(year, JAN, 7),
            # Christmas (Julian calendar).
            _("Різдво Христове (за юліанським календарем)"),
        )

        _add_with_observed(
            date(year, MAR, 8),
            # International Women's Day.
            _("Міжнародний жіночий день"),
        )

        # There is no holidays from March 15, 2022
        # https://zakon.rada.gov.ua/laws/show/2136-20#n26
        if year >= 2022:
            return None

        easter_date = easter(year, method=EASTER_ORTHODOX)
        # Easter Sunday (Pascha).
        name = _("Великдень (Пасха)")
        if year == 2000:
            _add_with_observed(easter_date, name, days=3)
        elif year in {
            2005,
            2016,
            2021,
        }:
            _add_with_observed(easter_date, name, days=2)
        else:
            _add_with_observed(easter_date, name)

        # Holy Trinity Day.
        _add_with_observed(easter_date + td(days=+49), _("Трійця"))

        dt = date(year, MAY, 1)
        if year >= 2018:
            # Labour Day.
            name = _("День праці")
            _add_with_observed(dt, name)
        else:
            # International Workers' Solidarity Day.
            name = _("День міжнародної солідарності трудящих")
            _add_with_observed(dt, name, days=2)
            _add_with_observed(dt + td(days=+1), name, days=2)

        dt = date(year, MAY, 9)
        name = (
            # Day of Victory over Nazism in World War II (Victory Day).
            _(
                "День перемоги над нацизмом у Другій світовій війні "
                "(День перемоги)"
            )
            if year >= 2016
            # Victory Day.
            else _("День перемоги")
        )
        _add_with_observed(dt, name)

        if year >= 1997:
            _add_with_observed(
                date(year, JUN, 28),
                # Day of the Constitution of Ukraine.
                _("День Конституції України"),
            )

        # Independence Day.
        name = _("День незалежності України")
        if year >= 1992:
            _add_with_observed(date(year, AUG, 24), name)
        else:
            self._add_holiday(name, JUL, 16)

        if year >= 2015:
            name = (
                # Day of the defender of Ukraine.
                _("День захисників і захисниць України")
                if year >= 2021
                # Defender of Ukraine Day.
                else _("День захисника України")
            )
            _add_with_observed(date(year, OCT, 14), name)

        if year <= 1999:
            # Anniversary of the Great October Socialist Revolution.
            name = _("Річниця Великої Жовтневої соціалістичної революції")
            _add_with_observed(date(year, NOV, 7), name, days=2)
            _add_with_observed(date(year, NOV, 8), name, days=2)

        if year >= 2017:
            _add_with_observed(
                date(year, DEC, 25),
                # Christmas (Gregorian calendar).
                _("Різдво Христове (за григоріанським календарем)"),
            )


class UA(Ukraine):
    pass


class UKR(Ukraine):
    pass
