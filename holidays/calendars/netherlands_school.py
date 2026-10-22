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

"""Netherlands school holidays dataset, transcribed from official sources.

The Ministry of Education fixes the dates per school year and spreads them over three
regions, Noord, Midden and Zuid, to stagger holiday traffic. A school belongs to the
region its premises are in. Only the Christmas, May and summer dates are binding; the
autumn and spring dates are published as advice that schools may depart from, and are
included here as published rather than as a guarantee.

Dates come from the regulations in the Staatscourant, which cover every school year
from 2013-2014 onwards. The open data feed carries the same tables but its archived
copies of the 2014-2015, 2015-2016 and 2016-2017 school years start each period a day
early, so the regulations are used throughout.

The dataset starts with the 2013-2014 school year, the first one whose summer break no
longer differs between primary and secondary education. Up to 2012-2013 the regulation
set a separate, longer summer break for secondary schools, which three regions alone
cannot express. The Caribbean Netherlands, a fourth summer region since 2025-2026, is
left out as well; it is not part of this entity.

Every period runs from a Saturday to a Sunday: nine days for the autumn, spring and May
breaks, sixteen for the Christmas break and forty-four for the summer break. The only
exception is the 2013-2014 May break, which the regulation extends to the Monday of
Liberation Day.

Ranges that run past 31 December appear under both years, since a year's holidays are
read from its own entry and clipped to it.

Sources:
    * [Regeling vaststelling schoolvakanties 2013-2016](https://web.archive.org/web/20261022045936/https://zoek.officielebekendmakingen.nl/stcrt-2012-27185.html)
    * [Regeling vaststelling schoolvakanties 2016-2019](https://web.archive.org/web/20261022050344/https://zoek.officielebekendmakingen.nl/stcrt-2015-35695.html)
    * [Regeling vaststelling schoolvakanties 2019-2022](https://web.archive.org/web/20261022050408/https://zoek.officielebekendmakingen.nl/stcrt-2018-11687.html)
    * [Regeling vaststelling schoolvakanties 2022-2025](https://web.archive.org/web/20261022050433/https://zoek.officielebekendmakingen.nl/stcrt-2021-25317.html)
    * [Regeling vaststelling schoolvakanties 2025-2030](https://web.archive.org/web/20261022050453/https://zoek.officielebekendmakingen.nl/stcrt-2024-19237.html)
    * [Regio-indeling](https://web.archive.org/web/20261012093116/https://www.rijksoverheid.nl/themas/onderwijs/schoolvakanties/regios-schoolvakantie)
    * [Open data feed](https://web.archive.org/web/20261022045915/https://opendata.rijksoverheid.nl/v1/infotypes/schoolholidays?output=json)
"""

(
    AUTUMN_BREAK,
    CHRISTMAS_BREAK,
    SPRING_BREAK,
    MAY_BREAK,
    SUMMER_BREAK,
) = range(5)

NETHERLANDS_SCHOOL_HOLIDAYS = {
    2013: {
        "Noord": (
            (0, 10, 19, 0, 10, 27, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (0, 10, 19, 0, 10, 27, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (0, 10, 12, 0, 10, 20, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
    },
    2014: {
        "Noord": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 2, SPRING_BREAK),
            (0, 4, 26, 0, 5, 5, MAY_BREAK),
            (0, 7, 5, 0, 8, 17, SUMMER_BREAK),
            (0, 10, 11, 0, 10, 19, AUTUMN_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 15, 0, 2, 23, SPRING_BREAK),
            (0, 4, 26, 0, 5, 5, MAY_BREAK),
            (0, 7, 19, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 18, 0, 10, 26, AUTUMN_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 15, 0, 2, 23, SPRING_BREAK),
            (0, 4, 26, 0, 5, 5, MAY_BREAK),
            (0, 7, 12, 0, 8, 24, SUMMER_BREAK),
            (0, 10, 18, 0, 10, 26, AUTUMN_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
    },
    2015: {
        "Noord": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 21, 0, 3, 1, SPRING_BREAK),
            (0, 5, 2, 0, 5, 10, MAY_BREAK),
            (0, 7, 4, 0, 8, 16, SUMMER_BREAK),
            (0, 10, 17, 0, 10, 25, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 21, 0, 3, 1, SPRING_BREAK),
            (0, 5, 2, 0, 5, 10, MAY_BREAK),
            (0, 7, 11, 0, 8, 23, SUMMER_BREAK),
            (0, 10, 17, 0, 10, 25, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 14, 0, 2, 22, SPRING_BREAK),
            (0, 5, 2, 0, 5, 10, MAY_BREAK),
            (0, 7, 18, 0, 8, 30, SUMMER_BREAK),
            (0, 10, 24, 0, 11, 1, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
    },
    2016: {
        "Noord": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 27, 0, 3, 6, SPRING_BREAK),
            (0, 4, 30, 0, 5, 8, MAY_BREAK),
            (0, 7, 16, 0, 8, 28, SUMMER_BREAK),
            (0, 10, 15, 0, 10, 23, AUTUMN_BREAK),
            (0, 12, 24, 1, 1, 8, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 2, 28, SPRING_BREAK),
            (0, 4, 30, 0, 5, 8, MAY_BREAK),
            (0, 7, 9, 0, 8, 21, SUMMER_BREAK),
            (0, 10, 15, 0, 10, 23, AUTUMN_BREAK),
            (0, 12, 24, 1, 1, 8, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 2, 28, SPRING_BREAK),
            (0, 4, 30, 0, 5, 8, MAY_BREAK),
            (0, 7, 23, 0, 9, 4, SUMMER_BREAK),
            (0, 10, 22, 0, 10, 30, AUTUMN_BREAK),
            (0, 12, 24, 1, 1, 8, CHRISTMAS_BREAK),
        ),
    },
    2017: {
        "Noord": (
            (-1, 12, 24, 0, 1, 8, CHRISTMAS_BREAK),
            (0, 2, 18, 0, 2, 26, SPRING_BREAK),
            (0, 4, 22, 0, 4, 30, MAY_BREAK),
            (0, 7, 22, 0, 9, 3, SUMMER_BREAK),
            (0, 10, 21, 0, 10, 29, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 24, 0, 1, 8, CHRISTMAS_BREAK),
            (0, 2, 25, 0, 3, 5, SPRING_BREAK),
            (0, 4, 22, 0, 4, 30, MAY_BREAK),
            (0, 7, 8, 0, 8, 20, SUMMER_BREAK),
            (0, 10, 14, 0, 10, 22, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 24, 0, 1, 8, CHRISTMAS_BREAK),
            (0, 2, 25, 0, 3, 5, SPRING_BREAK),
            (0, 4, 22, 0, 4, 30, MAY_BREAK),
            (0, 7, 15, 0, 8, 27, SUMMER_BREAK),
            (0, 10, 14, 0, 10, 22, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
    },
    2018: {
        "Noord": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 24, 0, 3, 4, SPRING_BREAK),
            (0, 4, 28, 0, 5, 6, MAY_BREAK),
            (0, 7, 21, 0, 9, 2, SUMMER_BREAK),
            (0, 10, 20, 0, 10, 28, AUTUMN_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 24, 0, 3, 4, SPRING_BREAK),
            (0, 4, 28, 0, 5, 6, MAY_BREAK),
            (0, 7, 14, 0, 8, 26, SUMMER_BREAK),
            (0, 10, 20, 0, 10, 28, AUTUMN_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 2, 25, SPRING_BREAK),
            (0, 4, 28, 0, 5, 6, MAY_BREAK),
            (0, 7, 7, 0, 8, 19, SUMMER_BREAK),
            (0, 10, 13, 0, 10, 21, AUTUMN_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
    },
    2019: {
        "Noord": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 16, 0, 2, 24, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 13, 0, 8, 25, SUMMER_BREAK),
            (0, 10, 19, 0, 10, 27, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 23, 0, 3, 3, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 20, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 10, 27, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 23, 0, 3, 3, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 6, 0, 8, 18, SUMMER_BREAK),
            (0, 10, 12, 0, 10, 20, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
    },
    2020: {
        "Noord": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 15, 0, 2, 23, SPRING_BREAK),
            (0, 4, 25, 0, 5, 3, MAY_BREAK),
            (0, 7, 4, 0, 8, 16, SUMMER_BREAK),
            (0, 10, 10, 0, 10, 18, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 1, SPRING_BREAK),
            (0, 4, 25, 0, 5, 3, MAY_BREAK),
            (0, 7, 18, 0, 8, 30, SUMMER_BREAK),
            (0, 10, 17, 0, 10, 25, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 1, SPRING_BREAK),
            (0, 4, 25, 0, 5, 3, MAY_BREAK),
            (0, 7, 11, 0, 8, 23, SUMMER_BREAK),
            (0, 10, 17, 0, 10, 25, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
    },
    2021: {
        "Noord": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 2, 28, SPRING_BREAK),
            (0, 5, 1, 0, 5, 9, MAY_BREAK),
            (0, 7, 10, 0, 8, 22, SUMMER_BREAK),
            (0, 10, 16, 0, 10, 24, AUTUMN_BREAK),
            (0, 12, 25, 1, 1, 9, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 2, 28, SPRING_BREAK),
            (0, 5, 1, 0, 5, 9, MAY_BREAK),
            (0, 7, 17, 0, 8, 29, SUMMER_BREAK),
            (0, 10, 16, 0, 10, 24, AUTUMN_BREAK),
            (0, 12, 25, 1, 1, 9, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 13, 0, 2, 21, SPRING_BREAK),
            (0, 5, 1, 0, 5, 9, MAY_BREAK),
            (0, 7, 24, 0, 9, 5, SUMMER_BREAK),
            (0, 10, 23, 0, 10, 31, AUTUMN_BREAK),
            (0, 12, 25, 1, 1, 9, CHRISTMAS_BREAK),
        ),
    },
    2022: {
        "Noord": (
            (-1, 12, 25, 0, 1, 9, CHRISTMAS_BREAK),
            (0, 2, 19, 0, 2, 27, SPRING_BREAK),
            (0, 4, 30, 0, 5, 8, MAY_BREAK),
            (0, 7, 16, 0, 8, 28, SUMMER_BREAK),
            (0, 10, 15, 0, 10, 23, AUTUMN_BREAK),
            (0, 12, 24, 1, 1, 8, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 25, 0, 1, 9, CHRISTMAS_BREAK),
            (0, 2, 26, 0, 3, 6, SPRING_BREAK),
            (0, 4, 30, 0, 5, 8, MAY_BREAK),
            (0, 7, 9, 0, 8, 21, SUMMER_BREAK),
            (0, 10, 22, 0, 10, 30, AUTUMN_BREAK),
            (0, 12, 24, 1, 1, 8, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 25, 0, 1, 9, CHRISTMAS_BREAK),
            (0, 2, 26, 0, 3, 6, SPRING_BREAK),
            (0, 4, 30, 0, 5, 8, MAY_BREAK),
            (0, 7, 23, 0, 9, 4, SUMMER_BREAK),
            (0, 10, 22, 0, 10, 30, AUTUMN_BREAK),
            (0, 12, 24, 1, 1, 8, CHRISTMAS_BREAK),
        ),
    },
    2023: {
        "Noord": (
            (-1, 12, 24, 0, 1, 8, CHRISTMAS_BREAK),
            (0, 2, 25, 0, 3, 5, SPRING_BREAK),
            (0, 4, 29, 0, 5, 7, MAY_BREAK),
            (0, 7, 22, 0, 9, 3, SUMMER_BREAK),
            (0, 10, 21, 0, 10, 29, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 24, 0, 1, 8, CHRISTMAS_BREAK),
            (0, 2, 25, 0, 3, 5, SPRING_BREAK),
            (0, 4, 29, 0, 5, 7, MAY_BREAK),
            (0, 7, 8, 0, 8, 20, SUMMER_BREAK),
            (0, 10, 14, 0, 10, 22, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 24, 0, 1, 8, CHRISTMAS_BREAK),
            (0, 2, 18, 0, 2, 26, SPRING_BREAK),
            (0, 4, 29, 0, 5, 7, MAY_BREAK),
            (0, 7, 15, 0, 8, 27, SUMMER_BREAK),
            (0, 10, 14, 0, 10, 22, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
    },
    2024: {
        "Noord": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 2, 25, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 20, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 26, 0, 11, 3, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 2, 25, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 13, 0, 8, 25, SUMMER_BREAK),
            (0, 10, 26, 0, 11, 3, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 10, 0, 2, 18, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 6, 0, 8, 18, SUMMER_BREAK),
            (0, 10, 19, 0, 10, 27, AUTUMN_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
    },
    2025: {
        "Noord": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 15, 0, 2, 23, SPRING_BREAK),
            (0, 4, 26, 0, 5, 4, MAY_BREAK),
            (0, 7, 12, 0, 8, 24, SUMMER_BREAK),
            (0, 10, 18, 0, 10, 26, AUTUMN_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 2, SPRING_BREAK),
            (0, 4, 26, 0, 5, 4, MAY_BREAK),
            (0, 7, 19, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 18, 0, 10, 26, AUTUMN_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 2, SPRING_BREAK),
            (0, 4, 26, 0, 5, 4, MAY_BREAK),
            (0, 7, 5, 0, 8, 17, SUMMER_BREAK),
            (0, 10, 11, 0, 10, 19, AUTUMN_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
    },
    2026: {
        "Noord": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 21, 0, 3, 1, SPRING_BREAK),
            (0, 4, 25, 0, 5, 3, MAY_BREAK),
            (0, 7, 4, 0, 8, 16, SUMMER_BREAK),
            (0, 10, 10, 0, 10, 18, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 14, 0, 2, 22, SPRING_BREAK),
            (0, 4, 25, 0, 5, 3, MAY_BREAK),
            (0, 7, 18, 0, 8, 30, SUMMER_BREAK),
            (0, 10, 17, 0, 10, 25, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 14, 0, 2, 22, SPRING_BREAK),
            (0, 4, 25, 0, 5, 3, MAY_BREAK),
            (0, 7, 11, 0, 8, 23, SUMMER_BREAK),
            (0, 10, 17, 0, 10, 25, AUTUMN_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
    },
    2027: {
        "Noord": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 2, 28, SPRING_BREAK),
            (0, 4, 24, 0, 5, 2, MAY_BREAK),
            (0, 7, 10, 0, 8, 22, SUMMER_BREAK),
            (0, 10, 16, 0, 10, 24, AUTUMN_BREAK),
            (0, 12, 25, 1, 1, 9, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 2, 28, SPRING_BREAK),
            (0, 4, 24, 0, 5, 2, MAY_BREAK),
            (0, 7, 17, 0, 8, 29, SUMMER_BREAK),
            (0, 10, 16, 0, 10, 24, AUTUMN_BREAK),
            (0, 12, 25, 1, 1, 9, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 13, 0, 2, 21, SPRING_BREAK),
            (0, 4, 24, 0, 5, 2, MAY_BREAK),
            (0, 7, 24, 0, 9, 5, SUMMER_BREAK),
            (0, 10, 23, 0, 10, 31, AUTUMN_BREAK),
            (0, 12, 25, 1, 1, 9, CHRISTMAS_BREAK),
        ),
    },
    2028: {
        "Noord": (
            (-1, 12, 25, 0, 1, 9, CHRISTMAS_BREAK),
            (0, 2, 19, 0, 2, 27, SPRING_BREAK),
            (0, 4, 29, 0, 5, 7, MAY_BREAK),
            (0, 7, 15, 0, 8, 27, SUMMER_BREAK),
            (0, 10, 14, 0, 10, 22, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 25, 0, 1, 9, CHRISTMAS_BREAK),
            (0, 2, 26, 0, 3, 5, SPRING_BREAK),
            (0, 4, 29, 0, 5, 7, MAY_BREAK),
            (0, 7, 8, 0, 8, 20, SUMMER_BREAK),
            (0, 10, 21, 0, 10, 29, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 25, 0, 1, 9, CHRISTMAS_BREAK),
            (0, 2, 26, 0, 3, 5, SPRING_BREAK),
            (0, 4, 29, 0, 5, 7, MAY_BREAK),
            (0, 7, 22, 0, 9, 3, SUMMER_BREAK),
            (0, 10, 21, 0, 10, 29, AUTUMN_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
    },
    2029: {
        "Noord": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 2, 25, SPRING_BREAK),
            (0, 4, 28, 0, 5, 6, MAY_BREAK),
            (0, 7, 21, 0, 9, 2, SUMMER_BREAK),
            (0, 10, 20, 0, 10, 28, AUTUMN_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
        "Midden": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 2, 25, SPRING_BREAK),
            (0, 4, 28, 0, 5, 6, MAY_BREAK),
            (0, 7, 7, 0, 8, 19, SUMMER_BREAK),
            (0, 10, 20, 0, 10, 28, AUTUMN_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
        "Zuid": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 10, 0, 2, 18, SPRING_BREAK),
            (0, 4, 28, 0, 5, 6, MAY_BREAK),
            (0, 7, 14, 0, 8, 26, SUMMER_BREAK),
            (0, 10, 13, 0, 10, 21, AUTUMN_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
    },
    2030: {
        "Noord": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 16, 0, 2, 24, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 20, 0, 9, 1, SUMMER_BREAK),
        ),
        "Midden": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 23, 0, 3, 3, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 13, 0, 8, 25, SUMMER_BREAK),
        ),
        "Zuid": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 23, 0, 3, 3, SPRING_BREAK),
            (0, 4, 27, 0, 5, 5, MAY_BREAK),
            (0, 7, 6, 0, 8, 18, SUMMER_BREAK),
        ),
    },
}
