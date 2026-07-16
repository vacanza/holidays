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
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class India(
    HolidayBase,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """India holidays.

    References:
        * <https://web.archive.org/web/20250413193616/https://www.india.gov.in/calendar>
        * <https://web.archive.org/web/20250413193624/https://www.india.gov.in/state-and-ut-holiday-calendar>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_India>
        * <https://web.archive.org/web/20250413193633/https://www.calendarlabs.com/holidays/india/2021>
        * <https://web.archive.org/web/20231118175007/http://slusi.dacnet.nic.in/watershedatlas/list_of_state_abbreviation.htm>
        * <https://web.archive.org/web/20231008063930/https://vahan.parivahan.gov.in/vahan4dashboard/>
        * <https://web.archive.org/web/20250803044148/https://doptcirculars.nic.in/Default.aspx?URL=dFaVfDsok83H>
        * <https://web.archive.org/web/20201027122146/https://doptcirculars.nic.in/Default.aspx?URL=dFaVfDsok83HARCH%20>
        * <https://web.archive.org/web/20220517110319/https://www.referencer.in/HolidayList.aspx>
        * <http://web.archive.org/web/20260618194243/https://www.scribd.com/document/921146658/Govt-Holiday-List-07>
        * <https://web.archive.org/web/20260620201925/https://www.sci.gov.in/calendar>
        * <https://web.archive.org/web/20260620202110/https://bombayhighcourt.nic.in/hccalender.php>
        * <https://web.archive.org/web/20260620202127/https://www.allahabadhighcourt.in/Calendar>
        * Andaman and Nicobar Islands:
            * <https://web.archive.org/web/20251214133200/https://andamannicobar.gov.in/admin-pannel/othersdoc/1-29-Holiday%20List%202026%20Gazette.pdf>
        * Gujarat:
            * <https://web.archive.org/web/20260122052040/https://images-gujarati.indianexpress.com/2025/11/gujarat-government-Year-2026-holiday-list.pdf>
        * Kerala:
            * <https://web.archive.org/web/20260329164551/https://kerala.gov.in/showcalendar/2026>
        * Maharashtra:
            * <https://web.archive.org/web/20260327070656/https://www.mcgm.gov.in/irj/go/km/docs/documents/HomePage%20Data/Whats%20New/Public%20Holidays%202026.pdf>
        * Punjab:
            * <https://web.archive.org/web/20260216022835/https://punjab.gov.in/wp-content/uploads/2025/12/Calender-2026.pdf>
        * Tamil Nadu:
            * [Tamil Monthly Calendar](https://web.archive.org/web/20231228103352/https://www.tamildailycalendar.com/tamil_monthly_calendar.php)
            * [Tamil Calendar](https://web.archive.org/web/20250429125140/https://www.prokerala.com/general/calendar/tamilcalendar.php)
        * Telangana:
            * <https://web.archive.org/web/20260224050455/https://transport.telangana.gov.in/html/registration-districtcodes.html>
            * <https://web.archive.org/web/20250219131214/https://www.thehindu.com/news/national/telangana/cm-firm-on-having-states-identity-as-tg-not-ts/article68187923.ece>
    """

    country = "IN"
    default_language = "en_IN"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # India gained independence on August 15, 1947.
    start_year = 1948
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
        "TG": "TS",
        "Telangana": "TS",
        "Telangāna": "TS",
        "Uttarakhand": "UK",
        "Uttarākhand": "UK",
        "Uttar Pradesh": "UP",
        "West Bengal": "WB",
    }
    supported_categories = (OPTIONAL, PUBLIC)
    supported_languages = ("bn", "en_IN", "en_US", "gu", "hi", "kn", "ml", "mr", "pa", "ta", "te")
    _deprecated_subdivisions = (
        "DD",  # Daman and Diu.
        "OR",  # Orissa.
    )

    holi_optional_years = {2002, 2011}

    janmashtami_optional_years = {2008, 2017}

    maha_shivaratri_optional_years = {
        2003,
        2009,
        2010,
        2013,
        2014,
        2015,
        2016,
        2020,
        2021,
        2023,
        2024,
        2026,
    }

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.

        In India, the dates of the Islamic calendar usually fall a day later than
        the corresponding dates in the Umm al-Qura calendar.
        """
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        IslamicHolidays.__init__(
            self,
            cls=IndiaIslamicHolidays,
            show_estimated=islamic_show_estimated,
            calendar_delta_days=+1,
        )
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, cls=IndiaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1950:
            # Republic Day.
            self._add_holiday_jan_26(tr("Republic Day"))

        # Dr. B. R. Ambedkar's Birthday.
        self._add_holiday_apr_14(tr("Dr. B. R. Ambedkar's Jayanti"))

        # Independence Day.
        self._add_holiday_aug_15(tr("Independence Day"))

        # Mahatma Gandhi's Birthday.
        self._add_holiday_oct_2(tr("Mahatma Gandhi's Jayanti"))

        # Hindu Holidays.

        if self._year < 2001 or self._year > 2035:
            warnings.warn(
                "Requested Holidays are available only from 2001 to 2035.",
                UserWarning,
                stacklevel=7,
            )

        if self._year not in self.maha_shivaratri_optional_years:
            # Maha Shivaratri.
            self._add_maha_shivaratri(tr("Maha Shivaratri"))

        if self._year not in self.holi_optional_years:
            # Holi.
            self._add_holi(tr("Holi"))

        if self._ram_navami and not self._is_sunday(self._ram_navami):
            # Ram Navami.
            self._add_ram_navami(tr("Ram Navami"))

        # Mahavira's Birthday.
        self._add_mahavir_jayanti(tr("Mahavir Jayanti"))

        # Buddha Purnima.
        self._add_buddha_purnima(tr("Buddha Purnima"))

        if self._year not in self.janmashtami_optional_years:
            # Janmashtami (Vaishnava).
            self._add_janmashtami(tr("Janmashtami (Vaishnava)"))

        # Dussehra.
        self._add_dussehra(tr("Dussehra"))

        # Diwali.
        self._add_diwali_india(tr("Diwali (Deepavali)"))

        # Guru Nanak's Birthday.
        self._add_guru_nanak_jayanti(tr("Guru Nanak's Jayanti"))

        # Islamic holidays.

        # Ashura.
        self._add_ashura_day(tr("Muharram"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Milad-un-Nabi"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Id-ul-Fitr"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Id-ul-Zuha (Bakrid)"))

        # Christian holidays.

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Christmas.
        self._add_christmas_day(tr("Christmas"))

        if self.subdiv == "OR":
            self._populate_subdiv_od_public_holidays()

    def _populate_optional_holidays(self):

        # New Year's Day.
        self._add_new_years_day(tr("New Year's Day"))

        # Hindu holidays.

        # Guru Gobind Singh's Birthday.
        name = tr("Guru Gobind Singh's Jayanti")
        if 2005 <= self._year <= 2011:
            self._add_holiday_jan_5(name)
        else:
            self._add_guru_gobind_singh_jayanti(name)

        if 2020 <= self._year <= 2022 or self._year == 2024:
            # Lohri.
            self._add_lohri(tr("Lohri"))

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        if self._year >= 2021 and self._year != 2023:
            # Magh Bihu.
            self._add_pongal(tr("Magh Bihu"))

        # Pongal.
        self._add_pongal(tr("Pongal"))

        if self._year != 2013:
            # Basant Panchami / Sri Panchami.
            self._add_basant_panchami(tr("Basant Panchami / Sri Panchami"))

        # Guru Ravi Das's Birthday.
        self._add_guru_ravidas_jayanti(tr("Guru Ravi Das's Jayanti"))

        # Shivaji's Birthday.
        self._add_holiday_feb_19(tr("Shivaji's Jayanti"))

        # Swami Dayanand Saraswati's Birthday.
        self._add_swami_dayanand_saraswati_jayanti(tr("Swami Dayanand Saraswati's Jayanti"))

        if self._year in self.maha_shivaratri_optional_years:
            # Maha Shivaratri.
            self._add_maha_shivaratri(tr("Maha Shivaratri"))

        if self._year <= 2011 or self._year >= 2016:
            # Dolyatra.
            self._add_holika_dahan(tr("Dolyatra"))

        # Holika Dahan.
        self._add_holika_dahan(tr("Holika Dahan"))

        if self._year in self.holi_optional_years:
            # Holi.
            self._add_holi(tr("Holi"))

        # Chaitra Sukladi.
        self._add_gudi_padwa(tr("Chaitra Sukladi"))

        # Cheti Chand.
        self._add_gudi_padwa(tr("Cheti Chand"))

        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))

        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

        if self._ram_navami and self._is_sunday(self._ram_navami):
            # Ram Navami.
            self._add_ram_navami(tr("Ram Navami"))

        # Meshadi (Tamil New Year's Day).
        self._add_holiday_apr_14(tr("Meshadi (Tamil New Year's Day)"))

        # Bahag Bihu.
        self._add_vaisakhadi(tr("Bahag Bihu"))

        # Vaisakhadi.
        self._add_vaisakhadi(tr("Vaisakhadi"))

        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))

        # Vishu.
        self._add_vishu(tr("Vishu"))

        if self._year >= 2008:
            # Guru Rabindranath's Birthday.
            self._add_rabindranath_birthday(tr("Guru Rabindranath's Jayanti"))

        # Rath Yatra.
        self._add_rath_yatra(tr("Rath Yatra"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Parsi New Year.
        self._add_parsi_new_year(tr("Parsi New Year"))

        # Onam.
        self._add_onam(tr("Onam"))

        if self._year in self.janmashtami_optional_years:
            # Janmashtami (Vaishnava).
            self._add_janmashtami(tr("Janmashtami (Vaishnava)"))

        if self._year not in {2012, 2023}:
            # Ganesh Chaturthi / Vinayak Chaturthi.
            self._add_ganesh_chaturthi(tr("Ganesh Chaturthi / Vinayak Chaturthi"))

        # Dussehra (Saptami).
        self._add_maha_saptami(tr("Dussehra (Saptami)"))

        # Dussehra (Mahashtami).
        self._add_maha_ashtami(tr("Dussehra (Mahashtami)"))

        # Dussehra (Mahanavami).
        if self._year != 2002:
            self._add_maha_navami(tr("Dussehra (Mahanavami)"))

        # Maharishi Valmiki's Birthday.
        self._add_maharishi_valmiki_jayanti(tr("Maharishi Valmiki's Jayanti"))

        if self._year >= 2012:
            # Karaka Chaturthi (Karwa Chouth).
            self._add_karwa_chauth(tr("Karaka Chaturthi (Karwa Chouth)"))

        if self._year <= 2018:
            # Diwali (South India).
            self._add_diwali_south_india(tr("Deepavali (South India)"))

        # Naraka Chaturdashi.
        self._add_naraka_chaturdashi(tr("Naraka Chaturdashi"))

        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))

        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

        if self._year >= 2011:
            # Pratihar Shashthi or Surya Shashthi (Chhat Puja).
            self._add_chhath_puja(tr("Pratihar Shashthi or Surya Shashthi (Chhat Puja)"))

        if self._year >= 2004:
            # Guru Tegh Bahadur's Martyrdom Day.
            self._add_holiday_nov_24(tr("Guru Tegh Bahadur's Martyrdom Day"))

        # Islamic holidays.

        # Ali's Birthday.
        self._add_ali_birthday_day(tr("Hazarat Ali's Birthday"))

        # Jumu'atul-Wida.
        self._add_jumuatul_wida(tr("Jamat-Ul-Vida"))

        # Christian holidays.

        if self._year >= 2003:
            # Christmas Eve.
            self._add_christmas_eve(tr("Christmas Eve"))

        if self._year >= 2007:
            # Easter Sunday.
            self._add_easter_sunday(tr("Easter Sunday"))

    # Andaman and Nicobar Islands.
    def _populate_subdiv_an_public_holidays(self):
        # Onam.
        self._add_onam(tr("Onam"))

    # Andhra Pradesh.
    def _populate_subdiv_ap_public_holidays(self):
        # Andhra Pradesh Foundation Day.
        self._add_holiday_nov_1(tr("Andhra Pradesh Foundation Day"))
        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

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

    # Chandigarh.
    def _populate_subdiv_ch_public_holidays(self):
        pass

    # Chhattisgarh.
    def _populate_subdiv_cg_public_holidays(self):
        # Chhattisgarh Foundation Day.
        self._add_holiday_nov_1(tr("Chhattisgarh Foundation Day"))

    # Delhi.
    def _populate_subdiv_dl_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))

    # Goa.
    def _populate_subdiv_ga_public_holidays(self):
        # Goa Liberation Day.
        self._add_holiday_dec_19(tr("Goa Liberation Day"))

    # Gujarat.
    def _populate_subdiv_gj_public_holidays(self):
        # Makar Sankranti.
        self._add_makar_sankranti(tr("Uttarayan"))
        # Gujarat Day.
        self._add_holiday_may_1(tr("Gujarat Day"))
        # Sardar Vallabhbhai Patel Jayanti.
        self._add_holiday_oct_31(tr("Sardar Vallabhbhai Patel Jayanti"))
        # Parsi New Year (Shahenshahi).
        self._add_parsi_new_year(tr("Parsi New Year (Shahenshahi)"))

    # Haryana.
    def _populate_subdiv_hr_public_holidays(self):
        # Haryana Foundation Day.
        self._add_holiday_nov_1(tr("Haryana Foundation Day"))

    # Himachal Pradesh.
    def _populate_subdiv_hp_public_holidays(self):
        # Himachal Day.
        self._add_holiday_apr_15(tr("Himachal Day"))

    # Jammu and Kashmir
    def _populate_subdiv_jk_public_holidays(self):
        pass

    # Jharkhand.
    def _populate_subdiv_jh_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))
        # Jharkhand Formation Day.
        self._add_holiday_nov_15(tr("Jharkhand Formation Day"))

    # Karnataka.
    def _populate_subdiv_ka_public_holidays(self):
        # Karnataka Rajyotsav.
        self._add_holiday_nov_1(tr("Karnataka Rajyotsava"))
        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

    # Kerala.
    def _populate_subdiv_kl_public_holidays(self):
        # Onam.
        self._add_onam(tr("Onam"))
        # Kerala Foundation Day.
        self._add_holiday_nov_1(tr("Kerala Foundation Day"))

    # Ladakh.
    def _populate_subdiv_la_public_holidays(self):
        pass

    # Maharashtra.
    def _populate_subdiv_mh_public_holidays(self):
        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))
        # Chhatrapati Shivaji Maharaj Jayanti.
        self._add_holiday_feb_19(tr("Chhatrapati Shivaji Maharaj Jayanti"))

        holi_dates = {
            2026: (MAR, 3),
        }
        # Holi.
        name = tr("Holi")
        if dt := holi_dates.get(self._year):
            self._add_holiday(name, dt)
        else:
            self._add_holi(name)

        # Maharashtra Day.
        self._add_holiday_may_1(tr("Maharashtra Day"))
        # Parsi New Year (Shahenshahi).
        self._add_parsi_new_year(tr("Parsi New Year (Shahenshahi)"))

    # Madhya Pradesh.
    def _populate_subdiv_mp_public_holidays(self):
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
        # Maha Vishuva Sankranti.
        self._add_holiday_apr_15(tr("Maha Vishuva Sankranti / Pana Sankranti"))

    # Puducherry.
    def _populate_subdiv_py_public_holidays(self):
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
        self._add_lohri(tr("Lohri"))
        # New Punjab Day.
        self._add_holiday_nov_1(tr("New Punjab Day"))

    # Rajasthan.
    def _populate_subdiv_rj_public_holidays(self):
        # Rajasthan Day.
        self._add_holiday_mar_30(tr("Rajasthan Day"))
        # Maharana Pratap Jayanti.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap Jayanti"))

    # Sikkim.
    def _populate_subdiv_sk_public_holidays(self):
        # Sikkim State Day.
        self._add_holiday_may_16(tr("Sikkim State Day"))

    # Tamil Nadu.
    def _populate_subdiv_tn_public_holidays(self):
        # Pongal.
        self._add_pongal(tr("Pongal"))
        # Thiruvalluvar Day / Mattu Pongal.
        self._add_thiruvalluvar_day(tr("Thiruvalluvar Day / Mattu Pongal"))
        # Uzhavar Thirunal.
        self._add_uzhavar_thirunal(tr("Uzhavar Thirunal"))
        # Puthandu.
        self._add_holiday_apr_14(tr("Puthandu (Tamil New Year)"))

    # Telangana.
    def _populate_subdiv_ts_public_holidays(self):
        # Telangana Formation Day.
        self._add_holiday_jun_2(tr("Telangana Formation Day"))
        # Bathukamma Festival.
        self._add_bathukamma(tr("Bathukamma Festival"))
        # Bonalu.
        self._add_bonalu(tr("Bonalu"))
        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

    # Uttarakhand.
    def _populate_subdiv_uk_public_holidays(self):
        pass

    # Uttar Pradesh.
    def _populate_subdiv_up_public_holidays(self):
        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))
        # UP Formation Day.
        self._add_holiday_jan_24(tr("UP Formation Day"))

    # West Bengal.
    def _populate_subdiv_wb_public_holidays(self):
        # Pohela Boisakh.
        self._add_holiday_apr_15(tr("Pohela Boishakh"))
        # Rabindra Jayanti.
        self._add_holiday_may_9(tr("Rabindra Jayanti"))


class IN(India):
    pass


class IND(India):
    pass


class IndiaIslamicHolidays(_CustomIslamicHolidays):
    ALI_BIRTHDAY_DATES_CONFIRMED_YEARS = (2001, 2026)
    ALI_BIRTHDAY_DATES = {
        2003: (SEP, 10),
        2018: (APR, 1),
        2024: (JAN, 25),
    }

    ASHURA_DATES_CONFIRMED_YEARS = (2001, 2026)
    ASHURA_DATES = {
        2006: (FEB, 9),
        2008: (JAN, 19),
    }

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2001, 2026)
    EID_AL_ADHA_DATES = {
        2005: (JAN, 21),
        2014: (OCT, 6),
        2015: (SEP, 25),
        2026: (MAY, 27),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2001, 2026)
    EID_AL_FITR_DATES = {
        2006: (OCT, 25),
        2016: (JUL, 6),
    }

    JUMUATUL_WIDA_DATES_CONFIRMED_YEARS = (2001, 2026)
    JUMUATUL_WIDA_DATES = {
        2009: (SEP, 18),
        2010: (SEP, 10),
        2015: (JUL, 17),
        2018: (JUN, 15),
        2023: (APR, 21),
        2026: (MAR, 20),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (2001, 2026)
    MAWLID_DATES = {
        2016: (DEC, 13),
        2017: (DEC, 2),
    }


class IndiaStaticHolidays:
    # Basant Panchami.
    name_basant_panchami = tr("Basant Panchami")

    # Sri Panchami.
    name_sri_panchami = tr("Sri Panchami")

    # Ganesh Chaturthi.
    name_ganesh_chaturthi = tr("Ganesh Chaturthi")

    # Vinayak Chaturthi.
    name_vinayak_chaturthi = tr("Vinayak Chaturthi")

    # Guru Tegh Bahadur's Martyrdom Day.
    name_guru_tegh_bahadur_martyrdom_day = tr("Guru Tegh Bahadur's Martyrdom Day")

    # Magh Bihu.
    name_magh_bihu = tr("Magh Bihu")

    # Janmashtami (Smarta).
    name_janmashtami_smarta = tr("Janmashtami (Smarta)")

    # Guru Gobind Singh's Birthday.
    name_guru_gobind_singh_birthday = tr("Guru Gobind Singh's Jayanti")

    special_public_holidays = {
        # Dussehra (Mahanavami).
        2002: (OCT, 14, tr("Dussehra (Mahanavami)")),
    }

    special_optional_holidays = {
        2002: (DEC, 8, name_guru_tegh_bahadur_martyrdom_day),
        2003: (NOV, 28, name_guru_tegh_bahadur_martyrdom_day),
        2007: (SEP, 3, name_janmashtami_smarta),
        2008: (AUG, 28, name_janmashtami_smarta),
        2011: (DEC, 31, name_guru_gobind_singh_birthday),
        2012: (
            (AUG, 21, name_vinayak_chaturthi),
            (SEP, 19, name_ganesh_chaturthi),
        ),
        2013: (
            (FEB, 14, name_sri_panchami),
            (FEB, 15, name_basant_panchami),
        ),
        2020: (AUG, 11, name_janmashtami_smarta),
        2021: (AUG, 30, name_janmashtami_smarta),
        2022: (AUG, 18, name_janmashtami_smarta),
        2023: (
            (JAN, 14, name_magh_bihu),
            (AUG, 20, name_vinayak_chaturthi),
            (SEP, 6, name_janmashtami_smarta),
            (SEP, 19, name_ganesh_chaturthi),
        ),
        2025: (AUG, 15, name_janmashtami_smarta),
    }
