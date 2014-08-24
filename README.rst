===========
holidays.py
===========

Holidays is a fast, efficient Python library for generating country-specific
sets of holidays on the fly. It aims to make determining whether a specific
date is a holiday as fast and flexible as possible.


Example Usage
-------------

.. code-block:: python

    >>> from holidays import Holidays
    >>> us_holidays = Holidays(country='US')
    >>> date(2014,1,1) in us_holidays
    True
    >>> date(2014,1,2) in us_holidays
    False
    >>> us_holidays[date(2014,1,1)]
    "New Year's Day"
    >>> '2014-01-01' in us_holidays
    True
    >>> '1/1/2014' in us_holidays
    True
    >>>1388597445 in us_holidays  # Unix timestamp
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

=============   ==========  ======================================================
Country         Param Abbr  Prov/State Options
=============   ==========  ======================================================
Canada          "CA"        AB, BC, MB, NB, NL, NS, NT, NU, **ON**, PE, QC, SK, YU
United States   "US"        None
=============   ==========  ======================================================


API
---

class holidays.Holiday(country="US", prov=None, years=[], expand=True, observed=True)
    The main Holiday class used to create holiday list objects.

Parameters:

country
    A string representing the country to generate the holidays for. (Default: "US")

prov
    A string specifying a prov/state within *country* that has unique statutory
    holidays. (Default: CA->ON, US->None)

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


More Examples
-------------

.. code-block:: python

    # Simplest example possible

    >>> from holidays import Holidays
    >>> date(2014,1,1) in Holidays(country='US')
    True
    >> date(2014,1,2) in Holidays(country='US')
    False

    # But this is not efficient because it is initializing a new Holiday object
    # and generating a list of all the holidays in 2014 during each comparison

    # It is more efficient to create the object only once

    >>> us_holidays = Holidays(country='US')
    >>> date(2014,1,1) in us_holidays
    True
    >> date(2014,1,2) in us_holidays
    False


    # So far we've only checked holidays in 2014 so that's the only year the
    # Holidays object has generated

    >>> us_holidays.years
    set([2014])
    >>> len(us_holidays)
    10

    # Because by default the `expand` param is True the Holiday object will add
    # holidays from other years as they are required.

    >>> date(2013,1,1) in us_holidays
    True
    >>> us_holidays.years
    set([2013,2014])
    >>> len(us_holidays)
    20

    # If we change the `expand` param to False the Holiday object will no longer
    # add holidays from new years

    >>> us_holidays.expand = False
    >>> date(2013,1,1) in us_holidays
    False
    >>> us.holidays.expand = True
    >>> date(2013,1,1) in us_holidays
    True

    # January 1st, 2012 fell on a Sunday so the statutory holiday was observed on
    # the 2nd. By default the `observed` param is True so the holiday list will
    # include January 2nd, 2012 as a holiday.

    >>> date(2012,1,1) in us_holidays
    True
    >>> us_holidays[date(2012,1,1)]
    "New Year's Eve"
    >>> date(2012,1,2) in us_holidays
    True
    >>> us_holidays.get(date(2012,1,2))
    "New Year's Eve (Observed)"

    # The `observed` and `expand` values can both be changed on the fly and the
    # holiday list will be adjusted accordingly

    >>> us_holidays.observed = False
    >>> date(2012,1,2) in us_holidays
    False
    us_holidays.observed = True
    >> date(2012,1,2) in us_holidays
    True

    # Sometimes you may not be able to use the official federal statutory
    # holiday list in your code. Let's pretend you work for a company that
    # does not include Columbus Day as a statutory holiday but does include
    # "Ninja Turtle Day" on July 13th. We can create a new class that inherits
    # the Holidays class and the only method we need to override is _populate()

    >>> from dateutil.relativedelta import relativedelta
    >>> class CorporateHolidays(Holidays):
    >>>     def _populate(self, year):
    >>>         # Populate the holiday list with the default US holidays
    >>>         # If you are creating a brand new holiday list you would
    >>>         # skip this line
    >>>         Holidays._populate(self, year)
    >>>         # Remove Columbus Day
    >>>         self.pop(date(year,10,1)+relativedelta(weekday=MO(+2)), None)
    >>>         # Add Ninja Turtle Day
    >>>         self[date(year,7,13)] = "Ninja Turtle Day"
    >>> date(2014,10,14) in Holidays(country="US")
    True
    >>> date(2014,10,14) in CorporateHolidays(country="US")
    False
    >>> date(2014,7,13) in Holidays(country="US")
    False
    >>> date(2014,7,13) in CorporateHolidays(country="US")
    True

    # If you write the code necessary to create a holiday list for a country not
    # not currently supported please contribute your code to the project!


Development Version
-------------------

The latest development version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade https://github.com/ryanss/holidays.py/tarball/master


Running Tests
-------------

.. code-block:: bash

    $ python tests.py


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
