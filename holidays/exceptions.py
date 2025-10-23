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


class InvalidCountryError(Exception):
    """
    Raise exception when the country is not available.
    """

    def __init__(self, country: str):
        """
        Args:
            country (str): Name of the unavailable country
        """
        self.message = f"Country {country} not available"
        super().__init__(self.message)


class InvalidFinancialMarketError(Exception):
    """
    Raise exception when the financial market is not available.
    """

    def __init__(self, financial_market: str):
        """
        Args:
            financial_market (str): Name of the unavailable financial market
        """
        self.message = f"Financial market {financial_market} not available"
        super().__init__(self.message)


class InvalidSubdivisionError(Exception):
    """
    Raise exception when the subdivision is not available.
    """

    def __init__(self, entity_code, subdiv: str):
        """
        Args:
            entity_code (str): Entity code
            subdiv (str): Name of the unavailable subdivision
        """
        self.message = f"Entity `{entity_code}` does not have subdivision {subdiv}"
        super().__init__(self.message)
