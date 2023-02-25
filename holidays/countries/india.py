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

import warnings
from datetime import date
from datetime import timedelta as td

from dateutil.easter import easter

from holidays.calendars import _islamic_to_gre
from holidays.constants import JAN, MAR, APR, MAY, JUN, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class India(HolidayBase):
    """
    https://www.india.gov.in/calendar
    https://www.india.gov.in/state-and-ut-holiday-calendar
    https://en.wikipedia.org/wiki/Public_holidays_in_India
    https://www.calendarlabs.com/holidays/india/2021
    https://slusi.dacnet.nic.in/watershedatlas/list_of_state_abbreviation.htm
    https://vahan.parivahan.gov.in/vahan4dashboard/
    """

    country = "IN"

    subdivisions = [
        "AN",  # Andaman and Nicobar Islands
        "AP",  # Andhra Pradesh
        "AR",  # Arunachal Pradesh
        "AS",  # Assam
        "BR",  # Bihar
        "CG",  # Chhattisgarh
        "CH",  # Chandigarh
        "DD",  # Daman and Diu
        "DH",  # Dadra and Nagar Haveli
        "DL",  # Delhi
        "GA",  # Goa
        "GJ",  # Gujarat
        "HP",  # Himachal Pradesh
        "HR",  # Haryana
        "JH",  # Jharkhand
        "JK",  # Jammu and Kashmir
        "KA",  # Karnataka
        "KL",  # Kerala
        "LA",  # Ladakh
        "LD",  # Lakshadweep
        "MH",  # Maharashtra
        "ML",  # Meghalaya
        "MN",  # Manipur
        "MP",  # Madhya Pradesh
        "MZ",  # Mizoram
        "NL",  # Nagaland
        "OR",  # Orissa / Odisha (Govt sites (dacnet/vahan) use code "OR")
        "PB",  # Punjab
        "PY",  # Pondicherry
        "RJ",  # Rajasthan
        "SK",  # Sikkim
        "TN",  # Tamil Nadu
        "TR",  # Tripura
        "TS",  # Telangana
        "UK",  # Uttarakhand
        "UP",  # Uttar Pradesh
        "WB",  # West Bengal
    ]

    def _populate(self, year):
        super()._populate(year)

        # Pongal/ Makar Sankranti
        self[date(year, JAN, 14)] = "Makar Sankranti / Pongal"

        if year >= 1950:
            # Republic Day
            self[date(year, JAN, 26)] = "Republic Day"

        if year >= 1947:
            # Independence Day
            self[date(year, AUG, 15)] = "Independence Day"

        # Gandhi Jayanti
        self[date(year, OCT, 2)] = "Gandhi Jayanti"

        # Labour Day
        self[date(year, MAY, 1)] = "Labour Day"

        # Christmas
        self[date(year, DEC, 25)] = "Christmas"

        # GJ: Gujarat
        if self.subdiv == "GJ":
            self[date(year, JAN, 14)] = "Uttarayan"
            self[date(year, MAY, 1)] = "Gujarat Day"
            self[date(year, OCT, 31)] = "Sardar Patel Jayanti"

        if self.subdiv == "BR":
            self[date(year, MAR, 22)] = "Bihar Day"

        if self.subdiv == "RJ":
            self[date(year, MAR, 30)] = "Rajasthan Day"
            self[date(year, JUN, 15)] = "Maharana Pratap Jayanti"

        if self.subdiv == "OR":
            self[date(year, APR, 1)] = "Odisha Day (Utkala Dibasa)"
            self[date(year, APR, 15)] = (
                "Maha Vishuva Sankranti / Pana" " Sankranti"
            )

        if self.subdiv in {
            "OR",
            "AP",
            "BR",
            "WB",
            "KL",
            "HR",
            "MH",
            "UP",
            "UK",
            "TN",
        }:
            self[date(year, APR, 14)] = "Dr. B. R. Ambedkar's Jayanti"

        if self.subdiv == "TN":
            self[date(year, APR, 14)] = "Puthandu (Tamil New Year)"
            self[date(year, APR, 15)] = "Puthandu (Tamil New Year)"

        if self.subdiv == "WB":
            self[date(year, APR, 14)] = "Pohela Boishakh"
            self[date(year, APR, 15)] = "Pohela Boishakh"
            self[date(year, MAY, 9)] = "Rabindra Jayanti"

        if self.subdiv == "AS":
            self[date(year, APR, 15)] = "Bihu (Assamese New Year)"

        if self.subdiv == "MH":
            self[date(year, MAY, 1)] = "Maharashtra Day"
            self[date(year, OCT, 15)] = "Dussehra"

        if self.subdiv == "SK":
            self[date(year, MAY, 16)] = "Annexation Day"

        if self.subdiv == "KA":
            self[date(year, NOV, 1)] = "Karnataka Rajyotsava"

        if self.subdiv == "AP":
            self[date(year, NOV, 1)] = "Andhra Pradesh Foundation Day"

        if self.subdiv == "HR":
            self[date(year, NOV, 1)] = "Haryana Foundation Day"

        if self.subdiv == "MP":
            self[date(year, NOV, 1)] = "Madhya Pradesh Foundation Day"

        if self.subdiv == "KL":
            self[date(year, NOV, 1)] = "Kerala Foundation Day"

        if self.subdiv == "CG":
            self[date(year, NOV, 1)] = "Chhattisgarh Foundation Day"

        if self.subdiv == "TS":
            self[date(year, OCT, 6)] = "Bathukamma Festival"
            self[date(year, APR, 6)] = "Eid al-Fitr"

        # Directly lifted Diwali and Holi dates from FBProphet from:
        # https://github.com/facebook/prophet/blob/main/python/prophet/hdays.py
        # Warnings kept in place so that users are aware

        if year < 2001 or year > 2030:
            warning_msg = (
                "Diwali and Holi holidays available from 2001 to 2030 only"
            )
            warnings.warn(warning_msg, Warning)

        # https://www.timeanddate.com/holidays/india/diwali
        diwali_dates = {
            2001: (NOV, 14),
            2002: (NOV, 4),
            2003: (OCT, 25),
            2004: (NOV, 12),
            2005: (NOV, 1),
            2006: (OCT, 21),
            2007: (NOV, 9),
            2008: (OCT, 28),
            2009: (OCT, 17),
            2010: (NOV, 5),
            2011: (OCT, 26),
            2012: (NOV, 13),
            2013: (NOV, 3),
            2014: (OCT, 23),
            2015: (NOV, 11),
            2016: (OCT, 30),
            2017: (OCT, 19),
            2018: (NOV, 7),
            2019: (OCT, 27),
            2020: (NOV, 14),
            2021: (NOV, 4),
            2022: (OCT, 24),
            2023: (NOV, 12),
            2024: (NOV, 1),
            2025: (OCT, 20),
            2026: (NOV, 8),
            2027: (OCT, 29),
            2028: (OCT, 17),
            2029: (NOV, 5),
            2030: (OCT, 26),
        }

        # https://www.timeanddate.com/holidays/india/holi
        holi_dates = {
            2001: (MAR, 10),
            2002: (MAR, 29),
            2003: (MAR, 18),
            2004: (MAR, 7),
            2005: (MAR, 26),
            2006: (MAR, 15),
            2007: (MAR, 4),
            2008: (MAR, 22),
            2009: (MAR, 11),
            2010: (MAR, 1),
            2011: (MAR, 20),
            2012: (MAR, 8),
            2013: (MAR, 27),
            2014: (MAR, 17),
            2015: (MAR, 6),
            2016: (MAR, 24),
            2017: (MAR, 13),
            2018: (MAR, 2),
            2019: (MAR, 21),
            2020: (MAR, 10),
            2021: (MAR, 29),
            2022: (MAR, 18),
            2023: (MAR, 8),
            2024: (MAR, 25),
            2025: (MAR, 14),
            2026: (MAR, 4),
            2027: (MAR, 22),
            2028: (MAR, 11),
            2029: (MAR, 1),
            2030: (MAR, 20),
        }

        if year in diwali_dates:
            hol_date = date(year, *diwali_dates[year])
            self[hol_date] = "Diwali"
        if year in holi_dates:
            hol_date = date(year, *holi_dates[year])
            self[hol_date] = "Holi"

        # Islamic holidays
        # Day of Ashura (10th day of 1st Islamic month)
        name = "Day of Ashura"
        for dt in _islamic_to_gre(year, 1, 10):
            self[dt] = f"{name}* (*estimated)"

        # Mawlid, Birth of the Prophet (12th day of 3rd Islamic month)
        name = "Mawlid"
        for dt in _islamic_to_gre(year, 3, 12):
            self[dt] = f"{name}* (*estimated)"

        # Eid ul-Fitr (1st and 2nd day of 10th Islamic month)
        name = "Eid ul-Fitr"
        for dt in _islamic_to_gre(year, 10, 1):
            self[dt] = f"{name}* (*estimated)"
            self[dt + td(days=+1)] = f"{name}* (*estimated)"

        # Eid al-Adha, i.e., Feast of the Sacrifice
        name = "Eid al-Adha"
        for dt in _islamic_to_gre(year, 12, 10):
            self[dt] = f"{name}* (*estimated)"
            self[dt + td(days=+1)] = f"{name}* (*estimated)"

        # Christian holidays
        easter_date = easter(year)
        self[easter_date + td(days=-7)] = "Palm Sunday"
        self[easter_date + td(days=-2)] = "Good Friday"
        self[easter_date] = "Easter Sunday"
        self[easter_date + td(days=+49)] = "Feast of Pentecost"
        self[date(year, DEC, 25)] = "Christmas Day"


class IN(India):
    pass


class IND(India):
    pass
