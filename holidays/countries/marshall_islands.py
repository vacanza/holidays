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

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_PREV_FRI, SUN_TO_NEXT_MON


class MarshallIslands(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """Marshall Islands holidays.

    References:
        * [Public Holiday Act 1988](https://web.archive.org/web/20240722022301/http://rmiparliament.org/cms/images/LEGISLATION/PRINCIPAL/1988/1988-0016/PublicHolidaysAct1988_1.pdf)
        * [P.L. 2003-99](https://web.archive.org/web/20250826051106/http://rmiparliament.org/cms/library/public-laws-by-years/22-2003.html?download=219:p-l-2003-99-public-holidays-march-1st-amendment-act-2003&start=20)
        * [P.L. 2015-38](https://web.archive.org/web/20250826045904/https://www.rmiparliament.org/cms/images/LEGISLATION/PHOCA/P.L._2015/P.L.%202015-38%20Public%20Holiday%20Amendment%20Act%202015.pdf)
        * [Public Holidays Act 1988 (Consolidated)](https://web.archive.org/web/20250826051925/http://rmiparliament.org/cms/images/LEGISLATION/PRINCIPAL/1988/1988-0016/1988-0016_2.pdf)
        * <https://web.archive.org/web/20240613114250/https://rmiparliament.org/cms/component/content/article/14-pressrelease/49-important-public-holidays.html?Itemid=101>
        * <https://web.archive.org/web/20230528174331/http://www.rmiembassyus.org/country-profile>
        * <https://en.wikipedia.org/wiki/Elections_in_the_Marshall_Islands>
        * [Nuclear Victims Remembrance Day](https://web.archive.org/web/20240421213436/https://www.pscrmi.net/_files/ugd/8c401f_ac2373f837334b19b6033c93867fb467.pdf)
        * <http://archive.today/2026.03.18-032824/https://www.pomoculture.org/2020/06/25/how-natives-drink-bravo-shots-for-example-mourning-and-nuclear-kitsch/>
        * [Constitution Day](https://web.archive.org/web/20241114230942/https://www.pscrmi.net/_files/ugd/8c401f_048d743d0fd742df980a09fce125c8fa.pdf)
        * [Fisherman's Day](https://web.archive.org/web/20241115013042/https://www.pscrmi.net/_files/ugd/8c401f_c1448f1df14a4244bb6391179aa85e5c.pdf)
        * [Manit Day](https://web.archive.org/web/20241115012706/https://www.pscrmi.net/_files/ugd/8c401f_39a1a9974cf54827b2017acc73a5018d.pdf)
        * [2019-2026](https://web.archive.org/web/20260208042153/https://www.pscrmi.net/rmi-holiday-memos)
    """

    country = "MH"
    # %s (observed).
    observed_label = "%s Holiday"
    # Public Holiday Act 1988.
    start_year = 1989

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        name = "New Year's Day"
        self._add_observed(self._add_new_years_day(name))
        self._add_observed(self._next_year_new_years_day, name=name)

        # Public Law 1995-134.
        # P.L. 2003-99 (Dec 2003): renamed to Memorial Day and Nuclear Survivors Remembrance Day.
        # P.L. 2005-35 (~May 2005): reverted to Nuclear Victims Remembrance Day.
        if self._year >= 1996:
            self._add_observed(
                self._add_holiday_mar_1(
                    # Memorial Day and Nuclear Survivors Remembrance Day.
                    "Memorial Day and Nuclear Survivors Remembrance Day"
                    if 2004 <= self._year <= 2005
                    # Nuclear Victims Remembrance Day.
                    else "Nuclear Victims Remembrance Day"
                )
            )

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Public Law 2005-35.
        if self._year >= 2006:
            # Constitution Day.
            self._add_observed(self._add_holiday_may_1("Constitution Day"))

        # Public Law 1995-134.
        if self._year >= 1996:
            # Fisherman's Day.
            self._add_holiday_1st_fri_of_jul("Fisherman's Day")

            # Dri-jerbal Day.
            self._add_holiday_1st_fri_of_sep("Dri-jerbal Day")

            # Manit Day.
            self._add_holiday_last_fri_of_sep("Manit Day")

        # President's Day.
        self._add_observed(self._add_holiday_nov_17("President's Day"))

        # Public Law 2015-38.
        if self._year >= 2015 and self._year % 4 == 3:
            # General Election Day.
            self._add_holiday_3rd_mon_of_nov("General Election Day")

        # Gospel Day.
        self._add_holiday_1st_fri_of_dec("Gospel Day")

        # Christmas Day.
        self._add_observed(self._add_christmas_day("Christmas Day"))


class HolidaysMH(MarshallIslands):
    pass


class MH(MarshallIslands):
    pass


class MHL(MarshallIslands):
    pass
