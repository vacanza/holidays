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


class HolidaysNC(France):
    """New Caledonia holidays.

    Alias of a French subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/New_Caledonia>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_France>
    """

    country = "NC"
    parent_entity = France
    subdivisions = ()  # Override France subdivisions.
    subdivisions_aliases = {}  # Override France subdivisions aliases.
    # France took formal possession of New Caledonia on September 24th, 1853.
    start_year = 1854

    def _populate_public_holidays(self) -> None:
        self.subdiv = "NC"
        super()._populate_public_holidays()


class NewCaledonia(HolidaysNC):
    pass


class NC(HolidaysNC):
    pass


class NCL(HolidaysNC):
    pass
