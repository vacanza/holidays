===========
holidays.py
===========

Holidays is a fast, efficient Python library for generating country-specific
sets of holidays on the fly. It aims to make determining whether a specific
date is a holiday as fast and flexible as possible.

.. image:: http://img.shields.io/travis/ryanss/holidays.py.svg
    :target: https://travis-ci.org/ryanss/holidays.py

.. image:: http://img.shields.io/coveralls/ryanss/holidays.py.svg
    :target: https://coveralls.io/r/ryanss/holidays.py

.. image:: http://img.shields.io/pypi/v/holidays.svg
    :target: https://pypi.python.org/pypi/holidays

.. image:: http://img.shields.io/pypi/dm/holidays.svg
    :target: https://pypi.python.org/pypi/holidays

.. image:: http://img.shields.io/pypi/l/holidays.svg
    :target: https://github.com/ryanss/holidays.py/blob/master/LICENSE


Example Usage
-------------

.. code-block:: python

    >>> import holidays
    >>> us_holidays = holidays.US()  # or holidays.UnitedStates()
    >>> date(2014, 1, 1) in us_holidays
    True
    >>> date(2014, 1, 2) in us_holidays
    False
    >>> us_holidays[date(2014, 1, 1)]
    "New Year's Day"
    >>> '2014-01-01' in us_holidays
    True
    >>> '1/1/2014' in us_holidays
    True
    >>> 1388597445 in us_holidays  # Unix timestamp
    True


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

============ ====  ======================================================
Country      Abbr  Prov/State Options
============ ====  ======================================================
Australia    AU    **ACT**, NSW, NT, QLD, SA, TAS, VIC, WA
Canada       CA    AB, BC, MB, NB, NL, NS, NT, NU, **ON**, PE, QC, SK, YU
Mexico       MX    None
NewZealand   NZ    NTL, AUK, TKI, HKB, WGN, MBH, NSN, CAN, STC, WTL, OTA, STL, CIT
UnitedStates US    None
============ ====  ======================================================


API
---

class holidays.HolidayBase(years=[], expand=True, observed=True, prov=None)
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
    A string specifying a province/state that has unique statutory holidays.
    (Default: Canada='ON', Mexico=None, UnitedStates=None)


More Examples
-------------

.. code-block:: python

    # Simplest example possible

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
    # generate the holidays from both of the initial objects

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
    # all ourself. This is how we would create a holidays class for a country
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


Development Version
-------------------

The latest development version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade https://github.com/ryanss/holidays.py/tarball/master


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
    $ coverage report


Contributions
-------------

.. _issues: https://github.com/ryanss/holidays.py/issues
.. __: https://github.com/ryanss/holidays.py/pulls

Issues_ and `Pull Requests`__ are always welcome.


License
-------

.. __: https://github.com/ryanss/holidays.py/raw/master/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
