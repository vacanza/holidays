#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.countries.france import France


class HolidaysTF(France):
    """French Southern Territories holidays.

    Alias of a French subdivision that is also officially assigned
        its own country code in ISO 31661.
    See <https://www.iso.org/obp/ui#iso:code:3166:TF>
    """

    country = "TF"
    parent_entity = France
    subdivisions = ()  # Override France subdivisions.
    subdivisions_aliases = {}  # Override France subdivisions aliases.
    # This overseas territory was separated in 1955.
    start_year = 1956

    def _populate_public_holidays(self) -> None:
        """
        Get only the main holidays of France
        See <https://holidayapi.com/countries/tf/2022>
        """
        self.subdiv = "TF"
        super()._populate_public_holidays()


class FrenchSouthernTerritories(HolidaysTF):
    pass


class TF(HolidaysTF):
    pass


class ATF(HolidaysTF):
    pass
