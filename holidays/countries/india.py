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
from holidays.constants import OPTIONAL, PUBLIC, WOMEN_OPTIONAL
from holidays.groups import (
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    PersianCalendarHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class India(
    HolidayBase,
    ChristianHolidays,
    HinduCalendarHolidays,
    InternationalHolidays,
    IslamicHolidays,
    PersianCalendarHolidays,
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
        * Chandigarh:
            * <http://web.archive.org/web/20260705144831/https://chandigarh.gov.in/files/updation2025/home25-17488-3012.pdf>
        * Goa:
            * <https://web.archive.org/web/20260718194348/https://goaprintingpress.gov.in/downloads/2526/2526-28-SII-OG.pdf>
        * Gujarat:
            * <https://web.archive.org/web/20260122052040/https://images-gujarati.indianexpress.com/2025/11/gujarat-government-Year-2026-holiday-list.pdf>
        * Haryana:
            * <https://web.archive.org/web/20260704094548/https://haryanacalendar.co.in/wp-content/uploads/2025/12/Haryana-Govt-Official-Notification-2026-PDF.pdf>
        * Himachal Pradesh:
            * <http://web.archive.org/web/20260627103337/https://www.comply360.in/labor-law-library/wp-content/uploads/2025/12/Notification-regarding-list-of-Holidays-for-the-Year-2026-in-Himachal-Pradesh-1.pdf>
        * Jammu and Kashmir:
            * https://web.archive.org/web/20260616165510/https://jkeducation.co.in/wp-content/uploads/2025/12/showOrder-4.pdf>
        * Kerala:
            * <https://web.archive.org/web/20260329164551/https://kerala.gov.in/showcalendar/2026>
        * Ladakh:
            * <http://web.archive.org/web/20260627104706/https://www.veerayeehr.com/wp-content/uploads/2025/12/Ladakh-state-list-of-holidays-2026.pdf>
        * Maharashtra:
            * <https://web.archive.org/web/20260327070656/https://www.mcgm.gov.in/irj/go/km/docs/documents/HomePage%20Data/Whats%20New/Public%20Holidays%202026.pdf>
        * Punjab:
            * <https://web.archive.org/web/20260216022835/https://punjab.gov.in/wp-content/uploads/2025/12/Calender-2026.pdf>
        * Rajasthan:
            * <https://web.archive.org/web/20260718191708/https://rajasthancalendar.co.in/wp-content/uploads/2025/12/Rajasthan-Govt-Calendar-2026.pdf>
        * Tamil Nadu:
            * [Tamil Monthly Calendar](https://web.archive.org/web/20231228103352/https://www.tamildailycalendar.com/tamil_monthly_calendar.php)
            * [Tamil Calendar](https://web.archive.org/web/20250429125140/https://www.prokerala.com/general/calendar/tamilcalendar.php)
        * Telangana:
            * <https://web.archive.org/web/20260224050455/https://transport.telangana.gov.in/html/registration-districtcodes.html>
            * <https://web.archive.org/web/20250219131214/https://www.thehindu.com/news/national/telangana/cm-firm-on-having-states-identity-as-tg-not-ts/article68187923.ece>
        * Uttar Pradesh:
            * <http://web.archive.org/web/20260714175419/https://ascent-hr.com/wp-content/uploads/2025/12/UP-Holiday-List-2026.pdf>
        * Uttarakhand:
            * <https://web.archive.org/web/20260704120047/https://spiderimg.amarujala.com/assets/applications/2025/12/24/holidays-list-2026_694beebe1007a.pdf>
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
    supported_categories = (OPTIONAL, PUBLIC, WOMEN_OPTIONAL)
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
        PersianCalendarHolidays.__init__(self)
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
            # Basant Panchami / Shri Panchami.
            self._add_basant_panchami(tr("Basant Panchami / Shri Panchami"))

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

        # Maharshi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

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
            self._add_holiday_nov_24(tr("Guru Tegh Bahadur's Shaheedi Diwas"))

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
        # Guru Gobind Singh's Birthday.
        self._add_guru_gobind_singh_jayanti(tr("Guru Gobind Singh's Jayanti"))
        # Maharshi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

    def _populate_subdiv_ch_optional_holidays(self):
        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))
        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))
        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))
        # Jor Mela Fatehgarh Sahib.
        name = tr("Jor Mela Fatehgarh Sahib")
        self._add_holiday_dec_26(name)
        self._add_holiday_dec_27(name)
        self._add_holiday_dec_28(name)

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
        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))
        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))
        # Ganesh Chaturthi (2nd Day).
        self._add_ganesh_chaturthi_day_two(tr("Ganesh Chaturthi (2nd Day)"))
        # Feast of St. Francis Xavier.
        self._add_holiday_dec_3(tr("Feast of St. Francis Xavier"))
        # Goa Liberation Day.
        self._add_holiday_dec_19(tr("Goa Liberation Day"))

    def _populate_subdiv_ga_optional_holidays(self):
        # Feast of St. Joseph Vaz.
        self._add_holiday_jan_16(tr("Feast of St. Joseph Vaz"))
        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))
        # Feast of Sacred Heart of Jesus.
        self._add_holiday_jun_12(tr("Feast of Sacred Heart of Jesus"))
        # All Souls day.
        self._add_all_souls_day(tr("All Souls Day"))
        # Feast of Immaculate Conception of Mary.
        self._add_holiday_dec_8(tr("Feast of Immaculate Conception of Mary"))
        # New Year's Eve.
        self._add_new_years_eve(tr("New Year's Eve"))

    # Gujarat.
    def _populate_subdiv_gj_public_holidays(self):
        # Makar Sankranti.
        self._add_makar_sankranti(tr("Uttarayan"))
        # Cheti Chand.
        self._add_cheti_chand(tr("Cheti Chand"))
        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))
        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))
        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))
        # Sardar Vallabhbhai Patel's Birthday.
        self._add_holiday_oct_31(tr("Sardar Vallabhbhai Patel's Jayanti"))
        # Parsi New Year (Shahenshahi).
        self._add_parsi_new_year(tr("Parsi New Year (Shahenshahi)"))

    # Haryana.
    def _populate_subdiv_hr_public_holidays(self):
        # Sir Chottu Ram's Birthday.
        self._add_basant_panchami(tr("Sir Chottu Ram's Jayanti"))
        # Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Martyrdom Day.
        name = tr("Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Shaheedi Diwas")
        self._add_holiday_mar_23(name)
        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))
        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))
        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))
        # Shaheed Udham Singh's Martyrdom Day.
        self._add_holiday_jul_31(tr("Shaheed Udham Singh's Shaheedi Diwas"))
        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))
        # Haryana War Heroes's Martyrdom Day.
        self._add_holiday_sep_23(tr("Haryana War Heroes's Shaheedi Diwas"))
        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))
        # Maharshi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))
        # Vishwakarma Day.
        self._add_govardhan_puja(tr("Vishwakarma Day"))
        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))
        # Akshay Tritiya.
        self._add_parshuram_jayanti(tr("Akshay Tritiya"))
        # Haryana Day.
        self._add_holiday_nov_1(tr("Haryana Day"))

    def _populate_subdiv_hr_optional_holidays(self):
        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))
        # Shaheed Udham Singh's Birthday.
        self._add_holiday_dec_26(tr("Shaheed Udham Singh's Jayanti"))

    # Himachal Pradesh.
    def _populate_subdiv_hp_public_holidays(self):
        # Statehood Day.
        self._add_holiday_jan_25(tr("Statehood Day"))
        # Guru Ravi Das's Birthday.
        self._add_guru_ravidas_jayanti(tr("Guru Ravi Das's Jayanti"))
        # Himachal Day.
        self._add_holiday_apr_15(tr("Himachal Day"))
        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))
        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))
        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))
        # Maharshi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

    def _populate_subdiv_hp_women_optional_holidays(self):
        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))
        # Karwa Chouth.
        self._add_karwa_chauth(tr("Karwa Chouth"))
        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

    # Jammu and Kashmir
    def _populate_subdiv_jk_public_holidays(self):
        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Shab-I-Miraj"))
        # 1st Navratra.
        self._add_chaitra_navratri(tr("1st Navratra"))
        # Nowruz.
        self._add_nowruz_day(tr("Nauroz"))
        # Baisakhi.
        self._add_vaisakhi(tr("Baisakhi"))
        # Mahanavami.
        self._add_maha_navami(tr("Mahanavami"))
        # Maharaja Hari Singh's Birthday.
        self._add_holiday_sep_23(tr("Maharaja Hari Singh's Jayanti"))
        # Accession Day.
        self._add_holiday_oct_26(tr("Accession Day"))

    def _populate_subdiv_jk_optional_holidays(self):
        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

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
        # Nowruz.
        self._add_nowruz_day(tr("Nauroz"))

    def _populate_subdiv_la_optional_holidays(self):
        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Shab-I-Miraj"))
        # 1st Navratra.
        self._add_chaitra_navratri(tr("1st Navratra"))
        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))
        # Baisakhi.
        self._add_vaisakhi(tr("Baisakhi"))
        # Eid al-Ghadeer.
        self._add_eid_al_ghadir_day(tr("Eid-e-Ghadeer"))
        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

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
        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))
        # Diwali (Bali Pratipada).
        self._add_govardhan_puja(tr("Diwali (Bali Pratipada)"))

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
        # Guru Gobind Singh's Birthday.
        self._add_guru_gobind_singh_jayanti(tr("Guru Gobind Singh's Jayanti"))
        # Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Martyrdom Day.
        self._add_holiday_mar_23(
            tr("Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Shaheedi Diwas")
        )
        # Guru Nabha Dass's Birthday.
        self._add_holiday_apr_8(tr("Guru Nabha Dass's Jayanti"))
        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))
        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))
        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))
        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))
        # Shaheed Udham Singh's Martyrdom Day.
        self._add_holiday_jul_31(tr("Shaheed Udham Singh's Shaheedi Diwas"))
        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))
        # Maharshi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))
        # Vishwakarma Day.
        self._add_govardhan_puja(tr("Vishwakarma Day"))
        # Kartar Singh Sarabha's Martyrdom Day.
        self._add_holiday_nov_16(tr("Kartar Singh Sarabha's Shaheedi Diwas"))
        if self._year >= 2004:
            # Guru Tegh Bahadur's Martyrdom Day.
            self._add_holiday_nov_24(tr("Guru Tegh Bahadur's Shaheedi Diwas"))
        # Jor Mela Fatehgarh Sahib.
        self._add_holiday_dec_28(tr("Jor Mela Fatehgarh Sahib"))

    def _populate_subdiv_pb_optional_holidays(self):
        # Lohri.
        self._add_lohri(tr("Lohri"))
        # Satguru Ram Singh's Birthday.
        self._add_basant_panchami(tr("Satguru Ram Singh's Jayanti"))
        # International Women's Day.
        self._add_womens_day(tr("International Women's Day"))
        # Hola Mohalla.
        self._add_hola_mohalla(tr("Hola Mohalla"))
        # Maharaja Ranjit Singh's Death Anniversary.
        self._add_holiday_jun_27(tr("Maharaja Ranjit Singh's Death Anniversary"))
        # Saragarhi Day.
        self._add_holiday_sep_12(tr("Saragarhi Day"))
        # Samvatsari Day.
        self._add_samvatsari_parva(tr("Samvatsari Day"))
        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))
        # Bhagat Singh's Birthday.
        self._add_holiday_sep_28(tr("Bhagat Singh's Jayanti"))
        # Baba Banda Singh Bahadur's Birthday.
        self._add_holiday_oct_16(tr("Baba Banda Singh Bahadur's Jayanti"))
        # New Punjab Day.
        self._add_holiday_nov_1(tr("New Punjab Day"))

    # Rajasthan.
    def _populate_subdiv_rj_public_holidays(self):
        # Holika Dahan.
        self._add_holika_dahan(tr("Holika Dahan"))
        # Cheti Chand.
        self._add_cheti_chand(tr("Cheti Chand"))
        # Mahatma Jyotiba Phule's Birthday.
        self._add_holiday_apr_11(tr("Mahatma Jyotiba Phule's Jayanti"))
        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))
        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))
        # International Day of the World's Indigenous Peoples.
        self._add_holiday_aug_9(tr("International Day of Adivasi Peoples"))
        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))
        # Khejarli's Martyrdom Day.
        self._add_holiday_sep_11(tr("Khejarli's Shaheedi Day"))
        # Sharad Navratri.
        self._add_sharad_navratri(tr("Sharad Navratri"))
        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))
        # Durgashtami.
        self._add_maha_ashtami(tr("Durgashtami"))
        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))
        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

    def _populate_subdiv_rj_optional_holidays(self):
        # Gadge Maharaj's Birthday.
        self._add_holiday_feb_23(tr("Gadge Maharaj's Jayanti"))
        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

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
        # Holika Dahan.
        self._add_holika_dahan(tr("Holika Dahan"))
        # Cheti Chand.
        self._add_cheti_chand(tr("Cheti Chand"))
        # Harela.
        self._add_holiday_jul_16(tr("Harela"))
        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))
        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))
        # Maharshi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))
        if self._year >= 2004:
            # Guru Tegh Bahadur's Martyrdom Day.
            self._add_holiday_nov_24(tr("Guru Tegh Bahadur's Shaheedi Diwas"))

    def _populate_subdiv_uk_optional_holidays(self):
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))
        # Veer Kesari Chand's Martyrdom Day.
        self._add_holiday_may_3(tr("Veer Kesari Chand's Shaheedi Diwas"))
        # Arbaaen.
        self._add_arbaeen_day(tr("Chehlum"))
        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))
        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))

    # Uttar Pradesh.
    def _populate_subdiv_up_public_holidays(self):
        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))
        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))
        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))
        # Chitragupt's Birthday.
        self._add_bhai_dooj(tr("Chitragupt's Jayanti"))

    def _populate_subdiv_up_optional_holidays(self):
        # Karpuri Thakur's Birthday.
        self._add_holiday_jan_24(tr("Karpuri Thakur's Jayanti"))
        # Cheti Chand.
        self._add_cheti_chand(tr("Cheti Chand"))
        # Maharshi Kashyap and Maharaj Nishad Raj's Graha Jayanti.
        self._add_holiday_apr_5(tr("Maharshi Kashyap and Maharaj Nishad Raj's Graha Jayanti"))
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))
        # Chandrashekhar's Birthday.
        self._add_holiday_apr_17(tr("Chandrashekhar's Jayanti"))
        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))
        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))
        # Arbaaen.
        self._add_arbaeen_day(tr("Chehlum"))
        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))
        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))
        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))
        # Sardar Vallabhbhai Patel's Birthday.
        self._add_holiday_oct_31(tr("Sardar Vallabhbhai Patel's Jayanti"))
        # Acharya Narendra Dev's Birthday.
        self._add_holiday_oct_31(tr("Acharya Narendra Dev's Jayanti"))
        # Veerangana Uda Devi's Martyrdom Day.
        self._add_holiday_nov_16(tr("Veerangana Uda Devi's Shaheedi Diwas"))
        # Chaudhary Charan Singh's Birthday.
        self._add_holiday_dec_23(tr("Chaudhary Charan Singh's Jayanti"))

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

    # Shri Panchami.
    name_shri_panchami = tr("Shri Panchami")

    # Ganesh Chaturthi.
    name_ganesh_chaturthi = tr("Ganesh Chaturthi")

    # Vinayak Chaturthi.
    name_vinayak_chaturthi = tr("Vinayak Chaturthi")

    # Guru Tegh Bahadur's Martyrdom Day.
    name_guru_tegh_bahadur_martyrdom_day = tr("Guru Tegh Bahadur's Shaheedi Diwas")

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
            (FEB, 14, name_shri_panchami),
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

    special_la_optional_holidays = {
        # Eid al-Ghadeer.
        2026: (JUN, 4, tr("Eid-e-Ghadeer")),
    }

    special_pb_public_holidays = {
        2002: (DEC, 8, name_guru_tegh_bahadur_martyrdom_day),
        2003: (NOV, 28, name_guru_tegh_bahadur_martyrdom_day),
    }

    special_uk_public_holidays = {
        2002: (DEC, 8, name_guru_tegh_bahadur_martyrdom_day),
        2003: (NOV, 28, name_guru_tegh_bahadur_martyrdom_day),
    }
