#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.helpers import _normalize_tuple


class StaticHolidays:
    """Helper class for special and substituted holidays support.

    Populates special and substituted holidays related data from
    an external class.
    """

    def __init__(self, cls, inter_year: bool = False) -> None:
        for attribute_name in cls.__dict__.keys():
            # Special holidays.
            if attribute_name.startswith("special_") and (
                value := getattr(cls, attribute_name, None)
            ):
                setattr(self, attribute_name, value)
                self.has_special_holidays = True

            # Substituted holidays.
            elif attribute_name.startswith("substituted_") and (
                value := getattr(cls, attribute_name, None)
            ):
                setattr(self, attribute_name, value)
                self.has_substituted_holidays = True

            # Has substituted holidays from another year.
            if inter_year:
                self.weekend_workdays = set()
                for subst_data in getattr(self, "special_public_holidays", {}).values():
                    for data in _normalize_tuple(subst_data):
                        if len(data) == 5:
                            _, _, from_month, from_day, from_year = data
                            from_date = date(from_year, from_month, from_day)
                            self.weekend_workdays.add(from_date)
