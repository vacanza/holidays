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
from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
)
from holidays.holiday_base import HolidayBase


class India(
    HolidayBase, ChristianHolidays, HinduCalendarHolidays, InternationalHolidays, IslamicHolidays
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
    default_language = "en_IN"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("en_IN", "en_US", "hi")
    subdivisions = (
        "AN",  # Andaman and Nicobar Islands.
        "AP",  # Andhra Pradesh.
        "AR",  # Arunachal Pradesh (Arunāchal Pradesh).
        "AS",  # Assam.
        "BR",  # Bihar (Bihār).
        "CG",  # Chhattisgarh (Chhattīsgarh).
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

    # India gained independence on August 15, 1947.
    start_year = 1948

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        :param islamic_show_estimated:
            Whether to add "estimated" label to Islamic holidays name if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=IndiaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1950:
            # Republic Day.
            self._add_holiday_jan_26(tr("Republic Day"))

        # Independence Day.
        self._add_holiday_aug_15(tr("Independence Day"))

        # Gandhi Jayanti.
        self._add_holiday_oct_2(tr("Gandhi Jayanti"))

        # Hindu Holidays.
        if self._year < 2001 or self._year > 2035:
            warning_msg = "Requested Holidays are available only from 2001 to 2035."
            warnings.warn(warning_msg, Warning)

        # Buddha Purnima.
        self._add_buddha_purnima(tr("Buddha Purnima"))

        # Diwali.
        self._add_diwali_india(tr("Diwali"))

        # Janmashtami.
        self._add_janmashtami(tr("Janmashtami"))

        # Dussehra.
        self._add_dussehra(tr("Dussehra"))

        # Mahavir Jayanti.
        self._add_mahavir_jayanti(tr("Mahavir Jayanti"))

        # Maha Shivaratri.
        self._add_maha_shivaratri(tr("Maha Shivaratri"))

        # Guru Nanak Jayanti.
        self._add_guru_nanak_jayanti(tr("Guru Nanak Jayanti"))

        # Islamic holidays.

        # Ashura.
        self._add_ashura_day(tr("Muharram"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Milad-un-Nabi"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Id-ul-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Bakrid"))

        # Christian holidays.

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Christmas.
        self._add_christmas_day(tr("Christmas"))

        if self.subdiv == "OR":
            self._populate_subdiv_od_public_holidays()

    def _populate_optional_holidays(self):
        # Hindu holidays.

        # Children's Day.
        self._add_holiday_nov_14(tr("Children's Day"))

        # Holi.
        self._add_holi(tr("Holi"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))

        # Labor Day.
        self._add_labor_day(tr("Labour Day"))

        # Maha Navami.
        self._add_maha_navami(tr("Maha Navami"))

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Ram Navami.
        self._add_ram_navami(tr("Ram Navami"))

        # Navratri / Sharad Navratri.
        self._add_sharad_navratri(tr("Navratri / Sharad Navratri"))

        # Christian holidays.

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # Palm Sunday.
        self._add_palm_sunday(tr("Palm Sunday"))

    # Andaman and Nicobar Islands.
    def _populate_subdiv_an_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # Andhra Pradesh.
    def _populate_subdiv_ap_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Andhra Pradesh Foundation Day.
        self._add_holiday_nov_1(tr("Andhra Pradesh Foundation Day"))

    # Assam.
    def _populate_subdiv_as_public_holidays(self):
        # Magh Bihu.
        self._add_makar_sankranti(tr("Magh Bihu"))
        # Assam Day.
        self._add_holiday_dec_2(tr("Assam Day"))

    # Bihar.
    def _populate_subdiv_br_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))
        # Bihar Day.
        self._add_holiday_mar_22(tr("Bihar Day"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # Chandigarh.
    def _populate_subdiv_ch_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # Chhattisgarh.
    def _populate_subdiv_cg_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Chhattisgarh Foundation Day.
        self._add_holiday_nov_1(tr("Chhattisgarh Foundation Day"))

    # Delhi.
    def _populate_subdiv_dl_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))

    # Goa.
    def _populate_subdiv_ga_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Goa Liberation Day.
        self._add_holiday_dec_19(tr("Goa Liberation Day"))

    # Gujarat.
    def _populate_subdiv_gj_public_holidays(self):
        # Makar Sankranti.
        self._add_makar_sankranti(tr("Uttarayan"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Gujarat Day.
        self._add_holiday_may_1(tr("Gujarat Day"))
        # Sardar Vallabhbhai Patel Jayanti.
        self._add_holiday_oct_31(tr("Sardar Vallabhbhai Patel Jayanti"))

    # Haryana.
    def _populate_subdiv_hr_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Haryana Foundation Day.
        self._add_holiday_nov_1(tr("Haryana Foundation Day"))

    # Himachal Pradesh.
    def _populate_subdiv_hp_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Himachal Day.
        self._add_holiday_apr_15(tr("Himachal Day"))

    # Jammu and Kashmir
    def _populate_subdiv_jk_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # Jharkhand.
    def _populate_subdiv_jh_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Jharkhand Formation Day.
        self._add_holiday_nov_15(tr("Jharkhand Formation Day"))

    # Karnataka.
    def _populate_subdiv_ka_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Karnataka Rajyotsav.
        self._add_holiday_nov_1(tr("Karnataka Rajyotsava"))

    # Kerala.
    def _populate_subdiv_kl_public_holidays(self):
        # Onam.
        self._add_onam(tr("Onam"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Kerala Foundation Day.
        self._add_holiday_nov_1(tr("Kerala Foundation Day"))

    # Ladakh.
    def _populate_subdiv_la_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # Maharashtra.
    def _populate_subdiv_mh_public_holidays(self):
        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))
        # Chhatrapati Shivaji Maharaj Jayanti.
        self._add_holiday_feb_19(tr("Chhatrapati Shivaji Maharaj Jayanti"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Maharashtra Day.
        self._add_holiday_may_1(tr("Maharashtra Day"))

    # Madhya Pradesh.
    def _populate_subdiv_mp_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Madhya Pradesh Foundation Day.
        self._add_holiday_nov_1(tr("Madhya Pradesh Foundation Day"))

    # Mizoram.
    def _populate_subdiv_mz_public_holidays(self):
        # Mizoram State Day.
        self._add_holiday_feb_20(tr("Mizoram State Day"))

    # Nagaland.
    def _populate_subdiv_nl_public_holidays(self):
        # Nagaland State Inauguration Day.
        self._add_holiday_dec_1(tr("Nagaland State Inauguration Day"))

    # Orissa / Odisha.
    def _populate_subdiv_od_public_holidays(self):
        # Odisha Day.
        self._add_holiday_apr_1(tr("Odisha Day (Utkala Dibasa)"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Maha Vishuva Sankranti.
        self._add_holiday_apr_15(tr("Maha Vishuva Sankranti / Pana Sankranti"))

    # Puducherry.
    def _populate_subdiv_py_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Puducherry De Jure Transfer Day.
        self._add_holiday_aug_16(tr("Puducherry De Jure Transfer Day"))
        # Puducherry Liberation Day.
        self._add_holiday_nov_1(tr("Puducherry Liberation Day"))

    # Punjab.
    def _populate_subdiv_pb_public_holidays(self):
        # Guru Gobind Singh Jayanti.
        self._add_guru_gobind_singh_jayanti(tr("Guru Gobind Singh Jayanti"))
        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))
        # Lohri.
        self._add_holiday_jan_13(tr("Lohri"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Punjabi Day.
        self._add_holiday_nov_1(tr("Punjab Day"))

    # Rajasthan.
    def _populate_subdiv_rj_public_holidays(self):
        # Rajasthan Day.
        self._add_holiday_mar_30(tr("Rajasthan Day"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Maharana Pratap Jayanti.
        self._add_holiday_jun_15(tr("Maharana Pratap Jayanti"))

    # Sikkim.
    def _populate_subdiv_sk_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Sikkim State Day.
        self._add_holiday_may_16(tr("Sikkim State Day"))

    # Tamil Nadu.
    def _populate_subdiv_tn_public_holidays(self):
        # Pongal.
        self._add_makar_sankranti(tr("Pongal"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Puthandu.
        self._add_holiday_apr_14(tr("Puthandu (Tamil New Year)"))

    # Telangana.
    def _populate_subdiv_ts_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Telangana Formation Day.
        self._add_holiday_jun_2(tr("Telangana Formation Day"))
        # Bathukamma Festival.
        self._add_holiday_oct_6(tr("Bathukamma Festival"))

    # Uttarakhand.
    def _populate_subdiv_uk_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # Uttar Pradesh.
    def _populate_subdiv_up_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))
        # UP Formation Day.
        self._add_holiday_jan_24(tr("UP Formation Day"))
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

    # West Bengal.
    def _populate_subdiv_wb_public_holidays(self):
        # Dr. B. R. Ambedkar Jayanti.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))
        # Pohela Boisakh.
        self._add_holiday_apr_15(tr("Pohela Boishakh"))
        # Rabindra Jayanti.
        self._add_holiday_may_9(tr("Rabindra Jayanti"))


class IndiaIslamicHolidays(_CustomIslamicHolidays):
    # Muharram / Day of Ashura.
    ASHURA_DATES = {
        2001: (APR, 4),
        2002: (MAR, 24),
        2003: (MAR, 14),
        2004: (MAR, 2),
        2005: (FEB, 19),
        2006: (FEB, 9),
        2007: (JAN, 30),
        2008: (JAN, 19),
        2009: ((JAN, 7), (DEC, 28)),
        2010: (DEC, 17),
        2011: (DEC, 6),
        2012: (NOV, 25),
        2013: (NOV, 14),
        2014: (NOV, 4),
        2015: (OCT, 24),
        2016: (OCT, 12),
        2017: (OCT, 1),
        2018: (SEP, 21),
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 20),
        2022: (AUG, 9),
        2023: (JUL, 29),
        2024: (JUL, 17),
        2025: (JUL, 6),
    }

    # Bakrid / Eid-al-Adha.
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 11), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 27),
        2013: (OCT, 16),
        2014: (OCT, 6),
        2015: (SEP, 25),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (AUG, 1),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    # Id-ul-Fitr / Eid-al-Fitr.
    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 3),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 20),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 16),
        2019: (JUN, 5),
        2020: (MAY, 25),
        2021: (MAY, 14),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 11),
        2025: (MAR, 31),
    }

    # Milad-un-Nabi / Mawlid.
    MAWLID_DATES = {
        2001: (JUN, 5),
        2002: (MAY, 25),
        2003: (MAY, 15),
        2004: (MAY, 3),
        2005: (APR, 22),
        2006: (APR, 11),
        2007: (APR, 1),
        2008: (MAR, 21),
        2009: (MAR, 9),
        2010: (FEB, 27),
        2011: (FEB, 16),
        2012: (FEB, 5),
        2013: (JAN, 25),
        2014: (JAN, 14),
        2015: ((JAN, 4), (DEC, 25)),
        2016: (DEC, 13),
        2017: (DEC, 2),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 30),
        2021: (OCT, 19),
        2022: (OCT, 9),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }


class IN(India):
    pass


class IND(India):
    pass
