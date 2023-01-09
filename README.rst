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

We currently support 101 countries. The standard way to refer to a country is by
using its `ISO 3166-1 alpha-2 code`_, the same used for domain names. The
following countries and their subdivisions are available:

.. list-table::
   :widths: 23 4 83 15
   :header-rows: 1
   :class: tight-table

   * - Country
     - Code
     - Subdivisions Available
     - Install extras
   * - Angola
     - AO
     - None
     - None
   * - Argentina
     - AR
     - None
     - None
   * - Armenia
     - AM
     - None
     - None
   * - Aruba
     - AW
     - None
     - None
   * - Australia
     - AU
     - States and territories: **ACT** (default), NSW, NT, QLD, SA, TAS, VIC, WA
     - None
   * - Austria
     - AT
     - States: 1, 2, 3, 4, 5, 6, 7, 8, **9** (default)
     - None
   * - Azerbaijan
     - AZ
     - None
     - holidays[islamic]
   * - Bangladesh
     - BD
     - None
     - None
   * - Belarus
     - BY
     - None
     - None
   * - Belgium
     - BE
     - None
     - None
   * - Bolivia
     - BO
     - Departments: B, C, H, L, N, O, P, S, T
     - None
   * - Bosnia and Herzegovina
     - BA
     - Departments: FBiH, RS, BD
     - None
   * - Botswana
     - BW
     - None
     - None
   * - Brazil
     - BR
     - States: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, RJ, RN, RO, RR, RS, SC, SE, SP, TO
     - None
   * - Bulgaria
     - BG
     - None
     - None
   * - Burundi
     - BI
     - None
     - holidays[islamic]
   * - Canada
     - CA
     - Provinces and territories: AB, BC, MB, NB, NL, NS NT, NU, **ON** (default), PE, QC, SK, YT
     - None
   * - Chile
     - CL
     - Regions: AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA, ML, NB, RM, TA, VS
     - None
   * - China
     - CN
     - None
     - None
   * - Colombia
     - CO
     - None
     - None
   * - Croatia
     - HR
     - None
     - None
   * - Cuba
     - CU
     - None
     - None
   * - Curaçao
     - CW
     - None
     - None
   * - Cyprus
     - CY
     - None
     - None
   * - Czechia
     - CZ
     - None
     - None
   * - Denmark
     - DK
     - None
     - None
   * - Djibouti
     - DJ
     - None
     - holidays[islamic]
   * - Dominican Republic
     - DO
     - None
     - None
   * - Egypt
     - EG
     - None
     - holidays[islamic]
   * - Estonia
     - EE
     - None
     - None
   * - Ethiopia
     - ET
     - None
     - holidays[islamic]
   * - Finland
     - FI
     - None
     - None
   * - France
     - FR
     - Départements: **Métropole** (default), Alsace-Moselle, Guadeloupe, Guyane, Martinique, Mayotte, Nouvelle-Calédonie, La Réunion, Polynésie Française, Saint-Barthélémy, Saint-Martin, Wallis-et-Futuna
     - None
   * - Georgia
     - GE
     - None
     - None
   * - Germany
     - DE
     - States: BB, BE, BW, BY, BYP, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH
     - None
   * - Greece
     - GR
     - None
     - None
   * - Honduras
     - HN
     - None
     - None
   * - Hong Kong
     - HK
     - None
     - None
   * - Hungary
     - HU
     - None
     - None
   * - Iceland
     - IS
     - None
     - None
   * - India
     - IN
     - States: AN, AP, AR, AS, BR, CG, CH, DD, DH, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA, LD, MH, ML, MN, MP, MZ, NL, OR, PB, PY, RJ, SK, TN, TR, TS, UK, UP, WB
     - None
   * - Indonesia
     - ID
     - None
     - None
   * - Ireland
     - IE
     - None
     - None
   * - Isle of Man
     - IM
     - None
     - None
   * - Israel
     - IL
     - None
     - holidays[jewish]
   * - Italy
     - IT
     - Provinces: AG, AL, AN, AO, AP, AQ, AR, AT, AV, BA, BG, BI, BL, BN, BO, BR, BS, BT, BZ, CA, CB, CE, CH, CL, CN, CO, CR, CS, CT, CZ, EN, FC, FE, FG, FI, FM, FR, GE, GO, GR, IM, IS, KR, LC, LE, LI, LO, LT, LU, MB, MC, ME, MI, MN, MO, MS, MT, NA, NO, NU, OR, PA, PC, PD, PE, PG, PI, PN, PO, PR, PT, PU, PV, PZ, RA, RC, RE, RG, RI, RM, RN, RO, SA, SI, SO, SP, SR, SS, SU, SV, TA, TE, TN, TO, TP, TR, TS, TV, UD, VA, VB, VC, VE, VI, VR, VT, VV; Cities: Barletta, Andria, Trani, Cesena, Forlì, Pesaro, Urbino
     - None
   * - Jamaica
     - JM
     - None
     - None
   * - Japan
     - JP
     - None
     - None
   * - Kazakhstan
     - KZ
     - None
     - holidays[islamic]
   * - Kenya
     - KE
     - None
     - None
   * - Latvia
     - LV
     - None
     - None
   * - Lesotho
     - LS
     - None
     - None
   * - Liechtenstein
     - LI
     - None
     - None
   * - Lithuania
     - LT
     - None
     - None
   * - Luxembourg
     - LU
     - None
     - None
   * - Madagascar
     - MG
     - None
     - None
   * - Malaysia
     - MY
     - States: JHR, KDH, KTN, MLK, NSN, PHG, PNG, PRK, PLS, SBH, SWK, SGR, TRG, KUL, LBN, PJY
     - holidays[islamic]
   * - Malawi
     - MW
     - None
     - None
   * - Malta
     - MT
     - None
     - None
   * - Mexico
     - MX
     - None
     - None
   * - Moldova
     - MD
     - None
     - None
   * - Morocco
     - MA
     - None
     - holidays[islamic]
   * - Mozambique
     - MZ
     - None
     - None
   * - Netherlands
     - NL
     - None
     - None
   * - Namibia
     - NA
     - None
     - None
   * - New Zealand
     - NZ
     - Regions: AUK, CAN, HKB, MBH, NSN, NTL, OTA, STL, TKI, WGN, WTC, CIT; Sub-regions: South Canterbury
     - None
   * - Nicaragua
     - NI
     - Departments: **MN** (default)
     - None
   * - Nigeria
     - NG
     - None
     - holidays[islamic]
   * - North Macedonia
     - MK
     - None
     - holidays[islamic]
   * - Norway
     - NO
     - None
     - None
   * - Pakistan
     - PK
     - None
     - None
   * - Paraguay
     - PY
     - None
     - None
   * - Peru
     - PE
     - None
     - None
   * - Poland
     - PL
     - None
     - None
   * - Portugal
     - PT
     - Districts: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18; Use subdiv='Ext' to include holidays most people have off
     - None
   * - Romania
     - RO
     - None
     - None
   * - Russia
     - RU
     - None
     - None
   * - Saudi Arabia
     - SA
     - None
     - None
   * - Serbia
     - RS
     - None
     - None
   * - Singapore
     - SG
     - None
     - holidays[islamic]
   * - Slovakia
     - SK
     - None
     - None
   * - Slovenia
     - SI
     - None
     - None
   * - South Africa
     - ZA
     - None
     - None
   * - South Korea
     - KR
     - None
     - holidays[korean-lunar]
   * - Spain
     - ES
     - Autonomous communities: AN (Andalucía), AR (Aragón), AS (Asturias), CB (Cantabria), CE (Ceuta), CL (Castilla y León), CM (Castilla La Mancha), CN (Canarias), CT (Cataluña), EX (Extremadura), GA (Galicia), IB (Islas Baleares), MC (Murcia), MD (Madrid), NC (Navarra), PV (País Vasco), RI (La Rioja), VC (Comunidad Valenciana)
     - holidays[islamic]
   * - Swaziland
     - SZ
     - None
     - None
   * - Sweden
     - SE
     - None
     - None
   * - Switzerland
     - CH
     - Cantons: AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
     - None
   * - Taiwan
     - TW
     - None
     - None
   * - Turkey
     - TR
     - None
     - holidays[islamic]
   * - Tunisia
     - TN
     - None
     - holidays[islamic]
   * - Ukraine
     - UA
     - None
     - None
   * - United Arab Emirates
     - AE
     - None
     - holidays[islamic]
   * - United Kingdom
     - GB
     - Subdivisions: **UK** (default), England, Northern Ireland, Scotland, Wales. For Isle of Man use country code IM.
     - None
   * - United States
     - US
     - States and territories: AL, AK, AS, AZ, AR, CA, CO, CT, DE, DC, FL, GA, GU, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MH, MA, MI, FM, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, MP, OH, OK, OR, PW, PA, PR, RI, SC, SD, TN, TX, UT, VT, VA, VI, WA, WV, WI, WY
     - None
   * - Uruguay
     - UY
     - None
     - None
   * - Uzbekistan
     - UZ
     - None
     - holidays[islamic]
   * - Venezuela
     - VE
     - None
     - None
   * - Vietnam
     - VN
     - None
     - holidays[korean-lunar]
   * - Zambia
     - ZM
     - None
     - None
   * - Zimbabwe
     - ZW
     - None
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
