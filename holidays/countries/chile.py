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

from datetime import date, datetime, timezone
from datetime import timedelta as td
from gettext import gettext as tr

from dateutil.easter import easter
from pymeeus.Epoch import Epoch
from pymeeus.Sun import Sun

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, MON
from holidays.holiday_base import HolidayBase

# use standard library for timezone
try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    from backports.zoneinfo import ZoneInfo  # type: ignore[no-redef]


class Chile(HolidayBase):
    """
    https://www.feriados.cl
    http://www.feriadoschilenos.cl/ (excellent history)
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Chile
    """

    country = "CL"
    special_holidays = {
        2022: ((SEP, 16, tr("Feriado nacional")),),
    }
    default_language = "es"
    # ISO 3166-2 codes for the principal subdivisions, called regions
    subdivisions = [
        "AI",
        "AN",
        "AP",
        "AR",
        "AT",
        "BI",
        "CO",
        "LI",
        "LL",
        "LR",
        "MA",
        "ML",
        "NB",
        "RM",
        "TA",
        "VS",
    ]

    def _populate(self, year):
        def _get_movable(hol_date: date) -> date:
            if year >= 2000:
                # floating Monday holiday (Law 19.668)
                if self._is_friday(hol_date):
                    hol_date = _get_nth_weekday_from(1, MON, hol_date)
                elif not self._is_weekend(hol_date):
                    hol_date = _get_nth_weekday_from(-1, MON, hol_date)
            return hol_date

        # Law 2.977 established official holidays for Chile
        # in its current form
        if year <= 1914:
            return None

        super()._populate(year)

        # New Year's Day (Law 2.977)
        self[date(year, JAN, 1)] = self.tr("Año Nuevo")
        # Day after, if it's a Sunday (Law 20.983)
        if year >= 2017 and self._is_sunday(date(year, JAN, 1)):
            self[date(year, JAN, 2)] = self.tr("Feriado nacional")

        # Holy Week (Law 2.977)
        easter_date = easter(year)
        self[easter_date + td(days=-2)] = self.tr("Viernes Santo")
        self[easter_date + td(days=-1)] = self.tr("Sábado Santo")

        # Ascension
        if year <= 1967:
            self[easter_date + td(days=+39)] = self.tr("Ascensión del Señor")

        # Corpus Christi
        if year <= 1967 or 1987 <= year <= 2006:
            # Law 19.668
            delta = +60 if year <= 1999 else +57
            self[easter_date + td(days=delta)] = self.tr("Corpus Christi")

        # Labour Day (Law 2.200, renamed with Law 18.018)
        if year >= 1932:
            self[date(year, MAY, 1)] = self.tr("Día Nacional del Trabajo")

        # Naval Glories Day (Law 2.977)
        self[date(year, MAY, 21)] = self.tr("Día de las Glorias Navales")

        # National Day of Indigenous Peoples
        name = self.tr("Día Nacional de los Pueblos Indígenas")
        if year == 2021:
            self[date(year, JUN, 21)] = name
        elif year >= 2022:
            epoch = Sun.get_equinox_solstice(year, target="summer")
            # Received date for UTC timezone needs to be adjusted
            # to match Chile's timezone
            # https://www.feriadoschilenos.cl/#DiaNacionalDeLosPueblosIndigenasII
            equinox = map(int, Epoch(epoch).get_full_date())
            adjusted_date = datetime(*equinox, tzinfo=timezone.utc).astimezone(
                ZoneInfo("America/Santiago")
            )
            self[date(year, JUN, adjusted_date.day)] = name

        # Saint Peter and Saint Paul (Law 16.840, Law 18.432)
        if year <= 1967 or year >= 1986:
            self[_get_movable(date(year, JUN, 29))] = self.tr(
                "San Pedro y San Pablo"
            )

        # Day of Virgin of Carmen (Law 20.148)
        if year >= 2007:
            self[date(year, JUL, 16)] = self.tr("Virgen del Carmen")

        # Day of Assumption of the Virgin (Law 2.977)
        self[date(year, AUG, 15)] = self.tr("Asunción de la Virgen")

        # Day of National Liberation (Law 18.026)
        if 1981 <= year <= 1998:
            self[date(year, SEP, 11)] = self.tr(
                "Día de la Liberación Nacional"
            )
        # Day of National Unity (Law 19.588, Law 19.793)
        elif 1999 <= year <= 2001:
            self[_get_nth_weekday_of_month(1, MON, SEP, year)] = self.tr(
                "Día de la Unidad Nacional"
            )

        # National Holiday Friday preceding Independence Day (Law 20.983)
        # Monday, September 17, 2007, is declared a holiday.
        if year >= 2017 and self._is_saturday(date(year, SEP, 18)):
            self[date(year, SEP, 17)] = self.tr("Fiestas Patrias")

        # National Holiday Monday preceding Independence Day (Law 20.215)
        if year >= 2007 and self._is_tuesday(date(year, SEP, 18)):
            self[date(year, SEP, 17)] = self.tr("Fiestas Patrias")

        # Independence Day (Law 2.977)
        self[date(year, SEP, 18)] = self.tr("Día de la Independencia")

        # Day of Glories of the Army of Chile (Law 2.977)
        self[date(year, SEP, 19)] = self.tr("Día de las Glorias del Ejército")

        # National Holiday Friday following Army Day (Law 20.215)
        if year >= 2008 and self._is_thursday(date(year, SEP, 19)):
            self[date(year, SEP, 20)] = self.tr("Fiestas Patrias")

        # Decree-law 636, Law 8.223
        if 1932 <= year <= 1944:
            self[date(year, SEP, 20)] = self.tr("Fiestas Patrias")

        # Columbus day (Law 3.810)
        if year >= 1922 and year != 1973:
            self[_get_movable(date(year, OCT, 12))] = (
                self.tr("Día del Encuentro de dos Mundos")
                if year >= 2000
                else self.tr("Día de la Raza")
            )

        # National Day of the Evangelical and Protestant Churches (Law 20.299)
        if year >= 2008:
            dt = date(year, OCT, 31)
            # This holiday is moved to the preceding Friday
            # if it falls on a Tuesday, or to the following Friday
            # if it falls on a Wednesday (Law 20.299)
            if self._is_wednesday(dt):
                dt += td(days=+2)
            elif self._is_tuesday(dt):
                dt += td(days=-4)
            self[dt] = self.tr(
                "Día Nacional de las Iglesias Evangélicas y Protestantes"
            )

        # All Saints Day (Law 2.977)
        self[date(year, NOV, 1)] = self.tr("Día de Todos los Santos")

        # Immaculate Conception (Law 2.977)
        self[date(year, DEC, 8)] = self.tr("La Inmaculada Concepción")

        if 1944 <= year <= 1988:
            self[date(year, DEC, 24)] = self.tr("Víspera de Navidad")

        # Christmas (Law 2.977)
        self[date(year, DEC, 25)] = self.tr("Navidad")

        # región de Arica y Parinacota
        if self.subdiv == "AP" and year >= 2013:
            # Law 20.663
            self[date(year, JUN, 7)] = self.tr(
                "Asalto y Toma del Morro de Arica"
            )

        # región de Ñuble
        if self.subdiv == "NB" and year >= 2014:
            # Law 20.678
            self[date(year, AUG, 20)] = self.tr(
                "Nacimiento del Prócer de la Independencia"
                " (Chillán y Chillán Viejo)"
            )


class CL(Chile):
    pass


class CHL(Chile):
    pass
