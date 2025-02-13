# holidays

A fast, efficient Python library for generating country- and
subdivision- (e.g. state or province) specific sets of
government-designated holidays on the fly. It aims to make determining
whether a specific date is a holiday as fast and flexible as possible.

| PyPI | [![PyPI downloads](https://img.shields.io/pypi/dm/holidays?color=41B5BE&style=flat)](https://pypi.org/project/holidays) [![PyPI version](https://img.shields.io/pypi/v/holidays?color=41B5BE&label=version&style=flat)](https://pypi.org/project/holidays) [![PyPI release date](https://img.shields.io/github/release-date/vacanza/holidays?color=41B5BE&style=flat)](https://github.com/vacanza/holidays/releases) |
|------|--------------------------------------------------------------------------------------------------|
| CI/CD | [![CI/CD status](https://img.shields.io/github/actions/workflow/status/vacanza/holidays/ci-cd.yml?branch=dev&color=41BE4A&style=flat)](https://github.com/vacanza/holidays/actions/workflows/ci-cd.yml?query=branch%3Adev) [![Documentation status](https://img.shields.io/readthedocs/holidays?color=41BE4A&style=flat)](https://holidays.readthedocs.io/en/latest/?badge=latest) |
| Code | [![License](https://img.shields.io/github/license/vacanza/holidays?color=41B5BE&style=flat)](https://github.com/vacanza/holidays/blob/dev/LICENSE) [![Python supported versions](https://img.shields.io/pypi/pyversions/holidays?label=python&color=41B5BE&style=flat)](https://pypi.org/project/holidays) [![Code style](https://img.shields.io/badge/style-ruff-41B5BE?style=flat)](https://github.com/astral-sh/ruff) [![Code coverage](https://img.shields.io/codecov/c/github/vacanza/holidays/dev?color=41B5BE&style=flat)](https://app.codecov.io/gh/vacanza/holidays) |
| GitHub   | [![GitHub stars](https://img.shields.io/github/stars/vacanza/holidays?color=41BE4A&style=flat)](https://github.com/vacanza/holidays/stargazers) [![GitHub forks](https://img.shields.io/github/forks/vacanza/holidays?color=41BE4A&style=flat)](https://github.com/vacanza/holidays/forks) [![GitHub contributors](https://img.shields.io/github/contributors/vacanza/holidays?color=41BE4A&style=flat)](https://github.com/vacanza/holidays/graphs/contributors) [![GitHub last commit](https://img.shields.io/github/last-commit/vacanza/holidays/dev?color=41BE4A&style=flat)](https://github.com/vacanza/holidays/commits/dev) |
| Citation | [![Open World Holidays Franework DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.14847397-41B5BE?style=flat)](https://doi.org/10.5281/zenodo.14847397) |

## Install

The latest stable version can always be installed or updated via pip:

``` shell
$ pip install --upgrade holidays
```

The latest development (dev) version can be installed directly from
GitHub:

``` shell
$ pip install --upgrade https://github.com/vacanza/holidays/tarball/dev
```

All new features are always first pushed to dev branch, then released on
main branch upon official version upgrades.

## Documentation

The documentation is hosted on [Read the
Docs](https://holidays.readthedocs.io/).

## Quick Start

``` python
from datetime import date
import holidays

us_holidays = holidays.US()  # this is a dict-like object
# the below is the same, but takes a string:
us_holidays = holidays.country_holidays('US')  # this is a dict-like object

nyse_holidays = holidays.NYSE()  # this is a dict-like object
# the below is the same, but takes a string:
nyse_holidays = holidays.financial_holidays('NYSE')  # this is a dict-like object

date(2015, 1, 1) in us_holidays  # True
date(2015, 1, 2) in us_holidays  # False
us_holidays.get('2014-01-01')  # "New Year's Day"
```

The HolidayBase dict-like class will also recognize date strings and
Unix timestamps:

``` python
'2014-01-01' in us_holidays  # True
'1/1/2014' in us_holidays    # True
1388597445 in us_holidays    # True
```

Some holidays may be only present in parts of a country:

``` python
us_pr_holidays = holidays.country_holidays('US', subdiv='PR')
'2018-01-06' in us_holidays     # False
'2018-01-06' in us_pr_holidays  # True
```

Please see the [holidays
documentation](https://holidays.readthedocs.io/) for additional examples
and detailed information.

## Available Countries

We currently support 158 country codes. The standard way to refer to a
country is by using its [ISO 3166-1 alpha-2
code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes), the
same used for domain names, and for a subdivision its [ISO 3166-2
code](https://en.wikipedia.org/wiki/ISO_3166-2). Some countries have
common or foreign names or abbreviations as aliases for their
subdivisions. These are defined in the (optional) `subdivisions_aliases`
attribute. Some of the countries support more than one language for
holiday names output. A default language is defined by
`default_language` (optional) attribute for each entity and is used as a
fallback when neither user specified language nor user locale language
available. The default language code is a [ISO 639-1
code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). A list of
all languages supported by country is defined by `supported_languages`
(optional) attribute. If there is no designated [ISO 639-1
code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) then [ISO
639-2 code](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) can
be used.

Many countries have other categories of holidays in addition to common
(national-wide) holidays: bank holidays, school holidays, additional
(paid or non-paid) holidays, holidays of state or public employees,
religious holidays (valid only for these religions followers). A list of
all categories supported by country is defined by `supported_categories`
(optional) attribute.

The following is a list of supported countries, their subdivisions
followed by their aliases (if any) in brackets, available languages and
additional holiday categories. All countries support **PUBLIC** holidays
category by default. All other default values are highlighted with bold:

| Country        |  Code  | Subdivisions  |     Supported Languages    |     Supported Categories |
|----------------|--------|---------------|----------------------------|--------------------------|
| Afghanistan    |  AF    |               |    en_US, **fa_AF**, ps_AF |                          |
| Albania        |  AL    |               |    en_US, **sq**, uk       |                          |
| Algeria        |  DZ    |               |    **ar**, en_US, fr       |                          |
| American <br> Samoa |  AS    | Can also be loaded as <br> country US, <br> subdivision AS |   | UNOFFICIAL
| Andorra        |  AD    |  Parishes: 02, 03, 04, <br> 05, 06, 07, 08 |   |   |
| Angola         |  AO    |               |    en_US, **pt_AO**, uk    |   |   |
| Argentina      |  AR    |               |    en_US, **es**, uk       |   |   |
| Armenia        |  AM    |               |    en_US, **hy**           |   |   |
| Aruba          |  AW    |               |    en_US, nl, **pap_AW**, uk |  |  |
| Australia      |  AU    |  States and territories: <br> ACT (Australian <br> Capital Territory), <br> NSW (New South <br> Wales), NT (Northern <br> Territory), QLD <br> (Queensland), SA <br> (South Australia), TAS <br> (Tasmania), VIC <br> (Victoria), WA <br> (Western Australia) | **en_AU**, en_US, th  | BANK, HALF_DAY |
| Austria        |  AT    |  States: 1 (Burgenland, <br> Bgld, B), 2 (Kärnten, <br> Ktn, K), 3 <br> (Niederösterreich, <br> NÖ, N), 4 <br> (Oberösterreich, OÖ, <br>  O), 5 (Salzburg, Sbg, <br> S), 6 (Steiermark, <br> Stmk, St), 7 (Tirol, T), <br> 8 (Vorarlberg, Vbg, V), <br> 9 (Wien, W) | **de**, en_US, uk | BANK |
| Azerbaijan     |  AZ     |      | **az**, en_US, uk | WORKDAY |

Bahamas         BS

Bahrain         BH                                      **ar**, en_US

Bangladesh      BD

Barbados        BB

Belarus         BY                                      **be**, en_US, WORKDAY
                                                      ru, th

Belgium         BE                                      de, en_US, fr, BANK
                                                      **nl**, uk

Belize          BZ

Bolivia         BO     Departments: B, C, H, L, N, O,   en_US, **es**,
                     P, S, T                          uk

Bosnia and      BA     Entities and district: BIH       **bs**, en_US,
Herzegovina            (Federacija Bosne i Hercegovine, sr, uk
                     FBiH), BRC (Brčko distrikt, BD),
                     SRP (Republika Srpska, RS)

Botswana        BW

Brazil          BR     States: AC (Acre), AL (Alagoas), en_US,         OPTIONAL
                     AM (Amazonas), AP (Amapá), BA    **pt_BR**, uk
                     (Bahia), CE (Ceará), DF
                     (Distrito Federal), ES (Espírito
                     Santo), GO (Goiás), MA
                     (Maranhão), MG (Minas Gerais),
                     MS (Mato Grosso do Sul), MT
                     (Mato Grosso), PA (Pará), PB
                     (Paraíba), PE (Pernambuco), PI
                     (Piauí), PR (Paraná), RJ (Rio de
                     Janeiro), RN (Rio Grande do
                     Norte), RO (Rondônia), RR
                     (Roraima), RS (Rio Grande do
                     Sul), SC (Santa Catarina), SE
                     (Sergipe), SP (São Paulo), TO
                     (Tocantins)

Brunei          BN                                      en_US, **ms**,
                                                      th

Bulgaria        BG                                      **bg**, en_US, SCHOOL
                                                      uk

Burkina Faso    BF

Burundi         BI

Cambodia        KH                                      en_US, **km**,
                                                      th

Cameroon        CM

Canada          CA     Provinces and territories: AB,   ar, **en_CA**, GOVERNMENT,
                     BC, MB, NB, NL, NS, NT, NU, ON,  en_US, fr, th  OPTIONAL
                     PE, QC, SK, YT

Chad            TD

Chile           CL     Regions: AI, AN, AP, AR, AT, BI, en_US, **es**, BANK
                     CO, LI, LL, LR, MA, ML, NB, RM,  uk
                     TA, VS

China           CN                                      en_US, th,     HALF_DAY
                                                      **zh_CN**,
                                                      zh_TW

Colombia        CO                                      en_US, **es**,
                                                      uk

Congo           CG                                      en_US, **fr**

Costa Rica      CR                                      en_US, **es**, OPTIONAL
                                                      uk

Croatia         HR                                      en_US, **hr**,
                                                      uk

Cuba            CU                                      en_US, **es**,
                                                      uk

Curacao         CW                                      en_US, nl,     HALF_DAY
                                                      **pap_CW**, uk

Cyprus          CY                                      **el**, en_CY, BANK, OPTIONAL
                                                      en_US, uk

Czechia         CZ                                      **cs**, en_US,
                                                      sk, uk

Denmark         DK                                      **da**, en_US, OPTIONAL
                                                      uk

Djibouti        DJ                                      ar, en_US,
                                                      **fr**

Dominica        DM

Dominican       DO                                      en_US, **es**,
Republic                                                uk

Ecuador         EC                                      en_US, **es**,
                                                      uk

Egypt           EG                                      **ar**, en_US

El Salvador     SV     Departments: AH (Ahuachapán), CA en_US, **es**,
                     (Cabañas), CH (Chalatenango), CU uk
                     (Cuscatlán), LI (La Libertad),
                     MO (Morazán), PA (La Paz), SA
                     (Santa Ana), SM (San Miguel), SO
                     (Sonsonate), SS (San Salvador),
                     SV (San Vicente), UN (La Unión),
                     US (Usulután)

Estonia         EE                                      en_US, **et**,
                                                      uk

Eswatini        SZ

Ethiopia        ET                                      **am**, ar,
                                                      en_US

Finland         FI                                      en_US, **fi**, UNOFFICIAL
                                                      sv_FI, uk

France          FR     DOM/TOM: BL (Saint-Barthélemy),  en_US, **fr**,
                     GES (Alsace, Champagne-Ardenne,  uk
                     Lorraine), GP (Guadeloupe), GY
                     (Guyane), MF (Saint-Martin), MQ
                     (Martinique), NC
                     (Nouvelle-Calédonie), PF
                     (Polynésie Française), RE (La
                     Réunion), WF (Wallis-et-Futuna),
                     YT (Mayotte)

Gabon           GA

Georgia         GE                                      en_US, **ka**, GOVERNMENT
                                                      uk

Germany         DE     States: BB (Brandenburg), BE     **de**, en_US, CATHOLIC
                     (Berlin), BW                     th, uk
                     (Baden-Württemberg), BY
                     (Bayern), HB (Bremen), HE
                     (Hessen), HH (Hamburg), MV
                     (Mecklenburg-Vorpommern), NI
                     (Niedersachsen), NW
                     (Nordrhein-Westfalen), RP
                     (Rheinland-Pfalz), SH
                     (Schleswig-Holstein), SL
                     (Saarland), SN (Sachsen), ST
                     (Sachsen-Anhalt), TH (Thüringen)

Ghana           GH

Greece          GR                                      **el**, en_US, HALF_DAY
                                                      uk

Greenland       GL                                      da, en_US,     OPTIONAL
                                                      **kl**

Guam            GU     Can also be loaded as country                   UNOFFICIAL
                     US, subdivision GU

Guatemala       GT                                      en_US, **es**

Guernsey        GG

Haiti           HT                                      en_US, es,     OPTIONAL
                                                      **fr_HT**, ht

Honduras        HN                                      en_US, **es**,
                                                      uk

Hong Kong       HK                                      en_HK, en_US,  OPTIONAL
                                                      th, zh_CN,
                                                      **zh_HK**

Hungary         HU                                      en_US, **hu**,
                                                      uk

Iceland         IS                                      en_US, **is**, HALF_DAY
                                                      uk

India           IN     States: AN, AP, AR, AS, BR, CG,
                     CH, DH, DL, GA, GJ, HP, HR, JH,
                     JK, KA, KL, LA, LD, MH, ML, MN,
                     MP, MZ, NL, OD, PB, PY, RJ, SK,
                     TN, TR, TS, UK, UP, WB

Indonesia       ID                                      en_US, **id**, GOVERNMENT
                                                      th, uk

Iran            IR                                      en_US,
                                                      **fa_IR**

Ireland         IE

Isle of Man     IM                                      **en_GB**,
                                                      en_US, th

Israel          IL                                      en_US, **he**, OPTIONAL,
                                                      th, uk         SCHOOL

Italy           IT     Provinces: AG (Agrigento), AL
                     (Alessandria), AN (Ancona), AO
                     (Aosta), AP (Ascoli Piceno), AQ
                     (L\'Aquila), AR (Arezzo), AT
                     (Asti), AV (Avellino), BA
                     (Bari), BG (Bergamo), BI
                     (Biella), BL (Belluno), BN
                     (Benevento), BO (Bologna), BR
                     (Brindisi), BS (Brescia), BT
                     (Barletta-Andria-Trani), BZ
                     (Bolzano), CA (Cagliari), CB
                     (Campobasso), CE (Caserta), CH
                     (Chieti), CL (Caltanissetta), CN
                     (Cuneo), CO (Como), CR
                     (Cremona), CS (Cosenza), CT
                     (Catania), CZ (Catanzaro), EN
                     (Enna), FC (Forli-Cesena,
                     Forlì-Cesena), FE (Ferrara), FG
                     (Foggia), FI (Firenze), FM
                     (Fermo), FR (Frosinone), GE
                     (Genova), GO (Gorizia), GR
                     (Grosseto), IM (Imperia), IS
                     (Isernia), KR (Crotone), LC
                     (Lecco), LE (Lecce), LI
                     (Livorno), LO (Lodi), LT
                     (Latina), LU (Lucca), MB (Monza
                     e Brianza), MC (Macerata), ME
                     (Messina), MI (Milano), MN
                     (Mantova), MO (Modena), MS
                     (Massa-Carrara), MT (Matera), NA
                     (Napoli), NO (Novara), NU
                     (Nuoro), OR (Oristano), PA
                     (Palermo), PC (Piacenza), PD
                     (Padova), PE (Pescara), PG
                     (Perugia), PI (Pisa), PN
                     (Pordenone), PO (Prato), PR
                     (Parma), PT (Pistoia), PU
                     (Pesaro e Urbino), PV (Pavia),
                     PZ (Potenza), RA (Ravenna), RC
                     (Reggio Calabria), RE (Reggio
                     Emilia), RG (Ragusa), RI
                     (Rieti), RM (Roma), RN (Rimini),
                     RO (Rovigo), SA (Salerno), SI
                     (Siena), SO (Sondrio), SP (La
                     Spezia), SR (Siracusa), SS
                     (Sassari), SU (Sud Sardegna), SV
                     (Savona), TA (Taranto), TE
                     (Teramo), TN (Trento), TO
                     (Torino), TP (Trapani), TR
                     (Terni), TS (Trieste), TV
                     (Treviso), UD (Udine), VA
                     (Varese), VB
                     (Verbano-Cusio-Ossola), VC
                     (Vercelli), VE (Venezia), VI
                     (Vicenza), VR (Verona), VT
                     (Viterbo), VV (Vibo Valentia).
                     Cities: Andria, Barletta,
                     Cesena, Forli (Forlì), Pesaro,
                     Trani, Urbino

Jamaica         JM

Japan           JP                                      en_US, **ja**, BANK
                                                      th

Jersey          JE

Jordan          JO                                      **ar**, en_US

Kazakhstan      KZ                                      en_US, **kk**,
                                                      uk

Kenya           KE

Kuwait          KW                                      **ar**, en_US

Kyrgyzstan      KG

Laos            LA                                      en_US, **lo**, BANK, SCHOOL,
                                                      th             WORKDAY

Latvia          LV                                      en_US, **lv**,
                                                      uk

Lesotho         LS

Liechtenstein   LI                                      **de**, en_US, BANK
                                                      uk

Lithuania       LT                                      en_US, **lt**,
                                                      uk

Luxembourg      LU                                      de, en_US, fr,
                                                      **lb**, uk

Madagascar      MG                                      en_US, **mg**,
                                                      uk

Malawi          MW

Malaysia        MY     States and federal territories:  en_US,
                     01 (Johor, JHR), 02 (Kedah,      **ms_MY**, th
                     KDH), 03 (Kelantan, KTN), 04
                     (Melaka, MLK), 05 (Negeri
                     Sembilan, NSN), 06 (Pahang,
                     PHG), 07 (Pulau Pinang, PNG), 08
                     (Perak, PRK), 09 (Perlis, PLS),
                     10 (Selangor, SGR), 11
                     (Terengganu, TRG), 12 (Sabah,
                     SBH), 13 (Sarawak, SWK), 14 (WP
                     Kuala Lumpur, KUL), 15 (WP
                     Labuan, LBN), 16 (WP Putrajaya,
                     PJY)

Maldives        MV

Malta           MT                                      en_US, **mt**

Marshall        MH
Islands (the)

Mauritania      MR

Mexico          MX                                      en_US, **es**,
                                                      uk

Moldova         MD                                      en_US, **ro**,
                                                      uk

Monaco          MC                                      en_US, **fr**,
                                                      uk

Montenegro      ME                                      **cnr**,       CATHOLIC,
                                                      en_US, uk      HEBREW,
                                                                     ISLAMIC,
                                                                     ORTHODOX,
                                                                     WORKDAY

Morocco         MA                                      **ar**, en_US,
                                                      fr

Mozambique      MZ                                      en_US,
                                                      **pt_MZ**, uk

Namibia         NA

Netherlands     NL                                      en_US, fy,     OPTIONAL
                                                      **nl**, uk

New Zealand     NZ     Regions and Special Island
                     Authorities: AUK (Auckland,
                     Tāmaki-Makaurau, AU), BOP (Bay
                     of Plenty, Toi Moana, BP), CAN
                     (Canterbury, Waitaha, CA), CIT
                     (Chatham Islands Territory,
                     Chatham Islands, Wharekauri,
                     CI), GIS (Gisborne, Te
                     Tairāwhiti, GI), HKB (Hawke\'s
                     Bay, Te Matau-a-Māui, HB), MBH
                     (Marlborough, MA), MWT (Manawatū
                     Whanganui, Manawatū-Whanganui,
                     MW), NSN (Nelson, Whakatū, NE),
                     NTL (Northland, Te Taitokerau,
                     NO), OTA (Otago, Ō Tākou, OT),
                     STL (Southland, Te Taiao Tonga,
                     SO), TAS (Tasman, Te tai o
                     Aorere, TS), TKI (Taranaki, TK),
                     WGN (Greater Wellington, Te Pane
                     Matua Taiao, Wellington, Te
                     Whanganui-a-Tara, WG), WKO
                     (Waikato, WK), WTC (West Coast,
                     Te Tai o Poutini, WC).
                     Subregions: South Canterbury

Nicaragua       NI     Subdivisions: AN (Costa Caribe   en_US, **es**,
                     Norte), AS (Costa Caribe Sur),   uk
                     BO (Boaco), CA (Carazo), CI
                     (Chinandega), CO (Chontales), ES
                     (Estelí), GR (Granada), JI
                     (Jinotega), LE (León), MD
                     (Madriz), MN (Managua), MS
                     (Masaya), MT (Matagalpa), NS
                     (Nueva Segovia), RI (Rivas), SJ
                     (Río San Juan)

Nigeria         NG

Northern        MP     Can also be loaded as country                   UNOFFICIAL
Mariana Islands        US, subdivision MP
(the)

North Macedonia MK

Norway          NO                                      en_US, **no**,
                                                      th, uk

Pakistan        PK

Palau           PW                                                     ARMED_FORCES,
                                                                     HALF_DAY

Panama          PA                                      en_US, **es**, BANK
                                                      uk

Papua New       PG
Guinea

Paraguay        PY                                      en_US, **es**, GOVERNMENT
                                                      uk

Peru            PE                                      en_US, **es**,
                                                      uk

Philippines     PH                                      **en_PH**,     WORKDAY
                                                      en_US, fil, th

Poland          PL                                      en_US, **pl**,
                                                      uk

Portugal        PT     Districts: 01 (Aveiro), 02       en_US,         OPTIONAL
                     (Beja), 03 (Braga), 04           **pt_PT**, uk
                     (Bragança), 05 (Castelo Branco),
                     06 (Coimbra), 07 (Évora), 08
                     (Faro), 09 (Guarda), 10
                     (Leiria), 11 (Lisboa), 12
                     (Portalegre), 13 (Porto), 14
                     (Santarém), 15 (Setúbal), 16
                     (Viana do Castelo), 17 (Vila
                     Real), 18 (Viseu), 20 (Região
                     Autónoma dos Açores), 30 (Região
                     Autónoma da Madeira)

Puerto Rico     PR     Can also be loaded as country                   UNOFFICIAL
                     US, subdivision PR

Romania         RO                                      en_US, **ro**,
                                                      uk

Russia          RU                                      en_US, **ru**,
                                                      th

Saint Kitts and KN                                                     HALF_DAY,
Nevis                                                                  WORKDAY

Saint Lucia     LC                                      **en_LC**,
                                                      en_US

Samoa           WS

San Marino      SM

Saudi Arabia    SA                                      **ar**, en_US

Serbia          RS                                      en_US, **sr**

Seychelles      SC                                      **en_SC**,
                                                      en_US

Singapore       SG                                      **en_SG**,
                                                      en_US, th

Slovakia        SK                                      en_US, **sk**, WORKDAY
                                                      uk

Slovenia        SI                                      en_US, **sl**, WORKDAY
                                                      uk

South Africa    ZA

South Korea     KR                                      en_US, **ko**, BANK
                                                      th

Spain           ES     Autonomous communities: AN, AR,  en_US, **es**,
                     AS, CB, CE, CL, CM, CN, CT, EX,  uk
                     GA, IB, MC, MD, ML, NC, PV, RI,
                     VC

Sri Lanka       LK                                      en_US,         BANK,
                                                      **si_LK**,     GOVERNMENT,
                                                      ta_LK          WORKDAY

Sweden          SE                                      en_US, **sv**,
                                                      th, uk

Switzerland     CH     Cantons: AG, AI, AR, BL, BS, BE, **de**, en_US, HALF_DAY,
                     FR, GE, GL, GR, JU, LU, NE, NW,  fr, it, uk     OPTIONAL
                     OW, SG, SH, SZ, SO, TG, TI, UR,
                     VD, VS, ZG, ZH

Taiwan          TW                                      en_US, th,
                                                      zh_CN,
                                                      **zh_TW**

Tanzania        TZ                                      en_US, **sw**  BANK

Thailand        TH                                      en_US, **th**  ARMED_FORCES,
                                                                     BANK,
                                                                     GOVERNMENT,
                                                                     SCHOOL, WORKDAY

Timor Leste     TL                                      en_US,         GOVERNMENT,
                                                      **pt_TL**, tet WORKDAY

Tonga           TO                                      en_US, **to**

Tunisia         TN                                      **ar**, en_US

Turkey          TR                                      en_US, **tr**, HALF_DAY
                                                      uk

Ukraine         UA                                      ar, en_US, th, WORKDAY
                                                      **uk**

United Arab     AE                                      **ar**, en_US, GOVERNMENT,
Emirates                                                th             OPTIONAL

United Kingdom  GB     Subdivisions: ENG (England), NIR **en_GB**,
                     (Northern Ireland), SCT          en_US, th
                     (Scotland), WLS (Wales)

United States   UM     Can also be loaded as country                   UNOFFICIAL
Minor Outlying         US, subdivision UM
Islands

United States   US     States and territories: AK, AL,                 UNOFFICIAL
of America             AR, AS, AZ, CA, CO, CT, DC, DE,
(the)                  FL, GA, GU, HI, IA, ID, IL, IN,
                     KS, KY, LA, MA, MD, ME, MI, MN,
                     MO, MP, MS, MT, NC, ND, NE, NH,
                     NJ, NM, NV, NY, OH, OK, OR, PA,
                     PR, RI, SC, SD, TN, TX, UM, UT,
                     VA, VI, VT, WA, WI, WV, WY

United States          See Virgin Islands (U.S.)                       UNOFFICIAL
Virgin Islands
(the)

Uruguay         UY                                      en_US, **es**, BANK
                                                      uk

Uzbekistan      UZ                                      en_US, uk,
                                                      **uz**

Vanuatu         VU

Vatican City    VA                                      en_US, **it**,
                                                      th

Venezuela       VE                                      en_US, **es**,
                                                      uk

Vietnam         VN                                      en_US, th,
                                                      **vi**

Virgin Islands  VI     Can also be loaded as country                   UNOFFICIAL
(U.S.)                 US, subdivision VI

Zambia          ZM

Zimbabwe        ZW
--------------------------------------------------------------------------------------

### Available Financial Markets

The standard way to refer to a financial market is to use its [ISO 10383
MIC](https://www.iso20022.org/market-identifier-codes) (Market
Identifier Code) as a "country" code when available. The following
financial markets are available:

  ------------------------------------------------------------------------------
  Entity       Code   Info                                          Supported
                                                                    Languages
  ------------ ------ --------------------------------------------- ------------
  Brasil,      BVMF   Brazil Stock Exchange and Over-the-Counter    en_US,
  Bolsa,              Market holidays (same as ANBIMA holidays)     **pt_BR**,
  Balcão                                                            uk

  European     XECB   Trans-European Automated Real-time Gross
  Central Bank        Settlement (TARGET2)

  ICE Futures  IFEU   A London-based Investment Exchange holidays
  Europe

  New York     XNYS   NYSE market holidays (used by all other
  Stock               US-exchanges, including NASDAQ, etc.)
  Exchange
  ------------------------------------------------------------------------------

## Contributions

[Issues](https://github.com/vacanza/holidays/issues) and [pull
requests](https://github.com/vacanza/holidays/pulls) are always welcome.
Please see
[here](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTING.rst)
for more information.

## License

Code and documentation are available according to the MIT License (see
[LICENSE](https://github.com/vacanza/holidays/blob/dev/LICENSE)).
