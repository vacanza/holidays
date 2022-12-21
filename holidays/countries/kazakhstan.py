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

from datetime import date, timedelta

from holidays.constants import JAN, MAR, MAY, JUL, AUG, OCT, DEC, WEEKEND
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Kazakhstan(HolidayBase):
    """
    1. https://www.officeholidays.com/countries/kazakhstan/2020
    2. https://egov.kz/cms/en/articles/holidays-calend
    3. https://en.wikipedia.org/wiki/Public_holidays_in_Kazakhstan

    All holidays get observed on weekdays if they fall on weekends
    and this has been implemented.

    In the event that a national holiday falls on weekend (Saturday or Sunday),
    the days-off shall be extended by one day.

    First day of Qurban Ait, celebrated by Muslim calendar,
    the 7th of January - Orthodox Christmas
    are non working days (without extending).

    http://adilet.zan.kz/rus/docs/K1500000414#z85
    According to paragraph 3 of Article 85 of the Labor Code of the RK
    for efficient usage of working in the period of holidays
    the Government has a right to carry days-off to other working days, but
    this has not been implemented as yet.
    """

    country = "KZ"

    def _populate(self, year):
        super()._populate(year)

        base_holidays = HolidayBase(year)
        non_extending_holidays = []

        """
        Populate the holidays for a given year
        """
        # New Year's holiday (2 days)
        base_holidays[date(year, JAN, 1)] = "New Year"
        base_holidays[date(year, JAN, 2)] = "New Year Holiday"

        # Orthodox Christmas
        hol_date = date(year, JAN, 7)

        non_extending_holidays.append(hol_date)

        base_holidays[hol_date] = "Orthodox Christmas"

        # Women's Day
        base_holidays[date(year, MAR, 8)] = "Women's Day"

        # Nauryz Holiday (3 days)
        base_holidays[date(year, MAR, 21)] = "Nauryz"
        base_holidays[date(year, MAR, 22)] = "Nauryz Holiday"
        base_holidays[date(year, MAR, 23)] = "Nauryz Holiday"

        # People Solidarity Holiday
        base_holidays[date(year, MAY, 1)] = "People's Solidarity Day"

        # Defender's Day
        base_holidays[date(year, MAY, 7)] = "Defender's Day"

        # Victory Day
        base_holidays[date(year, MAY, 9)] = "Victory Day"

        # Capital City Day
        base_holidays[date(year, JUL, 6)] = "Capital City Day"

        # Kurban Ait
        for hol_date in _islamic_to_gre(year, 12, 10):
            non_extending_holidays.append(hol_date)

            base_holidays[hol_date] = "Kurban Ait"

        # Constitution Day
        base_holidays[date(year, AUG, 30)] = "Constitution Day"

        # Republic Day
        if year >= 2022:
            base_holidays[date(year, OCT, 25)] = "Republic Day"

        # First President Day
        if year < 2022:
            base_holidays[date(year, DEC, 1)] = "First President Day"

        # Independence Day (2 days)
        base_holidays[date(year, DEC, 16)] = "Independence Day"

        if year < 2022:
            base_holidays[date(year, DEC, 17)] = "Independence Day Holiday"

        # Extend the holidays
        for hol_date in base_holidays:
            self[hol_date] = base_holidays[hol_date]

            if hol_date in non_extending_holidays:
                continue

            if hol_date.weekday() in WEEKEND:
                ext_hol_date = hol_date + timedelta(days=1)

                while (
                    ext_hol_date in (base_holidays | self)
                    or ext_hol_date.weekday() in WEEKEND
                ):
                    ext_hol_date += timedelta(days=1)

                self[ext_hol_date] = self[hol_date] + (
                    " Holiday" if self[hol_date][-7:] != "Holiday" else ""
                )


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass
