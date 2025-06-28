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


from holidays.holiday_base import HolidayBase


class ChildEntity:
    """A mixin for child entities that inherit from a parent entity."""

    parent_entity: type[HolidayBase]
    """The parent entity class."""

    subdivisions: tuple[str, ...] = ()
    """Override parent subdivisions."""

    subdivisions_aliases: dict[str, str] = {}
    """Override parent subdivisions aliases."""

    def __init__(self, *args, **kwargs):
        """Initialize the child entity using its country code.

        A child entity always has its own country code that is different from
        the parent entity's country code but is a subdivision of the parent
        entity.
        """
        kwargs["subdiv"] = self.country
        super().__init__(*args, **kwargs)
