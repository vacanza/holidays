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

from datetime import date, datetime

from dateutil import tz
from dateutil.easter import easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd
from pymeeus.Epoch import Epoch
from pymeeus.Sun import Sun

from holidays.constants import JAN, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import TUE, WED, THU, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase


class Chile(HolidayBase):
    """
    https://www.feriados.cl
    http://www.feriadoschilenos.cl/ (excellent history)
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Chile
    """

    country = "CL"
    special_holidays = {
        2022: ((SEP, 16, "Feriado nacional [National Holiday]"),),
    }
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

        # Law 2.977 established official holidays for Chile
        # in its current form
        if year <= 1914:
            return
        super()._populate(year)

        # New Year's Day (Law 2.977)
        self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"
        # Day after, if it's a Sunday (Law 20.983)
        if year >= 2017 and date(year, JAN, 1).weekday() == SUN:
            self[date(year, JAN, 2)] = "Fiestas Patrias [Holiday]"

        # Holy Week (Law 2.977)
        easter_date = easter(year)
        self[
            easter_date + rd(days=-2)
        ] = "Semana Santa (Viernes Santo) [Good Friday)]"
        self[
            easter_date + rd(days=-1)
        ] = "Semana Santa (Sábado Santo) [Good Saturday)]"

        # Ascension
        if year <= 1967:
            self[
                easter_date + rd(days=+39)
            ] = "Ascensión del Señor [Ascension of Jesus]"

        # Corpus Christi
        if year <= 1967 or 1987 <= year <= 2006:
            # Law 19.668
            if year <= 1999:
                dt = easter_date + rd(days=+60)
            else:
                dt = easter_date + rd(days=+57)
            self[dt] = "Corpus Christi [Corpus Christi]"

        # Labour Day (Law 2.200, renamed with Law 18.018)
        if year >= 1932:
            self[date(year, MAY, 1)] = "Día Nacional del Trabajo [Labour Day]"

        # Naval Glories Day (Law 2.977)
        self[date(year, MAY, 21)] = "Día de las Glorias Navales [Navy Day]"

        # National Day of Indigenous Peoples
        name = (
            "Día Nacional de los Pueblos Indígenas "
            "[National Day of Indigenous Peoples]"
        )
        if year == 2021:
            self[date(year, JUN, 21)] = name
        elif year >= 2022:
            epoch = Sun.get_equinox_solstice(year, target="summer")
            # Received date for UTC timezone needs to be adjusted
            # to match Chile's timezone
            # https://www.feriadoschilenos.cl/#DiaNacionalDeLosPueblosIndigenasII
            equinox = map(int, Epoch(epoch).get_full_date())
            adjusted_date = datetime(*equinox, tzinfo=tz.UTC).astimezone(
                tz.gettz("America/Santiago")
            )
            self[date(year, JUN, adjusted_date.day)] = name

        # Saint Peter and Saint Paul (Law 16.840, Law 18.432)
        if year <= 1967 or year >= 1986:
            dt = date(year, JUN, 29)
            if year >= 2000:
                # floating Monday holiday (Law 19.668)
                if dt.weekday() < FRI:
                    dt += rd(weekday=MO(-1))
                elif dt.weekday() == FRI:
                    dt += rd(weekday=MO)
            self[dt] = "San Pedro y San Pablo [Saint Peter and Saint Paul]"

        # Day of Virgin of Carmen (Law 20.148)
        if year >= 2007:
            self[
                date(year, JUL, 16)
            ] = "Virgen del Carmen [Our Lady of Mount Carmel]"

        # Day of Assumption of the Virgin (Law 2.977)
        self[
            date(year, AUG, 15)
        ] = "Asunción de la Virgen [Assumption of Mary]"

        # Day of National Liberation (Law 18.026)
        if 1981 <= year <= 1998:
            self[
                date(year, SEP, 11)
            ] = "Día de la Liberación Nacional [Day of National Liberation]"
        # Day of National Unity (Law 19.588, Law 19.793)
        elif 1999 <= year <= 2001:
            self[
                date(year, SEP, 1) + rd(weekday=MO)
            ] = "Día de la Unidad Nacional [Day of National Unity]"

        # National Holiday Friday preceding Independence Day (Law 20.983)
        # Monday, September 17, 2007, is declared a holiday.
        if year >= 2017 and date(year, SEP, 18).weekday() == SAT:
            self[date(year, SEP, 17)] = "Fiestas Patrias [Holiday]"

        # National Holiday Monday preceding Independence Day (Law 20.215)
        if year >= 2007 and date(year, SEP, 18).weekday() == TUE:
            self[date(year, SEP, 17)] = "Fiestas Patrias [Holiday]"

        # Independence Day (Law 2.977)
        self[
            date(year, SEP, 18)
        ] = "Día de la Independencia [Independence Day]"

        # Day of Glories of the Army of Chile (Law 2.977)
        self[
            date(year, SEP, 19)
        ] = "Día de las Glorias del Ejército [Army Day]"

        # National Holiday Friday following Army Day (Law 20.215)
        if year >= 2008 and date(year, SEP, 19).weekday() == THU:
            self[date(year, SEP, 20)] = "Fiestas Patrias [Holiday]"

        # Decree-law 636, Law 8.223
        if 1932 <= year <= 1944:
            self[date(year, SEP, 20)] = "Fiestas Patrias [Holiday]"

        # Columbus day (Law 3.810)
        if year >= 1922 and year != 1973:
            dt = date(year, OCT, 12)
            name = "Día de la Raza [Columbus day]"
            if year >= 2000:
                # floating Monday holiday (Law 19.668)
                if dt.weekday() < FRI:
                    dt += rd(weekday=MO(-1))
                elif dt.weekday() == FRI:
                    dt += rd(weekday=MO)
                if year <= 2019:
                    # Day of the Meeting of Two Worlds (Law 3.810)
                    name = (
                        "Día del Respeto a la Diversidad "
                        "[Day of the Meeting of Two Worlds]"
                    )
                else:
                    name = (
                        "Día del Descubrimiento de dos Mundos "
                        "[Discovery of Two Worlds' Day]"
                    )
            self[dt] = name

        # National Day of the Evangelical and Protestant Churches (Law 20.299)
        if year >= 2008:
            dt = date(year, OCT, 31)
            # This holiday is moved to the preceding Friday
            # if it falls on a Tuesday, or to the following Friday
            # if it falls on a Wednesday (Law 20.299)
            if dt.weekday() == WED:
                dt += rd(days=+2)
            elif dt.weekday() == TUE:
                dt += rd(days=-4)
            self[dt] = (
                "Día Nacional de las Iglesias Evangélicas y Protestantes"
                " [Reformation Day]"
            )

        # All Saints Day (Law 2.977)
        self[date(year, NOV, 1)] = "Día de Todos los Santos [All Saints Day]"

        # Immaculate Conception (Law 2.977)
        self[
            date(year, DEC, 8)
        ] = "La Inmaculada Concepción [Immaculate Conception]"

        if 1944 <= year <= 1988:
            self[date(year, DEC, 24)] = "Víspera de Navidad [Christmas Eve]"

        # Christmas (Law 2.977)
        self[date(year, DEC, 25)] = "Navidad [Christmas]"

        # región de Arica y Parinacota
        if self.subdiv == "AP" and year >= 2013:
            # Law 20.663
            self[date(year, JUN, 7)] = (
                "Asalto y Toma del Morro de Arica"
                " [Assault and Capture of Cape Arica]"
            )

        # región de Ñuble
        if self.subdiv == "NB" and year >= 2014:
            # Law 20.678
            self[date(year, AUG, 20)] = (
                "Nacimiento del Prócer de la Independencia"
                " (Chillán y Chillán Viejo)"
                " [Nativity of Bernardo O'Higgins]"
            )


class CL(Chile):
    pass


class CHL(Chile):
    pass
