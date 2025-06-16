#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import importlib
from collections.abc import Iterable
from threading import RLock
from typing import Any, Optional, Union

from holidays.holiday_base import HolidayBase

RegistryDict = dict[str, tuple[str, ...]]

COUNTRIES: RegistryDict = {
    "afghanistan": ("Afghanistan", "AF", "AFG"),
    "aland_islands": ("AlandIslands", "AX", "ALA", "HolidaysAX"),
    "albania": ("Albania", "AL", "ALB"),
    "algeria": ("Algeria", "DZ", "DZA"),
    "american_samoa": ("AmericanSamoa", "AS", "ASM", "HolidaysAS"),
    "andorra": ("Andorra", "AD", "AND"),
    "angola": ("Angola", "AO", "AGO"),
    "anguilla": ("Anguilla", "AI", "AIA"),
    "antigua_and_barbuda": ("AntiguaAndBarbuda", "AG", "ATG"),
    "argentina": ("Argentina", "AR", "ARG"),
    "armenia": ("Armenia", "AM", "ARM"),
    "aruba": ("Aruba", "AW", "ABW"),
    "australia": ("Australia", "AU", "AUS"),
    "austria": ("Austria", "AT", "AUT"),
    "azerbaijan": ("Azerbaijan", "AZ", "AZE"),
    "bahamas": ("Bahamas", "BS", "BHS"),
    "bahrain": ("Bahrain", "BH", "BAH"),
    "bangladesh": ("Bangladesh", "BD", "BGD"),
    "barbados": ("Barbados", "BB", "BRB"),
    "belarus": ("Belarus", "BY", "BLR"),
    "belgium": ("Belgium", "BE", "BEL"),
    "belize": ("Belize", "BZ", "BLZ"),
    "benin": ("Benin", "BJ", "BEN"),
    "bermuda": ("Bermuda", "BM", "BMU"),
    "bolivia": ("Bolivia", "BO", "BOL"),
    "bosnia_and_herzegovina": ("BosniaAndHerzegovina", "BA", "BIH"),
    "botswana": ("Botswana", "BW", "BWA"),
    "brazil": ("Brazil", "BR", "BRA"),
    "british_virgin_islands": ("BritishVirginIslands", "VG", "VGB"),
    "brunei": ("Brunei", "BN", "BRN"),
    "bulgaria": ("Bulgaria", "BG", "BLG"),
    "burkina_faso": ("BurkinaFaso", "BF", "BFA"),
    "burundi": ("Burundi", "BI", "BDI"),
    "cambodia": ("Cambodia", "KH", "KHM"),
    "cameroon": ("Cameroon", "CM", "CMR"),
    "canada": ("Canada", "CA", "CAN"),
    "chad": ("Chad", "TD", "TCD"),
    "chile": ("Chile", "CL", "CHL"),
    "china": ("China", "CN", "CHN"),
    "cocos_islands": ("CocosIslands", "CC", "CCK"),
    "colombia": ("Colombia", "CO", "COL"),
    "congo": ("Congo", "CG", "COG"),
    "cook_islands": ("CookIslands", "CK", "COK"),
    "costa_rica": ("CostaRica", "CR", "CRI"),
    "croatia": ("Croatia", "HR", "HRV"),
    "cuba": ("Cuba", "CU", "CUB"),
    "curacao": ("Curacao", "CW", "CUW"),
    "cyprus": ("Cyprus", "CY", "CYP"),
    "czechia": ("Czechia", "CZ", "CZE"),
    "denmark": ("Denmark", "DK", "DNK"),
    "djibouti": ("Djibouti", "DJ", "DJI"),
    "dominica": ("Dominica", "DM", "DMA"),
    "dominican_republic": ("DominicanRepublic", "DO", "DOM"),
    "ecuador": ("Ecuador", "EC", "ECU"),
    "egypt": ("Egypt", "EG", "EGY"),
    "jordan": ("Jordan", "JO", "JOR"),
    "el_salvador": ("ElSalvador", "SV", "SLV"),
    "equatorial_guinea": ("EquatorialGuinea", "GQ", "GNQ"),
    "estonia": ("Estonia", "EE", "EST"),
    "eswatini": ("Eswatini", "SZ", "SZW", "Swaziland"),
    "ethiopia": ("Ethiopia", "ET", "ETH"),
    "fiji": ("Fiji", "FJ", "FJI"),
    "finland": ("Finland", "FI", "FIN"),
    "france": ("France", "FR", "FRA"),
    "french_southern_territories": ("FrenchSouthernTerritories", "TF", "ATF", "HolidaysTF"),
    "gabon": ("Gabon", "GA", "GAB"),
    "georgia": ("Georgia", "GE", "GEO"),
    "germany": ("Germany", "DE", "DEU"),
    "ghana": ("Ghana", "GH", "GHA"),
    "greece": ("Greece", "GR", "GRC"),
    "greenland": ("Greenland", "GL", "GRL"),
    "grenada": ("Grenada", "GD", "GRD"),
    "guam": ("Guam", "GU", "GUM", "HolidaysGU"),
    "guatemala": ("Guatemala", "GT", "GUA"),
    "guernsey": ("Guernsey", "GG", "GGY"),
    "guinea": ("Guinea", "GN", "GIN"),
    "guyana": ("Guyana", "GY", "GUY"),
    "haiti": ("Haiti", "HT", "HTI"),
    "honduras": ("Honduras", "HN", "HND"),
    "hongkong": ("HongKong", "HK", "HKG"),
    "hungary": ("Hungary", "HU", "HUN"),
    "iceland": ("Iceland", "IS", "ISL"),
    "india": ("India", "IN", "IND"),
    "indonesia": ("Indonesia", "ID", "IDN"),
    "iran": ("Iran", "IR", "IRN"),
    "ireland": ("Ireland", "IE", "IRL"),
    "isle_of_man": ("IsleOfMan", "IM", "IMN"),
    "israel": ("Israel", "IL", "ISR"),
    "italy": ("Italy", "IT", "ITA"),
    "ivory_coast": ("IvoryCoast", "CI", "CIV"),
    "jamaica": ("Jamaica", "JM", "JAM"),
    "japan": ("Japan", "JP", "JPN"),
    "jersey": ("Jersey", "JE", "JEY"),
    "kazakhstan": ("Kazakhstan", "KZ", "KAZ"),
    "kenya": ("Kenya", "KE", "KEN"),
    "kuwait": ("Kuwait", "KW", "KWT"),
    "kyrgyzstan": ("Kyrgyzstan", "KG", "KGZ"),
    "laos": ("Laos", "LA", "LAO"),
    "latvia": ("Latvia", "LV", "LVA"),
    "lesotho": ("Lesotho", "LS", "LSO"),
    "liechtenstein": ("Liechtenstein", "LI", "LIE"),
    "lithuania": ("Lithuania", "LT", "LTU"),
    "luxembourg": ("Luxembourg", "LU", "LUX"),
    "macau": ("Macau", "MO", "MAC"),
    "madagascar": ("Madagascar", "MG", "MDG"),
    "malawi": ("Malawi", "MW", "MWI"),
    "malaysia": ("Malaysia", "MY", "MYS"),
    "maldives": ("Maldives", "MV", "MDV"),
    "malta": ("Malta", "MT", "MLT"),
    "marshall_islands": ("MarshallIslands", "MH", "MHL", "HolidaysMH"),
    "mauritania": ("Mauritania", "MR", "MRT"),
    "mexico": ("Mexico", "MX", "MEX"),
    "micronesia": ("Micronesia", "FM", "FSM"),
    "moldova": ("Moldova", "MD", "MDA"),
    "monaco": ("Monaco", "MC", "MCO"),
    "montenegro": ("Montenegro", "ME", "MNE"),
    "morocco": ("Morocco", "MA", "MOR"),
    "mozambique": ("Mozambique", "MZ", "MOZ"),
    "namibia": ("Namibia", "NA", "NAM"),
    "nauru": ("Nauru", "NR", "NRU"),
    "nepal": ("Nepal", "NP", "NPL"),
    "netherlands": ("Netherlands", "NL", "NLD"),
    "new_zealand": ("NewZealand", "NZ", "NZL"),
    "nicaragua": ("Nicaragua", "NI", "NIC"),
    "niger": ("Niger", "NE", "NER"),
    "nigeria": ("Nigeria", "NG", "NGA"),
    "north_macedonia": ("NorthMacedonia", "MK", "MKD"),
    "northern_mariana_islands": ("NorthernMarianaIslands", "MP", "MNP", "HolidaysMP"),
    "norway": ("Norway", "NO", "NOR"),
    "oman": ("Oman", "OM", "OMN"),
    "pakistan": ("Pakistan", "PK", "PAK"),
    "palau": ("Palau", "PW", "PLW"),
    "panama": ("Panama", "PA", "PAN"),
    "papua_new_guinea": ("PapuaNewGuinea", "PG", "PNG"),
    "paraguay": ("Paraguay", "PY", "PRY"),
    "peru": ("Peru", "PE", "PER"),
    "philippines": ("Philippines", "PH", "PHL"),
    "poland": ("Poland", "PL", "POL"),
    "portugal": ("Portugal", "PT", "PRT"),
    "puerto_rico": ("PuertoRico", "PR", "PRI", "HolidaysPR"),
    "qatar": ("Qatar", "QA", "QAT"),
    "romania": ("Romania", "RO", "ROU"),
    "russia": ("Russia", "RU", "RUS"),
    "saint_kitts_and_nevis": ("SaintKittsAndNevis", "KN", "KNA"),
    "saint_lucia": ("SaintLucia", "LC", "LCA"),
    "samoa": ("Samoa", "WS", "WSM"),
    "san_marino": ("SanMarino", "SM", "SMR"),
    "sao_tome_and_principe": ("SaoTomeAndPrincipe", "ST", "STP"),
    "saudi_arabia": ("SaudiArabia", "SA", "SAU"),
    "senegal": ("Senegal", "SN", "SEN"),
    "serbia": ("Serbia", "RS", "SRB"),
    "seychelles": ("Seychelles", "SC", "SYC"),
    "sierra_leone": ("SierraLeone", "SL", "SLE"),
    "singapore": ("Singapore", "SG", "SGP"),
    "slovakia": ("Slovakia", "SK", "SVK"),
    "slovenia": ("Slovenia", "SI", "SVN"),
    "solomon_islands": ("SolomonIslands", "SB", "SLB"),
    "south_africa": ("SouthAfrica", "ZA", "ZAF"),
    "south_korea": ("SouthKorea", "KR", "KOR", "Korea"),
    "spain": ("Spain", "ES", "ESP"),
    "sri_lanka": ("SriLanka", "LK", "LKA"),
    "suriname": ("Suriname", "SR", "SUR"),
    "svalbard_and_jan_mayen": ("SvalbardAndJanMayen", "SJ", "SJM", "HolidaysSJ"),
    "sweden": ("Sweden", "SE", "SWE"),
    "switzerland": ("Switzerland", "CH", "CHE"),
    "taiwan": ("Taiwan", "TW", "TWN"),
    "tanzania": ("Tanzania", "TZ", "TZA"),
    "thailand": ("Thailand", "TH", "THA"),
    "timor_leste": ("TimorLeste", "TL", "TLS"),
    "togo": ("Togo", "TG", "TGO"),
    "tonga": ("Tonga", "TO", "TON"),
    "trinidad_and_tobago": ("TrinidadAndTobago", "TT", "TTO"),
    "tunisia": ("Tunisia", "TN", "TUN"),
    "turkey": ("Turkey", "TR", "TUR"),
    "turks_and_caicos_islands": ("TurksAndCaicosIslands", "TC", "TCA"),
    "tuvalu": ("Tuvalu", "TV", "TUV"),
    "ukraine": ("Ukraine", "UA", "UKR"),
    "united_arab_emirates": ("UnitedArabEmirates", "AE", "ARE"),
    "united_kingdom": ("UnitedKingdom", "GB", "GBR", "UK"),
    "united_states_minor_outlying_islands": (
        "UnitedStatesMinorOutlyingIslands",
        "UM",
        "UMI",
        "HolidaysUM",
    ),
    "united_states_virgin_islands": ("UnitedStatesVirginIslands", "VI", "VIR", "HolidaysVI"),
    "united_states": ("UnitedStates", "US", "USA"),
    "uruguay": ("Uruguay", "UY", "URY"),
    "uzbekistan": ("Uzbekistan", "UZ", "UZB"),
    "vanuatu": ("Vanuatu", "VU", "VTU"),
    "vatican_city": ("VaticanCity", "VA", "VAT"),
    "venezuela": ("Venezuela", "VE", "VEN"),
    "vietnam": ("Vietnam", "VN", "VNM"),
    "yemen": ("Yemen", "YE", "YEM"),
    "zambia": ("Zambia", "ZM", "ZMB"),
    "zimbabwe": ("Zimbabwe", "ZW", "ZWE"),
}

FINANCIAL: RegistryDict = {
    "european_central_bank": ("EuropeanCentralBank", "XECB", "ECB", "TAR"),
    "ice_futures_europe": ("ICEFuturesEurope", "IFEU"),
    "ny_stock_exchange": ("NewYorkStockExchange", "XNYS", "NYSE"),
    "brasil_bolsa_balcao": ("BrasilBolsaBalcao", "BVMF", "B3"),
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
                "This is a holidays entity loader class. "
                "For entity inheritance purposes please import a class you "
                "want to derive from directly: e.g., "
                "`from holidays.countries import Entity` or "
                "`from holidays.financial import Entity`."
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
        entity_length: Union[int, Iterable[int]],
        include_aliases: bool = True,
    ) -> Iterable[str]:
        entity_length = {entity_length} if isinstance(entity_length, int) else set(entity_length)
        for entities in container.values():
            for entity in entities:
                if len(entity) in entity_length:
                    yield entity
                    # Assuming that the alpha-2 code goes first.
                    if not include_aliases:
                        break

    @staticmethod
    def get_country_codes(include_aliases: bool = True) -> Iterable[str]:
        """Get supported country codes.

        :param include_aliases:
            Whether to include entity aliases (e.g. UK for GB).
        """
        return EntityLoader._get_entity_codes(COUNTRIES, 2, include_aliases)

    @staticmethod
    def get_financial_codes(include_aliases: bool = True) -> Iterable[str]:
        """Get supported financial codes.

        :param include_aliases:
            Whether to include entity aliases(e.g. TAR for ECB, XNYS for NYSE).
        """
        return EntityLoader._get_entity_codes(FINANCIAL, (3, 4), include_aliases)

    @staticmethod
    def load(prefix: str, scope: dict) -> None:
        """Load country or financial entities."""
        entity_mapping = COUNTRIES if prefix == "countries" else FINANCIAL
        for module, entities in entity_mapping.items():
            scope.update(
                {
                    entity: EntityLoader(f"holidays.{prefix}.{module}.{entity}")
                    for entity in entities
                }
            )
