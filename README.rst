===============
python-holidays
===============

A fast, efficient Python library for generating country, province and state
specific sets of holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.

.. image:: http://img.shields.io/travis/dr-prodigy/python-holidays.svg
    :target: https://travis-ci.org/dr-prodigy/python-holidays

.. image:: http://img.shields.io/coveralls/dr-prodigy/python-holidays.svg
    :target: https://coveralls.io/r/dr-prodigy/python-holidays

.. image:: http://img.shields.io/pypi/v/holidays.svg
    :target: https://pypi.python.org/pypi/holidays

.. image:: http://img.shields.io/pypi/l/holidays.svg
    :target: https://github.com/dr-prodigy/python-holidays/blob/master/LICENSE


Example Usage
-------------

.. code-block:: python

    from datetime import date

    import holidays

    us_holidays = holidays.UnitedStates()
    # or:
    # us_holidays = holidays.US()
    # or:
    # us_holidays = holidays.CountryHoliday('US')
    # or, for specific prov / states:
    # us_holidays = holidays.CountryHoliday('US', prov=None, state='CA')

    date(2015, 1, 1) in us_holidays  # True
    date(2015, 1, 2) in us_holidays  # False

    # The Holiday class will also recognize strings of any format
    # and int/float representing a Unix timestamp
    '2014-01-01' in us_holidays  # True
    '1/1/2014' in us_holidays    # True
    1388597445 in us_holidays    # True

    us_holidays.get('2014-01-01')  # "New Year's Day"

    us_holidays['2014-01-01': '2014-01-03']  # [date(2014, 1, 1)]

    us_pr_holidays = holidays.UnitedStates(state='PR')  # or holidays.US(...), or holidays.CountryHoliday('US', state='PR')

    # some holidays are only present in parts of a country
    '2018-01-06' in us_holidays     # False
    '2018-01-06' in us_pr_holidays  # True

    # Easily create custom Holiday objects with your own dates instead
    # of using the pre-defined countries/states/provinces available
    custom_holidays = holidays.HolidayBase()
    # Append custom holiday dates by passing:
    # 1) a dict with date/name key/value pairs,
    custom_holidays.append({"2015-01-01": "New Year's Day"})
    # 2) a list of dates (in any format: date, datetime, string, integer),
    custom_holidays.append(['2015-07-01', '07/04/2015'])
    # 3) a single date item
    custom_holidays.append(date(2015, 12, 25))

    date(2015, 1, 1) in custom_holidays  # True
    date(2015, 1, 2) in custom_holidays  # False
    '12/25/2015' in custom_holidays      # True

    # For more complex logic like 4th Monday of January, you can inherit the
    # HolidayBase class and define your own _populate(year) method. See below
    # documentation for examples.


Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install holidays

If the above fails, please use easy_install instead:

.. code-block:: bash

    $ easy_install holidays


Available Countries
-------------------

=================== ======== =============================================================
Country             Abbr     Provinces/States Available
=================== ======== =============================================================
Argentina           AR       None
Aruba               AW       None
Australia           AU       prov = **ACT** (default), NSW, NT, QLD, SA, TAS, VIC, WA
Austria             AT       prov = B, K, N, O, S, ST, T, V, **W** (default)
Belarus             BY       None
Belgium             BE       None
Brazil              BR       state = AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG,
                             PA, PB, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO
Bulgaria            BG       None
Canada              CA       prov = AB, BC, MB, NB, NL, NS, NT, NU, **ON** (default),
                             PE, QC, SK, YU
Colombia            CO       None
Croatia             HR       None
Czechia             CZ       None
Denmark             DK       None
England                      None
Estonia             EE       None
EuropeanCentralBank ECB,TAR  Trans-European Automated Real-time Gross Settlement (TARGET2)
Finland             FI       None
France              FRA      **Métropole** (default), Alsace-Moselle, Guadeloupe, Guyane,
                             Martinique, Mayotte, Nouvelle-Calédonie, La Réunion,
                             Polynésie Française, Saint-Barthélémy, Saint-Martin,
                             Wallis-et-Futuna
Germany             DE       prov = BW, BY, BE, BB, HB, HH, HE, MV, NI, NW, RP, SL, SN,
                             ST, SH, TH
Hungary             HU       None
Iceland             IS       None
India               IND      prov = AS, SK, CG, KA, GJ, BR, RJ, OD, TN, AP, WB, KL, HR,
                             MH, MP, UP, UK, TN
Ireland             IE       None
IsleOfMan                    None
Italy               IT       prov = AN, AO, BA, BL, BO, BS, BZ, CB, Cesena, CH, CS, CT,
                             EN, FC, FE, FI, Forlì, FR, GE, GO, IS, KR, LT, MB, MI, MO,
                             MN, MS, NA, PA, PC, PD, PG, PR, RM, SP, TS, VI
Japan               JP       None
Kenya               KE       None
Lithuania           LT       None
Luxembourg          LU       None
Mexico              MX       None
Netherlands         NL       None
NewZealand          NZ       prov = NTL, AUK, TKI, HKB, WGN, MBH, NSN, CAN, STC, WTL,
                             OTA, STL, CIT
Northern Ireland             None
Norway              NO       None
Peru                PE       None
Poland              PL       None
Portugal            PT       None
PortugalExt         PTE      *Portugal plus extended days most people have off*
Russia              RU       None
Scotland                     None
Slovakia            SK       None
Slovenia            SI       None
South Africa        ZA       None
Spain               ES       prov = AND, ARG, AST, CAN, CAM, CAL, CAT, CVA, EXT, GAL,
                             IBA, ICA, MAD, MUR, NAV, PVA, RIO
Sweden              SE       None
Switzerland         CH       prov = AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU, LU,
                             NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
Ukraine             UA       None
UnitedKingdom       UK       None
UnitedStates        US       state = AL, AK, AS, AZ, AR, CA, CO, CT, DE, DC, FL, GA,
                             GU, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MH, MA, MI,
                             FM, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, MP,
                             OH, OK, OR, PW, PA, PR, RI, SC, SD, TN, TX, UT, VT, VA,
                             VI, WA, WV, WI, WY
Wales                        None
=================== ======== =============================================================


API
---

class holidays.HolidayBase(years=[], expand=True, observed=True, prov=None, state=None)
    The base class used to create holiday country classes.

Parameters:

years
    An iterable list of integers specifying the years that the Holiday object
    should pre-generate. This would generally only be used if setting *expand*
    to False. (Default: [])

expand
    A boolean value which specifies whether or not to append holidays in new
    years to the holidays object. (Default: True)

observed
    A boolean value which when set to True will include the observed day of a
    holiday that falls on a weekend, when appropriate. (Default: True)

prov
    A string specifying a province that has unique statutory holidays.
    (Default: Australia='ACT', Canada='ON', NewZealand=None)

state
    A string specifying a state that has unique statutory holidays.
    (Default: UnitedStates=None)

Methods:

get(key, default=None)
    Returns a string containing the name of the holiday(s) in date `key`, which
    can be of date, datetime, string, unicode, bytes, integer or float type. If
    multiple holidays fall on the same date the names will be separated by
    commas

get_list(key)
    Same as `get` except returns a `list` of holiday names instead of a comma
    separated string

pop(key, default=None)
    Same as `get` except the key is removed from the holiday object

update/append
    Accepts dictionary of {date: name} pairs, a list of dates, or even singular
    date/string/timestamp objects and adds them to the list of holidays


More Examples
-------------

.. code-block:: python

    # Simplest example possible

    >>> from datetime import date
    >>> import holidays
    >>> date(2014, 1, 1) in holidays.US()
    True
    >> date(2014, 1, 2) in holidays.US()
    False

    # But this is not efficient because it is initializing a new Holiday object
    # and generating a list of all the holidays in 2014 during each comparison

    # It is more efficient to create the object only once

    >>> us_holidays = holidays.US()
    >>> date(2014, 1, 1) in us_holidays
    True
    >> date(2014, 1, 2) in us_holidays
    False

    # Each country has two class names that can be called--a full name
    # and an abbreviation. Use whichever you prefer.

    >>> holidays.UnitedStates() == holidays.US()
    True
    >>> holidays.Canada() == holidays.CA()
    True
    >>> holidays.US() == holidays.CA()
    False

    # Let's print out the holidays in 2014 specific to California, USA

    >>> for date, name in sorted(holidays.US(state='CA', years=2014).items()):
    >>>     print(date, name)
    2014-01-01 New Year's Day
    2014-01-20 Martin Luther King, Jr. Day
    2014-02-15 Susan B. Anthony Day
    2014-02-17 Washington's Birthday
    2014-03-31 César Chávez Day
    2014-05-26 Memorial Day
    2014-07-04 Independence Day
    2014-09-01 Labor Day
    2014-10-13 Columbus Day
    2014-11-11 Veterans Day
    2014-11-27 Thanksgiving
    2014-12-25 Christmas Day

    # So far we've only checked holidays in 2014 so that's the only year the
    # Holidays object has generated

    >>> us_holidays.years
    set([2014])
    >>> len(us_holidays)
    10

    # Because by default the `expand` param is True the Holiday object will add
    # holidays from other years as they are required.

    >>> date(2013, 1, 1) in us_holidays
    True
    >>> us_holidays.years
    set([2013, 2014])
    >>> len(us_holidays)
    20

    # If we change the `expand` param to False the Holiday object will no longer
    # add holidays from new years

    >>> us_holidays.expand = False
    >>> date(2012, 1, 1) in us_holidays
    False
    >>> us.holidays.expand = True
    >>> date(2012, 1, 1) in us_holidays
    True

    # January 1st, 2012 fell on a Sunday so the statutory holiday was observed
    # on the 2nd. By default the `observed` param is True so the holiday list
    # will include January 2nd, 2012 as a holiday.

    >>> date(2012, 1, 1) in us_holidays
    True
    >>> us_holidays[date(2012, 1, 1)]
    "New Year's Eve"
    >>> date(2012, 1, 2) in us_holidays
    True
    >>> us_holidays.get(date(2012 ,1, 2))
    "New Year's Eve (Observed)"

    # The `observed` and `expand` values can both be changed on the fly and the
    # holiday list will be adjusted accordingly

    >>> us_holidays.observed = False
    >>> date(2012, 1, 2) in us_holidays
    False
    us_holidays.observed = True
    >> date(2012, 1, 2) in us_holidays
    True

    # Holiday objects can be added together and the resulting object will
    # generate the holidays from all of the initial objects

    >>> north_america = holidays.CA() + holidays.US() + holidays.MX()
    >>> north_america.get('2014-07-01')
    "Canada Day"
    >>> north_america.get('2014-07-04')
    "Independence Day"

    # The other form of addition is also available

    >>> north_america = holidays.Canada()
    >>> north_america += holidays.UnitedStates()
    >>> north_america += holidays.Mexico()
    >>> north_america.country
    ['CA', 'US', 'MX']

    # We can even get a set of holidays that include all the province- or
    # state-specific holidays using the built-in sum() function
    >>> a = sum([holidays.CA(prov=x) for x in holidays.CA.PROVINCES])
    >>> a.prov
    PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE',
                 'QC', 'SK', 'YU']

    # Sometimes we may not be able to use the official federal statutory
    # holiday list in our code. Let's pretend we work for a company that
    # does not include Columbus Day as a statutory holiday but does include
    # "Ninja Turtle Day" on July 13th. We can create a new class that inherits
    # the UnitedStates class and the only method we need to override is _populate()

    >>> from dateutil.relativedelta import relativedelta
    >>> class CorporateHolidays(holidays.UnitedStates):
    >>>     def _populate(self, year):
    >>>         # Populate the holiday list with the default US holidays
    >>>         holidays.UnitedStates._populate(self, year)
    >>>         # Remove Columbus Day
    >>>         self.pop(date(year, 10, 1) + relativedelta(weekday=MO(+2)), None)
    >>>         # Add Ninja Turtle Day
    >>>         self[date(year, 7, 13)] = "Ninja Turtle Day"
    >>> date(2014, 10, 14) in Holidays(country="US")
    True
    >>> date(2014, 10, 14) in CorporateHolidays(country="US")
    False
    >>> date(2014, 7, 13) in Holidays(country="US")
    False
    >>> date(2014 ,7, 13) in CorporateHolidays(country="US")
    True

    # We can also inherit from the HolidayBase class which has an empty
    # _populate method so we start with no holidays and must define them
    # all ourselves. This is how we would create a holidays class for a country
    # that is not supported yet.

    >>> class NewCountryHolidays(holidays.HolidayBase):
    >>>     def _populate(self, year):
    >>>         self[date(year, 1, 2)] = "Some Federal Holiday"
    >>>         self[date(year, 2, 3)] = "Another Federal Holiday"
    >>> hdays = NewCountryHolidays()

    # We can also include prov/state specific holidays in our new class.

    >>> class NewCountryHolidays(holidays.HolidayBase):
    >>>     def _populate(self, year):
    >>>         # Set default prov if not provided
    >>>         if self.prov == None:
    >>>             self.prov = 'XX'
    >>>         self[date(year, 1, 2)] = "Some Federal Holiday"
    >>>         if self.prov == 'XX':
    >>>             self[date(year, 2, 3)] = "Special XX province-only holiday"
    >>>         if self.prov == 'YY':
    >>>             self[date(year, 3, 4)] = "Special YY province-only holiday"
    >>> hdays = NewCountryHolidays()
    >>> hdays = NewCountryHolidays(prov='XX')

    # If you write the code necessary to create a holiday class for a country
    # not currently supported please contribute your code to the project!

    # Perhaps you just have a list of dates that are holidays and want to turn
    # them into a Holiday class to access all the useful functionality. You can
    # use the append() method which accepts a dictionary of {date: name} pairs,
    # a list of dates, or even singular date/string/timestamp objects.

    >>> custom_holidays = holidays.HolidaysBase()
    >>> custom_holidays.append(['2015-01-01', '07/04/2015'])
    >>> custom_holidays.append(date(2015, 12, 25))


>>> from datetime import date
>>> holidays.US()[date(2013, 12, 31): date(2014, 1, 2)]

Development Version
-------------------

The latest development (beta) version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade https://github.com/dr-prodigy/python-holidays/tarball/beta

All new features are always first pushed to beta branch, then released on
master branch upon official version upgrades.

Running Tests
-------------

.. code-block:: bash

    $ pip install flake8
    $ flake8 holidays.py tests.py
    $ python tests.py


Coverage
--------

.. code-block:: bash

    $ pip install coverage
    $ coverage run --omit=*site-packages* tests.py
    $ coverage report -m


Contributions
-------------

.. _issues: https://github.com/dr-prodigy/python-holidays/issues
.. __: https://github.com/dr-prodigy/python-holidays/pulls
.. _`beta branch`: https://github.com/dr-prodigy/python-holidays/tree/beta

Issues_ and `Pull Requests`__ are always welcome.

When contributing with fixes and new features, please start forking/branching
from `beta branch`_, to work on latest code and reduce merging issues.

Also, whenever possible, please provide 100% test coverage for your new code.

Thanks a lot for your support.

License
-------

.. __: https://github.com/dr-prodigy/python-holidays/raw/master/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
