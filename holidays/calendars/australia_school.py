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

"""Australian school holidays dataset, transcribed from official sources.

Each state and territory publishes its own school calendar; there is no national
one. Six publish term dates only, so their holidays are the gaps between terms.
New South Wales and Queensland publish the holiday periods themselves and those
are used verbatim - deriving Queensland's from its term dates reproduces its
published holidays exactly, which is the check that the derivation is sound.

Dates are student dates wherever a jurisdiction distinguishes them from staff
dates: the Northern Territory, Tasmania, Victoria and the ACT all have teachers
return before pupils, and New South Wales counts its staff development days
inside the term.

Ranges that run past 31 December appear under both years, since a year's
holidays are read from its own entry and clipped to it.

Two caveats on New South Wales. It runs two sets of term dates: Western Division
schools, in the far west of the state, start Term 1 about a week later than the
rest and their summer break runs on accordingly. Subdivisions here are states, so
one of the two has to stand for NSW, and these are the Eastern Division dates,
which cover the great majority of schools.

Its published holiday periods also stop short of the school development days that
open each term, because the department counts those inside the term even though
students do not attend. Those days are therefore not school holidays here either.
The public holidays at a term boundary are likewise excluded from its periods,
but they are covered by the PUBLIC category.

Sources:
    * [ACT](https://web.archive.org/web/20260909031430/https://www.act.gov.au/living-in-the-act/public-holidays-school-terms-and-daylight-saving)
    * [NSW](https://web.archive.org/web/20260726052159/https://education.nsw.gov.au/schooling/calendars/future-and-past-nsw-term-and-vacation-dates)
    * [NT](https://web.archive.org/web/20260906145204/https://nt.gov.au/learning/primary-and-secondary-students/school-term-dates-in-nt)
    * [QLD](https://web.archive.org/web/20260312112035/https://education.qld.gov.au/about-us/calendar/future-dates)
    * [SA](https://web.archive.org/web/20251222001032/https://www.education.sa.gov.au/parents-and-families/term-dates-south-australian-state-schools)
    * [TAS](https://web.archive.org/web/20260610091723/https://www.decyp.tas.gov.au/learning/term-dates/)
    * [VIC](https://web.archive.org/web/20260913195820/https://www.vic.gov.au/school-term-dates-and-holidays-victoria)
    * [WA](https://web.archive.org/web/20260911103607/https://www.education.wa.edu.au/future-term-dates)

Coverage stops where each jurisdiction stops publishing approved dates, so it is
uneven: the Northern Territory reaches 2032, the ACT and Tasmania only 2027.
Western Australia's 2030 onwards are marked preliminary and are left out.
"""

(SUMMER_HOLIDAYS, TERM_1_HOLIDAYS, TERM_2_HOLIDAYS, TERM_3_HOLIDAYS) = range(4)

AUSTRALIA_SCHOOL_HOLIDAYS = {
    2026: {
        "ACT": (
            (0, 1, 1, 0, 2, 1, SUMMER_HOLIDAYS),
            (0, 4, 3, 0, 4, 20, TERM_1_HOLIDAYS),
            (0, 7, 4, 0, 7, 20, TERM_2_HOLIDAYS),
            (0, 9, 26, 0, 10, 12, TERM_3_HOLIDAYS),
            (0, 12, 19, 1, 2, 1, SUMMER_HOLIDAYS),
        ),
        "NSW": (
            (0, 1, 1, 0, 1, 26, SUMMER_HOLIDAYS),
            (0, 4, 7, 0, 4, 17, TERM_1_HOLIDAYS),
            (0, 7, 6, 0, 7, 17, TERM_2_HOLIDAYS),
            (0, 9, 28, 0, 10, 9, TERM_3_HOLIDAYS),
            (0, 12, 18, 1, 1, 27, SUMMER_HOLIDAYS),
        ),
        "NT": (
            (0, 1, 1, 0, 1, 28, SUMMER_HOLIDAYS),
            (0, 4, 3, 0, 4, 13, TERM_1_HOLIDAYS),
            (0, 6, 20, 0, 7, 13, TERM_2_HOLIDAYS),
            (0, 9, 19, 0, 10, 5, TERM_3_HOLIDAYS),
            (0, 12, 11, 1, 1, 26, SUMMER_HOLIDAYS),
        ),
        "QLD": (
            (0, 1, 1, 0, 1, 26, SUMMER_HOLIDAYS),
            (0, 4, 3, 0, 4, 19, TERM_1_HOLIDAYS),
            (0, 6, 27, 0, 7, 12, TERM_2_HOLIDAYS),
            (0, 9, 19, 0, 10, 5, TERM_3_HOLIDAYS),
            (0, 12, 12, 1, 1, 26, SUMMER_HOLIDAYS),
        ),
        "SA": (
            (0, 1, 1, 0, 1, 26, SUMMER_HOLIDAYS),
            (0, 4, 11, 0, 4, 26, TERM_1_HOLIDAYS),
            (0, 7, 4, 0, 7, 19, TERM_2_HOLIDAYS),
            (0, 9, 26, 0, 10, 11, TERM_3_HOLIDAYS),
            (0, 12, 12, 1, 1, 26, SUMMER_HOLIDAYS),
        ),
        "TAS": (
            (0, 1, 1, 0, 2, 4, SUMMER_HOLIDAYS),
            (0, 4, 18, 0, 5, 3, TERM_1_HOLIDAYS),
            (0, 7, 11, 0, 7, 26, TERM_2_HOLIDAYS),
            (0, 10, 3, 0, 10, 18, TERM_3_HOLIDAYS),
            (0, 12, 19, 1, 2, 3, SUMMER_HOLIDAYS),
        ),
        "VIC": (
            (0, 1, 1, 0, 1, 27, SUMMER_HOLIDAYS),
            (0, 4, 3, 0, 4, 19, TERM_1_HOLIDAYS),
            (0, 6, 27, 0, 7, 12, TERM_2_HOLIDAYS),
            (0, 9, 19, 0, 10, 4, TERM_3_HOLIDAYS),
            (0, 12, 19, 1, 1, 27, SUMMER_HOLIDAYS),
        ),
        "WA": (
            (0, 1, 1, 0, 2, 1, SUMMER_HOLIDAYS),
            (0, 4, 3, 0, 4, 19, TERM_1_HOLIDAYS),
            (0, 7, 4, 0, 7, 19, TERM_2_HOLIDAYS),
            (0, 9, 26, 0, 10, 11, TERM_3_HOLIDAYS),
            (0, 12, 18, 1, 1, 31, SUMMER_HOLIDAYS),
        ),
    },
    2027: {
        "ACT": (
            (-1, 12, 19, 0, 2, 1, SUMMER_HOLIDAYS),
            (0, 4, 10, 0, 4, 27, TERM_1_HOLIDAYS),
            (0, 7, 3, 0, 7, 19, TERM_2_HOLIDAYS),
            (0, 9, 25, 0, 10, 11, TERM_3_HOLIDAYS),
            (0, 12, 18, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
        "NSW": (
            (-1, 12, 18, 0, 1, 27, SUMMER_HOLIDAYS),
            (0, 4, 12, 0, 4, 23, TERM_1_HOLIDAYS),
            (0, 7, 5, 0, 7, 16, TERM_2_HOLIDAYS),
            (0, 9, 27, 0, 10, 8, TERM_3_HOLIDAYS),
            (0, 12, 21, 1, 1, 28, SUMMER_HOLIDAYS),
        ),
        "NT": (
            (-1, 12, 11, 0, 1, 26, SUMMER_HOLIDAYS),
            (0, 4, 3, 0, 4, 12, TERM_1_HOLIDAYS),
            (0, 6, 19, 0, 7, 12, TERM_2_HOLIDAYS),
            (0, 9, 18, 0, 10, 4, TERM_3_HOLIDAYS),
            (0, 12, 10, 1, 1, 24, SUMMER_HOLIDAYS),
        ),
        "QLD": (
            (-1, 12, 12, 0, 1, 26, SUMMER_HOLIDAYS),
            (0, 3, 26, 0, 4, 11, TERM_1_HOLIDAYS),
            (0, 6, 26, 0, 7, 11, TERM_2_HOLIDAYS),
            (0, 9, 18, 0, 10, 4, TERM_3_HOLIDAYS),
            (0, 12, 11, 1, 1, 23, SUMMER_HOLIDAYS),
        ),
        "SA": (
            (-1, 12, 12, 0, 1, 26, SUMMER_HOLIDAYS),
            (0, 4, 10, 0, 4, 25, TERM_1_HOLIDAYS),
            (0, 7, 3, 0, 7, 18, TERM_2_HOLIDAYS),
            (0, 9, 25, 0, 10, 10, TERM_3_HOLIDAYS),
            (0, 12, 11, 1, 1, 30, SUMMER_HOLIDAYS),
        ),
        "TAS": (
            (-1, 12, 19, 0, 2, 3, SUMMER_HOLIDAYS),
            (0, 4, 10, 0, 4, 25, TERM_1_HOLIDAYS),
            (0, 7, 3, 0, 7, 18, TERM_2_HOLIDAYS),
            (0, 9, 25, 0, 10, 10, TERM_3_HOLIDAYS),
            (0, 12, 17, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
        "VIC": (
            (-1, 12, 19, 0, 1, 27, SUMMER_HOLIDAYS),
            (0, 3, 26, 0, 4, 11, TERM_1_HOLIDAYS),
            (0, 6, 26, 0, 7, 11, TERM_2_HOLIDAYS),
            (0, 9, 18, 0, 10, 3, TERM_3_HOLIDAYS),
            (0, 12, 18, 1, 1, 27, SUMMER_HOLIDAYS),
        ),
        "WA": (
            (-1, 12, 18, 0, 1, 31, SUMMER_HOLIDAYS),
            (0, 4, 10, 0, 4, 25, TERM_1_HOLIDAYS),
            (0, 7, 3, 0, 7, 18, TERM_2_HOLIDAYS),
            (0, 9, 25, 0, 10, 10, TERM_3_HOLIDAYS),
            (0, 12, 17, 1, 2, 1, SUMMER_HOLIDAYS),
        ),
    },
    2028: {
        "NSW": (
            (-1, 12, 21, 0, 1, 28, SUMMER_HOLIDAYS),
            (0, 4, 10, 0, 4, 21, TERM_1_HOLIDAYS),
            (0, 7, 10, 0, 7, 21, TERM_2_HOLIDAYS),
            (0, 10, 3, 0, 10, 13, TERM_3_HOLIDAYS),
            (0, 12, 22, 1, 1, 25, SUMMER_HOLIDAYS),
        ),
        "NT": (
            (-1, 12, 10, 0, 1, 24, SUMMER_HOLIDAYS),
            (0, 4, 8, 0, 4, 18, TERM_1_HOLIDAYS),
            (0, 6, 24, 0, 7, 17, TERM_2_HOLIDAYS),
            (0, 9, 23, 0, 10, 9, TERM_3_HOLIDAYS),
            (0, 12, 15, 1, 1, 29, SUMMER_HOLIDAYS),
        ),
        "QLD": (
            (-1, 12, 11, 0, 1, 23, SUMMER_HOLIDAYS),
            (0, 4, 1, 0, 4, 17, TERM_1_HOLIDAYS),
            (0, 6, 24, 0, 7, 9, TERM_2_HOLIDAYS),
            (0, 9, 16, 0, 10, 2, TERM_3_HOLIDAYS),
            (0, 12, 9, 1, 1, 21, SUMMER_HOLIDAYS),
        ),
        "SA": (
            (-1, 12, 11, 0, 1, 30, SUMMER_HOLIDAYS),
            (0, 4, 14, 0, 4, 30, TERM_1_HOLIDAYS),
            (0, 7, 8, 0, 7, 23, TERM_2_HOLIDAYS),
            (0, 9, 30, 0, 10, 15, TERM_3_HOLIDAYS),
            (0, 12, 16, 1, 1, 28, SUMMER_HOLIDAYS),
        ),
        "VIC": (
            (-1, 12, 18, 0, 1, 27, SUMMER_HOLIDAYS),
            (0, 4, 1, 0, 4, 17, TERM_1_HOLIDAYS),
            (0, 7, 1, 0, 7, 16, TERM_2_HOLIDAYS),
            (0, 9, 23, 0, 10, 8, TERM_3_HOLIDAYS),
            (0, 12, 22, 1, 1, 29, SUMMER_HOLIDAYS),
        ),
        "WA": (
            (-1, 12, 17, 0, 2, 1, SUMMER_HOLIDAYS),
            (0, 4, 8, 0, 4, 23, TERM_1_HOLIDAYS),
            (0, 7, 1, 0, 7, 16, TERM_2_HOLIDAYS),
            (0, 9, 23, 0, 10, 8, TERM_3_HOLIDAYS),
            (0, 12, 15, 1, 1, 30, SUMMER_HOLIDAYS),
        ),
    },
    2029: {
        "NSW": (
            (-1, 12, 22, 0, 1, 25, SUMMER_HOLIDAYS),
            (0, 4, 16, 0, 4, 27, TERM_1_HOLIDAYS),
            (0, 7, 9, 0, 7, 20, TERM_2_HOLIDAYS),
            (0, 10, 2, 0, 10, 12, TERM_3_HOLIDAYS),
            (0, 12, 21, 1, 1, 30, SUMMER_HOLIDAYS),
        ),
        "NT": (
            (-1, 12, 15, 0, 1, 29, SUMMER_HOLIDAYS),
            (0, 4, 7, 0, 4, 16, TERM_1_HOLIDAYS),
            (0, 6, 23, 0, 7, 16, TERM_2_HOLIDAYS),
            (0, 9, 22, 0, 10, 8, TERM_3_HOLIDAYS),
            (0, 12, 14, 1, 1, 29, SUMMER_HOLIDAYS),
        ),
        "QLD": (
            (-1, 12, 9, 0, 1, 21, SUMMER_HOLIDAYS),
            (0, 3, 30, 0, 4, 15, TERM_1_HOLIDAYS),
            (0, 6, 23, 0, 7, 8, TERM_2_HOLIDAYS),
            (0, 9, 15, 0, 10, 1, TERM_3_HOLIDAYS),
            (0, 12, 8, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
        "SA": (
            (-1, 12, 16, 0, 1, 28, SUMMER_HOLIDAYS),
            (0, 4, 14, 0, 4, 29, TERM_1_HOLIDAYS),
            (0, 7, 7, 0, 7, 22, TERM_2_HOLIDAYS),
            (0, 9, 29, 0, 10, 14, TERM_3_HOLIDAYS),
            (0, 12, 15, 1, 1, 28, SUMMER_HOLIDAYS),
        ),
        "VIC": (
            (-1, 12, 22, 0, 1, 29, SUMMER_HOLIDAYS),
            (0, 3, 30, 0, 4, 15, TERM_1_HOLIDAYS),
            (0, 6, 30, 0, 7, 15, TERM_2_HOLIDAYS),
            (0, 9, 22, 0, 10, 7, TERM_3_HOLIDAYS),
            (0, 12, 22, 1, 1, 29, SUMMER_HOLIDAYS),
        ),
        "WA": (
            (-1, 12, 15, 0, 1, 30, SUMMER_HOLIDAYS),
            (0, 3, 30, 0, 4, 15, TERM_1_HOLIDAYS),
            (0, 6, 30, 0, 7, 15, TERM_2_HOLIDAYS),
            (0, 9, 22, 0, 10, 7, TERM_3_HOLIDAYS),
            (0, 12, 20, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
    },
    2030: {
        "NSW": (
            (-1, 12, 21, 0, 1, 30, SUMMER_HOLIDAYS),
            (0, 4, 15, 0, 4, 26, TERM_1_HOLIDAYS),
            (0, 7, 8, 0, 7, 19, TERM_2_HOLIDAYS),
            (0, 9, 30, 0, 10, 11, TERM_3_HOLIDAYS),
            (0, 12, 20, 1, 1, 27, SUMMER_HOLIDAYS),
        ),
        "NT": (
            (-1, 12, 14, 0, 1, 29, SUMMER_HOLIDAYS),
            (0, 4, 6, 0, 4, 15, TERM_1_HOLIDAYS),
            (0, 6, 22, 0, 7, 15, TERM_2_HOLIDAYS),
            (0, 9, 21, 0, 10, 7, TERM_3_HOLIDAYS),
            (0, 12, 13, 1, 1, 28, SUMMER_HOLIDAYS),
        ),
        "SA": (
            (-1, 12, 15, 0, 1, 28, SUMMER_HOLIDAYS),
            (0, 4, 13, 0, 4, 28, TERM_1_HOLIDAYS),
            (0, 7, 6, 0, 7, 21, TERM_2_HOLIDAYS),
            (0, 9, 28, 0, 10, 13, TERM_3_HOLIDAYS),
            (0, 12, 14, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
        "VIC": (
            (-1, 12, 22, 0, 1, 29, SUMMER_HOLIDAYS),
            (0, 4, 6, 0, 4, 22, TERM_1_HOLIDAYS),
            (0, 6, 29, 0, 7, 14, TERM_2_HOLIDAYS),
            (0, 9, 21, 0, 10, 6, TERM_3_HOLIDAYS),
            (0, 12, 21, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
    },
    2031: {
        "NSW": ((-1, 12, 20, 0, 1, 27, SUMMER_HOLIDAYS),),
        "NT": (
            (-1, 12, 13, 0, 1, 28, SUMMER_HOLIDAYS),
            (0, 4, 5, 0, 4, 15, TERM_1_HOLIDAYS),
            (0, 6, 21, 0, 7, 14, TERM_2_HOLIDAYS),
            (0, 9, 20, 0, 10, 6, TERM_3_HOLIDAYS),
            (0, 12, 12, 1, 1, 27, SUMMER_HOLIDAYS),
        ),
    },
    2032: {
        "NT": (
            (-1, 12, 12, 0, 1, 27, SUMMER_HOLIDAYS),
            (0, 4, 10, 0, 4, 19, TERM_1_HOLIDAYS),
            (0, 6, 26, 0, 7, 19, TERM_2_HOLIDAYS),
            (0, 9, 25, 0, 10, 11, TERM_3_HOLIDAYS),
            (0, 12, 17, 0, 12, 31, SUMMER_HOLIDAYS),
        ),
    },
}
