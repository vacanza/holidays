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

"""Austrian school holidays data, derived from the Schulzeitgesetz 1985.

Unlike most school calendars, Austria's are set by federal law rather than published per
year, so all six breaks are computed from § 2 Schulzeitgesetz 1985 instead of transcribed.
Only two of them are staggered across the Bundesländer, and both staggerings come from the
school year itself: Burgenland, Niederösterreich and Wien start it on the 1st Monday of
September and the other six on the 2nd Monday (§ 2 Abs. 1), which moves their Hauptferien a
week earlier too (§ 2 Abs. 2 Z 2), and the Semesterferien run one week per Bundesland in a
fixed order through February (§ 2 Abs. 2 Z 1 lit. b).

The Semesterferien are the one break with per-year data. § 2 Abs. 2a lets the minister move
a single Bundesland's week by one, by regulation, where that Bundesland and its
Bildungsdirektion both apply for it on tourism grounds; the regulation has to be issued
before the start of the calendar year preceding the break. Those moves are recorded below,
and the statutory week applies to every year and Bundesland not listed.

Only the breaks themselves are covered. Individual schools may also declare a few
`schulautonome Tage` free (§ 2 Abs. 5), may opt out of the Herbstferien in favour of the
Tuesdays after Easter and Pentecost (§ 2 Abs. 5a), and may shift the edges of the
Weihnachtsferien for travel (§ 2 Abs. 4 Z 3). None of that is published centrally.

Dates start with 2021, the first calendar year that falls entirely under the current § 2
Abs. 4, which took effect on September 1st, 2020 and introduced the Herbstferien while
ending the Osterferien and Pfingstferien on the Monday rather than the Tuesday. Every break
from the 2020-2021 through the 2026-2027 school year was checked against the ministry's own
calendars, which also show where the published dates and the statute differ in presentation
rather than substance: the Herbstferien are listed from October 28th in 2024 and the
Weihnachtsferien from December 23rd in 2023, because the omitted day is a Sunday and a
Saturday respectively, already free under § 2 Abs. 4 Z 1 and Z 2 and so not part of the
break the statute names.

Sources:
    * [Schulzeitgesetz 1985, § 2](https://web.archive.org/web/20261022132837/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10009575)
    * [BGBl. I Nr. 49/2019, Ausschussbericht](https://web.archive.org/web/20250708135051/https://www.parlament.gv.at/dokument/XXVI/I/613/fname_751628.pdf)
    * [Schulferien 2021/2022](https://web.archive.org/web/20260313141155/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_21_22.html)
    * [Schulferien 2022/2023](https://web.archive.org/web/20260614032957/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_22_23.html)
    * [Schulferien 2023/2024](https://web.archive.org/web/20260607023018/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_23_24.html)
    * [Schulferien 2024/2025](https://web.archive.org/web/20260607020451/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_24_25.html)
    * [Schulferien 2025/2026](https://web.archive.org/web/20260710225417/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_25_26.html)
    * [Schulferien 2026/2027](https://web.archive.org/web/20260618083703/https://www.bmb.gv.at/Themen/schule/schulpraxis/termine/ferientermine_26_27.html)
"""

(
    AUTUMN_BREAK,
    CHRISTMAS_BREAK,
    SEMESTER_BREAK,
    EASTER_BREAK,
    WHIT_BREAK,
    SUMMER_BREAK,
) = range(6)

# First calendar year covered entirely by § 2 Abs. 4 as in effect since September 1st, 2020.
AUSTRIA_SCHOOL_HOLIDAYS_START_YEAR = 2021

# § 2 Abs. 2 Z 1 lit. b: the February week each Bundesland's Semesterferien starts in.
AUSTRIA_SEMESTER_BREAK_WEEKS = {
    "1": 2,  # Burgenland.
    "2": 2,  # Kärnten.
    "3": 1,  # Niederösterreich.
    "4": 3,  # Oberösterreich.
    "5": 2,  # Salzburg.
    "6": 3,  # Steiermark.
    "7": 2,  # Tirol.
    "8": 2,  # Vorarlberg.
    "9": 1,  # Wien.
}

# § 2 Abs. 2a moves, keyed by the calendar year the Semesterferien fall in.
AUSTRIA_SEMESTER_BREAK_WEEK_OVERRIDES = {
    # BGBl. II Nr. 487/2022: Vorarlberg.
    2024: {"8": 1},
    # BGBl. II Nr. 297/2025, Nr. 322/2025 and Nr. 343/2025: Vorarlberg, Tirol and Salzburg.
    2027: {"5": 3, "7": 3, "8": 3},
}

# § 2 Abs. 1: the Bundesländer whose school year starts on the 1st Monday of September, so
# that their Hauptferien both start and end a week before the other six (§ 2 Abs. 2 Z 2).
AUSTRIA_EARLY_SUMMER_BREAK_SUBDIVS = {
    "1",  # Burgenland.
    "3",  # Niederösterreich.
    "9",  # Wien.
}
