#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

__all__ = (
    "CountryHoliday",
    "country_holidays",
    "financial_holidays",
    "Holidays",
    "list_supported_countries",
    "list_supported_financial",
)

import importlib
import warnings
from functools import partial
from typing import Dict, Iterable, List, Optional, Union

from holidays.holiday_base import HolidayBase

country_to_module = {
    # List of all countries we support and the submodule name
    # The code itself must be the name of the class in that submodule
    # All country codes are ISO 3166-1 alpha-2 codes
    "AL": "albania",
    "AS": "american_samoa",
    "AD": "andorra",
    "AO": "angola",
    "AR": "argentina",
    "AM": "armenia",
    "AW": "aruba",
    "AU": "australia",
    "AT": "austria",
    "AZ": "azerbaijan",
    "BH": "bahrain",
    "BD": "bangladesh",
    "BY": "belarus",
    "BE": "belgium",
    "BO": "bolivia",
    "BA": "bosnia_and_herzegovina",
    "BW": "botswana",
    "BR": "brazil",
    "BG": "bulgaria",
    "BI": "burundi",
    "CA": "canada",
    "CL": "chile",
    "CN": "china",
    "CO": "colombia",
    "HR": "croatia",
    "CU": "cuba",
    "CW": "curacao",
    "CY": "cyprus",
    "CZ": "czechia",
    "DK": "denmark",
    "DJ": "djibouti",
    "DO": "dominican_republic",
    "EG": "egypt",
    "EE": "estonia",
    "SZ": "eswatini",
    "ET": "ethiopia",
    "FI": "finland",
    "FR": "france",
    "GE": "georgia",
    "DE": "germany",
    "GR": "greece",
    "GU": "guam",
    "VA": "vatican_city",
    "HN": "honduras",
    "HK": "hongkong",
    "HU": "hungary",
    "IS": "iceland",
    "IN": "india",
    "ID": "indonesia",
    "IE": "ireland",
    "IM": "isle_of_man",
    "IL": "israel",
    "IT": "italy",
    "JM": "jamaica",
    "JP": "japan",
    "KZ": "kazakhstan",
    "KE": "kenya",
    "KR": "south_korea",
    "KG": "kyrgyzstan",
    "LV": "latvia",
    "LS": "lesotho",
    "LI": "liechtenstein",
    "LT": "lithuania",
    "LU": "luxembourg",
    "MG": "madagascar",
    "MW": "malawi",
    "MY": "malaysia",
    "MT": "malta",
    "MH": "marshall_islands",
    "MX": "mexico",
    "MD": "moldova",
    "MC": "monaco",
    "ME": "montenegro",
    "MA": "morocco",
    "MZ": "mozambique",
    "NA": "namibia",
    "NL": "netherlands",
    "NZ": "new_zealand",
    "NI": "nicaragua",
    "NG": "nigeria",
    "MK": "north_macedonia",
    "MP": "northern_mariana_islands",
    "NO": "norway",
    "PK": "pakistan",
    "PA": "panama",
    "PY": "paraguay",
    "PE": "peru",
    "PH": "philippines",
    "PL": "poland",
    "PT": "portugal",
    "PR": "puerto_rico",
    "RO": "romania",
    "RU": "russia",
    "SM": "san_marino",
    "SA": "saudi_arabia",
    "RS": "serbia",
    "SG": "singapore",
    "SK": "slovakia",
    "SI": "slovenia",
    "ZA": "south_africa",
    "ES": "spain",
    "SE": "sweden",
    "CH": "switzerland",
    "TW": "taiwan",
    "TH": "thailand",
    "TN": "tunisia",
    "TR": "turkey",
    "UA": "ukraine",
    "AE": "united_arab_emirates",
    "GB": "united_kingdom",
    "US": "united_states",
    "UM": "united_states_minor_outlying_islands",
    "UY": "uruguay",
    "UZ": "uzbekistan",
    "VE": "venezuela",
    "VN": "vietnam",
    "VI": "united_states_virgin_islands",
    "ZM": "zambia",
    "ZW": "zimbabwe",
}
market_to_module = {
    # List of all financial market codes we support and the submodule name
    # The code itself must be the name of the class in that submodule
    # ISO 10383 market identifier codes (MIC):
    "XNYS": "ny_stock_exchange",
    # Pseudocodes (no ISO 10383 exists):
    "ECB": "european_central_bank",
    # Aliases:
    "NYSE": "ny_stock_exchange",
    "TAR": "european_central_bank",
}


class Holidays(HolidayBase):
    """
    This class instantiates public holidays for a single country or financial
    market. It maintains backwards compatibility with the original
    load-all-objects architecture while dramatically improving loading times by
    implementing lazy loading of the country or market, which is performed by
    the function :py:func:`country_holidays` or :py:func:`financial_holidays`.

    It does this by "inheriting" (i.e. adding) all the attributes and methods
    of the country- or market-specific subclass found in its file.

    TODO: Once the original load-all-objects architecture is fully deprecated,
    this class can be simplified/rearchitected.  For example, we can get rid of
    the bloat in submodules and have a single class per country/market.

    As a side benefit, all public holiday objects loaded correctly are of this
    :py:class:`Holidays` class (as opposed to a country- or market-specific
    subclass), and therefore easy to spot in development and fully documented.

    This class should not be instantiated directly (or lazy-loading won't take
    place), rather the public holiday :py:class:`Holidays` object should be
    instantiated by calling one of the two specialized functions, who also
    perform argument validation and provide documentation, as follows:

    >>> from holidays import country_holidays
    >>> us_holidays = country_holidays('US')

    >>> from holidays import financial_holidays
    >>> nyse_holidays = financial_holidays('XNYS')
    """

    def __init__(
        self,
        country: str = "",
        subdiv: Optional[str] = None,
        market: str = "",
        years: Optional[Union[int, Iterable[int]]] = None,
        observed: bool = True,
        language: Optional[str] = None,
    ) -> None:
        """
        :param country:
            An ISO 3166-1 alpha-2 country code. Takes precedence over
            ``market``.

        :param subdiv:
            The subdivision (e.g. state or province); only implemented for some
            countries (see documentation).

        :param market:
            An ISO 10383 market identifier code (MIC).  See
            https://www.iso20022.org/market-identifier-codes.

        :param years:
            The year(s) for which to pre-calculate public holidays at
            instantiation.

        :param observed:
            Whether to include the dates of when public holiday are observed
            (e.g. a holiday falling on a Sunday being observed the following
            Monday). False may not work for all markets.

        :param language:
            The language which the returned holiday names will be translated
            into. It must be an ISO 639-1 (2-letter) language code. If the
            language translation is not supported the original holiday names
            will be used.
        """
        if country in country_to_module:
            module_name = country_to_module[country.upper()]
            self._country_module = importlib.import_module(
                f"holidays.countries.{module_name}"
            )
        elif market in market_to_module:
            module_name = market_to_module[market.upper()]
            self._country_module = importlib.import_module(
                f"holidays.financial.{module_name}"
            )
        else:
            raise ValueError("Incorrect country or market argument.")

        # load the country subclass from its module
        self._subclass = getattr(
            self._country_module, (country or market).upper()
        )
        # if we loaded a sub-subclass of HolidayBase, go up one level
        if self._subclass.__base__ is not HolidayBase:
            self._subclass = self._subclass.__base__
        # add all the subclass' attributes to this one
        attrib_names = (
            attrib_name
            for attrib_name in self._subclass.__dict__.keys()
            if not attrib_name.startswith("__")
        )
        for attrib_name in attrib_names:
            attrib = getattr(self._subclass, attrib_name)
            if not callable(attrib):
                setattr(self, attrib_name, attrib)
            else:
                setattr(self, attrib_name, partial(attrib, self))

        if hasattr(self._subclass, "__init__"):
            self._subclass.__init__(
                self,
                years=years,
                observed=observed,
                subdiv=subdiv,
                language=language,
            )
        else:
            super().__init__(
                years=years,
                observed=observed,
                subdiv=subdiv,
                language=language,
            )


def country_holidays(
    country: str,
    subdiv: Optional[str] = None,
    years: Optional[Union[int, Iterable[int]]] = None,
    observed: bool = True,
    language: Optional[str] = None,
    prov: Optional[str] = None,
    state: Optional[str] = None,
    expand: Optional[bool] = None,
) -> Holidays:
    """
    Returns a :py:class:`Holidays` object with the public
    holidays of the country matching **country** and other keyword arguments.

    :param country:
        An ISO 3166-1 alpha-2 country code.

    :param subdiv:
        The subdivision (e.g. state or province); only implemented for some
        countries (see documentation).

    :param years:
        The year(s) for which to pre-calculate public holidays at
        instantiation.

    :param observed:
        Whether to include the dates of when public holiday are observed
        (e.g. a holiday falling on a Sunday being observed the following
        Monday). False may not work for all countries.

    :param language:
        The language which the returned holiday names will be translated
        into. It must be an ISO 639-1 (2-letter) language code. If the
        language translation is not supported, the holidays name in an official
        country language will be used.

    :param prov:
        *Deprecated*; use ``subdiv`` instead. Usage will raise a warning.

    :param state:
        *Deprecated*; use ``subdiv`` instead. Usage will raise a warning.

    :param expand:
        *Deprecated*. Usage will raise a warning.

    :return:
        A :py:class:`Holidays` object matching the **country**.

    The key of the :class:`dict`-like :class:`Holidays` object is the
    `date` of the public holiday, and the value is the name of the holiday.

    Dates where a key is not present are not public holidays or observed days
    (or, if **observed** is False, only the actual day of the holiday). If
    multiple public holidays fall on the same date, their names are
    concatenated with a semicolon (`;`) as a separator. Observed days will be
    so noted in the name.

    The key is always returned as a :class:`datetime.date` object but can be
    queried as one of:

    * :class:`datetime.date`,
    * :class:`datetime.datetime`,
    * :class:`str` of any format recognized by :func:`dateutil.parser.parse`,
    * :class:`float` or :class:`int` representing a POSIX timestamp.

    To maximize speed, the list of public holidays is built on the fly as
    needed, one calendar year at a time. When the object is instantiated
    without a **years** parameter, it is empty, but as soon as a key is
    accessed the public holidays for that entire year will be populated.

    If you need to list all the public holidays as opposed to querying
    individual dates, make sure to instantiate the class with the **years**
    parameter.

    Example usage:

    >>> from holidays.utils import country_holidays
    >>> us_holidays = country_holidays('US')

    The below will cause 2015 public holidays to be calculated on the fly:

    >>> from datetime import date
    >>> assert date(2015, 1, 1) in us_holidays

    If we now query another date in 2015, it will be faster because all of the
    year's public holidays are already calculated:

    >>> assert date(2015, 1, 2) not in us_holidays

    The :class:`Holidays` class also recognizes strings of many formats
    and numbers representing a POSIX timestamp:

    >>> assert '2014-01-01' in us_holidays
    >>> assert '1/1/2014' in us_holidays
    >>> assert 1388597445 in us_holidays

    Show the public holiday's name:

    >>> us_holidays.get('2014-01-01')
    "New Year's Day"

    Check a range:

    >>> us_holidays['2014-01-01': '2014-01-03']
    [datetime.date(2014, 1, 1)]

    List all 2020 public holidays:

    >>> us_holidays = country_holidays('US', years=2020)
    >>> for day in us_holidays.items():
    ...     print(day)
    (datetime.date(2020, 1, 1), "New Year's Day")
    (datetime.date(2020, 1, 20), 'Martin Luther King Jr. Day')
    (datetime.date(2020, 2, 17), "Washington's Birthday")
    (datetime.date(2020, 5, 25), 'Memorial Day')
    (datetime.date(2020, 7, 4), 'Independence Day')
    (datetime.date(2020, 7, 3), 'Independence Day (Observed)')
    (datetime.date(2020, 9, 7), 'Labor Day')
    (datetime.date(2020, 10, 12), 'Columbus Day')
    (datetime.date(2020, 11, 11), 'Veterans Day')
    (datetime.date(2020, 11, 26), 'Thanksgiving')
    (datetime.date(2020, 12, 25), 'Christmas Day')

    Some public holidays are only present in parts of a country:

    >>> us_pr_holidays = country_holidays('US', subdiv='PR')
    >>> assert '2018-01-06' not in us_holidays
    >>> assert '2018-01-06' in us_pr_holidays

    Append custom holiday dates by passing one of:

    * a :class:`dict` with date/name key/value pairs (e.g.
      ``{'2010-07-10': 'My birthday!'}``);
    * a single date (``'Holiday'`` will be used as a description);
    * a list of dates (``'Holiday'`` will be used as a description).

    The date can be one of the following:

    * :class:`datetime.date`,
    * :class:`datetime.datetime`,
    * :class:`str` of any format recognized by :func:`dateutil.parser.parse`,
    * :class:`float` or :class:`int` representing a POSIX timestamp.

    Examples:

    >>> custom_holidays = country_holidays('US', years=2015)
    >>> custom_holidays.update({'2015-01-01': "New Year's Day"})
    >>> custom_holidays.update(['2015-07-01', '07/04/2015'])
    >>> custom_holidays.update(date(2015, 12, 25))
    >>> assert date(2015, 1, 1) in custom_holidays
    >>> assert date(2015, 1, 2) not in custom_holidays
    >>> assert '12/25/2015' in custom_holidays

    For more complex logic, like 4th Monday of January, you can inherit the
    :class:`HolidayBase` class and define your own :meth:`_populate` method.
    See documentation for examples.
    """

    if prov is not None:
        warnings.warn(
            "The use of prov= is deprecated; please use subdiv=.",
            DeprecationWarning,
        )
        subdiv = prov
    if state is not None:
        warnings.warn(
            "The use of state= is deprecated; please use subdiv=.",
            DeprecationWarning,
        )
        subdiv = prov
    if expand is not None:
        warnings.warn(
            "The use of expand= is deprecated; please remove the argument.",
            DeprecationWarning,
        )

    iso_3166_1 = {
        # source https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes
        # As of 2023-03-21
        "AF",
        "AX",
        "AL",
        "DZ",
        "AS",
        "AD",
        "AO",
        "AI",
        "AQ",
        "AG",
        "AR",
        "AM",
        "AW",
        "AU",
        "AT",
        "AZ",
        "BS",
        "BH",
        "BD",
        "BB",
        "BY",
        "BE",
        "BZ",
        "BJ",
        "BM",
        "BT",
        "BO",
        "BQ",
        "BA",
        "BW",
        "BV",
        "BR",
        "IO",
        "BN",
        "BG",
        "BF",
        "BI",
        "CV",
        "KH",
        "CM",
        "CA",
        "KY",
        "CF",
        "TD",
        "CL",
        "CN",
        "CX",
        "CC",
        "CO",
        "KM",
        "CG",
        "CD",
        "CK",
        "CR",
        "CI",
        "HR",
        "CU",
        "CW",
        "CY",
        "CZ",
        "DK",
        "DJ",
        "DM",
        "DO",
        "EC",
        "EG",
        "SV",
        "GQ",
        "ER",
        "EE",
        "SZ",
        "ET",
        "FK",
        "FO",
        "FJ",
        "FI",
        "FR",
        "GF",
        "PF",
        "TF",
        "GA",
        "GM",
        "GE",
        "DE",
        "GH",
        "GI",
        "GR",
        "GL",
        "GD",
        "GP",
        "GU",
        "GT",
        "GG",
        "GN",
        "GW",
        "GY",
        "HT",
        "HM",
        "VA",
        "HN",
        "HK",
        "HU",
        "IS",
        "IN",
        "ID",
        "IR",
        "IQ",
        "IE",
        "IM",
        "IL",
        "IT",
        "JM",
        "JP",
        "JE",
        "JO",
        "KZ",
        "KE",
        "KI",
        "KP",
        "KR",
        "KW",
        "KG",
        "LA",
        "LV",
        "LB",
        "LS",
        "LR",
        "LY",
        "LI",
        "LT",
        "LU",
        "MO",
        "MG",
        "MW",
        "MY",
        "MV",
        "ML",
        "MT",
        "MH",
        "MQ",
        "MR",
        "MU",
        "YT",
        "MX",
        "FM",
        "MD",
        "MC",
        "MN",
        "ME",
        "MS",
        "MA",
        "MZ",
        "MM",
        "NA",
        "NR",
        "NP",
        "NL",
        "NC",
        "NZ",
        "NI",
        "NE",
        "NG",
        "NU",
        "NF",
        "MK",
        "MP",
        "NO",
        "OM",
        "PK",
        "PW",
        "PS",
        "PA",
        "PG",
        "PY",
        "PE",
        "PH",
        "PN",
        "PL",
        "PT",
        "PR",
        "QA",
        "RE",
        "RO",
        "RU",
        "RW",
        "BL",
        "SH",
        "KN",
        "LC",
        "MF",
        "PM",
        "VC",
        "WS",
        "SM",
        "ST",
        "SA",
        "SN",
        "RS",
        "SC",
        "SL",
        "SG",
        "SX",
        "SK",
        "SI",
        "SB",
        "SO",
        "ZA",
        "GS",
        "SS",
        "ES",
        "LK",
        "SD",
        "SR",
        "SJ",
        "SE",
        "CH",
        "SY",
        "TW",
        "TJ",
        "TZ",
        "TH",
        "TL",
        "TG",
        "TK",
        "TO",
        "TT",
        "TN",
        "TR",
        "TM",
        "TC",
        "TV",
        "UG",
        "UA",
        "AE",
        "GB",
        "US",
        "UM",
        "UY",
        "UZ",
        "VU",
        "VE",
        "VN",
        "VG",
        "VI",
        "WF",
        "EH",
        "YE",
        "ZM",
        "ZW",
    }
    # There is no ISO 3166-1 alpha-2 country code for the Republic of Kosovo,
    # however 'XK' is a self-assigned code that is used by many international
    # organisations per https://en.wikipedia.org/wiki/ISO_3166-2:RS#Note
    iso_3166_1.add("XK")

    country = country.upper()
    if country not in iso_3166_1:
        raise ValueError(
            f"'{country}' is not an ISO 3166-1 alpha-2 code; see "
            f"https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes."
        )
    if country not in country_to_module:
        raise NotImplementedError(
            f"We do not have holiday information for the country, dependent "
            f"territory, or special area of geographical "
            f"interest '{country}'.\n"
            "Please consider contributing these holidays to the project\n"
            "(see "
            "https://python-holidays.readthedocs.io/en/latest/contributing"
            ".html).\n"
            "Thank you.\n"
            "For a list of supported ISO 3166-1 alpha-2 codes supported, run\n"
            ">>> from holidays import list_supported_countries; "
            "list_supported_countries()"
        )

    return Holidays(
        country=country,
        subdiv=subdiv,
        years=years,
        observed=observed,
        language=language,
    )


def financial_holidays(
    market: str,
    subdiv: Optional[str] = None,
    years: Optional[Union[int, Iterable[int]]] = None,
    observed: bool = True,
    language: Optional[str] = None,
    expand: Optional[bool] = None,
) -> Holidays:
    """
    Returns a new dictionary-like :py:class:`Holidays` object for the public
    holidays of the financial market matching **market** and other keyword
    arguments.

    :param market:
        An ISO 10383 market identifier code (MIC).  See
        https://www.iso20022.org/market-identifier-codes.

    :param subdiv:
        Reserved for submarkets, but currenly not implemented (see
        documentation).

    :param years:
        The year(s) for which to pre-calculate public holidays at
        instantiation.

    :param observed:
        Whether to include the dates of when public holiday are observed
        (e.g. a holiday falling on a Sunday being observed the following
        Monday). False may not work for all markets.

    :param language:
        The language which the returned holiday names will be translated
        into. It must be an ISO 639-1 (2-letter) language code. If the
        language translation is not supported the original holiday names
        will be used.

    :param expand:
        *Deprecated*. Usage will raise a warning.

    :return:
        A :py:class:`HolidayBase` object matching the **market**.

    Example usage:

    >>> from holidays.utils import financial_holidays
    >>> nyse_holidays = financial_holidays('NYSE')

    See the documentation for :py:func:`country_holidays()` for further details
    and examples.
    """
    if expand is not None:
        warnings.warn(
            "The use of expand= is deprecated; please remove the argument.",
            DeprecationWarning,
        )

    market = market.upper()
    if market not in market_to_module:
        raise NotImplementedError(
            f"We do not have holiday information for the financial market "
            f"'{market}'.\n"
            "Please consider contributing these holidays to the project\n"
            "(see "
            "https://python-holidays.readthedocs.io/en/latest/contributing"
            ".html).\n"
            "Thank you."
            "For a list of financial markets supported, run\n"
            ">>> from holidays import list_supported_financial; "
            "list_supported_financial()"
        )

    return Holidays(
        market=market,
        subdiv=subdiv,
        years=years,
        observed=observed,
        language=language,
    )


def CountryHoliday(
    country: str,
    subdiv: Optional[str] = None,
    years: Optional[Union[int, Iterable[int]]] = None,
    expand: Optional[bool] = None,
    observed: bool = True,
    prov: Optional[str] = None,
    state: Optional[str] = None,
) -> HolidayBase:
    """
    Deprecated name for :py:func:`country_holidays`.

    :meta private:
    """

    warnings.warn(
        "CountryHoliday is deprecated, use country_holidays instead.",
        DeprecationWarning,
    )
    return country_holidays(
        country=country,
        subdiv=subdiv,
        years=years,
        observed=observed,
        prov=prov,
        state=state,
        expand=expand,
    )


def list_supported_countries() -> Dict[str, List[str]]:
    """
    Get all supported country codes and their subdivisions.

    :return:
        A dictionary where the key is the ISO 3166-1 alpha-2 code for a
        country, dependent territory, or special area of geographical interest,
        and the value is a list of ISO 3166-2 codes of supported subdivisions.
    """
    return {
        name: getattr(
            importlib.import_module(f"holidays.countries.{module_name}"), name
        ).subdivisions
        for name, module_name in country_to_module.items()
    }


def list_supported_financial() -> Dict[str, List[str]]:
    """
    Get all supported financial markets codes and their submarkets (if any).

    :return:
        A dictionary where the key is the market code (generally the ISO 10383
        Market Identifier Code) and the value is a list of supported submarkets
        (if any).
    """
    return {
        name: getattr(
            importlib.import_module(f"holidays.financial.{module_name}"), name
        ).subdivisions
        for name, module_name in market_to_module.items()
    }
