===============
python-holidays
===============

A fast, efficient Python library for generating country- and subdivision- (e.g.
state or province) specific sets of government-designated holidays on the fly.
It aims to make determining whether a specific date is a holiday as fast and
flexible as possible.

:Package:
    .. image:: https://img.shields.io/pypi/pyversions/holidays.svg?logo=python&label=Python&logoColor=gold
        :target: https://pypi.python.org/pypi/holidays
        :alt: Python supported versions

    .. image:: http://img.shields.io/pypi/v/holidays.svg?logo=pypi&label=PyPI&logoColor=gold
        :target: https://pypi.python.org/pypi/holidays
        :alt: PyPI version

    .. image:: https://img.shields.io/pypi/dm/holidays.svg?color=blue&label=Downloads&logo=pypi&logoColor=gold
        :target: https://pypi.python.org/pypi/holidays
        :alt: Downloads

:CD/CI:
    .. image:: https://github.com/dr-prodigy/python-holidays/workflows/Tests/badge.svg
        :target: actions

    .. image:: http://img.shields.io/coveralls/dr-prodigy/python-holidays/master
        :target: https://coveralls.io/r/dr-prodigy/python-holidays

:Docs:
    .. image:: https://readthedocs.org/projects/python-holidays/badge/?version=latest
        :target: https://python-holidays.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

:Meta:
    .. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :alt: Code style

    .. image:: http://img.shields.io/pypi/l/holidays.svg
        :target: LICENSE
        :alt: License

Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install --upgrade holidays


Documentation
-------------

.. _Read the Docs: https://python-holidays.readthedocs.io/

The documentation is hosted on `Read the Docs`_.


Quick Start
-----------

.. code-block:: python

    from datetime import date
    import holidays

    us_holidays = holidays.US()  # this is a dict
    # the below is the same, but takes a string:
    us_holidays = holidays.country_holidays('US')  # this is a dict

    nyse_holidays = holidays.NYSE()  # this is a dict
    # the below is the same, but takes a string:
    nyse_holidays = holidays.financial_holidays('NYSE')  # this is a dict

    date(2015, 1, 1) in us_holidays  # True
    date(2015, 1, 2) in us_holidays  # False
    us_holidays.get('2014-01-01')  # "New Year's Day"

The HolidayBase dict-like class will also recognize date strings and Unix
timestamps:

.. code-block:: python

    '2014-01-01' in us_holidays  # True
    '1/1/2014' in us_holidays    # True
    1388597445 in us_holidays    # True

Some holidays may be only present in parts of a country:

.. code-block:: python

    us_pr_holidays = holidays.country_holidays('US', subdiv='PR')
    '2018-01-06' in us_holidays     # False
    '2018-01-06' in us_pr_holidays  # True

.. _python-holidays documentation: https://python-holidays.readthedocs.io/

Please see the `python-holidays documentation`_ for additional examples and
detailed information.


Available Countries
-------------------

.. _ISO 3166-1 alpha-2 code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
.. _ISO 3166-2 code: https://en.wikipedia.org/wiki/ISO_3166-2

We currently support 119 country codes. The standard way to refer to a country
is by using its `ISO 3166-1 alpha-2 code`_, the same used for domain names, and
for a subdivision its `ISO 3166-2 code`_. The following countries and
subdivisions are available:

.. list-table::
   :widths: 23 4 83
   :header-rows: 1
   :class: tight-table

   * - Country
     - Code
     - Subdivisions Available
   * - Albania
     - AL
     - None
   * - American Samoa
     - AS
     - None; Can also be loaded as country US, subdivision AS
   * - Andorra
     - AD
     - Parishes: AD-02, AD-03, AD-04, AD-05, AD-06, AD-07, AD-08
   * - Angola
     - AO
     - None
   * - Argentina
     - AR
     - None
   * - Armenia
     - AM
     - None
   * - Aruba
     - AW
     - None
   * - Australia
     - AU
     - States and territories: **ACT** (default), NSW, NT, QLD, SA, TAS, VIC, WA
   * - Austria
     - AT
     - States: 1, 2, 3, 4, 5, 6, 7, 8, **9** (default)
   * - Azerbaijan
     - AZ
     - None
   * - Bahrain
     - BH
     - None
   * - Bangladesh
     - BD
     - None
   * - Belarus
     - BY
     - None
   * - Belgium
     - BE
     - None
   * - Bolivia
     - BO
     - Departments: B, C, H, L, N, O, P, S, T
   * - Bosnia and Herzegovina
     - BA
     - Departments: BD, FBiH, RS
   * - Botswana
     - BW
     - None
   * - Brazil
     - BR
     - States: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO
   * - Bulgaria
     - BG
     - None
   * - Burundi
     - BI
     - None
   * - Canada
     - CA
     - Provinces and territories: AB, BC, MB, NB, NL, NS, NT, NU, **ON** (default), PE, QC, SK, YT
   * - Chile
     - CL
     - Regions: AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA, ML, NB, RM, TA, VS
   * - China
     - CN
     - None
   * - Colombia
     - CO
     - None
   * - Croatia
     - HR
     - None
   * - Cuba
     - CU
     - None
   * - Curacao
     - CW
     - None
   * - Cyprus
     - CY
     - None
   * - Czechia
     - CZ
     - None
   * - Denmark
     - DK
     - None
   * - Djibouti
     - DJ
     - None
   * - Dominican Republic
     - DO
     - None
   * - Egypt
     - EG
     - None
   * - Estonia
     - EE
     - None
   * - Eswatini
     - SZ
     - None
   * - Ethiopia
     - ET
     - None
   * - Finland
     - FI
     - None
   * - France
     - FR
     - Départements: Alsace-Moselle, Guadeloupe, Guyane, La Réunion, Martinique, Mayotte, **Métropole** (default), Nouvelle-Calédonie, Polynésie Française, Saint-Barthélémy, Saint-Martin, Wallis-et-Futuna
   * - Georgia
     - GE
     - None
   * - Germany
     - DE
     - States: BB, BE, BW, BY, BYP, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH
   * - Greece
     - GR
     - None
   * - Guam
     - GU
     - None; Can also be loaded as country US, subdivision GU
   * - Honduras
     - HN
     - None
   * - Hong Kong
     - HK
     - None
   * - Hungary
     - HU
     - None
   * - Iceland
     - IS
     - None
   * - India
     - IN
     - States: AN, AP, AR, AS, BR, CG, CH, DD, DH, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA, LD, MH, ML, MN, MP, MZ, NL, OR, PB, PY, RJ, SK, TN, TR, TS, UK, UP, WB
   * - Indonesia
     - ID
     - None
   * - Ireland
     - IE
     - None
   * - Isle of Man
     - IM
     - None
   * - Israel
     - IL
     - None
   * - Italy
     - IT
     - Provinces: AG, AL, AN, AO, AP, AQ, AR, AT, AV, BA, BG, BI, BL, BN, BO, BR, BS, BT, BZ, CA, CB, CE, CH, CL, CN, CO, CR, CS, CT, CZ, EN, FC, FE, FG, FI, FM, FR, GE, GO, GR, IM, IS, KR, LC, LE, LI, LO, LT, LU, MB, MC, ME, MI, MN, MO, MS, MT, NA, NO, NU, OR, PA, PC, PD, PE, PG, PI, PN, PO, PR, PT, PU, PV, PZ, RA, RC, RE, RG, RI, RM, RN, RO, SA, SI, SO, SP, SR, SS, SU, SV, TA, TE, TN, TO, TP, TR, TS, TV, UD, VA, VB, VC, VE, VI, VR, VT, VV. Cities: Andria, Barletta, Cesena, Forlì, Pesaro, Trani, Urbino
   * - Jamaica
     - JM
     - None
   * - Japan
     - JP
     - None
   * - Kazakhstan
     - KZ
     - None
   * - Kenya
     - KE
     - None
   * - Kyrgyzstan
     - KG
     - None
   * - Latvia
     - LV
     - None
   * - Lesotho
     - LS
     - None
   * - Liechtenstein
     - LI
     - None
   * - Lithuania
     - LT
     - None
   * - Luxembourg
     - LU
     - None
   * - Madagascar
     - MG
     - None
   * - Malawi
     - MW
     - None
   * - Malaysia
     - MY
     - States: JHR, KDH, KTN, KUL, LBN, MLK, NSN, PHG, PJY, PLS, PNG, PRK, SBH, SGR, SWK, TRG
   * - Malta
     - MT
     - None
   * - Marshall Islands (the)
     - MH
     - None
   * - Mexico
     - MX
     - None
   * - Moldova
     - MD
     - None
   * - Monaco
     - MC
     - None
   * - Montenegro
     - ME
     - None
   * - Morocco
     - MA
     - None
   * - Mozambique
     - MZ
     - None
   * - Namibia
     - NA
     - None
   * - Netherlands
     - NL
     - None
   * - New Zealand
     - NZ
     - Regions: AUK, CAN, HKB, MBH, NSN, NTL, OTA, STL, TKI, WGN, WTC, CIT. Sub-regions: South Canterbury
   * - Nicaragua
     - NI
     - Departments: **MN** (default)
   * - Nigeria
     - NG
     - None
   * - Northern Mariana Islands (the)
     - MP
     - None; Can also be loaded as country US, subdivision MP
   * - North Macedonia
     - MK
     - None
   * - Norway
     - NO
     - None
   * - Pakistan
     - PK
     - None
   * - Panama
     - PA
     - None
   * - Paraguay
     - PY
     - None
   * - Peru
     - PE
     - None
   * - Philippines
     - PH
     - None
   * - Poland
     - PL
     - None
   * - Portugal
     - PT
     - Districts: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, Ext; Use subdiv='Ext' to include holidays most people have off
   * - Puerto Rico
     - PR
     - None; Can also be loaded as country US, subdivision PR
   * - Romania
     - RO
     - None
   * - Russia
     - RU
     - None
   * - San Marino
     - SM
     - None
   * - Saudi Arabia
     - SA
     - None
   * - Serbia
     - RS
     - None
   * - Singapore
     - SG
     - None
   * - Slovakia
     - SK
     - None
   * - Slovenia
     - SI
     - None
   * - South Africa
     - ZA
     - None
   * - South Korea
     - KR
     - None
   * - Spain
     - ES
     - Autonomous communities: AN, AR, AS, CB, CE, CL, CM, CN, CT, EX, GA, IB, MC, MD, ML, NC, PV, RI, VC
   * - Sweden
     - SE
     - None
   * - Switzerland
     - CH
     - Cantons: AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
   * - Taiwan
     - TW
     - None
   * - Thailand
     - TH
     - None
   * - Tunisia
     - TN
     - None
   * - Turkey
     - TR
     - None
   * - Ukraine
     - UA
     - None
   * - United Arab Emirates
     - AE
     - None
   * - United Kingdom
     - GB
     - Subdivisions: England, Northern Ireland, Scotland, **UK** (default), Wales; For Isle of Man use country code IM
   * - United States Minor Outlying Islands
     - UM
     - None; Can also be loaded as country US, subdivision UM
   * - United States of America (the)
     - US
     - States and territories: AL, AK, AS, AZ, AR, CA, CO, CT, DE, DC, FL, GA, GU, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MH, MA, MI, FM, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, MP, OH, OK, OR, PW, PA, PR, RI, SC, SD, TN, TX, UM, UT, VT, VA, VI, WA, WV, WI, WY
   * - United States Virgin Islands (the)
     -
     - See Virgin Islands (U.S.)
   * - Uruguay
     - UY
     - None
   * - Uzbekistan
     - UZ
     - None
   * - Vatican City
     - VA
     - None
   * - Venezuela
     - VE
     - None
   * - Vietnam
     - VN
     - None
   * - Virgin Islands (U.S.)
     - VI
     - None; Can also be loaded as country US, subdivision VI
   * - Zambia
     - ZM
     - None
   * - Zimbabwe
     - ZW
     - None


Available Financial Markets
===========================

.. _ISO 10383 MIC: https://www.iso20022.org/market-identifier-codes

The standard way to refer to a financial market is to use its `ISO 10383 MIC`_
(Market Identifier Code) as a "country" code when available. The
following financial markets are available:

.. list-table::
   :widths: 23 4 83
   :header-rows: 1
   :class: tight-table

   * - Entity
     - Code
     - Info
   * - European Central Bank
     - ECB
     - Trans-European Automated Real-time Gross Settlement (TARGET2)
   * - New York Stock Exchange
     - XNYS
     - NYSE market holidays (used by all other US-exchanges, including NASDAQ, etc.)


Localization
===========================

.. _ISO 639-1 code: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

Some of the supported entities (country/market) provide more than one
language for holiday names output. The default language is defined by
``default_language`` (optional) attribute for each entity and is used as a fallback
when neither user specified language nor user locale language available. The
default language code is a `ISO 639-1 code`_.

.. list-table::
   :widths: 23 4 83
   :header-rows: 1
   :class: tight-table

   * - Country
     - Default Language
     - Supported languages
   * - Argentina
     - es
     - en_US, es
   * - Armenia
     - hy
     - en_US, hy
   * - Belarus
     - be
     - be, en_US
   * - Bulgaria
     - bg
     - bg, en_US
   * - Canada
     - en
     - en, fr
   * - Cyprus
     - el
     - el, en
   * - Denmark
     - da
     - da, en_US
   * - Ethiopia
     - am
     - am, en_US
   * - Georgia
     - ka
     - en_US, ka
   * - Greece
     - el
     - el, en_US
   * - Japan
     - ja
     - en_US, ja
   * - Poland
     - pl
     - en_US, pl, uk
   * - Russia
     - ru
     - en_US, ru
   * - Serbia
     - sr
     - en_US, sr
   * - Ukraine
     - uk
     - en_US, uk


Beta Version
------------

The latest development (beta) version can be installed directly from GitHub:

.. code-block:: bash

    $ pip install --upgrade https://github.com/dr-prodigy/python-holidays/tarball/beta

All new features are always first pushed to beta branch, then released on
master branch upon official version upgrades.


Contributions
-------------

.. _Issues: https://github.com/dr-prodigy/python-holidays/issues
.. _pull requests: https://github.com/dr-prodigy/python-holidays/pulls
.. _here: CONTRIBUTING.rst

Issues_ and `pull requests`_ are always welcome.  Please see
`here`_ for more information.

License
-------

.. __: LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
