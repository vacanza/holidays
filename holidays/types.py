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

from datetime import date, datetime
from typing import Iterable, Tuple, Union

CategoryArg = Union[str, Iterable[str]]

DateArg = Union[date, Tuple[int, int]]

DateLike = Union[date, datetime, str, float, int]

SpecialHoliday = Union[Tuple[int, int, str], Tuple[Tuple[int, int, str], ...]]

SubstitutedHoliday = Union[
    Union[Tuple[int, int, int, int], Tuple[int, int, int, int, int]],
    Tuple[Union[Tuple[int, int, int, int], Tuple[int, int, int, int, int]], ...],
]
YearArg = Union[int, Iterable[int]]
