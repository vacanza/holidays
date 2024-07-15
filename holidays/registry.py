#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

import importlib
from threading import RLock
from typing import Any, Dict, Iterable, Optional, Tuple

from holidays.holiday_base import HolidayBase

RegistryDict = Dict[str, Tuple[str, ...]]

ISO_3166: RegistryDict = {
    "AD": ("AD", "AND"),  # Andorra
    "AE": ("AE", "ARE"),  # United Arab Emirates
    "AL": ("AL", "ALB"),  # Albania
    "AM": ("AM", "ARM"),  # Armenia
    "AO": ("AO", "AGO"),  # Angola
    "AR": ("AR", "ARG"),  # Argentina
    "AS": ("AS", "ASM"),  # AmericanSamoa
    "AT": ("AT", "AUT"),  # Austria
    "AU": ("AU", "AUS"),  # Australia
    "AW": ("AW", "ABW"),  # Aruba
    "AZ": ("AZ", "AZE"),  # Azerbaijan
    "BA": ("BA", "BIH"),  # Bosnia Herzegovina
    "BB": ("BB", "BRB"),  # Barbados
    "BD": ("BD", "BGD"),  # Bangladesh
    "BE": ("BE", "BEL"),  # Belgium
    "BF": ("BF", "BFA"),  # Burkina Faso
    "BG": ("BG", "BLG"),  # Bulgaria
    "BH": ("BH", "BAH"),  # Bahrain
    "BI": ("BI", "BDI"),  # Burundi
    "BN": ("BN", "BRN"),  # Brunei
    "BO": ("BO", "BOL"),  # Bolivia
    "BR": ("BR", "BRA"),  # Brazil
    "BS": ("BS", "BHS"),  # Bahamas
    "BW": ("BW", "BWA"),  # Botswana
    "BY": ("BY", "BLR"),  # Belarus
    "BZ": ("BZ", "BLZ"),  # Belize
    "CA": ("CA", "CAN"),  # Canada
    "CH": ("CH", "CHE"),  # Switzerland
    "CL": ("CL", "CHL"),  # Chile
    "CM": ("CM", "CMR"),  # Cameroon
    "CN": ("CN", "CHN"),  # China
    "CO": ("CO", "COL"),  # Colombia
    "CR": ("CR", "CRI"),  # Costa Rica
    "CU": ("CU", "CUB"),  # Cuba
    "CW": ("CW", "CUW"),  # Curacao
    "CY": ("CY", "CYP"),  # Cyprus
    "CZ": ("CZ", "CZE"),  # Czechia
    "DE": ("DE", "DEU"),  # Germany
    "DJ": ("DJ", "DJI"),  # Djibouti
    "DK": ("DK", "DNK"),  # Denmark
    "DO": ("DO", "DOM"),  # Dominican Republic
    "DZ": ("DZ", "DZA"),  # Algeria
    "EC": ("EC", "ECU"),  # Ecuador
    "EE": ("EE", "EST"),  # Estonia
    "EG": ("EG", "EGY"),  # Egypt
    "ES": ("ES", "ESP"),  # Spain
    "ET": ("ET", "ETH"),  # Ethiopia
    "FI": ("FI", "FIN"),  # Finland
    "FR": ("FR", "FRA"),  # France
    "GA": ("GA", "GAB"),  # Gabon
    "GB": ("GB", "GBR", "UK"),  # United Kingdom
    "GE": ("GE", "GEO"),  # Georgia
    "GH": ("GH", "GHA"),  # Ghana
    "GL": ("GL", "GRL"),  # Greenland
    "GR": ("GR", "GRC"),  # Greece
    "GT": ("GT", "GUA"),  # Guatemala
    "GU": ("GU", "GUM"),  # Guam
    "HK": ("HK", "HKG"),  # HongKong
    "HN": ("HN", "HND"),  # Honduras
    "HR": ("HR", "HRV"),  # Croatia
    "HU": ("HU", "HUN"),  # Hungary
    "ID": ("ID", "IDN"),  # Indonesia
    "IE": ("IE", "IRL"),  # Ireland
    "IL": ("IL", "ISR"),  # Israel
    "IM": ("IM", "IMN"),  # IsleOfMan
    "IN": ("IN", "IND"),  # India
    "IR": ("IR", "IRN"),  # Iran
    "IS": ("IS", "ISL"),  # Iceland
    "IT": ("IT", "ITA"),  # Italy
    "JE": ("JE", "JEY"),  # Jersey
    "JM": ("JM", "JAM"),  # Jamaica
    "JO": ("JO", "JOR"),  # Jordan
    "JP": ("JP", "JPN"),  # Japan
    "KE": ("KE", "KEN"),  # Kenya
    "KG": ("KG", "KGZ"),  # Kyrgyzstan
    "KH": ("KH", "KHM"),  # Cambodia
    "KR": ("KR", "KOR"),  # SouthKorea
    "KW": ("KW", "KWT"),  # Kuwait
    "KZ": ("KZ", "KAZ"),  # Kazakhstan
    "LA": ("LA", "LAO"),  # Laos
    "LI": ("LI", "LIE"),  # Liechtenstein
    "LS": ("LS", "LSO"),  # Lesotho
    "LT": ("LT", "LTU"),  # Lithuania
    "LU": ("LU", "LUX"),  # Luxembourg
    "LV": ("LV", "LVA"),  # Latvia
    "MA": ("MA", "MOR"),  # Morocco
    "MC": ("MC", "MCO"),  # Monaco
    "MD": ("MD", "MDA"),  # Moldova
    "ME": ("ME", "MNE"),  # Montenegro
    "MG": ("MG", "MDG"),  # Madagascar
    "MH": ("MH", "MHL"),  # Marshall Islands
    "MK": ("MK", "MKD"),  # North Macedonia
    "MP": ("MP", "MNP"),  # Northern Mariana Islands
    "MT": ("MT", "MLT"),  # Malta
    "MV": ("MV", "MDV"),  # Maldives
    "MW": ("MW", "MWI"),  # Malawi
    "MX": ("MX", "MEX"),  # Mexico
    "MY": ("MY", "MYS"),  # Malaysia
    "MZ": ("MZ", "MOZ"),  # Mozambique
    "NA": ("NA", "NAM"),  # Namibia
    "NG": ("NG", "NGA"),  # Nigeria
    "NI": ("NI", "NIC"),  # Nicaragua
    "NL": ("NL", "NLD"),  # Netherlands
    "NO": ("NO", "NOR"),  # Norway
    "NZ": ("NZ", "NZL"),  # NewZealand
    "PA": ("PA", "PAN"),  # Panama
    "PE": ("PE", "PER"),  # Peru
    "PG": ("PG", "PNG"),  # Papua New Guinea
    "PH": ("PH", "PHL"),  # Philippines
    "PK": ("PK", "PAK"),  # Pakistan
    "PL": ("PL", "POL"),  # Poland
    "PR": ("PR", "PRI"),  # PuertoRico
    "PT": ("PT", "PRT"),  # Portugal
    "PW": ("PW", "PLW"),  # Palau
    "PY": ("PY", "PRY"),  # Paraguay
    "RO": ("RO", "ROU"),  # Romania
    "RS": ("RS", "SRB"),  # Serbia
    "RU": ("RU", "RUS"),  # Russia
    "SA": ("SA", "SAU"),  # Saudi Arabia
    "SC": ("SC", "SYC"),  # Seychelles
    "SE": ("SE", "SWE"),  # Sweden
    "SG": ("SG", "SGP"),  # Singapore
    "SI": ("SI", "SVN"),  # Slovenia
    "SK": ("SK", "SVK"),  # Slovakia
    "SM": ("SM", "SMR"),  # San Marino
    "SV": ("SV", "SLV"),  # ElSalvador
    "SZ": ("SZ", "SZW"),  # Eswatini
    "TD": ("TD", "TCD"),  # Chad
    "TH": ("TH", "THA"),  # Thailand
    "TL": ("TL", "TLS"),  # Timor Leste
    "TN": ("TN", "TUN"),  # Tunisia
    "TO": ("TO", "TON"),  # Tonga
    "TR": ("TR", "TUR"),  # Turkey
    "TW": ("TW", "TWN"),  # Taiwan
    "TZ": ("TZ", "TZA"),  # Tanzania
    "UA": ("UA", "UKR"),  # Ukraine
    "UM": ("UM", "UMI"),  # United States Minor Outlying Islands
    "US": ("US", "USA"),  # United States
    "UY": ("UY", "URY"),  # Uruguay
    "UZ": ("UZ", "UZB"),  # Uzbekistan
    "VA": ("VA", "VAT"),  # VaticanCity
    "VE": ("VE", "VEN"),  # Venezuela
    "VI": ("VI", "VIR"),  # United States Virgin Islands
    "VN": ("VN", "VNM"),  # Vietnam
    "VU": ("VU", "VTU"),  # Vanuatu
    "ZA": ("ZA", "ZAF"),  # South Africa
    "ZM": ("ZM", "ZMB"),  # Zambia
    "ZW": ("ZW", "ZWE"),  # Zimbabwe
}

ISO_10383: RegistryDict = {
    "IFEU": ("IFEU",),  # ICE Futures Europe
    "XECB": ("XECB",),  # ECB Exchange Rates
    # "XNYS": ("XNYS", "NYSE"),  # New York Stock Exchange
    "XNYS": ("XNYS",),  # New York Stock Exchange
}

# A re-entrant lock. Once a thread has acquired a re-entrant lock,
# the same thread may acquire it again without blocking.
# https://docs.python.org/3/library/threading.html#rlock-objects
IMPORT_LOCK = RLock()


class EntityLoader:
    """Country and financial holidays entities lazy loader."""

    __slots__ = ("entity", "entity_name", "module_name")

    def __init__(self, path: str, *args, **kwargs) -> None:
        """Set up a lazy loader."""
        if args:
            raise TypeError(
                "This is a python-holidays entity loader class. "
                "For entity inheritance purposes please import a class you "
                "want to derive from directly: e.g., "
                "`from holidays.entities.iso_3166 import Entity` or "
                "`from holidays.entities.financial import Entity`."
            )

        entity_path = path.split(".")

        self.entity = None
        self.entity_name = entity_path[-1]
        self.module_name = ".".join(entity_path[0:-1])

        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs) -> HolidayBase:
        """Create a new instance of a lazy-loaded entity."""
        cls = self.get_entity()
        return cls(*args, **kwargs)  # type: ignore[misc, operator]

    def __getattr__(self, name: str) -> Optional[Any]:
        """Return attribute of a lazy-loaded entity."""
        cls = self.get_entity()
        return getattr(cls, name)

    def __str__(self) -> str:
        """Return lazy loader object string representation."""
        return (
            f"A lazy loader for {self.get_entity()}. For inheritance please "
            f"use the '{self.module_name}.{self.entity_name}' class directly."
        )

    def get_entity(self) -> Optional[HolidayBase]:
        """Return lazy-loaded entity."""
        if self.entity is None:
            # Avoid deadlock due to importlib.import_module not being thread-safe by caching all
            # the first imports in a dedicated thread.
            with IMPORT_LOCK:
                self.entity = getattr(importlib.import_module(self.module_name), self.entity_name)

        return self.entity

    @staticmethod
    def _get_entity_codes(
        container: RegistryDict,
        include_aliases: bool = False,
    ) -> Iterable[str]:
        if include_aliases:
            for entities in container.values():
                yield from entities
        else:
            yield from container.keys()

    @staticmethod
    def get_iso_3166_codes(include_aliases: bool = False) -> Iterable[str]:
        """Get supported country codes.

        :param include_aliases:
            Whether to include entity aliases.
        """
        return EntityLoader._get_entity_codes(ISO_3166, include_aliases=include_aliases)

    @staticmethod
    def get_iso_10383_codes(include_aliases: bool = False) -> Iterable[str]:
        """Get ISO 10383 entity codes.

        :param include_aliases:
            Whether to include entity aliases.
        """
        return EntityLoader._get_entity_codes(ISO_10383, include_aliases=include_aliases)

    @staticmethod
    def load(prefix: str, scope: Dict) -> None:
        """Load country or financial entities."""
        module_entities = {
            "ISO_10383": ISO_10383,
            "ISO_3166": ISO_3166,
        }.get(prefix)

        if module_entities is None:
            return None

        for module, entities in module_entities.items():
            scope.update(
                {
                    entity: EntityLoader(
                        f"holidays.entities.{prefix}.{module}.{module.capitalize()}Holidays"
                    )
                    for entity in entities
                }
            )
