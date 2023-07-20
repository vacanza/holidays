#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

# flake8: noqa: F401

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN,
    WEEKEND,
)

HOLIDAY_NAME_DELIMITER = "; "  # Holiday names separator.

# Supported holiday categories.
BANK = "bank"
EXTENDED = "extended"
GOVERNMENT = "government"
HALF_DAY = "half_day"
PUBLIC = "public"
SCHOOL = "school"
WORKDAY = "workday"

CHINESE = "chinese"
CHRISTIAN = "christian"
HEBREW = "hebrew"
HINDU = "hindu"
ISLAMIC = "islamic"

ALL_CATEGORIES = {
    BANK,
    CHINESE,
    CHRISTIAN,
    EXTENDED,
    GOVERNMENT,
    HALF_DAY,
    HEBREW,
    HINDU,
    ISLAMIC,
    PUBLIC,
    SCHOOL,
    WORKDAY,
}

# observed calculation rules
# tuple of 7 int (MON...SUN)
# 7 - next workday, -7 - prev workday
SUN_TO_MON = (0, 0, 0, 0, 0, 0, 1)
WEEKEND_TO_MON = (0, 0, 0, 0, 0, 2, 1)
SUN_TO_TUE = (0, 0, 0, 0, 0, 0, 2)
SAT_TO_MON = (0, 0, 0, 0, 0, 2, 0)
WEEKEND_TO_MON_OR_TUE = (0, 0, 0, 0, 0, 2, 2)
WEEKEND_TO_PREV_NEXT = (0, 0, 0, 0, 0, -1, 1)
THU_TO_FRI = (0, 0, 0, 1, 0, 0, 0)
TUE_TO_MON_AND_THU_TO_FRI = (0, -1, 0, 1, 0, 0, 0)
FRI_TO_SAT_AND_SUN_TO_MON = (0, 0, 0, 0, 1, 0, 1)
THU_TO_WED_AND_FRI_TO_SAT = (0, 0, 0, -1, 1, 0, 0)
FRI_TO_THU_AND_SAT_TO_SUN = (0, 0, 0, 0, -1, 1, 0)
FRI_TO_NEXTWORK = (0, 0, 0, 0, 7, 0, 0)
SAT_TO_NEXTWORK = (0, 0, 0, 0, 0, 7, 0)
SUN_TO_NEXTWORK = (0, 0, 0, 0, 0, 0, 7)
WEEKEND_TO_NEXTWORK = (0, 0, 0, 0, 0, 7, 7)
WEEKEND_TO_PREV_NEXT_WORK = (0, 0, 0, 0, 0, -7, 7)
THU_FRI_TO_NEXTWORK = (0, 0, 0, 7, 7, 0, 0)
FRI_SAT_TO_NEXTWORK = (0, 0, 0, 0, 7, 7, 0)
NEAREST_MON = (0, -1, -2, -3, 3, 2, 1)
