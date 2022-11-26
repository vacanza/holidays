#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO

from holidays.constants import SAT, SUN, JAN, MAY, JUL, SEP, OCT, DEC
from holidays.holiday_base import HolidayBase


class Botswana(HolidayBase):
    """
    https://www.gov.bw/public-holidays
    https://publicholidays.africa/botswana/2021-dates/
    https://www.timeanddate.com/holidays/botswana/
    http://www.ilo.org/dyn/travail/docs/1766/Public%20Holidays%20Act.pdf
    """

    country = "BW"
    special_holidays = {2019: ((JUL, 2, "Public Holiday"),)}

    def _populate(self, year: int):
        super()._populate(year)

        if year > 1965:
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, JAN, 2)] = "New Year's Day Holiday"

            # Easter and easter related calculations
            e = easter(year)
            good_friday = e - rd(days=2)
            easter_saturday = e - rd(days=1)
            easter_monday = e + rd(days=1)

            self[good_friday] = "Good Friday"
            self[easter_saturday] = "Holy Saturday"
            self[easter_monday] = "Easter Monday"

            self[date(year, MAY, 1)] = "Labour Day"
            ascension_day = e + rd(days=39)
            self[ascension_day] = "Ascension Day"

            self[date(year, JUL, 1)] = "Sir Seretse Khama Day"

            # 3rd Monday of July = "President's Day"
            d = date(year, JUL, 1) + rd(weekday=MO(+3))
            self[d] = "President's Day"
            self[d + rd(days=1)] = "President's Day Holiday"

            self[date(year, SEP, 30)] = "Botswana Day"
            self[date(year, OCT, 1)] = "Botswana Day Holiday"

            self[date(year, DEC, 25)] = "Christmas Day"
            self[date(year, DEC, 26)] = "Boxing Day"

        for k, v in list(self.items()):
            # Whenever Boxing Day falls on a Saturday,
            # it rolls over to the following Monday
            if (
                self.observed
                and year > 2015
                and k.weekday() == SAT
                and k.year == year
                and v.upper() in ("BOXING DAY", "LABOUR DAY")
            ):
                # Add the (Observed) holiday
                self[k + rd(days=2)] = v + " Holiday"
            if (
                self.observed
                and year > 1994
                and k.weekday() == SUN
                and k.year == year
                and v.upper() != "NEW YEAR'S DAY HOLIDAY"
            ):
                # Add the (Observed) holiday
                self[k + rd(days=1)] = v + " (Observed)"

            # If there is a holiday and an (Observed) holiday on the same day,
            # add an (Observed) holiday for that holiday
            if len(self.get(k).split(",")) > 1:
                # self.get(date) returns a string containing holidays as a
                # comma delimited string split on delimiter to determine if
                # there are multiple on the same day

                # Add an (Observed) for the one that is not (Observed)
                for i in self.get(k).split(","):
                    if " (Observed)" not in i:
                        self[k + rd(days=1)] = i.lstrip() + " (Observed)"


class BW(Botswana):
    pass


class BWA(Botswana):
    pass
