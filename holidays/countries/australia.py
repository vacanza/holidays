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
from datetime import timedelta as td

from holidays.calendars.gregorian import APR, AUG, SEP, OCT, FRI, _get_nth_weekday_from
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Australia(HolidayBase, ChristianHolidays, InternationalHolidays):
    """
    References:
      - https://www.qld.gov.au/recreation/travel/holidays
    """

    country = "AU"
    special_holidays = {
        2022: (SEP, 22, "National Day of Mourning for Queen Elizabeth II"),
    }
    subdivisions = ("ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA")

    @property
    def sovereign_birthday(self) -> str:
        """Sovereign's birthday holiday name."""
        return (
            "King's Birthday"
            if 1902 <= self._year <= 1951 or self._year >= 2023
            else "Queen's Birthday"
        )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _add_observed(self, dt: date, include_sat: bool = True, days: int = +1) -> None:
        if not self.observed:
            return None
        if self._is_sunday(dt) or (include_sat and self._is_saturday(dt)):
            self._add_holiday(
                "%s (Observed)" % self[dt], dt + td(days=+2 if self._is_saturday(dt) else days)
            )

    def _populate(self, year):
        super()._populate(year)

        # ACT:  Holidays Act 1958
        # NSW:  Public Holidays Act 2010
        # NT:   Public Holidays Act 2013
        # QLD:  Holidays Act 1983
        # SA:   Holidays Act 1910
        # TAS:  Statutory Holidays Act 2000
        # VIC:  Public Holidays Act 1993
        # WA:   Public and Bank Holidays Act 1972

        # TODO do more research on history of Aus holidays

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"))

        # Easter
        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")

        # Sovereign's Birthday
        if 1902 <= year <= 1935:
            if self._year >= 1912:
                self._add_holiday_jun_3(self.sovereign_birthday)  # George V
            else:
                self._add_holiday_nov_9(self.sovereign_birthday)  # Edward VII

    def _add_subdiv_holidays(self):
        # Australia Day
        if self._year >= 1935:
            name = (
                "Anniversary Day"
                if self.subdiv == "NSW" and self._year <= 1945
                else "Australia Day"
            )
            jan_26 = self._add_holiday_jan_26(name)
            if self._year >= 1946:
                self._add_observed(jan_26)
        elif self._year >= 1888 and self.subdiv != "SA":
            self._add_holiday_jan_26("Anniversary Day")

        # Anzac Day
        if self._year >= 1921:
            self._add_holiday_apr_25("Anzac Day")

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"), days=+2)

        # Boxing Day
        name = "Proclamation Day" if self.subdiv == "SA" else "Boxing Day"
        self._add_observed(self._add_christmas_day_two(name), days=+2)

        super()._add_subdiv_holidays()

    def _add_subdiv_act_holidays(self):
        # Easter
        self._add_holy_saturday("Easter Saturday")
        self._add_easter_sunday("Easter Sunday")

        # Labour Day
        self._add_holiday_1st_mon_of_oct("Labour Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Anzac Day
        if self._year >= 1921:
            self._add_observed(date(self._year, APR, 25), include_sat=False)

        # Canberra Day
        # Info from https://www.timeanddate.com/holidays/australia/canberra-day
        # and https://en.wikipedia.org/wiki/Canberra_Day
        if self._year >= 1913:
            name = "Canberra Day"
            if self._year <= 1957 or self._year == 2012:
                self._add_holiday_mar_12(name)
            elif self._year <= 2007:
                self._add_holiday_3rd_mon_of_mar(name)
            else:
                self._add_holiday_2nd_mon_of_mar(name)

        # Family & Community Day
        if 2007 <= self._year <= 2017:
            # first Monday of the September/October school holidays
            # moved to the second Monday if this falls on Labour day
            # TODO need a formula for the ACT school holidays then
            # http://www.cmd.act.gov.au/communication/holidays
            fc_dates = {
                2010: date(2010, SEP, 26),
                2011: date(2011, OCT, 10),
                2012: date(2012, OCT, 8),
                2013: date(2013, SEP, 30),
                2014: date(2014, SEP, 29),
                2015: date(2015, SEP, 28),
                2016: date(2016, SEP, 26),
                2017: date(2017, SEP, 25),
            }
            name = "Family & Community Day"
            if self._year in fc_dates:
                self._add_holiday(name, fc_dates[self._year])
            else:
                self._add_holiday_1st_tue_of_nov(name)

        # Reconciliation Day
        if self._year >= 2018:
            self._add_holiday_1st_mon_from_may_27("Reconciliation Day")

    def _add_subdiv_nsw_holidays(self):
        # Easter
        self._add_holy_saturday("Easter Saturday")
        self._add_easter_sunday("Easter Sunday")

        # Labour Day
        self._add_holiday_1st_mon_of_oct("Labour Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Bank Holiday
        if self._year >= 1912:
            self._add_holiday_1st_mon_of_aug("Bank Holiday")

    def _add_subdiv_nt_holidays(self):
        # Easter
        self._add_holy_saturday("Easter Saturday")

        # Labour Day
        self._add_holiday_1st_mon_of_may("May Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Anzac Day
        if self._year >= 1921:
            self._add_observed(date(self._year, APR, 25))

        # Picnic Day
        self._add_holiday_1st_mon_of_aug("Picnic Day")

    def _add_subdiv_qld_holidays(self):
        # Easter
        self._add_holy_saturday("Easter Saturday")
        self._add_easter_sunday("Easter Sunday")

        # Labour Day
        name = "Labour Day"
        if 2013 <= self._year <= 2015:
            self._add_holiday_1st_mon_of_oct(name)
        else:
            self._add_holiday_1st_mon_of_may(name)

        # Sovereign's Birthday
        if self._year >= 1936:
            if self._year <= 2015 and self._year != 2012:
                self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)
            else:
                self._add_holiday_1st_mon_of_oct(self.sovereign_birthday)
        if self._year == 2012:
            self._add_holiday_jun_11("Queen's Diamond Jubilee")

        # Anzac Day
        if self._year >= 1921:
            self._add_observed(date(self._year, APR, 25), include_sat=False)

        # The Royal Queensland Show (Ekka)
        # The Show starts on the first Friday of August - providing this is
        # not prior to the 5th - in which case it will begin on the second
        # Friday. The Wednesday during the show is a public holiday.
        ekka_dates = {
            2020: date(2020, AUG, 14),
            2021: date(2021, OCT, 29),
        }
        name = "The Royal Queensland Show"
        if self._year in ekka_dates:
            self._add_holiday(name, ekka_dates[self._year])
        else:
            self._add_holiday(
                name, _get_nth_weekday_from(+1, FRI, date(self._year, AUG, 5)) + td(days=+5)
            )

    def _add_subdiv_sa_holidays(self):
        # Easter
        self._add_holy_saturday("Easter Saturday")

        # Labour Day
        self._add_holiday_1st_mon_of_oct("Labour Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Anzac Day
        if self._year >= 1921:
            self._add_observed(date(self._year, APR, 25), include_sat=False)

        # Adelaide Cup
        name = "Adelaide Cup"
        if self._year >= 2006:
            self._add_holiday_2nd_mon_of_mar(name)
        else:
            self._add_holiday_3rd_mon_of_mar(name)

    def _add_subdiv_tas_holidays(self):
        # Labour Day
        self._add_holiday_2nd_mon_of_mar("Eight Hours Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

    def _add_subdiv_vic_holidays(self):
        # Easter
        self._add_holy_saturday("Easter Saturday")
        self._add_easter_sunday("Easter Sunday")

        # Labour Day
        self._add_holiday_2nd_mon_of_mar("Labour Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Melbourne Cup
        self._add_holiday_1st_tue_of_nov("Melbourne Cup")

        if self._year >= 2015:
            # Grand Final Day
            grand_final_dates = {
                # Rescheduled due to COVID-19
                2020: date(2020, OCT, 23),
                # Rescheduled due to COVID-19
                2021: date(2021, SEP, 24),
                2022: date(2022, SEP, 23),
            }
            name = "Grand Final Day"
            if self._year in grand_final_dates:
                self._add_holiday(name, grand_final_dates[self._year])
            else:
                self._add_holiday_1st_fri_from_sep_24(name)

    def _add_subdiv_wa_holidays(self):
        # Labour Day
        self._add_holiday_1st_mon_of_mar("Labour Day")

        # Sovereign's Birthday
        if self._year >= 1936:
            self._add_holiday_1st_mon_before_oct_1(self.sovereign_birthday)

        # Anzac Day
        if self._year >= 1921:
            self._add_observed(date(self._year, APR, 25))

        # Western Australia Day
        if self._year >= 1833:
            name = "Western Australia Day" if self._year >= 2015 else "Foundation Day"
            self._add_holiday_1st_mon_of_jun(name)


class AU(Australia):
    pass


class AUS(Australia):
    pass
