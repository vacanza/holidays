#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from holidays.holiday_base import HolidayBase


class TrinidadAndTobago(HolidayBase):
    """
    Trinidad and Tobago Holidays.

    References:
      * <https://en.wikipedia.org/wiki/Public_holidays_in_Trinidad_and_Tobago>
      * <https://otp.tt/trinidad-and-tobago/national-holidays-and-awards/>
    """

    country = "TT"


class TT(TrinidadAndTobago):
    pass


class TTO(TrinidadAndTobago):
    pass
