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

from datetime import date

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    WORKDAY_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class Azerbaijan(ObservedHolidayBase, InternationalHolidays, IslamicHolidays):
    # [1] https://en.wikipedia.org/wiki/Public_holidays_in_Azerbaijan
    # [2] https://az.wikipedia.org/wiki/Az%C9%99rbaycan%C4%B1n_d%C3%B6vl%C9%99t_bayramlar%C4%B1_v%C9%99_x%C3%BCsusi_g%C3%BCnl%C9%99ri  # noqa: E501
    # [3] https://www.sosial.gov.az/en/prod-calendar

    country = "AZ"
    observed_label = "%s (Observed)"

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=AzerbaijanIslamicHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        kwargs.setdefault("observed_since", 2006)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        if year <= 1989:
            return None

        super()._populate(year)
        dts_observed = set()
        dts_non_observed = set()
        dts_bairami = set()

        # New Year
        name = "New Year's Day"
        dts_observed.add(self._add_new_years_day(name))
        if year >= 2006:
            dts_observed.add(self._add_new_years_day_two(name))

        # Black January (without extending)
        if year >= 2000:
            dts_non_observed.add(self._add_holiday_jan_20("Black January"))

        # International Women's Day
        dts_observed.add(self._add_womens_day("International Women's Day"))

        # Novruz
        if year >= 2007:
            for day in range(20, 25):
                dts_observed.add(self._add_holiday("Novruz", MAR, day))

        # Victory Day
        dts_observed.add(self._add_world_war_two_victory_day("Victory Day over Fascism"))

        # Republic Day
        if year >= 1992:
            dts_observed.add(
                self._add_holiday_may_28("Independence Day" if year >= 2021 else "Republic Day")
            )

        # National Salvation Day
        if year >= 1997:
            dts_observed.add(self._add_holiday_jun_15("National Salvation Day"))

        # Memorial Day (without extending)
        if year >= 2021:
            dts_non_observed.add(self._add_holiday_sep_27("Memorial Day"))

        # Azerbaijan Armed Forces Day
        if year >= 1992:
            name = "Azerbaijan Armed Forces Day"
            if year <= 1997:
                self._add_holiday_oct_9(name)
            else:
                dts_observed.add(self._add_holiday_jun_26(name))

        # Independence Day
        if year <= 2005:
            self._add_holiday_oct_18("Independence Day")

        # Victory Day
        if year >= 2021:
            dts_observed.add(self._add_holiday_nov_8("Victory Day"))

        # Flag Day
        if year >= 2010:
            dts_observed.add(self._add_holiday_nov_9("Flag Day"))

        # International Solidarity Day of Azerbaijanis
        if year >= 1993:
            solidarity_name = "International Solidarity Day of Azerbaijanis"
            self._add_new_years_eve(solidarity_name)
            self._add_observed(date(year - 1, DEC, 31), name=solidarity_name)

        if year >= 1993:
            name = "Ramazan Bayrami"
            dts_bairami.update(self._add_eid_al_fitr_day(name))
            dts_bairami.update(self._add_eid_al_fitr_day_two(name))

            name = "Gurban Bayrami"
            dts_bairami.update(self._add_eid_al_adha_day(name))
            dts_bairami.update(self._add_eid_al_adha_day_two(name))

        # Article 105 of the Labor Code of the Republic of Azerbaijan states:
        # 5. If interweekly rest days and holidays that are not considered
        # working days overlap, that rest day is immediately transferred to
        # the next working day.
        if self.observed and year >= 2006:
            # observed holidays special cases
            special_dates_obs = {2007: (JAN, 3), 2072: (JAN, 5)}
            if year in special_dates_obs:
                self._add_holiday(
                    "Gurban Bayrami* (*estimated) (Observed)", special_dates_obs[year]
                )

            self._populate_observed(dts_observed.union(dts_bairami))

            for dt_observed in sorted(dts_bairami.difference(dts_non_observed)):
                # 6. If the holidays of Qurban and Ramadan coincide with
                # another holiday that is not considered a working day,
                # the next working day is considered a rest day.
                if len(self.get_list(dt_observed)) == 1:
                    continue
                for name in self.get_list(dt_observed):
                    if "Bayrami" in name:
                        self._add_observed(
                            dt_observed,
                            name=name,
                            rule=WORKDAY_TO_NEXT_WORKDAY,
                        )


class AZ(Azerbaijan):
    pass


class AZE(Azerbaijan):
    pass


class AzerbaijanIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2011: (NOV, 6),
        2012: (OCT, 25),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
    }

    EID_AL_FITR_DATES = {
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
    }
