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
.. _ISO 639-1 code: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
.. _ISO 639-2 code: https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes

We currently support 131 country codes. The standard way to refer to a country
is by using its `ISO 3166-1 alpha-2 code`_, the same used for domain names, and
for a subdivision its `ISO 3166-2 code`_. Some of the countries support more
than one language for holiday names output.
A default language is defined by ``default_language`` (optional) attribute
for each entity and is used as a fallback when neither user specified
language nor user locale language available. The default language code is
a `ISO 639-1 code`_. A list of all languages supported by country is defined by
``supported_languages`` (optional) attribute. If there is no designated
`ISO 639-1 code`_ then `ISO 639-2 code`_ can be used.

The list of supported countries, their subdivisions and supported languages
(all default values are hightlighted with bold):


.. list-table::
   :widths: 23 4 63 20
   :header-rows: 1
   :class: tight-table

   * - Country
     - Code
     - Subdivisions
     - Supported Languages
   * - Albania
     - AL
     -
     -
   * - Algeria
     - DZ
     -
     - **ar**, en_US
   * - American Samoa
     - AS
     - Can also be loaded as country US, subdivision AS
     -
   * - Andorra
     - AD
     - Parishes: 02, 03, 04, 05, 06, 07, 08
     -
   * - Angola
     - AO
     -
     -
   * - Argentina
     - AR
     -
     - en_US, **es**, uk
   * - Armenia
     - AM
     -
     - en_US, **hy**
   * - Aruba
     - AW
     -
     - en_US, nl, **pap**, uk
   * - Australia
     - AU
     - States and territories: **ACT**, NSW, NT, QLD, SA, TAS, VIC, WA
     -
   * - Austria
     - AT
     - States: 1, 2, 3, 4, 5, 6, 7, 8, **9**
     - **de**, en_US, uk
   * - Azerbaijan
     - AZ
     -
     -
   * - Bahrain
     - BH
     -
     - **ar**, en_US
   * - Bangladesh
     - BD
     -
     -
   * - Belarus
     - BY
     -
     - **be**, en_US
   * - Belgium
     - BE
     -
     - de, en_US, fr, **nl**, uk
   * - Belize
     - BZ
     -
     -
   * - Bolivia
     - BO
     - Departments: B, C, H, L, N, O, P, S, T
     -
   * - Bosnia and Herzegovina
     - BA
     - Entities and district: BIH, BRC, SRP
     - **bs**, en_US, sr, uk
   * - Botswana
     - BW
     -
     -
   * - Brazil
     - BR
     - States: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO
     -
   * - Brunei
     - BN
     -
     - en_US, **ms**, th
   * - Bulgaria
     - BG
     -
     - **bg**, en_US, uk
   * - Burkina Faso
     - BF
     -
     -
   * - Burundi
     - BI
     -
     -
   * - Cambodia
     - KH
     -
     - en_US, **km**, th
   * - Cameroon
     - CM
     -
     -
   * - Canada
     - CA
     - Provinces and territories: AB, BC, MB, NB, NL, NS, NT, NU, **ON**, PE, QC, SK, YT
     - ar, **en**, en_US, fr, th
   * - Chad
     - TD
     -
     -
   * - Chile
     - CL
     - Regions: AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA, ML, NB, RM, TA, VS
     - en_US, **es**, uk
   * - China
     - CN
     -
     -
   * - Colombia
     - CO
     -
     - en_US, **es**, uk
   * - Costa Rica
     - CR
     -
     - en_US, **es**, uk
   * - Croatia
     - HR
     -
     - en_US, **hr**, uk
   * - Cuba
     - CU
     -
     - en_US, **es**, uk
   * - Curacao
     - CW
     -
     - en_US, nl, **pap**, uk
   * - Cyprus
     - CY
     -
     - **el**, en_US
   * - Czechia
     - CZ
     -
     - **cs**, en_US, uk
   * - Denmark
     - DK
     -
     - **da**, en_US, uk
   * - Djibouti
     - DJ
     -
     -
   * - Dominican Republic
     - DO
     -
     - en_US, **es**, uk
   * - Ecuador
     - EC
     -
     - en_US, **es**, uk
   * - Egypt
     - EG
     -
     - **ar**, en_US
   * - El Salvador
     - SV
     - Departments: AH, CA, CH, CU, LI, MO, PA, SA, SM, SO, SS, SV, UN, US
     -
   * - Estonia
     - EE
     -
     - en_US, **et**, uk
   * - Eswatini
     - SZ
     -
     -
   * - Ethiopia
     - ET
     -
     - **am**, ar, en_US
   * - Finland
     - FI
     -
     - en_US, **fi**, sv, uk
   * - France
     - FR
     - Départements: BL, GES, GP, GY, MF, MQ, NC, PF, RE, WF, YT
     - en_US, **fr**, uk
   * - Gabon
     - GA
     -
     -
   * - Georgia
     - GE
     -
     - en_US, **ka**
   * - Germany
     - DE
     - States: BB, BE, BW, BY, BYP, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH
     - **de**, en_US, uk
   * - Greece
     - GR
     -
     - **el**, en_US
   * - Guam
     - GU
     - Can also be loaded as country US, subdivision GU
     -
   * - Guatemala
     - GT
     -
     - en_US, **es**
   * - Honduras
     - HN
     -
     - en_US, **es**, uk
   * - Hong Kong
     - HK
     -
     -
   * - Hungary
     - HU
     -
     - en_US, **hu**, uk
   * - Iceland
     - IS
     -
     - en_US, **is**, uk
   * - India
     - IN
     - States: AN, AP, AR, AS, BR, CG, CH, DD, DH, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA, LD, MH, ML, MN, MP, MZ, NL, OR, PB, PY, RJ, SK, TN, TR, TS, UK, UP, WB
     -
   * - Indonesia
     - ID
     -
     -
   * - Ireland
     - IE
     -
     -
   * - Isle of Man
     - IM
     -
     -
   * - Israel
     - IL
     -
     -
   * - Italy
     - IT
     - Provinces: AG, AL, AN, AO, AP, AQ, AR, AT, AV, BA, BG, BI, BL, BN, BO, BR, BS, BT, BZ, CA, CB, CE, CH, CL, CN, CO, CR, CS, CT, CZ, EN, FC, FE, FG, FI, FM, FR, GE, GO, GR, IM, IS, KR, LC, LE, LI, LO, LT, LU, MB, MC, ME, MI, MN, MO, MS, MT, NA, NO, NU, OR, PA, PC, PD, PE, PG, PI, PN, PO, PR, PT, PU, PV, PZ, RA, RC, RE, RG, RI, RM, RN, RO, SA, SI, SO, SP, SR, SS, SU, SV, TA, TE, TN, TO, TP, TR, TS, TV, UD, VA, VB, VC, VE, VI, VR, VT, VV. Cities: Andria, Barletta, Cesena, Forli, Pesaro, Trani, Urbino
     -
   * - Jamaica
     - JM
     -
     -
   * - Japan
     - JP
     -
     - en_US, **ja**
   * - Kazakhstan
     - KZ
     -
     -
   * - Kenya
     - KE
     -
     -
   * - Kyrgyzstan
     - KG
     -
     -
   * - Latvia
     - LV
     -
     - en_US, **lv**, uk
   * - Lesotho
     - LS
     -
     -
   * - Liechtenstein
     - LI
     -
     - **de**, en_US, uk
   * - Lithuania
     - LT
     -
     - en_US, **lt**, uk
   * - Luxembourg
     - LU
     -
     - de, en_US, fr, **lb**, uk
   * - Madagascar
     - MG
     -
     - en_US, **mg**, uk
   * - Malawi
     - MW
     -
     -
   * - Malaysia
     - MY
     - States: JHR, KDH, KTN, KUL, LBN, MLK, NSN, PHG, PJY, PLS, PNG, PRK, SBH, SGR, SWK, TRG
     -
   * - Malta
     - MT
     -
     - en_MT, **mt**
   * - Marshall Islands (the)
     - MH
     -
     -
   * - Mexico
     - MX
     -
     - en_US, **es**, uk
   * - Moldova
     - MD
     -
     - en_US, **ro**, uk
   * - Monaco
     - MC
     -
     - en_US, **fr**, uk
   * - Montenegro
     - ME
     -
     -
   * - Morocco
     - MA
     -
     - **ar**, en_US
   * - Mozambique
     - MZ
     -
     -
   * - Namibia
     - NA
     -
     -
   * - Netherlands
     - NL
     -
     - en_US, **nl**, uk
   * - New Zealand
     - NZ
     - Regions: AUK, BOP, CAN, CIT, GIS, HKB, MBH, MWT, NSN, NTL, OTA, STL, TAS, TKI, WGN, WKO, WTC
     -
   * - Nicaragua
     - NI
     - Departments: AN, AS, BO, CA, CI, CO, ES, GR, JI, LE, MD, **MN**, MS, MT, NS, RI, SJ
     - en_US, **es**, uk
   * - Nigeria
     - NG
     -
     -
   * - Northern Mariana Islands (the)
     - MP
     - Can also be loaded as country US, subdivision MP
     -
   * - North Macedonia
     - MK
     -
     -
   * - Norway
     - NO
     -
     - en_US, **no**, uk
   * - Pakistan
     - PK
     -
     -
   * - Panama
     - PA
     -
     -
   * - Paraguay
     - PY
     -
     - en_US, **es**, uk
   * - Peru
     - PE
     -
     - en_US, **es**, uk
   * - Philippines
     - PH
     -
     -
   * - Poland
     - PL
     -
     - en_US, **pl**, uk
   * - Portugal
     - PT
     - Districts: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 30, Ext; Use subdiv='Ext' to include holidays most people have off
     - en_US, **pt_PT**
   * - Puerto Rico
     - PR
     - Can also be loaded as country US, subdivision PR
     -
   * - Romania
     - RO
     -
     - en_US, **ro**, uk
   * - Russia
     - RU
     -
     - en_US, **ru**
   * - San Marino
     - SM
     -
     -
   * - Saudi Arabia
     - SA
     -
     - **ar**, en_US
   * - Serbia
     - RS
     -
     - en_US, **sr**
   * - Singapore
     - SG
     -
     -
   * - Slovakia
     - SK
     -
     - en_US, **sk**, uk
   * - Slovenia
     - SI
     -
     - en_US, **sl**, uk
   * - South Africa
     - ZA
     -
     -
   * - South Korea
     - KR
     -
     -
   * - Spain
     - ES
     - Autonomous communities: AN, AR, AS, CB, CE, CL, CM, CN, CT, EX, GA, IB, MC, MD, ML, NC, PV, RI, VC
     -
   * - Sweden
     - SE
     -
     - en_US, **sv**, uk
   * - Switzerland
     - CH
     - Cantons: AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
     - **de**, en_US, fr, it, uk
   * - Taiwan
     - TW
     -
     -
   * - Thailand
     - TH
     -
     - en_US, **th**
   * - Tunisia
     - TN
     -
     - **ar**, en_US
   * - Turkey
     - TR
     -
     -
   * - Ukraine
     - UA
     -
     - ar, en_US, **uk**
   * - United Arab Emirates
     - AE
     -
     - **ar**, en_US
   * - United Kingdom
     - GB
     - Subdivisions: ENG, NIR, SCT, WLS
     -
   * - United States Minor Outlying Islands
     - UM
     - Can also be loaded as country US, subdivision UM
     -
   * - United States of America (the)
     - US
     - States and territories: AK, AL, AR, AS, AZ, CA, CO, CT, DC, DE, FL, FM, GA, GU, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MH, MI, MN, MO, MP, MS, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, PR, PW, RI, SC, SD, TN, TX, UM, UT, VA, VI, VT, WA, WI, WV, WY
     -
   * - United States Virgin Islands (the)
     -
     - See Virgin Islands (U.S.)
     -
   * - Uruguay
     - UY
     -
     - en_US, **es**, uk
   * - Uzbekistan
     - UZ
     -
     -
   * - Vatican City
     - VA
     -
     -
   * - Venezuela
     - VE
     -
     - en_US, **es**, uk
   * - Vietnam
     - VN
     -
     -
   * - Virgin Islands (U.S.)
     - VI
     - Can also be loaded as country US, subdivision VI
     -
   * - Zambia
     - ZM
     -
     -
   * - Zimbabwe
     - ZW
     -
     -


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
