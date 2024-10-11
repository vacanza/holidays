#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from typing import Union

from holidays.calendars.gregorian import MON, TUE, WED, THU, FRI, SAT, SUN
from holidays.constants import PUBLIC, UNOFFICIAL
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ObservedRule,
    MON_TO_NEXT_TUE,
    FRI_TO_PREV_THU,
    SAT_TO_PREV_FRI,
    SUN_TO_NEXT_MON,
    SAT_SUN_TO_PREV_FRI,
    SAT_SUN_TO_NEXT_MON,
)

GA_IN_WASHINGTON_BIRTHDAY = ObservedRule(
    {MON: +1, TUE: -1, WED: -1, THU: +1, FRI: -1, SAT: -2, SUN: -2}
)


class UnitedStates(ObservedHolidayBase, ChristianHolidays, InternationalHolidays):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States

    For Northern Mariana Islands (subdivision MP):
    - https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/
    - https://webcache.googleusercontent.com/search?q=cache:C17_7FBgPtQJ:https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/&hl=en&gl=sg&strip=1&vwsrc=0

    Columbus Day / Indigenous Peoples' Day history:
    - https://www.pewresearch.org/short-reads/2023/10/05/working-on-columbus-day-or-indigenous-peoples-day-it-depends-on-where-your-job-is/
    - https://www.officeholidays.com/holidays/usa/columbus-day-state-guide
    - https://en.wikipedia.org/wiki/Indigenous_Peoples%27_Day_(United_States)
    - https://www.sos.ri.gov/divisions/civics-and-education/reference-desk/ri-state-holidays
    - https://web.archive.org/web/20080831103521/http://www.dpa.ca.gov/personnel-policies/holidays.htm

    Frances Xavier Cabrini Day:
        - https://leg.colorado.gov/sites/default/files/2020a_1031_signed.pdf

    Washington's Birthday (GA):
        - https://www.gasupreme.us/court-information/holidays-2/

    Washington's Birthday (IN):
        - https://www.in.gov/spd/benefits/state-holidays/

    American Samoa holidays:
        - https://asbar.org/code-annotated/1-0501-public-holidays/
    """

    country = "US"
    supported_categories = (PUBLIC, UNOFFICIAL)
    observed_label = "%s (observed)"
    subdivisions: Union[tuple[()], tuple[str, ...]] = (
        "AK",  # Alaska.
        "AL",  # Alabama.
        "AR",  # Arkansas.
        "AS",  # American Samoa.
        "AZ",  # Arizona.
        "CA",  # California.
        "CO",  # Colorado.
        "CT",  # Connecticut.
        "DC",  # District of Columbia.
        "DE",  # Delaware.
        "FL",  # Florida.
        "GA",  # Georgia.
        "GU",  # Guam.
        "HI",  # Hawaii.
        "IA",  # Iowa.
        "ID",  # Idaho.
        "IL",  # Illinois.
        "IN",  # Indiana.
        "KS",  # Kansas.
        "KY",  # Kentucky.
        "LA",  # Louisiana.
        "MA",  # Massachusetts.
        "MD",  # Maryland.
        "ME",  # Maine.
        "MI",  # Michigan.
        "MN",  # Minnesota.
        "MO",  # Missouri.
        "MP",  # Northern Mariana Islands.
        "MS",  # Mississippi.
        "MT",  # Montana.
        "NC",  # North Carolina.
        "ND",  # North Dakota.
        "NE",  # Nebraska.
        "NH",  # New Hampshire.
        "NJ",  # New Jersey.
        "NM",  # New Mexico.
        "NV",  # Nevada.
        "NY",  # New York.
        "OH",  # Ohio.
        "OK",  # Oklahoma.
        "OR",  # Oregon.
        "PA",  # Pennsylvania.
        "PR",  # Puerto Rico.
        "RI",  # Rhode Island.
        "SC",  # South Carolina.
        "SD",  # South Dakota.
        "TN",  # Tennessee.
        "TX",  # Texas.
        "UM",  # United States Minor Outlying Islands.
        "UT",  # Utah.
        "VA",  # Virginia.
        "VI",  # Virgin Islands, U.S..
        "VT",  # Vermont.
        "WA",  # Washington.
        "WI",  # Wisconsin.
        "WV",  # West Virginia.
        "WY",  # Wyoming.
    )

    _deprecated_subdivisions = (
        "FM",
        "MH",
        "PW",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day
        if self._year >= 1871:
            name = "New Year's Day"
            self._add_observed(self._add_new_years_day(name))
            self._add_observed(self._next_year_new_years_day, name=name)

        # Memorial Day
        if self._year >= 1888:
            name = "Memorial Day"
            if self._year >= 1971:
                self._add_holiday_last_mon_of_may(name)
            else:
                self._add_holiday_may_30(name)

        # Juneteenth Day
        if self._year >= 2021:
            self._add_observed(self._add_holiday_jun_19("Juneteenth National Independence Day"))

        # Independence Day
        if self._year >= 1871:
            self._add_observed(self._add_holiday_jul_4("Independence Day"))

        # Labor Day
        if self._year >= 1894:
            self._add_holiday_1st_mon_of_sep("Labor Day")

        # Veterans Day
        if self._year >= 1938:
            name = "Veterans Day" if self._year >= 1954 else "Armistice Day"
            if 1971 <= self._year <= 1977:
                self._add_holiday_4th_mon_of_oct(name)
            else:
                self._add_observed(self._add_remembrance_day(name))

        # Thanksgiving
        if self._year >= 1871:
            self._add_holiday_4th_thu_of_nov("Thanksgiving")

        # Christmas Day
        if self._year >= 1871:
            self._add_observed(self._add_christmas_day("Christmas Day"))

    def _add_christmas_eve_holiday(self):
        # Christmas Eve
        # If on Friday, observed on Thursday
        # If on Saturday or Sunday, observed on Friday
        name = "Christmas Eve"
        self._add_observed(
            self._add_christmas_eve(name), name=name, rule=FRI_TO_PREV_THU + SAT_SUN_TO_PREV_FRI
        )

    def _populate_subdiv_holidays(self):
        if PUBLIC not in self.categories:
            return None

        # Martin Luther King Jr. Day
        if self._year >= 1986 and self.subdiv not in {"AL", "AR", "AZ", "GA", "ID", "MS", "NH"}:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King Jr. Day")

        # Washington's Birthday
        if self._year >= 1879 and self.subdiv not in {
            "AL",
            "AR",
            "DE",
            "FL",
            "GA",
            "IN",
            "NM",
            "PR",
            "VI",
        }:
            name = "Washington's Birthday"
            if self._year >= 1971:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_feb_22(name)

        # Columbus Day
        if self._year >= 1937 and (
            self.subdiv is None
            or self.subdiv
            in {
                "AS",
                "AZ",
                "CT",
                "GA",
                "ID",
                "IL",
                "IN",
                "MA",
                "MD",
                "MO",
                "MT",
                "NJ",
                "NY",
                "OH",
                "PA",
                "UT",
                "WV",
            }
        ):
            name = "Columbus Day"
            if self._year >= 1971:
                self._add_holiday_2nd_mon_of_oct(name)
            else:
                self._add_columbus_day(name)

        super()._populate_subdiv_holidays()

    def _populate_subdiv_ak_public_holidays(self):
        # Seward's Day
        if self._year >= 1918:
            name = "Seward's Day"
            if self._year >= 1955:
                self._add_holiday_last_mon_of_mar(name)
            else:
                self._add_holiday_mar_30(name)

        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day" if self._year >= 2015 else "Columbus Day"
            )

        # Alaska Day
        if self._year >= 1867:
            self._add_observed(self._add_holiday_oct_18("Alaska Day"))

    def _populate_subdiv_al_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan("Martin Luther King, Jr & Robert E. Lee's Birthday")

        # Washington's Birthday
        name = "George Washington & Thomas Jefferson's Birthday"
        if self._year >= 1971:
            self._add_holiday_3rd_mon_of_feb(name)
        else:
            self._add_holiday_feb_22(name)

        # Confederate Memorial Day
        if self._year >= 1866:
            self._add_holiday_4th_mon_of_apr("Confederate Memorial Day")

        # Jefferson Davis Birthday
        if self._year >= 1890:
            self._add_holiday_1st_mon_of_jun("Jefferson Davis Birthday")

        # Columbus Day / American Indian Heritage Day / Fraternal Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Columbus Day / American Indian Heritage Day / Fraternal Day"
                if self._year >= 2000
                else "Columbus Day / Fraternal Day"
            )

    def _populate_subdiv_ar_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            name = (
                "Martin Luther King Jr. Day"
                if self._year >= 2018
                else "Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays"
            )
            self._add_holiday_3rd_mon_of_jan(name)

        # Washington's Birthday
        name = "George Washington's Birthday and Daisy Gatson Bates Day"
        if self._year >= 1971:
            self._add_holiday_3rd_mon_of_feb(name)
        else:
            self._add_holiday_feb_22(name)

    def _populate_subdiv_as_public_holidays(self):
        # American Samoa Flag Day
        if self._year >= 1901:
            self._add_observed(self._add_holiday_apr_17("American Samoa Flag Day"))

        # Manu'a Islands Cession Day
        if self._year >= 1983:
            self._add_observed(self._add_holiday_jul_16("Manu'a Islands Cession Day"))

        # White Sunday
        self._add_holiday_2nd_sun_of_oct("White Sunday")

    def _populate_subdiv_az_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan("Dr. Martin Luther King Jr. / Civil Rights Day")

    def _populate_subdiv_ca_public_holidays(self):
        # Lincoln's Birthday
        if 1971 <= self._year <= 2009:
            self._add_observed(self._add_holiday_feb_12("Lincoln's Birthday"))

        # Susan B. Anthony Day
        if self._year >= 2014:
            self._add_holiday_feb_15("Susan B. Anthony Day")

        # Cesar Chavez Day
        if self._year >= 1995:
            self._add_observed(self._add_holiday_mar_31("Cesar Chavez Day"), rule=SUN_TO_NEXT_MON)

        # Columbus Day
        if 1971 <= self._year <= 2008:
            self._add_holiday_2nd_mon_of_oct("Columbus Day")

        # Day After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

    def _populate_subdiv_co_public_holidays(self):
        # Cesar Chavez Day
        if self._year >= 2001:
            self._add_holiday_mar_31("Cesar Chavez Day")

        # Frances Xavier Cabrini Day
        if self._year >= 2020:
            self._add_holiday_1st_mon_of_oct("Frances Xavier Cabrini Day")

    def _populate_subdiv_ct_public_holidays(self):
        # Lincoln's Birthday
        if self._year >= 1971:
            self._add_observed(self._add_holiday_feb_12("Lincoln's Birthday"))

        # Good Friday
        self._add_good_friday("Good Friday")

    def _populate_subdiv_dc_public_holidays(self):
        # Inauguration Day
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            name = "Inauguration Day"
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )

        # Emancipation Day
        if self._year >= 2005:
            self._add_observed(self._add_holiday_apr_16("Emancipation Day"))

        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day" if self._year >= 2019 else "Columbus Day"
            )

    def _populate_subdiv_de_public_holidays(self):
        # Good Friday
        self._add_good_friday("Good Friday")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

        # Day After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

    def _populate_subdiv_fl_public_holidays(self):
        # Susan B. Anthony Day
        if self._year >= 2011:
            self._add_holiday_feb_15("Susan B. Anthony Day")

        # Friday After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Friday After Thanksgiving")

    def _populate_subdiv_ga_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                "Martin Luther King Jr. Day" if self._year >= 2012 else "Robert E. Lee's Birthday"
            )

        # Confederate Memorial Day
        if self._year >= 1866:
            name = "State Holiday" if self._year >= 2016 else "Confederate Memorial Day"
            if self._year == 2020:
                self._add_holiday_apr_10(name)
            else:
                self._add_holiday_4th_mon_of_apr(name)

        # Robert E. Lee's Birthday
        if self._year >= 1986:
            self._add_holiday_1_day_past_4th_thu_of_nov(
                "State Holiday" if self._year >= 2016 else "Robert E. Lee's Birthday"
            )

        # Washington's Birthday
        self._add_holiday(
            "Washington's Birthday",
            self._get_observed_date(self._christmas_day, rule=GA_IN_WASHINGTON_BIRTHDAY),
        )

    def _populate_subdiv_gu_public_holidays(self):
        # Guam Discovery Day
        if self._year >= 1970:
            self._add_holiday_1st_mon_of_mar("Guam Discovery Day")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Liberation Day (Guam)
        if self._year >= 1945:
            self._add_holiday_jul_21("Liberation Day (Guam)")

        # All Souls' Day
        self._add_all_souls_day("All Souls' Day")

        # Lady of Camarin Day
        self._add_immaculate_conception_day("Lady of Camarin Day")

    def _populate_subdiv_hi_public_holidays(self):
        # Prince Jonah Kuhio Kalanianaole Day
        if self._year >= 1949:
            self._add_observed(self._add_holiday_mar_26("Prince Jonah Kuhio Kalanianaole Day"))

        # Kamehameha Day
        if self._year >= 1872:
            jun_11 = self._add_holiday_jun_11("Kamehameha Day")
            if self._year >= 2011:
                self._add_observed(jun_11)

        # Statehood Day
        if self._year >= 1959:
            self._add_holiday_3rd_fri_of_aug("Statehood Day")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

    def _populate_subdiv_ia_public_holidays(self):
        # Lincoln's Birthday
        if self._year >= 1971:
            self._add_observed(self._add_holiday_feb_12("Lincoln's Birthday"))

    def _populate_subdiv_id_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                "Martin Luther King Jr. / Idaho Human Rights Day"
                if self._year >= 2006
                else "Martin Luther King Jr. Day",
            )

    def _populate_subdiv_il_public_holidays(self):
        # Lincoln's Birthday
        if self._year >= 1971:
            self._add_observed(self._add_holiday_feb_12("Lincoln's Birthday"))

        # Casimir Pulaski Day
        if self._year >= 1978:
            self._add_holiday_1st_mon_of_mar("Casimir Pulaski Day")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

    def _populate_subdiv_in_public_holidays(self):
        # Good Friday
        self._add_good_friday("Good Friday")

        # Primary Election Day
        if self._year >= 2015 or (self._year >= 2006 and self._year % 2 == 0):
            self._add_holiday_1_day_past_1st_mon_of_may("Primary Election Day")

        # Election Day
        if self._year >= 2015 or (self._year >= 2008 and self._year % 2 == 0):
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

        # Lincoln's Birthday
        if self._year >= 2010:
            self._add_holiday_1_day_past_4th_thu_of_nov("Lincoln's Birthday")

        # Washington's Birthday
        self._add_holiday(
            "Washington's Birthday",
            self._get_observed_date(self._christmas_day, rule=GA_IN_WASHINGTON_BIRTHDAY),
        )

    def _populate_subdiv_ks_public_holidays(self):
        # Christmas Eve
        if self._year >= 2013:
            self._add_christmas_eve_holiday()

    def _populate_subdiv_ky_public_holidays(self):
        # Good Friday
        self._add_good_friday("Good Friday")

        # New Year's Eve
        if self._year >= 2013:
            self._add_observed(self._add_new_years_eve("New Year's Eve"))

    def _populate_subdiv_la_public_holidays(self):
        # Inauguration Day
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            name = "Inauguration Day"
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )

        # Mardi Gras
        if self._year >= 1857:
            self._add_carnival_tuesday("Mardi Gras")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

    def _populate_subdiv_ma_public_holidays(self):
        # Evacuation Day
        if self._year >= 1901:
            self._add_observed(
                self._add_holiday_mar_17("Evacuation Day"), rule=SAT_SUN_TO_NEXT_MON
            )

        # Patriots' Day
        if self._year >= 1894:
            name = "Patriots' Day"
            if self._year >= 1969:
                self._add_holiday_3rd_mon_of_apr(name)
            else:
                self._add_holiday_apr_19(name)

    def _populate_subdiv_md_public_holidays(self):
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            # Inauguration Day
            name = "Inauguration Day"
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )

        # American Indian Heritage Day
        if self._year >= 2008:
            self._add_holiday_1_day_past_4th_thu_of_nov("American Indian Heritage Day")

    def _populate_subdiv_me_public_holidays(self):
        # Patriots' Day
        if self._year >= 1894:
            name = "Patriots' Day"
            if self._year >= 1969:
                self._add_holiday_3rd_mon_of_apr("Patriots' Day")
            else:
                self._add_holiday_apr_19(name)

        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day" if self._year >= 2019 else "Columbus Day"
            )

    def _populate_subdiv_mi_public_holidays(self):
        if self._year >= 2013:
            # Christmas Eve
            self._add_christmas_eve_holiday()

            # New Year's Eve
            self._add_observed(self._add_new_years_eve("New Year's Eve"))

    def _populate_subdiv_mn_public_holidays(self):
        pass

    def _populate_subdiv_mo_public_holidays(self):
        # Truman Day
        if self._year >= 1949:
            self._add_observed(self._add_holiday_may_8("Truman Day"))

    def _populate_subdiv_mp_public_holidays(self):
        # Commonwealth Covenant Day in Northern Mariana Islands
        self._add_observed(self._add_holiday_mar_24("Commonwealth Covenant Day"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Commonwealth Cultural Day in Northern Mariana Islands
        self._add_holiday_2nd_mon_of_oct("Commonwealth Cultural Day")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

        # Citizenship Day in Northern Mariana Islands
        self._add_observed(self._add_holiday_nov_4("Citizenship Day"))

        # Constitution Day in Northern Mariana Islands
        self._add_observed(self._add_holiday_dec_8("Constitution Day"))

    def _populate_subdiv_ms_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                "Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays",
            )

        # Confederate Memorial Day
        if self._year >= 1866:
            self._add_holiday_last_mon_of_apr("Confederate Memorial Day")

    def _populate_subdiv_mt_public_holidays(self):
        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

    def _populate_subdiv_nc_public_holidays(self):
        # Good Friday
        self._add_good_friday("Good Friday")

        # Day After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

        # Christmas Eve
        if self._year >= 2013:
            self._add_christmas_eve_holiday()

        # Day After Christmas
        if self._year >= 2013:
            # If on Saturday or Sunday, observed on Monday
            # If on Monday, observed on Tuesday
            name = "Day After Christmas"
            self._add_observed(
                self._add_christmas_day_two(name),
                name=name,
                rule=MON_TO_NEXT_TUE + SAT_SUN_TO_NEXT_MON,
            )

    def _populate_subdiv_nd_public_holidays(self):
        pass

    def _populate_subdiv_ne_public_holidays(self):
        # Arbor Day
        if self._year >= 1875:
            name = "Arbor Day"
            if self._year >= 1989:
                self._add_holiday_last_fri_of_apr(name)
            else:
                self._add_holiday_apr_22(name)

        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day" if self._year >= 2020 else "Columbus Day"
            )

    def _populate_subdiv_nh_public_holidays(self):
        # Martin Luther King Jr. Day
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan("Dr. Martin Luther King Jr. / Civil Rights Day")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

        # Day After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

    def _populate_subdiv_nj_public_holidays(self):
        # Lincoln's Birthday
        if self._year >= 1971:
            self._add_observed(self._add_holiday_feb_12("Lincoln's Birthday"))

        # Good Friday
        self._add_good_friday("Good Friday")

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

    def _populate_subdiv_nm_public_holidays(self):
        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day" if self._year >= 2019 else "Columbus Day"
            )

        # Presidents' Day
        self._add_holiday_1_day_past_4th_thu_of_nov("Presidents' Day")

    def _populate_subdiv_nv_public_holidays(self):
        # Nevada Day
        if self._year >= 1933:
            name = "Nevada Day"
            self._add_observed(
                self._add_holiday_last_fri_of_oct(name)
                if self._year >= 2000
                else self._add_holiday_oct_31(name)
            )

        # Family Day
        self._add_holiday_1_day_past_4th_thu_of_nov("Family Day")

    def _populate_subdiv_ny_public_holidays(self):
        # Lincoln's Birthday
        if self._year >= 1971:
            self._add_observed(self._add_holiday_feb_12("Lincoln's Birthday"))

        # Susan B. Anthony Day
        if self._year >= 2004:
            self._add_holiday_feb_15("Susan B. Anthony Day")

        # Election Day
        if self._year >= 2015 or (self._year >= 2008 and self._year % 2 == 0):
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

    def _populate_subdiv_oh_public_holidays(self):
        pass

    def _populate_subdiv_ok_public_holidays(self):
        # Day After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

    def _populate_subdiv_or_public_holidays(self):
        pass

    def _populate_subdiv_pa_public_holidays(self):
        # Day After Thanksgiving
        self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

    def _populate_subdiv_pr_public_holidays(self):
        # Epiphany
        self._add_epiphany_day("Epiphany")

        # Washington's Birthday
        self._add_holiday_3rd_mon_of_feb("Presidents' Day")

        # Emancipation Day
        self._add_observed(self._add_holiday_mar_22("Emancipation Day"), rule=SUN_TO_NEXT_MON)

        # Good Friday
        self._add_good_friday("Good Friday")

        # Constitution Day
        self._add_observed(self._add_holiday_jul_25("Constitution Day"), rule=SUN_TO_NEXT_MON)

        # Discovery Day
        self._add_observed(self._add_holiday_nov_19("Discovery Day"), rule=SUN_TO_NEXT_MON)

    def _populate_subdiv_ri_public_holidays(self):
        # Victory Day
        if self._year >= 1948:
            self._add_holiday_2nd_mon_of_aug("Victory Day")

        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day / Columbus Day" if self._year >= 2022 else "Columbus Day"
            )

    def _populate_subdiv_sc_public_holidays(self):
        # Confederate Memorial Day
        if self._year >= 1866:
            self._add_holiday_4th_mon_of_apr("Confederate Memorial Day")

    def _populate_subdiv_sd_public_holidays(self):
        # Native Americans' Day / Columbus Day
        if self._year >= 1937:
            name = "Native Americans' Day" if self._year >= 1990 else "Columbus Day"
            if self._year >= 1970:
                self._add_holiday_2nd_mon_of_oct(name)
            else:
                self._add_columbus_day(name)

    def _populate_subdiv_tn_public_holidays(self):
        # Good Friday
        self._add_good_friday("Good Friday")

    def _populate_subdiv_tx_public_holidays(self):
        # Confederate Memorial Day
        if self._year >= 1931:
            self._add_holiday_jan_19("Confederate Memorial Day")

        # Texas Independence Day
        if self._year >= 1874:
            self._add_holiday_mar_2("Texas Independence Day")

        # Cesar Chavez Day
        if self._year >= 2000:
            self._add_holiday_mar_31("Cesar Chavez Day")

        # Good Friday
        self._add_good_friday("Good Friday")

        # San Jacinto Day
        if self._year >= 1875:
            self._add_holiday_apr_21("San Jacinto Day")

        # Emancipation Day In Texas
        if self._year >= 1980:
            self._add_holiday_jun_19("Emancipation Day In Texas")

        # Lyndon Baines Johnson Day
        if self._year >= 1973:
            self._add_holiday_aug_27("Lyndon Baines Johnson Day")

        # Friday After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Friday After Thanksgiving")

        # Christmas Eve
        if self._year >= 1981:
            self._add_christmas_eve_holiday()

        # Day After Christmas
        if self._year >= 1981:
            self._add_christmas_day_two("Day After Christmas")

    def _populate_subdiv_um_public_holidays(self):
        pass

    def _populate_subdiv_ut_public_holidays(self):
        # Pioneer Day
        if self._year >= 1849:
            self._add_observed(self._add_holiday_jul_24("Pioneer Day"))

    def _populate_subdiv_va_public_holidays(self):
        # Lee Jackson Day
        if 1889 <= self._year <= 2020:
            name = "Lee Jackson Day"
            if self._year >= 2000:
                self._add_holiday_3_days_prior_3rd_mon_of_jan(name)
            elif self._year >= 1983:
                self._add_holiday_3rd_mon_of_jan(name)
            else:
                self._add_holiday_jan_19(name)

        # Inauguration Day
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            name = "Inauguration Day"
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )
        # Indigenous Peoples' Day
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                "Indigenous Peoples' Day" if self._year >= 2020 else "Columbus Day"
            )

    def _populate_subdiv_vi_public_holidays(self):
        # Three Kings Day
        self._add_epiphany_day("Three Kings Day")

        # Washington's Birthday
        name = "Presidents' Day"
        if self._year >= 1971:
            self._add_holiday_3rd_mon_of_feb(name)
        else:
            self._add_holiday_feb_22(name)

        # Transfer Day
        self._add_holiday_mar_31("Transfer Day")

        # Holy Thursday
        self._add_holy_thursday("Holy Thursday")

        # Good Friday
        self._add_good_friday("Good Friday")

        # Easter Monday
        self._add_easter_monday("Easter Monday")

        # Emancipation Day in US Virgin Islands
        self._add_holiday_jul_3("Emancipation Day")

        # Columbus Day
        if self._year >= 1937:
            name = "Columbus Day and Puerto Rico Friendship Day"
            if self._year >= 1970:
                self._add_holiday_2nd_mon_of_oct(name)
            else:
                self._add_columbus_day(name)

        # Liberty Day
        self._add_holiday_nov_1("Liberty Day")

        # Christmas Second Day
        self._add_christmas_day_two("Christmas Second Day")

    def _populate_subdiv_vt_public_holidays(self):
        # Town Meeting Day
        if self._year >= 1800:
            self._add_holiday_1st_tue_of_mar("Town Meeting Day")

        # Bennington Battle Day
        if self._year >= 1778:
            self._add_observed(self._add_holiday_aug_16("Bennington Battle Day"))

    def _populate_subdiv_wa_public_holidays(self):
        pass

    def _populate_subdiv_wi_public_holidays(self):
        # Susan B. Anthony Day
        if self._year >= 1976:
            self._add_holiday_feb_15("Susan B. Anthony Day")

        if self._year >= 2012:
            # Christmas Eve
            self._add_christmas_eve_holiday()

            # New Year's Eve
            self._add_observed(self._add_new_years_eve("New Year's Eve"))

    def _populate_subdiv_wv_public_holidays(self):
        # West Virginia Day
        if self._year >= 1927:
            self._add_observed(self._add_holiday_jun_20("West Virginia Day"))

        # Election Day
        if self._year >= 2008 and self._year % 2 == 0:
            self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")

        # Day After Thanksgiving
        if self._year >= 1975:
            self._add_holiday_1_day_past_4th_thu_of_nov("Day After Thanksgiving")

    def _populate_subdiv_wy_public_holidays(self):
        pass

    def _populate_unofficial_holidays(self):
        # Very common celebrated cultural days, but no official observance.
        # Due to its nature, no in-lieus are observed.

        # Valentine's Day
        # While the modern iteration of Valentine's Day has started in the UK in 1797,
        # it wasn't until 1847 in the US that this started to be observed here.

        if self._year >= 1847:
            self._add_holiday_feb_14("Valentine's Day")

        # Saint Patrick's Day
        # Started in Boston in 1737 for the US.

        self._add_holiday_mar_17("Saint Patrick's Day")

        # Halloween
        # Halloween began in the US sometime around the 19th century.

        self._add_holiday_oct_31("Halloween")

        # Continental US non-Public dates

        if self.subdiv not in {"AS", "GU", "MP", "PR", "UM", "VI"}:
            # Groundhog Day
            # First observed on Feb 2 in 1886 in Continental US + Hawaii.

            if self._year >= 1886:
                self._add_holiday_feb_2("Groundhog Day")

            # Election Day
            # May be duplicates for certain states which has this as their actual public holiday.
            # The current US Presidential Election date pattern was codified in 1848 nationwide.

            if self._year >= 1848 and self._year % 4 == 0:
                self._add_holiday_1_day_past_1st_mon_of_nov("Election Day")


class US(UnitedStates):
    pass


class USA(UnitedStates):
    pass
