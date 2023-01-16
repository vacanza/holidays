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

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, DEC
from holidays.holiday_base import HolidayBase


class Paraguay(HolidayBase):
    """
    https://www.ghp.com.py/news/feriados-nacionales-del-ano-2019-en-paraguay
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Paraguay
    http://www.calendarioparaguay.com/
    """

    country = "PY"
    special_holidays = {
        # public holiday for business purposes, in view of
        # the recently increased risk of Dengue fever
        2007: ((JAN, 29, "Public Holiday"),),
        # public sector holiday to celebrate Paraguay's
        # football team's qualification for the 2010 World Cup
        2009: ((SEP, 10, "Public Holiday"),),
        2010: (
            # public holiday to coincide with the Paraguay-Italy
            # game of the current World Cup
            (JUN, 14, "Public Holiday"),
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2011: (
            # public holiday to coincide with the current anti-Dengue drive
            (APR, 19, "Public Holiday"),
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 20, "Public sector Holiday"),
            # public holidays to commemorate the Bicentennial
            # of Paraguay's independence
            (MAY, 14, "Public Holiday"),
            (MAY, 16, "Public Holiday"),
            # 2 year-end public sector holidays
            (DEC, 23, "Public sector Holiday"),
            (DEC, 30, "Public sector Holiday"),
        ),
        2012: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 4, "Public sector Holiday"),
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2013: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (MAR, 27, "Public sector Holiday"),
            # date of the inauguration of President-elect
            # Horacio Cartes, as a one-off non-working public holiday
            (AUG, 14, "Public Holiday"),
        ),
        2014: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 16, "Public sector Holiday"),
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2015: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 1, "Public sector Holiday"),
            # public holidays in Paraguay on account
            # of the upcoming visit of Pope Francis in Paraguay
            (JUL, 10, "Public Holiday"),
            (JUL, 11, "Public Holiday"),
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2016: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (MAR, 23, "Public sector Holiday"),
            (DEC, 26, "Public Holiday"),
        ),
        2017: (
            (JAN, 2, "Public Holiday"),
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (MAR, 28, "Public sector Holiday"),
        ),
        2018: (
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2019: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 17, "Public sector Holiday"),
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2020: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 8, "Public sector Holiday"),
        ),
        2021: (
            # 2 year-end public sector holidays
            (DEC, 24, "Public sector Holiday"),
            (DEC, 31, "Public sector Holiday"),
        ),
        2022: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 13, "Public sector Holiday"),
            # public sector holiday due to the annual May 1st
            # public holiday falling on a Sunday
            (MAY, 2, "Public Holiday"),
        ),
    }

    def _add_holiday(self, dt: date, name: str) -> None:
        if self.observed or not self._is_weekend(dt):
            self[dt] = name

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        self._add_holiday(date(year, JAN, 1), "Año Nuevo [New Year's Day]")

        # Patriots day
        dates_obs = {
            2013: (MAR, 4),
            2016: (FEB, 29),
            2018: (FEB, 26),
            2022: (FEB, 28),
        }
        self[
            date(year, *dates_obs.get(year, (MAR, 1)))
        ] = "Día de los Héroes de la Patria [Patriots Day]"

        # Holy Week
        easter_date = easter(year)
        self[easter_date + rd(days=-3)] = "Jueves Santo [Maundy Thursday]"
        self[easter_date + rd(days=-2)] = "Viernes Santo [Good Friday]"
        self._add_holiday(easter_date, "Día de Pascuas [Easter Day]")

        # Labor Day
        self._add_holiday(
            date(year, MAY, 1), "Día del Trabajador [Labour Day]"
        )

        # Independence Day
        name = "Día de la Independencia Nacional [Independence Day]"
        if year == 2021:
            self[date(year, MAY, 14)] = name
            self[date(year, MAY, 15)] = name
        elif year >= 2012:
            self._add_holiday(date(year, MAY, 14), name)
            self._add_holiday(date(year, MAY, 15), name)
        else:
            self._add_holiday(date(year, MAY, 15), name)

        # Peace in Chaco Day.
        dates_obs = {
            2014: (JUN, 16),
            2018: (JUN, 11),
        }
        self._add_holiday(
            date(year, *dates_obs.get(year, (JUN, 12))),
            "Día de la Paz del Chaco [Chaco Armistice Day]",
        )

        # Asuncion Fundation's Day
        self._add_holiday(
            date(year, AUG, 15),
            "Día de la Fundación de Asunción [Asuncion Foundation's Day]",
        )

        # Boqueron's Battle
        if year >= 2000:
            dates_obs = {
                2015: (SEP, 28),
                2016: (OCT, 3),
                2017: (OCT, 2),
                2021: (SEP, 27),
                2022: (OCT, 3),
            }
            self._add_holiday(
                date(year, *dates_obs.get(year, (SEP, 29))),
                "Día de la Batalla de Boquerón [Boqueron Battle Day]",
            )

        # Caacupe Virgin Day
        self._add_holiday(
            date(year, DEC, 8),
            "Día de la Virgen de Caacupé [Caacupe Virgin Day]",
        )

        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"


class PY(Paraguay):
    pass


class PRY(Paraguay):
    pass
