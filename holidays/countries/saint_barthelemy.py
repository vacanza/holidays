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
from holidays.mixins.child_entity import ChildEntity


class HolidaysBL(ChildEntity, France):
    """Saint Barthélemy holidays.

    Alias of a French subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/Saint_Barthélemy>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_France>
    """

    country = "BL"
    parent_entity = France
    # Cession from Guadeloupe on July 15th, 2007.
    start_year = 2008


class SaintBarthelemy(HolidaysBL):
    pass


class BL(HolidaysBL):
    pass


class BLM(HolidaysBL):
    pass
