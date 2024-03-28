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

from holidays.constants import PUBLIC, UNOFFICIAL
from holidays.countries.united_states import US


class HolidaysUM(US):
    # Alias of a US subdivision that is also officially assigned its own
    # country code in ISO 3166-1.  See
    # https://en.wikipedia.org/wiki/ISO_3166-2:US#Subdivisions_included_in_ISO_3166-1

    country = "UM"
    supported_categories = (PUBLIC, UNOFFICIAL)
    subdivisions = ()  # Override US subdivisions.

    def _populate_public_holidays(self) -> None:
        self.subdiv = "UM"
        super()._populate_public_holidays()

    def _populate_unofficial_holidays(self) -> None:
        self.subdiv = "UM"
        super()._populate_unofficial_holidays()


class UM(HolidaysUM):
    pass


class UMI(HolidaysUM):
    pass


class UnitedStatesMinorOutlyingIslands(HolidaysUM):
    pass
