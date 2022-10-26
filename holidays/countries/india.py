#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import warnings
from datetime import date

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class India(HolidayBase):
    # https://www.india.gov.in/calendar
    # https://www.india.gov.in/state-and-ut-holiday-calendar
    # https://en.wikipedia.org/wiki/Public_holidays_in_India
    # https://www.calendarlabs.com/holidays/india/2021
    # https://slusi.dacnet.nic.in/watershedatlas/list_of_state_abbreviation.htm
    # https://vahan.parivahan.gov.in/vahan4dashboard/

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

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
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

        if self.subdiv in (
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
        ):
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

        if year < 2010 or year > 2030:
            warning_msg = (
                "Diwali and Holi holidays available from 2010 to 2030 only"
            )
            warnings.warn(warning_msg, Warning)

        name1 = "Diwali"
        name2 = "Holi"

        if year == 2010:
            self[date(year, DEC, 5)] = name1
            self[date(year, FEB, 28)] = name2
        elif year == 2011:
            self[date(year, OCT, 26)] = name1
            self[date(year, MAR, 19)] = name2
        elif year == 2012:
            self[date(year, NOV, 13)] = name1
            self[date(year, MAR, 8)] = name2
        elif year == 2013:
            self[date(year, NOV, 3)] = name1
            self[date(year, MAR, 26)] = name2
        elif year == 2014:
            self[date(year, OCT, 23)] = name1
            self[date(year, MAR, 17)] = name2
        elif year == 2015:
            self[date(year, NOV, 11)] = name1
            self[date(year, MAR, 6)] = name2
        elif year == 2016:
            self[date(year, OCT, 30)] = name1
            self[date(year, MAR, 24)] = name2
        elif year == 2017:
            self[date(year, OCT, 19)] = name1
            self[date(year, MAR, 13)] = name2
        elif year == 2018:
            self[date(year, NOV, 7)] = name1
            self[date(year, MAR, 2)] = name2
        elif year == 2019:
            self[date(year, OCT, 27)] = name1
            self[date(year, MAR, 21)] = name2
        elif year == 2020:
            self[date(year, NOV, 14)] = name1
            self[date(year, MAR, 9)] = name2
        elif year == 2021:
            self[date(year, NOV, 4)] = name1
            self[date(year, MAR, 28)] = name2
        elif year == 2022:
            self[date(year, OCT, 24)] = name1
            self[date(year, MAR, 18)] = name2
        elif year == 2023:
            self[date(year, OCT, 12)] = name1
            self[date(year, MAR, 7)] = name2
        elif year == 2024:
            self[date(year, NOV, 1)] = name1
            self[date(year, MAR, 25)] = name2
        elif year == 2025:
            self[date(year, OCT, 21)] = name1
            self[date(year, MAR, 14)] = name2
        elif year == 2026:
            self[date(year, NOV, 8)] = name1
            self[date(year, MAR, 3)] = name2
        elif year == 2027:
            self[date(year, OCT, 29)] = name1
            self[date(year, MAR, 22)] = name2
        elif year == 2028:
            self[date(year, OCT, 17)] = name1
            self[date(year, MAR, 11)] = name2
        elif year == 2029:
            self[date(year, NOV, 5)] = name1
            self[date(year, FEB, 28)] = name2
        elif year == 2030:
            self[date(year, OCT, 26)] = name1
            self[date(year, MAR, 19)] = name2
        else:
            pass


class IN(India):
    pass


class IND(India):
    pass
