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

from dateutil.easter import easter

from holidays.calendars import _get_nth_weekday_from, _get_nth_weekday_of_month
from holidays.constants import JAN, FEB, MAR, APR, JUN, JUL, SEP, OCT, NOV
from holidays.constants import DEC, MON, TUE, WED
from holidays.holiday_base import HolidayBase


class NewZealand(HolidayBase):
    country = "NZ"
    special_holidays = {2022: ((SEP, 26, "Queen Elizabeth II Memorial Day"),)}
    subdivisions = [
        # https://en.wikipedia.org/wiki/ISO_3166-2:NZ
        "AUK",  # Auckland / Tāmaki-makau-rau
        # "BOP",  # Bay of Plenty / Te Moana a Toi Te Huatahi
        "CAN",  # Canterbury / Waitaha
        # "GIS",  # Gisborne / Tūranga nui a Kiwa
        "HKB",  # Hawke's Bay / Te Matau a Māui
        "MBH",  # Marlborough
        # "MWT",  # Manawatu-Wanganui
        "NSN",  # Nelson / Whakatū
        "NTL",  # Northland / Te Tai tokerau
        "OTA",  # Otago / Ō Tākou
        "STL",  # Southland / Murihiku
        # "TAS",  # Tasman
        "TKI",  # Taranaki
        # "WKO",  # Waikato
        "WGN",  # Wellington / Te Whanga-nui-a-Tara
        "WTC",  # West Coast / Te Taihau ā uru
        "CIT",  # Chatham Islands Territory / Wharekauri
        "South Canterbury",
    ]
    _deprecated_subdivisions = [
        "Auckland",
        "Canterbury",
        "Chatham Islands",
        "Hawke's Bay",
        "Marlborough",
        "Northland",
        "Nelson",
        "Otago",
        "South Canterbury",
        "Southland",
        "Taranaki",
        "Waitangi",
        "Wellington",
        "West Coast",
        "Westland",  # Correct name is West Coast
        "WTL",  # Correct code is WTC
    ]

    def _get_nearest_monday(self, dt: date) -> date:
        return _get_nth_weekday_from(
            1 if self._is_friday(dt) or self._is_weekend(dt) else -1, MON, dt
        )

    def _add_observed(self, dt: date) -> None:
        if self.observed and self._is_weekend(dt):
            obs_date = _get_nth_weekday_from(1, MON, dt)
            if self.get(obs_date):
                obs_date += td(days=+1)
            self[obs_date] = f"{self[dt]} (Observed)"

    def _populate(self, year):
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

        if year <= 1893:
            return None

        super()._populate(year)

        # New Year's Day
        jan1 = date(year, JAN, 1)
        self[jan1] = "New Year's Day"

        jan2 = date(year, JAN, 2)
        self[jan2] = "Day after New Year's Day"
        self._add_observed(jan1)
        self._add_observed(jan2)

        # Waitangi Day
        if year >= 1974:
            name = "New Zealand Day"
            if year >= 1977:
                name = "Waitangi Day"
            feb6 = date(year, FEB, 6)
            self[feb6] = name
            if year >= 2014:
                self._add_observed(feb6)

        # Anzac Day
        if year >= 1921:
            apr25 = date(year, APR, 25)
            self[apr25] = "Anzac Day"
            if year >= 2014:
                self._add_observed(apr25)

        # Easter
        easter_date = easter(year)
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date + td(days=+1)] = "Easter Monday"

        # Sovereign's Birthday
        if year >= 1902:
            name = "King's Birthday"
            if 1952 <= year <= 2022:
                name = "Queen's Birthday"
            if year == 1952:
                self[date(year, JUN, 2)] = name  # Elizabeth II
            elif year >= 1938:
                self[
                    _get_nth_weekday_of_month(1, MON, JUN, year)
                ] = name  # EII & GVI
            elif year == 1937:
                self[date(year, JUN, 9)] = name  # George VI
            elif year == 1936:
                self[date(year, JUN, 23)] = name  # Edward VIII
            elif year >= 1912:
                self[date(year, JUN, 3)] = name  # George V
            else:
                # http://paperspast.natlib.govt.nz/cgi-bin/paperspast?a=d&d=NZH19091110.2.67
                self[date(year, NOV, 9)] = name  # Edward VII

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
        if year in dates_obs:
            self[date(year, *dates_obs[year])] = "Matariki"

        # Labour Day
        name = "Labour Day"
        if year >= 1910:
            self[_get_nth_weekday_of_month(4, MON, OCT, year)] = name
        elif year >= 1900:
            self[_get_nth_weekday_of_month(2, WED, OCT, year)] = name

        # Christmas Day
        dec25 = date(year, DEC, 25)
        self[dec25] = "Christmas Day"

        # Boxing Day
        dec26 = date(year, DEC, 26)
        self[dec26] = "Boxing Day"
        self._add_observed(dec25)
        self._add_observed(dec26)

        # Province Anniversary Day
        if self.subdiv in {"Auckland", "AUK", "Northland", "NTL"}:
            if 1964 <= year <= 1973 and self.subdiv in {"Northland", "NTL"}:
                name = "Waitangi Day"
                dt = date(year, FEB, 6)
            else:
                name = "Auckland Anniversary Day"
                dt = date(year, JAN, 29)
            self[self._get_nearest_monday(dt)] = name

        elif self.subdiv in {"New Plymouth", "Taranaki", "TKI"}:
            self[
                _get_nth_weekday_of_month(2, MON, MAR, year)
            ] = "Taranaki Anniversary Day"

        elif self.subdiv in {"Hawke's Bay", "HKB"}:
            self[
                _get_nth_weekday_of_month(4, MON, OCT, year) + td(days=-3)
            ] = "Hawke's Bay Anniversary Day"

        elif self.subdiv in {"WGN", "Wellington"}:
            self[
                self._get_nearest_monday(date(year, JAN, 22))
            ] = "Wellington Anniversary Day"

        elif self.subdiv in {"Marlborough", "MBH"}:
            self[
                _get_nth_weekday_of_month(4, MON, OCT, year) + td(days=+7)
            ] = "Marlborough Anniversary Day"

        elif self.subdiv in {"Nelson", "NSN"}:
            self[
                self._get_nearest_monday(date(year, FEB, 1))
            ] = "Nelson Anniversary Day"

        elif self.subdiv in {"CAN", "Canterbury"}:
            self[
                _get_nth_weekday_of_month(1, TUE, NOV, year) + td(days=+10)
            ] = "Canterbury Anniversary Day"

        elif self.subdiv in {"South Canterbury", "STC"}:
            self[
                _get_nth_weekday_of_month(4, MON, SEP, year)
            ] = "South Canterbury Anniversary Day"

        elif self.subdiv in {"WTC", "West Coast", "WTL", "Westland"}:
            name = "West Coast Anniversary Day"
            # Observance varies?!?!
            if year == 2005:  # special case?!?!
                self[date(year, DEC, 5)] = name
            else:
                self[self._get_nearest_monday(date(year, DEC, 1))] = name

        elif self.subdiv in {"OTA", "Otago"}:
            # there is no easily determined single day of local observance?!?!
            dt = self._get_nearest_monday(date(year, MAR, 23))
            if dt == easter_date + td(days=+1):  # Avoid Easter Monday
                dt += td(days=+1)
            self[dt] = "Otago Anniversary Day"

        elif self.subdiv in {"STL", "Southland"}:
            name = "Southland Anniversary Day"
            if year >= 2012:
                self[easter_date + td(days=+2)] = name
            else:
                self[self._get_nearest_monday(date(year, JAN, 17))] = name

        elif self.subdiv in {"CIT", "Chatham Islands"}:
            self[
                self._get_nearest_monday(date(year, NOV, 30))
            ] = "Chatham Islands Anniversary Day"


class NZ(NewZealand):
    pass


class NZL(NewZealand):
    pass
