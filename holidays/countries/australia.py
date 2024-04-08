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

from datetime import timedelta as td

from holidays.calendars.gregorian import JAN, APR, JUN, AUG, SEP, OCT, DEC
from holidays.constants import BANK, HALF_DAY, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    SUN_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class Australia(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    """
    References:
      - https://www.qld.gov.au/recreation/travel/holidays
      - `ACT Holidays Act 1958 <https://www.legislation.act.gov.au/a/1958-19>`_
      - `ACT 2013-2023 <https://www.cmtedd.act.gov.au/archived-content/holidays/previous-years>`_
      - `NSW Banks and Bank Holidays Act 1912 <https://legislation.nsw.gov.au/view/html/repealed/current/act-1912-043>`_
      - `NSW Public Holidays Act 2010 <https://legislation.nsw.gov.au/view/html/inforce/current/act-2010-115>`_
      - `NT Public Holidays Act 1981 <https://legislation.nt.gov.au/api/sitecore/Act/PDF?id=12145>`_
      - `QLD Holidays Act 1983 <https://www.legislation.qld.gov.au/view/html/inforce/current/act-1983-018>`_
      - `QLD 2012-2024 <https://www.qld.gov.au/recreation/travel/holidays/public>`_
      - `SA Holidays Act 1910 <https://www.legislation.sa.gov.au/LZ/C/A/HOLIDAYS%20ACT%201910.aspx>`_
      - `SA Public Holidays Act 2023 <https://www.legislation.sa.gov.au/LZ/C/A/Public%20Holidays%20Act%202023.aspx>`_
      - `SA 2023-2024 <https://www.safework.sa.gov.au/resources/public-holidays>`_
      - `SA 2007-2021 <https://safework.sa.gov.au/__data/assets/pdf_file/0007/235474/Public-Holidays-since-2007.pdf>`_
      - `TAS Statutory Holidays Act 2000 <https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096>`_
      - `VIC Public Holidays Act 1993 <https://www.legislation.vic.gov.au/in-force/acts/public-holidays-act-1993/027>`_
      - `VIC Minister appointment <https://www.gazette.vic.gov.au/gazette/Gazettes2015/GG2015S229.pdf>`_
      - `VIC 2018-2024 <https://business.vic.gov.au/business-information/public-holidays>`_
      - `WA Public and Bank Holidays Act 1972 <https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_a639.html>`_
      - `WA 2019-2023 <https://www.commerce.wa.gov.au/labour-relations/previous-years-public-holiday-dates>`_
    """

    country = "AU"
    supported_categories = (BANK, HALF_DAY, PUBLIC)
    observed_label = "%s (observed)"
    subdivisions = ("ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA")
    subdivisions_aliases = {
        "Australian Capital Territory": "ACT",
        "New South Wales": "NSW",
        "Northern Territory": "NT",
        "Queensland": "QLD",
        "South Australia": "SA",
        "Tasmania": "TAS",
        "Victoria": "VIC",
        "Western Australia": "WA",
    }

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
        StaticHolidays.__init__(self, AustraliaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Sovereign's Birthday.
        if 1902 <= self._year <= 1935:
            if self._year >= 1912:
                self._add_holiday_jun_3(self.sovereign_birthday)  # George V
            else:
                self._add_holiday_nov_9(self.sovereign_birthday)  # Edward VII

        if self.subdiv:
            return None

        # Common holidays.

        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # Australia Day.
        if self._year >= 1935:
            self._add_holiday_jan_26("Australia Day")

        # ANZAC Day.
        if self._year >= 1921:
            self._add_anzac_day("ANZAC Day")

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Boxing Day.
        self._add_christmas_day_two("Boxing Day")

    def _populate_subdiv_act_public_holidays(self):
        # New Year's Day.
        # 1959-1992: SUN - move to MON.
        # 1993-2014: SAT, SUN - move to MON.
        # from 2015: SAT, SUN - add MON.

        # New Year's Day.
        name = "New Year's Day"
        if self._year >= 2015:
            self._add_observed(self._add_new_years_day(name))
        elif self._year >= 1959:
            jan_1 = (JAN, 1)
            if self._is_sunday(jan_1) or (self._year >= 1993 and self._is_saturday(jan_1)):
                self._add_holiday_1st_mon_from_jan_1(name)
            else:
                self._add_new_years_day(name)
        else:
            self._add_new_years_day(name)

        # Australia Day.
        # 1959-1989: not MON - move to MON.
        # from 1990: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1935 else "Anniversary Day"
            if 1959 <= self._year <= 1989 or (self._year >= 1990 and self._is_weekend(JAN, 26)):
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Canberra Day.
        if self._year >= 1913:
            name = "Canberra Day"
            if self._year <= 1958 or self._year == 2012:
                self._add_holiday_mar_12(name)
            elif self._year <= 2007:
                self._add_holiday_3rd_mon_of_mar(name)
            else:
                self._add_holiday_2nd_mon_of_mar(name)

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Sunday.
        if self._year >= 2016:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        # from 1959: SUN - move to MON.

        # ANZAC Day.
        if self._year >= 1921:
            name = "ANZAC Day"
            if self._year >= 1959 and self._is_sunday(APR, 25):
                self._add_holiday_1st_mon_from_apr_25(name)
            else:
                self._add_anzac_day(name)

        # Reconciliation Day.
        if self._year >= 2018:
            self._add_holiday_1st_mon_from_may_27("Reconciliation Day")

        # Sovereign's Birthday.
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Family & Community Day.
        # (First Monday of the September/October school holidays;
        # moved to the second Monday if this falls on Labour day).
        if 2010 <= self._year <= 2017:
            fc_dates = {
                2010: (SEP, 26),
                2011: (OCT, 10),
                2012: (OCT, 8),
                2013: (SEP, 30),
                2014: (SEP, 29),
                2015: (SEP, 28),
                2016: (SEP, 26),
                2017: (SEP, 25),
            }
            self._add_holiday("Family & Community Day", fc_dates[self._year])

        # Labour Day.
        self._add_holiday_1st_mon_of_oct("Labour Day")

        # Christmas Day.
        # 1958-1991: SUN - to MON.
        # 1992-2013: SAT, SUN - to MON.
        # from 2014: SAT - add MON, SUN - add TUE.

        # Christmas Day.
        name = "Christmas Day"
        if self._year >= 2014:
            self._add_observed(self._add_christmas_day(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 1958:
            dec_25 = (DEC, 25)
            if self._is_weekend(dec_25) or (self._year >= 1992 and self._is_saturday(dec_25)):
                self._add_holiday_1st_mon_from_dec_25(name)
            else:
                self._add_christmas_day(name)
        else:
            self._add_christmas_day(name)

        # Boxing Day.
        # 1958-1991: SUN - to MON, MON - to TUE.
        # 1992-2013: SAT - to MON, SUN - to TUE, MON - to TUE.
        # from 2014: SAT - add MON, SUN - add TUE.

        # Boxing Day.
        name = "Boxing Day"
        if self._year >= 2014:
            self._add_observed(self._add_christmas_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 1958:
            dec_26 = (DEC, 26)
            if self._year >= 1992:
                if self._is_saturday(dec_26):
                    self._add_holiday_1st_mon_from_dec_26(name)
                elif self._is_sunday(dec_26) or self._is_monday(dec_26):
                    self._add_holiday_1st_tue_from_dec_26(name)
                else:
                    self._add_christmas_day_two(name)
            else:
                if self._is_sunday(dec_26):
                    self._add_holiday_1st_mon_from_dec_26(name)
                elif self._is_monday(dec_26):
                    self._add_holiday_1st_tue_from_dec_26(name)
                else:
                    self._add_christmas_day_two(name)
        else:
            self._add_christmas_day_two(name)

    def _populate_subdiv_act_bank_holidays(self):
        # Bank Holiday.
        self._add_holiday_1st_mon_of_aug("Bank Holiday")

    def _populate_subdiv_nsw_public_holidays(self):
        # New Year's Day.
        # 1912-2010: SUN - add MON.
        # from 2011: SAT, SUN - add MON.

        # New Year's Day.
        self._add_observed(
            self._add_new_years_day("New Year's Day"),
            rule=SAT_SUN_TO_NEXT_MON if self._year >= 2011 else SUN_TO_NEXT_MON,
        )

        # Australia Day.
        # 1912-2010: SUN - add MON.
        # from 2011: SAT, SUN - to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1946 else "Anniversary Day"
            if self._year >= 2011:
                if self._is_weekend(JAN, 26):
                    self._add_holiday_1st_mon_from_jan_26(name)
                else:
                    self._add_holiday_jan_26(name)
            else:
                self._add_observed(self._add_holiday_jan_26(name), rule=SUN_TO_NEXT_MON)

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Sunday.
        if self._year >= 2011:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        # 1912-2010: SUN - add MON.
        # from 2011: normal.

        # ANZAC Day.
        if self._year >= 1921:
            apr_25 = self._add_anzac_day("ANZAC Day")
            if self._year <= 2010:
                self._add_observed(apr_25)

        # Labour Day.
        self._add_holiday_1st_mon_of_oct("Labour Day")

        # Sovereign's Birthday.
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Bank Holiday.
        if 1912 <= self._year <= 2010:
            self._add_holiday_1st_mon_of_aug("Bank Holiday")

        # Christmas Day.
        # 1912-2010: SUN - add TUE.
        # from 2011: SAT - add MON, SUN - add TUE.

        # Christmas Day.
        self._add_observed(
            self._add_christmas_day("Christmas Day"),
            rule=SAT_SUN_TO_NEXT_MON_TUE if self._year >= 2011 else SUN_TO_NEXT_TUE,
        )

        # Boxing Day.
        # 1912-2010: SUN - add MON.
        # from 2011: SAT - add MON, SUN - add TUE.

        # Boxing Day.
        self._add_observed(
            self._add_christmas_day_two("Boxing Day"),
            rule=SAT_SUN_TO_NEXT_MON_TUE if self._year >= 2011 else SUN_TO_NEXT_MON,
        )

    def _populate_subdiv_nsw_bank_holidays(self):
        # Bank Holiday.
        if self._year >= 2011:
            self._add_holiday_1st_mon_of_aug("Bank Holiday")

    def _populate_subdiv_nt_public_holidays(self):
        # New Year's Day.
        # 1982-2016: SAT, SUN - move to MON.
        # from 2017: SAT, SUN - add MON.

        # New Year's Day.
        name = "New Year's Day"
        if self._year >= 2017:
            self._add_observed(self._add_new_years_day(name))
        elif self._year >= 1982 and self._is_weekend(JAN, 1):
            self._add_holiday_1st_mon_from_jan_1(name)
        else:
            self._add_new_years_day(name)

        # Australia Day.
        # from 1982: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1935 else "Anniversary Day"
            if self._year >= 1982 and self._is_weekend(JAN, 26):
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Sunday.
        if self._year >= 2024:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        # from 1982: SUN - to MON.

        # ANZAC Day.
        if self._year >= 1921:
            name = "ANZAC Day"
            if self._year >= 1982 and self._is_sunday(APR, 25):
                self._add_holiday_1st_mon_from_apr_25(name)
            else:
                self._add_anzac_day(name)

        # Labour Day.
        self._add_holiday_1st_mon_of_may("May Day")

        # Sovereign's Birthday.
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Picnic Day.
        self._add_holiday_1st_mon_of_aug("Picnic Day")

        # Christmas Day.
        # 1981-2015: SAT, SUN - to MON.
        # from 2016: SAT, SUN - add MON.

        # Christmas Day.
        name = "Christmas Day"
        if self._year >= 2016:
            self._add_observed(self._add_christmas_day(name))
        elif self._year >= 1981 and self._is_weekend(DEC, 25):
            self._add_holiday_1st_mon_from_dec_25(name)
        else:
            self._add_christmas_day(name)

        # Boxing Day.
        # 1981-2022: SAT - to MON, SUN - to TUE, MON - to TUE.
        # from 2023: SAT - add MON, SUN - add TUE, MON - add TUE.
        name = "Boxing Day"
        if self._year >= 2023:
            self._add_observed(
                self._add_christmas_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE
            )
        elif self._year >= 1981:
            dec_26 = (DEC, 26)
            if self._is_saturday(dec_26):
                self._add_holiday_1st_mon_from_dec_26(name)
            elif self._is_sunday(dec_26) or self._is_monday(dec_26):
                self._add_holiday_1st_tue_from_dec_26(name)
            else:
                self._add_christmas_day_two(name)
        else:
            self._add_christmas_day_two(name)

    def _populate_subdiv_nt_half_day_holidays(self):
        if self._year >= 2016:
            begin_time_label = "%s (from 7pm)"

            # Christmas Eve.
            self._add_christmas_eve(begin_time_label % "Christmas Eve")

            # New Year's Eve.
            self._add_new_years_eve(begin_time_label % "New Year's Eve")

    def _populate_subdiv_qld_public_holidays(self):
        # New Year's Day.
        # 1984-2011: SUN - move to MON.
        # from 2012: SAT, SUN - add MON.

        # New Year's Day.
        name = "New Year's Day"
        if self._year >= 2012:
            self._add_observed(self._add_new_years_day(name))
        elif self._year >= 1984 and self._is_sunday(JAN, 1):
            self._add_holiday_1st_mon_from_jan_1(name)
        else:
            self._add_new_years_day(name)

        # Australia Day.
        # 1984-1995: not MON - move to MON.
        # from 1996: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1935 else "Anniversary Day"
            if 1984 <= self._year <= 1995 or (self._year >= 1996 and self._is_weekend(JAN, 26)):
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Sunday.
        if self._year >= 2017:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        # from 1984: SUN - move to MON.

        # ANZAC Day.
        if self._year >= 1921:
            name = "ANZAC Day"
            if self._year >= 1984 and self._is_sunday(APR, 25):
                self._add_holiday_1st_mon_from_apr_25(name)
            else:
                self._add_anzac_day(name)

        # Labour Day.
        name = "Labour Day"
        if 2013 <= self._year <= 2015:
            self._add_holiday_1st_mon_of_oct(name)
        else:
            self._add_holiday_1st_mon_of_may(name)

        # Sovereign's Birthday.
        if self._year >= 1936:
            if self._year <= 2015 and self._year != 2012:
                self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)
            else:
                self._add_holiday_1st_mon_of_oct(self.sovereign_birthday)

        # The Royal Queensland Show (Ekka).
        # The Show starts on the first Friday of August - providing this is
        # not prior to the 5th - in which case it will begin on the second
        # Friday. The Wednesday during the show is a public holiday.
        ekka_dates = {
            2020: (AUG, 14),
            2021: (OCT, 29),
        }
        name = "The Royal Queensland Show"
        if self._year in ekka_dates:
            self._add_holiday(name, ekka_dates[self._year])
        else:
            # [1st FRI after Aug 5] + 5 days = [1st WED after Aug 10]
            self._add_holiday_1st_wed_from_aug_10(name)

        # Christmas Day.
        # 1984-2010: SUN - to MON.
        # from 2011: SAT - add MON, SUN - add TUE.

        # Christmas Day.
        name = "Christmas Day"
        if self._year >= 2011:
            self._add_observed(self._add_christmas_day(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 1984 and self._is_sunday(DEC, 25):
            self._add_holiday_1st_mon_from_dec_25(name)
        else:
            self._add_christmas_day(name)

        # Boxing Day.
        # 1984-1910: SUN - to MON, MON - to TUE.
        # from 2011: SAT - add MON, SUN - add TUE.

        # Boxing Day.
        name = "Boxing Day"
        if self._year >= 2011:
            self._add_observed(self._add_christmas_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 1984:
            dec_26 = (DEC, 26)
            if self._is_sunday(dec_26):
                self._add_holiday_1st_mon_from_dec_26(name)
            elif self._is_monday(dec_26):
                self._add_holiday_1st_tue_from_dec_26(name)
            else:
                self._add_christmas_day_two(name)
        else:
            self._add_christmas_day_two(name)

    def _populate_subdiv_sa_public_holidays(self):
        # New Year's Day.
        # 1984-2003: SAT, SUN - move to MON.
        # 2004-2023: SAT - move to MON, SUN - add MON.
        # from 2024: SAT, SUN - add MON.

        # New Year's Day.
        name = "New Year's Day"
        jan_1 = (JAN, 1)
        if self._year >= 2024:
            self._add_observed(self._add_new_years_day(name))
        elif self._year >= 2004:
            if self._is_saturday(jan_1):
                self._add_holiday_1st_mon_from_jan_1(name)
            else:
                self._add_observed(self._add_new_years_day(name), rule=SUN_TO_NEXT_MON)
        elif self._year >= 1984 and self._is_weekend(jan_1):
            self._add_holiday_1st_mon_from_jan_1(name)
        else:
            self._add_new_years_day(name)

        # Australia Day.
        # 1984-1993: not MON - move to MON.
        # 1994-2003: SAT, SUN - move to MON.
        # 2004-2023: SAT - move to MON, SUN - add MON.
        # from 2024: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1935:
            name = "Australia Day"
            jan_26 = (JAN, 26)
            if 1994 <= self._year <= 2003 or self._year >= 2024:
                if self._is_weekend(jan_26):
                    self._add_holiday_1st_mon_from_jan_26(name)
                else:
                    self._add_holiday_jan_26(name)
            elif self._year >= 2004:
                if self._is_saturday(jan_26):
                    self._add_holiday_1st_mon_from_jan_26(name)
                else:
                    self._add_observed(self._add_holiday_jan_26(name), rule=SUN_TO_NEXT_MON)
            elif self._year >= 1984:
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Adelaide Cup Day.
        # 2006-2023: changed each year by SA Government Proclamation from the 3rd Monday in May
        # to the 2nd Monday in March.
        # from 2024: changed to the 2nd Monday in March officially.

        # Adelaide Cup Day.
        name = "Adelaide Cup Day"
        if self._year >= 2006:
            self._add_holiday_2nd_mon_of_mar(name)
        else:
            self._add_holiday_3rd_mon_of_may(name)

        # Easter Saturday.
        self._add_holy_saturday("Easter Saturday")

        # Easter Sunday.
        if self._year >= 2024:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        if self._year >= 1921:
            apr_25 = self._add_anzac_day("ANZAC Day")
            if self._year <= 2023:
                self._add_observed(apr_25, rule=SUN_TO_NEXT_MON)

        # Sovereign's Birthday.
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Labour Day.
        self._add_holiday_1st_mon_of_oct("Labour Day")

        # Proclamation Day.
        # 1984-1992: SAT, SUN - move to MON.
        # 1993-2002: SAT - to MON, SUN - to TUE, MON - to TUE.
        # 2003-2023: SAT - to MON, SUN - add TUE, MON - add TUE.
        # from 2024: SAT - add MON, SUN - add TUE, MON - add TUE.
        # (Placed before Christmas Day for proper observed calculation).

        # Proclamation Day.
        name = "Proclamation Day"
        dec_26 = (DEC, 26)
        if self._year >= 2024:
            self._add_observed(
                self._add_christmas_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE
            )
        elif self._year >= 2003:
            if self._is_saturday(dec_26):
                self._add_holiday_1st_mon_from_dec_26(name)
            else:
                self._add_observed(
                    self._add_christmas_day_two(name), rule=SUN_TO_NEXT_TUE + MON_TO_NEXT_TUE
                )
        elif self._year >= 1993:
            if self._is_saturday(dec_26):
                self._add_holiday_1st_mon_from_dec_26(name)
            elif self._is_sunday(dec_26) or self._is_monday(dec_26):
                self._add_holiday_1st_tue_from_dec_26(name)
            else:
                self._add_christmas_day_two(name)
        elif self._year >= 1984 and self._is_weekend(dec_26):
            self._add_holiday_1st_mon_from_dec_26(name)
        else:
            self._add_christmas_day_two(name)

        # Christmas Day.
        # 1984-2002: SAT, SUN - move to MON.
        # 2003-2023: SAT - move to MON, SUN - add MON.
        # from 2024: SAT, SUN - add MON.

        # Christmas Day.
        name = "Christmas Day"
        dec_25 = (DEC, 25)
        if self._year >= 2024:
            self._add_observed(self._add_christmas_day(name))
        elif self._year >= 2003:
            if self._is_saturday(dec_25):
                self._add_holiday_1st_mon_from_dec_25(name)
            else:
                self._add_observed(self._add_christmas_day(name), rule=SUN_TO_NEXT_MON)
        elif self._year >= 1984 and self._is_weekend(dec_25):
            self._add_holiday_1st_mon_from_dec_25(name)
        else:
            self._add_christmas_day(name)

    def _populate_subdiv_sa_half_day_holidays(self):
        if self._year >= 2012:
            begin_time_label = "%s (from 7pm)"

            # Christmas Eve.
            self._add_christmas_eve(begin_time_label % "Christmas Eve")

            # New Year's Eve.
            self._add_new_years_eve(begin_time_label % "New Year's Eve")

    def _populate_subdiv_tas_public_holidays(self):
        # New Year's Day.
        # from 2001: SAT, SUN - move to MON.

        # New Year's Day.
        name = "New Year's Day"
        if self._year >= 2001 and self._is_weekend(JAN, 1):
            self._add_holiday_1st_mon_from_jan_1(name)
        else:
            self._add_new_years_day(name)

        # Australia Day.
        # from 2001: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1935 else "Anniversary Day"
            if self._year >= 2001 and self._is_weekend(JAN, 26):
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Labour Day.
        self._add_holiday_2nd_mon_of_mar("Eight Hours Day")

        # Easter Tuesday.
        if self._year <= 2010:
            self._add_holiday("Easter Tuesday", self._easter_sunday + td(days=+2))

        # ANZAC Day.
        if self._year >= 1921:
            self._add_anzac_day("ANZAC Day")

        # Sovereign's Birthday.
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Christmas Day.
        # 2000-2009: SAT - to MON, SUN - to TUE.
        # from 2010: SAT - add MON, SUN - add TUE.

        # Christmas Day.
        name = "Christmas Day"
        if self._year >= 2010:
            self._add_observed(self._add_christmas_day(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 2000:
            dec_25 = (DEC, 25)
            if self._is_saturday(dec_25):
                self._add_holiday_1st_mon_from_dec_25(name)
            elif self._is_sunday(dec_25):
                self._add_holiday_1st_tue_from_dec_25(name)
            else:
                self._add_christmas_day(name)
        else:
            self._add_christmas_day(name)

        # Boxing Day.
        # from 2000: SAT - to MON, SUN - to TUE.

        # Boxing Day.
        name = "Boxing Day"
        if self._year >= 2000:
            dec_26 = (DEC, 26)
            if self._is_saturday(dec_26):
                self._add_holiday_1st_mon_from_dec_26(name)
            elif self._is_sunday(dec_26):
                self._add_holiday_1st_tue_from_dec_26(name)
            else:
                self._add_christmas_day_two(name)
        else:
            self._add_christmas_day_two(name)

    def _populate_subdiv_vic_public_holidays(self):
        # New Year's Day.
        # 1994-1997: SUN - add MON.
        # 1998-2008: SUN - move to MON.
        # from 2009: SAT, SUN - add MON.

        # New Year's Day.
        name = "New Year's Day"
        if self._year >= 2009:
            self._add_observed(self._add_new_years_day(name))
        elif self._year >= 1998:
            if self._is_sunday(JAN, 1):
                self._add_holiday_1st_mon_from_jan_1(name)
            else:
                self._add_new_years_day(name)
        elif self._year >= 1994:
            self._add_observed(self._add_new_years_day(name), rule=SUN_TO_NEXT_MON)
        else:
            self._add_new_years_day(name)

        # Australia Day.
        # from 2009: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1935 else "Anniversary Day"
            if self._year >= 2009 and self._is_weekend(JAN, 26):
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Labour Day.
        self._add_holiday_2nd_mon_of_mar("Labour Day")

        # Easter Saturday.
        if self._year >= 2003:
            self._add_holy_saturday("Easter Saturday")

        # Easter Sunday.
        if self._year >= 2016:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        if self._year >= 1921:
            self._add_anzac_day("ANZAC Day")

        # Sovereign's Birthday.
        if self._year >= 1936:
            self._add_holiday_2nd_mon_of_jun(self.sovereign_birthday)

        # Grand Final Day.
        if self._year >= 2015:
            grand_final_dates = {
                2015: (OCT, 2),
                2016: (SEP, 30),
                # Rescheduled due to COVID-19.
                2020: (OCT, 23),
            }
            name = "Grand Final Day"
            if self._year in grand_final_dates:
                self._add_holiday(name, grand_final_dates[self._year])
            else:
                self._add_holiday_1_day_prior_last_sat_of_sep(name)

        # Melbourne Cup Day.
        if self._year >= 2009:
            self._add_holiday_1st_tue_of_nov("Melbourne Cup Day")

        # Christmas Day.
        # 2008-2018: SAT - to MON, SUN - to TUE.
        # from 2019: SAT - add MON, SUN - add TUE.

        # Christmas Day.
        name = "Christmas Day"
        if self._year >= 2019:
            self._add_observed(self._add_christmas_day(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 2000:
            dec_25 = (DEC, 25)
            if self._is_saturday(dec_25):
                self._add_holiday_1st_mon_from_dec_25(name)
            elif self._is_sunday(dec_25):
                self._add_holiday_1st_tue_from_dec_25(name)
            else:
                self._add_christmas_day(name)
        else:
            self._add_christmas_day(name)

        # Boxing Day.
        # 1994-2008: SUN - to MON.
        # from 2009: SAT - add MON, SUN - add TUE.

        # Boxing Day.
        name = "Boxing Day"
        if self._year >= 2009:
            self._add_observed(self._add_christmas_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        elif self._year >= 1994 and self._is_sunday(DEC, 26):
            self._add_holiday_1st_tue_from_dec_26(name)
        else:
            self._add_christmas_day_two(name)

    def _populate_subdiv_wa_public_holidays(self):
        # New Year's Day.
        # from 1973: SAT, SUN - add MON.

        # New Year's Day.
        jan_1 = self._add_new_years_day("New Year's Day")
        if self._year >= 1973:
            self._add_observed(jan_1)

        # Australia Day.
        # 1973-1993: not MON - move to MON.
        # from 1994: SAT, SUN - move to MON.

        # Australia Day.
        if self._year >= 1888:
            name = "Australia Day" if self._year >= 1935 else "Anniversary Day"
            if self._year >= 1994:
                if self._is_weekend(JAN, 26):
                    self._add_holiday_1st_mon_from_jan_26(name)
                else:
                    self._add_holiday_jan_26(name)
            elif self._year >= 1973:
                self._add_holiday_1st_mon_from_jan_26(name)
            else:
                self._add_holiday_jan_26(name)

        # Labour Day.
        self._add_holiday_1st_mon_of_mar("Labour Day")

        # Easter Sunday.
        if self._year >= 2022:
            self._add_easter_sunday("Easter Sunday")

        # ANZAC Day.
        if self._year >= 1921:
            apr_25 = self._add_anzac_day("ANZAC Day")
            if self._year >= 1973:
                self._add_observed(apr_25)

        # Western Australia Day.
        if self._year >= 1833:
            self._add_holiday_1st_mon_of_jun(
                "Western Australia Day" if self._year >= 2012 else "Foundation Day"
            )

        # Sovereign's Birthday.
        if self._year >= 1936:
            if self._year >= 1984:
                # Celebration Day for the Anniversary of the Birthday of the Reigning Sovereign
                # to be appointed for each year by proclamation published in the Government Gazette
                sovereign_birthday_dates = {
                    2011: (OCT, 28),
                    2012: (OCT, 1),
                    2024: (SEP, 23),
                }
                if self._year in sovereign_birthday_dates:
                    self._add_holiday(
                        self.sovereign_birthday, sovereign_birthday_dates[self._year]
                    )
                else:
                    self._add_holiday_last_mon_of_sep(self.sovereign_birthday)
            else:
                self._add_holiday_2nd_mon_of_oct(self.sovereign_birthday)

        # Boxing Day.
        # 1972-1975: SAT - add MON, SUN - add TUE.
        # from 1976: SAT - add MON, SUN - add TUE, MON - add TUE.
        # (Placed before Christmas Day for proper observed calculation).

        # Boxing Day.
        dec_26 = self._add_christmas_day_two("Boxing Day")
        if self._year >= 1972:
            self._add_observed(
                dec_26,
                rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE
                if self._year >= 1976
                else SAT_SUN_TO_NEXT_MON_TUE,
            )

        # Christmas Day.
        # from 1972: SAT, SUN - add MON.

        # Christmas Day.
        dec_25 = self._add_christmas_day("Christmas Day")
        if self._year >= 1972:
            self._add_observed(dec_25)


class AU(Australia):
    pass


class AUS(Australia):
    pass


class AustraliaStaticHolidays:
    special_public_holidays = {
        2022: (SEP, 22, "National Day of Mourning for Queen Elizabeth II"),
    }

    special_act_public_holidays = {
        2020: (APR, 20, "Declared public holiday"),
        2021: (APR, 25, "Additional public holiday"),
    }

    special_qld_public_holidays = {
        2012: (JUN, 11, "Queen's Diamond Jubilee"),
    }

    special_qld_public_holidays_observed = {
        2010: (DEC, 28, "Christmas Day"),
        2011: (JAN, 3, "New Year's Day"),
    }

    special_wa_public_holidays = {
        # In 2011 both ANZAC Day and Easter Monday fell on Monday 25 April.
        2011: (APR, 26, "Special public holiday"),
    }
