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

from holidays.countries.france import France


class HolidaysYT(France):
    """Mayotte holidays.

    Alias of a French subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/French_Guiana>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_France>
    """

    country = "YT"
    parent_entity = France
    subdivisions = ()  # Override France subdivisions.
    subdivisions_aliases = {}  # Override France subdivisions aliases.
    # Sold to France on April 25th, 1841.
    start_year = 1842

    def _populate_public_holidays(self) -> None:
        self.subdiv = "976"
        super()._populate_public_holidays()


class Mayotte(HolidaysYT):
    pass


class YT(HolidaysYT):
    pass


class MYT(HolidaysYT):
    pass
