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

from gettext import gettext as tr

from holidays.constants import PUBLIC, UNOFFICIAL
from holidays.countries.finland import Finland


class Aland(Finland):
    """Aland Islands holidays.

    References:
        * https://en.wikipedia.org/wiki/Public_holidays_in_%C3%85land
        * https://date.nager.at/PublicHoliday/%C3%85land-Islands/2025
        * https://www.bank-holidays.com/country/Aland-Islands_194.htm
    """

    country = "AX"
    supported_categories = (PUBLIC, UNOFFICIAL)
    subdivisions = ()
    start_year = 1920

    def _populate_unofficial_holidays(self) -> None:
        self.subdiv = "AX"
        super()._populate_unofficial_holidays()

    def _populate_public_holidays(self):
        self.subdiv = "AX"
        super()._populate_public_holidays()

        # Autonomy Day
        self._add_holiday_jun_9(tr("Självstyrelsedagen"))


class AX(Aland):
    """Alternative name for the Åland Islands holidays (ISO 3166-1 alpha-2 code)."""

    pass


class ALA(Aland):
    """Alternative name for the Åland Islands holidays (ISO 3166-1 alpha-3 code)."""

    pass
