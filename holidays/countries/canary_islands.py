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

from holidays.countries.spain import Spain
from holidays.mixins.child_entity import ChildEntity


class HolidaysIC(ChildEntity, Spain):
    """Canary Islands holidays.

    Alias of a Spanish subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Spain>
        * <https://en.wikipedia.org/wiki/Canary_Islands>
    """

    country = "IC"
    parent_entity = Spain
    parent_entity_subdivision_code = "CN"
    # The autonomous community of the Canary Islands was established in 1982.
    start_year = 1983


class CanaryIslands(HolidaysIC):
    pass


class IC(CanaryIslands):
    pass
