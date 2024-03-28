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
from datetime import timedelta as td

from holidays.calendars.gregorian import JAN, FEB, MAR, JUN, JUL, SEP, NOV, DEC
from holidays.groups import ChristianHolidays, InternationalHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    ALL_TO_NEAREST_MON,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class NewZealand(ObservedHolidayBase, ChristianHolidays, InternationalHolidays, StaticHolidays):
    country = "NZ"
    observed_label = "%s (observed)"
    subdivisions = (
        # https://en.wikipedia.org/wiki/ISO_3166-2:NZ
        "AUK",  # Auckland / Tāmaki-makaurau
        "BOP",  # Bay of Plenty / Toi Moana
        "CAN",  # Canterbury / Waitaha
        "CIT",  # Chatham Islands Territory / Wharekauri
        "GIS",  # Gisborne / Te Tairāwhiti
        "HKB",  # Hawke's Bay / Te Matau a Māui
        "MBH",  # Marlborough
        "MWT",  # Manawatū Whanganui
        "NSN",  # Nelson / Whakatū
        "NTL",  # Northland / Te Tai tokerau
        "OTA",  # Otago / Ō Tākou
        "STL",  # Southland / Te Taiao Tonga
        "TAS",  # Tasman / Te tai o Aorere
        "TKI",  # Taranaki
        "WGN",  # Greater Wellington / Te Pane Matua Taiao
        "WKO",  # Waikato
        "WTC",  # West Coast / Te Tai o Poutini
    )

    _deprecated_subdivisions = (
        "Auckland",
        "Canterbury",
        "Chatham Islands",
        "Hawke's Bay",
        "Marlborough",
        "Nelson",
        "New Plymouth",
        "Northland",
        "Otago",
        "South Canterbury",
        "STC",
        "Southland",
        "Taranaki",
        "Waitangi",
        "Wellington",
        "West Coast",
        "Westland",  # Correct name is West Coast
        "WTL",  # Correct code is WTC
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, NewZelandStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _get_nearest_monday(self, *args) -> date:
        dt = args if len(args) > 1 else args[0]
        dt = dt if isinstance(dt, date) else date(self._year, *dt)
        return self._get_observed_date(dt, rule=ALL_TO_NEAREST_MON)

    def _populate_public_holidays(self):
        # Bank Holidays Act 1873
        # The Employment of Females Act 1873
        # Factories Act 1894
        # Industrial Conciliation and Arbitration Act 1894
        # Labour Day Act 1899
        # Anzac Day Act 1920, 1949, 1956
        # New Zealand Day Act 1973
        # Waitangi Day Act 1960, 1976
        # Sovereign's Birthday Observance Act 1937, 1952
        # Holidays Act 1981, 2003

        if self._year <= 1893:
            return None

        # New Year's Day
        self._add_observed(self._add_new_years_day("New Year's Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)
        self._add_observed(
            self._add_new_years_day_two("Day after New Year's Day"), rule=SAT_SUN_TO_NEXT_MON_TUE
        )

        # Waitangi Day
        if self._year >= 1974:
            name = "Waitangi Day" if self._year >= 1977 else "New Zealand Day"
            feb_6 = self._add_holiday_feb_6(name)
            if self._year >= 2014:
                self._add_observed(feb_6)

        # Anzac Day
        if self._year >= 1921:
            apr_25 = self._add_anzac_day("Anzac Day")
            if self._year >= 2014:
                self._add_observed(apr_25)

        # Easter
        self._add_good_friday("Good Friday")
        self._add_easter_monday("Easter Monday")

        # Sovereign's Birthday
        if self._year >= 1902:
            name = "Queen's Birthday" if 1952 <= self._year <= 2022 else "King's Birthday"
            if self._year == 1952:
                self._add_holiday_jun_2(name)  # Elizabeth II
            elif self._year >= 1938:
                self._add_holiday_1st_mon_of_jun(name)  # EII & GVI
            elif self._year == 1937:
                self._add_holiday_jun_9(name)  # George VI
            elif self._year == 1936:
                self._add_holiday_jun_23(name)  # Edward VIII
            elif self._year >= 1912:
                self._add_holiday_jun_3(name)  # George V
            else:
                # http://paperspast.natlib.govt.nz/cgi-bin/paperspast?a=d&d=NZH19091110.2.67
                self._add_holiday_nov_9(name)  # Edward VII

        # Matariki
        dates_obs = {
            2022: (JUN, 24),
            2023: (JUL, 14),
            2024: (JUN, 28),
            2025: (JUN, 20),
            2026: (JUL, 10),
            2027: (JUN, 25),
            2028: (JUL, 14),
            2029: (JUL, 6),
            2030: (JUN, 21),
            2031: (JUL, 11),
            2032: (JUL, 2),
            2033: (JUN, 24),
            2034: (JUL, 7),
            2035: (JUN, 29),
            2036: (JUL, 18),
            2037: (JUL, 10),
            2038: (JUN, 25),
            2039: (JUL, 15),
            2040: (JUL, 6),
            2041: (JUL, 19),
            2042: (JUL, 11),
            2043: (JUL, 3),
            2044: (JUN, 24),
            2045: (JUL, 7),
            2046: (JUN, 29),
            2047: (JUL, 19),
            2048: (JUL, 3),
            2049: (JUN, 25),
            2050: (JUL, 15),
            2051: (JUN, 30),
            2052: (JUN, 21),
        }
        if self._year in dates_obs:
            self._add_holiday("Matariki", dates_obs[self._year])

        # Labour Day
        if self._year >= 1900:
            name = "Labour Day"
            if self._year >= 1910:
                self._add_holiday_4th_mon_of_oct(name)
            else:
                self._add_holiday_2nd_wed_of_oct(name)

        # Christmas Day
        self._add_observed(self._add_christmas_day("Christmas Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Boxing Day
        self._add_observed(self._add_christmas_day_two("Boxing Day"), rule=SAT_SUN_TO_NEXT_MON_TUE)

        if self.subdiv == "Auckland":
            self._populate_subdiv_auk_public_holidays()
        elif self.subdiv == "Canterbury":
            self._populate_subdiv_can_public_holidays()
        elif self.subdiv == "Chatham Islands":
            self._populate_subdiv_cit_public_holidays()
        elif self.subdiv == "Hawke's Bay":
            self._populate_subdiv_hkb_public_holidays()
        elif self.subdiv == "Marlborough":
            self._populate_subdiv_mbh_public_holidays()
        elif self.subdiv == "Nelson":
            self._populate_subdiv_nsn_public_holidays()
        elif self.subdiv == "Northland":
            self._populate_subdiv_ntl_public_holidays()
        elif self.subdiv == "Otago":
            self._populate_subdiv_ota_public_holidays()
        elif self.subdiv in {"New Plymouth", "Taranaki"}:
            self._populate_subdiv_tki_public_holidays()
        elif self.subdiv == "South Canterbury":
            self._populate_subdiv_stc_public_holidays()
        elif self.subdiv == "Southland":
            self._populate_subdiv_stl_public_holidays()
        elif self.subdiv == "Wellington":
            self._populate_subdiv_wgn_public_holidays()
        elif self.subdiv in {"West Coast", "WTL", "Westland"}:
            self._populate_subdiv_wtc_public_holidays()

    def _populate_subdiv_auk_public_holidays(self):
        self._add_holiday("Auckland Anniversary Day", self._get_nearest_monday(JAN, 29))

    def _populate_subdiv_can_public_holidays(self):
        self._add_holiday_10_days_past_1st_tue_of_nov("Canterbury Anniversary Day")

    def _populate_subdiv_cit_public_holidays(self):
        self._add_holiday("Chatham Islands Anniversary Day", self._get_nearest_monday(NOV, 30))

    def _populate_subdiv_hkb_public_holidays(self):
        self._add_holiday_3_days_prior_4th_mon_of_oct("Hawke's Bay Anniversary Day")

    def _populate_subdiv_mbh_public_holidays(self):
        self._add_holiday_7_days_past_4th_mon_of_oct("Marlborough Anniversary Day")

    def _populate_subdiv_nsn_public_holidays(self):
        self._add_holiday("Nelson Anniversary Day", self._get_nearest_monday(FEB, 1))

    def _populate_subdiv_ntl_public_holidays(self):
        if 1964 <= self._year <= 1973:
            name = "Waitangi Day"
            dt = (FEB, 6)
        else:
            name = "Auckland Anniversary Day"
            dt = (JAN, 29)
        self._add_holiday(name, self._get_nearest_monday(dt))

    def _populate_subdiv_ota_public_holidays(self):
        # there is no easily determined single day of local observance?!?!
        dt = self._get_nearest_monday(MAR, 23)
        if dt == self._easter_sunday + td(days=+1):  # Avoid Easter Monday
            dt += td(days=+1)
        self._add_holiday("Otago Anniversary Day", dt)

    def _populate_subdiv_stc_public_holidays(self):
        self._add_holiday_4th_mon_of_sep("South Canterbury Anniversary Day")

    def _populate_subdiv_stl_public_holidays(self):
        dt = (
            self._easter_sunday + td(days=+2)
            if self._year >= 2012
            else self._get_nearest_monday(JAN, 17)
        )
        self._add_holiday("Southland Anniversary Day", dt)

    def _populate_subdiv_tki_public_holidays(self):
        self._add_holiday_2nd_mon_of_mar("Taranaki Anniversary Day")

    def _populate_subdiv_wgn_public_holidays(self):
        self._add_holiday("Wellington Anniversary Day", self._get_nearest_monday(JAN, 22))

    def _populate_subdiv_wtc_public_holidays(self):
        dt = (
            date(self._year, DEC, 5)
            if self._year == 2005  # special case?!?!
            else self._get_nearest_monday(DEC, 1)
        )
        self._add_holiday("West Coast Anniversary Day", dt)


class NZ(NewZealand):
    pass


class NZL(NewZealand):
    pass


class NewZelandStaticHolidays:
    special_public_holidays = {
        2022: (SEP, 26, "Queen Elizabeth II Memorial Day"),
    }
