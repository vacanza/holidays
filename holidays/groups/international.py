#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.calendars.gregorian import JAN


class InternationalHolidays:
    """
    International holidays.
    """

    @property
    def _next_year_new_years_day(self):
        """
        Return New Year's Day of next year.
        """
        return date(self._year + 1, JAN, 1)

    def _add_africa_day(self, name):
        """
        Add Africa Day (May 25th)

        Africa Day (formerly African Freedom Day and African Liberation Day)
        is the annual commemoration of the foundation of the Organisation
        of African Unity on 25 May 1963.
        https://en.wikipedia.org/wiki/Africa_Day
        """
        return self._add_holiday_may_25(name)

    def _add_anzac_day(self, name):
        """
        Add Anzac Day (April 25th)

        Anzac Day is a national day of remembrance in Australia and New Zealand
        that broadly commemorates all Australians and New Zealanders "who
        served and died in all wars, conflicts, and peacekeeping operations"
        and "the contribution and suffering of all those who have served".

        Anzac Day is a public holiday in Australia, New Zealand, and Tonga; it
        used to be a public holiday in Samoa up until 2008.
        https://en.wikipedia.org/wiki/Anzac_Day
        """
        return self._add_holiday_apr_25(name)

    def _add_childrens_day(self, name, variation="JUN"):
        """
        Add International Children's Day (June 1).

        In 1925, International Children's Day was first proclaimed in Geneva
        during the World Conference on Child Welfare. Since 1950, it is
        celebrated on June 1 in many countries.

        As such, this entry currently defaults to June 1, though this also
        supports another internationally adopted variant, November 20th.
        https://en.wikipedia.org/wiki/Children's_Day
        """
        if variation == "JUN":
            return self._add_holiday_jun_1(name)
        elif variation == "NOV":
            return self._add_holiday_nov_20(name)
        else:
            raise ValueError(
                f"Unknown variation name: {variation}. "
                "This entry currently supports `JUN` and `NOV` variation only."
            )

    def _add_columbus_day(self, name):
        """
        Add Columbus Day (October 12th)

        Columbus Day is a national holiday which officially celebrates the
        anniversary of Christopher Columbus's arrival in the Americas.
        https://en.wikipedia.org/wiki/Columbus_Day
        """
        return self._add_holiday_oct_12(name)

    def _add_labor_day(self, name):
        """
        Add International Workers' Day (May 1st)

        International Workers' Day, also known as Labour Day, is a celebration
        of labourers and the working classes that is promoted by the
        international labour movement.
        https://en.wikipedia.org/wiki/International_Workers%27_Day
        """
        return self._add_holiday_may_1(name)

    def _add_labor_day_two(self, name):
        """
        Add International Workers' Day Two (May 2nd)

        https://en.wikipedia.org/wiki/International_Workers%27_Day
        """
        return self._add_holiday_may_2(name)

    def _add_labor_day_three(self, name):
        """
        Add International Workers' Day Three (May 3rd)

        https://en.wikipedia.org/wiki/International_Workers%27_Day
        """
        return self._add_holiday_may_3(name)

    def _add_new_years_day(self, name) -> date:
        """
        Add New Year's Day (January 1st).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday_jan_1(name)

    def _add_new_years_day_two(self, name) -> date:
        """
        Add New Year's Day Two (January 2nd).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday_jan_2(name)

    def _add_new_years_day_three(self, name) -> date:
        """
        Add New Year's Day Three (January 3rd).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday_jan_3(name)

    def _add_new_years_day_four(self, name) -> date:
        """
        Add New Year's Day Four (January 4th).

        New Year's Day is a festival observed in most of the world on
        1 January, the first day of the year in the modern Gregorian calendar.
        https://en.wikipedia.org/wiki/New_Year%27s_Day
        """
        return self._add_holiday_jan_4(name)

    def _add_remembrance_day(self, name):
        """
        Add Remembrance Day / Armistice Day (Nov 11th)

        It's a memorial day since the end of the First World War in 1919
        to honour armed forces members who have died in the line of duty.
        https://en.wikipedia.org/wiki/Remembrance_Day
        """
        return self._add_holiday_nov_11(name)

    def _add_new_years_eve(self, name) -> date:
        """
        Add New Year's Eve (December 31st).

        In the Gregorian calendar, New Year's Eve, also known as Old Year's
        Day or Saint Sylvester's Day in many countries, is the evening or the
        entire day of the last day of the year, on 31 December.
        https://en.wikipedia.org/wiki/New_Year%27s_Eve
        """
        return self._add_holiday_dec_31(name)

    def _add_womens_day(self, name):
        """
        Add International Women's Day (March 8th).

        International Women's Day is a global holiday celebrated as a focal
        point in the women's rights movement, bringing attention to issues
        such as gender equality, reproductive rights, and violence and abuse
        against women.
        https://en.wikipedia.org/wiki/International_Women%27s_Day
        """
        return self._add_holiday_mar_8(name)

    def _add_world_war_two_victory_day(self, name):
        """
        Add Victory Day (May 9th)

        Victory Day is a holiday that commemorates the victory over Nazi
        Germany in 1945.
        https://en.wikipedia.org/wiki/Victory_Day_(9_May)
        """
        return self._add_holiday_may_9(name)

    def _add_united_nations_day(self, name):
        """
        Add United Nations Day (Oct 24th)

        United Nations Day is an annual commemorative day, reflecting the
        official creation of the United Nations on 24 October 1945.
        https://en.wikipedia.org/wiki/United_Nations_Day
        """
        return self._add_holiday_oct_24(name)
