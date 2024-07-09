========
holidays
========

A fast, efficient Python library for generating country- and subdivision- (e.g.
state or province) specific sets of government-designated holidays on the fly.
It aims to make determining whether a specific date is a holiday as fast and
flexible as possible.

.. |downloads| image:: https://img.shields.io/pypi/dm/holidays?color=41B5BE&style=flat
    :target: https://pypi.org/project/holidays
    :alt: PyPI downloads

.. |version| image:: https://img.shields.io/pypi/v/holidays?color=41B5BE&label=version&style=flat
    :target: https://pypi.org/project/holidays
    :alt: PyPI version

.. |release date| image:: https://img.shields.io/github/release-date/vacanza/python-holidays?color=41B5BE&style=flat
    :target: https://github.com/vacanza/python-holidays/releases
    :alt: PyPI release date

.. |status| image:: https://img.shields.io/github/actions/workflow/status/vacanza/python-holidays/ci-cd.yml?branch=dev&color=41BE4A&style=flat
    :target: https://github.com/vacanza/python-holidays/actions/workflows/ci-cd.yml?query=branch%3Adev
    :alt: CI/CD status

.. |documentation| image:: https://img.shields.io/readthedocs/python-holidays?color=41BE4A&style=flat
    :target: https://python-holidays.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status

.. |license| image:: https://img.shields.io/github/license/vacanza/python-holidays?color=41B5BE&style=flat
    :target: https://github.com/vacanza/python-holidays/blob/dev/LICENSE
    :alt: License

.. |python versions| image:: https://img.shields.io/pypi/pyversions/holidays?label=python&color=41B5BE&style=flat
    :target: https://pypi.org/project/holidays
    :alt: Python supported versions

.. |style| image:: https://img.shields.io/badge/style-ruff-41B5BE?style=flat
    :target: https://github.com/astral-sh/ruff
    :alt: Code style

.. |coverage| image:: https://img.shields.io/codecov/c/github/vacanza/python-holidays/dev?color=41B5BE&style=flat
    :target: https://app.codecov.io/gh/vacanza/python-holidays
    :alt: Code coverage

.. |stars| image:: https://img.shields.io/github/stars/vacanza/python-holidays?color=41BE4A&style=flat
    :target: https://github.com/vacanza/python-holidays/stargazers
    :alt: GitHub stars

.. |forks| image:: https://img.shields.io/github/forks/vacanza/python-holidays?color=41BE4A&style=flat
    :target: https://github.com/vacanza/python-holidays/forks
    :alt: GitHub forks

.. |contributors| image:: https://img.shields.io/github/contributors/vacanza/python-holidays?color=41BE4A&style=flat
    :target: https://github.com/vacanza/python-holidays/graphs/contributors
    :alt: GitHub contributors

.. |last commit| image:: https://img.shields.io/github/last-commit/vacanza/python-holidays/dev?color=41BE4A&style=flat
    :target: https://github.com/vacanza/python-holidays/commits/dev
    :alt: GitHub last commit

+--------+------------------------------------------------+
| PyPI   | |downloads| |version| |release date|           |
+--------+------------------------------------------------+
| CI/CD  | |status| |documentation|                       |
+--------+------------------------------------------------+
| Code   | |license| |python versions| |style| |coverage| |
+--------+------------------------------------------------+
| GitHub | |stars| |forks| |contributors| |last commit|   |
+--------+------------------------------------------------+

Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: shell

    $ pip install --upgrade holidays

The latest development (dev) version can be installed directly from GitHub:

.. code-block:: shell

    $ pip install --upgrade https://github.com/vacanza/python-holidays/tarball/dev

All new features are always first pushed to dev branch, then released on
main branch upon official version upgrades.

Documentation
-------------

.. _Read the Docs: https://python-holidays.readthedocs.io/

The documentation is hosted on `Read the Docs`_.


Quick Start
-----------

.. code-block:: python

    from datetime import date
    import holidays

    us_holidays = holidays.US()  # this is a dict-like object
    # the below is the same, but takes a string:
    us_holidays = holidays.iso_3166_holidays('US')  # this is a dict-like object

    nyse_holidays = holidays.NYSE()  # this is a dict-like object
    # the below is the same, but takes a string:
    nyse_holidays = holidays.iso_10383_holidays('NYSE')  # this is a dict-like object

    date(2015, 1, 1) in us_holidays  # True
    date(2015, 1, 2) in us_holidays  # False
    us_holidays.get('2014-01-01')  # "New Year's Day"

The HolidayBase dict-like class will also recognize date strings and Unix
timestamps:

.. code-block:: python

    '2014-01-01' in us_holidays  # True
    '1/1/2014' in us_holidays    # True
    1388597445 in us_holidays    # True

Some holidays may be only present in parts of an entity:

.. code-block:: python

    us_pr_holidays = holidays.iso_3166_holidays('US', subdiv='PR')
    '2018-01-06' in us_holidays     # False
    '2018-01-06' in us_pr_holidays  # True

.. _python-holidays documentation: https://python-holidays.readthedocs.io/

Please see the `python-holidays documentation`_ for additional examples and
detailed information.


Available ISO 3166 Entities
---------------------------

.. _ISO 3166-1 alpha-2 code: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
.. _ISO 3166-2 code: https://en.wikipedia.org/wiki/ISO_3166-2
.. _ISO 639-1 code: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
.. _ISO 639-2 code: https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes

We currently support 148 ISO 3166 entity codes. The standard way to refer to an entity
is by using its `ISO 3166-1 alpha-2 code`_, the same used for domain names, and
for a subdivision its `ISO 3166-2 code`_. Some entities have common or foreign
names or abbreviations as aliases for their subdivisions. These are defined in
the (optional) ``subdivisions_aliases`` attribute.
Some of the entities support more than one language for holiday names output.
A default language is defined by ``default_language`` (optional) attribute
for each entity and is used as a fallback when neither user specified
language nor user locale language available. The default language code is
a `ISO 639-1 code`_. A list of all languages supported by entity is defined by
``supported_languages`` (optional) attribute. If there is no designated
`ISO 639-1 code`_ then `ISO 639-2 code`_ can be used.

Many entities have other categories of holidays in addition to common (national-wide) holidays:
bank holidays, school holidays, additional (paid or non-paid) holidays, holidays of state or
public employees, religious holidays (valid only for these religions followers). A list of all
categories supported by entity is defined by ``supported_categories`` (optional) attribute.

The following is a list of supported entities, their subdivisions followed by their
aliases (if any) in brackets, available languages and additional holiday categories.
All entities support **PUBLIC** holidays category by default.
All other default values are highlighted with bold:


.. list-table::
  :widths: 20 4 46 20 10
  :header-rows: 1
  :class: tight-table

  * - Code
    - Name
    - Subdivisions
    - Languages
    - Categories
  * - AD
    - Andorra
    - 02, 03, 04, 05, 06, 07, 08
    -
    -
  * - AE
    - United Arab Emirates
    -
    - **ar**, en_US
    -
  * - AL
    - Albania
    -
    -
    -
  * - AM
    - Armenia
    -
    - en_US, **hy**
    -
  * - AO
    - Angola
    -
    - en_US, **pt_AO**, uk
    -
  * - AR
    - Argentina
    -
    - en_US, **es**, uk
    -
  * - AS
    - American Samoa
    -
    -
    - UNOFFICIAL
  * - AT
    - Austria
    - 1 (Burgenland, Bgld, B), 2 (Kärnten, Ktn, K), 3 (Niederösterreich, NÖ, N), 4 (Oberösterreich, OÖ, O), 5 (Salzburg, Sbg, S), 6 (Steiermark, Stmk, St), 7 (Tirol, T), 8 (Vorarlberg, Vbg, V), 9 (Wien, W)
    - **de**, en_US, uk
    - BANK
  * - AU
    - Australia
    - ACT (Australian Capital Territory), NSW (New South Wales), NT (Northern Territory), QLD (Queensland), SA (South Australia), TAS (Tasmania), VIC (Victoria), WA (Western Australia)
    -
    - BANK, HALF_DAY
  * - AW
    - Aruba
    -
    - en_US, nl, **pap_AW**, uk
    -
  * - AZ
    - Azerbaijan
    -
    - **az**, en_US, uk
    - WORKDAY
  * - BA
    - Bosnia and Herzegovina
    - BIH, BRC, SRP
    - **bs**, en_US, sr, uk
    -
  * - BB
    - Barbados
    -
    -
    -
  * - BD
    - Bangladesh
    -
    -
    -
  * - BE
    - Belgium
    -
    - de, en_US, fr, **nl**, uk
    - BANK
  * - BF
    - Burkina Faso
    -
    -
    -
  * - BG
    - Bulgaria
    -
    - **bg**, en_US, uk
    - SCHOOL
  * - BH
    - Bahrain
    -
    - **ar**, en_US
    -
  * - BI
    - Burundi
    -
    -
    -
  * - BN
    - Brunei Darussalam
    -
    - en_US, **ms**, th
    -
  * - BO
    - Bolivia
    - B, C, H, L, N, O, P, S, T
    - en_US, **es**, uk
    -
  * - BR
    - Brazil
    - AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO
    -
    - OPTIONAL
  * - BS
    - Bahamas
    -
    -
    -
  * - BW
    - Botswana
    -
    -
    -
  * - BY
    - Belarus
    -
    - **be**, en_US
    -
  * - BZ
    - Belize
    -
    -
    -
  * - CA
    - Canada
    - AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT
    - ar, **en_CA**, en_US, fr, th
    - GOVERNMENT, OPTIONAL
  * - CH
    - Switzerland
    - AG, AI, AR, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH
    - **de**, en_US, fr, it, uk
    - HALF_DAY, OPTIONAL
  * - CL
    - Chile
    - AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA, ML, NB, RM, TA, VS
    - en_US, **es**, uk
    - BANK
  * - CM
    - Cameroon
    -
    -
    -
  * - CN
    - China
    -
    - en_US, th, **zh_CN**, zh_TW
    - HALF_DAY
  * - CO
    - Colombia
    -
    - en_US, **es**, uk
    -
  * - CR
    - Costa Rica
    -
    - en_US, **es**, uk
    - OPTIONAL
  * - CU
    - Cuba
    -
    - en_US, **es**, uk
    -
  * - CW
    - Curaçao
    -
    - en_US, nl, **pap_CW**, uk
    -
  * - CY
    - Cyprus
    -
    - **el**, en_CY, en_US, uk
    - BANK, OPTIONAL
  * - CZ
    - Czechia
    -
    - **cs**, en_US, sk, uk
    -
  * - DE
    - Germany
    - BB, BE, BW, BY, BYP, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH
    - **de**, en_US, uk
    -
  * - DJ
    - Djibouti
    -
    - ar, en_US, **fr**
    -
  * - DK
    - Denmark
    -
    - **da**, en_US, uk
    - OPTIONAL
  * - DO
    - Dominican Republic
    -
    - en_US, **es**, uk
    -
  * - DZ
    - Algeria
    -
    - **ar**, en_US, fr
    -
  * - EC
    - Ecuador
    -
    - en_US, **es**, uk
    -
  * - EE
    - Estonia
    -
    - en_US, **et**, uk
    -
  * - EG
    - Egypt
    -
    - **ar**, en_US
    -
  * - ES
    - Spain
    - AN, AR, AS, CB, CE, CL, CM, CN, CT, EX, GA, IB, MC, MD, ML, NC, PV, RI, VC
    - en_US, **es**, uk
    -
  * - ET
    - Ethiopia
    -
    - **am**, ar, en_US
    -
  * - FI
    - Finland
    -
    - en_US, **fi**, sv, uk
    -
  * - FR
    - France
    - BL, GES, GP, GY, MF, MQ, NC, PF, RE, WF, YT
    - en_US, **fr**, uk
    -
  * - GA
    - Gabon
    -
    -
    -
  * - GB
    - United Kingdom of Great Britain and Northern Ireland
    - ENG (England), NIR (Northern Ireland), SCT (Scotland), WLS (Wales)
    -
    -
  * - GE
    - Georgia
    -
    - en_US, **ka**, uk
    - GOVERNMENT
  * - GH
    - Ghana
    -
    -
    -
  * - GL
    - Greenland
    -
    - da, en_US, **kl**
    - OPTIONAL
  * - GR
    - Greece
    -
    - **el**, en_US, uk
    - HALF_DAY
  * - GT
    - Guatemala
    -
    - en_US, **es**
    -
  * - GU
    - Guam
    -
    -
    - UNOFFICIAL
  * - HK
    - Hong Kong
    -
    -
    - OPTIONAL
  * - HN
    - Honduras
    -
    - en_US, **es**, uk
    -
  * - HR
    - Croatia
    -
    - en_US, **hr**, uk
    -
  * - HU
    - Hungary
    -
    - en_US, **hu**, uk
    -
  * - ID
    - Indonesia
    -
    - en_US, **id**, uk
    - GOVERNMENT
  * - IE
    - Ireland
    -
    -
    - 
  * - IL
    - Israel
    -
    - en_US, **he**, uk
    - OPTIONAL, SCHOOL
  * - IM
    - Isle of Man
    -
    -
    -
  * - IN
    - India
    - AN, AP, AR, AS, BR, CG, CH, DH, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA, LD, MH, ML, MN, MP, MZ, NL, OD, PB, PY, RJ, SK, TN, TR, TS, UK, UP, WB
    - 
    -
  * - IR
    - Iran
    -
    - en_US, **fa**
    -
  * - IS
    - Iceland
    -
    - en_US, **is**, uk
    -
  * - IT
    - Italy
    - AG, AL, AN, AO, AP, AQ, AR, AT, AV, BA, BG, BI, BL, BN, BO, BR, BS, BT, BZ, CA, CB, CE, CH, CL, CN, CO, CR, CS, CT, CZ, EN, FC, FE, FG, FI, FM, FR, GE, GO, GR, IM, IS, KR, LC, LE, LI, LO, LT, LU, MB, MC, ME, MI, MN, MO, MS, MT, NA, NO, NU, OR, PA, PC, PD, PE, PG, PI, PN, PO, PR, PT, PU, PV, PZ, RA, RC, RE, RG, RI, RM, RN, RO, SA, SI, SO, SP, SR, SS, SU, SV, TA, TE, TN, TO, TP, TR, TS, TV, UD, VA, VB, VC, VE, VI, VR, VT, VV, Andria, Barletta, Cesena, Forli, Pesaro, Trani, Urbino
    -
    -
  * - JE
    - Jersey
    -
    -
    -
  * - JM
    - Jamaica
    -
    -
    -
  * - JO
    - Jordan
    -
    - **ar**, en_US
    -
  * - JP
    - Japan
    -
    - en_US, **ja**, th
    - BANK
  * - KE
    - Kenya
    -
    -
    -
  * - KG
    - Kyrgyzstan
    -
    -
    -
  * - KH
    - Cambodia
    -
    - en_US, **km**, th
    -
  * - KR
    - South Korea
    -
    - en_US, **ko**, th
    - BANK
  * - KW
    - Kuwait
    -
    - **ar**, en_US
    -
  * - KZ
    - Kazakhstan
    -
    -
    -
  * - LA
    - Laos
    -
    - en_US, **lo**, th
    - BANK, SCHOOL, WORKDAY
  * - LI
    - Liechtenstein
    -
    - **de**, en_US, uk
    - BANK
  * - LS
    - Lesotho
    -
    -
    -
  * - LT
    - Lithuania
    -
    - en_US, **lt**, uk
    -
  * - LU
    - Luxembourg
    -
    - de, en_US, fr, **lb**, uk
    -
  * - LV
    - Latvia
    -
    - en_US, **lv**, uk
    -
  * - MA
    - Morocco
    -
    - **ar**, en_US, fr
    -
  * - MC
    - Monaco
    -
    - en_US, **fr**, uk
    -
  * - MD
    - Moldova
    -
    - en_US, **ro**, uk
    -
  * - ME
    - Montenegro
    -
    -
    -
  * - MG
    - Madagascar
    -
    - en_US, **mg**, uk
    -
  * - MH
    - Marshall Islands
    -
    -
    -
  * - MK
    - North Macedonia
    -
    -
    -
  * - MP
    - Northern Mariana Islands
    -
    -
    - UNOFFICIAL
  * - MT
    - Malta
    -
    - en_US, **mt**
    -
  * - MV
    - Maldives
    -
    -
    -
  * - MW
    - Malawi
    -
    -
    -
  * - MX
    - Mexico
    -
    - en_US, **es**, uk
    -
  * - MY
    - Malaysia
    - 01 (Johor), 02 (Kedah), 03 (Kelantan), 04 (Melaka), 05 (Negeri Sembilan), 06 (Pahang), 07 (Pulau Pinang), 08 (Perak), 09 (Perlis), 10 (Selangor), 11 (Terengganu), 12 (Sabah), 13 (Sarawak), 14 (WP Kuala Lumpur), 15 (WP Labuan), 16 (WP Putrajaya)
    - en_US, **ms_MY**
    -
  * - MZ
    - Mozambique
    -
    - en_US, **pt_MZ**, uk
    -
  * - NA
    - Namibia
    -
    -
    -
  * - NG
    - Nigeria
    -
    -
    -
  * - NI
    - Nicaragua
    - AN, AS, BO, CA, CI, CO, ES, GR, JI, LE, MD, MN, MS, MT, NS, RI, SJ
    - en_US, **es**, uk
    -
  * - NL
    - Netherlands
    -
    - en_US, **nl**, uk
    - OPTIONAL
  * - NO
    - Norway
    -
    - en_US, **no**, uk
    -
  * - NZ
    - New Zealand
    - AUK (Auckland), BOP (Bay of Plenty), CAN (Canterbury), CIT (Chatham Islands), GIS (Gisborne), HKB (Hawke's Bay), MBH (Marlborough), MWT (Manawatū Whanganui), NSN (Nelson), NTL (Northland), OTA (Otago), STL (Southland), TAS (Tasman), TKI (Taranaki), WGN (Greater Wellington), WKO (Waikato), WTC (West Coast)
    -
    -
  * - PA
    - Panama
    -
    -
    -
  * - PE
    - Peru
    -
    - en_US, **es**, uk
    -
  * - PG
    - Papua New Guinea
    -
    -
    -
  * - PH
    - Philippines
    -
    -
    -
  * - PK
    - Pakistan
    -
    -
    -
  * - PL
    - Poland
    -
    - en_US, **pl**, uk
    -
  * - PR
    - Puerto Rico
    -
    -
    - UNOFFICIAL
  * - PT
    - Portugal
    - 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 30
    - en_US, **pt_PT**, uk
    - OPTIONAL
  * - PW
    - Palau
    -
    -
    - ARMED_FORCES, HALF_DAY
  * - PY
    - Paraguay
    -
    - en_US, **es**, uk
    - GOVERNMENT
  * - RO
    - Romania
    -
    - en_US, **ro**, uk
    -
  * - RS
    - Serbia
    -
    - en_US, **sr**
    -
  * - RU
    - Russian Federation
    -
    - en_US, **ru**
    -
  * - SA
    - Saudi Arabia
    -
    - **ar**, en_US
    -
  * - SC
    - Seychelles
    -
    - **en_SC**, en_US
    -
  * - SE
    - Sweden
    -
    - en_US, **sv**, uk
    -
  * - SG
    - Singapore
    -
    -
    -
  * - SI
    - Slovenia
    -
    - en_US, **sl**, uk
    -
  * - SK
    - Slovakia
    -
    - en_US, **sk**, uk
    - WORKDAY
  * - SM
    - San Marino
    -
    -
    -
  * - SV
    - El Salvador
    - AH, CA, CH, CU, LI, MO, PA, SA, SM, SO, SS, SV, UN, US
    -
    -
  * - SZ
    - Eswatini
    -
    -
    -
  * - TD
    - Chad
    -
    -
    -
  * - TH
    - Thailand
    -
    - en_US, **th**
    - ARMED_FORCES, BANK, GOVERNMENT, SCHOOL, WORKDAY
  * - TL
    - Timor-Leste
    -
    - en_US, **pt_TL**, tet
    - GOVERNMENT, WORKDAY
  * - TN
    - Tunisia
    -
    - **ar**, en_US
    -
  * - TO
    - Tonga
    -
    - en_US, **to**
    -
  * - TR
    - Türkiye
    -
    - en_US, **tr**, uk
    - HALF_DAY
  * - TW
    - Taiwan
    -
    - en_US, th, zh_CN, **zh_TW**
    -
  * - TZ
    - Tanzania
    -
    - en_US, **sw**
    - BANK
  * - UA
    - Ukraine
    -
    - ar, en_US, **uk**
    -
  * - UM
    - United States Minor Outlying Islands
    - 
    -
    - UNOFFICIAL
  * - US
    - United States of America
    - AK, AL, AR, AS, AZ, CA, CO, CT, DC, DE, FL, GA, GU, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MP, MS, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, PR, RI, SC, SD, TN, TX, UM, UT, VA, VI, VT, WA, WI, WV, WY
    -
    - UNOFFICIAL
  * - UY
    - Uruguay
    -
    - en_US, **es**, uk
    - BANK
  * - UZ
    - Uzbekistan
    -
    - en_US, uk, **uz**
    -
  * - VA
    - Holy See
    -
    -
    -
  * - VE
    - Venezuela
    -
    - en_US, **es**, uk
    -
  * - VI
    - Virgin Islands (U.S.)
    -
    -
    - UNOFFICIAL
  * - VN
    - Vietnam
    -
    -
    -
  * - VU
    - Vanuatu
    -
    -
    -
  * - ZA
    - South Africa
    -
    -
    -
  * - ZM
    - Zambia
    -
    -
    -
  * - ZW
    - Zimbabwe
    -
    -
    -

Available ISO 10383 Entities
============================

.. _ISO 10383 MIC: https://www.iso20022.org/market-identifier-codes

The standard way to refer to an ISO 10383 entity is to use its `ISO 10383 MIC`_
(Market Identifier Code). The following ISO 10383 entities are available:

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
   * - ICE Futures Europe 
     - IFEU
     - A London-based Investment Exchange holidays
   * - New York Stock Exchange
     - XNYS
     - NYSE market holidays (used by all other US-exchanges, including NASDAQ, etc.)


Contributions
-------------

.. _Issues: https://github.com/vacanza/python-holidays/issues
.. _pull requests: https://github.com/vacanza/python-holidays/pulls
.. _here: https://github.com/vacanza/python-holidays/blob/dev/CONTRIBUTING.rst

Issues_ and `pull requests`_ are always welcome.  Please see
`here`_ for more information.

License
-------

.. __: https://github.com/vacanza/python-holidays/blob/dev/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
