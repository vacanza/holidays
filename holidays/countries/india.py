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

from holidays.groups import (
    HinduCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.holiday_base import HolidayBase


class India(
    HolidayBase, HinduCalendarHolidays, ChristianHolidays, InternationalHolidays, IslamicHolidays
):
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
        "AR",  # Arunachal Pradesh (Arunāchal Pradesh).
        "AS",  # Assam.
        "BR",  # Bihar (Bihār).
        "CG",  # Chattisgarh (Chhattīsgarh).
        "CH",  # Chandigarh (Chandīgarh).
        "DH",  # Dadra and Nagar Haveli and Daman and Diu(Dādra and Nagar Haveli and Damān and Diu)
        "DL",  # Delhi.
        "GA",  # Goa.
        "GJ",  # Gujarat (Gujarāt).
        "HP",  # Himachal Pradesh (Himāchal Pradesh).
        "HR",  # Haryana (Haryāna).
        "JH",  # Jharkhand (Jhārkhand).
        "JK",  # Jammu and Kashmir (Jammu and Kashmīr).
        "KA",  # Karnataka (Karnātaka).
        "KL",  # Kerala.
        "LA",  # Ladakh (Ladākh).
        "LD",  # Lakshadweep.
        "MH",  # Maharashtra (Mahārāshtra).
        "ML",  # Meghalaya (Meghālaya).
        "MN",  # Manipur.
        "MP",  # Madhya Pradesh.
        "MZ",  # Mizoram.
        "NL",  # Nagaland (Nāgāland).
        "OD",  # Odisha.
        "PB",  # Punjab.
        "PY",  # Puducherry.
        "RJ",  # Rajasthan (Rājasthān).
        "SK",  # Sikkim.
        "TN",  # Tamil Nadu (Tamil Nādu).
        "TR",  # Tripura.
        "TS",  # Telangana (Telangāna).
        "UK",  # Uttarakhand (Uttarākhand).
        "UP",  # Uttar Pradesh.
        "WB",  # West Bengal.
    )
    _deprecated_subdivisions = (
        "DD",  # Daman and Diu.
        "OR",  # Orissa.
    )
    subdivisions_aliases = {
        "Andaman and Nicobar Islands": "AN",
        "Andhra Pradesh": "AP",
        "Arunachal Pradesh": "AR",
        "Arunāchal Pradesh": "AR",
        "Assam": "AS",
        "Bihar": "BR",
        "Bihār": "BR",
        "Chhattisgarh": "CG",
        "Chhattīsgarh": "CG",
        "Chandigarh": "CH",
        "Chandīgarh": "CH",
        "Dadra and Nagar Haveli and Daman and Diu": "DH",
        "Dādra and Nagar Haveli and Damān and Diu": "DH",
        "Delhi": "DL",
        "Goa": "GA",
        "Gujarat": "GJ",
        "Gujarāt": "GJ",
        "Himachal Pradesh": "HP",
        "Himāchal Pradesh": "HP",
        "Haryana": "HR",
        "Haryāna": "HR",
        "Jharkhand": "JH",
        "Jhārkhand": "JH",
        "Jammu and Kashmir": "JK",
        "Jammu and Kashmīr": "JK",
        "Karnataka": "KA",
        "Karnātaka": "KA",
        "Kerala": "KL",
        "Ladakh": "LA",
        "Ladākh": "LA",
        "Lakshadweep": "LD",
        "Maharashtra": "MH",
        "Mahārāshtra": "MH",
        "Meghalaya": "ML",
        "Meghālaya": "ML",
        "Manipur": "MN",
        "Madhya Pradesh": "MP",
        "Mizoram": "MZ",
        "Nagaland": "NL",
        "Nāgāland": "NL",
        "Odisha": "OD",
        "Punjab": "PB",
        "Puducherry": "PY",
        "Rajasthan": "RJ",
        "Rājasthān": "RJ",
        "Sikkim": "SK",
        "Tamil Nadu": "TN",
        "Tamil Nādu": "TN",
        "Tripura": "TR",
        "Telangana": "TS",
        "Telangāna": "TS",
        "Uttarakhand": "UK",
        "Uttarākhand": "UK",
        "Uttar Pradesh": "UP",
        "West Bengal": "WB",
    }

    def __init__(self, *args, **kwargs):
        HinduCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1950:
            # Republic Day.
            self._add_holiday_jan_26("Republic Day")

        if self._year >= 1947:
            # Independence Day.
            self._add_holiday_aug_15("Independence Day")

        # Gandhi Jayanti.
        self._add_holiday_oct_2("Gandhi Jayanti")

        # Children's Day.
        self._add_holiday_nov_14("Children's Day")

        # Labour Day.
        self._add_labor_day("Labour Day")

        # Hindu Holidays.
        if self._year < 2001 or self._year > 2035:
            warning_msg = "Requested Holidays are available only from 2001 to 2035."
            warnings.warn(warning_msg, Warning)

        # Diwali.
        self._add_diwali_india("Diwali")

        # Holi.
        self._add_holi("Holi")
        # Holi.
        self._add_holi("Holi")

        # Govardhan Puja.
        self._add_govardhan_puja("Govardhan Puja")
        # Govardhan Puja.
        self._add_govardhan_puja("Govardhan Puja")

        # Raksha Bandhan.
        self._add_raksha_bandhan("Raksha Bandhan")
        # Raksha Bandhan.
        self._add_raksha_bandhan("Raksha Bandhan")

        # Janmashtami.
        self._add_janmashtami("Janmashtami")
        # Janmashtami.
        self._add_janmashtami("Janmashtami")

        # Dussehra.
        self._add_dussehra("Dussehra")
        # Dussehra.
        self._add_dussehra("Dussehra")

        # Mahavir Jayanti.
        self._add_mahavir_jayanti("Mahavir Jayanti")
        # Mahavir Jayanti.
        self._add_mahavir_jayanti("Mahavir Jayanti")

        # Maha Shivaratri.
        self._add_maha_shivaratri("Maha Shivaratri")
        # Maha Shivaratri.
        self._add_maha_shivaratri("Maha Shivaratri")

        # Navratri / Sharad Navratri.
        self._add_sharad_navratri("Navratri / Sharad Navratri")
        # Navratri / Sharad Navratri.
        self._add_sharad_navratri("Navratri / Sharad Navratri")

        # Ram Navami.
        self._add_ram_navami("Ram Navami")
        # Ram Navami.
        self._add_ram_navami("Ram Navami")

        # Maha Navami.
        self._add_maha_navami("Maha Navami")
        # Maha Navami.
        self._add_maha_navami("Maha Navami")

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi("Ganesh Chaturthi")
        self._add_maha_navami("Maha Navami")

        # Makar Sankranti.
        self._add_makar_sankranti("Makar Sankranti")

        # Guru Nanak Jayanti.
        self._add_guru_nanak_jayanti("Guru Nanak Jayanti")
        # Guru Nanak Jayanti.
        self._add_guru_nanak_jayanti("Guru Nanak Jayanti")

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

    # Andaman and Nicobar Islands.
    def _populate_subdiv_an_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Andhra Pradesh.
    def _populate_subdiv_ap_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Andhra Pradesh Foundation Day")

    # Assam.
    def _populate_subdiv_as_public_holidays(self):
        self._add_makar_sankranti("Bihu")
        self._add_holiday_dec_2("Asssam Day")

    # Bihar.
    def _populate_subdiv_br_public_holidays(self):
        self._add_chhath_puja("Chhath Puja")

        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_mar_22("Bihar Day")

    # Chhattisgarh.
    def _populate_subdiv_cg_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Chhattisgarh Foundation Day")

    # Chandigarh.
    def _populate_subdiv_ch_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Delhi.
    def _populate_subdiv_dl_public_holidays(self):
        self._add_chhath_puja("Chhath Puja")

    # Goa.
    def _populate_subdiv_ga_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_dec_19("Goa Liberation Day")

    # Gujarat.
    def _populate_subdiv_gj_public_holidays(self):
        self._add_makar_sankranti("Uttarayan")

        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_may_1("Gujarat Day")
        self._add_holiday_oct_31("Sardar Vallabhbhai Patel Jayanti")

    # Himachal Pradesh.
    def _populate_subdiv_hp_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_15("Haryana Day")

    # Haryana.
    def _populate_subdiv_hr_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Haryana Foundation Day")

    # Jammu and Kashmir
    def _populate_subdiv_jk_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Jharkhand.
    def _populate_subdiv_jh_public_holidays(self):
        self._add_chhath_puja("Chhath Puja")

        self._add_holiday_nov_15("Jharkhand Formation Day")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Karnataka.
    def _populate_subdiv_ka_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Karnataka Rajyotsava")

    # Ladakh.
    def _populate_subdiv_la_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Kerala.
    def _populate_subdiv_kl_public_holidays(self):
        self._add_onam("Onam")

        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Kerala Foundation Day")

    # Mizoram.
    def _populate_subdiv_mz_public_holidays(self):
        self._add_holiday_feb_20("Mizoram State Day")

    # Maharashtra.
    def _populate_subdiv_mh_public_holidays(self):
        self._add_gudi_padwa("Gudi Padwa")

        self._add_holiday_feb_19("Chhatrapati Shivaji Maharaj Jayanti")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_may_1("Maharashtra Day")
        self._add_holiday_oct_15("Dussehra")

    # Madhya Pradesh.
    def _populate_subdiv_mp_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_nov_1("Madhya Pradesh Foundation Day")

    # Nagaland.
    def _populate_subdiv_nl_public_holidays(self):
        self._add_holiday_dec_1("Nagaland State Inauguration Day")

    # Orissa / Odisha.
    def _populate_subdiv_od_public_holidays(self):
        self._add_holiday_apr_1("Odisha Day (Utkala Dibasa)")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_15("Maha Vishuva Sankranti / Pana Sankranti")

    # Punjab.
    def _populate_subdiv_pb_public_holidays(self):
        self._add_guru_gobind_singh_jayanti("Guru Gobind Singh Jayanti")

        self._add_vaisakhi("Vaisakhi")

        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_jan_13("Lohri")
        self._add_holiday_nov_1("Punjab Day")

    # Puducherry.
    def _populate_subdiv_py_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_aug_16("Puducherry De Jure Transfer Day")
        self._add_holiday_nov_1("Puducherry Liberation  Day")

    # Rajasthan.
    def _populate_subdiv_rj_public_holidays(self):
        self._add_holiday_mar_30("Rajasthan Day")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_jun_15("Maharana Pratap Jayanti")

    # Sikkim.
    def _populate_subdiv_sk_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_may_16("Sikkim State Day")

    # Tamil Nadu.
    def _populate_subdiv_tn_public_holidays(self):
        self._add_makar_sankranti("Pongal")

        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_14("Puthandu (Tamil New Year)")
        self._add_holiday_apr_15("Puthandu (Tamil New Year)")

    # Telangana.
    def _populate_subdiv_ts_public_holidays(self):
        self._add_holiday_apr_6("Eid al-Fitr")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_jun_2("Telangana Formation Day")
        self._add_holiday_oct_6("Bathukamma Festival")

    # Uttarakhand.
    def _populate_subdiv_uk_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # Uttar Pradesh.
    def _populate_subdiv_up_public_holidays(self):
        self._add_chhath_puja("Chhath Puja")

        self._add_holiday_jan_24("UP Formation Day")
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")

    # West Bengal.
    def _populate_subdiv_wb_public_holidays(self):
        self._add_holiday_apr_14("Dr. B. R. Ambedkar's Jayanti")
        self._add_holiday_apr_14("Pohela Boishakh")
        self._add_holiday_apr_15("Pohela Boishakh")
        self._add_holiday_may_1("May Day")
        self._add_holiday_may_9("Rabindra Jayanti")


class IN(India):
    pass


class IND(India):
    pass
