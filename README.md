# Holidays

A fast, efficient Python library for generating country- and subdivision- (e.g. state or province)
specific sets of government-designated holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.

<!-- markdownlint-disable MD033 -->
<table>
  <tr>
    <td>PyPI</td>
    <td>
      <a href="https://pypi.org/project/holidays"><img src="https://img.shields.io/pypi/dm/holidays?color=41B5BE&style=flat" alt="PyPI downloads"></a>&nbsp;<a href="https://pypi.org/project/holidays"><img src="https://img.shields.io/pypi/v/holidays?color=41B5BE&label=version&style=flat" alt="PyPI version"></a>&nbsp;<a href="https://github.com/vacanza/holidays/releases"><img src="https://img.shields.io/github/release-date/vacanza/holidays?color=41B5BE&style=flat" alt="PyPI release date"></a>
    </td>
  </tr>
  <tr>
    <td>CI/CD</td>
    <td>
      <a href="https://github.com/vacanza/holidays/actions/workflows/ci-cd.yml?query=branch%3Adev"><img src="https://img.shields.io/github/actions/workflow/status/vacanza/holidays/ci-cd.yml?branch=dev&color=41BE4A&style=flat" alt="CI/CD status"></a>&nbsp;<a href="https://holidays.readthedocs.io/en/latest/?badge=latest"><img src="https://img.shields.io/readthedocs/holidays?color=41BE4A&style=flat" alt="Documentation status"></a>
    </td>
  </tr>
  <tr>
    <td>Code</td>
    <td>
      <a href="https://github.com/vacanza/holidays/blob/dev/LICENSE"><img src="https://img.shields.io/github/license/vacanza/holidays?color=41B5BE&style=flat" alt="License"></a>&nbsp;<a href="https://pypi.org/project/holidays"><img src="https://img.shields.io/pypi/pyversions/holidays?label=python&color=41B5BE&style=flat" alt="Python supported versions"></a>&nbsp;<a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/badge/style-ruff-41B5BE?style=flat" alt="Code style"></a>&nbsp;<a href="https://app.codecov.io/gh/vacanza/holidays"><img src="https://img.shields.io/codecov/c/github/vacanza/holidays/dev?color=41B5BE&style=flat" alt="Code coverage"></a>
    </td>
  </tr>
  <tr>
    <td>GitHub</td>
    <td>
      <a href="https://github.com/vacanza/holidays/stargazers"><img src="https://img.shields.io/github/stars/vacanza/holidays?color=41BE4A&style=flat" alt="GitHub stars"></a>&nbsp;<a href="https://github.com/vacanza/holidays/forks"><img src="https://img.shields.io/github/forks/vacanza/holidays?color=41BE4A&style=flat" alt="GitHub forks"></a>&nbsp;<a href="https://github.com/vacanza/holidays/graphs/contributors"><img src="https://img.shields.io/github/contributors/vacanza/holidays?color=41BE4A&style=flat" alt="GitHub contributors"></a>&nbsp;<a href="https://github.com/vacanza/holidays/commits/dev"><img src="https://img.shields.io/github/last-commit/vacanza/holidays/dev?color=41BE4A&style=flat" alt="GitHub last commit"></a>
    </td>
  </tr>
  <tr>
    <td>Citation</td>
    <td>
      <a href="https://doi.org/10.5281/zenodo.14884702"><img src="https://img.shields.io/badge/DOI-10.5281/zenodo.14884702-41B5BE?style=flat" alt="Open World Holidays Framework DOI"></a>
    </td>
  </tr>
</table>

## Install

The latest stable version can always be installed or updated via pip:

``` shell
pip install --upgrade holidays
```

The latest development (dev) version can be installed directly from GitHub:

``` shell
pip install --upgrade https://github.com/vacanza/holidays/tarball/dev
```

All new features are always first pushed to dev branch, then released on main branch upon official
version upgrades.

## Documentation

The documentation is hosted on [Read the Docs](https://holidays.readthedocs.io/).

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

The HolidayBase dict-like class will also recognize date strings and Unix timestamps:

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

Please see the [holidays documentation](https://holidays.readthedocs.io/) for additional examples
and detailed information.

## Available Countries

We currently support 165 country codes. The standard way to refer to a country is by using its [ISO
3166-1 alpha-2 code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes), the same used
for domain names, and for a subdivision its [ISO 3166-2
code](https://en.wikipedia.org/wiki/ISO_3166-2). Some countries have common or foreign names or
abbreviations as aliases for their subdivisions. These are defined in the (optional)
`subdivisions_aliases` attribute. Some of the countries support more than one language for holiday
names output. A default language is defined by `default_language` (optional) attribute for each
entity and is used as a fallback when neither user specified language nor user locale language
available. The default language code is a [ISO 639-1
code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). A list of all languages supported by
country is defined by `supported_languages` (optional) attribute. If there is no designated [ISO
639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) then [ISO 639-2
code](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) can be used.

Many countries have other categories of holidays in addition to common (national-wide) holidays:
bank holidays, school holidays, additional (paid or non-paid) holidays, holidays of state or public
employees, religious holidays (valid only for these religions followers). A list of all categories
supported by country is defined by `supported_categories` (optional) attribute.

The following is a list of supported countries, their subdivisions followed by their aliases (if
any) in brackets, available languages and additional holiday categories. All countries support
**PUBLIC** holidays category by default. All other default values are highlighted with bold:

<table style="width: 100%">
<colgroup>
<col style="width: 20.0%" />
<col style="width: 4.0%" />
<col style="width: 46.0%" />
<col style="width: 20.0%" />
<col style="width: 10.0%" />
</colgroup>
<thead>
<tr>
<th>Country</th>
<th>Code</th>
<th>Subdivisions</th>
<th>Supported Languages</th>
<th>Supported Categories</th>
</tr>
</thead>
<tbody>
<tr>
<td>Afghanistan</td>
<td>AF</td>
<td></td>
<td>en_US, <strong>fa_AF</strong>, ps_AF</td>
<td></td>
</tr>
<tr>
<td>Albania</td>
<td>AL</td>
<td></td>
<td>en_US, <strong>sq</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Algeria</td>
<td>DZ</td>
<td></td>
<td><strong>ar</strong>, en_US, fr</td>
<td></td>
</tr>
<tr>
<td>American Samoa</td>
<td>AS</td>
<td>Can also be loaded as country US, subdivision AS</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>Andorra</td>
<td>AD</td>
<td>Parishes: 02, 03, 04, 05, 06, 07, 08</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Angola</td>
<td>AO</td>
<td></td>
<td>en_US, <strong>pt_AO</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Antigua and Barbuda</td>
<td>AG</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Argentina</td>
<td>AR</td>
<td>Provinces: A (Salta), B (Buenos Aires), C (Ciudad Autónoma de Buenos Aires), D (San Luis), E (Entre Ríos), F (La Rioja), G (Santiago del Estero), H (Chaco), J (San Juan), K (Catamarca), L (La Pampa), M (Mendoza), N (Misiones), P (Formosa), Q (Neuquén), R (Río Negro), S (Santa Fe), T (Tucumán), U (Chubut), V (Tierra del Fuego), W (Corrientes), X (Córdoba), Y (Jujuy), Z (Santa Cruz)</td>
<td>en_US, <strong>es</strong>, uk</td>
<td>ARMENIAN, BANK, GOVERNMENT, HEBREW, ISLAMIC</td>
</tr>
<tr>
<td>Armenia</td>
<td>AM</td>
<td></td>
<td>en_US, <strong>hy</strong></td>
<td></td>
</tr>
<tr>
<td>Aruba</td>
<td>AW</td>
<td></td>
<td>en_US, nl, <strong>pap_AW</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Australia</td>
<td>AU</td>
<td>States and territories: ACT (Australian Capital Territory), NSW (New South Wales), NT (Northern Territory), QLD (Queensland), SA (South Australia), TAS (Tasmania), VIC (Victoria), WA (Western Australia)</td>
<td><strong>en_AU</strong>, en_US, th</td>
<td>BANK, HALF_DAY</td>
</tr>
<tr>
<td>Austria</td>
<td>AT</td>
<td>States: 1 (Burgenland, Bgld, B), 2 (Kärnten, Ktn, K), 3 (Niederösterreich, NÖ, N), 4 (Oberösterreich, OÖ, O), 5 (Salzburg, Sbg, S), 6 (Steiermark, Stmk, St), 7 (Tirol, T), 8 (Vorarlberg, Vbg, V), 9 (Wien, W)</td>
<td><strong>de</strong>, en_US, uk</td>
<td>BANK</td>
</tr>
<tr>
<td>Azerbaijan</td>
<td>AZ</td>
<td></td>
<td><strong>az</strong>, en_US, uk</td>
<td>WORKDAY</td>
</tr>
<tr>
<td>Bahamas</td>
<td>BS</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bahrain</td>
<td>BH</td>
<td></td>
<td><strong>ar</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Bangladesh</td>
<td>BD</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Barbados</td>
<td>BB</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Belarus</td>
<td>BY</td>
<td></td>
<td><strong>be</strong>, en_US, ru, th</td>
<td>WORKDAY</td>
</tr>
<tr>
<td>Belgium</td>
<td>BE</td>
<td></td>
<td>de, en_US, fr, <strong>nl</strong>, uk</td>
<td>BANK</td>
</tr>
<tr>
<td>Belize</td>
<td>BZ</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bolivia</td>
<td>BO</td>
<td>Departments: B, C, H, L, N, O, P, S, T</td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Bosnia and Herzegovina</td>
<td>BA</td>
<td>Entities and district: BIH (Federacija Bosne i Hercegovine, FBiH), BRC (Brčko distrikt, BD), SRP (Republika Srpska, RS)</td>
<td><strong>bs</strong>, en_US, sr, uk</td>
<td></td>
</tr>
<tr>
<td>Botswana</td>
<td>BW</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Brazil</td>
<td>BR</td>
<td>States: AC (Acre), AL (Alagoas), AM (Amazonas), AP (Amapá), BA (Bahia), CE (Ceará), DF (Distrito Federal), ES (Espírito Santo), GO (Goiás), MA (Maranhão), MG (Minas Gerais), MS (Mato Grosso do Sul), MT (Mato Grosso), PA (Pará), PB (Paraíba), PE (Pernambuco), PI (Piauí), PR (Paraná), RJ (Rio de Janeiro), RN (Rio Grande do Norte), RO (Rondônia), RR (Roraima), RS (Rio Grande do Sul), SC (Santa Catarina), SE (Sergipe), SP (São Paulo), TO (Tocantins)</td>
<td>en_US, <strong>pt_BR</strong>, uk</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Brunei</td>
<td>BN</td>
<td></td>
<td>en_US, <strong>ms</strong>, th</td>
<td></td>
</tr>
<tr>
<td>Bulgaria</td>
<td>BG</td>
<td></td>
<td><strong>bg</strong>, en_US, uk</td>
<td>SCHOOL</td>
</tr>
<tr>
<td>Burkina Faso</td>
<td>BF</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Burundi</td>
<td>BI</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Cambodia</td>
<td>KH</td>
<td></td>
<td>en_US, <strong>km</strong>, th</td>
<td></td>
</tr>
<tr>
<td>Cameroon</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Canada</td>
<td>CA</td>
<td>Provinces and territories: AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT</td>
<td>ar, <strong>en_CA</strong>, en_US, fr, th</td>
<td>GOVERNMENT, OPTIONAL</td>
</tr>
<tr>
<td>Chad</td>
<td>TD</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Chile</td>
<td>CL</td>
<td>Regions: AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA, ML, NB, RM, TA, VS</td>
<td>en_US, <strong>es</strong>, uk</td>
<td>BANK</td>
</tr>
<tr>
<td>China</td>
<td>CN</td>
<td></td>
<td>en_US, th, <strong>zh_CN</strong>, zh_TW</td>
<td>HALF_DAY</td>
</tr>
<tr>
<td>Colombia</td>
<td>CO</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Congo</td>
<td>CG</td>
<td></td>
<td>en_US, <strong>fr</strong></td>
<td></td>
</tr>
<tr>
<td>Costa Rica</td>
<td>CR</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Croatia</td>
<td>HR</td>
<td></td>
<td>en_US, <strong>hr</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Cuba</td>
<td>CU</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Curacao</td>
<td>CW</td>
<td></td>
<td>en_US, nl, <strong>pap_CW</strong>, uk</td>
<td>HALF_DAY</td>
</tr>
<tr>
<td>Cyprus</td>
<td>CY</td>
<td></td>
<td><strong>el</strong>, en_CY, en_US, uk</td>
<td>BANK, OPTIONAL</td>
</tr>
<tr>
<td>Czechia</td>
<td>CZ</td>
<td></td>
<td><strong>cs</strong>, en_US, sk, uk</td>
<td></td>
</tr>
<tr>
<td>Denmark</td>
<td>DK</td>
<td></td>
<td><strong>da</strong>, en_US, uk</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Djibouti</td>
<td>DJ</td>
<td></td>
<td>ar, en_US, <strong>fr</strong></td>
<td></td>
</tr>
<tr>
<td>Dominica</td>
<td>DM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Dominican Republic</td>
<td>DO</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Ecuador</td>
<td>EC</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Egypt</td>
<td>EG</td>
<td></td>
<td><strong>ar</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>El Salvador</td>
<td>SV</td>
<td>Departments: AH (Ahuachapán), CA (Cabañas), CH (Chalatenango), CU (Cuscatlán), LI (La Libertad), MO (Morazán), PA (La Paz), SA (Santa Ana), SM (San Miguel), SO (Sonsonate), SS (San Salvador), SV (San Vicente), UN (La Unión), US (Usulután)</td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Estonia</td>
<td>EE</td>
<td></td>
<td>en_US, <strong>et</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Eswatini</td>
<td>SZ</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ethiopia</td>
<td>ET</td>
<td></td>
<td><strong>am</strong>, ar, en_US</td>
<td></td>
</tr>
<tr>
<td>Fiji</td>
<td>FJ</td>
<td></td>
<td></td>
<td>WORKDAY</td>
</tr>
<tr>
<td>Finland</td>
<td>FI</td>
<td></td>
<td>en_US, <strong>fi</strong>, sv_FI, uk</td>
<td>UNOFFICIAL</td>
</tr>
<tr>
<td>France</td>
<td>FR</td>
<td>DOM/TOM: BL (Saint-Barthélemy), GES (Alsace, Champagne-Ardenne, Lorraine), GP (Guadeloupe), GY (Guyane), MF (Saint-Martin), MQ (Martinique), NC (Nouvelle-Calédonie), PF (Polynésie Française), RE (La Réunion), WF (Wallis-et-Futuna), YT (Mayotte)</td>
<td>en_US, <strong>fr</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Gabon</td>
<td>GA</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Georgia</td>
<td>GE</td>
<td></td>
<td>en_US, <strong>ka</strong>, uk</td>
<td>GOVERNMENT</td>
</tr>
<tr>
<td>Germany</td>
<td>DE</td>
<td>States: BB (Brandenburg), BE (Berlin), BW (Baden-Württemberg), BY (Bayern), HB (Bremen), HE (Hessen), HH (Hamburg), MV (Mecklenburg-Vorpommern), NI (Niedersachsen), NW (Nordrhein-Westfalen), RP (Rheinland-Pfalz), SH (Schleswig-Holstein), SL (Saarland), SN (Sachsen), ST (Sachsen-Anhalt), TH (Thüringen)</td>
<td><strong>de</strong>, en_US, th, uk</td>
<td>CATHOLIC</td>
</tr>
<tr>
<td>Ghana</td>
<td>GH</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Greece</td>
<td>GR</td>
<td></td>
<td><strong>el</strong>, en_US, uk</td>
<td>HALF_DAY</td>
</tr>
<tr>
<td>Greenland</td>
<td>GL</td>
<td></td>
<td>da, en_US, fi, is, <strong>kl</strong>, no, sv, uk</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Guam</td>
<td>GU</td>
<td>Can also be loaded as country US, subdivision GU</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>Guatemala</td>
<td>GT</td>
<td></td>
<td>en_US, <strong>es</strong></td>
<td></td>
</tr>
<tr>
<td>Guernsey</td>
<td>GG</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<tr>
<td>Guinea</td>
<td>GN</td>
<td></td>
<td>en_US, <strong>fr</strong></td>
<td></td>
</tr>
<tr>
<td>Haiti</td>
<td>HT</td>
<td></td>
<td>en_US, es, <strong>fr_HT</strong>, ht</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Honduras</td>
<td>HN</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Hong Kong</td>
<td>HK</td>
<td></td>
<td>en_HK, en_US, th, zh_CN, <strong>zh_HK</strong></td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Hungary</td>
<td>HU</td>
<td></td>
<td>en_US, <strong>hu</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Iceland</td>
<td>IS</td>
<td></td>
<td>en_US, <strong>is</strong>, uk</td>
<td>HALF_DAY</td>
</tr>
<tr>
<td>India</td>
<td>IN</td>
<td>States: AN (Andaman and Nicobar Islands), AP (Andhra Pradesh), AR (Arunachal Pradesh, Arunāchal Pradesh), AS (Assam), BR (Bihar, Bihār), CG (Chhattisgarh, Chhattīsgarh), CH (Chandigarh, Chandīgarh), DH (Dadra and Nagar Haveli and Daman and Diu, Dādra and Nagar Haveli and Damān and Diu), DL (Delhi), GA (Goa), GJ (Gujarat, Gujarāt), HP (Himachal Pradesh, Himāchal Pradesh), HR (Haryana, Haryāna), JH (Jharkhand, Jhārkhand), JK (Jammu and Kashmir, Jammu and Kashmīr), KA (Karnataka, Karnātaka), KL (Kerala), LA (Ladakh, Ladākh), LD (Lakshadweep), MH (Maharashtra, Mahārāshtra), ML (Meghalaya, Meghālaya), MN (Manipur), MP (Madhya Pradesh), MZ (Mizoram), NL (Nagaland, Nāgāland), OD (Odisha), PB (Punjab), PY (Puducherry), RJ (Rajasthan, Rājasthān), SK (Sikkim), TN (Tamil Nadu, Tamil Nādu), TR (Tripura), TS (Telangana, Telangāna), UK (Uttarakhand, Uttarākhand), UP (Uttar Pradesh), WB (West Bengal)</td>
<td><strong>en_IN</strong>, en_US, hi</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Indonesia</td>
<td>ID</td>
<td></td>
<td>en_US, <strong>id</strong>, th, uk</td>
<td>GOVERNMENT</td>
</tr>
<tr>
<td>Iran</td>
<td>IR</td>
<td></td>
<td>en_US, <strong>fa_IR</strong></td>
<td></td>
</tr>
<tr>
<td>Ireland</td>
<td>IE</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Isle of Man</td>
<td>IM</td>
<td></td>
<td><strong>en_GB</strong>, en_US, th</td>
<td></td>
</tr>
<tr>
<td>Israel</td>
<td>IL</td>
<td></td>
<td>en_US, <strong>he</strong>, th, uk</td>
<td>OPTIONAL, SCHOOL</td>
</tr>
<tr>
<td>Italy</td>
<td>IT</td>
<td>Provinces: AG (Agrigento), AL (Alessandria), AN (Ancona), AO (Aosta), AP (Ascoli Piceno), AQ (L'Aquila), AR (Arezzo), AT (Asti), AV (Avellino), BA (Bari), BG (Bergamo), BI (Biella), BL (Belluno), BN (Benevento), BO (Bologna), BR (Brindisi), BS (Brescia), BT (Barletta-Andria-Trani), BZ (Bolzano), CA (Cagliari), CB (Campobasso), CE (Caserta), CH (Chieti), CL (Caltanissetta), CN (Cuneo), CO (Como), CR (Cremona), CS (Cosenza), CT (Catania), CZ (Catanzaro), EN (Enna), FC (Forli-Cesena, Forlì-Cesena), FE (Ferrara), FG (Foggia), FI (Firenze), FM (Fermo), FR (Frosinone), GE (Genova), GO (Gorizia), GR (Grosseto), IM (Imperia), IS (Isernia), KR (Crotone), LC (Lecco), LE (Lecce), LI (Livorno), LO (Lodi), LT (Latina), LU (Lucca), MB (Monza e Brianza), MC (Macerata), ME (Messina), MI (Milano), MN (Mantova), MO (Modena), MS (Massa-Carrara), MT (Matera), NA (Napoli), NO (Novara), NU (Nuoro), OR (Oristano), PA (Palermo), PC (Piacenza), PD (Padova), PE (Pescara), PG (Perugia), PI (Pisa), PN (Pordenone), PO (Prato), PR (Parma), PT (Pistoia), PU (Pesaro e Urbino), PV (Pavia), PZ (Potenza), RA (Ravenna), RC (Reggio Calabria), RE (Reggio Emilia), RG (Ragusa), RI (Rieti), RM (Roma), RN (Rimini), RO (Rovigo), SA (Salerno), SI (Siena), SO (Sondrio), SP (La Spezia), SR (Siracusa), SS (Sassari), SU (Sud Sardegna), SV (Savona), TA (Taranto), TE (Teramo), TN (Trento), TO (Torino), TP (Trapani), TR (Terni), TS (Trieste), TV (Treviso), UD (Udine), VA (Varese), VB (Verbano-Cusio-Ossola), VC (Vercelli), VE (Venezia), VI (Vicenza), VR (Verona), VT (Viterbo), VV (Vibo Valentia). Cities: Andria, Barletta, Cesena, Forli (Forlì), Pesaro, Trani, Urbino</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ivory Coast</td>
<td>CI</td>
<td></td>
<td>en_CI, en_US, <strong>fr</strong></td>
<td></td>
</tr>
<tr>
<td>Jamaica</td>
<td>JM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Japan</td>
<td>JP</td>
<td></td>
<td>en_US, <strong>ja</strong>, th</td>
<td>BANK</td>
</tr>
<tr>
<td>Jersey</td>
<td>JE</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Jordan</td>
<td>JO</td>
<td></td>
<td><strong>ar</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Kazakhstan</td>
<td>KZ</td>
<td></td>
<td>en_US, <strong>kk</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Kenya</td>
<td>KE</td>
<td></td>
<td><strong>en_KE</strong>, en_US, sw</td>
<td>HINDU, ISLAMIC</td>
</tr>
<tr>
<td>Kuwait</td>
<td>KW</td>
<td></td>
<td><strong>ar</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Kyrgyzstan</td>
<td>KG</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Laos</td>
<td>LA</td>
<td></td>
<td>en_US, <strong>lo</strong>, th</td>
<td>BANK, SCHOOL, WORKDAY</td>
</tr>
<tr>
<td>Latvia</td>
<td>LV</td>
<td></td>
<td>en_US, <strong>lv</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Lesotho</td>
<td>LS</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Liechtenstein</td>
<td>LI</td>
<td></td>
<td><strong>de</strong>, en_US, uk</td>
<td>BANK</td>
</tr>
<tr>
<td>Lithuania</td>
<td>LT</td>
<td></td>
<td>en_US, <strong>lt</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Luxembourg</td>
<td>LU</td>
<td></td>
<td>de, en_US, fr, <strong>lb</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Macau</td>
<td>MO</td>
<td>Historical municipalities: I (Concelho das Ilhas, 海島市, 海岛市), M (Concelho de Macau, 澳門市, 澳门市)</td>
<td>en_MO, en_US, pt_MO, th, zh_CN, <strong>zh_MO</strong></td>
<td>GOVERNMENT, MANDATORY</td>
</tr>
<tr>
<td>Madagascar</td>
<td>MG</td>
<td></td>
<td>en_US, <strong>mg</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Malawi</td>
<td>MW</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Malaysia</td>
<td>MY</td>
<td>States and federal territories: 01 (Johor, JHR), 02 (Kedah, KDH), 03 (Kelantan, KTN), 04 (Melaka, MLK), 05 (Negeri Sembilan, NSN), 06 (Pahang, PHG), 07 (Pulau Pinang, PNG), 08 (Perak, PRK), 09 (Perlis, PLS), 10 (Selangor, SGR), 11 (Terengganu, TRG), 12 (Sabah, SBH), 13 (Sarawak, SWK), 14 (WP Kuala Lumpur, KUL), 15 (WP Labuan, LBN), 16 (WP Putrajaya, PJY)</td>
<td>en_US, <strong>ms_MY</strong>, th</td>
<td></td>
</tr>
<tr>
<td>Maldives</td>
<td>MV</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Malta</td>
<td>MT</td>
<td></td>
<td>en_US, <strong>mt</strong></td>
<td></td>
</tr>
<tr>
<td>Marshall Islands (the)</td>
<td>MH</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mauritania</td>
<td>MR</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Mexico</td>
<td>MX</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Moldova</td>
<td>MD</td>
<td></td>
<td>en_US, <strong>ro</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Monaco</td>
<td>MC</td>
<td></td>
<td>en_US, <strong>fr</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Montenegro</td>
<td>ME</td>
<td></td>
<td><strong>cnr</strong>, en_US, uk</td>
<td>CATHOLIC, HEBREW, ISLAMIC, ORTHODOX, WORKDAY</td>
</tr>
<tr>
<td>Morocco</td>
<td>MA</td>
<td></td>
<td><strong>ar</strong>, en_US, fr</td>
<td></td>
</tr>
<tr>
<td>Mozambique</td>
<td>MZ</td>
<td></td>
<td>en_US, <strong>pt_MZ</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Namibia</td>
<td>NA</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Netherlands</td>
<td>NL</td>
<td></td>
<td>en_US, fy, <strong>nl</strong>, uk</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>New Zealand</td>
<td>NZ</td>
<td>Regions and Special Island Authorities: AUK (Auckland, Tāmaki-Makaurau, AU), BOP (Bay of Plenty, Toi Moana, BP), CAN (Canterbury, Waitaha, CA), CIT (Chatham Islands Territory, Chatham Islands, Wharekauri, CI), GIS (Gisborne, Te Tairāwhiti, GI), HKB (Hawke's Bay, Te Matau-a-Māui, HB), MBH (Marlborough, MA), MWT (Manawatū Whanganui, Manawatū-Whanganui, MW), NSN (Nelson, Whakatū, NE), NTL (Northland, Te Taitokerau, NO), OTA (Otago, Ō Tākou, OT), STL (Southland, Te Taiao Tonga, SO), TAS (Tasman, Te tai o Aorere, TS), TKI (Taranaki, TK), WGN (Greater Wellington, Te Pane Matua Taiao, Wellington, Te Whanganui-a-Tara, WG), WKO (Waikato, WK), WTC (West Coast, Te Tai o Poutini, WC). Subregions: South Canterbury</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Nicaragua</td>
<td>NI</td>
<td>Subdivisions: AN (Costa Caribe Norte), AS (Costa Caribe Sur), BO (Boaco), CA (Carazo), CI (Chinandega), CO (Chontales), ES (Estelí), GR (Granada), JI (Jinotega), LE (León), MD (Madriz), MN (Managua), MS (Masaya), MT (Matagalpa), NS (Nueva Segovia), RI (Rivas), SJ (Río San Juan)</td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Nigeria</td>
<td>NG</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Northern Mariana Islands (the)</td>
<td>MP</td>
<td>Can also be loaded as country US, subdivision MP</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>North Macedonia</td>
<td>MK</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Norway</td>
<td>NO</td>
<td></td>
<td>en_US, <strong>no</strong>, th, uk</td>
<td></td>
</tr>
<tr>
<td>Pakistan</td>
<td>PK</td>
<td></td>
<td><strong>en_PK</strong>, en_US, ur_PK</td>
<td></td>
</tr>
<tr>
<td>Palau</td>
<td>PW</td>
<td></td>
<td></td>
<td>ARMED_FORCES, HALF_DAY</td>
</tr>
<tr>
<td>Panama</td>
<td>PA</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td>BANK</td>
</tr>
<tr>
<td>Papua New Guinea</td>
<td>PG</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Paraguay</td>
<td>PY</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td>GOVERNMENT</td>
</tr>
<tr>
<td>Peru</td>
<td>PE</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Philippines</td>
<td>PH</td>
<td></td>
<td><strong>en_PH</strong>, en_US, fil, th</td>
<td>WORKDAY</td>
</tr>
<tr>
<td>Poland</td>
<td>PL</td>
<td></td>
<td>de, en_US, <strong>pl</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Portugal</td>
<td>PT</td>
<td>Districts: 01 (Aveiro), 02 (Beja), 03 (Braga), 04 (Bragança), 05 (Castelo Branco), 06 (Coimbra), 07 (Évora), 08 (Faro), 09 (Guarda), 10 (Leiria), 11 (Lisboa), 12 (Portalegre), 13 (Porto), 14 (Santarém), 15 (Setúbal), 16 (Viana do Castelo), 17 (Vila Real), 18 (Viseu), 20 (Região Autónoma dos Açores), 30 (Região Autónoma da Madeira)</td>
<td>en_US, <strong>pt_PT</strong>, uk</td>
<td>OPTIONAL</td>
</tr>
<tr>
<td>Puerto Rico</td>
<td>PR</td>
<td>Can also be loaded as country US, subdivision PR</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>Qatar</td>
<td>QA</td>
<td></td>
<td><strong>ar_QA</strong>, en_US</td>
<td>BANK</td>
</tr>
<tr>
<td>Romania</td>
<td>RO</td>
<td></td>
<td>en_US, <strong>ro</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Russia</td>
<td>RU</td>
<td></td>
<td>en_US, <strong>ru</strong>, th</td>
<td></td>
</tr>
<tr>
<td>Saint Kitts and Nevis</td>
<td>KN</td>
<td></td>
<td></td>
<td>HALF_DAY, WORKDAY</td>
</tr>
<tr>
<td>Saint Lucia</td>
<td>LC</td>
<td></td>
<td><strong>en_LC</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Samoa</td>
<td>WS</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>San Marino</td>
<td>SM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Saudi Arabia</td>
<td>SA</td>
<td></td>
<td><strong>ar</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Serbia</td>
<td>RS</td>
<td></td>
<td>en_US, <strong>sr</strong></td>
<td></td>
</tr>
<tr>
<td>Seychelles</td>
<td>SC</td>
<td></td>
<td><strong>en_SC</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Singapore</td>
<td>SG</td>
<td></td>
<td><strong>en_SG</strong>, en_US, th</td>
<td></td>
</tr>
<tr>
<td>Slovakia</td>
<td>SK</td>
<td></td>
<td>en_US, <strong>sk</strong>, uk</td>
<td>WORKDAY</td>
</tr>
<tr>
<td>Slovenia</td>
<td>SI</td>
<td></td>
<td>en_US, <strong>sl</strong>, uk</td>
<td>WORKDAY</td>
</tr>
<tr>
<td>South Africa</td>
<td>ZA</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>South Korea</td>
<td>KR</td>
<td></td>
<td>en_US, <strong>ko</strong>, th</td>
<td>BANK</td>
</tr>
<tr>
<td>Spain</td>
<td>ES</td>
<td>Autonomous communities: AN, AR, AS, CB, CE, CL, CM, CN, CT, EX, GA, IB, MC, MD, ML, NC, PV, RI, VC</td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Sri Lanka</td>
<td>LK</td>
<td></td>
<td>en_US, <strong>si_LK</strong>, ta_LK</td>
<td>BANK, GOVERNMENT, WORKDAY</td>
</tr>
<tr>
<td>Sweden</td>
<td>SE</td>
<td></td>
<td>en_US, <strong>sv</strong>, th, uk</td>
<td></td>
</tr>
<tr>
<td>Switzerland</td>
<td>CH</td>
<td>Cantons: AG, AI, AR, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH</td>
<td><strong>de</strong>, en_US, fr, it, uk</td>
<td>HALF_DAY, OPTIONAL</td>
</tr>
<tr>
<td>Taiwan</td>
<td>TW</td>
<td></td>
<td>en_US, th, zh_CN, <strong>zh_TW</strong></td>
<td>GOVERNMENT, OPTIONAL, SCHOOL, WORKDAY</td>
</tr>
<tr>
<td>Tanzania</td>
<td>TZ</td>
<td></td>
<td>en_US, <strong>sw</strong></td>
<td>BANK</td>
</tr>
<tr>
<td>Thailand</td>
<td>TH</td>
<td></td>
<td>en_US, <strong>th</strong></td>
<td>ARMED_FORCES, BANK, GOVERNMENT, SCHOOL, WORKDAY</td>
</tr>
<tr>
<td>Timor Leste</td>
<td>TL</td>
<td></td>
<td>en_TL, en_US, <strong>pt_TL</strong>, tet, th</td>
<td>GOVERNMENT, WORKDAY</td>
</tr>
<tr>
<td>Tonga</td>
<td>TO</td>
<td></td>
<td>en_US, <strong>to</strong></td>
<td></td>
</tr>
<tr>
<td>Tunisia</td>
<td>TN</td>
<td></td>
<td><strong>ar</strong>, en_US</td>
<td></td>
</tr>
<tr>
<td>Turkey</td>
<td>TR</td>
<td></td>
<td>en_US, <strong>tr</strong>, uk</td>
<td>HALF_DAY</td>
</tr>
<tr>
<td>Tuvalu</td>
<td>TV</td>
<td>Town/Island Councils: FUN (Funafuti), NIT (Niutao), NKF (Nukufetau), NKL (Nukulaelae), NMA (Nanumea), NMG (Nanumaga, Nanumanga), NUI (Nui), VAI (Vaitupu)</td>
<td>en_GB, en_US, <strong>tvl</strong></td>
<td></td>
</tr>
<tr>
<td>Ukraine</td>
<td>UA</td>
<td></td>
<td>ar, en_US, th, <strong>uk</strong></td>
<td>WORKDAY</td>
</tr>
<tr>
<td>United Arab Emirates</td>
<td>AE</td>
<td></td>
<td><strong>ar</strong>, en_US, th</td>
<td>GOVERNMENT, OPTIONAL</td>
</tr>
<tr>
<td>United Kingdom</td>
<td>GB</td>
<td>Subdivisions: ENG (England), NIR (Northern Ireland), SCT (Scotland), WLS (Wales)</td>
<td><strong>en_GB</strong>, en_US, th</td>
<td></td>
</tr>
<tr>
<td>United States Minor Outlying Islands</td>
<td>UM</td>
<td>Can also be loaded as country US, subdivision UM</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>United States of America (the)</td>
<td>US</td>
<td>States and territories: AK, AL, AR, AS, AZ, CA, CO, CT, DC, DE, FL, GA, GU, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MP, MS, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, PR, RI, SC, SD, TN, TX, UM, UT, VA, VI, VT, WA, WI, WV, WY</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>United States Virgin Islands (the)</td>
<td></td>
<td>See Virgin Islands (U.S.)</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>Uruguay</td>
<td>UY</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td>BANK</td>
</tr>
<tr>
<td>Uzbekistan</td>
<td>UZ</td>
<td></td>
<td>en_US, uk, <strong>uz</strong></td>
<td></td>
</tr>
<tr>
<td>Vanuatu</td>
<td>VU</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Vatican City</td>
<td>VA</td>
<td></td>
<td>en_US, <strong>it</strong>, th</td>
<td></td>
</tr>
<tr>
<td>Venezuela</td>
<td>VE</td>
<td></td>
<td>en_US, <strong>es</strong>, uk</td>
<td></td>
</tr>
<tr>
<td>Vietnam</td>
<td>VN</td>
<td></td>
<td>en_US, th, <strong>vi</strong></td>
<td></td>
</tr>
<tr>
<td>Virgin Islands (U.S.)</td>
<td>VI</td>
<td>Can also be loaded as country US, subdivision VI</td>
<td></td>
<td>GOVERNMENT, UNOFFICIAL</td>
</tr>
<tr>
<td>Zambia</td>
<td>ZM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Zimbabwe</td>
<td>ZW</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Available Financial Markets

The standard way to refer to a financial market is to use its [ISO 10383
MIC](https://www.iso20022.org/market-identifier-codes) (Market Identifier Code) as a "market"
code when available. The following financial markets are available:

<table style="width: 100%">
<colgroup>
<col style="width: 20.0%" />
<col style="width: 4.0%" />
<col style="width: 65.0%" />
<col style="width: 15.0%" />
</colgroup>
<thead>
<tr>
<th>Entity</th>
<th>Code</th>
<th>Info</th>
<th>Supported Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td>Brasil, Bolsa, Balcão</td>
<td>BVMF</td>
<td>Brazil Stock Exchange and Over-the-Counter Market holidays (same as ANBIMA holidays)</td>
<td>en_US, <strong>pt_BR</strong>, uk</td>
</tr>
<tr>
<td>European Central Bank</td>
<td>XECB</td>
<td>Trans-European Automated Real-time Gross Settlement (TARGET2)</td>
<td></td>
</tr>
<tr>
<td>ICE Futures Europe</td>
<td>IFEU</td>
<td>A London-based Investment Exchange holidays</td>
<td></td>
</tr>
<tr>
<td>New York Stock Exchange</td>
<td>XNYS</td>
<td>NYSE market holidays (used by all other US-exchanges, including NASDAQ, etc.)</td>
<td></td>
</tr>
</tbody>
</table>

## Contributions

[Issues](https://github.com/vacanza/holidays/issues) and [pull
requests](https://github.com/vacanza/holidays/pulls) are always welcome. Please see
[here](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTING.md) for more information.

## License

Code and documentation are available according to the MIT License (see
[LICENSE](https://github.com/vacanza/holidays/blob/dev/LICENSE)).
