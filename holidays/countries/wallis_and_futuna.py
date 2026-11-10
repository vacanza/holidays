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


class WallisAndFutuna(ChildEntity, France):
    """Wallis and Futuna holidays.

    Alias of a French subdivision that is also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/Wallis_and_Futuna>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_France>
        * <https://www.wallis-et-futuna.gouv.fr/contenu/telechargement/14506/119308/file/AIT%20avec%20signature%20-%20MAJ%20DU%2020%20-03-2025.pdf>
        * <https://www.wallis-et-futuna.gouv.fr/index.php/contenu/telechargement/14313/117620/file/Arr%C3%AAt%C3%A9%20jours%20f%C3%A9ri%C3%A9s%202025.pdf>
    """

    country = "WF"
    parent_entity = France
    # Separation from French Caledonia on July 29th, 1961.
    start_year = 1962


class HolidaysWF(WallisAndFutuna):
    pass


class WF(WallisAndFutuna):
    pass


class WLF(WallisAndFutuna):
    pass
