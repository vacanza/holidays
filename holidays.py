# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2018
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date, datetime
from dateutil.easter import easter, EASTER_ORTHODOX
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
import six

__version__ = '0.9.8'


MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)
WEEKEND = (SATURDAY, SUNDAY)


class HolidayBase(dict):
    PROVINCES = []

    def __init__(self, years=[], expand=True, observed=True,
                 prov=None, state=None):
        self.observed = observed
        self.expand = expand
        if isinstance(years, int):
            years = [years, ]
        self.years = set(years)
        if not getattr(self, 'prov', False):
            self.prov = prov
        self.state = state
        for year in list(self.years):
            self._populate(year)

    def __setattr__(self, key, value):
        if key == 'observed' and len(self) > 0:
            dict.__setattr__(self, key, value)
            if value is True:
                # Add (Observed) dates
                years = list(self.years)
                self.years = set()
                self.clear()
                for year in years:
                    self._populate(year)
            else:
                # Remove (Observed) dates
                for k, v in list(self.items()):
                    if v.find("Observed") >= 0:
                        del self[k]
        else:
            return dict.__setattr__(self, key, value)

    def __keytransform__(self, key):
        if isinstance(key, datetime):
            key = key.date()
        elif isinstance(key, date):
            key = key
        elif isinstance(key, int) or isinstance(key, float):
            key = datetime.utcfromtimestamp(key).date()
        elif isinstance(key, six.string_types):
            try:
                key = parse(key).date()
            except (ValueError, OverflowError):
                raise ValueError("Cannot parse date from string '%s'" % key)
        else:
            raise TypeError("Cannot convert type '%s' to date." % type(key))

        if self.expand and key.year not in self.years:
            self.years.add(key.year)
            self._populate(key.year)
        return key

    def __contains__(self, key):
        return dict.__contains__(self, self.__keytransform__(key))

    def __getitem__(self, key):
        return dict.__getitem__(self, self.__keytransform__(key))

    def __setitem__(self, key, value):
        if key in self:
            if self.get(key).find(value) < 0 \
                    and value.find(self.get(key)) < 0:
                value = "%s, %s" % (value, self.get(key))
            else:
                value = self.get(key)
        return dict.__setitem__(self, self.__keytransform__(key), value)

    def update(self, *args):
        args = list(args)
        for arg in args:
            if isinstance(arg, dict):
                for key, value in list(arg.items()):
                    self[key] = value
            elif isinstance(arg, list):
                for item in arg:
                    self[item] = "Holiday"
            else:
                self[arg] = "Holiday"

    def append(self, *args):
        return self.update(*args)

    def get(self, key, default=None):
        return dict.get(self, self.__keytransform__(key), default)

    def get_list(self, key):
        return [h for h in self.get(key, "").split(", ") if h]

    def pop(self, key, default=None):
        if default is None:
            return dict.pop(self, self.__keytransform__(key))
        return dict.pop(self, self.__keytransform__(key), default)

    def __eq__(self, other):
        return dict.__eq__(self, other) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return dict.__ne__(self, other) or self.__dict__ != other.__dict__

    def __add__(self, other):
        if isinstance(other, int) and other == 0:
            # Required to sum() list of holidays
            # sum([h1, h2]) is equivalent to (0 + h1 + h2)
            return self
        elif not isinstance(other, HolidayBase):
            raise TypeError()
        HolidaySum = createHolidaySum(self, other)
        country = (getattr(self, 'country', None) or
                   getattr(other, 'country', None))
        if self.country and other.country and self.country != other.country:
            c1 = self.country
            if not isinstance(c1, list):
                c1 = [c1]
            c2 = other.country
            if not isinstance(c2, list):
                c2 = [c2]
            country = c1 + c2
        prov = getattr(self, 'prov', None) or getattr(other, 'prov', None)
        if self.prov and other.prov and self.prov != other.prov:
            p1 = self.prov if isinstance(self.prov, list) else [self.prov]
            p2 = other.prov if isinstance(other.prov, list) else [other.prov]
            prov = p1 + p2
        return HolidaySum(years=(self.years | other.years),
                          expand=(self.expand or other.expand),
                          observed=(self.observed or other.observed),
                          country=country, prov=prov)

    def __radd__(self, other):
        return self.__add__(other)

    def _populate(self, year):
        pass


def createHolidaySum(h1, h2):

    class HolidaySum(HolidayBase):

        def __init__(self, country, **kwargs):
            self.country = country
            self.holidays = []
            if getattr(h1, 'holidays', False):
                for h in h1.holidays:
                    self.holidays.append(h)
            else:
                self.holidays.append(h1)
            if getattr(h2, 'holidays', False):
                for h in h2.holidays:
                    self.holidays.append(h)
            else:
                self.holidays.append(h2)
            HolidayBase.__init__(self, **kwargs)

        def _populate(self, year):
            for h in self.holidays[::-1]:
                h._populate(year)
                self.update(h)

    return HolidaySum


def CountryHoliday(country, prov=None, state=None):
    try:
        country_holiday = globals()[country](prov=prov, state=state)
    except (KeyError):
        raise KeyError("Country %s not available" % country)
    return country_holiday


class Argentina(HolidayBase):
    # https://www.argentina.gob.ar/interior/feriados
    # https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Argentina
    # http://servicios.lanacion.com.ar/feriados
    # https://www.clarin.com/feriados/

    def __init__(self, **kwargs):
        self.country = 'AR'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if not self.observed and date(year, 1, 1).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 1, 1)] = "Año Nuevo [New Year's Day]"

        # Carnival days
        name = "Día de Carnaval [Carnival's Day]"
        self[easter(year) - rd(days=48)] = name
        self[easter(year) - rd(days=47)] = name

        # Memory's National Day for the Truth and Justice
        name = "Día Nacional de la Memoria por la Verdad y la Justicia " \
               "[Memory's National Day for the Truth and Justice]"

        if not self.observed and date(year, 3, 24).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 3, 24)] = name

        # Holy Week
        name_thu = "Semana Santa (Jueves Santo)  [Holy day (Holy Thursday)]"
        name_fri = "Semana Santa (Viernes Santo)  [Holy day (Holy Friday)]"
        name_easter = 'Día de Pascuas [Easter Day]'

        self[easter(year) + rd(weekday=TH(-1))] = name_thu
        self[easter(year) + rd(weekday=FR(-1))] = name_fri

        if not self.observed and easter(year).weekday() in WEEKEND:
            pass
        else:
            self[easter(year)] = name_easter

        # Veterans Day and the Fallen in the Malvinas War
        if not self.observed and date(year, 4, 2).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 4, 2)] = "Día del Veterano y de los Caidos " \
                                     "en la Guerra de Malvinas [Veterans Day" \
                                     "and the Fallen in the Malvinas War]"

        # Labor Day
        name = "Día del Trabajo [Labour Day]"
        if not self.observed and date(year, 5, 1).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 5, 1)] = name

        # May Revolution Day
        name = "Día de la Revolucion de Mayo [May Revolution Day]"
        if not self.observed and date(year, 5, 25).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 5, 25)] = name

        # Day Pass to the Immortality of General Martín Miguel de Güemes.
        name = "Día Pase a la Inmortalidad " \
               "del General Martín Miguel de Güemes [Day Pass " \
               "to the Immortality of General Martín Miguel de Güemes]"
        if not self.observed and date(year, 6, 17).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 6, 17)] = name

        # Day Pass to the Immortality of General D. Manuel Belgrano.
        name = "Día Pase a la Inmortalidad " \
               "del General D. Manuel Belgrano [Day Pass " \
               "to the Immortality of General D. Manuel Belgrano]"
        if not self.observed and date(year, 6, 20).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 6, 20)] = name

        # Independence Day
        name = "Día de la Independencia [Independence Day]"
        if not self.observed and date(year, 7, 9).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 7, 9)] = name

        # Day Pass to the Immortality of General D. José de San Martin
        name = "Día Pase a la Inmortalidad " \
               "del General D. José de San Martin [Day Pass " \
               "to the Immortality of General D. José de San Martin]"
        if not self.observed and date(year, 8, 17).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 8, 17)] = name

        # Respect for Cultural Diversity Day or Columbus day
        if not self.observed and date(year, 10, 12).weekday() in WEEKEND:
            pass
        elif year < 2010:
            self[date(year, 10, 12)] = "Día de la Raza [Columbus day]"
        else:
            self[date(year, 10, 12)] = "Día del Respeto a la Diversidad" \
                                       " Cultural [Respect for Cultural " \
                                       "Diversity Day]"
        # National Sovereignty Day
        name = "Día Nacional de la Soberanía [National Sovereignty Day]"
        if not self.observed and date(year, 11, 20).weekday() in WEEKEND:
            pass
        elif year >= 2010:
            self[date(year, 11, 20)] = name

        # Immaculate Conception
        if not self.observed and date(year, 12, 8).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 12, 8)
                 ] = "La Inmaculada Concepción [Immaculate Conception]"

        # Christmas
        self[date(year, 12, 25)] = "Navidad [Christmas]"


class AR(Argentina):
    pass


class Belarus(HolidayBase):
    """
    http://president.gov.by/en/holidays_en/
    http://www.belarus.by/en/about-belarus/national-holidays
    """
    def __init__(self, **kwargs):
        self.country = "BY"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # The current set of holidays came into force in 1998
        # http://laws.newsby.org/documents/ukazp/pos05/ukaz05806.htm
        if year <= 1998:
            return

        # New Year's Day
        self[date(year, 1, 1)] = "Новый год"

        # Christmas Day (Orthodox)
        self[date(year, 1, 7)] = "Рождество Христово " \
                                 "(православное Рождество)"

        # Women's Day
        self[date(year, 3, 8)] = "День женщин"

        # Radunitsa ("Day of Rejoicing")
        self[easter(year, method=EASTER_ORTHODOX) + rd(days=9)] = "Радуница"

        # Labour Day
        self[date(year, 5, 1)] = "Праздник труда"

        # Victory Day
        self[date(year, 5, 9)] = "День Победы"

        # Independence Day
        self[date(year, 7, 3)] = "День Независимости Республики Беларусь " \
                                 "(День Республики)"

        # October Revolution Day
        self[date(year, 11, 7)] = "День Октябрьской революции"

        # Christmas Day (Catholic)
        self[date(year, 12, 25)] = "Рождество Христово " \
                                   "(католическое Рождество)"


class BY(Belarus):
    pass


class Brazil(HolidayBase):
    """
    https://pt.wikipedia.org/wiki/Feriados_no_Brasil
    """

    STATES = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT',
              'MS', 'MG', 'PA', 'PB', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR',
              'SC', 'SP', 'SE', 'TO']

    def __init__(self, **kwargs):
        self.country = 'BR'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, 1, 1)] = "Ano novo"

        self[date(year, 4, 21)] = "Tiradentes"

        self[date(year, 5, 1)] = "Dia Mundial do Trabalho"

        self[date(year, 9, 7)] = "Independência do Brasil"

        self[date(year, 10, 12)] = "Nossa Senhora Aparecida"

        self[date(year, 11, 2)] = "Finados"

        self[date(year, 11, 15)] = "Proclamação da República"

        # Christmas Day
        self[date(year, 12, 25)] = "Natal"

        self[easter(year)] = "Páscoa"

        self[easter(year) + rd(days=60)] = "Corpus Christi"

        quaresma = easter(year) - rd(days=46)
        self[quaresma] = "Quarta-feira de cinzas (Início da Quaresma)"

        self[quaresma - rd(weekday=TU)] = "Carnaval"

        if self.state == 'AC':
            self[date(year, 1, 23)] = "Dia do evangélico"
            self[date(year, 6, 15)] = "Aniversário do Acre"
            self[date(year, 9, 5)] = "Dia da Amazônia"
            self[date(year, 11, 17)] = "Assinatura do Tratado de Petrópolis"

        if self.state == 'AL':
            self[date(year, 6, 24)] = "São João"
            self[date(year, 6, 29)] = "São Pedro"
            self[date(year, 9, 16)] = "Emancipação política de Alagoas"
            self[date(year, 11, 20)] = "Consciência Negra"

        if self.state == 'AP':
            self[date(year, 3, 19)] = "Dia de São José"
            self[date(year, 7, 25)] = "São Tiago"
            self[date(year, 10, 5)] = "Criação do estado"
            self[date(year, 11, 20)] = "Consciência Negra"

        if self.state == 'AM':
            self[date(year, 9, 5)] = "Elevação do Amazonas" \
                " à categoria de província"
            self[date(year, 11, 20)] = "Consciência Negra"
            self[date(year, 12, 8)] = "Dia de Nossa Senhora da Conceição"

        if self.state == 'BA':
            self[date(year, 7, 2)] = "Independência da Bahia"

        if self.state == 'CE':
            self[date(year, 3, 19)] = "São José"
            self[date(year, 3, 25)] = "Data Magna do Ceará"

        if self.state == 'DF':
            self[date(year, 4, 21)] = "Fundação de Brasília"
            self[date(year, 11, 30)] = "Dia do Evangélico"

        if self.state == 'ES':
            self[date(year, 10, 28)] = "Dia do Servidor Público"

        if self.state == 'GO':
            self[date(year, 10, 28)] = "Dia do Servidor Público"

        if self.state == 'MA':
            self[date(year, 7, 28)] = "Adesão do Maranhão" \
                " à independência do Brasil"
            self[date(year, 12, 8)] = "Dia de Nossa Senhora da Conceição"

        if self.state == 'MT':
            self[date(year, 11, 20)] = "Consciência Negra"

        if self.state == 'MS':
            self[date(year, 10, 11)] = "Criação do estado"

        if self.state == 'MG':
            self[date(year, 4, 21)] = "Data Magna de MG"

        if self.state == 'PA':
            self[date(year, 8, 15)] = "Adesão do Grão-Pará" \
                " à independência do Brasil"

        if self.state == 'PB':
            self[date(year, 8, 5)] = "Fundação do Estado"

        if self.state == 'PE':
            self[date(year, 3, 6)] = "Revolução Pernambucana (Data Magna)"
            self[date(year, 6, 24)] = "São João"

        if self.state == 'PI':
            self[date(year, 3, 13)] = "Dia da Batalha do Jenipapo"
            self[date(year, 10, 19)] = "Dia do Piauí"

        if self.state == 'RJ':
            self[date(year, 4, 23)] = "Dia de São Jorge"
            self[date(year, 10, 28)] = "Dia do Funcionário Público"
            self[date(year, 11, 20)] = "Zumbi dos Palmares"

        if self.state == 'RN':
            self[date(year, 6, 29)] = "Dia de São Pedro"
            self[date(year, 10, 3)] = "Mártires de Cunhaú e Uruaçuu"

        if self.state == 'RS':
            self[date(year, 9, 20)] = "Revolução Farroupilha"

        if self.state == 'RO':
            self[date(year, 1, 4)] = "Criação do estado"
            self[date(year, 6, 18)] = "Dia do Evangélico"

        if self.state == 'RR':
            self[date(year, 10, 5)] = "Criação de Roraima"

        if self.state == 'SC':
            self[date(year, 8, 11)] = "Criação da capitania," \
                " separando-se de SP"

        if self.state == 'SP':
            self[date(year, 7, 9)] = "Revolução Constitucionalista de 1932"

        if self.state == 'SE':
            self[date(year, 7, 8)] = "Autonomia política de Sergipe"

        if self.state == 'TO':
            self[date(year, 1, 1)] = "Instalação de Tocantins"
            self[date(year, 9, 8)] = "Nossa Senhora da Natividade"
            self[date(year, 10, 5)] = "Criação de Tocantins"


class BR(Brazil):
    pass


class Canada(HolidayBase):

    PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE',
                 'QC', 'SK', 'YU']

    def __init__(self, **kwargs):
        self.country = 'CA'
        self.prov = kwargs.pop('prov', 'ON')
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year >= 1867:
            name = "New Year's Day"
            self[date(year, 1, 1)] = name
            if self.observed and date(year, 1, 1).weekday() == 6:
                self[date(year, 1, 1) + rd(days=+1)] = name + " (Observed)"
            elif self.observed and date(year, 1, 1).weekday() == 5:
                # Add Dec 31st from the previous year without triggering
                # the entire year to be added
                expand = self.expand
                self.expand = False
                self[date(year, 1, 1) + rd(days=-1)] = name + " (Observed)"
                self.expand = expand
            # The next year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday)
            if self.observed and date(year, 12, 31).weekday() == 4:
                self[date(year, 12, 31)] = name + " (Observed)"

        # Family Day / Louis Riel Day (MB) / Islander Day (PE)
        # / Heritage Day (NS, YU)
        if self.prov in ('AB', 'SK', 'ON') and year >= 2008:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov in ('AB', 'SK') and year >= 2007:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov == 'AB' and year >= 1990:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov == 'BC':
            if year >= 2013 and year <= 2018:
                self[date(year, 2, 1) + rd(weekday=MO(+2))] = "Family Day"
            elif year > 2018:
                self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov == 'MB' and year >= 2008:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Louis Riel Day"
        elif self.prov == 'PE' and year >= 2010:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Islander Day"
        elif self.prov == 'PE' and year == 2009:
            self[date(year, 2, 1) + rd(weekday=MO(+2))] = "Islander Day"
        elif self.prov in 'NS' and year >= 2015:
            # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Heritage Day"
        elif self.prov in 'YU':
            # start date?
            # http://heritageyukon.ca/programs/heritage-day
            # https://en.wikipedia.org/wiki/Family_Day_(Canada)#Yukon_Heritage_Day
            # Friday before the last Sunday in February
            dt = date(year, 3, 1) + rd(weekday=SU(-1)) + rd(weekday=FR(-1))
            self[dt] = "Heritage Day"

        # St. Patrick's Day
        if self.prov == 'NL' and year >= 1900:
            dt = date(year, 3, 17)
            # Nearest Monday to March 17
            dt1 = date(year, 3, 17) + rd(weekday=MO(-1))
            dt2 = date(year, 3, 17) + rd(weekday=MO(+1))
            if dt2 - dt <= dt - dt1:
                self[dt2] = "St. Patrick's Day"
            else:
                self[dt1] = "St. Patrick's Day"

        # Good Friday
        if self.prov != 'QC' and year >= 1867:
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if self.prov == 'QC' and year >= 1867:
            self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # St. George's Day
        if self.prov == 'NL' and year == 2010:
            # 4/26 is the Monday closer to 4/23 in 2010
            # but the holiday was observed on 4/19? Crazy Newfies!
            self[date(2010, 4, 19)] = "St. George's Day"
        elif self.prov == 'NL' and year >= 1990:
            dt = date(year, 4, 23)
            # Nearest Monday to April 23
            dt1 = dt + rd(weekday=MO(-1))
            dt2 = dt + rd(weekday=MO(+1))
            if dt2 - dt < dt - dt1:
                self[dt2] = "St. George's Day"
            else:
                self[dt1] = "St. George's Day"

        # Victoria Day / National Patriots' Day (QC)
        if self.prov not in ('NB', 'NS', 'PE', 'NL', 'QC') and year >= 1953:
            self[date(year, 5, 24) + rd(weekday=MO(-1))] = "Victoria Day"
        elif self.prov == 'QC' and year >= 1953:
            name = "National Patriots' Day"
            self[date(year, 5, 24) + rd(weekday=MO(-1))] = name

        # National Aboriginal Day
        if self.prov == 'NT' and year >= 1996:
            self[date(year, 6, 21)] = "National Aboriginal Day"

        # St. Jean Baptiste Day
        if self.prov == 'QC' and year >= 1925:
            self[date(year, 6, 24)] = "St. Jean Baptiste Day"
            if self.observed and date(year, 6, 24).weekday() == 6:
                self[date(year, 6, 25)] = "St. Jean Baptiste Day (Observed)"

        # Discovery Day
        if self.prov == 'NL' and year >= 1997:
            dt = date(year, 6, 24)
            # Nearest Monday to June 24
            dt1 = dt + rd(weekday=MO(-1))
            dt2 = dt + rd(weekday=MO(+1))
            if dt2 - dt <= dt - dt1:
                self[dt2] = "Discovery Day"
            else:
                self[dt1] = "Discovery Day"
        elif self.prov == 'YU' and year >= 1912:
            self[date(year, 8, 1) + rd(weekday=MO(+3))] = "Discovery Day"

        # Canada Day / Memorial Day (NL)
        if self.prov != 'NL' and year >= 1867:
            if year >= 1983:
                name = "Canada Day"
            else:
                name = "Dominion Day"
            self[date(year, 7, 1)] = name
            if year >= 1879 and self.observed \
                    and date(year, 7, 1).weekday() in (5, 6):
                self[date(year, 7, 1) + rd(weekday=MO)] = name + " (Observed)"
        elif year >= 1867:
            if year >= 1983:
                name = "Memorial Day"
            else:
                name = "Dominion Day"
            self[date(year, 7, 1)] = name
            if year >= 1879 and self.observed \
                    and date(year, 7, 1).weekday() in (5, 6):
                self[date(year, 7, 1) + rd(weekday=MO)] = name + " (Observed)"

        # Nunavut Day
        if self.prov == 'NU' and year >= 2001:
            self[date(year, 7, 9)] = "Nunavut Day"
            if self.observed and date(year, 7, 9).weekday() == 6:
                self[date(year, 7, 10)] = "Nunavut Day (Observed)"
        elif self.prov == 'NU' and year == 2000:
            self[date(2000, 4, 1)] = "Nunavut Day"

        # Civic Holiday
        if self.prov in ('ON', 'MB', 'NT') and year >= 1900:
            self[date(year, 8, 1) + rd(weekday=MO)] = "Civic Holiday"
        elif self.prov in 'AB' and year >= 1974:
            # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
            self[date(year, 8, 1) + rd(weekday=MO)] = "Heritage Day"
        elif self.prov in 'BC' and year >= 1974:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, 8, 1) + rd(weekday=MO)] = "British Columbia Day"
        elif self.prov in 'NB' and year >= 1900:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, 8, 1) + rd(weekday=MO)] = "New Brunswick Day"
        elif self.prov in 'SK' and year >= 1900:
            # https://en.wikipedia.org/wiki/Civic_Holiday
            self[date(year, 8, 1) + rd(weekday=MO)] = "Saskatchewan Day"

        # Labour Day
        if year >= 1894:
            self[date(year, 9, 1) + rd(weekday=MO)] = "Labour Day"

        # Thanksgiving
        if self.prov not in ('NB', 'NS', 'PE', 'NL') and year >= 1931:
            if year == 1935:
                # in 1935, Canadian Thanksgiving was moved due to the General
                # Election falling on the second Monday of October
                # https://books.google.ca/books?id=KcwlQsmheG4C&pg=RA1-PA1940&lpg=RA1-PA1940&dq=canada+thanksgiving+1935&source=bl&ots=j4qYrcfGuY&sig=gxXeAQfXVsOF9fOwjSMswPHJPpM&hl=en&sa=X&ved=0ahUKEwjO0f3J2PjOAhVS4mMKHRzKBLAQ6AEIRDAG#v=onepage&q=canada%20thanksgiving%201935&f=false
                self[date(1935, 10, 25)] = "Thanksgiving"
            else:
                self[date(year, 10, 1) + rd(weekday=MO(+2))] = "Thanksgiving"

        # Remembrance Day
        name = "Remembrance Day"
        provinces = ('ON', 'QC', 'NS', 'NL', 'NT', 'PE', 'SK')
        if self.prov not in provinces and year >= 1931:
            self[date(year, 11, 11)] = name
        elif self.prov in ('NS', 'NL', 'NT', 'PE', 'SK') and year >= 1931:
            self[date(year, 11, 11)] = name
            if self.observed and date(year, 11, 11).weekday() == 6:
                name = name + " (Observed)"
                self[date(year, 11, 11) + rd(weekday=MO)] = name

        # Christmas Day
        if year >= 1867:
            self[date(year, 12, 25)] = "Christmas Day"
            if self.observed and date(year, 12, 25).weekday() == 5:
                self[date(year, 12, 24)] = "Christmas Day (Observed)"
            elif self.observed and date(year, 12, 25).weekday() == 6:
                self[date(year, 12, 26)] = "Christmas Day (Observed)"

        # Boxing Day
        if year >= 1867:
            name = "Boxing Day"
            name_observed = name + " (Observed)"
            if self.observed and date(year, 12, 26).weekday() in (5, 6):
                self[date(year, 12, 26) + rd(weekday=MO)] = name_observed
            elif self.observed and date(year, 12, 26).weekday() == 0:
                self[date(year, 12, 27)] = name_observed
            else:
                self[date(year, 12, 26)] = name


class CA(Canada):
    pass


class Colombia(HolidayBase):
    # https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_Colombia

    def __init__(self, **kwargs):
        self.country = 'CO'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # Fixed date holidays!
        # If observed=True and they fall on a weekend they are not observed.
        # If observed=False there are 18 holidays

        # New Year's Day
        if self.observed and date(year, 1, 1).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 1, 1)] = "Año Nuevo [New Year's Day]"

        # Labor Day
        self[date(year, 5, 1)] = "Día del Trabajo [Labour Day]"

        # Independence Day
        name = "Día de la Independencia [Independence Day]"
        if self.observed and date(year, 7, 20).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 7, 20)] = name

        # Battle of Boyaca
        self[date(year, 8, 7)] = "Batalla de Boyacá [Battle of Boyacá]"

        # Immaculate Conception
        if self.observed and date(year, 12, 8).weekday() in WEEKEND:
            pass
        else:
            self[date(year, 12, 8)
                 ] = "La Inmaculada Concepción [Immaculate Conception]"

        # Christmas
        self[date(year, 12, 25)] = "Navidad [Christmas]"

        # Emiliani Law holidays!
        # Unless they fall on a Monday they are observed the following monday

        #  Epiphany
        name = "Día de los Reyes Magos [Epiphany]"
        if date(year, 1, 6).weekday() == 0 or not self.observed:
            self[date(year, 1, 6)] = name
        else:
            self[date(year, 1, 6) + rd(weekday=MO)] = name + "(Observed)"

        # Saint Joseph's Day
        name = "Día de San José [Saint Joseph's Day]"
        if date(year, 3, 19).weekday() == 0 or not self.observed:
            self[date(year, 3, 19)] = name
        else:
            self[date(year, 3, 19) + rd(weekday=MO)] = name + "(Observed)"

        # Saint Peter and Saint Paul's Day
        name = "San Pedro y San Pablo [Saint Peter and Saint Paul]"
        if date(year, 6, 29).weekday() == 0 or not self.observed:
            self[date(year, 6, 29)] = name
        else:
            self[date(year, 6, 29) + rd(weekday=MO)] = name + "(Observed)"

        # Assumption of Mary
        name = "La Asunción [Assumption of Mary]"
        if date(year, 8, 15).weekday() == 0 or not self.observed:
            self[date(year, 8, 15)] = name
        else:
            self[date(year, 8, 15) + rd(weekday=MO)] = name + "(Observed)"

        # Discovery of America
        name = "Descubrimiento de América [Discovery of America]"
        if date(year, 10, 12).weekday() == 0 or not self.observed:
            self[date(year, 10, 12)] = name
        else:
            self[date(year, 10, 12) + rd(weekday=MO)] = name + "(Observed)"

        # All Saints’ Day
        name = "Dia de Todos los Santos [All Saint's Day]"
        if date(year, 11, 1).weekday() == 0 or not self.observed:
            self[date(year, 11, 1)] = name
        else:
            self[date(year, 11, 1) + rd(weekday=MO)] = name + "(Observed)"

        # Independence of Cartagena
        name = "Independencia de Cartagena [Independence of Cartagena]"
        if date(year, 11, 11).weekday() == 0 or not self.observed:
            self[date(year, 11, 11)] = name
        else:
            self[date(year, 11, 11) + rd(weekday=MO)] = name + "(Observed)"

        # Holidays based on Easter

        # Maundy Thursday
        self[easter(year) + rd(weekday=TH(-1))
             ] = "Jueves Santo [Maundy Thursday]"

        # Good Friday
        self[easter(year) + rd(weekday=FR(-1))
             ] = "Viernes Santo [Good Friday]"

        # Holidays based on Easter but are observed the following monday
        # (unless they occur on a monday)

        # Ascension of Jesus
        name = "Ascensión del señor [Ascension of Jesus]"
        hdate = easter(year) + rd(days=+39)
        if hdate.weekday() == 0 or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name + "(Observed)"

        # Corpus Christi
        name = "Corpus Christi [Corpus Christi]"
        hdate = easter(year) + rd(days=+60)
        if hdate.weekday() == 0 or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name + "(Observed)"

        # Sacred Heart
        name = "Sagrado Corazón [Sacred Heart]"
        hdate = easter(year) + rd(days=+68)
        if hdate.weekday() == 0 or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name + "(Observed)"


class CO(Colombia):
    pass


class Mexico(HolidayBase):

    def __init__(self, **kwargs):
        self.country = 'MX'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        name = "Año Nuevo [New Year's Day]"
        self[date(year, 1, 1)] = name
        if self.observed and date(year, 1, 1).weekday() == 6:
            self[date(year, 1, 1) + rd(days=+1)] = name + " (Observed)"
        elif self.observed and date(year, 1, 1).weekday() == 5:
            # Add Dec 31st from the previous year without triggering
            # the entire year to be added
            expand = self.expand
            self.expand = False
            self[date(year, 1, 1) + rd(days=-1)] = name + " (Observed)"
            self.expand = expand
        # The next year's observed New Year's Day can be in this year
        # when it falls on a Friday (Jan 1st is a Saturday)
        if self.observed and date(year, 12, 31).weekday() == 4:
            self[date(year, 12, 31)] = name + " (Observed)"

        # Constitution Day
        name = "Día de la Constitución [Constitution Day]"
        if 2006 >= year >= 1917:
            self[date(year, 2, 5)] = name
        elif year >= 2007:
            self[date(year, 2, 1) + rd(weekday=MO(+1))] = name

        # Benito Juárez's birthday
        name = "Natalicio de Benito Juárez [Benito Juárez's birthday]"
        if 2006 >= year >= 1917:
            self[date(year, 3, 21)] = name
        elif year >= 2007:
            self[date(year, 3, 1) + rd(weekday=MO(+3))] = name

        # Labor Day
        if year >= 1923:
            self[date(year, 5, 1)] = "Día del Trabajo [Labour Day]"
            if self.observed and date(year, 5, 1).weekday() == 5:
                self[date(year, 5, 1) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 5, 1).weekday() == 6:
                self[date(year, 5, 1) + rd(days=+1)] = name + " (Observed)"

        # Independence Day
        name = "Día de la Independencia [Independence Day]"
        self[date(year, 9, 16)] = name
        if self.observed and date(year, 9, 16).weekday() == 5:
            self[date(year, 9, 16) + rd(days=-1)] = name + " (Observed)"
        elif self.observed and date(year, 9, 16).weekday() == 6:
            self[date(year, 9, 16) + rd(days=+1)] = name + " (Observed)"

        # Revolution Day
        name = "Día de la Revolución [Revolution Day]"
        if 2006 >= year >= 1917:
            self[date(year, 11, 20)] = name
        elif year >= 2007:
            self[date(year, 11, 1) + rd(weekday=MO(+3))] = name

        # Change of Federal Government
        # Every six years--next observance 2018
        name = "Transmisión del Poder Ejecutivo Federal"
        name += " [Change of Federal Government]"
        if (2018 - year) % 6 == 0:
            self[date(year, 12, 1)] = name
            if self.observed and date(year, 12, 1).weekday() == 5:
                self[date(year, 12, 1) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 12, 1).weekday() == 6:
                self[date(year, 12, 1) + rd(days=+1)] = name + " (Observed)"

        # Christmas
        self[date(year, 12, 25)] = "Navidad [Christmas]"
        if self.observed and date(year, 12, 25).weekday() == 5:
            self[date(year, 12, 25) + rd(days=-1)] = name + " (Observed)"
        elif self.observed and date(year, 12, 25).weekday() == 6:
            self[date(year, 12, 25) + rd(days=+1)] = name + " (Observed)"


class MX(Mexico):
    pass


class Ukraine(HolidayBase):
    """
    http://zakon1.rada.gov.ua/laws/show/322-08/paran454#n454
    """
    def __init__(self, **kwargs):
        self.country = "UA"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # The current set of holidays came into force in 1991
        # But most holiday days was inplemented in 1981
        if year < 1918:
            return

        # New Year's Day
        if year >= 1898:
            self[date(year, 1, 1)] = "Новий рік"

        # Christmas Day (Orthodox)
        if year >= 1991:
            self[date(year, 1, 7)] = "Різдво Христове" \
                                     " (православне)"

        # Women's Day
        if year > 1965:
            self[date(year, 3, 8)] = "Міжнародний жіночий день"

        # Easter
        if year >= 1991:
            self[easter(year, method=EASTER_ORTHODOX)] = "Пасха" \
                                                         " (Великдень)"

        # Holy trinity
        if year >= 1991:
            self[easter(year, method=EASTER_ORTHODOX) + rd(days=49)] = "Трійця"

        # Labour Day
        if year > 2017:
            name = "День праці"
        elif 1917 < year <= 2017:
            name = "День міжнародної солідарності трудящих"
        self[date(year, 5, 1)] = name

        # Labour Day in past
        if 1928 < year < 2018:
            self[date(year, 5, 2)] = "День міжнародної солідарності трудящих"

        # Victory Day
        name = "День перемоги"
        if year >= 1965:
            self[date(year, 5, 9)] = name
        if 1945 <= year < 1947:
            self[date(year, 5, 9)] = name
            self[date(year, 9, 3)] = "День перемоги над Японією"

        # Constitution Day
        if year >= 1997:
            self[date(year, 6, 28)] = "День Конституції України"

        # Independence Day
        name = "День незалежності України"
        if year > 1991:
            self[date(year, 8, 24)] = name
        elif year == 1991:
            self[date(year, 7, 16)] = name

        # Day of the defender of Ukraine
        if year >= 2015:
            self[date(year, 10, 14)] = "День захисника України"

        # USSR Constitution day
        name = "День Конституції СРСР"
        if 1981 <= year < 1991:
            self[date(year, 10, 7)] = name
        elif 1937 <= year < 1981:
            self[date(year, 12, 5)] = name

        # October Revolution
        if 1917 < year < 2000:
            if year <= 1991:
                name = "Річниця Великої Жовтневої" \
                       " соціалістичної революції"
            else:
                name = "Річниця жовтневого перевороту"
            self[date(year, 11, 7)] = name
            self[date(year, 11, 8)] = name

        # Christmas Day (Catholic)
        if year >= 2017:
            self[date(year, 12, 25)] = "Різдво Христове" \
                                       " (католицьке)"
        # USSR holidays
        # Bloody_Sunday_(1905)
        if 1917 <= year < 1951:
            self[date(year, 1, 22)] = "День пам'яті 9 січня 1905 року"

        # Paris_Commune
        if 1917 < year < 1929:
            self[date(year, 3, 18)] = "День паризької комуни"


class UA(Ukraine):
    pass


class UnitedStates(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States

    STATES = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
              'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
              'MD', 'MH', 'MA', 'MI', 'FM', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV',
              'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW',
              'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'VI',
              'WA', 'WV', 'WI', 'WY']

    def __init__(self, **kwargs):
        self.country = 'US'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        if year > 1870:
            name = "New Year's Day"
            self[date(year, 1, 1)] = name
            if self.observed and date(year, 1, 1).weekday() == 6:
                self[date(year, 1, 1) + rd(days=+1)] = name + " (Observed)"
            elif self.observed and date(year, 1, 1).weekday() == 5:
                # Add Dec 31st from the previous year without triggering
                # the entire year to be added
                expand = self.expand
                self.expand = False
                self[date(year, 1, 1) + rd(days=-1)] = name + " (Observed)"
                self.expand = expand
            # The next year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday)
            if self.observed and date(year, 12, 31).weekday() == 4:
                self[date(year, 12, 31)] = name + " (Observed)"

        # Epiphany
        if self.state == 'PR':
            self[date(year, 1, 6)] = "Epiphany"

        # Three King's Day
        if self.state == 'VI':
            self[date(year, 1, 6)] = "Three King's Day"

        # Lee Jackson Day
        name = "Lee Jackson Day"
        if self.state == 'VA' and year >= 2000:
            dt = date(year, 1, 1) + rd(weekday=MO(+3)) + rd(weekday=FR(-1))
            self[dt] = name
        elif self.state == 'VA' and year >= 1983:
            self[date(year, 1, 1) + rd(weekday=MO(+3))] = name
        elif self.state == 'VA' and year >= 1889:
            self[date(year, 1, 19)] = name

        # Inauguration Day
        if self.state in ('DC', 'LA', 'MD', 'VA') and year >= 1789:
            name = "Inauguration Day"
            if (year - 1789) % 4 == 0 and year >= 1937:
                self[date(year, 1, 20)] = name
                if date(year, 1, 20).weekday() == 6:
                    self[date(year, 1, 21)] = name + " (Observed)"
            elif (year - 1789) % 4 == 0:
                self[date(year, 3, 4)] = name
                if date(year, 3, 4).weekday() == 6:
                    self[date(year, 3, 5)] = name + " (Observed)"

        # Martin Luther King, Jr. Day
        if year >= 1986:
            name = "Martin Luther King, Jr. Day"
            if self.state == 'AL':
                name = "Robert E. Lee/Martin Luther King Birthday"
            elif self.state in ('AS', 'MS'):
                name = ("Dr. Martin Luther King Jr. "
                        "and Robert E. Lee's Birthdays")
            elif self.state in ('AZ', 'NH'):
                name = "Dr. Martin Luther King Jr./Civil Rights Day"
            elif self.state == 'GA' and year < 2012:
                name = "Robert E. Lee's Birthday"
            elif self.state == 'ID' and year >= 2006:
                name = "Martin Luther King, Jr. - Idaho Human Rights Day"
            self[date(year, 1, 1) + rd(weekday=MO(+3))] = name

        # Lincoln's Birthday
        name = "Lincoln's Birthday"
        if (self.state in ('CT', 'IL', 'IA', 'NJ', 'NY') and year >= 1971) \
                or (self.state == 'CA' and 1971 <= year <= 2009):
            self[date(year, 2, 12)] = name
            if self.observed and date(year, 2, 12).weekday() == 5:
                self[date(year, 2, 11)] = name + " (Observed)"
            elif self.observed and date(year, 2, 12).weekday() == 6:
                self[date(year, 2, 13)] = name + " (Observed)"

        # Susan B. Anthony Day
        if (self.state == 'CA' and year >= 2014) \
                or (self.state == 'FL' and year >= 2011) \
                or (self.state == 'NY' and year >= 2004) \
                or (self.state == 'WI' and year >= 1976):
            self[date(year, 2, 15)] = "Susan B. Anthony Day"

        # Washington's Birthday
        name = "Washington's Birthday"
        if self.state == 'AL':
            name = "George Washington/Thomas Jefferson Birthday"
        elif self.state == 'AS':
            name = "George Washington's Birthday and Daisy Gatson Bates Day"
        elif self.state in ('PR', 'VI'):
            name = "Presidents' Day"
        if self.state not in ('DE', 'FL', 'GA', 'NM', 'PR'):
            if year > 1970:
                self[date(year, 2, 1) + rd(weekday=MO(+3))] = name
            elif year >= 1879:
                self[date(year, 2, 22)] = name
        elif self.state == 'GA':
            if date(year, 12, 24).weekday() != 2:
                self[date(year, 12, 24)] = name
            else:
                self[date(year, 12, 26)] = name
        elif self.state in ('PR', 'VI'):
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = name

        # Mardi Gras
        if self.state == 'LA' and year >= 1857:
            self[easter(year) + rd(days=-47)] = "Mardi Gras"

        # Guam Discovery Day
        if self.state == 'GU' and year >= 1970:
            self[date(year, 3, 1) + rd(weekday=MO)] = "Guam Discovery Day"

        # Casimir Pulaski Day
        if self.state == 'IL' and year >= 1978:
            self[date(year, 3, 1) + rd(weekday=MO)] = "Casimir Pulaski Day"

        # Texas Independence Day
        if self.state == 'TX' and year >= 1874:
            self[date(year, 3, 2)] = "Texas Independence Day"

        # Town Meeting Day
        if self.state == 'VT' and year >= 1800:
            self[date(year, 3, 1) + rd(weekday=TU)] = "Town Meeting Day"

        # Evacuation Day
        if self.state == 'MA' and year >= 1901:
            name = "Evacuation Day"
            self[date(year, 3, 17)] = name
            if date(year, 3, 17).weekday() in (5, 6):
                self[date(year, 3, 17) + rd(weekday=MO)] = name + " (Observed)"

        # Emancipation Day
        if self.state == 'PR':
            self[date(year, 3, 22)] = "Emancipation Day"
            if self.observed and date(year, 3, 22).weekday() == 6:
                self[date(year, 3, 23)] = "Emancipation Day (Observed)"

        # Prince Jonah Kuhio Kalanianaole Day
        if self.state == 'HI' and year >= 1949:
            name = "Prince Jonah Kuhio Kalanianaole Day"
            self[date(year, 3, 26)] = name
            if self.observed and date(year, 3, 26).weekday() == 5:
                self[date(year, 3, 25)] = name + " (Observed)"
            elif self.observed and date(year, 3, 26).weekday() == 6:
                self[date(year, 3, 27)] = name + " (Observed)"

        # Steward's Day
        name = "Steward's Day"
        if self.state == 'AK' and year >= 1955:
            self[date(year, 4, 1) + rd(days=-1, weekday=MO(-1))] = name
        elif self.state == 'AK' and year >= 1918:
            self[date(year, 3, 30)] = name

        # César Chávez Day
        name = "César Chávez Day"
        if self.state == 'CA' and year >= 1995:
            self[date(year, 3, 31)] = name
            if self.observed and date(year, 3, 31).weekday() == 6:
                self[date(year, 4, 1)] = name + " (Observed)"
        elif self.state == 'TX' and year >= 2000:
            self[date(year, 3, 31)] = name

        # Transfer Day
        if self.state == 'VI':
            self[date(year, 3, 31)] = "Transfer Day"

        # Emancipation Day
        if self.state == 'DC' and year >= 2005:
            name = "Emancipation Day"
            self[date(year, 4, 16)] = name
            if self.observed and date(year, 4, 16).weekday() == 5:
                self[date(year, 4, 15)] = name + " (Observed)"
            elif self.observed and date(year, 4, 16).weekday() == 6:
                self[date(year, 4, 17)] = name + " (Observed)"

        # Patriots' Day
        if self.state in ('ME', 'MA') and year >= 1969:
            self[date(year, 4, 1) + rd(weekday=MO(+3))] = "Patriots' Day"
        elif self.state in ('ME', 'MA') and year >= 1894:
            self[date(year, 4, 19)] = "Patriots' Day"

        # Holy Thursday
        if self.state == 'VI':
            self[easter(year) + rd(weekday=TH(-1))] = "Holy Thursday"

        # Good Friday
        if self.state in ('CT', 'DE', 'GU', 'IN', 'KY', 'LA',
                          'NJ', 'NC', 'PR', 'TN', 'TX', 'VI'):
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if self.state == 'VI':
            self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # Confederate Memorial Day
        name = "Confederate Memorial Day"
        if self.state in ('AL', 'GA', 'MS', 'SC') and year >= 1866:
            if self.state == 'GA' and year >= 2016:
                name = "State Holiday"
            self[date(year, 4, 1) + rd(weekday=MO(+4))] = name
        elif self.state == 'TX' and year >= 1931:
            self[date(year, 1, 19)] = name

        # San Jacinto Day
        if self.state == 'TX' and year >= 1875:
            self[date(year, 4, 21)] = "San Jacinto Day"

        # Arbor Day
        if self.state == 'NE' and year >= 1989:
            self[date(year, 4, 30) + rd(weekday=FR(-1))] = "Arbor Day"
        elif self.state == 'NE' and year >= 1875:
            self[date(year, 4, 22)] = "Arbor Day"

        # Primary Election Day
        if self.state == 'IN' and \
                ((year >= 2006 and year % 2 == 0) or year >= 2015):
            dt = date(year, 5, 1) + rd(weekday=MO)
            self[dt + rd(days=+1)] = "Primary Election Day"

        # Truman Day
        if self.state == 'MO' and year >= 1949:
            name = "Truman Day"
            self[date(year, 5, 8)] = name
            if self.observed and date(year, 5, 8).weekday() == 5:
                self[date(year, 5, 7)] = name + " (Observed)"
            elif self.observed and date(year, 5, 8).weekday() == 6:
                self[date(year, 5, 10)] = name + " (Observed)"

        # Memorial Day
        if year > 1970:
            self[date(year, 5, 31) + rd(weekday=MO(-1))] = "Memorial Day"
        elif year >= 1888:
            self[date(year, 5, 30)] = "Memorial Day"

        # Jefferson Davis Birthday
        name = "Jefferson Davis Birthday"
        if self.state == 'AL' and year >= 1890:
            self[date(year, 6, 1) + rd(weekday=MO)] = name

        # Kamehameha Day
        if self.state == 'HI' and year >= 1872:
            self[date(year, 6, 11)] = "Kamehameha Day"
            if self.observed and year >= 2011:
                if date(year, 6, 11).weekday() == 5:
                    self[date(year, 6, 10)] = "Kamehameha Day (Observed)"
                elif date(year, 6, 11).weekday() == 6:
                    self[date(year, 6, 12)] = "Kamehameha Day (Observed)"

        # Emancipation Day In Texas
        if self.state == 'TX' and year >= 1980:
            self[date(year, 6, 19)] = "Emancipation Day In Texas"

        # West Virginia Day
        name = "West Virginia Day"
        if self.state == 'WV' and year >= 1927:
            self[date(year, 6, 20)] = name
            if self.observed and date(year, 6, 20).weekday() == 5:
                self[date(year, 6, 19)] = name + " (Observed)"
            elif self.observed and date(year, 6, 20).weekday() == 6:
                self[date(year, 6, 21)] = name + " (Observed)"

        # Emancipation Day in US Virgin Islands
        if self.state == 'VI':
            self[date(year, 7, 3)] = "Emancipation Day"

        # Independence Day
        if year > 1870:
            name = "Independence Day"
            self[date(year, 7, 4)] = name
            if self.observed and date(year, 7, 4).weekday() == 5:
                self[date(year, 7, 4) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 7, 4).weekday() == 6:
                self[date(year, 7, 4) + rd(days=+1)] = name + " (Observed)"

        # Liberation Day (Guam)
        if self.state == 'GU' and year >= 1945:
            self[date(year, 7, 21)] = "Liberation Day (Guam)"

        # Pioneer Day
        if self.state == 'UT' and year >= 1849:
            name = "Pioneer Day"
            self[date(year, 7, 24)] = name
            if self.observed and date(year, 7, 24).weekday() == 5:
                self[date(year, 7, 24) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 7, 24).weekday() == 6:
                self[date(year, 7, 24) + rd(days=+1)] = name + " (Observed)"

        # Constitution Day
        if self.state == 'PR':
            self[date(year, 7, 25)] = "Constitution Day"
            if self.observed and date(year, 7, 25).weekday() == 6:
                self[date(year, 7, 26)] = "Constitution Day (Observed)"

        # Victory Day
        if self.state == 'RI' and year >= 1948:
            self[date(year, 8, 1) + rd(weekday=MO(+2))] = "Victory Day"

        # Statehood Day (Hawaii)
        if self.state == 'HI' and year >= 1959:
            self[date(year, 8, 1) + rd(weekday=FR(+3))] = "Statehood Day"

        # Bennington Battle Day
        if self.state == 'VT' and year >= 1778:
            name = "Bennington Battle Day"
            self[date(year, 8, 16)] = name
            if self.observed and date(year, 8, 16).weekday() == 5:
                self[date(year, 8, 15)] = name + " (Observed)"
            elif self.observed and date(year, 8, 16).weekday() == 6:
                self[date(year, 8, 17)] = name + " (Observed)"

        # Lyndon Baines Johnson Day
        if self.state == 'TX' and year >= 1973:
            self[date(year, 8, 27)] = "Lyndon Baines Johnson Day"

        # Labor Day
        if year >= 1894:
            self[date(year, 9, 1) + rd(weekday=MO)] = "Labor Day"

        # Columbus Day
        if self.state not in ('AK', 'DE', 'FL', 'HI', 'NV'):
            if self.state == 'SD':
                name = "Native American Day"
            elif self.state == 'VI':
                name = "Columbus Day and Puerto Rico Friendship Day"
            else:
                name = "Columbus Day"
            if year >= 1970:
                self[date(year, 10, 1) + rd(weekday=MO(+2))] = name
            elif year >= 1937:
                self[date(year, 10, 12)] = name

        # Alaska Day
        if self.state == 'AK' and year >= 1867:
            self[date(year, 10, 18)] = "Alaska Day"
            if self.observed and date(year, 10, 18).weekday() == 5:
                self[date(year, 10, 18) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 10, 18).weekday() == 6:
                self[date(year, 10, 18) + rd(days=+1)] = name + " (Observed)"

        # Nevada Day
        if self.state == 'NV' and year >= 1933:
            dt = date(year, 10, 31)
            if year >= 2000:
                dt += rd(weekday=FR(-1))
            self[dt] = "Nevada Day"
            if self.observed and dt.weekday() == 5:
                self[dt + rd(days=-1)] = "Nevada Day (Observed)"
            elif self.observed and dt.weekday() == 6:
                self[dt + rd(days=+1)] = "Nevada Day (Observed)"

        # Liberty Day
        if self.state == 'VI':
            self[date(year, 11, 1)] = "Liberty Day"

        # Election Day
        if (self.state in ('DE', 'HI', 'IL', 'IN', 'LA',
                           'MT', 'NH', 'NJ', 'NY', 'WV') and
                year >= 2008 and year % 2 == 0) \
                or (self.state in ('IN', 'NY') and year >= 2015):
            dt = date(year, 11, 1) + rd(weekday=MO)
            self[dt + rd(days=+1)] = "Election Day"

        # All Souls' Day
        if self.state == 'GU':
            self[date(year, 11, 2)] = "All Souls' Day"

        # Veterans Day
        if year > 1953:
            name = "Veterans Day"
        else:
            name = "Armistice Day"
        if 1978 > year > 1970:
            self[date(year, 10, 1) + rd(weekday=MO(+4))] = name
        elif year >= 1938:
            self[date(year, 11, 11)] = name
            if self.observed and date(year, 11, 11).weekday() == 5:
                self[date(year, 11, 11) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 11, 11).weekday() == 6:
                self[date(year, 11, 11) + rd(days=+1)] = name + " (Observed)"

        # Discovery Day
        if self.state == 'PR':
            self[date(year, 11, 19)] = "Discovery Day"
            if self.observed and date(year, 11, 19).weekday() == 6:
                self[date(year, 11, 20)] = "Discovery Day (Observed)"

        # Thanksgiving
        if year > 1870:
            self[date(year, 11, 1) + rd(weekday=TH(+4))] = "Thanksgiving"

        # Day After Thanksgiving
        # Friday After Thanksgiving
        # Lincoln's Birthday
        # American Indian Heritage Day
        # Family Day
        # New Mexico Presidents' Day
        if (self.state in ('DE', 'FL', 'NH', 'NC', 'OK', 'TX', 'WV') and
                year >= 1975) \
                or (self.state == 'IN' and year >= 2010) \
                or (self.state == 'MD' and year >= 2008) \
                or self.state in ('NV', 'NM'):
            if self.state in ('DE', 'NH', 'NC', 'OK', 'WV'):
                name = "Day After Thanksgiving"
            elif self.state in ('FL', 'TX'):
                name = "Friday After Thanksgiving"
            elif self.state == 'IN':
                name = "Lincoln's Birthday"
            elif self.state == 'MD' and year >= 2008:
                name = "American Indian Heritage Day"
            elif self.state == 'NV':
                name = "Family Day"
            elif self.state == 'NM':
                name = "Presidents' Day"
            dt = date(year, 11, 1) + rd(weekday=TH(+4))
            self[dt + rd(days=+1)] = name

        # Robert E. Lee's Birthday
        if self.state == 'GA' and year >= 1986:
            if year >= 2016:
                name = "State Holiday"
            else:
                name = "Robert E. Lee's Birthday"
            self[date(year, 11, 29) + rd(weekday=FR(-1))] = name

        # Lady of Camarin Day
        if self.state == 'GU':
            self[date(year, 12, 8)] = "Lady of Camarin Day"

        # Christmas Eve
        if self.state == 'AS' or \
                (self.state in ('KS', 'MI', 'NC') and year >= 2013) or \
                (self.state == 'TX' and year >= 1981) or \
                (self.state == 'WI' and year >= 2012):
            name = "Christmas Eve"
            self[date(year, 12, 24)] = name
            name = name + " (Observed)"
            # If on Friday, observed on Thursday
            if self.observed and date(year, 12, 24).weekday() == 4:
                self[date(year, 12, 24) + rd(days=-1)] = name
            # If on Saturday or Sunday, observed on Friday
            elif self.observed and date(year, 12, 24).weekday() in (5, 6):
                self[date(year, 12, 24) + rd(weekday=FR(-1))] = name

        # Christmas Day
        if year > 1870:
            name = "Christmas Day"
            self[date(year, 12, 25)] = "Christmas Day"
            if self.observed and date(year, 12, 25).weekday() == 5:
                self[date(year, 12, 25) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 12, 25).weekday() == 6:
                self[date(year, 12, 25) + rd(days=+1)] = name + " (Observed)"

        # Day After Christmas
        if self.state == 'NC' and year >= 2013:
            name = "Day After Christmas"
            self[date(year, 12, 26)] = name
            name = name + " (Observed)"
            # If on Saturday or Sunday, observed on Monday
            if self.observed and date(year, 12, 26).weekday() in (5, 6):
                self[date(year, 12, 26) + rd(weekday=MO)] = name
            # If on Monday, observed on Tuesday
            elif self.observed and date(year, 12, 26).weekday() == 0:
                self[date(year, 12, 26) + rd(days=+1)] = name
        elif self.state == 'TX' and year >= 1981:
            self[date(year, 12, 26)] = "Day After Christmas"
        elif self.state == 'VI':
            self[date(year, 12, 26)] = "Christmas Second Day"

        # New Year's Eve
        if (self.state in ('KY', 'MI') and year >= 2013) or \
                (self.state == 'WI' and year >= 2012):
            name = "New Year's Eve"
            self[date(year, 12, 31)] = name
            if self.observed and date(year, 12, 31).weekday() == 5:
                self[date(year, 12, 30)] = name + " (Observed)"


class US(UnitedStates):
    pass


class NewZealand(HolidayBase):
    PROVINCES = ['NTL', 'AUK', 'TKI', 'HKB', 'WGN', 'MBH', 'NSN', 'CAN',
                 'STC', 'WTL', 'OTA', 'STL', 'CIT']

    def __init__(self, **kwargs):
        self.country = 'NZ'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Bank Holidays Act 1873
        # The Employment of Females Act 1873
        # Factories Act 1894
        # Industrial Conciliation and Arbitration Act 1894
        # Labour Day Act 1899
        # Anzac Day Act 1920, 1949, 1956
        # New Zealand Day Act 1973
        # Waitangi Day Act 1960, 1976
        # Sovereign's Birthday Observance Act 1937, 1952
        # Holidays Act 1981, 2003
        if year < 1894:
            return

        # New Year's Day
        name = "New Year's Day"
        jan1 = date(year, 1, 1)
        self[jan1] = name
        if self.observed and jan1.weekday() in WEEKEND:
            self[date(year, 1, 3)] = name + " (Observed)"

        name = "Day after New Year's Day"
        jan2 = date(year, 1, 2)
        self[jan2] = name
        if self.observed and jan2.weekday() in WEEKEND:
            self[date(year, 1, 4)] = name + " (Observed)"

        # Waitangi Day
        if year > 1973:
            name = "New Zealand Day"
            if year > 1976:
                name = "Waitangi Day"
            feb6 = date(year, 2, 6)
            self[feb6] = name
            if self.observed and year >= 2014 and feb6.weekday() in WEEKEND:
                self[feb6 + rd(weekday=MO)] = name + " (Observed)"

        # Easter
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"
        self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # Anzac Day
        if year > 1920:
            name = "Anzac Day"
            apr25 = date(year, 4, 25)
            self[apr25] = name
            if self.observed and year >= 2014 and apr25.weekday() in WEEKEND:
                self[apr25 + rd(weekday=MO)] = name + " (Observed)"

        # Sovereign's Birthday
        if year >= 1952:
            name = "Queen's Birthday"
        elif year > 1901:
            name = "King's Birthday"
        if year == 1952:
            self[date(year, 6, 2)] = name  # Elizabeth II
        elif year > 1937:
            self[date(year, 6, 1) + rd(weekday=MO(+1))] = name  # EII & GVI
        elif year == 1937:
            self[date(year, 6, 9)] = name   # George VI
        elif year == 1936:
            self[date(year, 6, 23)] = name  # Edward VIII
        elif year > 1911:
            self[date(year, 6, 3)] = name   # George V
        elif year > 1901:
            # http://paperspast.natlib.govt.nz/cgi-bin/paperspast?a=d&d=NZH19091110.2.67
            self[date(year, 11, 9)] = name  # Edward VII

        # Labour Day
        name = "Labour Day"
        if year >= 1910:
            self[date(year, 10, 1) + rd(weekday=MO(+4))] = name
        elif year > 1899:
            self[date(year, 10, 1) + rd(weekday=WE(+2))] = name

        # Christmas Day
        name = "Christmas Day"
        dec25 = date(year, 12, 25)
        self[dec25] = name
        if self.observed and dec25.weekday() in WEEKEND:
            self[date(year, 12, 27)] = name + " (Observed)"

        # Boxing Day
        name = "Boxing Day"
        dec26 = date(year, 12, 26)
        self[dec26] = name
        if self.observed and dec26.weekday() in WEEKEND:
            self[date(year, 12, 28)] = name + " (Observed)"

        # Province Anniversary Day
        if self.prov in ('NTL', 'Northland', 'AUK', 'Auckland'):
            if 1963 < year <= 1973 and self.prov in ('NTL', 'Northland'):
                name = "Waitangi Day"
                dt = date(year, 2, 6)
            else:
                name = "Auckland Anniversary Day"
                dt = date(year, 1, 29)
            if dt.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                self[dt + rd(weekday=MO(-1))] = name
            else:
                self[dt + rd(weekday=MO)] = name

        elif self.prov in ('TKI', 'Taranaki', 'New Plymouth'):
            name = "Taranaki Anniversary Day"
            self[date(year, 3, 1) + rd(weekday=MO(+2))] = name

        elif self.prov in ('HKB', "Hawke's Bay"):
            name = "Hawke's Bay Anniversary Day"
            labour_day = date(year, 10, 1) + rd(weekday=MO(+4))
            self[labour_day + rd(weekday=FR(-1))] = name

        elif self.prov in ('WGN', 'Wellington'):
            name = "Wellington Anniversary Day"
            jan22 = date(year, 1, 22)
            if jan22.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                self[jan22 + rd(weekday=MO(-1))] = name
            else:
                self[jan22 + rd(weekday=MO)] = name

        elif self.prov in ('MBH', 'Marlborough'):
            name = "Marlborough Anniversary Day"
            labour_day = date(year, 10, 1) + rd(weekday=MO(+4))
            self[labour_day + rd(weeks=1)] = name

        elif self.prov in ('NSN', 'Nelson'):
            name = "Nelson Anniversary Day"
            feb1 = date(year, 2, 1)
            if feb1.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                self[feb1 + rd(weekday=MO(-1))] = name
            else:
                self[feb1 + rd(weekday=MO)] = name

        elif self.prov in ('CAN', 'Canterbury'):
            name = "Canterbury Anniversary Day"
            showday = date(year, 11, 1) + rd(weekday=TU) + rd(weekday=FR(+2))
            self[showday] = name

        elif self.prov in ('STC', 'South Canterbury'):
            name = "South Canterbury Anniversary Day"
            dominion_day = date(year, 9, 1) + rd(weekday=MO(4))
            self[dominion_day] = name

        elif self.prov in ('WTL', 'Westland'):
            name = "Westland Anniversary Day"
            dec1 = date(year, 12, 1)
            # Observance varies?!?!
            if year == 2005:     # special case?!?!
                self[date(year, 12, 5)] = name
            elif dec1.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                self[dec1 + rd(weekday=MO(-1))] = name
            else:
                self[dec1 + rd(weekday=MO)] = name

        elif self.prov in ('OTA', 'Otago'):
            name = "Otago Anniversary Day"
            mar23 = date(year, 3, 23)
            # there is no easily determined single day of local observance?!?!
            if mar23.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                dt = mar23 + rd(weekday=MO(-1))
            else:
                dt = mar23 + rd(weekday=MO)
            if dt == easter(year) + rd(weekday=MO):    # Avoid Easter Monday
                dt += rd(days=1)
            self[dt] = name

        elif self.prov in ('STL', 'Southland'):
            name = "Southland Anniversary Day"
            jan17 = date(year, 1, 17)
            if year > 2011:
                self[easter(year) + rd(weekday=TU)] = name
            else:
                if jan17.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                    self[jan17 + rd(weekday=MO(-1))] = name
                else:
                    self[jan17 + rd(weekday=MO)] = name

        elif self.prov in ('CIT', 'Chatham Islands'):
            name = "Chatham Islands Anniversary Day"
            nov30 = date(year, 11, 30)
            if nov30.weekday() in (TUESDAY, WEDNESDAY, THURSDAY):
                self[nov30 + rd(weekday=MO(-1))] = name
            else:
                self[nov30 + rd(weekday=MO)] = name


class NZ(NewZealand):
    pass


class Australia(HolidayBase):
    PROVINCES = ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA']

    def __init__(self, **kwargs):
        self.country = 'AU'
        self.prov = kwargs.pop('prov', kwargs.pop('state', 'ACT'))
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # ACT:  Holidays Act 1958
        # NSW:  Public Holidays Act 2010
        # NT:   Public Holidays Act 2013
        # QLD:  Holidays Act 1983
        # SA:   Holidays Act 1910
        # TAS:  Statutory Holidays Act 2000
        # VIC:  Public Holidays Act 1993
        # WA:   Public and Bank Holidays Act 1972

        # TODO do more research on history of Aus holidays

        # New Year's Day
        name = "New Year's Day"
        jan1 = date(year, 1, 1)
        self[jan1] = name
        if self.observed and jan1.weekday() in WEEKEND:
            self[jan1 + rd(weekday=MO)] = name + " (Observed)"

        # Australia Day
        jan26 = date(year, 1, 26)
        if year >= 1935:
            if self.prov == 'NSW' and year < 1946:
                name = "Anniversary Day"
            else:
                name = "Australia Day"
            self[jan26] = name
            if self.observed and year >= 1946 and jan26.weekday() in WEEKEND:
                self[jan26 + rd(weekday=MO)] = name + " (Observed)"
        elif year >= 1888 and self.prov != 'SA':
            name = "Anniversary Day"
            self[jan26] = name

        # Adelaide Cup
        if self.prov == 'SA':
            name = "Adelaide Cup"
            if year >= 2006:
                # subject to proclamation ?!?!
                self[date(year, 3, 1) + rd(weekday=MO(+2))] = name
            else:
                self[date(year, 3, 1) + rd(weekday=MO(+3))] = name

        # Canberra Day
        if self.prov == 'ACT':
            name = "Canberra Day"
            self[date(year, 3, 1) + rd(weekday=MO(+1))] = name

        # Easter
        self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"
        if self.prov in ('ACT', 'NSW', 'NT', 'QLD', 'SA', 'VIC'):
            self[easter(year) + rd(weekday=SA(-1))] = "Easter Saturday"
        if self.prov == 'NSW':
            self[easter(year)] = "Easter Sunday"
        self[easter(year) + rd(weekday=MO)] = "Easter Monday"

        # Anzac Day
        if year > 1920:
            name = "Anzac Day"
            apr25 = date(year, 4, 25)
            self[apr25] = name
            if self.observed:
                if apr25.weekday() == SATURDAY and self.prov in ('WA', 'NT'):
                    self[apr25 + rd(weekday=MO)] = name + " (Observed)"
                elif (apr25.weekday() == SUNDAY and
                      self.prov in ('ACT', 'QLD', 'SA', 'WA', 'NT')):
                    self[apr25 + rd(weekday=MO)] = name + " (Observed)"

        # Western Australia Day
        if self.prov == 'WA' and year > 1832:
            if year >= 2015:
                name = "Western Australia Day"
            else:
                name = "Foundation Day"
            self[date(year, 6, 1) + rd(weekday=MO(+1))] = name

        # Sovereign's Birthday
        if year >= 1952:
            name = "Queen's Birthday"
        elif year > 1901:
            name = "King's Birthday"
        if year >= 1936:
            name = "Queen's Birthday"
            if self.prov == 'QLD':
                if year == 2012:
                    self[date(year, 6, 11)] = "Queen's Diamond Jubilee"
                if year < 2016 and year != 2012:
                    dt = date(year, 6, 1) + rd(weekday=MO(+2))
                    self[dt] = name
                else:
                    dt = date(year, 10, 1) + rd(weekday=MO)
                    self[dt] = name
            elif self.prov == 'WA':
                # by proclamation ?!?!
                self[date(year, 10, 1) + rd(weekday=MO(-1))] = name
            else:
                dt = date(year, 6, 1) + rd(weekday=MO(+2))
                self[dt] = name
        elif year > 1911:
            self[date(year, 6, 3)] = name   # George V
        elif year > 1901:
            self[date(year, 11, 9)] = name  # Edward VII

        # Picnic Day
        if self.prov == 'NT':
            name = "Picnic Day"
            self[date(year, 8, 1) + rd(weekday=MO)] = name

        # Labour Day
        name = "Labour Day"
        if self.prov in ('NSW', 'ACT', 'SA'):
            self[date(year, 10, 1) + rd(weekday=MO)] = name
        elif self.prov == 'WA':
            self[date(year, 3, 1) + rd(weekday=MO)] = name
        elif self.prov == 'VIC':
            self[date(year, 3, 1) + rd(weekday=MO(+2))] = name
        elif self.prov == 'QLD':
            if 2013 <= year <= 2015:
                self[date(year, 10, 1) + rd(weekday=MO)] = name
            else:
                self[date(year, 5, 1) + rd(weekday=MO)] = name
        elif self.prov == 'NT':
            name = "May Day"
            self[date(year, 5, 1) + rd(weekday=MO)] = name
        elif self.prov == 'TAS':
            name = "Eight Hours Day"
            self[date(year, 3, 1) + rd(weekday=MO(+2))] = name

        # Family & Community Day
        if self.prov == 'ACT':
            name = "Family & Community Day"
            if 2007 <= year <= 2009:
                self[date(year, 11, 1) + rd(weekday=TU)] = name
            elif year == 2010:
                # first Monday of the September/October school holidays
                # moved to the second Monday if this falls on Labour day
                # TODO need a formula for the ACT school holidays then
                # http://www.cmd.act.gov.au/communication/holidays
                self[date(year, 9, 26)] = name
            elif year == 2011:
                self[date(year, 10, 10)] = name
            elif year == 2012:
                self[date(year, 10, 8)] = name
            elif year == 2013:
                self[date(year, 9, 30)] = name
            elif year == 2014:
                self[date(year, 9, 29)] = name
            elif year == 2015:
                self[date(year, 9, 28)] = name
            elif year == 2016:
                self[date(year, 9, 26)] = name
            elif 2017 <= year <= 2020:
                labour_day = date(year, 10, 1) + rd(weekday=MO)
                if year == 2017:
                    dt = date(year, 9, 23) + rd(weekday=MO)
                elif year == 2018:
                    dt = date(year, 9, 29) + rd(weekday=MO)
                elif year == 2019:
                    dt = date(year, 9, 28) + rd(weekday=MO)
                elif year == 2020:
                    dt = date(year, 9, 26) + rd(weekday=MO)
                if dt == labour_day:
                    dt += rd(weekday=MO(+1))
                self[date(year, 9, 26)] = name

        # Melbourne Cup
        if self.prov == 'VIC':
            name = "Melbourne Cup"
            self[date(year, 11, 1) + rd(weekday=TU)] = name

        # The Royal Queensland Show (Ekka)
        # The Show starts on the first Friday of August - providing this is
        # not prior to the 5th - in which case it will begin on the second
        # Friday. The Wednesday during the show is a public holiday.
        if self.prov == 'QLD':
            name = "The Royal Queensland Show"
            self[date(year, 8, 5) + rd(weekday=FR) + rd(weekday=WE)] = name

        # Christmas Day
        name = "Christmas Day"
        dec25 = date(year, 12, 25)
        self[dec25] = name
        if self.observed and dec25.weekday() in WEEKEND:
            self[date(year, 12, 27)] = name + " (Observed)"

        # Boxing Day
        if self.prov == 'SA':
            name = "Proclamation Day"
        else:
            name = "Boxing Day"
        dec26 = date(year, 12, 26)
        self[dec26] = name
        if self.observed and dec26.weekday() in WEEKEND:
            self[date(year, 12, 28)] = name + " (Observed)"


class AU(Australia):
    pass


class Germany(HolidayBase):
    """Official holidays for Germany in its current form.

    This class doesn't return any holidays before 1990-10-03.

    Before that date the current Germany was separated into the "German
    Democratic Republic" and the "Federal Republic of Germany" which both had
    somewhat different holidays. Since this class is called "Germany" it
    doesn't really make sense to include the days from the two former
    countries.

    Note that Germany doesn't have rules for holidays that happen on a
    Sunday. Those holidays are still holiday days but there is no additional
    day to make up for the "lost" day.

    Also note that German holidays are partly declared by each province there
    are some weired edge cases:

        - "Mariä Himmelfahrt" is only a holiday in Bavaria (BY) if your
          municipality is mostly catholic which in term depends on census data.
          Since we don't have this data but most municipalities in Bavaria
          *are* mostly catholic, we count that as holiday for whole Bavaria.
        - There is an "Augsburger Friedensfest" which only exists in the town
          Augsburg. This is excluded for Bavaria.
        - "Gründonnerstag" (Thursday before easter) is not a holiday but pupil
           don't have to go to school (but only in Baden Württemberg) which is
           solved by adjusting school holidays to include this day. It is
           excluded from our list.
        - "Fronleichnam" is a holiday in certain, explicitly defined
          municipalities in Saxony (SN) and Thuringia (TH). We exclude it from
          both provinces.
    """

    PROVINCES = ['BW', 'BY', 'BE', 'BB', 'HB', 'HH', 'HE', 'MV', 'NI', 'NW',
                 'RP', 'SL', 'SN', 'ST', 'SH', 'TH']

    def __init__(self, **kwargs):
        self.country = 'DE'
        self.prov = kwargs.pop('prov', 'SH')
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year <= 1989:
            return

        if year == 1990:
            self[date(year, 6, 17)] = 'Tag der deutschen Einheit'

        if year > 1990:

            self[date(year, 1, 1)] = 'Neujahr'

            if self.prov in ('BW', 'BY', 'ST'):
                self[date(year, 1, 6)] = 'Heilige Drei Könige'

            self[easter(year) - rd(days=2)] = 'Karfreitag'

            # will always be a Sunday and we have no "observed" rule so
            # this is pretty pointless but it's nonetheless an official
            # holiday by law
            self[easter(year)] = 'Ostersonntag'

            self[easter(year) + rd(days=1)] = 'Ostermontag'

            self[date(year, 5, 1)] = 'Erster Mai'

            self[easter(year) + rd(days=39)] = 'Christi Himmelfahrt'

            # will always be a Sunday and we have no "observed" rule so
            # this is pretty pointless but it's nonetheless an official
            # holiday by law
            self[easter(year) + rd(days=49)] = 'Pfingstsonntag'

            self[easter(year) + rd(days=50)] = 'Pfingstmontag'

            if self.prov in ('BW', 'BY', 'HE', 'NW', 'RP', 'SL'):
                self[easter(year) + rd(days=60)] = 'Fronleichnam'

            if self.prov in ('BY', 'SL'):
                self[date(year, 8, 15)] = 'Mariä Himmelfahrt'

            self[date(year, 10, 3)] = 'Tag der Deutschen Einheit'

        if self.prov in ('BB', 'MV', 'SN', 'ST', 'TH'):
            self[date(year, 10, 31)] = 'Reformationstag'

        if self.prov in ('HB', 'SH', 'NI', 'HH') and year >= 2018:
            self[date(year, 10, 31)] = 'Reformationstag'

        # in 2017 all states got the Reformationstag (500th anniversary of
        # Luther's thesis)
        if year == 2017:
            self[date(year, 10, 31)] = 'Reformationstag'

        # since 2018 additional states got the Reformationstag
        if year >= 2018:
            if self.prov in ('HB', 'HH', 'NI', 'SH'):
                self[date(year, 10, 31)] = 'Reformationstag'

        if self.prov in ('BW', 'BY', 'NW', 'RP', 'SL'):
            self[date(year, 11, 1)] = 'Allerheiligen'

        if (year >= 1990 and year <= 1994) or self.prov == 'SN':
            # can be calculated as "last wednesday before year-11-23" which is
            # why we need to go back two wednesdays if year-11-23 happens to be
            # a wednesday
            base_data = date(year, 11, 23)
            weekday_delta = WE(-2) if base_data.weekday() == 2 else WE(-1)
            self[base_data + rd(weekday=weekday_delta)] = 'Buß- und Bettag'

        self[date(year, 12, 25)] = 'Erster Weihnachtstag'
        self[date(year, 12, 26)] = 'Zweiter Weihnachtstag'


class DE(Germany):
    pass


class Austria(HolidayBase):
    PROVINCES = ['B', 'K', 'N', 'O', 'S', 'ST', 'T', 'V', 'W']

    def __init__(self, **kwargs):
        self.country = 'AT'
        self.prov = kwargs.pop('prov', kwargs.pop('state', 'W'))
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # public holidays
        self[date(year, 1, 1)] = "Neujahr"
        self[date(year, 1, 6)] = "Heilige Drei Könige"
        self[easter(year) + rd(weekday=MO)] = "Ostermontag"
        self[date(year, 5, 1)] = "Staatsfeiertag"
        self[easter(year) + rd(days=39)] = "Christi Himmelfahrt"
        self[easter(year) + rd(days=50)] = "Pfingstmontag"
        self[easter(year) + rd(days=60)] = "Fronleichnam"
        self[date(year, 8, 15)] = "Maria Himmelfahrt"
        if 1919 <= year <= 1934:
            self[date(year, 11, 12)] = "Nationalfeiertag"
        if year >= 1967:
            self[date(year, 10, 26)] = "Nationalfeiertag"
        self[date(year, 11, 1)] = "Allerheiligen"
        self[date(year, 12, 8)] = "Maria Empfängnis"
        self[date(year, 12, 25)] = "Christtag"
        self[date(year, 12, 26)] = "Stefanitag"


class AT(Austria):
    pass


class Denmark(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Denmark

    def __init__(self, **kwargs):
        self.country = 'DK'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Public holidays
        self[date(year, 1, 1)] = "Nytårsdag"
        self[easter(year) + rd(weekday=TH(-1))] = "Skærtorsdag"
        self[easter(year) + rd(weekday=FR(-1))] = "Langfredag"
        self[easter(year)] = "Påskedag"
        self[easter(year) + rd(weekday=MO)] = "Anden påskedag"
        self[easter(year) + rd(weekday=FR(+4))] = "Store bededag"
        self[easter(year) + rd(days=39)] = "Kristi himmelfartsdag"
        self[easter(year) + rd(days=49)] = "Pinsedag"
        self[easter(year) + rd(days=50)] = "Anden pinsedag"
        self[date(year, 12, 25)] = "Juledag"
        self[date(year, 12, 26)] = "Anden juledag"


class DK(Denmark):
    pass


class UnitedKingdom(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom

    def __init__(self, **kwargs):
        self.country = 'UK'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):

        # New Year's Day
        if year >= 1974:
            name = "New Year's Day"
            self[date(year, 1, 1)] = name
            if self.observed and date(year, 1, 1).weekday() == 6:
                self[date(year, 1, 1) + rd(days=+1)] = name + " (Observed)"
            elif self.observed and date(year, 1, 1).weekday() == 5:
                self[date(year, 1, 1) + rd(days=+2)] = name + " (Observed)"

        # New Year Holiday
        if self.country in ('UK', 'Scotland'):
            name = "New Year Holiday"
            if self.country == 'UK':
                name += " [Scotland]"
            self[date(year, 1, 2)] = name
            if self.observed and date(year, 1, 2).weekday() in (5, 6):
                self[date(year, 1, 2) + rd(days=+2)] = name + " (Observed)"
            elif self.observed and date(year, 1, 2).weekday() == 0:
                self[date(year, 1, 2) + rd(days=+1)] = name + " (Observed)"

        # St. Patrick's Day
        if self.country in ('UK', 'Northern Ireland', 'Ireland'):
            name = "St. Patrick's Day"
            if self.country == 'UK':
                name += " [Northern Ireland]"
            self[date(year, 3, 17)] = name
            if self.observed and date(year, 3, 17).weekday() in (5, 6):
                self[date(year, 3, 17) + rd(weekday=MO)] = name + " (Observed)"

        # Good Friday
        if self.country != 'Ireland':
            self[easter(year) + rd(weekday=FR(-1))] = "Good Friday"

        # Easter Monday
        if self.country != 'Scotland':
            name = "Easter Monday"
            if self.country == 'UK':
                name += " [England, Wales, Northern Ireland]"
            self[easter(year) + rd(weekday=MO)] = name

        # May Day bank holiday (first Monday in May)
        if year >= 1978:
            name = "May Day"
            if year == 1995:
                dt = date(year, 5, 8)
            else:
                dt = date(year, 5, 1)
            if dt.weekday() == 0:
                self[dt] = name
            elif dt.weekday() == 1:
                self[dt + rd(days=+6)] = name
            elif dt.weekday() == 2:
                self[dt + rd(days=+5)] = name
            elif dt.weekday() == 3:
                self[dt + rd(days=+4)] = name
            elif dt.weekday() == 4:
                self[dt + rd(days=+3)] = name
            elif dt.weekday() == 5:
                self[dt + rd(days=+2)] = name
            elif dt.weekday() == 6:
                self[dt + rd(days=+1)] = name

        # Spring bank holiday (last Monday in May)
        if self.country != 'Ireland':
            name = "Spring Bank Holiday"
            if year == 2012:
                self[date(year, 6, 4)] = name
            elif year >= 1971:
                self[date(year, 5, 31) + rd(weekday=MO(-1))] = name

        # June bank holiday (first Monday in June)
        if self.country == 'Ireland':
            self[date(year, 6, 1) + rd(weekday=MO)] = "June Bank Holiday"

        # TT bank holiday (first Friday in June)
        if self.country == 'Isle of Man':
            self[date(year, 6, 1) + rd(weekday=FR)] = "TT Bank Holiday"

        # Tynwald Day
        if self.country == 'Isle of Man':
            self[date(year, 7, 5)] = "Tynwald Day"

        # Battle of the Boyne
        if self.country in ('UK', 'Northern Ireland'):
            name = "Battle of the Boyne"
            if self.country == 'UK':
                name += " [Northern Ireland]"
            self[date(year, 7, 12)] = name

        # Summer bank holiday (first Monday in August)
        if self.country in ('UK', 'Scotland', 'Ireland'):
            name = "Summer Bank Holiday"
            if self.country == 'UK':
                name += " [Scotland]"
            self[date(year, 8, 1) + rd(weekday=MO)] = name

        # Late Summer bank holiday (last Monday in August)
        if self.country not in ('Scotland', 'Ireland') and year >= 1971:
            name = "Late Summer Bank Holiday"
            if self.country == 'UK':
                name += " [England, Wales, Northern Ireland]"
            self[date(year, 8, 31) + rd(weekday=MO(-1))] = name

        # October Bank Holiday (last Monday in October)
        if self.country == 'Ireland':
            name = "October Bank Holiday"
            self[date(year, 10, 31) + rd(weekday=MO(-1))] = name

        # St. Andrew's Day
        if self.country in ('UK', 'Scotland'):
            name = "St. Andrew's Day"
            if self.country == 'UK':
                name += " [Scotland]"
            self[date(year, 11, 30)] = name

        # Christmas Day
        name = "Christmas Day"
        self[date(year, 12, 25)] = name
        if self.observed and date(year, 12, 25).weekday() == 5:
            self[date(year, 12, 27)] = name + " (Observed)"
        elif self.observed and date(year, 12, 25).weekday() == 6:
            self[date(year, 12, 27)] = name + " (Observed)"

        # Boxing Day
        name = "Boxing Day"
        self[date(year, 12, 26)] = name
        if self.observed and date(year, 12, 26).weekday() == 5:
            self[date(year, 12, 28)] = name + " (Observed)"
        elif self.observed and date(year, 12, 26).weekday() == 6:
            self[date(year, 12, 28)] = name + " (Observed)"

        # Special holidays
        if self.country != 'Ireland':
            if year == 1977:
                self[date(year, 6, 7)] = "Silver Jubilee of Elizabeth II"
            elif year == 1981:
                self[date(year, 7, 29)] = "Wedding of Charles and Diana"
            elif year == 1999:
                self[date(year, 12, 31)] = "Millennium Celebrations"
            elif year == 2002:
                self[date(year, 6, 3)] = "Golden Jubilee of Elizabeth II"
            elif year == 2011:
                self[date(year, 4, 29)] = "Wedding of William and Catherine"
            elif year == 2012:
                self[date(year, 6, 5)] = "Diamond Jubilee of Elizabeth II"


class UK(UnitedKingdom):
    pass


class England(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'England'
        HolidayBase.__init__(self, **kwargs)


class Wales(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'Wales'
        HolidayBase.__init__(self, **kwargs)


class Scotland(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'Scotland'
        HolidayBase.__init__(self, **kwargs)


class IsleOfMan(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'Isle of Man'
        HolidayBase.__init__(self, **kwargs)


class NorthernIreland(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'Northern Ireland'
        HolidayBase.__init__(self, **kwargs)


class Ireland(UnitedKingdom):

    def __init__(self, **kwargs):
        self.country = 'Ireland'
        HolidayBase.__init__(self, **kwargs)


class IE(Ireland):
    pass


class Spain(HolidayBase):
    PROVINCES = ['AND', 'ARG', 'AST', 'CAN', 'CAM', 'CAL', 'CAT', 'CVA',
                 'EXT', 'GAL', 'IBA', 'ICA', 'MAD', 'MUR', 'NAV', 'PVA', 'RIO']

    def __init__(self, **kwargs):
        self.country = 'ES'
        self.prov = kwargs.pop('prov', kwargs.pop('state', ''))
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "Año nuevo"
        self[date(year, 1, 6)] = "Epifanía del Señor"
        if self.prov and self.prov in ['CVA', 'MUR', 'MAD', 'NAV', 'PVA']:
            self[date(year, 3, 19)] = "San José"
        if self.prov and self.prov != 'CAT':
            self[easter(year) + rd(weeks=-1, weekday=TH)] = "Jueves Santo"
        self[easter(year) + rd(weeks=-1, weekday=FR)] = "Viernes Santo"
        if self.prov and self.prov in ['CAT', 'PVA', 'NAV', 'CVA', 'IBA']:
            self[easter(year) + rd(weekday=MO)] = "Lunes de Pascua"
        self[date(year, 5, 1)] = "Día del Trabajador"
        if self.prov and self.prov in ['CAT', 'GAL']:
            self[date(year, 6, 24)] = "San Juan"
        self[date(year, 8, 15)] = "Asunción de la Virgen"
        self[date(year, 10, 12)] = "Día de la Hispanidad"
        self[date(year, 11, 1)] = "Todos los Santos"
        self[date(year, 12, 6)] = "Día de la constitución Española"
        self[date(year, 12, 8)] = "La Inmaculada Concepción"
        self[date(year, 12, 25)] = "Navidad"
        if self.prov and self.prov in ['CAT', 'IBA']:
            self[date(year, 12, 26)] = "San Esteban"
        # Provinces festive day
        if self.prov:
            if self.prov == 'AND':
                self[date(year, 2, 28)] = "Día de Andalucia"
            elif self.prov == 'ARG':
                self[date(year, 4, 23)] = "Día de San Jorge"
            elif self.prov == 'AST':
                self[date(year, 3, 8)] = "Día de Asturias"
            elif self.prov == 'CAN':
                self[date(year, 2, 28)] = "Día de la Montaña"
            elif self.prov == 'CAM':
                self[date(year, 2, 28)] = "Día de Castilla - La Mancha"
            elif self.prov == 'CAL':
                self[date(year, 4, 23)] = "Día de Castilla y Leon"
            elif self.prov == 'CAT':
                self[date(year, 9, 11)] = "Día Nacional de Catalunya"
            elif self.prov == 'CVA':
                self[date(year, 10, 9)] = "Día de la Comunidad Valenciana"
            elif self.prov == 'EXT':
                self[date(year, 9, 8)] = "Día de Extremadura"
            elif self.prov == 'GAL':
                self[date(year, 7, 25)] = "Día Nacional de Galicia"
            elif self.prov == 'IBA':
                self[date(year, 3, 1)] = "Día de las Islas Baleares"
            elif self.prov == 'ICA':
                self[date(year, 5, 30)] = "Día de Canarias"
            elif self.prov == 'MAD':
                self[date(year, 5, 2)] = "Día de Comunidad De Madrid"
            elif self.prov == 'MUR':
                self[date(year, 6, 9)] = "Día de la Región de Murcia"
            elif self.prov == 'NAV':
                self[date(year, 9, 27)] = "Día de Navarra"
            elif self.prov == 'PVA':
                self[date(year, 10, 25)] = "Día del Páis Vasco"
            elif self.prov == 'RIO':
                self[date(year, 6, 9)] = "Día de La Rioja"


class ES(Spain):
    pass


class EuropeanCentralBank(HolidayBase):
    # https://en.wikipedia.org/wiki/TARGET2
    # http://www.ecb.europa.eu/press/pr/date/2000/html/pr001214_4.en.html

    def __init__(self, **kwargs):
        self.country = 'EU'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "New Year's Day"
        e = easter(year)
        self[e - rd(days=2)] = "Good Friday"
        self[e + rd(days=1)] = "Easter Monday"
        self[date(year, 5, 1)] = "1 May (Labour Day)"
        self[date(year, 12, 25)] = "Christmas Day"
        self[date(year, 12, 26)] = "26 December"


class ECB(EuropeanCentralBank):
    pass


class TAR(EuropeanCentralBank):
    pass


class Czech(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_the_Czech_Republic

    def __init__(self, **kwargs):
        self.country = 'CZ'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "Den obnovy samostatného českého státu" \
            if year >= 2000 else \
            "Nový rok"

        e = easter(year)
        if year <= 1951 or year >= 2016:
            self[e - rd(days=2)] = "Velký pátek"
        self[e + rd(days=1)] = "Velikonoční pondělí"

        if year >= 1951:
            self[date(year, 5, 1)] = "Svátek práce"
        if year >= 1992:
            self[date(year, 5, 8)] = "Den vítězství"
        elif year >= 1947:
            self[date(year, 5, 9)] = "Den vítězství nad hitlerovským fašismem"
        if year >= 1951:
            self[date(year, 7, 5)] = "Den slovanských věrozvěstů " \
                "Cyrila a Metoděje"
            self[date(year, 7, 6)] = "Den upálení mistra Jana Husa"
        if year >= 2000:
            self[date(year, 9, 28)] = "Den české státnosti"
        if year >= 1951:
            self[date(year, 10, 28)] = "Den vzniku samostatného " \
                "československého státu"
        if year >= 1990:
            self[date(year, 11, 17)] = "Den boje za svobodu a demokracii"

        if year >= 1990:
            self[date(year, 12, 24)] = "Štědrý den"
        if year >= 1951:
            self[date(year, 12, 25)] = "1. svátek vánoční"
            self[date(year, 12, 26)] = "2. svátek vánoční"


class CZ(Czech):
    pass


class Slovak(HolidayBase):
    # https://sk.wikipedia.org/wiki/Sviatok
    # https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1993/241/20181011.html

    def __init__(self, **kwargs):
        self.country = 'SK'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "Deň vzniku Slovenskej republiky" \

        self[date(year, 1, 6)] = "Zjavenie Pána (Traja králi a vianočný" \
            "sviatok pravoslávnych kresťanov)"

        e = easter(year)
        self[e - rd(days=2)] = "Veľký piatok"
        self[e + rd(days=1)] = "Veľkonočný pondelok"

        self[date(year, 5, 1)] = "Sviatok práce"

        if year >= 1997:
            self[date(year, 5, 8)] = "Deň víťazstva nad fašizmom"

        self[date(year, 7, 5)] = "Sviatok svätého Cyrila a svätého Metoda"

        self[date(year, 8, 29)] = "Výročie Slovenského národného povstania"

        self[date(year, 9, 1)] = "Deň Ústavy Slovenskej republiky"

        self[date(year, 9, 15)] = "Sedembolestná Panna Mária"
        if year == 2018:
            self[date(year, 10, 30)] = "100. výročie prijatia Deklarácie " \
                                       "slovenského národa"
        self[date(year, 11, 1)] = "Sviatok Všetkých svätých"

        if year >= 2001:
            self[date(year, 11, 17)] = "Deň boja za slobodu a demokraciu"

        self[date(year, 12, 24)] = "Štedrý deň"

        self[date(year, 12, 25)] = "Prvý sviatok vianočný"

        self[date(year, 12, 26)] = "Druhý sviatok vianočný"


class SK(Slovak):
    pass


class Polish(HolidayBase):
    # https://pl.wikipedia.org/wiki/Dni_wolne_od_pracy_w_Polsce

    def __init__(self, **kwargs):
        self.country = 'PL'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = 'Nowy Rok'
        if year >= 2011:
            self[date(year, 1, 6)] = 'Święto Trzech Króli'

        e = easter(year)
        self[e] = 'Niedziela Wielkanocna'
        self[e + rd(days=1)] = 'Poniedziałek Wielkanocny'

        if year >= 1950:
            self[date(year, 5, 1)] = 'Święto Państwowe'
        if year >= 1919:
            self[date(year, 5, 3)] = 'Święto Narodowe Trzeciego Maja'

        self[e + rd(days=49)] = 'Zielone Świątki'
        self[e + rd(days=60)] = 'Dzień Bożego Ciała'

        self[date(year, 8, 15)] = 'Wniebowzięcie Najświętszej Marii Panny'

        self[date(year, 11, 1)] = 'Uroczystość Wszystkich świętych'
        if (1937 <= year <= 1945) or year >= 1989:
            self[date(year, 11, 11)] = 'Narodowe Święto Niepodległości'

        self[date(year, 12, 25)] = 'Boże Narodzenie (pierwszy dzień)'
        self[date(year, 12, 26)] = 'Boże Narodzenie (drugi dzień)'


class PL(Polish):
    pass


class Portugal(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Portugal

    def __init__(self, **kwargs):
        self.country = 'PT'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "Ano Novo"

        e = easter(year)

        # carnival is no longer a holiday, but some companies let workers off.
        # @todo recollect the years in which it was a public holiday
        # self[e - rd(days=47)] = "Carnaval"
        self[e - rd(days=2)] = "Sexta-feira Santa"
        self[e] = "Páscoa"

        # Revoked holidays in 2013–2015
        if year < 2013 or year > 2015:
            self[e + rd(days=60)] = "Corpo de Deus"
            self[date(year, 10,  5)] = "Implantação da República"
            self[date(year, 11,  1)] = "Dia de Todos os Santos"
            self[date(year, 12,  1)] = "Restauração da Independência"

        self[date(year,  4, 25)] = "Dia da Liberdade"
        self[date(year,  5,  1)] = "Dia do Trabalhador"
        self[date(year,  6, 10)] = "Dia de Portugal"
        self[date(year,  8, 15)] = "Assunção de Nossa Senhora"
        self[date(year, 12,  8)] = "Imaculada Conceição"
        self[date(year, 12, 25)] = "Christmas Day"


class PT(Portugal):
    pass


class PortugalExt(Portugal):
    """
    Adds extended days that most people have as a bonus from their companies:
    - Carnival
    - the day before and after xmas
    - the day before the new year
    - Lisbon's city holiday
    """
    def _populate(self, year):
        super(PortugalExt, self)._populate(year)

        e = easter(year)
        self[e - rd(days=47)] = "Carnaval"
        self[date(year, 12, 24)] = "Vespera de Natal"
        self[date(year, 12, 26)] = "26 de Dezembro"
        self[date(year, 12, 31)] = "Vespera de Ano novo"
        self[date(year,  6, 13)] = "Dia de Santo António"

        # TODO add bridging days
        # - get Holidays that occur on Tuesday  and add Monday (-1 day)
        # - get Holidays that occur on Thursday and add Friday (+1 day)


class PTE(PortugalExt):
    pass


class Netherlands(HolidayBase):
    SUNDAY = 6

    def __init__(self, **kwargs):
        # http://www.iamsterdam.com/en/plan-your-trip/practical-info/public-holidays
        self.country = "NL"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New years
        self[date(year, 1, 1)] = "Nieuwjaarsdag"

        easter_date = easter(year)

        # Easter
        self[easter_date] = "Eerste paasdag"

        # Second easter day
        self[easter_date + rd(days=1)] = "Tweede paasdag"

        # Ascension day
        self[easter_date + rd(days=39)] = "Hemelvaart"

        # Pentecost
        self[easter_date + rd(days=49)] = "Eerste Pinksterdag"

        # Pentecost monday
        self[easter_date + rd(days=50)] = "Tweede Pinksterdag"

        # First christmas
        self[date(year, 12, 25)] = "Eerste Kerstdag"

        # Second christmas
        self[date(year, 12, 26)] = "Tweede Kerstdag"

        # Liberation day
        if year >= 1945 and year % 5 == 0:
            self[date(year, 5, 5)] = "Bevrijdingsdag"

        # Kingsday
        if year >= 2014:
            kings_day = date(year, 4, 27)
            if kings_day.weekday() == self.SUNDAY:
                kings_day = kings_day - rd(days=1)

            self[kings_day] = "Koningsdag"

        # Queen's day
        if 1891 <= year <= 2013:
            queens_day = date(year, 4, 30)
            if year <= 1948:
                queens_day = date(year, 8, 31)

            if queens_day.weekday() == self.SUNDAY:
                if year < 1980:
                    queens_day = queens_day + rd(days=1)
                else:
                    queens_day = queens_day - rd(days=1)

            self[queens_day] = "Koninginnedag"


class NL(Netherlands):
    pass


class Norway(HolidayBase):
    """
    Norwegian holidays.
    Note that holidays falling on a sunday is "lost",
    it will not be moved to another day to make up for the collision.

    In Norway, ALL sundays are considered a holiday (https://snl.no/helligdag).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.

    Primary sources:
    https://lovdata.no/dokument/NL/lov/1947-04-26-1
    https://no.wikipedia.org/wiki/Helligdager_i_Norge
    https://www.timeanddate.no/merkedag/norge/
    """
    def __init__(self, include_sundays=True, **kwargs):
        """

        :param include_sundays: Whether to consider sundays as a holiday
        (which they are in Norway)
        :param kwargs:
        """
        self.country = "NO"
        self.include_sundays = include_sundays
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Add all the sundays of the year before adding the "real" holidays
        if self.include_sundays:
            first_day_of_year = date(year, 1, 1)
            first_sunday_of_year = first_day_of_year\
                + rd(days=SUNDAY - first_day_of_year.weekday())
            cur_date = first_sunday_of_year

            while cur_date < date(year+1, 1, 1):
                assert cur_date.weekday() == SUNDAY

                self[cur_date] = "Søndag"
                cur_date += rd(days=7)

        # ========= Static holidays =========
        self[date(year, 1, 1)] = "Første nyttårsdag"

        # Source: https://lovdata.no/dokument/NL/lov/1947-04-26-1
        if year >= 1947:
            self[date(year, 5,  1)] = "Arbeidernes dag"
            self[date(year, 5, 17)] = "Grunnlovsdag"

        # According to https://no.wikipedia.org/wiki/F%C3%B8rste_juledag,
        # these dates are only valid from year > 1700
        # Wikipedia has no source for the statement, so leaving this be for now
        self[date(year, 12, 25)] = "Første juledag"
        self[date(year, 12, 26)] = "Andre juledag"

        # ========= Moving holidays =========
        # NOTE: These are probably subject to the same > 1700
        # restriction as the above dates. The only source I could find for how
        # long Easter has been celebrated in Norway was
        # https://www.hf.uio.no/ikos/tjenester/kunnskap/samlinger/norsk-folkeminnesamling/livs-og-arshoytider/paske.html
        # which says
        # "(...) has been celebrated for over 1000 years (...)" (in Norway)
        e = easter(year)
        maundy_thursday = e - rd(days=3)
        good_friday = e - rd(days=2)
        resurrection_sunday = e
        easter_monday = e + rd(days=1)
        ascension_thursday = e + rd(days=39)
        pentecost = e + rd(days=49)
        pentecost_day_two = e + rd(days=50)

        assert maundy_thursday.weekday() == THURSDAY
        assert good_friday.weekday() == FRIDAY
        assert resurrection_sunday.weekday() == SUNDAY
        assert easter_monday.weekday() == MONDAY
        assert ascension_thursday.weekday() == THURSDAY
        assert pentecost.weekday() == SUNDAY
        assert pentecost_day_two.weekday() == MONDAY

        self[maundy_thursday] = "Skjærtorsdag"
        self[good_friday] = "Langfredag"
        self[resurrection_sunday] = "Første påskedag"
        self[easter_monday] = "Andre påskedag"
        self[ascension_thursday] = "Kristi himmelfartsdag"
        self[pentecost] = "Første pinsedag"
        self[pentecost_day_two] = "Andre pinsedag"


class NO(Norway):
    pass


class Italy(HolidayBase):
    PROVINCES = ['MI', 'RM']

    def __init__(self, **kwargs):
        self.country = 'IT'
        self.prov = kwargs.pop('prov', kwargs.pop('state', ''))
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "Capodanno"
        self[date(year, 1, 6)] = "Epifania del Signore"
        self[easter(year)] = "Pasqua di Resurrezione"
        self[easter(year) + rd(weekday=MO)] = "Lunedì dell'Angelo"
        if year >= 1946:
            self[date(year, 4, 25)] = "Festa della Liberazione"
        self[date(year, 5, 1)] = "Festa dei Lavoratori"
        if year >= 1948:
            self[date(year, 6, 2)] = "Festa della Repubblica"
        self[date(year, 8, 15)] = "Assunzione della Vergine"
        self[date(year, 11, 1)] = "Tutti i Santi"
        self[date(year, 12, 8)] = "Immacolata Concezione"
        self[date(year, 12, 25)] = "Natale"
        self[date(year, 12, 26)] = "Santo Stefano"
        # Provinces festive day
        # TODO: add all provinces' saints
        if self.prov:
            if self.prov == 'MI':
                self[date(year, 12, 7)] = "Sant'Ambrogio"
            if self.prov == 'RM':
                self[date(year, 6, 29)] = "Santi Pietro e Paolo"


class IT(Italy):
    pass


class Sweden(HolidayBase):
    """
    Swedish holidays.
    Note that holidays falling on a sunday are "lost",
    it will not be moved to another day to make up for the collision.
    In Sweden, ALL sundays are considered a holiday
    (https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige).
    Initialize this class with include_sundays=False
    to not include sundays as a holiday.
    Primary sources:
    https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige and
    http://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1989253-om-allmanna-helgdagar_sfs-1989-253
    """

    def __init__(self, include_sundays=True, **kwargs):
        """
        :param include_sundays: Whether to consider sundays as a holiday
        (which they are in Sweden)
        :param kwargs:
        """
        self.country = "SE"
        self.include_sundays = include_sundays
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Add all the sundays of the year before adding the "real" holidays
        if self.include_sundays:
            first_day_of_year = date(year, 1, 1)
            first_sunday_of_year = first_day_of_year\
                + rd(days=SUNDAY - first_day_of_year.weekday())
            cur_date = first_sunday_of_year

            while cur_date < date(year + 1, 1, 1):
                assert cur_date.weekday() == SUNDAY

                self[cur_date] = "Söndag"
                cur_date += rd(days=7)

        # ========= Static holidays =========
        self[date(year, 1, 1)] = "Nyårsdagen"

        self[date(year, 1, 6)] = "Trettondedag jul"

        # Source: https://sv.wikipedia.org/wiki/F%C3%B6rsta_maj
        if year >= 1939:
            self[date(year, 5, 1)] = "Första maj"

        # Source: https://sv.wikipedia.org/wiki/Sveriges_nationaldag
        if year >= 2005:
            self[date(year, 6, 6)] = "Sveriges nationaldag"

        self[date(year, 12, 24)] = "Julafton"
        self[date(year, 12, 25)] = "Juldagen"
        self[date(year, 12, 26)] = "Annandag jul"
        self[date(year, 12, 31)] = "Nyårsafton"

        # ========= Moving holidays =========
        e = easter(year)
        maundy_thursday = e - rd(days=3)
        good_friday = e - rd(days=2)
        easter_saturday = e - rd(days=1)
        resurrection_sunday = e
        easter_monday = e + rd(days=1)
        ascension_thursday = e + rd(days=39)
        pentecost = e + rd(days=49)
        pentecost_day_two = e + rd(days=50)

        assert maundy_thursday.weekday() == THURSDAY
        assert good_friday.weekday() == FRIDAY
        assert easter_saturday.weekday() == SATURDAY
        assert resurrection_sunday.weekday() == SUNDAY
        assert easter_monday.weekday() == MONDAY
        assert ascension_thursday.weekday() == THURSDAY
        assert pentecost.weekday() == SUNDAY
        assert pentecost_day_two.weekday() == MONDAY

        self[good_friday] = "Långfredagen"
        self[resurrection_sunday] = "Påskdagen"
        self[easter_monday] = "Annandag påsk"
        self[ascension_thursday] = "Kristi himmelsfärdsdag"
        self[pentecost] = "Pingstdagen"
        if year <= 2004:
            self[pentecost_day_two] = "Annandag pingst"

        # Midsummer evening. Friday between June 19th and June 25th
        self[date(year, 6, 19) + rd(weekday=FR)] = "Midsommarafton"

        # Midsummer day. Saturday between June 20th and June 26th
        if year >= 1953:
            self[date(year, 6, 20) + rd(weekday=SA)] = "Midsommardagen"
        else:
            self[date(year, 6, 24)] = "Midsommardagen"
            # All saints day. Friday between October 31th and November 6th
        self[date(year, 10, 31) + rd(weekday=SA)] = "Alla helgons dag"

        if year <= 1953:
            self[date(year, 3, 25)] = "Jungfru Marie bebådelsedag"


class SE(Sweden):
    pass


class Japan(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Japan

    def __init__(self, **kwargs):
        self.country = 'JP'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year < 1949 or year > 2099:
            raise NotImplementedError

        # New Year's Day
        self[date(year, 1, 1)] = "元日"

        # Coming of Age Day
        if year <= 1999:
            self[date(year, 1, 15)] = "成人の日"
        else:
            self[date(year, 1, 1) + rd(weekday=MO(+2))] = "成人の日"

        # Foundation Day
        self[date(year, 2, 11)] = "建国記念の日"

        # Vernal Equinox Day
        self[self._vernal_equinox_day(year)] = "春分の日"

        # The former Emperor's Birthday, Greenery Day or Showa Day
        if year <= 1988:
            self[date(year, 4, 29)] = "天皇誕生日"
        elif year <= 2006:
            self[date(year, 4, 29)] = "みどりの日"
        else:
            self[date(year, 4, 29)] = "昭和の日"

        # Constitution Memorial Day
        self[date(year, 5, 3)] = "憲法記念日"

        # Greenery Day
        if year >= 2007:
            self[date(year, 5, 4)] = "みどりの日"

        # Children's Day
        self[date(year, 5, 5)] = "こどもの日"

        # Marine Day
        if 1996 <= year <= 2002:
            self[date(year, 7, 20)] = "海の日"
        elif year >= 2003:
            self[date(year, 7, 1) + rd(weekday=MO(+3))] = "海の日"

        # Mountain Day
        if year >= 2016:
            self[date(year, 8, 11)] = "山の日"

        # Respect for the Aged Day
        if 1966 <= year <= 2002:
            self[date(year, 9, 15)] = "敬老の日"
        elif year >= 2003:
            self[date(year, 9, 1) + rd(weekday=MO(+3))] = "敬老の日"

        # Autumnal Equinox Day
        self[self._autumnal_equinox_day(year)] = "秋分の日"

        # Health and Sports Day
        if 1966 <= year <= 1999:
            self[date(year, 10, 10)] = "体育の日"
        elif year >= 2000:
            self[date(year, 10, 1) + rd(weekday=MO(+2))] = "体育の日"

        # Culture Day
        self[date(year, 11, 3)] = "文化の日"

        # Labour Thanksgiving Day
        self[date(year, 11, 23)] = "勤労感謝の日"

        # The Emperor's Birthday
        if year >= 1989:
            self[date(year, 12, 23)] = "天皇誕生日"

        # A weekday between national holidays becomes a holiday too (国民の休日)
        self._add_national_holidays(year)

        # Substitute holidays
        self._add_substitute_holidays(year)

    def _vernal_equinox_day(self, year):
        day = 20
        if year % 4 == 0:
            if year <= 1956:
                day = 21
            elif year >= 2092:
                day = 19
        elif year % 4 == 1:
            if year <= 1989:
                day = 21
        elif year % 4 == 2:
            if year <= 2022:
                day = 21
        elif year % 4 == 3:
            if year <= 2055:
                day = 21
        return date(year, 3, day)

    def _autumnal_equinox_day(self, year):
        day = 22
        if year % 4 == 0:
            if year <= 2008:
                day = 23
        elif year % 4 == 1:
            if year <= 2041:
                day = 23
        elif year % 4 == 2:
            if year <= 2074:
                day = 23
        elif year % 4 == 3:
            if year <= 1979:
                day = 24
            else:
                day = 23
        return date(year, 9, day)

    def _add_national_holidays(self, year):
        if year in (1993, 1999, 2004, 1988, 1994, 2005, 1989, 1995, 2000, 2006,
                    1990, 2001, 1991, 1996, 2002):
            self[date(year, 5, 4)] = "国民の休日"

        if year in (2032, 2049, 2060, 2077, 2088, 2094):
            self[date(year, 9, 21)] = "国民の休日"

        if year in (2009, 2015, 2026, 2037, 2043, 2054, 2065, 2071, 2099):
            self[date(year, 9, 22)] = "国民の休日"

    def _add_substitute_holidays(self, year):
        table = (
            (1, 2, (1978, 1984, 1989, 1995, 2006, 2012, 2017, 2023, 2034, 2040,
                    2045)),
            (1, 16, (1978, 1984, 1989, 1995)),
            (2, 12, (1979, 1990, 1996, 2001, 2007, 2018, 2024, 2029, 2035,
                     2046)),
            (3, 21, (1988, 2005, 2016, 2033, 2044, 2050)),
            (3, 22, (1982, 1999, 2010, 2027)),
            (4, 30, (1973, 1979, 1984, 1990, 2001, 2007, 2012, 2018, 2029,
                     2035, 2040, 2046)),
            (5, 4, (1981, 1987, 1992, 1998)),
            (5, 6, (1985, 1991, 1996, 2002, 2013, 2019, 2024, 2030, 2041, 2047,
                    2008, 2014, 2025, 2031, 2036, 2042, 2009, 2015, 2020, 2026,
                    2037, 2043, 2048)),
            (7, 21, (1997,)),
            (8, 12, (2019, 2024, 2030, 2041, 2047)),
            (9, 16, (1974, 1985, 1991, 1996, 2002)),
            (9, 23, (2024,)),
            (9, 24, (1973, 1984, 1990, 2001, 2007, 2018, 2029, 2035, 2046)),
            (10, 11, (1976, 1982, 1993, 1999)),
            (11, 4, (1974, 1985, 1991, 1996, 2002, 2013, 2019, 2024, 2030,
                     2041, 2047)),
            (11, 24, (1975, 1980, 1986, 1997, 2003, 2008, 2014, 2025, 2031,
                      2036, 2042)),
            (12, 24, (1990, 2001, 2007, 2012, 2018)),
        )
        for holiday in table:
            month = holiday[0]
            day = holiday[1]
            years = holiday[2]
            if year in years:
                self[date(year, month, day)] = "振替休日"


class JP(Japan):
    pass


class France(HolidayBase):
    """Official French holidays.

    Some provinces have specific holidays, only those are included in the
    PROVINCES, because these provinces have different administrative status,
    which makes it difficult to enumerate.

    For religious holidays usually happening on Sundays (Easter, Pentecost),
    only the following Monday is considered a holiday.

    Primary sources:
        https://fr.wikipedia.org/wiki/Fêtes_et_jours_fériés_en_France
        https://www.service-public.fr/particuliers/vosdroits/F2405
    """

    PROVINCES = ['Métropole', 'Alsace-Moselle', 'Guadeloupe', 'Guyane',
                 'Martinique', 'Mayotte', 'Nouvelle-Calédonie', 'La Réunion',
                 'Polynésie Française', 'Saint-Barthélémy', 'Saint-Martin',
                 'Wallis-et-Futuna']

    def __init__(self, **kwargs):
        self.country = 'FR'
        self.prov = kwargs.pop('prov', 'Métropole')
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # Civil holidays
        if year > 1810:
            self[date(year, 1, 1)] = "Jour de l'an"

        if year > 1919:
            name = 'Fête du Travail'
            if year <= 1948:
                name += ' et de la Concorde sociale'
            self[date(year, 5, 1)] = name

        if (1953 <= year <= 1959) or year > 1981:
            self[date(year, 5, 8)] = 'Armistice 1945'

        if year >= 1880:
            self[date(year, 7, 14)] = 'Fête nationale'

        if year >= 1918:
            self[date(year, 11, 11)] = 'Armistice 1918'

        # Religious holidays
        if self.prov in ['Alsace-Moselle', 'Guadeloupe', 'Guyane',
                         'Martinique', 'Polynésie Française']:
            self[easter(year) - rd(days=2)] = 'Vendredi saint'

        if self.prov == 'Alsace-Moselle':
            self[date(year, 12, 26)] = 'Deuxième jour de Noël'

        if year >= 1886:
            self[easter(year) + rd(days=1)] = 'Lundi de Pâques'
            self[easter(year) + rd(days=50)] = 'Lundi de Pentecôte'

        if year >= 1802:
            self[easter(year) + rd(days=39)] = 'Ascension'
            self[date(year, 8, 15)] = 'Assomption'
            self[date(year, 11, 1)] = 'Toussaint'

            name = 'Noël'
            if self.prov == 'Alsace-Moselle':
                name = 'Premier jour de ' + name
            self[date(year, 12, 25)] = name

        # Non-metropolitan holidays (starting dates missing)
        if self.prov == 'Mayotte':
            self[date(year, 4, 27)] = "Abolition de l'esclavage"

        if self.prov == 'Wallis-et-Futuna':
            self[date(year, 4, 28)] = 'Saint Pierre Chanel'

        if self.prov == 'Martinique':
            self[date(year, 5, 22)] = "Abolition de l'esclavage"

        if self.prov in ['Guadeloupe', 'Saint-Martin']:
            self[date(year, 5, 27)] = "Abolition de l'esclavage"

        if self.prov == 'Guyane':
            self[date(year, 6, 10)] = "Abolition de l'esclavage"

        if self.prov == 'Polynésie Française':
            self[date(year, 6, 29)] = "Fête de l'autonomie"

        if self.prov in ['Guadeloupe', 'Martinique']:
            self[date(year, 7, 21)] = 'Fête Victor Schoelcher'

        if self.prov == 'Wallis-et-Futuna':
            self[date(year, 7, 29)] = 'Fête du Territoire'

        if self.prov == 'Nouvelle-Calédonie':
            self[date(year, 9, 24)] = 'Fête de la Citoyenneté'

        if self.prov == 'Saint-Barthélémy':
            self[date(year, 10, 9)] = "Abolition de l'esclavage"

        if self.prov == 'La Réunion' and year >= 1981:
            self[date(year, 12, 20)] = "Abolition de l'esclavage"


# FR already exists (Friday), we don't want to mess it up
class FRA(France):
    pass


class Belgium(HolidayBase):
    """
    https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen
    https://nl.wikipedia.org/wiki/Feestdagen_in_Belgi%C3%AB
    """
    def __init__(self, **kwargs):
        self.country = "BE"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New years
        self[date(year, 1, 1)] = "Nieuwjaarsdag"

        easter_date = easter(year)

        # Easter
        self[easter_date] = "Pasen"

        # Second easter day
        self[easter_date + rd(days=1)] = "Paasmaandag"

        # Ascension day
        self[easter_date + rd(days=39)] = "O.L.H. Hemelvaart"

        # Pentecost
        self[easter_date + rd(days=49)] = "Pinksteren"

        # Pentecost monday
        self[easter_date + rd(days=50)] = "Pinkstermaandag"

        # International Workers' Day
        self[date(year, 5, 1)] = "Dag van de Arbeid"

        # Belgian National Day
        self[date(year, 7, 21)] = "Nationale feestdag"

        # Assumption of Mary
        self[date(year, 8, 15)] = "O.L.V. Hemelvaart"

        # All Saints' Day
        self[date(year, 11, 1)] = "Allerheiligen"

        # Armistice Day
        self[date(year, 11, 11)] = "Wapenstilstand"

        # First christmas
        self[date(year, 12, 25)] = "Kerstmis"


class BE(Belgium):
    pass


class SouthAfrica(HolidayBase):
    def __init__(self, **kwargs):
        # http://www.gov.za/about-sa/public-holidays
        self.country = "ZA"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, 1, 1)] = "New Year's Day"
        self[date(year, 3, 21)] = "Human Rights Day"

        e = easter(year)
        good_friday = e - rd(days=2)
        easter_monday = e + rd(days=1)
        self[good_friday] = "Good Friday"
        self[easter_monday] = "Family Day"

        self[date(year, 4, 27)] = "Freedom Day"
        self[date(year, 5, 1)] = "Worker's Day"
        self[date(year, 6, 16)] = "Youth Day"
        self[date(year, 8, 9)] = "National Women's Day"
        self[date(year, 9, 24)] = "Heritage Day"
        self[date(year, 12, 16)] = "Day of Reconciliation"
        self[date(year, 12, 25)] = "Christmas Day"
        self[date(year, 12, 26)] = "Day of Goodwill"

        for k, v in list(self.items()):
            if self.observed and k.weekday() == 6:
                self[k + rd(days=1)] = v + " (Observed)"


class ZA(SouthAfrica):
    pass


class Slovenia(HolidayBase):
    """
    Contains all work-free public holidays in Slovenia.
    No holidays are returned before year 1991 when Slovenia became independent
    country. Before that Slovenia was part of Socialist federal republic of
    Yugoslavia.

    List of holidays (including those that are not work-free:
    https://en.wikipedia.org/wiki/Public_holidays_in_Slovenia
    """

    def __init__(self, **kwargs):
        self.country = 'SI'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year <= 1990:
            return

        if year > 1991:
            self[date(year, 1, 1)] = "novo leto"

            # Between 2012 and 2017 2nd January was not public holiday,
            # or at least not work-free day
            if year < 2013 or year > 2016:
                self[date(year, 1, 2)] = "novo leto"

            # Prešeren's day, slovenian cultural holiday
            self[date(year, 2, 8)] = "Prešernov dan"

            # Easter monday is the only easter related work-free day
            easter_day = easter(year)
            self[easter_day + rd(days=1)] = "Velikonočni ponedeljek"

            # Day of uprising against occupation
            self[date(year, 4, 27)] = "dan upora proti okupatorju"

            # Labour day, two days of it!
            self[date(year, 5, 1)] = "praznik dela"
            self[date(year, 5, 2)] = "praznik dela"

            # Statehood day
            self[date(year, 6, 25)] = "dan državnosti"

            # Assumption day
            self[date(year, 8, 15)] = "Marijino vnebovzetje"

            # Reformation day
            self[date(year, 10, 31)] = "dan reformacije"

            # Remembrance day
            self[date(year, 11, 1)] = "dan spomina na mrtve"

            # Christmas
            self[date(year, 12, 25)] = "Božič"

            # Day of independence and unity
            self[date(year, 12, 26)] = "dan samostojnosti in enotnosti"


class SI(Slovenia):
    pass


class Finland(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Finland

    def __init__(self, **kwargs):
        self.country = "FI"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        e = easter(year)

        self[date(year, 1, 1)] = "Uudenvuodenpäivä"
        self[date(year, 1, 6)] = "Loppiainen"
        self[e - rd(days=2)] = "Pitkäperjantai"
        self[e] = "Pääsiäispäivä"
        self[e + rd(days=1)] = "2. pääsiäispäivä"
        self[date(year, 5, 1)] = "Vappu"
        self[e + rd(days=39)] = "Helatorstai"
        self[e + rd(days=49)] = "Helluntaipäivä"
        self[date(year, 6, 20) + rd(weekday=SA)] = "Juhannuspäivä"
        self[date(year, 10, 31) + rd(weekday=SA)] = "Pyhäinpäivä"
        self[date(year, 12, 6)] = "Itsenäisyyspäivä"
        self[date(year, 12, 25)] = "Joulupäivä"
        self[date(year, 12, 26)] = "Tapaninpäivä"

        # Juhannusaatto (Midsummer Eve) and Jouluaatto (Christmas Eve) are not
        # official holidays, but are de facto.
        self[date(year, 6, 19) + rd(weekday=FR)] = "Juhannusaatto"
        self[date(year, 12, 24)] = "Jouluaatto"


class FI(Finland):
    pass


class Switzerland(HolidayBase):
    PROVINCES = ['AG', 'AR', 'AI', 'BL', 'BS', 'BE', 'FR', 'GE', 'GL',
                 'GR', 'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SZ',
                 'SO', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH']

    def __init__(self, **kwargs):
        self.country = 'CH'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # public holidays
        self[date(year, 1, 1)] = 'Neujahrestag'

        if self.prov in ('AG', 'BE', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU',
                         'NE', 'OW', 'SH', 'SO', 'TG', 'VD', 'ZG', 'ZH'):
            self[date(year, 1, 2)] = 'Berchtoldstag'

        if self.prov in ('SZ', 'TI', 'UR'):
            self[date(year, 1, 6)] = 'Heilige Drei Könige'

        if self.prov == 'NE':
            self[date(year, 3, 1)] = 'Jahrestag der Ausrufung der Republik'

        if self.prov in ('NW', 'SZ', 'TI', 'UR', 'VS'):
            self[date(year, 3, 19)] = 'Josefstag'

        # Näfelser Fahrt (first Thursday in April but not in Holy Week)
        if self.prov == 'GL' and year >= 1835:
            if ((date(year, 4, 1) + rd(weekday=FR)) !=
                    (easter(year) - rd(days=2))):
                self[date(year, 4, 1) + rd(weekday=TH)] = 'Näfelser Fahrt'
            else:
                self[date(year, 4, 8) + rd(weekday=TH)] = 'Näfelser Fahrt'

        # it's a Holiday on a Sunday
        self[easter(year)] = 'Ostern'

        # VS don't have easter
        if self.prov != 'VS':
            self[easter(year) - rd(days=2)] = 'Karfreitag'
            self[easter(year) + rd(weekday=MO)] = 'Ostermontag'

        if self.prov in ('BL', 'BS', 'JU', 'NE', 'SH', 'SO', 'TG', 'TI',
                         'ZH'):
            self[date(year, 5, 1)] = 'Tag der Arbeit'

        self[easter(year) + rd(days=39)] = 'Auffahrt'

        # it's a Holiday on a Sunday
        self[easter(year) + rd(days=49)] = 'Pfingsten'

        self[easter(year) + rd(days=50)] = 'Pfingstmontag'

        if self.prov in ('AI', 'JU', 'LU', 'NW', 'OW', 'SZ', 'TI', 'UR',
                         'VS', 'ZG'):
            self[easter(year) + rd(days=60)] = 'Fronleichnam'

        if self.prov == 'JU':
            self[date(year, 6, 23)] = 'Fest der Unabhängigkeit'

        if self.prov == 'TI':
            self[date(year, 6, 29)] = 'Peter und Paul'

        if year >= 1291:
            self[date(year, 8, 1)] = 'Nationalfeiertag'

        if self.prov in ('AI', 'JU', 'LU', 'NW', 'OW', 'SZ', 'TI', 'UR',
                         'VS', 'ZG'):
            self[date(year, 8, 15)] = 'Maria Himmelfahrt'

        if self.prov == 'OW':
            self[date(year, 9, 25)] = 'Bruder Klaus'

        if self.prov in ('AI', 'GL', 'JU', 'LU', 'NW', 'OW', 'SG', 'SZ',
                         'TI', 'UR', 'VS', 'ZG'):
            self[date(year, 11, 1)] = 'Allerheiligen'

        if self.prov in ('AI', 'LU', 'NW', 'OW', 'SZ', 'TI', 'UR', 'VS',
                         'ZG'):
            self[date(year, 12, 8)] = 'Maria Empfängnis'

        if self.prov == 'GE':
            self[date(year, 12, 12)] = 'Escalade de Genève'

        self[date(year, 12, 25)] = 'Weihnachten'

        if self.prov in ('AG', 'AR', 'AI', 'BL', 'BS', 'BE', 'FR', 'GL',
                         'GR', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SZ',
                         'SO', 'TG', 'TI', 'UR', 'ZG', 'ZH'):
            self[date(year, 12, 26)] = 'Stephanstag'

        if self.prov == 'GE':
            self[date(year, 12, 31)] = 'Wiederherstellung der Republik'


class CH(Switzerland):
    pass


class Hungary(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Hungary

    def __init__(self, **kwargs):
        self.country = "HU"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New years
        self[date(year, 1, 1)] = "Újév"

        # National Day
        self[date(year, 3, 15)] = "Nemzeti ünnep"

        easter_date = easter(year)

        # Good Friday
        self[easter_date + rd(weekday=FR(-1))] = "Nagypéntek"

        # Easter
        self[easter_date] = "Húsvét"

        # Second easter day
        self[easter_date + rd(days=1)] = "Húsvét Hétfő"

        # Pentecost
        self[easter_date + rd(days=49)] = "Pünkösd"

        # Pentecost monday
        self[easter_date + rd(days=50)] = "Pünkösdhétfő"

        # International Workers' Day
        self[date(year, 5, 1)] = "A Munka ünnepe"

        # State Foundation Day
        self[date(year, 8, 20)] = "Az államalapítás ünnepe"

        # National Day
        self[date(year, 10, 23)] = "Nemzeti ünnep"

        # All Saints' Day
        self[date(year, 11, 1)] = "Mindenszentek"

        # First christmas
        self[date(year, 12, 25)] = "Karácsony"

        # Second christmas
        self[date(year, 12, 26)] = "Karácsony másnapja"


class HU(Hungary):
    pass


class India(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_India
    # https://www.calendarlabs.com/holidays/india/
    # https://slusi.dacnet.nic.in/watershedatlas/list_of_state_abbreviation.htm

    PROVINCES = ['AS', 'CG', 'SK', 'KA', 'GJ', 'BR', 'RJ', 'OD',
                 'TN', 'AP', 'WB', 'KL', 'HR', 'MH', 'MP', 'UP', 'UK']

    def __init__(self, **kwargs):
        self.country = "IND"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New year
        self[date(year, 1, 1)] = "New Year"

        # Pongal/ Makar Sankranti
        self[date(year, 1, 14)] = "Makar Sankranti / Pongal"

        if year >= 1950:
            # Republic Day
            self[date(year, 1, 26)] = "Republic Day"

        if year >= 1947:
            # Independence Day
            self[date(year, 8, 15)] = "Independence Day"

        # Gandhi Jayanti
        self[date(year, 10, 2)] = "Gandhi Jayanti"

        # Labour Day
        self[date(year, 5, 1)] = "Labour Day"

        # Christmas
        self[date(year, 12, 25)] = "Christmas"

        # GJ: Gujarat
        if self.prov == "GJ":
            self[date(year, 1, 14)] = "Uttarayan"
            self[date(year, 5, 1)] = "Gujarat Day"
            self[date(year, 10, 31)] = "Sardar Patel Jayanti"

        if self.prov == 'BR':
            self[date(year, 3, 22)] = "Bihar Day"

        if self.prov == 'RJ':
            self[date(year, 3, 30)] = "Rajasthan Day"
            self[date(year, 6, 15)] = "Maharana Pratap Jayanti"

        if self.prov == 'OD':
            self[date(year, 4, 1)] = "Odisha Day (Utkala Dibasa)"
            self[date(year, 4, 15)] = "Maha Vishuva Sankranti / Pana Sankranti"

        if self.prov in ('OD', 'AP', 'BR', 'WB', 'KL',
                         'HR', 'MH', 'UP', 'UK', 'TN'):
            self[date(year, 4, 14)] = "Dr. B. R. Ambedkar's Jayanti"

        if self.prov == 'TN':
            self[date(year, 4, 14)] = "Puthandu (Tamil New Year)"
            self[date(year, 4, 15)] = "Puthandu (Tamil New Year)"

        if self.prov == 'WB':
            self[date(year, 4, 14)] = "Pohela Boishakh"
            self[date(year, 4, 15)] = "Pohela Boishakh"
            self[date(year, 5, 9)] = "Rabindra Jayanti"

        if self.prov == 'AS':
            self[date(year, 4, 15)] = "Bihu (Assamese New Year)"

        if self.prov == 'MH':
            self[date(year, 5, 1)] = "Maharashtra Day"

        if self.prov == 'SK':
            self[date(year, 5, 16)] = "Annexation Day"

        if self.prov == 'KA':
            self[date(year, 11, 1)] = "Karnataka Rajyotsava"

        if self.prov == 'AP':
            self[date(year, 11, 1)] = "Andhra Pradesh Foundation Day"

        if self.prov == 'HR':
            self[date(year, 11, 1)] = "Haryana Foundation Day"

        if self.prov == 'MP':
            self[date(year, 11, 1)] = "Madhya Pradesh Foundation Day"

        if self.prov == 'KL':
            self[date(year, 11, 1)] = "Kerala Foundation Day"

        if self.prov == 'CG':
            self[date(year, 11, 1)] = "Chhattisgarh Foundation Day"


class IND(India):
    pass


class Croatia(HolidayBase):

    # https://en.wikipedia.org/wiki/Public_holidays_in_Croatia

    def __init__(self, **kwargs):
        self.country = "HR"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New years
        self[date(year, 1, 1)] = "Nova Godina"
        # Epiphany
        self[date(year, 1, 6)] = "Sveta tri kralja"
        easter_date = easter(year)

        # Easter
        self[easter_date] = "Uskrs"
        # Easter Monday
        self[easter_date + rd(days=1)] = "Uskrsni ponedjeljak"

        # Corpus Christi
        self[easter_date + rd(days=60)] = "Tijelovo"

        # International Workers' Day
        self[date(year, 5, 1)] = "Međunarodni praznik rada"

        # Anti-fascist struggle day
        self[date(year, 6, 22)] = "Dan antifašističke borbe"

        # Statehood day
        self[date(year, 6, 22)] = "Dan državnosti"

        # Victory and Homeland Thanksgiving Day
        self[date(year, 8, 5)] = "Dan pobjede i domovinske zahvalnosti"

        # Assumption of Mary
        self[date(year, 8, 15)] = "Velika Gospa"

        # Independence Day
        self[date(year, 10, 8)] = "Dan neovisnosti"

        # All Saints' Day
        self[date(year, 11, 1)] = "Svi sveti"

        # Christmas day
        self[date(year, 12, 25)] = "Božić"

        # St. Stephen's day
        self[date(year, 12, 26)] = "Sveti Stjepan"


class HR(Croatia):
    pass
