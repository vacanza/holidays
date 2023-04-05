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

from datetime import timedelta as td
from gettext import gettext as tr

from dateutil.easter import easter

from holidays.constants import JAN, MAY, JUL, AUG, SEP, DEC
from holidays.holiday_base import HolidayBase


class Nicaragua(HolidayBase):
    country = "NI"
    default_language = "es"
    subdivisions = [
        "AN",
        "AS",
        "BO",
        "CA",
        "CI",
        "CO",
        "ES",
        "GR",
        "JI",
        "LE",
        "MD",
        "MN",
        "MS",
        "MT",
        "NS",
        "RI",
        "SJ",
    ]

    def __init__(self, **kwargs):
        # Default subdivision to MN; prov for backwards compatibility
        if not kwargs.get("subdiv", kwargs.get("prov")):
            kwargs["subdiv"] = "MN"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day.
        self._add_holiday(tr("Año Nuevo"), JAN, 1)

        easter_date = easter(year)
        # Maundy Thursday.
        self._add_holiday(tr("Jueves Santo"), easter_date + td(days=-3))
        # Good Friday.
        self._add_holiday(tr("Viernes Santo"), easter_date + td(days=-2))
        # Labour Day.
        self._add_holiday(tr("Día del Trabajo"), MAY, 1)

        if year >= 1979:
            # Revolution Day.
            self._add_holiday(tr("Día de la Revolución"), JUL, 19)

        # Battle of San Jacinto Day.
        self._add_holiday(tr("Batalla de San Jacinto"), SEP, 14)
        # Independence Day.
        self._add_holiday(tr("Día de la Independencia"), SEP, 15)
        # Virgin's Day.
        self._add_holiday(tr("Concepción de María"), DEC, 8)
        # Christmas.
        self._add_holiday(tr("Navidad"), DEC, 25)

        # Provinces festive day
        if self.subdiv == "MN":
            # Descent of Saint Dominic.
            self._add_holiday(tr("Bajada de Santo Domingo"), AUG, 1)
            # Ascent of Saint Dominic.
            self._add_holiday(tr("Subida de Santo Domingo"), AUG, 10)


class NI(Nicaragua):
    pass


class NIC(Nicaragua):
    pass
