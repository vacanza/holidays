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

#  Supported holiday categories constants
BANK = "BANK"
EXTENDED = "EXTENDED"
GOVERNMENT = "GOVERNMENT"
HALF_DAY = "HALF-DAY"
PUBLIC = "PUBLIC"
SCHOOL = "SCHOOL"

CHINESE = "CHINESE"
CHRISTIAN = "CHRISTIAN"
HINDU = "HINDU"
ISLAMIC = "ISLAMIC"
JEWISH = "JEWISH"

ALL_CATEGORIES = {
    BANK,
    EXTENDED,
    GOVERNMENT,
    HALF_DAY,
    PUBLIC,
    SCHOOL,
    CHINESE,
    CHRISTIAN,
    HINDU,
    ISLAMIC,
    JEWISH,
}
