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

from collections.abc import Iterable
from datetime import date

from holidays.helpers import _normalize_tuple


class StaticHolidays:
    """Helper class for special and substituted holidays support.

    Populates special and substituted holidays related data from one or more
    external classes.

    When multiple classes are provided, `special_*` dictionaries are merged by
    year (entries are appended). Each dictionary is shallow-copied onto the
    instance so the source class attributes are never mutated.
    `weekend_workdays` is derived once after all sources have been loaded.
    """

    def __init__(self, cls: type | Iterable[type]) -> None:
        """
        Args:
            cls:
                A static-holidays class, or an iterable of such classes to load
                and merge in order.
        """
        classes = (cls,) if isinstance(cls, type) else tuple(cls)
        for holiday_cls in classes:
            for attribute_name in holiday_cls.__dict__:
                # Special holidays.
                if (
                    attribute_name.startswith("special_")
                    and (value := getattr(holiday_cls, attribute_name, None))
                    and isinstance(value, dict)
                ):
                    if special_holidays := getattr(self, attribute_name, None):
                        for year, holidays_tuple in value.items():
                            special_holidays[year] = _normalize_tuple(
                                special_holidays.get(year, ())
                            ) + _normalize_tuple(holidays_tuple)
                    else:
                        setattr(self, attribute_name, dict(value))

                    self.has_special_holidays = True

                # "Substituted" labels.
                elif attribute_name.startswith("substituted_") and (
                    value := getattr(holiday_cls, attribute_name, None)
                ):
                    setattr(self, attribute_name, value)

        # Populate substituted holidays from adjacent years.
        # Always rebuild from special_public_holidays (full scan below); prior
        # values are not preserved because they are fully reconstructible here.
        self.weekend_workdays: set[date] = set()
        for special_public_holidays in getattr(self, "special_public_holidays", {}).values():
            for special_public_holiday in _normalize_tuple(special_public_holidays):
                # Normally, special holiday is a 3 item tuple: (month, day, name).
                if len(special_public_holiday) < 4:  # Skip non-substituted holidays.
                    continue

                # Handle cross-year substituted holidays.
                if len(special_public_holiday) == 5:  # The fifth element is the year.
                    _, _, from_month, from_day, from_year = special_public_holiday
                    self.weekend_workdays.add(date(from_year, from_month, from_day))

                self.has_substituted_holidays = True
