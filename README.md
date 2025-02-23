# holidays

A fast, efficient Python library for generating country- and
subdivision- (e.g. state or province) specific sets of
government-designated holidays on the fly. It aims to make determining
whether a specific date is a holiday as fast and flexible as possible.

<table>
  <tr>
    <td>PyPI</td>
    <td>
      <a href="https://pypi.org/project/holidays">
        <img src="https://img.shields.io/pypi/dm/holidays?color=41B5BE&style=flat" alt="PyPI downloads">
      </a>
      <a href="https://pypi.org/project/holidays">
        <img src="https://img.shields.io/pypi/v/holidays?color=41B5BE&label=version&style=flat" alt="PyPI version">
      </a>
      <a href="https://github.com/vacanza/holidays/releases">
        <img src="https://img.shields.io/github/release-date/vacanza/holidays?color=41B5BE&style=flat" alt="PyPI release date">
      </a>
    </td>
  </tr>
  <tr>
    <td>CI/CD</td>
    <td>
      <a href="https://github.com/vacanza/holidays/actions/workflows/ci-cd.yml?query=branch%3Adev">
        <img src="https://img.shields.io/github/actions/workflow/status/vacanza/holidays/ci-cd.yml?branch=dev&color=41BE4A&style=flat" alt="CI/CD status">
      </a>
      <a href="https://holidays.readthedocs.io/en/latest/?badge=latest">
        <img src="https://img.shields.io/readthedocs/holidays?color=41BE4A&style=flat" alt="Documentation status">
      </a>
    </td>
  </tr>
  <tr>
    <td>Code</td>
    <td>
      <a href="https://github.com/vacanza/holidays/blob/dev/LICENSE">
        <img src="https://img.shields.io/github/license/vacanza/holidays?color=41B5BE&style=flat" alt="License">
      </a>
      <a href="https://pypi.org/project/holidays">
        <img src="https://img.shields.io/pypi/pyversions/holidays?label=python&color=41B5BE&style=flat" alt="Python supported versions">
      </a>
      <a href="https://github.com/astral-sh/ruff">
        <img src="https://img.shields.io/badge/style-ruff-41B5BE?style=flat" alt="Code style">
      </a>
      <a href="https://app.codecov.io/gh/vacanza/holidays">
        <img src="https://img.shields.io/codecov/c/github/vacanza/holidays/dev?color=41B5BE&style=flat" alt="Code coverage">
      </a>
    </td>
  </tr>
  <tr>
    <td>GitHub</td>
    <td>
      <a href="https://github.com/vacanza/holidays/stargazers">
        <img src="https://img.shields.io/github/stars/vacanza/holidays?color=41BE4A&style=flat" alt="GitHub stars">
      </a>
      <a href="https://github.com/vacanza/holidays/forks">
        <img src="https://img.shields.io/github/forks/vacanza/holidays?color=41BE4A&style=flat" alt="GitHub forks">
      </a>
      <a href="https://github.com/vacanza/holidays/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/vacanza/holidays?color=41BE4A&style=flat" alt="GitHub contributors">
      </a>
      <a href="https://github.com/vacanza/holidays/commits/dev">
        <img src="https://img.shields.io/github/last-commit/vacanza/holidays/dev?color=41BE4A&style=flat" alt="GitHub last commit">
      </a>
    </td>
  </tr>
  <tr>
    <td>Citation</td>
    <td>
      <a href="https://doi.org/10.5281/zenodo.14847397">
        <img src="https://img.shields.io/badge/DOI-10.5281/zenodo.14847397-41B5BE?style=flat" alt="Open World Holidays Framework DOI">
      </a>
    </td>
  </tr>
</table>

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
<th><p>Country</p></th>
<th><p>Code</p></th>
<th><p>Subdivisions</p></th>
<th><p>Supported Languages</p></th>
<th><p>Supported Categories</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Afghanistan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AF</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>fa_AF</strong>, ps_AF</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Albania</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AL</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>sq</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Algeria</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US, fr</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>American Samoa</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AS</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Can also be loaded as country US, subdivision AS</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Andorra</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AD</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Parishes: 02, 03, 04, 05, 06, 07, 08</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Angola</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pt_AO</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Argentina</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Armenia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>hy</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Aruba</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, nl, <strong>pap_AW</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Australia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AU</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States and territories: ACT (Australian Capital Territory), NSW (New South Wales), NT (Northern Territory), QLD (Queensland), SA (South Australia), TAS (Tasmania), VIC (Victoria), WA (Western Australia)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_AU</strong>, en_US, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK, HALF_DAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Austria</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AT</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States: 1 (Burgenland, Bgld, B), 2 (Kärnten, Ktn, K), 3 (Niederösterreich, NÖ, N), 4 (Oberösterreich, OÖ, O), 5 (Salzburg, Sbg, S), 6 (Steiermark, Stmk, St), 7 (Tirol, T), 8 (Vorarlberg, Vbg, V), 9 (Wien, W)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>de</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Azerbaijan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>az</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WORKDAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Bahamas</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BS</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Bahrain</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BH</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Bangladesh</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BD</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Barbados</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BB</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Belarus</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BY</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>be</strong>, en_US, ru, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Belgium</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>de, en_US, fr, <strong>nl</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Belize</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Bolivia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BO</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Departments: B, C, H, L, N, O, P, S, T</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Bosnia and Herzegovina</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BA</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Entities and district: BIH (Federacija Bosne i Hercegovine, FBiH), BRC (Brčko distrikt, BD), SRP (Republika Srpska, RS)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>bs</strong>, en_US, sr, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Botswana</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Brazil</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BR</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States: AC (Acre), AL (Alagoas), AM (Amazonas), AP (Amapá), BA (Bahia), CE (Ceará), DF (Distrito Federal), ES (Espírito Santo), GO (Goiás), MA (Maranhão), MG (Minas Gerais), MS (Mato Grosso do Sul), MT (Mato Grosso), PA (Pará), PB (Paraíba), PE (Pernambuco), PI (Piauí), PR (Paraná), RJ (Rio de Janeiro), RN (Rio Grande do Norte), RO (Rondônia), RR (Roraima), RS (Rio Grande do Sul), SC (Santa Catarina), SE (Sergipe), SP (São Paulo), TO (Tocantins)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pt_BR</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Brunei</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BN</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ms</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Bulgaria</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>bg</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SCHOOL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Burkina Faso</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BF</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Burundi</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BI</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Cambodia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KH</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>km</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Cameroon</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Canada</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CA</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Provinces and territories: AB, BC, MB, NB, NL, NS, NT, NU, ON, PE, QC, SK, YT</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ar, <strong>en_CA</strong>, en_US, fr, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GOVERNMENT, OPTIONAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Chad</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TD</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Chile</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CL</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Regions: AI, AN, AP, AR, AT, BI, CO, LI, LL, LR, MA, ML, NB, RM, TA, VS</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>China</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CN</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, th, <strong>zh_CN</strong>, zh_TW</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Colombia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Congo</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>fr</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Costa Rica</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Croatia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>hr</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Cuba</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CU</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Curacao</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, nl, <strong>pap_CW</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Cyprus</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CY</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>el</strong>, en_CY, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK, OPTIONAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Czechia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>cs</strong>, en_US, sk, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Denmark</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DK</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>da</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Djibouti</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DJ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>ar, en_US, <strong>fr</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Dominica</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Dominican Republic</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Ecuador</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>EC</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Egypt</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>EG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>El Salvador</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SV</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Departments: AH (Ahuachapán), CA (Cabañas), CH (Chalatenango), CU (Cuscatlán), LI (La Libertad), MO (Morazán), PA (La Paz), SA (Santa Ana), SM (San Miguel), SO (Sonsonate), SS (San Salvador), SV (San Vicente), UN (La Unión), US (Usulután)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Estonia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>EE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>et</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Eswatini</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Ethiopia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ET</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>am</strong>, ar, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Finland</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>FI</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>fi</strong>, sv_FI, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>France</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>FR</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DOM/TOM: BL (Saint-Barthélemy), GES (Alsace, Champagne-Ardenne, Lorraine), GP (Guadeloupe), GY (Guyane), MF (Saint-Martin), MQ (Martinique), NC (Nouvelle-Calédonie), PF (Polynésie Française), RE (La Réunion), WF (Wallis-et-Futuna), YT (Mayotte)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>fr</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Gabon</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Georgia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ka</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GOVERNMENT</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Germany</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>DE</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States: BB (Brandenburg), BE (Berlin), BW (Baden-Württemberg), BY (Bayern), HB (Bremen), HE (Hessen), HH (Hamburg), MV (Mecklenburg-Vorpommern), NI (Niedersachsen), NW (Nordrhein-Westfalen), RP (Rheinland-Pfalz), SH (Schleswig-Holstein), SL (Saarland), SN (Sachsen), ST (Sachsen-Anhalt), TH (Thüringen)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>de</strong>, en_US, th, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CATHOLIC</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Ghana</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GH</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Greece</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>el</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Greenland</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GL</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>da, en_US, fi, is, <strong>kl</strong>, no, sv, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Guam</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GU</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Can also be loaded as country US, subdivision GU</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Guatemala</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GT</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Guernsey</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Haiti</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HT</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, es, <strong>fr_HT</strong>, ht</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Honduras</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HN</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Hong Kong</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HK</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_HK, en_US, th, zh_CN, <strong>zh_HK</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Hungary</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HU</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>hu</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Iceland</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IS</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>is</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>India</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IN</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States: AN, AP, AR, AS, BR, CG, CH, DH, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA, LD, MH, ML, MN, MP, MZ, NL, OD, PB, PY, RJ, SK, TN, TR, TS, UK, UP, WB</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Indonesia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ID</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>id</strong>, th, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GOVERNMENT</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Iran</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>fa_IR</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Ireland</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Isle of Man</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_GB</strong>, en_US, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Israel</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IL</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>he</strong>, th, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL, SCHOOL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Italy</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IT</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Provinces: AG (Agrigento), AL (Alessandria), AN (Ancona), AO (Aosta), AP (Ascoli Piceno), AQ (L’Aquila), AR (Arezzo), AT (Asti), AV (Avellino), BA (Bari), BG (Bergamo), BI (Biella), BL (Belluno), BN (Benevento), BO (Bologna), BR (Brindisi), BS (Brescia), BT (Barletta-Andria-Trani), BZ (Bolzano), CA (Cagliari), CB (Campobasso), CE (Caserta), CH (Chieti), CL (Caltanissetta), CN (Cuneo), CO (Como), CR (Cremona), CS (Cosenza), CT (Catania), CZ (Catanzaro), EN (Enna), FC (Forli-Cesena, Forlì-Cesena), FE (Ferrara), FG (Foggia), FI (Firenze), FM (Fermo), FR (Frosinone), GE (Genova), GO (Gorizia), GR (Grosseto), IM (Imperia), IS (Isernia), KR (Crotone), LC (Lecco), LE (Lecce), LI (Livorno), LO (Lodi), LT (Latina), LU (Lucca), MB (Monza e Brianza), MC (Macerata), ME (Messina), MI (Milano), MN (Mantova), MO (Modena), MS (Massa-Carrara), MT (Matera), NA (Napoli), NO (Novara), NU (Nuoro), OR (Oristano), PA (Palermo), PC (Piacenza), PD (Padova), PE (Pescara), PG (Perugia), PI (Pisa), PN (Pordenone), PO (Prato), PR (Parma), PT (Pistoia), PU (Pesaro e Urbino), PV (Pavia), PZ (Potenza), RA (Ravenna), RC (Reggio Calabria), RE (Reggio Emilia), RG (Ragusa), RI (Rieti), RM (Roma), RN (Rimini), RO (Rovigo), SA (Salerno), SI (Siena), SO (Sondrio), SP (La Spezia), SR (Siracusa), SS (Sassari), SU (Sud Sardegna), SV (Savona), TA (Taranto), TE (Teramo), TN (Trento), TO (Torino), TP (Trapani), TR (Terni), TS (Trieste), TV (Treviso), UD (Udine), VA (Varese), VB (Verbano-Cusio-Ossola), VC (Vercelli), VE (Venezia), VI (Vicenza), VR (Verona), VT (Viterbo), VV (Vibo Valentia). Cities: Andria, Barletta, Cesena, Forli (Forlì), Pesaro, Trani, Urbino</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Jamaica</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>JM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Japan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>JP</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ja</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Jersey</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>JE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Jordan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>JO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Kazakhstan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>kk</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Kenya</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Kuwait</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Kyrgyzstan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Laos</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>lo</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK, SCHOOL, WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Latvia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LV</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>lv</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Lesotho</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LS</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Liechtenstein</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LI</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>de</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Lithuania</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LT</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>lt</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Luxembourg</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LU</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>de, en_US, fr, <strong>lb</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Madagascar</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>mg</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Malawi</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Malaysia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MY</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States and federal territories: 01 (Johor, JHR), 02 (Kedah, KDH), 03 (Kelantan, KTN), 04 (Melaka, MLK), 05 (Negeri Sembilan, NSN), 06 (Pahang, PHG), 07 (Pulau Pinang, PNG), 08 (Perak, PRK), 09 (Perlis, PLS), 10 (Selangor, SGR), 11 (Terengganu, TRG), 12 (Sabah, SBH), 13 (Sarawak, SWK), 14 (WP Kuala Lumpur, KUL), 15 (WP Labuan, LBN), 16 (WP Putrajaya, PJY)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ms_MY</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Maldives</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MV</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Malta</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MT</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>mt</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Marshall Islands (the)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MH</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Mauritania</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Mexico</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MX</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Moldova</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MD</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ro</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Monaco</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MC</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>fr</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Montenegro</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ME</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>cnr</strong>, en_US, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CATHOLIC, HEBREW, ISLAMIC, ORTHODOX, WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Morocco</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US, fr</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Mozambique</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pt_MZ</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Namibia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Netherlands</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NL</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, fy, <strong>nl</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>New Zealand</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NZ</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Regions and Special Island Authorities: AUK (Auckland, Tāmaki-Makaurau, AU), BOP (Bay of Plenty, Toi Moana, BP), CAN (Canterbury, Waitaha, CA), CIT (Chatham Islands Territory, Chatham Islands, Wharekauri, CI), GIS (Gisborne, Te Tairāwhiti, GI), HKB (Hawke’s Bay, Te Matau-a-Māui, HB), MBH (Marlborough, MA), MWT (Manawatū Whanganui, Manawatū-Whanganui, MW), NSN (Nelson, Whakatū, NE), NTL (Northland, Te Taitokerau, NO), OTA (Otago, Ō Tākou, OT), STL (Southland, Te Taiao Tonga, SO), TAS (Tasman, Te tai o Aorere, TS), TKI (Taranaki, TK), WGN (Greater Wellington, Te Pane Matua Taiao, Wellington, Te Whanganui-a-Tara, WG), WKO (Waikato, WK), WTC (West Coast, Te Tai o Poutini, WC). Subregions: South Canterbury</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Nicaragua</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NI</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Subdivisions: AN (Costa Caribe Norte), AS (Costa Caribe Sur), BO (Boaco), CA (Carazo), CI (Chinandega), CO (Chontales), ES (Estelí), GR (Granada), JI (Jinotega), LE (León), MD (Madriz), MN (Managua), MS (Masaya), MT (Matagalpa), NS (Nueva Segovia), RI (Rivas), SJ (Río San Juan)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Nigeria</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Northern Mariana Islands (the)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MP</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Can also be loaded as country US, subdivision MP</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>North Macedonia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>MK</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Norway</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>no</strong>, th, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Pakistan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PK</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Palau</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>ARMED_FORCES, HALF_DAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Panama</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Papua New Guinea</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Paraguay</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PY</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GOVERNMENT</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Peru</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Philippines</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PH</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_PH</strong>, en_US, fil, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WORKDAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Poland</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PL</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pl</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Portugal</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PT</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Districts: 01 (Aveiro), 02 (Beja), 03 (Braga), 04 (Bragança), 05 (Castelo Branco), 06 (Coimbra), 07 (Évora), 08 (Faro), 09 (Guarda), 10 (Leiria), 11 (Lisboa), 12 (Portalegre), 13 (Porto), 14 (Santarém), 15 (Setúbal), 16 (Viana do Castelo), 17 (Vila Real), 18 (Viseu), 20 (Região Autónoma dos Açores), 30 (Região Autónoma da Madeira)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pt_PT</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>OPTIONAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Puerto Rico</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>PR</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Can also be loaded as country US, subdivision PR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Romania</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>RO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ro</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Russia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>RU</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ru</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Saint Kitts and Nevis</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KN</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY, WORKDAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Saint Lucia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LC</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_LC</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Samoa</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WS</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>San Marino</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Saudi Arabia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Serbia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>RS</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>sr</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Seychelles</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SC</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_SC</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Singapore</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SG</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_SG</strong>, en_US, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Slovakia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SK</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>sk</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WORKDAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Slovenia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SI</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>sl</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>South Africa</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ZA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>South Korea</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>KR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>ko</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Spain</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ES</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Autonomous communities: AN, AR, AS, CB, CE, CL, CM, CN, CT, EX, GA, IB, MC, MD, ML, NC, PV, RI, VC</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Sri Lanka</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>LK</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>si_LK</strong>, ta_LK</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK, GOVERNMENT, WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Sweden</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>SE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>sv</strong>, th, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Switzerland</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>CH</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Cantons: AG, AI, AR, BL, BS, BE, FR, GE, GL, GR, JU, LU, NE, NW, OW, SG, SH, SZ, SO, TG, TI, UR, VD, VS, ZG, ZH</p></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>de</strong>, en_US, fr, it, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY, OPTIONAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Taiwan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, th, zh_CN, <strong>zh_TW</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Tanzania</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>sw</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Thailand</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TH</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>th</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ARMED_FORCES, BANK, GOVERNMENT, SCHOOL, WORKDAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Timor Leste</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TL</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pt_TL</strong>, tet</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GOVERNMENT, WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Tonga</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TO</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>to</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Tunisia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TN</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Turkey</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>TR</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>tr</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>HALF_DAY</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Ukraine</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>UA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>ar, en_US, th, <strong>uk</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ><p>WORKDAY</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>United Arab Emirates</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>AE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>ar</strong>, en_US, th</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GOVERNMENT, OPTIONAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>United Kingdom</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>GB</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Subdivisions: ENG (England), NIR (Northern Ireland), SCT (Scotland), WLS (Wales)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p><strong>en_GB</strong>, en_US, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>United States Minor Outlying Islands</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>UM</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Can also be loaded as country US, subdivision UM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>United States of America (the)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>US</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>States and territories: AK, AL, AR, AS, AZ, CA, CO, CT, DC, DE, FL, GA, GU, HI, IA, ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MP, MS, MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA, PR, RI, SC, SD, TN, TX, UM, UT, VA, VI, VT, WA, WI, WV, WY</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>United States Virgin Islands (the)</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>See Virgin Islands (U.S.)</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Uruguay</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>UY</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BANK</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Uzbekistan</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>UZ</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, uk, <strong>uz</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Vanuatu</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>VU</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Vatican City</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>VA</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>it</strong>, th</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Venezuela</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>VE</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>es</strong>, uk</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Vietnam</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>VN</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, th, <strong>vi</strong></p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Virgin Islands (U.S.)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>VI</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Can also be loaded as country US, subdivision VI</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ><p>UNOFFICIAL</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>Zambia</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ZM</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Zimbabwe</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>ZW</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
</tbody>
</table>

### Available Financial Markets

The standard way to refer to a financial market is to use its [ISO 10383
MIC](https://www.iso20022.org/market-identifier-codes) (Market
Identifier Code) as a "country" code when available. The following
financial markets are available:

<table>
<colgroup>
<col style="width: 17.7%" />
<col style="width: 3.1%" />
<col style="width: 63.8%" />
<col style="width: 15.4%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Entity</p></th>
<th class="head"><p>Code</p></th>
<th class="head"><p>Info</p></th>
<th class="head"><p>Supported Languages</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>Brasil, Bolsa, Balcão</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>BVMF</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Brazil Stock Exchange and Over-the-Counter Market holidays (same as ANBIMA holidays)</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>en_US, <strong>pt_BR</strong>, uk</p></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>European Central Bank</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>XECB</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>Trans-European Automated Real-time Gross Settlement (TARGET2)</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-even"><td style="white-space: normal; word-break: break-word;" ><p>ICE Futures Europe</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>IFEU</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>A London-based Investment Exchange holidays</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
<tr class="row-odd"><td style="white-space: normal; word-break: break-word;" ><p>New York Stock Exchange</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>XNYS</p></td>
<td style="white-space: normal; word-break: break-word;" ><p>NYSE market holidays (used by all other US-exchanges, including NASDAQ, etc.)</p></td>
<td style="white-space: normal; word-break: break-word;" ></td>
</tr>
</tbody>
</table>


## Contributions

[Issues](https://github.com/vacanza/holidays/issues) and [pull
requests](https://github.com/vacanza/holidays/pulls) are always welcome.
Please see
[here](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTING.rst)
for more information.

## License

Code and documentation are available according to the MIT License (see
[LICENSE](https://github.com/vacanza/holidays/blob/dev/LICENSE)).
