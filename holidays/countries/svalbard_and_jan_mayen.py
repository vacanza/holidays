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

from holidays.countries.norway import Norway


class HolidaysSJ(Norway):
    """Svalbard and Jan Mayen holidays.

    Alias of Norwegian subdivisions that are also officially assigned
    its own country code in ISO 3166-1.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Svalbard>
    """

    country = "SJ"
    parent_entity = Norway
    default_language = "no"
    subdivisions = ()  # Override Norway subdivisions.
    subdivisions_aliases = {}  # Override Norway subdivisions aliases.
    supported_languages = ("en_US", "no", "th", "uk")

    def _populate_public_holidays(self) -> None:
        self.subdiv = "21"
        super()._populate_public_holidays()


class SvalbardAndJanMayen(HolidaysSJ):
    pass


class SJ(HolidaysSJ):
    pass


class SJM(HolidaysSJ):
    pass
