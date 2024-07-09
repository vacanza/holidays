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

"""
References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    - https://web.archive.org/web/20130703014214/http://www.hrsdc.gc.ca/eng/labour/overviews/employment_standards/holidays.shtml
    - https://www.alberta.ca/alberta-general-holidays
    - https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/employment-standards/statutory-holidays
    - http://web2.gov.mb.ca/laws/statutes/ccsm/r120e.php
    - https://www2.gnb.ca/content/gnb/en/departments/elg/local_government/content/governance/content/days_of_rest_act.html
    - https://www.ontario.ca/document/your-guide-employment-standards-act-0/public-holidays
    - https://www.officeholidays.com/countries/canada/
    - https://www.timeanddate.com/holidays/canada/
"""

from datetime import date
from gettext import gettext as tr
from typing import Optional

from holidays.calendars.gregorian import MAR, APR, JUN, JUL, SEP
from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ALL_TO_NEAREST_MON,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
    SUN_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
)


class CaHolidays(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """A class to represent holidays for Canada."""

    country = "CA"
    name = "Canada"
    default_language = "en_CA"
    # %s (observed).
    observed_label = tr("%s (observed)")
    supported_categories = (GOVERNMENT, OPTIONAL, PUBLIC)
    subdivisions = (
        "AB",
        "BC",
        "MB",
        "NB",
        "NL",
        "NS",
        "NT",
        "NU",
        "ON",
        "PE",
        "QC",
        "SK",
        "YT",
    )
    supported_languages = ("ar", "en_CA", "en_US", "fr", "th")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, CaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _get_nearest_monday(self, *args) -> Optional[date]:
        return self._get_observed_date(date(self._year, *args), rule=ALL_TO_NEAREST_MON)

    def _add_statutory_holidays(self):
        """A class to represent holidays for Nationwide statutory."""

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        if self._year >= 1879:
            self._canada_day = self._add_holiday_jul_1(
                # Canada Day.
                tr("Canada Day")
                if self._year >= 1983
                # Dominion Day.
                else tr("Dominion Day")
            )

        if self._year >= 1894:
            # Labor Day.
            self._add_holiday_1st_mon_of_sep(tr("Labour Day"))

        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

    def _populate_public_holidays(self):
        if self._year <= 1866:
            return None

        self._add_statutory_holidays()

        self._add_observed(self._christmas_day)

    def _populate_government_holidays(self):
        """Holidays for federally regulated workplaces."""

        if self._year <= 1866:
            return None

        self._add_statutory_holidays()

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1879:
            self._add_observed(self._canada_day)

        if self._year >= 2021:
            self._add_observed(
                # National Day for Truth and Reconciliation.
                self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))
            )

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

        self._add_observed(self._christmas_day, rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day.
        self._add_observed(
            self._add_christmas_day_two(tr("Boxing Day")), rule=SAT_SUN_TO_NEXT_MON_TUE
        )

    def _populate_optional_holidays(self):
        if self._year <= 1866:
            return None

        # Christmas Day.
        self._add_observed(
            self._add_christmas_day(tr("Christmas Day")), rule=SAT_SUN_TO_NEXT_MON_TUE
        )

        # Boxing Day.
        self._add_observed(
            self._add_christmas_day_two(tr("Boxing Day")), rule=SAT_SUN_TO_NEXT_MON_TUE
        )

    def _add_thanksgiving_day(self):
        if self._year >= 1931:
            # Thanksgiving Day.
            name = tr("Thanksgiving Day")
            # in 1935, Canadian Thanksgiving was moved due to the General
            # Election falling on the second Monday of October
            # http://tiny.cc/can_thkgvg
            if self._year == 1935:
                self._add_holiday_oct_25(name)
            else:
                self._add_holiday_2nd_mon_of_oct(name)

    def _populate_subdiv_ab_public_holidays(self):
        if self._year >= 1990:
            # Family Day.
            self._add_holiday_3rd_mon_of_feb(tr("Family Day"))

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1879:
            self._add_observed(self._canada_day, rule=SUN_TO_NEXT_MON)

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

    def _populate_subdiv_ab_optional_holidays(self):
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # https://en.wikipedia.org/wiki/Civic_Holiday#Alberta
        if self._year >= 1974:
            # Heritage Day.
            self._add_holiday_1st_mon_of_aug(tr("Heritage Day"))

        if self._year >= 2021:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        # Boxing Day.
        self._add_christmas_day_two(tr("Boxing Day"))

    def _populate_subdiv_bc_public_holidays(self):
        if self._year >= 2013:
            name = tr("Family Day")
            if self._year >= 2019:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_2nd_mon_of_feb(name)

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1879:
            self._add_observed(self._canada_day, rule=SUN_TO_NEXT_MON)

        # https://en.wikipedia.org/wiki/Civic_Holiday#British_Columbia
        if self._year >= 1974:
            # British Columbia Day.
            self._add_holiday_1st_mon_of_aug(tr("British Columbia Day"))

        if self._year >= 2023:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _populate_subdiv_mb_public_holidays(self):
        if self._year >= 2008:
            # Louis Riel Day.
            self._add_holiday_3rd_mon_of_feb(tr("Louis Riel Day"))

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        self._add_thanksgiving_day()

    def _populate_subdiv_mb_optional_holidays(self):
        if self._year >= 1900:
            name = (
                # Terry Fox Day.
                tr("Terry Fox Day")
                if self._year >= 2015
                # Civic Holiday.
                else tr("Civic Holiday")
            )
            self._add_holiday_1st_mon_of_aug(name)

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _populate_subdiv_nb_public_holidays(self):
        if self._year >= 2018:
            # Family Day.
            self._add_holiday_3rd_mon_of_feb(tr("Family Day"))

        # https://en.wikipedia.org/wiki/Civic_Holiday#New_Brunswick
        if self._year >= 1975:
            # New Brunswick Day.
            self._add_holiday_1st_mon_of_aug(tr("New Brunswick Day"))

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _populate_subdiv_nb_optional_holidays(self):
        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        self._add_thanksgiving_day()

        # Boxing Day.
        self._add_christmas_day_two(tr("Boxing Day"))

    def _populate_subdiv_nl_public_holidays(self):
        if self._year >= 1917:
            # Memorial Day.
            self._add_holiday_jul_1(tr("Memorial Day"))

        if self._year >= 1879:
            self._add_observed(self._canada_day)

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

    def _populate_subdiv_nl_optional_holidays(self):
        if self._year >= 1900:
            # St. Patrick's Day.
            self._add_holiday(tr("St. Patrick's Day"), self._get_nearest_monday(MAR, 17))

        if self._year >= 1990:
            # Nearest Monday to April 23
            # 4/26 is the Monday closer to 4/23 in 2010
            # but the holiday was observed on 4/19? Crazy Newfies!
            dt = date(2010, APR, 19) if self._year == 2010 else self._get_nearest_monday(APR, 23)
            # St. George's Day.
            self._add_holiday(tr("St. George's Day"), dt)

        if self._year >= 1997:
            # Discovery Day.
            self._add_holiday(tr("Discovery Day"), self._get_nearest_monday(JUN, 24))

        if self._year >= 1900:
            # Orangemen's Day.
            self._add_holiday(tr("Orangemen's Day"), self._get_nearest_monday(JUL, 12))

        self._add_thanksgiving_day()

        # Boxing Day.
        self._add_christmas_day_two(tr("Boxing Day"))

    def _populate_subdiv_ns_public_holidays(self):
        # http://novascotia.ca/lae/employmentrights/NovaScotiaHeritageDay.asp
        if self._year >= 2015:
            # Heritage Day.
            self._add_holiday_3rd_mon_of_feb(tr("Heritage Day"))

        if self._year >= 1981:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

    def _populate_subdiv_ns_optional_holidays(self):
        if self._year >= 1996:
            # Natal Day.
            self._add_holiday_1st_mon_of_aug(tr("Natal Day"))

    def _populate_subdiv_nt_public_holidays(self):
        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1996:
            # National Aboriginal Day.
            self._add_holiday_jun_21(tr("National Aboriginal Day"))

        if self._year >= 1900:
            # Civic Holiday.
            self._add_holiday_1st_mon_of_aug(tr("Civic Holiday"))

        if self._year >= 2022:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _populate_subdiv_nu_public_holidays(self):
        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1900:
            # Civic Holiday.
            self._add_holiday_1st_mon_of_aug(tr("Civic Holiday"))

        if self._year >= 2022:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_remembrance_day(tr("Remembrance Day"))

    def _populate_subdiv_nu_optional_holidays(self):
        if self._year >= 2000:
            # Nunavut Day.
            name = tr("Nunavut Day")
            if self._year == 2000:
                self._add_holiday_apr_1(name)
            else:
                self._add_holiday_jul_9(name)

    def _populate_subdiv_on_public_holidays(self):
        if self._year >= 2008:
            # Family Day.
            self._add_holiday_3rd_mon_of_feb(tr("Family Day"))

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        self._add_thanksgiving_day()

        self._add_observed(self._add_christmas_day_two(tr("Boxing Day")), rule=SUN_TO_NEXT_TUE)

    def _populate_subdiv_on_optional_holidays(self):
        if self._year >= 1900:
            # Civic Holiday.
            self._add_holiday_1st_mon_of_aug(tr("Civic Holiday"))

    def _populate_subdiv_pe_public_holidays(self):
        if self._year >= 2009:
            # Islander Day.
            name = tr("Islander Day")
            if self._year >= 2010:
                self._add_holiday_3rd_mon_of_feb(name)
            else:
                self._add_holiday_2nd_mon_of_feb(name)

        if self._year >= 1879:
            self._add_observed(self._canada_day)

        if self._year >= 2022:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

    def _populate_subdiv_qc_public_holidays(self):
        if self._year >= 2003:
            # National Patriots' Day.
            self._add_holiday_1st_mon_before_may_24(tr("National Patriots' Day"))

        if self._year >= 1925:
            self._add_observed(
                # St. Jean Baptiste Day.
                self._add_saint_johns_day(tr("St. Jean Baptiste Day")),
                rule=SUN_TO_NEXT_MON,
            )

        if self._year >= 1879:
            self._add_observed(self._canada_day, rule=SUN_TO_NEXT_MON)

        self._add_thanksgiving_day()

    def _populate_subdiv_qc_optional_holidays(self):
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

    def _populate_subdiv_sk_public_holidays(self):
        if self._year >= 2007:
            # Family Day.
            self._add_holiday_3rd_mon_of_feb(tr("Family Day"))

        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 1879:
            self._add_observed(self._canada_day)

        # https://en.wikipedia.org/wiki/Civic_Holiday#Saskatchewan
        if self._year >= 1900:
            # Saskatchewan Day.
            self._add_holiday_1st_mon_of_aug(tr("Saskatchewan Day"))

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

    def _populate_subdiv_yt_public_holidays(self):
        if self._year >= 1953:
            # Victoria Day.
            self._add_holiday_1st_mon_before_may_24(tr("Victoria Day"))

        if self._year >= 2017:
            # National Aboriginal Day.
            self._add_holiday_jun_21(tr("National Aboriginal Day"))

        if self._year >= 1879:
            self._add_observed(self._canada_day)

        if self._year >= 1912:
            # Discovery Day.
            self._add_holiday_3rd_mon_of_aug(tr("Discovery Day"))

        if self._year >= 2023:
            # National Day for Truth and Reconciliation.
            self._add_holiday_sep_30(tr("National Day for Truth and Reconciliation"))

        self._add_thanksgiving_day()

        if self._year >= 1931:
            # Remembrance Day.
            self._add_observed(self._add_remembrance_day(tr("Remembrance Day")))

    def _populate_subdiv_yt_optional_holidays(self):
        # Friday before the last Sunday in February
        if self._year >= 1976:
            self._add_holiday_2_days_prior_last_sun_of_feb(tr("Heritage Day"))


class CaStaticHolidays:
    # Funeral of Queen Elizabeth II.
    queen_funeral = tr("Funeral of Her Majesty the Queen Elizabeth II")

    special_bc_public_holidays = {
        2022: (SEP, 19, queen_funeral),
    }

    special_nb_public_holidays = {
        2022: (SEP, 19, queen_funeral),
    }

    special_nl_public_holidays = {
        2022: (SEP, 19, queen_funeral),
    }

    special_ns_public_holidays = {
        2022: (SEP, 19, queen_funeral),
    }

    special_pe_public_holidays = {
        2022: (SEP, 19, queen_funeral),
    }

    special_yt_public_holidays = {
        2022: (SEP, 19, queen_funeral),
    }
