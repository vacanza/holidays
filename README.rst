===============
python-holidays
===============

A fast, efficient Python library for generating country, province and state
specific sets of holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.

.. image:: https://github.com/dr-prodigy/python-holidays/workflows/Tests/badge.svg
    :target: https://github.com/dr-prodigy/python-holidays/actions

.. image:: http://img.shields.io/coveralls/dr-prodigy/python-holidays/master
    :target: https://coveralls.io/r/dr-prodigy/python-holidays

.. image:: http://img.shields.io/pypi/v/holidays.svg
    :target: https://pypi.python.org/pypi/holidays

.. image:: http://img.shields.io/pypi/l/holidays.svg
    :target: https://github.com/dr-prodigy/python-holidays/blob/master/LICENSE

.. image:: https://readthedocs.org/projects/python-holidays/badge/?version=latest
    :target: https://python-holidays.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


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

.. _ISO 3166-1 alpha-2 code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

The standard way to refer to a country is by using its
`ISO 3166-1 alpha-2 code`_, the same used for domain names. The
following countries and their subdivisions are available:

===================== ===== ====================================================
Country               Code  Subdivisions Available
===================== ===== ====================================================
Angola                AO    None
Argentina             AR    None
Aruba                 AW    None
Australia             AU    prov = **ACT** (default), NSW, NT, QLD, SA, TAS,
                            VIC, WA
Austria               AT    prov = 1, 2, 3, 4, 5, 6, 7, 8, **9** (default)
Azerbaijan            AZ    None
Bangladesh            BD    None
Belarus               BY    None
Belgium               BE    None
Botswana              BW    None
Brazil                BR    state = AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG,
                            MS, MT, PA, PB, PE, PI, RJ, RN, RO, RR, RS, SC, SE,
                            SP, TO
Bulgaria              BG    None
Burundi               BI    None
Canada                CA    prov = AB, BC, MB, NB, NL, NS, NT, NU, **ON**
                            (default), PE, QC, SK, YU
Chile                 CL    state = AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA,
                            ML, NB, RM, TA, VS
China                 CN    None
Colombia              CO    None
Croatia               HR    None
Curacao               CW    None
Czechia               CZ    None
Denmark               DK    None
Djibouti              DJ    None
Dominican Republic    DO    None
Egypt                 EG    None
Estonia               EE    None
Ethiopia              ET    None
Finland               FI    None
France                FR    prov = **Métropole** (default), Alsace-Moselle,
                            Guadeloupe, Guyane, Martinique, Mayotte,
                            Nouvelle-Calédonie, La Réunion, Polynésie
                            Française, Saint-Barthélémy, Saint-Martin,
                            Wallis-et-Futuna
Georgia               GE    None
Germany               DE    prov = BB, BE, BW, BY, BYP, HB, HE, HH, MV, NI, NW,
                            RP, SH, SL, SN, ST, TH
Greece                GR    None
Honduras              HN    None
Hong Kong             HK    None
Hungary               HU    None
Iceland               IS    None
India                 IN    prov = AP, AS, BR, CG, GJ, HR, KA, KL, MH, MP, OD,
                            RJ, SK, TN, TN, UK, UP, WB
Ireland               IE    None
Israel                IL    None
Italy                 IT    prov = AN, AO, BA, BL, BO, BS, BZ, CB, CH, CS, CT,
                            EN, FC, FE, FI, FR, GE, GO, IS, KR, LT, MB, MI, MO
                            MN, MS, NA, PA, PC, PD, PG, PR, RM, SP, TS, VI,
                            Cesena, Forlì
Jamaica               JM    None
Japan                 JP    None
Kazakhstan            KZ    None
Kenya                 KE    None
Korea                 KR    None
Latvia                LV    None
Lesotho               LS    None
Lithuania             LT    None
Luxembourg            LU    None
Malaysia              MY    state = JHR, KDH, KTN, MLK, NSN, PHG, PNG, PRK, PLS,
                            SBH, SWK, SGR, TRG, KUL, LBN, PJY
Malawi                MW    None
Mexico                MX    None
Morocco               MA    None
Mozambique            MZ    None
Netherlands           NL    None
Namibia               NA    None
New Zealand           NZ    prov = AUK, CAN, CIT, HKB, MBH, NSN, NTL, OTA, STC,
                            STL, TKI, WGN, WTL
Nicaragua             NI    prov = MN
Nigeria               NG    None
North Macedonia       MK    None
Norway                NO    None
Paraguay              PY    None
Peru                  PE    None
Poland                PL    None
Portugal              PT    None
Portugal (Extended)   PTE   *Portugal plus days most people have off*
Romania               RO    None
Russia                RU    None
Saudi Arabia          SA    None
Serbia                RS    None
Singapore             SG    None
Slovakia              SK    None
Slovenia              SI    None
South Africa          ZA    None
Spain                 ES    prov = AN (Andalucía), AR (Aragón), AS (Asturias),
                            CB (Cantabria), CE (Ceuta), CL (Castilla y León),
                            CM (Castilla La Mancha), CN (Canarias), CT (Cataluña),
                            EX (Extremadura), GA (Galicia), IB (Islas Baleares),
                            MC (Murcia), MD (Madrid), NC (Navarra), PV (País Vasco),
                            RI (La Rioja), VC (Comunidad Valenciana)
Swaziland             SZ    None
Sweden                SE    None
Switzerland           CH    prov = AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU,
                            LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS,
                            ZG, ZH
Taiwan                TW    None
Turkey                TR    None
Tunisia               TN    None
Ukraine               UA    None
United Arab Emirates  AE    None
United Kingdom        GB    state = England, Isle of Man, Northern Ireland,
                            Scotland, Wales
United Kingdom        UK    *Deprecated alias for GB*
United States         US    state = AL, AK, AS, AZ, AR, CA, CO, CT, DE, DC, FL,
                            GA, GU, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MH
                            MA, MI, FM, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY,
                            NC, ND, MP, OH, OK, OR, PW, PA, PR, RI, SC, SD, TN,
                            TX, UT, VT, VA, VI, WA, WV, WI, WY
Venezuela             VE    None
Vietnam               VN    None
Zambia                ZM    None
Zimbabwe              ZW    None
===================== ===== ====================================================

    # The ``observed`` and ``expand`` values can both be changed on the fly and the
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

    # Holidays can be retrieved using their name too.
    # ``get_named(key)`` receives a string and returns a list of holidays
    # matching it (even partially, with case insensitive check)

    >>> us_holidays = holidays.UnitedStates(years=2020)
    >>> us_holidays.get_named('day')
    [datetime.date(2020, 1, 1), datetime.date(2020, 1, 20),
    datetime.date(2020, 2, 17), datetime.date(2020, 5, 25),
    datetime.date(2020, 7, 4), datetime.date(2020, 7, 3),
    datetime.date(2020, 9, 7), datetime.date(2020, 10, 12),
    datetime.date(2020, 11, 11), datetime.date(2020, 12, 25)]

    # Sometimes we may not be able to use the official federal statutory
    # holiday list in our code. Let's pretend we work for a company that
    # does not include Columbus Day as a statutory holiday but does include
    # "Ninja Turtle Day" on July 13th. We can create a new class that inherits
    # the UnitedStates class and the only method we need to override is _populate()

    >>> class CorporateHolidays(holidays.UnitedStates):
    >>>     def _populate(self, year):
    >>>         # Populate the holiday list with the default US holidays
    >>>         holidays.UnitedStates._populate(self, year)
    >>>         # Remove Columbus Day
    >>>         self.pop_named("Columbus Day")
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

    >>> custom_holidays = holidays.HolidayBase()
    >>> custom_holidays.append(['2015-01-01', '07/04/2015'])
    >>> custom_holidays.append(date(2015, 12, 25))


>>> from datetime import date
>>> holidays.US()[date(2013, 12, 31): date(2014, 1, 2)]

# Intermediate years are only shown if they are listed in the years parameter.

>>> holidays.US(years=[2014])[datetime.date(2013, 1, 1): datetime.date(2015, 12, 31)]

Development Version
-------------------

The latest development (beta) version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade https://github.com/dr-prodigy/python-holidays/tarball/beta

All new features are always first pushed to beta branch, then released on
master branch upon official version upgrades.

Running Tests and Coverage
--------------------------

Project provides automated tests and coverage checks with pytest. Here is the
commands to execute them.

.. code-block:: bash

    $ pip install -r requirements_dev.txt
    $ python -m pytest .

Or, if you want to retrieve uncovered lines too

.. code-block:: bash

    $ python -m pytest --cov-report term-missing .


Ensure all staged files are up to standard
------------------------------------------

.. _pre-commit: https://github.com/dr-prodigy/python-holidays/issues

Install the githooks with `pre-commit`_, after that the quality assurance
tests will run on all staged files before you commit them and intercept
the commit if the staged files aren't up to standard.

.. code-block:: bash

    $ pre-commit install

Manually run the quality assurance tests on all tracked files.

.. code-block:: bash

    $ pre-commit run -a


Build sphinx documentation
--------------------------

.. _readthedocs.io: https://python-holidays.readthedocs.io/en/latest/

Project provides a sphinx documentation source under ./docs/source, published
online on `readthedocs.io`_.
To test/build locally the documentation in html, run this command:

.. code-block:: bash

    $ sphinx-build -b html docs/source/ docs/build/html


Contributions
-------------

.. _issues: https://github.com/dr-prodigy/python-holidays/issues
.. __: https://github.com/dr-prodigy/python-holidays/pulls
.. _`beta branch`: https://github.com/dr-prodigy/python-holidays/tree/beta

Issues_ and `Pull Requests`__ are always welcome.

When contributing with fixes and new features, please start forking/branching
from `beta branch`_, to work on latest code and reduce merging issues.

Contributed PR are required to include valid test coverage **(95%
minimum, 100% whenever possible)** in order to be merged.

Thanks a lot for your support.

License
-------

.. __: https://github.com/dr-prodigy/python-holidays/raw/master/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
