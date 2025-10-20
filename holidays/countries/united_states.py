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

from gettext import gettext as tr

from holidays.calendars.gregorian import (
    FEB,
    MAR,
    APR,
    MAY,
    SEP,
    NOV,
    DEC,
    MON,
    TUE,
    WED,
    THU,
    FRI,
    SAT,
    SUN,
)
from holidays.constants import GOVERNMENT, PUBLIC, UNOFFICIAL
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
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


class UnitedStates(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """United States of America (the) holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_United_States>
        * <https://en.wikipedia.org/wiki/Uniform_Monday_Holiday_Act>
        * [Federal holidays](https://web.archive.org/web/20250426120914/https://opm.gov/policy-data-oversight/pay-leave/federal-holidays/)
        * [Federal holidays history](https://web.archive.org/web/20250626042129/https://www.congress.gov/crs_external_products/R/PDF/R41990/R41990.11.pdf)
        * [16 Stat. 168](https://web.archive.org/web/20240602080239/https://memory.loc.gov/cgi-bin/ampage?collId=llsl&fileName=016/llsl016.db&recNum=203)
        * [Thanksgiving Day Proclamations 1789-Present](https://web.archive.org/web/20240621142029/https://www.whatsoproudlywehail.org/curriculum/the-american-calendar/thanksgiving-day-proclamations-1789-present/)
        * [H.J. RES. 41](https://web.archive.org/web/20250222190611/https://www.archives.gov/global-pages/larger-image.html?i=/legislative/features/thanksgiving/images/joint-res-l.jpg&c=/legislative/features/thanksgiving/images/joint-res.caption.html)
        * [H.J. RES. 41 December 9th, 1941 Amendment](https://web.archive.org/web/20250523062313/https://www.archives.gov/global-pages/larger-image.html?i=/legislative/features/thanksgiving/images/amendment-l.jpg&c=/legislative/features/thanksgiving/images/amendment.caption.html)
        * [B-112525 February 27th, 1953 32 COMP. GEN. 378](https://web.archive.org/web/20201001081239/https://www.gao.gov/products/b-112525#mt=e-report)
        * [Public Law 89-554](https://web.archive.org/web/20250512204449/https://www.govinfo.gov/content/pkg/STATUTE-80/pdf/STATUTE-80-Pg378.pdf)
        * [E.O. 11582 of February 11th, 1971](https://web.archive.org/web/20250326234305/https://www.archives.gov/federal-register/codification/executive-order/11582.html)
        * Washington's Birthday:
            * [AK](https://web.archive.org/web/20250306070343/https://doa.alaska.gov/calendar/)
            * [AL](https://web.archive.org/web/20250125202410/https://admincode.legislature.state.al.us/administrative-code/670-X-12-.01)
            * [AR](https://web.archive.org/web/20250213100442/https://arkleg.state.ar.us/Home/FTPDocument?path=/ACTS/2001/Public/ACT304.pdf)
            * [AZ](https://web.archive.org/web/20250323052619/https://www.azleg.gov/ars/1/00301.htm)
            * [CA](https://web.archive.org/web/20250414210521/http://www.sos.ca.gov/state-holidays/)
            * [CO](https://web.archive.org/web/20250409020643/https://leg.colorado.gov/sites/default/files/images/olls/crs2023-title-24.pdf)
            * [GA](https://web.archive.org/web/20250204223228/https://www.gasupreme.us/court-information/holidays-2/)
            * [HI](https://web.archive.org/web/20250313033818/https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/HRS0008/HRS_0008-0001.htm)
            * [ID](https://web.archive.org/web/20250328091357/https://idaho.gov/government/state-holidays/)
            * IN:
                * <https://web.archive.org/web/20250119103241/https://digital.statelib.lib.in.us/infoexpress/holidays.aspx>
                * <https://web.archive.org/web/20250418142531/https://www.in.gov/spd/benefits/state-holidays/>
            * [MD](https://web.archive.org/web/20250310030503/https://msa.maryland.gov/msa/mdmanual/01glance/html/holidayl.html)
            * [MI](https://web.archive.org/web/20250328094534/https://www.michigan.gov/som/government/state-holidays)
            * [MN](https://web.archive.org/web/20250322174508/https://www.revisor.mn.gov/statutes/cite/645.44)
            * [MT](https://web.archive.org/web/20250408030903/https://archive.legmt.gov/bills/mca/title_0010/chapter_0010/part_0020/section_0160/0010-0010-0020-0160.html)
            * [NJ](https://web.archive.org/web/20250409164919/https://nj.gov/nj/about/facts/holidays/)
            * [OH](https://web.archive.org/web/20250307080858/https://codes.ohio.gov/ohio-revised-code/section-1.14)
            * [OK](https://web.archive.org/web/20250424191658/https://oklahoma.gov/omes/divisions/human-capital-management/employee-benefits/leave-holidays/holidays.html)
            * [OR](https://web.archive.org/web/20250209222310/https://www.oregonlegislature.gov/bills_laws/ors/ors187.html)
            * [PA](https://web.archive.org/web/20241226003617/https://www.legis.state.pa.us/WU01/LI/LI/US/PDF/1893/0/0138..PDF)
            * [PR](https://en.wikipedia.org/wiki/Public_holidays_in_Puerto_Rico)
            * [SC](https://web.archive.org/web/20250212044252/https://www.scstatehouse.gov/code/t53c005.php)
            * [TN](https://web.archive.org/web/20250404130210/https://www.tn.gov/about-tn/state-holidays.html)
            * [TX](https://web.archive.org/web/20250314100137/http://www.tsl.texas.gov/ref/abouttx/holidays)
            * [UT](https://web.archive.org/web/20250312095206/https://le.utah.gov/xcode/Title63G/Chapter1/63G-1-S301.html)
            * [VA](https://web.archive.org/web/20250309075526/https://law.lis.virginia.gov/vacode/title2.2/chapter33/section2.2-3300/)
            * [VT](https://web.archive.org/web/20250415013508/https://legislature.vermont.gov/statutes/section/01/007/00371)
            * [WA](https://web.archive.org/web/20250414010238/https://app.leg.wa.gov/RCW/default.aspx?cite=1.16.050)
            * [WV](https://web.archive.org/web/20250328050144/http://code.wvlegislature.gov/2-2-1/)
            * [WY](https://web.archive.org/web/20250405094801/https://ai.wyo.gov/about-us/state-holidays-and-office-closures)
        * Columbus Day / Indigenous Peoples' Day history:
            * <https://web.archive.org/web/20250315203844/https://www.pewresearch.org/short-reads/2023/10/05/working-on-columbus-day-or-indigenous-peoples-day-it-depends-on-where-your-job-is/>
            * <https://web.archive.org/web/20240715051215/https://www.officeholidays.com/holidays/usa/columbus-day-state-guide>
            * <https://en.wikipedia.org/wiki/Indigenous_Peoples'_Day_(United_States)>
            * <https://web.archive.org/web/20250416043551/https://www.sos.ri.gov/divisions/civics-and-education/reference-desk/ri-state-holidays>
            * <https://web.archive.org/web/20080831103521/http://www.dpa.ca.gov/personnel-policies/holidays.htm>
        * [Frances Xavier Cabrini Day](https://web.archive.org/web/20250405014031/https://leg.colorado.gov/sites/default/files/2020a_1031_signed.pdf)
        * Northern Mariana Islands (subdivision MP):
            * <https://web.archive.org/web/20240727045236/https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/>
            * <https://web.archive.org/web/20250429140158/https://governor.gov.mp/archived-news/executive-actions-archive/memorandum-2022-legal-holidays/>
        * American Samoa:
            * <https://web.archive.org/web/20240808163628/https://asbar.org/code-annotated/1-0501-public-holidays/>
    """

    country = "US"
    default_language = "en_US"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_languages = ("en_US", "th")
    # Independence Declared on July 4th, 1776.
    start_year = 1777
    subdivisions: tuple[()] | tuple[str, ...] = (
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
    subdivisions_aliases = {
        "Alaska": "AK",
        "Alabama": "AL",
        "Arkansas": "AR",
        "American Samoa": "AS",
        "Arizona": "AZ",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "District of Columbia": "DC",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Guam": "GU",
        "Hawaii": "HI",
        "Iowa": "IA",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Massachusetts": "MA",
        "Maryland": "MD",
        "Maine": "ME",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Missouri": "MO",
        "Northern Mariana Islands": "MP",
        "Mississippi": "MS",
        "Montana": "MT",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Nebraska": "NE",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "Nevada": "NV",
        "New York": "NY",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Puerto Rico": "PR",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "United States Minor Outlying Islands": "UM",
        "Utah": "UT",
        "Virginia": "VA",
        "Virgin Islands, U.S.": "VI",
        "Vermont": "VT",
        "Washington": "WA",
        "Wisconsin": "WI",
        "West Virginia": "WV",
        "Wyoming": "WY",
    }
    supported_categories = (GOVERNMENT, PUBLIC, UNOFFICIAL)
    _deprecated_subdivisions = (
        "FM",
        "MH",
        "PW",
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=UnitedStatesStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_TO_PREV_FRI + SUN_TO_NEXT_MON)
        # B-11252 February 27th, 1953 32 COMP. GEN. 378.
        kwargs.setdefault("observed_since", 1953)
        super().__init__(*args, **kwargs)

    def _populate_common(self, *, include_federal: bool = False):
        """
        Populates common US holidays.

        Federal Holidays were first codified on June 28th, 1870
        via 16 Stat. 168.

        First regulation on holidays in-lieu observance is from B-112525
        February 27th, 1953 32 COMP. GEN. 378 document which shifts
        from SUN to next MON only.

        It wouldn't be until Public Law 89-554 from September 6th, 1966
        that SAT to previous MON is listed as well.

        This would be finally consolidated as part of E.O. 11582 of
        February 11th, 1971 later.

        :param include_federal:
            Whether to include federal-specific holidays.
        """
        self._observed_rule = (
            SAT_TO_PREV_FRI + SUN_TO_NEXT_MON if self._year >= 1966 else SUN_TO_NEXT_MON
        )

        if self._year >= 1871:
            # New Year's Day.
            name = tr("New Year's Day")
            self._add_observed(self._add_new_years_day(name))
            # Public Law 89-554 of September 6th, 1966.
            if self._year >= 1967:
                self._add_observed(self._next_year_new_years_day, name=name)

        if include_federal:
            if self._year >= 1986:
                # Birthday of Martin Luther King, Jr..
                self._add_holiday_3rd_mon_of_jan(tr("Birthday of Martin Luther King, Jr."))

            if self._year >= 1879:
                # Washington's Birthday.
                name = tr("Washington's Birthday")
                if self._year >= 1971:
                    self._add_holiday_3rd_mon_of_feb(name)
                else:
                    dt = self._add_holiday_feb_22(name)
                    # B-112525 February 27th, 1953 32 COMP. GEN. 378.
                    if self._year >= 1954:
                        self._add_observed(dt)

        if self._year >= 1971:
            # Memorial Day.
            self._add_holiday_last_mon_of_may(tr("Memorial Day"))

        if self._year >= 2021:
            self._add_observed(
                # Juneteenth National Independence Day.
                self._add_holiday_jun_19(tr("Juneteenth National Independence Day"))
            )

        if self._year >= 1870:
            # Independence Day.
            self._add_observed(self._add_holiday_jul_4(tr("Independence Day")))

        if self._year >= 1894:
            # Labor Day.
            self._add_holiday_1st_mon_of_sep(tr("Labor Day"))

        if include_federal and self._year >= 1971:
            # Columbus Day.
            self._add_holiday_2nd_mon_of_oct(tr("Columbus Day"))

        if self._year >= 1938:
            name = (
                # Veterans Day.
                tr("Veterans Day")
                if self._year >= 1954
                # Armistice Day.
                else tr("Armistice Day")
            )
            if 1971 <= self._year <= 1977:
                self._add_holiday_4th_mon_of_oct(name)
            else:
                self._add_observed(self._add_remembrance_day(name))

        # Thanksgiving Day.
        # Began to be declared annually in 1862 by Abraham Lincoln.
        # First declared as last THU of NOV in 1863.
        # Briefly moved to 3rd THU of NOV by Franklin Delano Roosevelt from 1939 to 1941.
        # First codified as last THU of NOV on October 6th, 1941 via H.J. RES. 41.
        # Become 4th THU of NOV from 1942 onwards via a Senate Amendment on December 9th, 1941.
        # For Pre-1862 observances, see UnitedStatesStaticHolidays.

        if self._year >= 1862:
            thanksgiving_day_dates = {
                1862: (APR, 10),
                1865: (DEC, 7),
                1869: (NOV, 18),
                1939: (NOV, 23),
                1940: (NOV, 21),
                1941: (NOV, 20),
            }
            # Thanksgiving Day.
            name = tr("Thanksgiving Day")
            if dt := thanksgiving_day_dates.get(self._year):
                self._add_holiday(name, dt)
            elif self._year >= 1942:
                self._add_holiday_4th_thu_of_nov(name)
            else:
                self._add_holiday_last_thu_of_nov(name)

        if self._year >= 1870:
            # Christmas Day.
            self._add_observed(self._add_christmas_day(tr("Christmas Day")))

    def _populate_public_holidays(self):
        self._populate_common()

        if 1888 <= self._year <= 1970:
            # Memorial Day.
            self._add_holiday_may_30(tr("Memorial Day"))

    def _add_christmas_eve_holiday(self):
        # If on Friday, observed on Thursday.
        # If on Saturday or Sunday, observed on Friday.

        # Christmas Eve.
        name = tr("Christmas Eve")
        self._add_observed(
            self._add_christmas_eve(name), name=name, rule=FRI_TO_PREV_THU + SAT_SUN_TO_PREV_FRI
        )

    def _populate_subdiv_holidays(self):
        if PUBLIC not in self.categories:
            return None

        if self._year >= 1986 and self.subdiv not in {"AL", "AR", "AZ", "GA", "ID", "MS", "NH"}:
            # Martin Luther King Jr. Day.
            self._add_holiday_3rd_mon_of_jan(tr("Martin Luther King Jr. Day"))

        if self._year >= 1879 and self.subdiv not in {
            "AK",
            "AL",
            "AR",
            "AZ",
            "CA",
            "CO",
            "DE",
            "FL",
            "GA",
            "HI",
            "ID",
            "IN",
            "MD",
            "MN",
            "MT",
            "NJ",
            "NM",
            "OH",
            "OK",
            "OR",
            "PA",
            "PR",
            "SC",
            "TN",
            "TX",
            "UT",
            "VA",
            "VI",
            "VT",
            "WA",
            "WV",
            "WY",
        }:
            # Washington's Birthday.
            name = tr("Washington's Birthday")
            if self._year >= 1971:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_feb_22(name)

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
            # Columbus Day.
            name = tr("Columbus Day")
            if self._year >= 1971:
                self._add_holiday_2nd_mon_of_oct(name)
            else:
                self._add_columbus_day(name)

        super()._populate_subdiv_holidays()

    def _populate_subdiv_ak_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        # No observance in 1921: https://web.archive.org/web/20230208015211/https://chroniclingamerica.loc.gov/lccn/sn86072239/1922-03-29/ed-1/seq-8/
        if self._year >= 1918 and self._year != 1921:
            # Seward's Day.
            name = tr("Seward's Day")
            if self._year >= 1955:
                self._add_holiday_last_mon_of_mar(name)
            else:
                self._add_holiday_mar_30(name)

        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day.
                tr("Indigenous Peoples' Day")
                if self._year >= 2015
                # Columbus Day.
                else tr("Columbus Day")
            )

        # https://web.archive.org/web/20120502232826/http://www.alaskadispatch.com/article/happy-alaska-day-great-land
        if self._year >= 1917:
            # Alaska Day.
            self._add_observed(self._add_holiday_oct_18(tr("Alaska Day")))

    def _populate_subdiv_al_public_holidays(self):
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                # Martin Luther King, Jr & Robert E. Lee's Birthday.
                tr("Martin Luther King, Jr & Robert E. Lee's Birthday")
            )

        if self._year >= 1879:
            # George Washington & Thomas Jefferson's Birthday.
            name = tr("George Washington & Thomas Jefferson's Birthday")
            if self._year >= 1971:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_feb_22(name)

        if self._year >= 1866:
            # Confederate Memorial Day.
            self._add_holiday_4th_mon_of_apr(tr("Confederate Memorial Day"))

        if self._year >= 1890:
            # Jefferson Davis Birthday.
            self._add_holiday_1st_mon_of_jun(tr("Jefferson Davis Birthday"))

        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Columbus Day / American Indian Heritage Day / Fraternal Day.
                tr("Columbus Day / American Indian Heritage Day / Fraternal Day")
                if self._year >= 2000
                # Columbus Day / Fraternal Day.
                else tr("Columbus Day / Fraternal Day")
            )

    def _populate_subdiv_ar_public_holidays(self):
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                # Martin Luther King Jr. Day.
                tr("Martin Luther King Jr. Day")
                if self._year >= 2018
                # Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays.
                else tr("Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays")
            )

        if self._year >= 1879:
            # George Washington's Birthday and Daisy Gatson Bates Day.
            name = tr("George Washington's Birthday and Daisy Gatson Bates Day")
            if self._year >= 1971:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_feb_22(name)

    def _populate_subdiv_as_public_holidays(self):
        if self._year >= 1901:
            # American Samoa Flag Day.
            self._add_observed(self._add_holiday_apr_17(tr("American Samoa Flag Day")))

        if self._year >= 1983:
            # Manu'a Islands Cession Day.
            self._add_observed(self._add_holiday_jul_16(tr("Manu'a Islands Cession Day")))

        # White Sunday.
        self._add_holiday_2nd_sun_of_oct(tr("White Sunday"))

    def _populate_subdiv_az_public_holidays(self):
        if self._year >= 1986:
            # Dr. Martin Luther King Jr. / Civil Rights Day.
            self._add_holiday_3rd_mon_of_jan(tr("Dr. Martin Luther King Jr. / Civil Rights Day"))

        if self._year >= 1971:
            # Lincoln/Washington Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Lincoln/Washington Presidents' Day"))

    def _populate_subdiv_ca_public_holidays(self):
        if 1971 <= self._year <= 2009:
            # Lincoln's Birthday.
            self._add_observed(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 2014:
            # Susan B. Anthony Day.
            self._add_holiday_feb_15(tr("Susan B. Anthony Day"))

        if self._year >= 1995:
            self._add_observed(
                # Cesar Chavez Day.
                self._add_holiday_mar_31(tr("Cesar Chavez Day")),
                rule=SUN_TO_NEXT_MON,
            )

        if 1971 <= self._year <= 2008:
            # Columbus Day.
            self._add_holiday_2nd_mon_of_oct(tr("Columbus Day"))

        if self._year >= 1975:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_co_public_holidays(self):
        if self._year >= 1971:
            # Washington-Lincoln Day.
            self._add_holiday_3rd_mon_of_feb(tr("Washington-Lincoln Day"))

        if self._year >= 2001:
            # Cesar Chavez Day.
            self._add_holiday_mar_31(tr("Cesar Chavez Day"))

        if self._year >= 2020:
            # Frances Xavier Cabrini Day.
            self._add_holiday_1st_mon_of_oct(tr("Frances Xavier Cabrini Day"))

    def _populate_subdiv_ct_public_holidays(self):
        if self._year >= 1971:
            # Lincoln's Birthday.
            self._add_observed(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

    def _populate_subdiv_dc_public_holidays(self):
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            # Inauguration Day.
            name = tr("Inauguration Day")
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )

        if self._year >= 2005:
            # Emancipation Day.
            self._add_observed(self._add_holiday_apr_16(tr("Emancipation Day")))

        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day.
                tr("Indigenous Peoples' Day")
                if self._year >= 2019
                # Columbus Day.
                else tr("Columbus Day")
            )

    def _populate_subdiv_de_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        if self._year >= 1975:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_fl_public_holidays(self):
        if self._year >= 2011:
            # Susan B. Anthony Day.
            self._add_holiday_feb_15(tr("Susan B. Anthony Day"))

        if self._year >= 1975:
            # Friday After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Friday After Thanksgiving"))

    def _populate_subdiv_ga_public_holidays(self):
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                # Martin Luther King Jr. Day.
                tr("Martin Luther King Jr. Day")
                if self._year >= 2012
                # Robert E. Lee's Birthday.
                else tr("Robert E. Lee's Birthday")
            )

        if self._year >= 1866:
            name = (
                # State Holiday.
                tr("State Holiday")
                if self._year >= 2016
                # Confederate Memorial Day.
                else tr("Confederate Memorial Day")
            )
            if self._year == 2020:
                self._add_holiday_apr_10(name)
            else:
                self._add_holiday_4th_mon_of_apr(name)

        if self._year >= 1986:
            self._add_holiday_1_day_past_4th_thu_of_nov(
                # State Holiday.
                tr("State Holiday")
                if self._year >= 2016
                # Robert E. Lee's Birthday.
                else tr("Robert E. Lee's Birthday")
            )

        if self._year >= 1879:
            self._add_holiday(
                # Washington's Birthday.
                tr("Washington's Birthday"),
                self._get_observed_date(self._christmas_day, rule=GA_IN_WASHINGTON_BIRTHDAY),
            )

    def _populate_subdiv_gu_public_holidays(self):
        if self._year >= 1970:
            # Guam Discovery Day.
            self._add_holiday_1st_mon_of_mar(tr("Guam Discovery Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 1945:
            # Liberation Day (Guam).
            self._add_holiday_jul_21(tr("Liberation Day (Guam)"))

        # All Souls' Day.
        self._add_all_souls_day(tr("All Souls' Day"))

        # Lady of Camarin Day.
        self._add_immaculate_conception_day(tr("Lady of Camarin Day"))

    def _populate_subdiv_hi_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 1949:
            # Prince Jonah Kuhio Kalanianaole Day.
            self._add_observed(self._add_holiday_mar_26(tr("Prince Jonah Kuhio Kalanianaole Day")))

        if self._year >= 1872:
            # Kamehameha Day.
            jun_11 = self._add_holiday_jun_11(tr("Kamehameha Day"))
            if self._year >= 2011:
                self._add_observed(jun_11)

        if self._year >= 1959:
            # Statehood Day.
            self._add_holiday_3rd_fri_of_aug(tr("Statehood Day"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

    def _populate_subdiv_ia_public_holidays(self):
        if self._year >= 1971:
            # Lincoln's Birthday.
            self._add_observed(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

    def _populate_subdiv_id_public_holidays(self):
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                # Martin Luther King Jr. / Idaho Human Rights Day.
                tr("Martin Luther King Jr. / Idaho Human Rights Day")
                if self._year >= 2006
                # Martin Luther King Jr. Day.
                else tr("Martin Luther King Jr. Day")
            )

        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

    def _populate_subdiv_il_public_holidays(self):
        if self._year >= 1971:
            # Lincoln's Birthday.
            self._add_observed(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

        if self._year >= 1978:
            # Casimir Pulaski Day.
            self._add_holiday_1st_mon_of_mar(tr("Casimir Pulaski Day"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

    def _populate_subdiv_in_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 2015 or (self._year >= 2006 and self._year % 2 == 0):
            # Primary Election Day.
            self._add_holiday_1_day_past_1st_mon_of_may(tr("Primary Election Day"))

        if self._year >= 2015 or (self._year >= 2008 and self._year % 2 == 0):
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        if self._year >= 2010:
            # Lincoln's Birthday.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Lincoln's Birthday"))

        if self._year >= 1879:
            self._add_holiday(
                # Washington's Birthday.
                tr("Washington's Birthday"),
                self._get_observed_date(self._christmas_day, rule=GA_IN_WASHINGTON_BIRTHDAY),
            )

    def _populate_subdiv_ks_public_holidays(self):
        if self._year >= 2013:
            # Christmas Eve.
            self._add_christmas_eve_holiday()

    def _populate_subdiv_ky_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 2013:
            # New Year's Eve.
            self._add_observed(self._add_new_years_eve(tr("New Year's Eve")))

    def _populate_subdiv_la_public_holidays(self):
        if self._year >= 1857:
            # Mardi Gras.
            self._add_carnival_tuesday(tr("Mardi Gras"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

    def _populate_subdiv_ma_public_holidays(self):
        if self._year >= 1901:
            self._add_observed(
                # Evacuation Day.
                self._add_holiday_mar_17(tr("Evacuation Day")),
                rule=SAT_SUN_TO_NEXT_MON,
            )

        if self._year >= 1894:
            # Patriots' Day.
            name = tr("Patriots' Day")
            if self._year >= 1969:
                self._add_holiday_3rd_mon_of_apr(name)
            else:
                self._add_holiday_apr_19(name)

    def _populate_subdiv_md_public_holidays(self):
        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            # Inauguration Day.
            name = tr("Inauguration Day")
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )

        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 2008:
            # American Indian Heritage Day.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("American Indian Heritage Day"))

    def _populate_subdiv_me_public_holidays(self):
        if self._year >= 1894:
            # Patriots' Day.
            name = tr("Patriots' Day")
            if self._year >= 1969:
                self._add_holiday_3rd_mon_of_apr(tr("Patriots' Day"))
            else:
                self._add_holiday_apr_19(name)

        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day.
                tr("Indigenous Peoples' Day")
                if self._year >= 2019
                # Columbus Day.
                else tr("Columbus Day")
            )

    def _populate_subdiv_mi_public_holidays(self):
        if self._year >= 2013:
            # Christmas Eve.
            self._add_christmas_eve_holiday()

            # New Year's Eve.
            self._add_observed(self._add_new_years_eve(tr("New Year's Eve")))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        if self._year >= 2017:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_mn_public_holidays(self):
        if self._year >= 1971:
            # Washington's and Lincoln's Birthday.
            self._add_holiday_3rd_mon_of_feb(tr("Washington's and Lincoln's Birthday"))

    def _populate_subdiv_mo_public_holidays(self):
        if self._year >= 1949:
            # Truman Day.
            self._add_observed(self._add_holiday_may_8(tr("Truman Day")))

    def _populate_subdiv_mp_public_holidays(self):
        # Commonwealth Covenant Day.
        self._add_observed(self._add_holiday_mar_24(tr("Commonwealth Covenant Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Commonwealth Cultural Day.
        self._add_holiday_2nd_mon_of_oct(tr("Commonwealth Cultural Day"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        # Citizenship Day.
        self._add_observed(self._add_holiday_nov_4(tr("Citizenship Day")))

        # Constitution Day.
        self._add_observed(self._add_holiday_dec_8(tr("Constitution Day")))

    def _populate_subdiv_ms_public_holidays(self):
        if self._year >= 1986:
            self._add_holiday_3rd_mon_of_jan(
                # Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays.
                tr("Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays")
            )

        if self._year >= 1866:
            # Confederate Memorial Day.
            self._add_holiday_last_mon_of_apr(tr("Confederate Memorial Day"))

    def _populate_subdiv_mt_public_holidays(self):
        if self._year >= 1971:
            # Lincoln's and Washington's Birthdays.
            self._add_holiday_3rd_mon_of_feb(tr("Lincoln's and Washington's Birthdays"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

    def _populate_subdiv_nc_public_holidays(self):
        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 1975:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

        if self._year >= 2013:
            # Christmas Eve.
            self._add_christmas_eve_holiday()

        # If on Saturday or Sunday, observed on Monday
        # If on Monday, observed on Tuesday
        if self._year >= 2013:
            # Day After Christmas.
            name = tr("Day After Christmas")
            self._add_observed(
                self._add_christmas_day_two(name),
                name=name,
                rule=MON_TO_NEXT_TUE + SAT_SUN_TO_NEXT_MON,
            )

    def _populate_subdiv_nd_public_holidays(self):
        pass

    def _populate_subdiv_ne_public_holidays(self):
        if self._year >= 1875:
            # Arbor Day.
            name = tr("Arbor Day")
            if self._year >= 1989:
                self._add_holiday_last_fri_of_apr(name)
            else:
                self._add_holiday_apr_22(name)

        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day.
                tr("Indigenous Peoples' Day")
                if self._year >= 2020
                # Columbus Day.
                else tr("Columbus Day")
            )

    def _populate_subdiv_nh_public_holidays(self):
        if self._year >= 1986:
            # Dr. Martin Luther King Jr. / Civil Rights Day.
            self._add_holiday_3rd_mon_of_jan(tr("Dr. Martin Luther King Jr. / Civil Rights Day"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        if self._year >= 1975:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_nj_public_holidays(self):
        if self._year >= 1971:
            # Lincoln's Birthday.
            self._add_observed(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

            # Presidents Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

    def _populate_subdiv_nm_public_holidays(self):
        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day.
                tr("Indigenous Peoples' Day")
                if self._year >= 2019
                # Columbus Day.
                else tr("Columbus Day")
            )

        # Presidents' Day.
        self._add_holiday_1_day_past_4th_thu_of_nov(tr("Presidents' Day"))

    def _populate_subdiv_nv_public_holidays(self):
        if self._year >= 1933:
            # Nevada Day.
            name = tr("Nevada Day")
            self._add_observed(
                self._add_holiday_last_fri_of_oct(name)
                if self._year >= 2000
                else self._add_holiday_oct_31(name)
            )

        # Family Day.
        self._add_holiday_1_day_past_4th_thu_of_nov(tr("Family Day"))

    def _populate_subdiv_ny_public_holidays(self):
        if self._year >= 1971:
            # Lincoln's Birthday.
            self._add_observed(self._add_holiday_feb_12(tr("Lincoln's Birthday")))

        if self._year >= 2004:
            # Susan B. Anthony Day.
            self._add_holiday_feb_15(tr("Susan B. Anthony Day"))

        if self._year >= 2015 or (self._year >= 2008 and self._year % 2 == 0):
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

    def _populate_subdiv_oh_public_holidays(self):
        if self._year >= 1971:
            # Washington-Lincoln Day.
            self._add_holiday_3rd_mon_of_feb(tr("Washington-Lincoln Day"))

    def _populate_subdiv_ok_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 1975:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_or_public_holidays(self):
        if self._year >= 1971:
            # Presidents Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents Day"))

    def _populate_subdiv_pa_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        # Day After Thanksgiving.
        self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_pr_public_holidays(self):
        # Epiphany.
        self._add_epiphany_day(tr("Epiphany"))

        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        # Emancipation Day.
        self._add_observed(self._add_holiday_mar_22(tr("Emancipation Day")), rule=SUN_TO_NEXT_MON)

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Constitution Day.
        self._add_observed(self._add_holiday_jul_25(tr("Constitution Day")), rule=SUN_TO_NEXT_MON)

        # Discovery Day.
        self._add_observed(self._add_holiday_nov_19(tr("Discovery Day")), rule=SUN_TO_NEXT_MON)

    def _populate_subdiv_ri_public_holidays(self):
        if self._year >= 1948:
            # Victory Day.
            self._add_holiday_2nd_mon_of_aug(tr("Victory Day"))

        if self._year >= 1971:
            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day / Columbus Day.
                tr("Indigenous Peoples' Day / Columbus Day")
                if self._year >= 2022
                # Columbus Day.
                else tr("Columbus Day")
            )

    def _populate_subdiv_sc_public_holidays(self):
        if self._year >= 1971:
            # President's Day.
            self._add_holiday_3rd_mon_of_feb(tr("President's Day"))

        if self._year >= 1866:
            # Confederate Memorial Day.
            self._add_holiday_4th_mon_of_apr(tr("Confederate Memorial Day"))

    def _populate_subdiv_sd_public_holidays(self):
        if self._year >= 1937:
            name = (
                # Native Americans' Day.
                tr("Native Americans' Day")
                if self._year >= 1990
                # Columbus Day.
                else tr("Columbus Day")
            )
            if self._year >= 1970:
                self._add_holiday_2nd_mon_of_oct(name)
            else:
                self._add_columbus_day(name)

    def _populate_subdiv_tn_public_holidays(self):
        if self._year >= 1971:
            # President's Day.
            self._add_holiday_3rd_mon_of_feb(tr("President's Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

    def _populate_subdiv_tx_public_holidays(self):
        if self._year >= 1931:
            # Confederate Memorial Day.
            self._add_holiday_jan_19(tr("Confederate Memorial Day"))

        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 1874:
            # Texas Independence Day.
            self._add_holiday_mar_2(tr("Texas Independence Day"))

        if self._year >= 2000:
            # Cesar Chavez Day.
            self._add_holiday_mar_31(tr("Cesar Chavez Day"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 1875:
            # San Jacinto Day.
            self._add_holiday_apr_21(tr("San Jacinto Day"))

        if self._year >= 1980:
            # Emancipation Day In Texas.
            self._add_holiday_jun_19(tr("Emancipation Day In Texas"))

        if self._year >= 1973:
            # Lyndon Baines Johnson Day.
            self._add_holiday_aug_27(tr("Lyndon Baines Johnson Day"))

        if self._year >= 1975:
            # Friday After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Friday After Thanksgiving"))

        if self._year >= 1981:
            # Christmas Eve.
            self._add_christmas_eve_holiday()

            # Day After Christmas.
            self._add_christmas_day_two(tr("Day After Christmas"))

    def _populate_subdiv_um_public_holidays(self):
        pass

    def _populate_subdiv_ut_public_holidays(self):
        if self._year >= 1971:
            # Washington and Lincoln Day.
            self._add_holiday_3rd_mon_of_feb(tr("Washington and Lincoln Day"))

        if self._year >= 1849:
            # Pioneer Day.
            self._add_observed(self._add_holiday_jul_24(tr("Pioneer Day")))

    def _populate_subdiv_va_public_holidays(self):
        if 1889 <= self._year <= 2020:
            # Lee Jackson Day.
            name = tr("Lee Jackson Day")
            if self._year >= 2000:
                self._add_holiday_3_days_prior_3rd_mon_of_jan(name)
            elif self._year >= 1983:
                self._add_holiday_3rd_mon_of_jan(name)
            else:
                self._add_holiday_jan_19(name)

        if self._year >= 1789 and (self._year - 1789) % 4 == 0:
            # Inauguration Day.
            name = tr("Inauguration Day")
            self._add_observed(
                self._add_holiday_jan_20(name)
                if self._year >= 1937
                else self._add_holiday_mar_4(name),
                rule=SUN_TO_NEXT_MON,
            )

        if self._year >= 1971:
            # George Washington Day.
            self._add_holiday_3rd_mon_of_feb(tr("George Washington Day"))

            self._add_holiday_2nd_mon_of_oct(
                # Indigenous Peoples' Day.
                tr("Indigenous Peoples' Day")
                if self._year >= 2020
                # Columbus Day.
                else tr("Columbus Day")
            )

    def _populate_subdiv_vi_public_holidays(self):
        # Three Kings Day.
        self._add_epiphany_day(tr("Three Kings Day"))

        if self._year >= 1879:
            # Presidents' Day.
            name = tr("Presidents' Day")
            if self._year >= 1971:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_feb_22(name)

        # Transfer Day.
        self._add_holiday_mar_31(tr("Transfer Day"))

        # Holy Thursday.
        self._add_holy_thursday(tr("Holy Thursday"))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Emancipation Day.
        self._add_holiday_jul_3(tr("Emancipation Day"))

        if self._year >= 1937:
            # Columbus Day and Puerto Rico Friendship Day.
            name = tr("Columbus Day and Puerto Rico Friendship Day")
            if self._year >= 1970:
                self._add_holiday_2nd_mon_of_oct(name)
            else:
                self._add_columbus_day(name)

        # Liberty Day.
        self._add_holiday_nov_1(tr("Liberty Day"))

        # Christmas Second Day.
        self._add_christmas_day_two(tr("Christmas Second Day"))

    def _populate_subdiv_vt_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 1800:
            # Town Meeting Day.
            self._add_holiday_1st_tue_of_mar(tr("Town Meeting Day"))

        if self._year >= 1778:
            # Bennington Battle Day.
            self._add_observed(self._add_holiday_aug_16(tr("Bennington Battle Day")))

    def _populate_subdiv_wa_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

    def _populate_subdiv_wi_public_holidays(self):
        if self._year >= 1976:
            # Susan B. Anthony Day.
            self._add_holiday_feb_15(tr("Susan B. Anthony Day"))

        if self._year >= 2012:
            # Christmas Eve.
            self._add_christmas_eve_holiday()

            # New Year's Eve.
            self._add_observed(self._add_new_years_eve(tr("New Year's Eve")))

    def _populate_subdiv_wv_public_holidays(self):
        if self._year >= 1971:
            # Presidents' Day.
            self._add_holiday_3rd_mon_of_feb(tr("Presidents' Day"))

        if self._year >= 1927:
            # West Virginia Day.
            self._add_observed(self._add_holiday_jun_20(tr("West Virginia Day")))

        if self._year >= 2008 and self._year % 2 == 0:
            # Election Day.
            self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))

        if self._year >= 1975:
            # Day After Thanksgiving.
            self._add_holiday_1_day_past_4th_thu_of_nov(tr("Day After Thanksgiving"))

    def _populate_subdiv_wy_public_holidays(self):
        if self._year >= 1971:
            # President's Day.
            self._add_holiday_3rd_mon_of_feb(tr("President's Day"))

    def _populate_government_holidays(self):
        # Added by 16 Stat. 168, effectdive date June 28th, 1870.
        # New Year's Day check for 1871 is included.
        if self._year >= 1870:
            # Federal holidays in the United States.
            self._populate_common(include_federal=True)

    def _populate_unofficial_holidays(self):
        # Very common celebrated cultural days, but no official observance.
        # Due to its nature, no in-lieus are observed.

        # Valentine's Day.
        # While the modern iteration of Valentine's Day has started in the UK in 1797,
        # it wasn't until 1847 in the US that this started to be observed here.

        if self._year >= 1847:
            # Valentine's Day.
            self._add_holiday_feb_14(tr("Valentine's Day"))

        # Saint Patrick's Day.
        # Started in Boston in 1737 for the US.

        # Saint Patrick's Day.
        self._add_saint_patricks_day(tr("Saint Patrick's Day"))

        # Mother's Day.
        # Starts to be observed by most US states by 1911.
        # Officially proclaimed as a National Holiday by President Woodrow Wilson in 1914.

        if self._year >= 1914:
            # Mother's Day.
            self._add_holiday_2nd_sun_of_may(tr("Mother's Day"))

        # Father's Day.
        # First founded in the state of Washington by Sonora Smart Dodd in 1910.
        # Officially proclaimed as a National Holiday by President Richard Nixon in 1972.

        if self._year >= 1972:
            # Father's Day.
            self._add_holiday_3rd_sun_of_jun(tr("Father's Day"))

        # Halloween.
        # Halloween began in the US sometime around the 19th century.

        # Halloween.
        self._add_holiday_oct_31(tr("Halloween"))

        # Continental US non-Public dates

        if self.subdiv not in {"AS", "GU", "MP", "PR", "UM", "VI"}:
            # Groundhog Day
            # First observed on Feb 2 in 1886 in Continental US + Hawaii.

            if self._year >= 1886:
                # Groundhog Day.
                self._add_holiday_feb_2(tr("Groundhog Day"))

            # Election Day
            # May be duplicates for certain states which has this as their actual public holiday.
            # The current US Presidential Election date pattern was codified in 1848 nationwide.

            if self._year >= 1848 and self._year % 4 == 0:
                # Election Day.
                self._add_holiday_1_day_past_1st_mon_of_nov(tr("Election Day"))


class US(UnitedStates):
    pass


class USA(UnitedStates):
    pass


class UnitedStatesStaticHolidays(StaticHolidays):
    """United States special holidays.

    Thanksgiving Proclamation References:
        * [1777](https://web.archive.org/web/20240621142028/https://pilgrimhall.org/pdf/TG_First_National_Thanksgiving_Proclamation_1777.pdf)
        * [1782](https://web.archive.org/web/20240621142030/https://www.loc.gov/exhibits/religion/vc006491.jpg)
        * [1789](https://web.archive.org/web/20240621142029/https://www.whatsoproudlywehail.org/curriculum/the-american-calendar/thanksgiving-proclamation-1789-2)
        * [1795](https://web.archive.org/web/20240621142029/https://founders.archives.gov/documents/Washington/05-17-02-0239)
        * [1798](https://web.archive.org/web/20240621142029/https://founders.archives.gov/documents/Adams/99-02-02-2386)
        * [1799](https://web.archive.org/web/20240621142029/https://founders.archives.gov/documents/Adams/99-02-02-3372)
        * [1813](https://web.archive.org/web/20240621142030/https://founders.archives.gov/documents/Madison/03-06-02-0434)
        * [1815](https://web.archive.org/web/20240621142030/https://founders.archives.gov/documents/Madison/03-09-02-0066)

    Pre-1971 Inauguration Day observances has been moved here.
    """

    # Fasting and Humiliation Day.
    fasting_and_humiliation_day_name = tr("Fasting and Humiliation Day")
    # Public Humiliation and Prayer Day.
    public_humiliation_and_prayer_day_name = tr("Public Humiliation and Prayer Day")
    # Public Thanksgiving and Prayer Day.
    public_thanksgiving_and_prayer_day_name = tr("Public Thanksgiving and Prayer Day")

    # Inauguration Day.
    inauguration_day_name = tr("Inauguration Day")

    special_public_holidays = {
        1777: (DEC, 18, public_thanksgiving_and_prayer_day_name),
        1782: (NOV, 28, public_thanksgiving_and_prayer_day_name),
        1789: (NOV, 26, public_thanksgiving_and_prayer_day_name),
        1795: (FEB, 19, public_thanksgiving_and_prayer_day_name),
        1798: (MAY, 9, fasting_and_humiliation_day_name),
        1799: (APR, 25, fasting_and_humiliation_day_name),
        1813: (SEP, 9, public_humiliation_and_prayer_day_name),
        1815: (APR, 13, public_humiliation_and_prayer_day_name),
    }

    # Pre-1953 Inauguration Day observances.
    special_dc_public_holidays_observed = {
        1877: (MAR, 5, inauguration_day_name),
        1917: (MAR, 5, inauguration_day_name),
    }
    special_md_public_holidays_observed = {
        1877: (MAR, 5, inauguration_day_name),
        1917: (MAR, 5, inauguration_day_name),
    }
    special_va_public_holidays_observed = {
        1877: (MAR, 5, inauguration_day_name),
        1917: (MAR, 5, inauguration_day_name),
    }
