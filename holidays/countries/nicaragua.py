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
        self[date(year, JAN, 1)] = _("Año Nuevo")

        easter_date = easter(year)
        # Maundy Thursday.
        self[easter_date + td(days=-3)] = _("Jueves Santo")
        # Good Friday.
        self[easter_date + td(days=-2)] = _("Viernes Santo")
        # Labour Day.
        self[date(year, MAY, 1)] = _("Día del Trabajo")

        if year >= 1979:
            # Revolution Day.
            self[date(year, JUL, 19)] = _("Día de la Revolución")

        # Battle of San Jacinto Day.
        self[date(year, SEP, 14)] = _("Batalla de San Jacinto")
        # Independence Day.
        self[date(year, SEP, 15)] = _("Día de la Independencia")
        # Virgin's Day.
        self[date(year, DEC, 8)] = _("Concepción de María")
        # Christmas.
        self[date(year, DEC, 25)] = _("Navidad")

        # Provinces festive day
        if self.subdiv == "MN":
            # Descent of Saint Dominic.
            self[date(year, AUG, 1)] = _("Bajada de Santo Domingo")
            # Ascent of Saint Dominic.
            self[date(year, AUG, 10)] = _("Subida de Santo Domingo")


class NI(Nicaragua):
    pass


class NIC(Nicaragua):
    pass
