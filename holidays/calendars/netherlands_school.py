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

Every break covers a whole number of ISO weeks: one for the autumn, spring and May breaks,
two for the Christmas break and six for the summer break. It runs from the Saturday before
its first week through the Sunday that ends its last week, the single exception being the
2013-2014 May break, which the regulation extends by a day to Liberation Day on Monday, May
5th, 2014. Only the week numbers vary, so those are all that is recorded below, which is
also how the regulations stagger the regions.

Dates come from the regulations in the Staatscourant, which cover every school year from
2013-2014 onwards. The open data feed publishes the same tables, but only for the upcoming
school years, and its archived copies start a period a day early in four cases: every break
of 2014-2015 and of 2015-2016, the 2016-2017 autumn break and the 2018-2019 spring break in
Zuid. The regulations are therefore used throughout.

The dataset starts with the 2013-2014 school year, the first one whose summer break no
longer differs between primary and secondary education. Up to 2012-2013 the regulation set a
separate, longer summer break for secondary schools, which three regions alone cannot
express. The Caribbean Netherlands, a fourth summer region since 2025-2026, is left out as
well; Bonaire, Sint Eustatius and Saba are the separate `BQ` entity.

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

# Number of ISO weeks each break covers.
NETHERLANDS_SCHOOL_HOLIDAY_WEEK_COUNTS = {
    AUTUMN_BREAK: 1,
    CHRISTMAS_BREAK: 2,
    SPRING_BREAK: 1,
    MAY_BREAK: 1,
    SUMMER_BREAK: 6,
}

# The Christmas break is nationwide and falls in week 52 of every school year covered here.
NETHERLANDS_CHRISTMAS_BREAK_WEEK = 52

# The 2013-2014 May break ran a day longer, through Liberation Day on May 5th, 2014.
NETHERLANDS_EXTENDED_MAY_BREAK_SCHOOL_YEARS = {2013}

# Order of the per-region week numbers below.
NETHERLANDS_SCHOOL_HOLIDAY_REGIONS = ("Noord", "Midden", "Zuid")

# School year start -> autumn, spring and summer weeks per region, then the May break week.
# The Christmas break is the same nationwide, so it is not repeated here.
NETHERLANDS_SCHOOL_HOLIDAYS = {
    2013: ((43, 43, 42), (9, 8, 8), (28, 30, 29), 18),
    2014: ((42, 43, 43), (9, 9, 8), (28, 29, 30), 19),
    2015: ((43, 43, 44), (9, 8, 8), (29, 28, 30), 18),
    2016: ((42, 42, 43), (8, 9, 9), (30, 28, 29), 17),
    2017: ((43, 42, 42), (9, 9, 8), (30, 29, 28), 18),
    2018: ((43, 43, 42), (8, 9, 9), (29, 30, 28), 18),
    2019: ((43, 43, 42), (8, 9, 9), (28, 30, 29), 18),
    2020: ((42, 43, 43), (8, 8, 7), (28, 29, 30), 18),
    2021: ((42, 42, 43), (8, 9, 9), (29, 28, 30), 18),
    2022: ((42, 43, 43), (9, 9, 8), (30, 28, 29), 18),
    2023: ((43, 42, 42), (8, 8, 7), (30, 29, 28), 18),
    2024: ((44, 44, 43), (8, 9, 9), (29, 30, 28), 18),
    2025: ((43, 43, 42), (9, 8, 8), (28, 30, 29), 18),
    2026: ((42, 43, 43), (8, 8, 7), (28, 29, 30), 17),
    2027: ((42, 42, 43), (8, 9, 9), (29, 28, 30), 18),
    2028: ((42, 43, 43), (8, 8, 7), (30, 28, 29), 18),
    2029: ((43, 43, 42), (8, 9, 9), (30, 29, 28), 18),
}
