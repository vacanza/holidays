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

from holidays.constants import PUBLIC, UNOFFICIAL, WORKDAY
from holidays.countries.finland import Finland


class HolidaysAX(Finland):
    """Åland Islands holidays.

    Alias of a Finnish subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    !!! note "Note"
        Åland's Autonomy Day is currently added in Finland's implementation.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Åland>
        * <https://en.wikipedia.org/wiki/Åland's_Autonomy_Day>
    """

    country = "AX"
    parent_entity = Finland
    default_language = "fi"
    supported_languages = ("en_US", "fi", "sv_FI", "th", "uk")
    supported_categories = (PUBLIC, UNOFFICIAL, WORKDAY)
    subdivisions = ()  # Override Finland subdivisions.
    subdivisions_aliases = {}  # Override Finland subdivisions aliases.
    # Åland Islands got its autonomy on May 7th, 1920.
    start_year = 1921

    def _populate_public_holidays(self) -> None:
        self.subdiv = "01"
        super()._populate_public_holidays()

    def _populate_unofficial_holidays(self) -> None:
        self.subdiv = "01"
        super()._populate_unofficial_holidays()

    def _populate_workday_holidays(self) -> None:
        self.subdiv = "01"
        super()._populate_workday_holidays()


class AlandIslands(HolidaysAX):
    pass


class AX(HolidaysAX):
    pass


class ALA(HolidaysAX):
    pass
