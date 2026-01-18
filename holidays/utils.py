# holidays
# --------
# A concise, efficient library for generating country, province, and state
# holiday sets on demand. Designed for fast, flexible holiday lookup.
#
# **Authors:** Vacanza Team and contributors (see CONTRIBUTORS)
# **Maintainers:** dr-prodigy <dr.prodigy.github@gmail.com> (2017-2023),
#                ryanss <ryanssdev@icloud.com> (2014-2017)
# **Website:** https://github.com/vacanza/holidays
# **License:** MIT (see LICENSE file)

__all__ = (
    "country_holidays",
    "CountryHoliday",
    "financial_holidays",
    "list_localized_countries",
    "list_localized_financial",
    "list_long_breaks",
    "list_supported_countries",
    "list_supported_financial",
)

import warnings
from collections.abc import Iterable
from datetime import date
from functools import cache

from holidays.calendars.gregorian import _timedelta
from holidays.holiday_base import CategoryArg, HolidayBase
from holidays.registry import EntityLoader


def country_holidays(
    country: str,
    subdiv: str | None = None,
    years: int | Iterable[int] | None = None,
    expand: bool = True,
    observed: bool = True,
    prov: str | None = None,
    state: str | None = None,
    language: str | None = None,
    categories: CategoryArg | None = None,
) -> HolidayBase:
    """Create and return a `HolidayBase` instance for a country.

    This convenience function instantiates the holiday entity class named
    by `country` (ISO 3166-1 alpha-2 code) from the `holidays` package and
    returns it. The returned object behaves like a `dict` with `date` keys
    and holiday-name values.

    Key options (high level):
    - **subdiv**: subdivision code (ISO 3166-2 or alias).
    - **years**: pre-calculate holidays for given year(s).
    - **expand**: if True, calculate an entire year on first access.
    - **observed**: include observed dates (e.g., Monday for Sunday holidays).
    - **language**: preferred language for holiday names (see supported languages).

    Notes:
    - The function raises `NotImplementedError` if the named country entity
      is not available.
    - Accepted key types for membership checks include `date`, `datetime`,
      strings parseable by `dateutil`, and POSIX timestamps (int/float).

    Example:
        >>> from holidays import country_holidays
        >>> us = country_holidays('US', years=2020)

    See module-level documentation for more usage examples and details.
    """
    import holidays

    try:
        return getattr(holidays, country)(
            years=years,
            subdiv=subdiv,
            expand=expand,
            observed=observed,
            prov=prov,
            state=state,
            language=language,
            categories=categories,
        )
    except AttributeError:
        raise NotImplementedError(f"Country {country} not available")


def financial_holidays(
    market: str,
    subdiv: str | None = None,
    years: int | Iterable[int] | None = None,
    expand: bool = True,
    observed: bool = True,
    language: str | None = None,
    categories: CategoryArg | None = None,
) -> HolidayBase:
    """Create and return a `HolidayBase` instance for a financial market.

    This function mirrors `country_holidays` but targets financial market
    entities (identified by ISO 10383 MIC codes). It returns a `HolidayBase`
    object which can be used for membership checks and iteration.

    Key options (high level):
    - **market**: ISO 10383 MIC code (e.g., 'XNYS').
    - **years**: pre-calculate holidays for given year(s).
    - **expand**: if True, calculate an entire year on first access.
    - **observed**: include observed dates.

    Notes:
    - Raises `NotImplementedError` if the named market entity is not available.
    - For details and usage patterns, see `country_holidays` documentation.
    """
    import holidays

    try:
        return getattr(holidays, market)(
            years=years,
            subdiv=subdiv,
            expand=expand,
            observed=observed,
            language=language,
            categories=categories,
        )
    except AttributeError:
        raise NotImplementedError(f"Financial market {market} not available")


def CountryHoliday(  # noqa: N802
    country: str,
    subdiv: str | None = None,
    years: int | Iterable[int] | None = None,
    expand: bool = True,
    observed: bool = True,
    prov: str | None = None,
    state: str | None = None,
) -> HolidayBase:
    """
    Note:
        Deprecated name for `country_holidays()`.
    """

    warnings.warn(
        "CountryHoliday is deprecated, use country_holidays instead.", DeprecationWarning
    )
    return country_holidays(country, subdiv, years, expand, observed, prov, state)


def _list_localized_entities(entity_codes: Iterable[str]) -> dict[str, list[str]]:
    """Get all localized entities and languages they support.

    Args:
        entity_codes:
            A list of entity codes.

    Returns:
        A dictionary where key is an entity code and value is a list of supported
        languages (either ISO 639-1 or a combination of ISO 639-1 and ISO 3166-1 codes joined
        with "_").
    """
    import holidays

    localized_countries = {}
    for entity_code in entity_codes:
        languages = getattr(holidays, entity_code).supported_languages
        if not languages:
            continue
        localized_countries[entity_code] = sorted(languages)

    return localized_countries


@cache
def list_localized_countries(include_aliases: bool = True) -> dict[str, list[str]]:
    """Get all localized countries and languages they support.

    Args:
        include_aliases:
            Whether to include entity aliases (e.g. UK for GB).

    Returns:
        A dictionary where key is an ISO 3166-1 alpha-2 country code and value is a
        list of supported languages (either ISO 639-1 or a combination of ISO 639-1
        and ISO 3166-1 codes joined with "_").
    """
    return _list_localized_entities(EntityLoader.get_country_codes(include_aliases))


@cache
def list_localized_financial(include_aliases: bool = True) -> dict[str, list[str]]:
    """Get all localized financial markets and languages they support.

    Args:
        include_aliases:
            Whether to include entity aliases (e.g. TAR for ECB, XNYS for NYSE).

    Returns:
        A dictionary where key is a market code and value is a list of supported
        subdivision codes.
    """
    return _list_localized_entities(EntityLoader.get_financial_codes(include_aliases))


def _list_supported_entities(entity_codes: Iterable[str]) -> dict[str, list[str]]:
    """Get all supported entities and their subdivisions.

    Args:
        entity_codes:
            A list of entity codes.

    Returns:
        A dictionary where key is an entity code and value is a list of supported
        subdivision codes.
    """
    import holidays

    return {
        country_code: list(getattr(holidays, country_code).subdivisions)
        for country_code in entity_codes
    }


@cache
def list_supported_countries(include_aliases: bool = True) -> dict[str, list[str]]:
    """Get all supported countries and their subdivisions.

    Args:
        include_aliases:
            Whether to include entity aliases (e.g. UK for GB).

    Returns:
        A dictionary where key is an ISO 3166-1 alpha-2 country code and value
        is a list of supported subdivision codes.
    """
    return _list_supported_entities(EntityLoader.get_country_codes(include_aliases))


@cache
def list_supported_financial(include_aliases: bool = True) -> dict[str, list[str]]:
    """Get all supported financial markets and their subdivisions.

    Args:
        include_aliases:
            Whether to include entity aliases (e.g. NYSE for XNYS, TAR for XECB).

    Returns:
        A dictionary where key is a market code and value is a list of supported
        subdivision codes.
    """
    return _list_supported_entities(EntityLoader.get_financial_codes(include_aliases))


def list_long_breaks(
    instance: HolidayBase, *, minimum_break_length: int = 3, require_weekend_overlap: bool = True
) -> list[list[date]]:
    """Return lists of consecutive holiday dates representing long breaks.

    Args:
        instance: HolidayBase object containing holidays data.
        minimum_break_length: **Minimum number of consecutive holiday days** to
            consider as a long break (default: 3).
        require_weekend_overlap: If True, only include breaks that overlap a
            weekend (default: True).

    Returns:
        A list of lists; each inner list contains consecutive `date` objects
        representing a long break that meets the criteria.
    """
    long_breaks = []
    seen_dates = set()

    for dt in sorted(instance.keys()):
        if dt in seen_dates:
            continue

        previous_working_day = instance.get_nth_working_day(dt, -1)
        next_working_day = instance.get_nth_working_day(dt, +1)
        long_break_length = (next_working_day - previous_working_day).days - 1

        if long_break_length < minimum_break_length:
            continue

        is_long_break = not require_weekend_overlap
        long_break_dates = []
        for delta_days in range(1, long_break_length + 1):
            holiday = _timedelta(previous_working_day, delta_days)
            if not is_long_break and instance._is_weekend(holiday):
                is_long_break = True
            long_break_dates.append(holiday)
            seen_dates.add(holiday)

        if is_long_break:
            long_breaks.append(long_break_dates)

    return long_breaks
