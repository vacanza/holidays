# -*- coding: utf-8 -*-

#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)
#  Version: 0.4 (October 4, 2015)


from datetime import date, datetime
from dateutil.easter import easter
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA
import six


__version__ = '0.4'


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
            key = datetime.fromtimestamp(key).date()
        elif isinstance(key, six.string_types):
            try:
                key = parse(key).date()
            except:
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
        return (dict.__eq__(self, other) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return (dict.__ne__(self, other) or self.__dict__ != other.__dict__)

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
            if self.state != 'GA' or year < 2012:
                self[date(year, 1, 1) + rd(weekday=MO(+3))] = name

        # Lincoln's Birthday
        name = "Lincoln's Birthday"
        if (self.state in ('CT', 'IL', 'IA', 'NJ', 'NY') and year >= 1971) \
                or (self.state == 'CA' and year >= 1971 and year <= 2009):
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
        if self.state == 'IN' and ((year >= 2006 and year % 2 == 0)
                                   or year >= 2015):
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
        if (self.state in
                ('DE', 'HI', 'IL', 'IN', 'LA', 'MT', 'NH', 'NJ', 'NY', 'WV')
                and year >= 2008 and year % 2 == 0) \
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
        if (self.state in ('DE', 'FL', 'NH', 'NC', 'OK', 'TX', 'WV') and year >= 1975) \
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
        if self.state == 'GA' and year >= 2012:
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
                    self[date(year, 10, 1)] = name
                    self[date(year, 6, 11)] = "Queen's Diamond Jubilee"
                else:
                    dt = date(year, 6, 1) + rd(weekday=MO(+2))
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
