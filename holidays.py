# -*- coding: utf-8 -*-

#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country-specific sets of
#  holidays on the fly. It aims to make determining whether a specific date is
#  a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)

__version__ = '0.3-dev'


from datetime import date, datetime
from dateutil.easter import easter
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TH, FR


class HolidayBase(dict):

    def __init__(self, years=[], expand=True, observed=True, prov=None):
        self.observed = observed
        self.expand = expand
        self.years = set(years)
        if not getattr(self, 'prov', False):
            self.prov = prov
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
        try:
            # Python 2
            is_string = isinstance(key, str) or isinstance(key, unicode)
        except NameError:
            # Python 3
            is_string = isinstance(key, bytes) or isinstance(key, str)

        if isinstance(key, datetime):
            key = key.date()
        elif isinstance(key, date):
            key = key
        elif isinstance(key, int) or isinstance(key, float):
            key = datetime.fromtimestamp(key).date()
        elif is_string:
            try:
                key = parse(key).date()
            except TypeError:
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
        return dict.__setitem__(self, self.__keytransform__(key), value)

    def get(self, key):
        return dict.get(self, self.__keytransform__(key))

    def pop(self, key, default=None):
        if default is None:
            return dict.pop(self, self.__keytransform__(key))
        return dict.pop(self, self.__keytransform__(key), default)

    def __eq__(self, other):
        return (dict.__eq__(self, other) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return (dict.__ne__(self, other) or self.__dict__ != other.__dict__)

    def __add__(self, other):
        if not isinstance(other, HolidayBase):
            raise TypeError()
        HolidaySum = createHolidaySum(self, other)
        prov = getattr(self, 'prov', None) or getattr(other, 'prov', None)
        return HolidaySum(years=(self.years | other.years), expand=self.expand,
                          observed=self.observed, prov=prov)

    def __radd__(self, other):
        return self.__add__(other)


def createHolidaySum(h1, h2):

    class HolidaySum(HolidayBase):

        def __init__(self, **kwargs):
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


class Canada(HolidayBase):

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
            # The next year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday)
            if self.observed and date(year, 12, 31).weekday() == 4:
                self[date(year, 12, 31)] = name + " (Observed)"

        # Islander Day
        if self.prov == 'PE' and year >= 2010:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Islander Day"
        elif self.prov == 'PE' and year == 2009:
            self[date(year, 2, 1) + rd(weekday=MO(+2))] = "Islander Day"

        # Family Day / Louis Riel Day (MB)
        if self.prov in ('AB', 'SK', 'ON') and year >= 2008:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov in ('AB', 'SK') and year >= 2007:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov == 'AB' and year >= 1990:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Family Day"
        elif self.prov == 'BC' and year >= 2013:
            self[date(year, 2, 1) + rd(weekday=MO(+2))] = "Family Day"
        elif self.prov == 'MB' and year >= 2008:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = "Louis Riel Day"

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

        # Victoria Day / National Patriotes Day (QC)
        if self.prov not in ('NB', 'NS', 'PE', 'NL', 'QC') and year >= 1953:
            self[date(year, 5, 24) + rd(weekday=MO(-1))] = "Victoria Day"
        elif self.prov == 'QC' and year >= 1953:
            name = "National Patriotes Day"
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
            name = "Canada Day"
            self[date(year, 7, 1)] = name
            if self.observed and date(year, 7, 1).weekday() in (5, 6):
                self[date(year, 7, 1) + rd(weekday=MO)] = name + " (Observed)"
        elif year >= 1867:
            name = "Memorial Day"
            self[date(year, 7, 1)] = name
            if self.observed and date(year, 7, 1).weekday() in (5, 6):
                self[date(year, 7, 1) + rd(weekday=MO)] = name + " (Observed)"

        # Nunavut Day
        if self.prov == 'NU' and year >= 2001:
            self[date(year, 7, 9)] = "Nunavut Day"
            if self.observed and date(year, 7, 9).weekday() == 6:
                self[date(year, 7, 10)] = "Nunavut Day (Observed)"
        elif self.prov == 'NU' and year == 2000:
            self[date(2000, 4, 1)] = "Nunavut Day"

        # Civic Holiday
        if self.prov in ('SK', 'ON', 'MB', 'NT') and year >= 1900:
            self[date(year, 8, 1) + rd(weekday=MO)] = "Civic Holiday"
        elif self.prov in ('BC') and year >= 1974:
            self[date(year, 8, 1) + rd(weekday=MO)] = "British Columbia Day"

        # Labour Day
        if year >= 1894:
            self[date(year, 9, 1) + rd(weekday=MO)] = "Labour Day"

        # Thanksgiving
        if self.prov not in ('NB', 'NS', 'PE', 'NL') and year >= 1931:
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


class UnitedStates(HolidayBase):

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
            # The next year's observed New Year's Day can be in this year
            # when it falls on a Friday (Jan 1st is a Saturday)
            if self.observed and date(year, 12, 31).weekday() == 4:
                self[date(year, 12, 31)] = name + " (Observed)"

        # Martin Luther King, Jr. Day
        if year >= 1986:
            name = "Martin Luther King, Jr. Day"
            self[date(year, 1, 1) + rd(weekday=MO(+3))] = name

        # Washington's Birthday
        name = "Washington's Birthday"
        if year > 1970:
            self[date(year, 2, 1) + rd(weekday=MO(+3))] = name
        elif year >= 1879:
            self[date(year, 2, 22)] = name

        # Memorial Day
        if year > 1970:
            self[date(year, 5, 31) + rd(weekday=MO(-1))] = "Memorial Day"
        elif year >= 1888:
            self[date(year, 5, 30)] = "Memorial Day"

        # Independence Day
        if year > 1870:
            name = "Independence Day"
            self[date(year, 7, 4)] = name
            if self.observed and date(year, 7, 4).weekday() == 5:
                self[date(year, 7, 4) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 7, 4).weekday() == 6:
                self[date(year, 7, 4) + rd(days=+1)] = name + " (Observed)"

        # Labor Day
        if year >= 1894:
            self[date(year, 9, 1) + rd(weekday=MO)] = "Labor Day"

        # Columbus Day
        if year >= 1970:
            self[date(year, 10, 1) + rd(weekday=MO(+2))] = "Columbus Day"
        elif year >= 1937:
            self[date(year, 10, 12)] = "Columbus Day"

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

        # Thanksgiving
        if year > 1870:
            self[date(year, 11, 1) + rd(weekday=TH(+4))] = "Thanksgiving"

        # Christmas Day
        if year > 1870:
            name = "Christmas Day"
            self[date(year, 12, 25)] = "Christmas Day"
            if self.observed and date(year, 12, 25).weekday() == 5:
                self[date(year, 12, 25) + rd(days=-1)] = name + " (Observed)"
            elif self.observed and date(year, 12, 25).weekday() == 6:
                self[date(year, 12, 25) + rd(days=+1)] = name + " (Observed)"


class US(UnitedStates):
    pass
