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

"""Polish school holidays data, transcribed from official sources.

Three of the four Polish school breaks are fixed by the Rozporządzenie Ministra Edukacji
Narodowej z dnia 11 sierpnia 2017 r. w sprawie organizacji roku szkolnego and are computed
rather than stored: the Christmas break runs Dec 23rd to Dec 31st (from Dec 22nd when that
is a Monday), the Easter break from the Thursday before Easter through the Tuesday after it,
and the summer break from the day after classes end through Aug 31st. Classes end on the
first Friday after Jun 20th, or on the Wednesday before it when the intervening Thursday is
a public holiday, which only Corpus Christi can be.

That last clause and the summer break's start were both introduced on June 13th, 2019. The
earlier wording began the summer break on the first Saturday after classes ended, which
needs no separate rule: without the Corpus Christi clause classes always ended on a Friday,
so the two readings pick the same day. The 2017-2018 calendar confirms it, ending classes on
Friday Jun 22nd, 2018 and opening the summer break the next day.

Only the winter break is set per year. The minister assigns each voivodeship a two-week
period between mid-January and the end of February, announced no later than the end of June
two years ahead, so the table below has to be extended as new announcements appear. Every
period runs Monday through Sunday, so one ISO week number per voivodeship is enough. The
number of groups is not fixed, it was four through 2024-2025 and three since, and the weeks
are not contiguous: a week is always skipped between the last two groups.

The 2020-2021 winter break is the one break set outside the usual announcement. The whole
country took it at the same time, in the first week of January, under § 11gd of the
COVID-19 schooling regulation; it needs no special case here, being week 1 for all sixteen.

Dates start with the 2017-2018 school year, the first one under the 2017 regulation. The
rules above hold from then on, so the first fully covered calendar year is 2018.

Sources:
    * [Dz.U. 2023 poz. 1211, consolidated text of the 2017 regulation](https://web.archive.org/web/20260109101730/https://api.sejm.gov.pl/eli/acts/DU/2023/1211/text.pdf)
    * [Dz.U. 2020 poz. 2111, § 11gd](https://web.archive.org/web/20260118090726/https://api.sejm.gov.pl/eli/acts/DU/2020/2111/text.pdf)
    * [Kalendarz roku szkolnego 2017/2018](https://web.archive.org/web/20250531154227/https://www.gov.pl/attachment/793fe87a-fa9e-426c-bcc0-27a8529f51c3)
    * [Ferie zimowe 2019](https://web.archive.org/web/20250526113519/https://www.gov.pl/web/edukacja/ferie-zimowe-2019)
    * [Kalendarz roku szkolnego 2019/2020](https://web.archive.org/web/20260316182418/https://www.gov.pl/attachment/44e42d57-5ee7-4f7f-ac5d-2406b6a49bcc)
    * [Kalendarz roku szkolnego 2021/2022](https://web.archive.org/web/20260202143701/https://www.gov.pl/web/edukacja/kalendarz-roku-szkolnego-20212022)
    * [Kalendarz roku szkolnego 2022/2023](https://web.archive.org/web/20260217122839/https://www.gov.pl/web/edukacja/kalendarz-roku-szkolnego-20222023)
    * [Terminy ferii zimowych w roku szkolnym 2023/2024](https://web.archive.org/web/20260616222728/https://www.gov.pl/web/edukacja/terminy-ferii-zimowych-w-roku-szkolnym-20232024)
    * [Kalendarz roku szkolnego 2024/2025](https://web.archive.org/web/20250913005131/https://www.gov.pl/attachment/a208f13d-7752-45fa-a423-79658ad01ae1)
    * [Kalendarz roku szkolnego 2025/2026](https://web.archive.org/web/20260211011152/https://www.gov.pl/attachment/7112b88a-0237-4f83-b133-0d72c4ac83dc)
    * [Kalendarz roku szkolnego 2026/2027](https://web.archive.org/web/20261023091817/https://www.gov.pl/attachment/07b00367-6dbc-48bf-a69e-eaf1da41e3b2)
    * [Terminy ferii zimowych w roku szkolnym 2027/2028](https://www.gov.pl/web/edukacja/terminy-ferii-zimowych-w-roku-szkolnym-20272028)
"""

(
    CHRISTMAS_BREAK,
    WINTER_BREAK,
    EASTER_BREAK,
    SUMMER_BREAK,
) = range(4)

# First calendar year covered in full by the 2017 regulation.
POLAND_SCHOOL_HOLIDAYS_START_YEAR = 2018

# Order of the per-voivodeship week numbers below, matching `Poland.subdivisions`.
POLAND_SCHOOL_HOLIDAY_SUBDIVS = (
    "02",  # Dolnośląskie.
    "04",  # Kujawsko-pomorskie.
    "06",  # Lubelskie.
    "08",  # Lubuskie.
    "10",  # Łódzkie.
    "12",  # Małopolskie.
    "14",  # Mazowieckie.
    "16",  # Opolskie.
    "18",  # Podkarpackie.
    "20",  # Podlaskie.
    "22",  # Pomorskie.
    "24",  # Śląskie.
    "26",  # Świętokrzyskie.
    "28",  # Warmińsko-mazurskie.
    "30",  # Wielkopolskie.
    "32",  # Zachodniopomorskie.
)

# School year start -> the ISO week each voivodeship's two-week winter break opens in.
POLAND_WINTER_BREAK_WEEKS = {
    2017: (3, 7, 5, 7, 5, 7, 3, 3, 5, 4, 5, 5, 7, 4, 7, 3),
    2018: (5, 3, 7, 3, 7, 3, 5, 5, 7, 4, 7, 7, 3, 4, 3, 5),
    2019: (7, 5, 3, 5, 3, 5, 7, 7, 3, 4, 3, 3, 5, 4, 5, 7),
    2020: (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    2021: (5, 3, 7, 3, 7, 3, 5, 5, 7, 4, 7, 7, 3, 4, 3, 5),
    2022: (7, 5, 3, 5, 3, 5, 7, 7, 3, 4, 3, 3, 5, 4, 5, 7),
    2023: (3, 7, 5, 7, 5, 7, 3, 3, 5, 4, 5, 5, 7, 4, 7, 3),
    2024: (6, 4, 8, 4, 8, 4, 6, 6, 8, 5, 8, 8, 4, 5, 4, 6),
    2025: (6, 6, 8, 8, 6, 6, 4, 6, 8, 4, 4, 8, 4, 4, 8, 6),
    2026: (3, 7, 5, 7, 3, 7, 5, 3, 3, 3, 5, 3, 5, 7, 7, 7),
    2027: (7, 3, 7, 3, 5, 7, 5, 7, 5, 3, 3, 7, 3, 5, 3, 3),
}
