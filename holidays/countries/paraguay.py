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
from gettext import gettext as tr

from dateutil.easter import easter

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
    default_language = "es"

    # Public holiday.
    public_holiday = tr("Asueto adicionale")
    # Public sector holiday.
    public_sector_holiday = tr("Asueto de la Administración Pública")
    special_holidays = {
        # public holiday for business purposes, in view of
        # the recently increased risk of Dengue fever
        2007: ((JAN, 29, public_holiday),),
        # public sector holiday to celebrate Paraguay's
        # football team's qualification for the 2010 World Cup
        2009: ((SEP, 10, public_holiday),),
        2010: (
            # public holiday to coincide with the Paraguay-Italy
            # game of the current World Cup
            (JUN, 14, public_holiday),
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2011: (
            # public holiday to coincide with the current anti-Dengue drive
            (APR, 19, public_holiday),
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 20, public_sector_holiday),
            # public holidays to commemorate the Bicentennial
            # of Paraguay's independence
            (MAY, 14, public_holiday),
            (MAY, 16, public_holiday),
            # 2 year-end public sector holidays
            (DEC, 23, public_sector_holiday),
            (DEC, 30, public_sector_holiday),
        ),
        2012: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 4, public_sector_holiday),
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2013: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (MAR, 27, public_sector_holiday),
            # date of the inauguration of President-elect
            # Horacio Cartes, as a one-off non-working public holiday
            (AUG, 14, public_holiday),
        ),
        2014: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 16, public_sector_holiday),
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2015: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 1, public_sector_holiday),
            # public holidays in Paraguay on account
            # of the upcoming visit of Pope Francis in Paraguay
            (JUL, 10, public_holiday),
            (JUL, 11, public_holiday),
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2016: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (MAR, 23, public_sector_holiday),
        ),
        2017: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (MAR, 28, public_sector_holiday),
        ),
        2018: (
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2019: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 17, public_sector_holiday),
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2020: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 8, public_sector_holiday),
        ),
        2021: (
            # 2 year-end public sector holidays
            (DEC, 24, public_sector_holiday),
            (DEC, 31, public_sector_holiday),
        ),
        2022: (
            # public sector holiday to let civil servants
            # begin their Holy Week earlier
            (APR, 13, public_sector_holiday),
            # public sector holiday due to the annual May 1st
            # public holiday falling on a Sunday
            (MAY, 2, public_sector_holiday),
        ),
    }

    def _add_observed_holiday(self, name: str, dt: date) -> None:
        if self.observed or not self._is_weekend(dt):
            super()._add_holiday(name, dt)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_observed_holiday(tr("Año Nuevo"), date(year, JAN, 1))

        dates_obs = {
            2013: (MAR, 4),
            2016: (FEB, 29),
            2018: (FEB, 26),
            2022: (FEB, 28),
        }
        # Patriots Day.
        self._add_holiday(
            tr("Día de los Héroes de la Patria"),
            date(year, *dates_obs.get(year, (MAR, 1))),
        )

        # Holy Week
        easter_date = easter(year)
        # Maundy Thursday.
        self._add_holiday(tr("Jueves Santo"), easter_date + td(days=-3))
        # Good Friday.
        self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))
        # Easter Day.
        self._add_observed_holiday(tr("Día de Pascuas"), easter_date)

        # Labour Day.
        self._add_observed_holiday(
            tr("Día del Trabajador"), date(year, MAY, 1)
        )

        # Independence Day.
        name = tr("Día de la Independencia Nacional")
        if year == 2021:
            self._add_holiday(name, date(year, MAY, 14))
            self._add_holiday(name, date(year, MAY, 15))
        elif year >= 2012:
            self._add_observed_holiday(name, date(year, MAY, 14))
            self._add_observed_holiday(name, date(year, MAY, 15))
        else:
            self._add_observed_holiday(name, date(year, MAY, 15))

        dates_obs = {
            2014: (JUN, 16),
            2018: (JUN, 11),
        }
        self._add_observed_holiday(
            # Chaco Armistice Day.
            tr("Día de la Paz del Chaco"),
            date(year, *dates_obs.get(year, (JUN, 12))),
        )

        self._add_observed_holiday(
            # Asuncion Foundation's Day.
            tr("Día de la Fundación de Asunción"),
            date(year, AUG, 15),
        )

        if year >= 2000:
            dates_obs = {
                2015: (SEP, 28),
                2016: (OCT, 3),
                2017: (OCT, 2),
                2021: (SEP, 27),
                2022: (OCT, 3),
            }
            self._add_observed_holiday(
                # Boqueron Battle Day.
                tr("Día de la Batalla de Boquerón"),
                date(year, *dates_obs.get(year, (SEP, 29))),
            )

        self._add_observed_holiday(
            # Caacupe Virgin Day.
            tr("Día de la Virgen de Caacupé"),
            date(year, DEC, 8),
        )

        # Christmas.
        self._add_holiday(tr("Navidad"), date(year, DEC, 25))


class PY(Paraguay):
    pass


class PRY(Paraguay):
    pass
