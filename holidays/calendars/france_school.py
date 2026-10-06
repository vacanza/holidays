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

"""France school holidays dataset, from the official school calendar open data.

The Ministry of National Education sets the school calendar of mainland France by
arrêté, a few years ahead, and publishes it as open data. Mainland France is split
into three zones by académie, which share the All Saints', Christmas and summer
breaks and the Ascension bridge but stagger the winter and spring breaks:

    * Zone A: Besançon, Bordeaux, Clermont-Ferrand, Dijon, Grenoble, Limoges, Lyon,
      Poitiers.
    * Zone B: Aix-Marseille, Amiens, Lille, Nancy-Metz, Nantes, Nice, Normandie,
      Orléans-Tours, Reims, Rennes, Strasbourg.
    * Zone C: Créteil, Montpellier, Paris, Toulouse, Versailles.

The calendar gives the day classes end (pupils leave after class) and the day they
resume (in the morning). A break runs from the first day off to the day before
classes resume. Pupils without Saturday classes are off from Friday evening, so a
break whose classes end on a Saturday starts that Saturday. The Ascension bridge
always runs from Ascension Thursday to the following Sunday.

Ranges that run past 31 December appear under both years, since a year's holidays
are read from its own entry and clipped to it.

Sources:
    * [Calendrier scolaire](https://web.archive.org/web/20260206165036/https://www.education.gouv.fr/calendrier-scolaire-100148)
    * [Le calendrier scolaire (open data)](https://web.archive.org/web/20260202011841/https://data.education.gouv.fr/explore/dataset/fr-en-calendrier-scolaire/)
    * [Arrêté du 7 décembre 2022 (2023-2024 to 2025-2026)](https://web.archive.org/web/20250326034935/https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046704476/)
    * [Arrêté du 22 octobre 2025 (2026-2027)](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000052416058)
    * [Arrêté du 21 juillet 2026 (2027-2028)](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054457294)

The open data starts with the 2017-2018 school year. The summer break of 2028 is not
included, since the date classes resume in September 2028 is not published yet.
"""

(
    ALL_SAINTS_BREAK,
    CHRISTMAS_BREAK,
    WINTER_BREAK,
    SPRING_BREAK,
    ASCENSION_BREAK,
    SUMMER_BREAK,
) = range(6)

FRANCE_SCHOOL_HOLIDAYS = {
    2017: {
        "A": (
            (0, 10, 21, 0, 11, 5, ALL_SAINTS_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "B": (
            (0, 10, 21, 0, 11, 5, ALL_SAINTS_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "C": (
            (0, 10, 21, 0, 11, 5, ALL_SAINTS_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
    },
    2018: {
        "A": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 10, 0, 2, 25, WINTER_BREAK),
            (0, 4, 7, 0, 4, 22, SPRING_BREAK),
            (0, 7, 7, 0, 9, 2, SUMMER_BREAK),
            (0, 10, 20, 0, 11, 4, ALL_SAINTS_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 24, 0, 3, 11, WINTER_BREAK),
            (0, 4, 21, 0, 5, 6, SPRING_BREAK),
            (0, 7, 7, 0, 9, 2, SUMMER_BREAK),
            (0, 10, 20, 0, 11, 4, ALL_SAINTS_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 3, 4, WINTER_BREAK),
            (0, 4, 14, 0, 4, 29, SPRING_BREAK),
            (0, 7, 7, 0, 9, 2, SUMMER_BREAK),
            (0, 10, 20, 0, 11, 4, ALL_SAINTS_BREAK),
            (0, 12, 22, 1, 1, 6, CHRISTMAS_BREAK),
        ),
    },
    2019: {
        "A": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 16, 0, 3, 3, WINTER_BREAK),
            (0, 4, 13, 0, 4, 28, SPRING_BREAK),
            (0, 5, 30, 0, 6, 2, ASCENSION_BREAK),
            (0, 7, 6, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 11, 3, ALL_SAINTS_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 9, 0, 2, 24, WINTER_BREAK),
            (0, 4, 6, 0, 4, 22, SPRING_BREAK),
            (0, 5, 30, 0, 6, 2, ASCENSION_BREAK),
            (0, 7, 6, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 11, 3, ALL_SAINTS_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 22, 0, 1, 6, CHRISTMAS_BREAK),
            (0, 2, 23, 0, 3, 10, WINTER_BREAK),
            (0, 4, 20, 0, 5, 5, SPRING_BREAK),
            (0, 5, 30, 0, 6, 2, ASCENSION_BREAK),
            (0, 7, 6, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 11, 3, ALL_SAINTS_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
    },
    2020: {
        "A": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 8, WINTER_BREAK),
            (0, 4, 18, 0, 5, 3, SPRING_BREAK),
            (0, 5, 21, 0, 5, 24, ASCENSION_BREAK),
            (0, 7, 4, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 17, 0, 11, 1, ALL_SAINTS_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 15, 0, 3, 1, WINTER_BREAK),
            (0, 4, 11, 0, 4, 26, SPRING_BREAK),
            (0, 5, 21, 0, 5, 24, ASCENSION_BREAK),
            (0, 7, 4, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 17, 0, 11, 1, ALL_SAINTS_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 8, 0, 2, 23, WINTER_BREAK),
            (0, 4, 4, 0, 4, 19, SPRING_BREAK),
            (0, 5, 21, 0, 5, 24, ASCENSION_BREAK),
            (0, 7, 4, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 17, 0, 11, 1, ALL_SAINTS_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
    },
    2021: {
        "A": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 6, 0, 2, 21, WINTER_BREAK),
            (0, 4, 10, 0, 4, 25, SPRING_BREAK),
            (0, 5, 13, 0, 5, 16, ASCENSION_BREAK),
            (0, 7, 7, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 23, 0, 11, 7, ALL_SAINTS_BREAK),
            (0, 12, 18, 1, 1, 2, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 3, 7, WINTER_BREAK),
            (0, 4, 10, 0, 4, 25, SPRING_BREAK),
            (0, 5, 13, 0, 5, 16, ASCENSION_BREAK),
            (0, 7, 7, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 23, 0, 11, 7, ALL_SAINTS_BREAK),
            (0, 12, 18, 1, 1, 2, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 13, 0, 2, 28, WINTER_BREAK),
            (0, 4, 10, 0, 4, 25, SPRING_BREAK),
            (0, 5, 13, 0, 5, 16, ASCENSION_BREAK),
            (0, 7, 7, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 23, 0, 11, 7, ALL_SAINTS_BREAK),
            (0, 12, 18, 1, 1, 2, CHRISTMAS_BREAK),
        ),
    },
    2022: {
        "A": (
            (-1, 12, 18, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 12, 0, 2, 27, WINTER_BREAK),
            (0, 4, 16, 0, 5, 1, SPRING_BREAK),
            (0, 5, 26, 0, 5, 29, ASCENSION_BREAK),
            (0, 7, 8, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 22, 0, 11, 6, ALL_SAINTS_BREAK),
            (0, 12, 17, 1, 1, 2, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 18, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 5, 0, 2, 20, WINTER_BREAK),
            (0, 4, 9, 0, 4, 24, SPRING_BREAK),
            (0, 5, 26, 0, 5, 29, ASCENSION_BREAK),
            (0, 7, 8, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 22, 0, 11, 6, ALL_SAINTS_BREAK),
            (0, 12, 17, 1, 1, 2, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 18, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 19, 0, 3, 6, WINTER_BREAK),
            (0, 4, 23, 0, 5, 8, SPRING_BREAK),
            (0, 5, 26, 0, 5, 29, ASCENSION_BREAK),
            (0, 7, 8, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 22, 0, 11, 6, ALL_SAINTS_BREAK),
            (0, 12, 17, 1, 1, 2, CHRISTMAS_BREAK),
        ),
    },
    2023: {
        "A": (
            (-1, 12, 17, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 4, 0, 2, 19, WINTER_BREAK),
            (0, 4, 8, 0, 4, 23, SPRING_BREAK),
            (0, 5, 18, 0, 5, 21, ASCENSION_BREAK),
            (0, 7, 8, 0, 9, 3, SUMMER_BREAK),
            (0, 10, 21, 0, 11, 5, ALL_SAINTS_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 17, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 11, 0, 2, 26, WINTER_BREAK),
            (0, 4, 15, 0, 5, 1, SPRING_BREAK),
            (0, 5, 18, 0, 5, 21, ASCENSION_BREAK),
            (0, 7, 8, 0, 9, 3, SUMMER_BREAK),
            (0, 10, 21, 0, 11, 5, ALL_SAINTS_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 17, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 18, 0, 3, 5, WINTER_BREAK),
            (0, 4, 22, 0, 5, 8, SPRING_BREAK),
            (0, 5, 18, 0, 5, 21, ASCENSION_BREAK),
            (0, 7, 8, 0, 9, 3, SUMMER_BREAK),
            (0, 10, 21, 0, 11, 5, ALL_SAINTS_BREAK),
            (0, 12, 23, 1, 1, 7, CHRISTMAS_BREAK),
        ),
    },
    2024: {
        "A": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 17, 0, 3, 3, WINTER_BREAK),
            (0, 4, 13, 0, 4, 28, SPRING_BREAK),
            (0, 5, 9, 0, 5, 12, ASCENSION_BREAK),
            (0, 7, 6, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 11, 3, ALL_SAINTS_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 24, 0, 3, 10, WINTER_BREAK),
            (0, 4, 20, 0, 5, 5, SPRING_BREAK),
            (0, 5, 9, 0, 5, 12, ASCENSION_BREAK),
            (0, 7, 6, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 11, 3, ALL_SAINTS_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 23, 0, 1, 7, CHRISTMAS_BREAK),
            (0, 2, 10, 0, 2, 25, WINTER_BREAK),
            (0, 4, 6, 0, 4, 21, SPRING_BREAK),
            (0, 5, 9, 0, 5, 12, ASCENSION_BREAK),
            (0, 7, 6, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 19, 0, 11, 3, ALL_SAINTS_BREAK),
            (0, 12, 21, 1, 1, 5, CHRISTMAS_BREAK),
        ),
    },
    2025: {
        "A": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 22, 0, 3, 9, WINTER_BREAK),
            (0, 4, 19, 0, 5, 4, SPRING_BREAK),
            (0, 5, 29, 0, 6, 1, ASCENSION_BREAK),
            (0, 7, 5, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 18, 0, 11, 2, ALL_SAINTS_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 8, 0, 2, 23, WINTER_BREAK),
            (0, 4, 5, 0, 4, 21, SPRING_BREAK),
            (0, 5, 29, 0, 6, 1, ASCENSION_BREAK),
            (0, 7, 5, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 18, 0, 11, 2, ALL_SAINTS_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 21, 0, 1, 5, CHRISTMAS_BREAK),
            (0, 2, 15, 0, 3, 2, WINTER_BREAK),
            (0, 4, 12, 0, 4, 27, SPRING_BREAK),
            (0, 5, 29, 0, 6, 1, ASCENSION_BREAK),
            (0, 7, 5, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 18, 0, 11, 2, ALL_SAINTS_BREAK),
            (0, 12, 20, 1, 1, 4, CHRISTMAS_BREAK),
        ),
    },
    2026: {
        "A": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 7, 0, 2, 22, WINTER_BREAK),
            (0, 4, 4, 0, 4, 19, SPRING_BREAK),
            (0, 5, 14, 0, 5, 17, ASCENSION_BREAK),
            (0, 7, 4, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 17, 0, 11, 1, ALL_SAINTS_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 14, 0, 3, 1, WINTER_BREAK),
            (0, 4, 11, 0, 4, 26, SPRING_BREAK),
            (0, 5, 14, 0, 5, 17, ASCENSION_BREAK),
            (0, 7, 4, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 17, 0, 11, 1, ALL_SAINTS_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 20, 0, 1, 4, CHRISTMAS_BREAK),
            (0, 2, 21, 0, 3, 8, WINTER_BREAK),
            (0, 4, 18, 0, 5, 3, SPRING_BREAK),
            (0, 5, 14, 0, 5, 17, ASCENSION_BREAK),
            (0, 7, 4, 0, 8, 31, SUMMER_BREAK),
            (0, 10, 17, 0, 11, 1, ALL_SAINTS_BREAK),
            (0, 12, 19, 1, 1, 3, CHRISTMAS_BREAK),
        ),
    },
    2027: {
        "A": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 13, 0, 2, 28, WINTER_BREAK),
            (0, 4, 10, 0, 4, 25, SPRING_BREAK),
            (0, 5, 6, 0, 5, 9, ASCENSION_BREAK),
            (0, 7, 3, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 23, 0, 11, 7, ALL_SAINTS_BREAK),
            (0, 12, 18, 1, 1, 2, CHRISTMAS_BREAK),
        ),
        "B": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 20, 0, 3, 7, WINTER_BREAK),
            (0, 4, 17, 0, 5, 2, SPRING_BREAK),
            (0, 5, 6, 0, 5, 9, ASCENSION_BREAK),
            (0, 7, 3, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 23, 0, 11, 7, ALL_SAINTS_BREAK),
            (0, 12, 18, 1, 1, 2, CHRISTMAS_BREAK),
        ),
        "C": (
            (-1, 12, 19, 0, 1, 3, CHRISTMAS_BREAK),
            (0, 2, 6, 0, 2, 21, WINTER_BREAK),
            (0, 4, 3, 0, 4, 18, SPRING_BREAK),
            (0, 5, 6, 0, 5, 9, ASCENSION_BREAK),
            (0, 7, 3, 0, 9, 1, SUMMER_BREAK),
            (0, 10, 23, 0, 11, 7, ALL_SAINTS_BREAK),
            (0, 12, 18, 1, 1, 2, CHRISTMAS_BREAK),
        ),
    },
    2028: {
        "A": (
            (-1, 12, 18, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 19, 0, 3, 5, WINTER_BREAK),
            (0, 4, 22, 0, 5, 8, SPRING_BREAK),
            (0, 5, 25, 0, 5, 28, ASCENSION_BREAK),
        ),
        "B": (
            (-1, 12, 18, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 5, 0, 2, 20, WINTER_BREAK),
            (0, 4, 8, 0, 4, 23, SPRING_BREAK),
            (0, 5, 25, 0, 5, 28, ASCENSION_BREAK),
        ),
        "C": (
            (-1, 12, 18, 0, 1, 2, CHRISTMAS_BREAK),
            (0, 2, 12, 0, 2, 27, WINTER_BREAK),
            (0, 4, 15, 0, 5, 1, SPRING_BREAK),
            (0, 5, 25, 0, 5, 28, ASCENSION_BREAK),
        ),
    },
}

__all__ = (
    "ALL_SAINTS_BREAK",
    "ASCENSION_BREAK",
    "CHRISTMAS_BREAK",
    "FRANCE_SCHOOL_HOLIDAYS",
    "SPRING_BREAK",
    "SUMMER_BREAK",
    "WINTER_BREAK",
)
