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

import warnings

from holidays.calendars.gregorian import MAR, OCT, NOV
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class India(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """
    https://www.india.gov.in/calendar
    https://www.india.gov.in/state-and-ut-holiday-calendar
    https://en.wikipedia.org/wiki/Public_holidays_in_India
    https://www.calendarlabs.com/holidays/india/2021
    https://slusi.dacnet.nic.in/watershedatlas/list_of_state_abbreviation.htm
    https://vahan.parivahan.gov.in/vahan4dashboard/
    """

    country = "IN"
    subdivisions = (
        "AN",  # Andaman and Nicobar Islands.
        "AP",  # Andhra Pradesh.
        "AR",  # Arunāchal Pradesh.
        "AS",  # Assam.
        "BR",  # Bihār.
        "CG",  # Chhattīsgarh.
        "CH",  # Chandīgarh.
        "DH",  # Dādra and Nagar Haveli and Damān and Diu.
        "DL",  # Delhi.
        "GA",  # Goa.
        "GJ",  # Gujarāt.
        "HP",  # Himāchal Pradesh.
        "HR",  # Haryāna.
        "JH",  # Jhārkhand.
        "JK",  # Jammu and Kashmīr.
        "KA",  # Karnātaka.
        "KL",  # Kerala.
        "LA",  # Ladākh.
        "LD",  # Lakshadweep.
        "MH",  # Mahārāshtra.
        "ML",  # Meghālaya.
        "MN",  # Manipur.
        "MP",  # Madhya Pradesh.
        "MZ",  # Mizoram.
        "NL",  # Nāgāland.
        "OD",  # Odisha.
        "PB",  # Punjab.
        "PY",  # Puducherry.
        "RJ",  # Rājasthān.
        "SK",  # Sikkim.
        "TN",  # Tamil Nādu.
        "TR",  # Tripura.
        "TS",  # Telangāna.
        "UK",  # Uttarākhand.
        "UP",  # Uttar Pradesh.
        "WB",  # West Bengal.
    )
    _deprecated_subdivisions = (
        "DD",  # Daman and Diu.
        "OR",  # Orissa.
    )

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Makar Sankranti / Pongal.
        self._add_holiday_jan_14("Makar Sankranti / Pongal")

        if self._year >= 1950:
            # Republic Day.
            self._add_holiday_jan_26("Republic Day")

        if self._year >= 1947:
            # Independence Day.
            self._add_holiday_aug_15("Independence Day")

        # Gandhi Jayanti.
        self._add_holiday_oct_2("Gandhi Jayanti")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # Directly lifted Diwali and Holi dates from FBProphet from:
        # https://github.com/facebook/prophet/blob/main/python/prophet/hdays.py
        # Warnings kept in place so that users are aware
        if self._year < 2001 or self._year > 2030:
            warning_msg = "Diwali and Holi holidays available from 2001 to 2030 only"
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

        if self._year in diwali_dates:
            self._add_holiday("Diwali", diwali_dates[self._year])

        if self._year in holi_dates:
            self._add_holiday("Holi", holi_dates[self._year])

        # Islamic holidays.
        # Day of Ashura.
        self._add_ashura_day("Day of Ashura")

        # Birth of the Prophet.
        self._add_mawlid_day("Mawlid")

        # Eid ul-Fitr.
        name = "Eid ul-Fitr"
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)

        # Eid al-Adha.
        name = "Eid al-Adha"
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)

        # Christian holidays.
        self._add_palm_sunday("Palm Sunday")
        self._add_good_friday("Good Friday")
        self._add_easter_sunday("Easter Sunday")
        self._add_whit_sunday("Feast of Pentecost")
        self._add_christmas_day("Christmas Day")

        if self.subdiv == "OR":
            self._populate_subdiv_od_public_holidays()

    # Andhra Pradesh.
    def _populate_subdiv_ap_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Andhra Pradesh Foundation Day")

    # Assam.
    def _populate_subdiv_as_public_holidays(self):
        self._add_holiday_apr_15("Bihu (Assamese New Year)")

    # Bihar.
    def _populate_subdiv_br_public_holidays(self):
        self._add_holiday_mar_22("Bihar Day")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Chhattisgarh.
    def _populate_subdiv_cg_public_holidays(self):
        self._add_holiday_nov_1("Chhattisgarh Foundation Day")

    # Gujarat.
    def _populate_subdiv_gj_public_holidays(self):
        self._add_holiday_jan_14("Uttarayan")
        self._add_holiday_may_1("Gujarat Day")
        self._add_holiday_oct_31("Sardar Patel Jayanti")

    # Haryana.
    def _populate_subdiv_hr_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Haryana Foundation Day")

    # Karnataka.
    def _populate_subdiv_ka_public_holidays(self):
        self._add_holiday_nov_1("Karnataka Rajyotsava")

    # Kerala.
    def _populate_subdiv_kl_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Kerala Foundation Day")

    # Maharashtra.
    def _populate_subdiv_mh_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_may_1("Maharashtra Day")
        self._add_holiday_oct_15("Dussehra")

    # Madhya Pradesh.
    def _populate_subdiv_mp_public_holidays(self):
        self._add_holiday_nov_1("Madhya Pradesh Foundation Day")

    # Orissa / Odisha.
    def _populate_subdiv_od_public_holidays(self):
        self._add_holiday_apr_1("Odisha Day (Utkala Dibasa)")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_15("Maha Vishuva Sankranti / Pana Sankranti")

    # Rajasthan.
    def _populate_subdiv_rj_public_holidays(self):
        self._add_holiday_mar_30("Rajasthan Day")
        self._add_holiday_jun_15("Maharana Pratap Jayanti")

    # Sikkim.
    def _populate_subdiv_sk_public_holidays(self):
        self._add_holiday_may_16("Annexation Day")

    # Tamil Nadu.
    def _populate_subdiv_tn_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_14("Puthandu (Tamil New Year)")
        self._add_holiday_apr_15("Puthandu (Tamil New Year)")

    # Telangana.
    def _populate_subdiv_ts_public_holidays(self):
        self._add_holiday_apr_6("Eid al-Fitr")
        self._add_holiday_oct_6("Bathukamma Festival")

    # Uttarakhand.
    def _populate_subdiv_uk_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Uttar Pradesh.
    def _populate_subdiv_up_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # West Bengal.
    def _populate_subdiv_wb_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_14("Pohela Boishakh")
        self._add_holiday_apr_15("Pohela Boishakh")
        self._add_holiday_may_9("Rabindra Jayanti")


class IN(India):
    pass


class IND(India):
    pass
