===============
python-holidays
===============

A fast, efficient Python library for generating country- and subdivision- (e.g.
state or province) specific sets of government-designated holidays on the fly.
It aims to make determining whether a specific date is a holiday as fast and
flexible as possible.

.. image:: https://github.com/dr-prodigy/python-holidays/workflows/Tests/badge.svg
    :target: actions

.. image:: http://img.shields.io/coveralls/dr-prodigy/python-holidays/master
    :target: https://coveralls.io/r/dr-prodigy/python-holidays

.. image:: http://img.shields.io/pypi/v/holidays.svg
    :target: https://pypi.python.org/pypi/holidays

.. image:: http://img.shields.io/pypi/l/holidays.svg
    :target: LICENSE

.. image:: https://readthedocs.org/projects/python-holidays/badge/?version=latest
    :target: https://python-holidays.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install --update holidays


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

.. _documentation: https://python-holidays.readthedocs.io/

Please see the `documentation`_ for additional examples and detailed
information.


Available Countries
-------------------

.. _ISO 3166-1 alpha-2 code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes

We currently support 86 countries. The standard way to refer to a country is by
using its `ISO 3166-1 alpha-2 code`_, the same used for domain names. The
following countries and their subdivisions are available:

.. list-table::
   :widths: 23 4 83
   :header-rows: 1
   :class: tight-table

   * - Country
     - Code
     - Subdivisions Available
   * - Angola
     - AO
     - None
   * - Argentina
     - AR
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
   * - Bangladesh
     - BD
     - None
   * - Belarus
     - BY
     - None
   * - Belgium
     - BE
     - None
   * - Botswana
     - BW
     - None
   * - Brazil
     - BR
     - States: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, RJ, RN, RO, RR, RS, SC, SE, SP, TO
   * - Bulgaria
     - BG
     - None
   * - Burundi
     - BI
     - None
   * - Canada
     - CA
     - Provinces and territories: AB, BC, MB, NB, NL, NS NT, NU, **ON** (default), PE, QC, SK, YU
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
   * - Curaçao
     - CW
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
   * - Ethiopia
     - ET
     - None
   * - Finland
     - FI
     - None
   * - France
     - FR
     - Départements: **Métropole** (default), Alsace-Moselle, Guadeloupe, Guyane, Martinique, Mayotte, Nouvelle-Calédonie, La Réunion, Polynésie Française, Saint-Barthélémy, Saint-Martin, Wallis-et-Futuna
   * - Georgia
     - GE
     - None
   * - Germany
     - DE
     - States: BB, BE, BW, BY, BYP, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH
   * - Greece
     - GR
     - None
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
     - States: AP, AS, BR, CG, GJ, HR, KA, KL, MH, MP, OD, RJ, SK, TN, TN, UK, UP, WB
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
     - Provinces: AG, AL, AN, AO, AP, AQ, AR, AT, AV, BA, BG, BI, BL, BN, BO, BR, BS, BT, BZ, CA, CB, CE, CH, CL, CN, CO, CR, CS, CT, CZ, EN, FC, FE, FG, FI, FM, FR, GE, GO, GR, IM, IS, KR, LC, LE, LI, LO, LT, LU, MB, MC, ME, MI, MN, MO, MS, MT, NA, NO, NU, OR, PA, PC, PD, PE, PG, PI, PN, PO, PR, PT, PU, PV, PZ, RA, RC, RE, RG, RI, RM, RN, RO, SA, SI, SO, SP, SR, SS, SU, SV, TA, TE, TN, TO, TP, TR, TS, TV, UD, VA, VB, VC, VE, VI, VR, VT, VV; Cities: Barletta, Andria, Trani, Cesena, Forlì, Pesaro, Urbino
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
   * - Korea
     - KR
     - None
   * - Latvia
     - LV
     - None
   * - Lesotho
     - LS
     - None
   * - Lithuania
     - LT
     - None
   * - Luxembourg
     - LU
     - None
   * - Malaysia
     - MY
     - States: JHR, KDH, KTN, MLK, NSN, PHG, PNG, PRK, PLS, SBH, SWK, SGR, TRG, KUL, LBN, PJY
   * - Malawi
     - MW
     - None
   * - Mexico
     - MX
     - None
   * - Morocco
     - MA
     - None
   * - Mozambique
     - MZ
     - None
   * - Netherlands
     - NL
     - None
   * - Namibia
     - NA
     - None
   * - New Zealand
     - NZ
     - Regions: AUK, CAN, HKB, MBH, NSN, NTL, OTA, STL, TKI, WGN, WTC, CIT; Sub-regions: South Canterbury
   * - Nicaragua
     - NI
     - Departments: **MN** (default)
   * - Nigeria
     - NG
     - None
   * - North Macedonia
     - MK
     - None
   * - Norway
     - NO
     - None
   * - Paraguay
     - PY
     - None
   * - Peru
     - PE
     - None
   * - Poland
     - PL
     - None
   * - Portugal
     - PT
     - Use subd='Ext' to include holidays most people have off
   * - Romania
     - RO
     - None
   * - Russia
     - RU
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
   * - Spain
     - ES
     - Autonomous communities: AN (Andalucía), AR (Aragón), AS (Asturias), CB (Cantabria), CE (Ceuta), CL (Castilla y León), CM (Castilla La Mancha), CN (Canarias), CT (Cataluña), EX (Extremadura), GA (Galicia), IB (Islas Baleares), MC (Murcia), MD (Madrid), NC (Navarra), PV (País Vasco), RI (La Rioja), VC (Comunidad Valenciana)
   * - Swaziland
     - SZ
     - None
   * - Sweden
     - SE
     - None
   * - Switzerland
     - CH
     - Cantons: AG, AR, AI, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
   * - Taiwan
     - TW
     - None
   * - Turkey
     - TR
     - None
   * - Tunisia
     - TN
     - None
   * - Ukraine
     - UA
     - None
   * - United Arab Emirates
     - AE
     - None
   * - United Kingdom
     - GB
     - Subdivisions: **UK** (default), England, Northern Ireland, Scotland, Wales. For Isle of Man use country code IM.
   * - United States
     - US
     - States and territories: AL, AK, AS, AZ, AR, CA, CO, CT, DE, DC, FL, GA, GU, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MH, MA, MI, FM, MN, MS, MO, MT, NE, NV, NH, NJ, NM, NY, NC, ND, MP, OH, OK, OR, PW, PA, PR, RI, SC, SD, TN, TX, UT, VT, VA, VI, WA, WV, WI, WY
   * - Uruguay
     - UY
     - None
   * - Uzbekistan
     - UZ
     - None
   * - Venezuela
     - VE
     - None
   * - Vietnam
     - VN
     - None
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
