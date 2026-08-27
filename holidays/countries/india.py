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
from holidays.constants import GOVERNMENT, OPTIONAL, OPTIONAL_WOMEN, PUBLIC
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
        * <https://web.archive.org/web/20260618194243/https://www.scribd.com/document/921146658/Govt-Holiday-List-07>
        * <https://web.archive.org/web/20260620201925/https://www.sci.gov.in/calendar>
        * <https://web.archive.org/web/20260620202110/https://bombayhighcourt.nic.in/hccalender.php>
        * <https://web.archive.org/web/20260620202127/https://www.allahabadhighcourt.in/Calendar>
        * Andaman and Nicobar Islands:
            * <https://web.archive.org/web/20251214133200/https://andamannicobar.gov.in/admin-pannel/othersdoc/1-29-Holiday%20List%202026%20Gazette.pdf>
        * Andhra Pradesh:
            * <https://web.archive.org/web/20260608074309/https://www.veerayeehr.com/wp-content/uploads/2025/12/Andhra-Pradesh-Holiday-List-2026.pdf>
        * Arunachal Pradesh:
            * <https://web.archive.org/web/20260822103542/https://only30sec.com/wp-content/uploads/2026/01/Arunachal-Pradesh-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Assam:
            * <https://web.archive.org/web/20260822104103/https://only30sec.com/wp-content/uploads/2025/11/Assam-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Bihar:
            * <https://web.archive.org/web/20260825183642/https://only30sec.com/wp-content/uploads/2025/11/Bihar-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Chandigarh:
            * <https://web.archive.org/web/20260705144831/https://chandigarh.gov.in/files/updation2025/home25-17488-3012.pdf>
        * Dadra and Nagar Haveli and Daman and Diu:
            * <https://web.archive.org/web/20251224204021/https://cdnbbsr.s3waas.gov.in/s371e09b16e21f7b6919bbfc43f6a5b2f0/uploads/2025/12/202512241352239707.pdf>
        * Goa:
            * <https://web.archive.org/web/20260718194348/https://goaprintingpress.gov.in/downloads/2526/2526-28-SII-OG.pdf>
        * Gujarat:
            * <https://web.archive.org/web/20260122052040/https://images-gujarati.indianexpress.com/2025/11/gujarat-government-Year-2026-holiday-list.pdf>
            * [Gujarat Holidays 2010-2026](https://archive.org/details/gujarat-holidays)
        * Haryana:
            * <https://web.archive.org/web/20260704094548/https://haryanacalendar.co.in/wp-content/uploads/2025/12/Haryana-Govt-Official-Notification-2026-PDF.pdf>
        * Himachal Pradesh:
            * <https://web.archive.org/web/20260627103337/https://www.comply360.in/labor-law-library/wp-content/uploads/2025/12/Notification-regarding-list-of-Holidays-for-the-Year-2026-in-Himachal-Pradesh-1.pdf>
        * Jammu and Kashmir:
            * https://web.archive.org/web/20260616165510/https://jkeducation.co.in/wp-content/uploads/2025/12/showOrder-4.pdf>
        * Jharkhand:
            * <https://web.archive.org/web/20260826145700/https://jharkhandcalendar.co.in/wp-content/uploads/2025/12/jaharkand-calendar-2026.pdf>
        * Karnataka:
            * <https://web.archive.org/web/20260822102104/https://only30sec.com/wp-content/uploads/2025/11/Karnataka-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Kerala:
            * <https://web.archive.org/web/20260329164551/https://kerala.gov.in/showcalendar/2026>
            * <https://web.archive.org/web/20260827190400/https://only30sec.com/wp-content/uploads/2025/11/Kerala-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Ladakh:
            * <https://web.archive.org/web/20260627104706/https://www.veerayeehr.com/wp-content/uploads/2025/12/Ladakh-state-list-of-holidays-2026.pdf>
        * Madhya Pradesh:
            * <https://archive.org/details/madhya-pradesh-government-2026-holidays-notification>
        * Maharashtra:
            * <https://web.archive.org/web/20260327070656/https://www.mcgm.gov.in/irj/go/km/docs/documents/HomePage%20Data/Whats%20New/Public%20Holidays%202026.pdf>
        * Manipur:
            * <https://web.archive.org/web/20260822114331/https://www.scribd.com/document/985577686/Manipur-Holiday-List-2026>
        * Meghalaya:
            * <https://web.archive.org/web/20260815172406/https://meghalaya.gov.in/sites/default/files/holiday_files/GAA_78_2025_23.pdf>
        * Mizoram:
            * <https://web.archive.org/web/20260822104707/https://only30sec.com/wp-content/uploads/2025/11/Mizoram-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
            * <https://web.archive.org/web/20260324051214/http://mizoram.nic.in/gov/hols.htm>
        * Nagaland:
            * <https://web.archive.org/web/20260412133333/https://cag.gov.in/uploads/media/Holiday-list-2026-069099b1b46e314-06360641.pdf>
        * Odisha:
            * <https://web.archive.org/web/20260826132225/https://only30sec.com/wp-content/uploads/2025/11/Odisha-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
            * <https://archive.org/details/odisha-government-optional-holidays-list-2026>
        * Punjab:
            * <https://web.archive.org/web/20260216022835/https://punjab.gov.in/wp-content/uploads/2025/12/Calender-2026.pdf>
        * Rajasthan:
            * <https://web.archive.org/web/20260718191708/https://rajasthancalendar.co.in/wp-content/uploads/2025/12/Rajasthan-Govt-Calendar-2026.pdf>
        * Sikkim:
            * <https://web.archive.org/web/20260827185054/https://only30sec.com/wp-content/uploads/2025/11/Sikkim-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Tamil Nadu:
            * [Tamil Monthly Calendar](https://web.archive.org/web/20231228103352/https://www.tamildailycalendar.com/tamil_monthly_calendar.php)
            * [Tamil Calendar](https://web.archive.org/web/20250429125140/https://www.prokerala.com/general/calendar/tamilcalendar.php)
        * Telangana:
            * <https://web.archive.org/web/20260224050455/https://transport.telangana.gov.in/html/registration-districtcodes.html>
            * <https://web.archive.org/web/20250219131214/https://www.thehindu.com/news/national/telangana/cm-firm-on-having-states-identity-as-tg-not-ts/article68187923.ece>
            * <https://web.archive.org/web/20260822101015/https://only30sec.com/wp-content/uploads/2025/12/Telangana-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
        * Tripura:
            * <https://web.archive.org/web/20260821101146/https://hrengage.ai/holiday-list/tripura/2026>
        * Uttar Pradesh:
            * <https://web.archive.org/web/20260714175419/https://ascent-hr.com/wp-content/uploads/2025/12/UP-Holiday-List-2026.pdf>
        * Uttarakhand:
            * <https://web.archive.org/web/20260704120047/https://spiderimg.amarujala.com/assets/applications/2025/12/24/holidays-list-2026_694beebe1007a.pdf>
        * West Bengal:
            * <https://web.archive.org/web/20260825190250/https://only30sec.com/wp-content/uploads/2025/12/West-Bengal-state-Govt.-2026-holidays-list-pdf-Bank-General-Public-Restricted-holidays.pdf>
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
    supported_categories = (GOVERNMENT, OPTIONAL, OPTIONAL_WOMEN, PUBLIC)
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

        if self._year not in self.holi_optional_years and self._normalized_subdiv != "MH":
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

        if self.subdiv == "DD":
            self._populate_subdiv_dh_public_holidays()

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

        if self._normalized_subdiv != "MH":
            self._add_ganesh_chaturthi(
                # Ganesh Chaturthi / Vinayak Chaturthi.
                tr("Ganesh Chaturthi / Vinayak Chaturthi")
                if self._year not in {2012, 2023}
                # Ganesh Chaturthi.
                else tr("Ganesh Chaturthi")
            )

            dates = {
                2012: (AUG, 21),
                2023: (AUG, 20),
            }
            if dt := dates.get(self._year):
                # Vinayak Chaturthi.
                self._add_holiday(tr("Vinayak Chaturthi"), dt)

        # Dussehra (Saptami).
        self._add_maha_saptami(tr("Dussehra (Saptami)"))

        # Dussehra (Mahashtami).
        self._add_maha_ashtami(tr("Dussehra (Mahashtami)"))

        # Dussehra (Mahanavami).
        if self._year != 2002:
            self._add_maha_navami(tr("Dussehra (Mahanavami)"))

        # Maharishi Valmiki's Birthday.
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
            # Pratihar Shashthi or Surya Shashthi (Chhath Puja).
            self._add_chhath_puja(tr("Pratihar Shashthi or Surya Shashthi (Chhath Puja)"))

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
        pass

    def _populate_subdiv_ap_government_holidays(self):
        self._populate_public_holidays()

        # Babu Jagjivan Ram's Birthday.
        self._add_holiday_apr_5(tr("Babu Jagjivan Ram's Jayanti"))

        # Hindu holidays.

        # Bhogi.
        self._add_lohri(tr("Bhogi"))

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        # Kanuma
        self._add_vassi_uttarayan(tr("Kanuma"))

        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

        # Varalakshmi Vratam.
        self._add_varalakshmi_vratam(tr("Varalakshmi Vratam"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Durgashtami.
        self._add_maha_ashtami(tr("Durgashtami"))

    def _populate_subdiv_ap_optional_holidays(self):
        # Boxing Day.
        self._add_holiday_dec_26(tr("Boxing Day"))

        # Islamic holidays.

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Shab-I-Miraj"))

        # Eid al-Ghadir.
        self._add_eid_al_ghadir_day(tr("Eid-e-Ghadeer"))

    # Arunachal Pradesh.
    def _populate_subdiv_ar_public_holidays(self):
        # Statehood Day.
        self._add_holiday_feb_20(tr("Statehood Day"))

        # Indigenous Faith Day.
        self._add_holiday_dec_1(tr("Indigenous Faith Day"))

        # Hindu holidays.

        # Bahag Bihu.
        self._add_vaisakhadi(tr("Bahag Bihu"))

        # Mahashtami.
        self._add_maha_ashtami(tr("Mahashtami"))

    def _populate_subdiv_ar_optional_holidays(self):
        #  Lingri Niki Sii Donyi Polo Yullo.
        self._add_holiday_dec_26(tr("Lingri Niki Sii Donyi Polo Yullo"))

    # Assam.
    def _populate_subdiv_as_public_holidays(self):
        # Netaji Subhas Chandra Bose's Birthday.
        self._add_holiday_jan_23(tr("Netaji Subhas Chandra Bose Jayanti"))

        # May Day.
        self._add_labor_day(tr("May Day"))

        # Hindu holidays.

        # Magh Bihu.
        self._add_pongal(tr("Magh Bihu"))

        # Bahag Bihu.
        self._add_vaisakhadi(tr("Bahag Bihu"))

    def _populate_subdiv_as_optional_holidays(self):
        # Silpi Divas.
        self._add_holiday_jan_17(tr("Silpi Divas"))

        # Gurudev Kalicharan Brahma's Birthday.
        self._add_holiday_apr_18(tr("Gurudev Kalicharan Brahma's Jayanti"))

        # Bishnu Prasad Rabha's Death Anniversary.
        self._add_holiday_jun_20(tr("Bishnu Prasad Rabha's Death Anniversary"))

        # Kut.
        self._add_holiday_nov_1(tr("Kut"))

        # Martyrs' Day.
        self._add_holiday_dec_10(tr("Shaheedi Divas"))

        # Hindu holidays.

        # Wangala Festival.
        self._add_wangala_festival(tr("Wangala Festival"))

    # Bihar.
    def _populate_subdiv_br_public_holidays(self):
        pass

    def _populate_subdiv_br_government_holidays(self):
        # Hindu holidays.

        # Mahasaptami.
        self._add_maha_saptami(tr("Mahasaptami"))

        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))

        # Islamic holidays.

        # Arbaeen.
        self._add_arbaeen_day(tr("Chehlum"))

    def _populate_subdiv_br_optional_holidays(self):
        # Karpuri Thakur's Birthday.
        self._add_holiday_jan_24(tr("Karpuri Thakur's Jayanti"))

        # Rajendra Prasad's Birthday.
        self._add_holiday_dec_3(tr("Rajendra Prasad's Jayanti"))

        # Hindu holidays.

        # Hartalika Teej.
        self._add_hartalika_teej(tr("Hartalika Teej"))

        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))

        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

    # Chandigarh.
    def _populate_subdiv_ch_public_holidays(self):
        # Hindu holidays.

        # Guru Gobind Singh's Birthday.
        self._add_guru_gobind_singh_jayanti(tr("Guru Gobind Singh's Jayanti"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

    def _populate_subdiv_ch_optional_holidays(self):
        # Jor Mela Fatehgarh Sahib.
        name = tr("Jor Mela Fatehgarh Sahib")
        self._add_holiday_dec_26(name)
        self._add_holiday_dec_27(name)
        self._add_holiday_dec_28(name)

        # Hindu holidays.

        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))

        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))

    # Chhattisgarh.
    def _populate_subdiv_cg_public_holidays(self):
        pass

    def _populate_subdiv_cg_government_holidays(self):
        self._populate_public_holidays()

        # International Day of the World's Indigenous Peoples.
        self._add_holiday_aug_9(tr("International Day of Adivasi Peoples"))

        # Guru Ghasidas's Birthday.
        self._add_holiday_dec_18(tr("Guru Ghasidas's Jayanti"))

        # Hindu Holidays.

        # Maa Shakambhari's Birthday.
        self._add_shakambhari_purnima(tr("Maa Shakambhari's Jayanti"))

        # Cherchera.
        self._add_shakambhari_purnima(tr("Cherchera"))

        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))

        # Hareli.
        self._add_hariyali_amavasya(tr("Hareli"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Hartalika Teej.
        self._add_hartalika_teej(tr("Hartalika Teej"))

        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))

    def _populate_subdiv_cg_optional_holidays(self):
        # Savitribai Phule's Birthday.
        self._add_holiday_jan_3(tr("Savitribai Phule's Jayanti"))

        # Gend Singh's Martyrdom Day.
        self._add_holiday_jan_20(tr("Gend Singh's Shaheedi Diwas"))

        # Netaji Subhas Chandra Bose's Birthday.
        self._add_holiday_jan_23(tr("Netaji Subhas Chandra Bose Jayanti"))

        # Veerangana Avantibai's Martyrdom Day.
        self._add_holiday_mar_20(tr("Veerangana Avantibai's Shaheedi Diwas"))

        # Veerangana Durgavati's Martyrdom Day.
        self._add_holiday_jun_24(tr("Veerangana Durgavati's Shaheedi Diwas"))

        # Shaheed Veer Narayan Singh's Martyrdom Day.
        self._add_holiday_dec_1(tr("Shaheed Veer Narayan Singh's Shaheedi Diwas"))

        # Hindu Holidays.

        # Maa Shakambhari's Birthday.
        self._add_shakambhari_purnima(tr("Maa Shakambhari's Jayanti"))

        # Cherchera.
        self._add_shakambhari_purnima(tr("Cherchera"))

        # Shri Vallabhacharya's Birthday.
        self._add_shri_vallabhacharya_jayanti(tr("Shri Vallabhacharya's Jayanti"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Adi Shankaracharya's Birthday.
        self._add_adi_shankaracharya_jayanti(tr("Adi Shankaracharya's Jayanti"))

        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))

        # Mahesh Navami.
        self._add_mahesh_navami(tr("Mahesh Navami"))

        # Naag Panchami.
        self._add_naag_panchami(tr("Naag Panchami"))

        # Harchath.
        self._add_hal_shashthi(tr("Harchath"))

        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

        # Sarva Pitra Moksha Amavasya.
        self._add_pitra_moksh_amavasya(tr("Sarva Pitra Moksha Amavasya"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

        # Maharaj Ajmodh Dev's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharaj Ajmodh Dev's Jayanti"))

        # Sant Guru Tekchand Maharaj Samadhi Utsav.
        self._add_maharshi_valmiki_jayanti(tr("Sant Guru Tekchand Maharaj Samadhi Utsav"))

        # Diwali (South India).
        self._add_diwali_south_india(tr("Deepavali (South India)"))

        # Dattatreya's Birthday.
        self._add_dattatreya_jayanti(tr("Dattatreya's Jayanti"))

    # Dadra and Nagar Haveli and Daman and Diu.
    def _populate_subdiv_dh_public_holidays(self):
        # Hindu Holidays.

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        # Magh Bihu.
        self._add_pongal(tr("Magh Bihu"))

        # Pongal.
        self._add_pongal(tr("Pongal"))

        # Chaitra Sukladi.
        self._add_gudi_padwa(tr("Chaitra Sukladi"))

        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))

        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

        # Cheti Chand.
        self._add_gudi_padwa(tr("Cheti Chand"))

        # Parsi New Year (Shahenshahi).
        self._add_parsi_new_year(tr("Parsi New Year (Shahenshahi)"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Ganesh Chaturthi / Vinayak Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi / Vinayak Chaturthi"))

        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))

        # Pratihar Shashthi or Surya Shashthi (Chhath Puja).
        self._add_chhath_puja(tr("Pratihar Shashthi or Surya Shashthi (Chhath Puja)"))

    # Delhi.
    def _populate_subdiv_dl_public_holidays(self):
        pass

    # Goa.
    def _populate_subdiv_ga_public_holidays(self):
        # Saint Francis Xavier's Day.
        self._add_holiday_dec_3(tr("# Saint Francis Xavier's Day."))

        # Goa Liberation Day.
        self._add_holiday_dec_19(tr("Goa Liberation Day"))

        # Hindu Holidays.

        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Ganesh Chaturthi (2nd Day).
        self._add_ganesh_chaturthi_day_two(tr("Ganesh Chaturthi (2nd Day)"))

    def _populate_subdiv_ga_optional_holidays(self):
        # Saint Joseph Vaz's Day.
        self._add_holiday_jan_16(tr("Saint Joseph Vaz's Day"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))

        # Sacred Heart.
        self._add_holiday_68_days_past_easter(tr("Feast of Sacred Heart of Jesus"))

        # All Souls' Day.
        self._add_all_souls_day(tr("All Souls' Day"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("Feast of Immaculate Conception of Mary"))

        # New Year's Eve.
        self._add_new_years_eve(tr("New Year's Eve"))

    # Gujarat.
    def _populate_subdiv_gj_public_holidays(self):
        # Gujarat Day.
        self._add_holiday_may_1(tr("Gujarat Day"))

        # Sardar Vallabhbhai Patel's Jayanti.
        self._add_holiday_oct_31(tr("Sardar Vallabhbhai Patel's Jayanti"))

        # Hindu holidays.

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Uttarayan"))

        # Cheti Chand.
        self._add_gudi_padwa(tr("Cheti Chand"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Samvatsari Day.
        self._add_samvatsari_parva(tr("Samvatsari Day"))

        # Gujarati New Year.
        self._add_vikram_samvat_new_year(tr("Vikram Samvat New Year"))

        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

        # Parsi New Year (Shahenshahi).
        self._add_parsi_new_year(tr("Parsi New Year (Shahenshahi)"))

    def _populate_subdiv_gj_optional_holidays(self):
        # Hindu holidays.

        # Vassi Uttarayan.
        self._add_vassi_uttarayan(tr("Vassi Uttarayan"))

        # Hatkeshwar's Birthday.
        self._add_hatkeshwar_jayanti(tr("Hatkeshwar's Jayanti"))

        # Hanuman's Birthday.
        self._add_hanuman_jayanti(tr("Hanuman's Jayanti"))

        # Shri Vallabhacharya's Birthday.
        self._add_shri_vallabhacharya_jayanti(tr("Shri Vallabhacharya's Jayanti"))

        # Adi Shankaracharya's Birthday.
        self._add_adi_shankaracharya_jayanti(tr("Adi Shankaracharya's Jayanti"))

        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

        # Samvatsari Day.
        self._add_samvatsari_parva(tr("Samvatsari Day"))

        # Dev Diwali
        self._add_dev_diwali(tr("Dev Diwali"))

    # Haryana.
    def _populate_subdiv_hr_public_holidays(self):
        self._add_holiday_mar_23(
            # Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Martyrdom Day.
            tr("Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Shaheedi Diwas")
        )

        # Shaheed Udham Singh's Martyrdom Day.
        self._add_holiday_jul_31(tr("Shaheed Udham Singh's Shaheedi Diwas"))

        # Haryana War Heroes' Martyrdom Day.
        self._add_holiday_sep_23(tr("Haryana War Heroes' Shaheedi Diwas"))

        # Haryana Day.
        self._add_holiday_nov_1(tr("Haryana Day"))

        # Hindu holidays.

        # Sir Chottu Ram's Birthday.
        self._add_basant_panchami(tr("Sir Chottu Ram's Jayanti"))

        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))

        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))

        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

        # Vishwakarma Day.
        self._add_govardhan_puja(tr("Vishwakarma Day"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Akshay Tritiya.
        self._add_parshuram_jayanti(tr("Akshay Tritiya"))

    def _populate_subdiv_hr_optional_holidays(self):
        # Shaheed Udham Singh's Birthday.
        self._add_holiday_dec_26(tr("Shaheed Udham Singh's Jayanti"))

        # Hindu holidays.

        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

    # Himachal Pradesh.
    def _populate_subdiv_hp_public_holidays(self):
        # Statehood Day.
        self._add_holiday_jan_25(tr("Statehood Day"))

        # Himachal Day.
        self._add_holiday_apr_15(tr("Himachal Day"))

        # Hindu holidays.

        # Guru Ravi Das's Birthday.
        self._add_guru_ravidas_jayanti(tr("Guru Ravi Das's Jayanti"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))

        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

    def _populate_subdiv_hp_optional_women_holidays(self):
        # Hindu holidays.

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Karwa Chouth.
        self._add_karwa_chauth(tr("Karwa Chouth"))

        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

    # Jammu and Kashmir
    def _populate_subdiv_jk_public_holidays(self):
        # Maharaja Hari Singh's Birthday.
        self._add_holiday_sep_23(tr("Maharaja Hari Singh's Jayanti"))

        # Accession Day.
        self._add_holiday_oct_26(tr("Accession Day"))

        # Hindu holidays.

        # 1st Navratra.
        self._add_chaitra_navratri(tr("1st Navratra"))

        # Baisakhi.
        self._add_vaisakhi(tr("Baisakhi"))

        # Mahanavami.
        self._add_maha_navami(tr("Mahanavami"))

        # Islamic holidays.

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Shab-I-Miraj"))

        # Nowruz.
        self._add_nowruz_day(tr("Nauroz"))

    def _populate_subdiv_jk_optional_holidays(self):
        # Hindu holidays.

        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

    # Jharkhand.
    def _populate_subdiv_jh_public_holidays(self):
        # Hindu holidays.

        # Karma Puja.
        self._add_parivartini_ekadashi(tr("Karma Puja"))

        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))

    def _populate_subdiv_jh_government_holidays(self):
        self._populate_public_holidays()

        # Netaji Subhas Chandra Bose's Birthday.
        self._add_holiday_jan_23(tr("Netaji Subhas Chandra Bose Jayanti"))

        # Labor Day.
        self._add_labor_day(tr("Majdoor Diwas"))

        # Hindu holidays.

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        # Rath Yatra.
        self._add_rath_yatra(tr("Rath Yatra"))

        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))

        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))

        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

    # Karnataka.
    def _populate_subdiv_ka_public_holidays(self):
        # May Day.
        self._add_labor_day(tr("May Day"))

        # Hindu holidays.

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        # Ugadi.
        self._add_gudi_padwa(tr("Ugadi"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

    def _populate_subdiv_ka_optional_holidays(self):
        # Holy Saturday.
        self._add_holy_saturday(tr("Holy Saturday"))

        # Hindu holidays.

        # Adi Shankaracharya's Birthday.
        self._add_adi_shankaracharya_jayanti(tr("Adi Shankaracharya's Jayanti"))

        # Varalakshmi Vratam.
        self._add_varalakshmi_vratam(tr("Varalakshmi Vratam"))

        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))

        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

    # Kerala.
    def _populate_subdiv_kl_public_holidays(self):
        # Mannam's Birthday.
        self._add_holiday_jan_2(tr("Mannam's Jayanti"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Maundy Thursday"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # May Day.
        self._add_labor_day(tr("May Day"))

        # Sree Narayana Guru's Death Anniversary.
        self._add_holiday_sep_21(tr("Sree Narayana Guru's Death Anniversary"))

        # Hindu holidays.

        # Vishu.
        self._add_vishu(tr("Vishu"))

        # Onam.
        self._add_onam(tr("Onam"))

        # Onam (Day 2).
        self._add_onam_day_two(tr("Onam (Day 2)"))

        # Onam (Day 3).
        self._add_onam_day_three(tr("Onam (Day 3)"))

        # Onam (Day 4).
        self._add_onam_day_four(tr("Onam (Day 4)"))

        # Mahanavami.
        self._add_maha_navami(tr("Mahanavami"))

    def _populate_subdiv_kl_optional_holidays(self):
        # Hindu holidays.

        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))

    # Ladakh.
    def _populate_subdiv_la_public_holidays(self):
        # Islamic holidays.

        # Nowruz.
        self._add_nowruz_day(tr("Nauroz"))

    def _populate_subdiv_la_optional_holidays(self):
        # Hindu holidays.

        # 1st Navratra.
        self._add_chaitra_navratri(tr("1st Navratra"))

        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))

        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

        # Islamic holidays.

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Shab-I-Miraj"))

        # Eid al-Ghadir.
        self._add_eid_al_ghadir_day(tr("Eid-e-Ghadeer"))

    # Madhya Pradesh.
    def _populate_subdiv_mp_public_holidays(self):
        # Veerangana Avantibai's Martyrdom Day.
        self._add_holiday_mar_20(tr("Veerangana Avantibai's Shaheedi Diwas"))

        # Hindu Holidays.

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))

    def _populate_subdiv_mp_government_holidays(self):
        self._populate_public_holidays()

        # Tribal Pride Day.
        self._add_holiday_nov_15(tr("Janjatiya Gaurav Divas"))

        # Hindu Holidays.

        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))

        # Cheti Chand.
        self._add_gudi_padwa(tr("Cheti Chand"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

        # Govardhan Puja.
        self._add_govardhan_puja(tr("Govardhan Puja"))

    def _populate_subdiv_mp_optional_holidays(self):
        # Hemu Kalani's Martyrdom Day.
        self._add_holiday_jan_21(tr("Hemu Kalani's Shaheedi Diwas"))

        # Mahatma Jyotiba Phule's Birthday.
        self._add_holiday_apr_11(tr("Mahatma Jyotiba Phule's Jayanti"))

        # Veerangana Durgavati's Martyrdom Day.
        self._add_holiday_jun_24(tr("Veerangana Durgavati's Shaheedi Diwas"))

        #  Durgadas Rathore's Birthday.
        self._add_holiday_aug_13(tr("Durgadas Rathore's Jayanti"))

        # International Day of Persons with Disabilities.
        self._add_holiday_dec_3(tr("Vishva Divyang Divas"))

        # Guru Ghasidas's Birthday.
        self._add_holiday_dec_18(tr("Guru Ghasidas's Jayanti"))

        # Hindu Holidays.

        # Maharishi Guru Gokuldas's Birthday.
        self._add_holiday_jan_6(tr("Maharshi Guru Gokuldas's Jayanti"))

        # Lord Meenesh's Birthday.
        self._add_matsya_jayanti(tr("Bhagvan Meenesh's Jayanti"))

        # Shri Vallabhacharya's Birthday.
        self._add_shri_vallabhacharya_jayanti(tr("Shri Vallabhacharya's Jayanti"))

        # Akshay Tritiya.
        self._add_parshuram_jayanti(tr("Akshay Tritiya"))

        # Adi Shankaracharya's Birthday.
        self._add_adi_shankaracharya_jayanti(tr("Adi Shankaracharya's Jayanti"))

        # Mahesh Navami.
        self._add_mahesh_navami(tr("Mahesh Navami"))

        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))

        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))

        # Guru Purnima.
        self._add_guru_purnima(tr("Guru Purnima"))

        # Naag Panchami.
        self._add_naag_panchami(tr("Naag Panchami"))

        # Tulsidas's Birthday.
        self._add_tulsidas_jayanti(tr("Tulsidas's Jayanti"))

        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))

        # Dol Gyaras.
        self._add_parivartini_ekadashi(tr("Dol Gyaras"))

        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

        # Sarva Pitra Moksha Amavasya.
        self._add_pitra_moksh_amavasya(tr("Sarva Pitra Moksha Amavasya"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

        # Maharaj Ajmodh Dev's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharaj Ajmodh Dev's Jayanti"))

        # Sant Guru Tekchand Maharaj Samadhi Utsav.
        self._add_maharshi_valmiki_jayanti(tr("Sant Guru Tekchand Maharaj Samadhi Utsav"))

        # Dattatreya's Birthday.
        self._add_dattatreya_jayanti(tr("Dattatreya's Jayanti"))

    # Maharashtra.
    def _populate_subdiv_mh_public_holidays(self):
        # Chhatrapati Shivaji Maharaj Jayanti.
        self._add_holiday_feb_19(tr("Chhatrapati Shivaji Maharaj Jayanti"))

        # Maharashtra Day.
        self._add_holiday_may_1(tr("Maharashtra Day"))

        # Hindu Holidays.

        # Gudi Padwa.
        self._add_gudi_padwa(tr("Gudi Padwa"))

        holi_dates = {
            2026: (MAR, 3),
        }
        # Holi.
        name = tr("Holi")
        if dt := holi_dates.get(self._year):
            self._add_holiday(name, dt)
        else:
            self._add_holi(name)

        # Parsi New Year (Shahenshahi).
        self._add_parsi_new_year(tr("Parsi New Year (Shahenshahi)"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Diwali (Bali Pratipada).
        self._add_govardhan_puja(tr("Diwali (Bali Pratipada)"))

    # Manipur.
    def _populate_subdiv_mn_public_holidays(self):
        pass

    def _populate_subdiv_mn_government_holidays(self):
        self._populate_public_holidays()

        # Maharaja Gambhir Singh's Death Anniversary.
        self._add_holiday_jan_9(tr("Maharaja Gambhir Singh's Death Anniversary"))

        # Lui Ngai Ni.
        self._add_holiday_feb_15(tr("Lui Ngai Ni"))

        # Khongjom Day.
        self._add_holiday_apr_23(tr("Khongjom Day"))

        # May Day.
        self._add_labor_day(tr("May Day"))

        # Patriot's Day.
        self._add_holiday_aug_13(tr("Patriot's Day"))

        # Kut.
        self._add_holiday_nov_1(tr("Kut"))

        # Hindu Holidays.

        # Holika Dahan.
        self._add_holika_dahan(tr("Holika Dahan"))

        # Rath Yatra.
        self._add_rath_yatra(tr("Rath Yatra"))

        # Mera Chaoren Houba.
        self._add_sharad_navratri(tr("Mera Chaoren Houba"))

    def _populate_subdiv_mn_optional_holidays(self):
        # Players' Day.
        self._add_holiday_feb_25(tr("Players' Day"))

        # Post Christmas.
        self._add_christmas_day_two(tr("Post Christmas"))

        # New Year's Eve.
        self._add_new_years_eve(tr("New Year's Eve"))

    # Meghalaya.
    def _populate_subdiv_ml_public_holidays(self):
        pass

    def _populate_subdiv_ml_government_holidays(self):
        self._populate_public_holidays()

        # U Tirot Sing's Death Anniversary.
        self._add_holiday_jul_17(tr("U Tirot Sing's Death Anniversary"))

        # Seng Kut Snem.
        self._add_holiday_nov_23(tr("Seng Kut Snem"))

        # Pa Togan Nengminja Sangma's Death Anniversary.
        self._add_holiday_dec_12(tr("Pa Togan Nengminja Sangma's Death Anniversary"))

        # U Soso Thama's Death Anniversary.
        self._add_holiday_dec_18(tr("U Soso Thama's Death Anniversary"))

        # Christmas Festival.
        name = "Christmas Festival"
        self._add_christmas_eve(name)
        self._add_christmas_day_two(name)
        self._add_christmas_day_three(name)

        # U Kiang Nongbah Death Anniversary.
        self._add_holiday_dec_30(tr("U Kiang Nongbah Death Anniversary"))

        # Hindu Holidays.

        # Wangala Festival.
        self._add_wangala_festival(tr("Wangala Festival"))

    def _populate_subdiv_ml_optional_holidays(self):
        # All Souls' Day.
        self._add_all_souls_day(tr("All Souls' Day"))

    # Mizoram.
    def _populate_subdiv_mz_public_holidays(self):
        # Post New Year.
        self._add_new_years_day_two(tr("Post New Year"))

        # Missionary Day.
        self._add_holiday_jan_11(tr("Missionary Day"))

        # Young Mizo Association's Day.
        self._add_holiday_jun_15(tr("Young Mizo Association's Day"))

        if self._year >= 1987:
            # Peace Accord Day.
            self._add_holiday_jun_30(tr("Remna Ni"))

        # Mizo Hmeichhe Insuihkhawm Pawl's Day.
        self._add_holiday_jul_6(tr("Mizo Hmeichhe Insuihkhawm Pawl's Day"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Christmas Eve"))

        # Post Christmas.
        self._add_christmas_day_two(tr("Post Christmas"))

        # New Year's Eve.
        self._add_new_years_eve(tr("New Year's Eve"))

    def _populate_subdiv_mz_optional_holidays(self):
        # Zomi Namni.
        self._add_holiday_feb_20(tr("Zomi Namni"))

        # Post Christmas (Day 4).
        self._add_christmas_day_four(tr("Post Christmas (Day 4)"))

    # Nagaland.
    def _populate_subdiv_nl_public_holidays(self):
        pass

    # Orissa / Odisha.
    def _populate_subdiv_od_public_holidays(self):
        pass

    def populate_subdiv_od_government_holidays(self):
        # Netaji Subhas Chandra Bose's Birthday.
        self._add_holiday_jan_23(tr("Netaji Subhas Chandra Bose Jayanti"))

        # Dola Purnima.
        self._add_holika_dahan(tr("Dola Purnima"))

        # Utkal Divas.
        self._add_holiday_apr_1(tr("Utkal Divas"))

        # Maha Visua Sankranti.
        self._add_vaisakhi(tr("Maha Visua Sankranti"))

        # Rath Yatra.
        self._add_rath_yatra(tr("Rath Yatra"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Mahalaya.
        self._add_pitra_moksh_amavasya(tr("Mahalaya"))

        # Mahasaptami.
        self._add_maha_saptami(tr("Mahasaptami"))

        # Mahashtami.
        self._add_maha_ashtami(tr("Mahashtami"))

        # Mahanavami.
        self._add_maha_navami(tr("Mahanavami"))

    # Puducherry.
    def _populate_subdiv_py_public_holidays(self):
        # Puducherry De Jure Transfer Day.
        self._add_holiday_aug_16(tr("Puducherry De Jure Transfer Day"))
        # Puducherry Liberation Day.
        self._add_holiday_nov_1(tr("Puducherry Liberation Day"))

    # Punjab.
    def _populate_subdiv_pb_public_holidays(self):
        self._add_holiday_mar_23(
            # Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Martyrdom Day.
            tr("Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Shaheedi Diwas")
        )

        # Guru Nabha Dass's Birthday.
        self._add_holiday_apr_8(tr("Guru Nabha Dass's Jayanti"))

        # Shaheed Udham Singh's Martyrdom Day.
        self._add_holiday_jul_31(tr("Shaheed Udham Singh's Shaheedi Diwas"))

        # Kartar Singh Sarabha's Martyrdom Day.
        self._add_holiday_nov_16(tr("Kartar Singh Sarabha's Shaheedi Diwas"))

        # Jor Mela Fatehgarh Sahib.
        self._add_holiday_dec_28(tr("Jor Mela Fatehgarh Sahib"))

        # Hindu holidays.

        # Guru Gobind Singh's Birthday.
        self._add_guru_gobind_singh_jayanti(tr("Guru Gobind Singh's Jayanti"))

        # Vaisakhi.
        self._add_vaisakhi(tr("Vaisakhi"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Guru Arjun Dev's Martyrdom Day.
        self._add_guru_arjun_dev_martyrdom_day(tr("Guru Arjun Dev's Shaheedi Diwas"))

        # Sant Kabir's Birthday.
        self._add_kabir_jayanti(tr("Sant Kabir's Jayanti"))

        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

        # Vishwakarma Day.
        self._add_govardhan_puja(tr("Vishwakarma Day"))

        if self._year >= 2004:
            # Guru Tegh Bahadur's Martyrdom Day.
            self._add_holiday_nov_24(tr("Guru Tegh Bahadur's Shaheedi Diwas"))

    def _populate_subdiv_pb_optional_holidays(self):
        # International Women's Day.
        self._add_womens_day(tr("International Women's Day"))

        # Maharaja Ranjit Singh's Death Anniversary.
        self._add_holiday_jun_27(tr("Maharaja Ranjit Singh's Death Anniversary"))

        # Bhagat Singh's Birthday.
        self._add_holiday_sep_28(tr("Bhagat Singh's Jayanti"))

        # Baba Banda Singh Bahadur's Birthday.
        self._add_holiday_oct_16(tr("Baba Banda Singh Bahadur's Jayanti"))

        # New Punjab Day.
        self._add_holiday_nov_1(tr("New Punjab Day"))

        # Saragarhi Day.
        self._add_holiday_sep_12(tr("Saragarhi Day"))

        # Hindu holidays.

        # Lohri.
        self._add_lohri(tr("Lohri"))

        # Satguru Ram Singh's Birthday.
        self._add_basant_panchami(tr("Satguru Ram Singh's Jayanti"))

        # Hola Mohalla.
        self._add_hola_mohalla(tr("Hola Mohalla"))

        # Samvatsari Day.
        self._add_samvatsari_parva(tr("Samvatsari Day"))

        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

    # Rajasthan.
    def _populate_subdiv_rj_public_holidays(self):
        # Mahatma Jyotiba Phule's Birthday.
        self._add_holiday_apr_11(tr("Mahatma Jyotiba Phule's Jayanti"))

        # International Day of the World's Indigenous Peoples.
        self._add_holiday_aug_9(tr("International Day of Adivasi Peoples"))

        # Khejarli's Martyrdom Day.
        self._add_holiday_sep_11(tr("Khejarli's Shaheedi Diwas"))

        # Hindu Holidays.

        # Holika Dahan.
        self._add_holika_dahan(tr("Holika Dahan"))

        # Cheti Chand.
        self._add_gudi_padwa(tr("Cheti Chand"))

        # Lord Shri Parshuram's Birthday.
        self._add_parshuram_jayanti(tr("Bhagvan Shri Parshuram's Jayanti"))

        # Maharana Pratap's Birthday.
        self._add_maharana_pratap_jayanti(tr("Maharana Pratap's Jayanti"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

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
        self._add_holiday_feb_26(
            # Akhil Sikkim Khas Chettri Bahun Kalyan Sangh's Foundation Day
            tr("Akhil Sikkim Khas Chettri Bahun Kalyan Sangh's Foundation Day")
        )

        # Sikkim State Day.
        self._add_holiday_may_16(tr("Sikkim State Day"))

        # Bhanu's Birthday.
        self._add_holiday_jul_13(tr("Bhanu's Jayanti"))

        # Nepali Bhasa Manyata Day.
        self._add_holiday_aug_20(tr("Nepali Bhasa Manyata Diwas"))

        #  Late Nar Bahadur Bhandari's Birthday.
        self._add_holiday_oct_5(tr("Late Nar Bahadur Bhandari's Jayanti"))

        # Hindu holidays.

        # Makar Sankranti.
        self._add_makar_sankranti(tr("Makar Sankranti"))

        # Sonam Lochhar.
        self._add_sonam_losar(tr("Sonam Lochhar"))

        # Hartalika Teej.
        self._add_hartalika_teej(tr("Hartalika Teej"))

        # Tamu Lochhar.
        self._add_tamu_losar(tr("Tamu Lochhar"))

    def _populate_subdiv_sk_optional_holidays(self):
        # May Day.
        self._add_labor_day(tr("May Day"))

        # Late Tenzing Norgay Sherpa's Birthday.
        self._add_holiday_may_29(tr("Late Tenzing Norgay Sherpa's Jayanti"))

        # The Dalai Lama's Birthday.
        self._add_holiday_jul_6(tr("The Dalai Lama's Jayanti"))

        # Drivers' Day.
        self._add_holiday_jul_27(tr("Sarathi Diwas"))

        # Satya Sai Baba of Puttaparthi's Birthday.
        self._add_holiday_nov_23(tr("Satya Sai Baba of Puttaparthi's Jayanti"))

        # Hindu holidays.

        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))

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
        pass

    def _populate_subdiv_ts_government_holidays(self):
        self._populate_public_holidays()

        # Babu Jagjivan Ram's Birthday.
        self._add_holiday_apr_5(tr("Babu Jagjivan Ram's Jayanti"))

        # Boxing Day.
        self._add_holiday_dec_26(tr("Boxing Day"))

        # Hindu holidays.

        # Bonalu.
        self._add_bonalu(tr("Bonalu"))

        # Ganesh Chaturthi.
        self._add_ganesh_chaturthi(tr("Ganesh Chaturthi"))

        # Bathukamma.
        self._add_bathukamma(tr("Bathukamma"))

    def _populate_subdiv_ts_optional_holidays(self):
        # Hindu holidays.

        # Kanuma
        self._add_vassi_uttarayan(tr("Kanuma"))

        # Varalakshmi Vratam.
        self._add_varalakshmi_vratam(tr("Varalakshmi Vratam"))

        # Islamic holidays.

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("Shab-I-Miraj"))

        # Eid al-Ghadir.
        self._add_eid_al_ghadir_day(tr("Eid-e-Ghadeer"))

    # Tripura.
    def _populate_subdiv_tr_public_holidays(self):
        # Netaji Subhas Chandra Bose's Birthday.
        self._add_holiday_jan_23(tr("Netaji Subhas Chandra Bose's Jayanti"))

        # Maharaja Bir Bikram Kishore Manikya Bahadur's Birthday.
        self._add_holiday_aug_19(tr("Maharaja Bir Bikram Kishore Manikya Bahadur's Jayanti"))

        # Hindu holidays.

        # Bengali's New Year.
        self.add_pohela_boishakh(tr("Pohela Boishakh"))

        # Garia Puja.
        self._add_garia_puja(tr("Garia Puja"))

        # Kharchi Puja.
        self._add_kharchi_puja(tr("Kharchi Puja"))

        # Ker Puja.
        self._add_ker_puja(tr("Ker Puja"))

        # Mahasaptami.
        self._add_maha_saptami(tr("Mahasaptami"))

        # Mahashtami.
        self._add_maha_ashtami(tr("Mahashtami"))

    # Uttarakhand.
    def _populate_subdiv_uk_public_holidays(self):
        # Harela.
        self._add_holiday_jul_16(tr("Harela"))

        # Hindu holidays.

        # Holika Dahan.
        self._add_holika_dahan(tr("Holika Dahan"))

        # Cheti Chand.
        self._add_gudi_padwa(tr("Cheti Chand"))

        # Raksha Bandhan.
        self._add_raksha_bandhan(tr("Raksha Bandhan"))

        # Vishwakarma Puja.
        self._add_vishwakarma_puja(tr("Vishwakarma Puja"))

        # Maharishi Valmiki's Birthday.
        self._add_maharshi_valmiki_jayanti(tr("Maharshi Valmiki's Jayanti"))

        if self._year >= 2004:
            # Guru Tegh Bahadur's Martyrdom Day.
            self._add_holiday_nov_24(tr("Guru Tegh Bahadur's Shaheedi Diwas"))

    def _populate_subdiv_uk_optional_holidays(self):
        # Veer Kesari Chand's Martyrdom Day.
        self._add_holiday_may_3(tr("Veer Kesari Chand's Shaheedi Diwas"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Hindu holidays.

        # Anant Chaturdashi.
        self._add_anant_chaturdashi(tr("Anant Chaturdashi"))

        # Maharaj Agrasen's Birthday.
        self._add_sharad_navratri(tr("Maharaj Agrasen's Jayanti"))

        # Islamic holidays.

        # Arbaeen.
        self._add_arbaeen_day(tr("Chehlum"))

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
        self._add_gudi_padwa(tr("Cheti Chand"))
        # Maharishi Kashyap and Maharaj Nishad Raj's Graha Jayanti.
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
        # Swami Vivekananda's Birthday.
        self._add_holiday_jan_12(tr("Swami Vivekananda's Jayanti"))

        # Netaji Subhas Chandra Bose's Birthday.
        self._add_holiday_jan_23(tr("Netaji Subhas Chandra Bose's Jayanti"))

        # May Day.
        self._add_labor_day(tr("May Day"))

        # Birsa Munda's Birthday.
        self._add_holiday_nov_15(tr("Birsa Munda's Jayanti"))

        # Hindu holidays.

        # Bengali's New Year.
        self.add_pohela_boishakh(tr("Pohela Boishakh"))

        # Mahalaya.
        self._add_pitra_moksh_amavasya(tr("Mahalaya"))

        # Mahasaptami.
        self._add_maha_saptami(tr("Mahasaptami"))

        # Mahashtami.
        self._add_maha_ashtami(tr("Mahashtami"))

        # Mahanavami.
        self._add_maha_navami(tr("Mahanavami"))

        # Kali Puja.
        self._add_kali_puja(tr("Kali Puja"))

        # Bhai Duj.
        self._add_bhai_dooj(tr("Bhai Duj"))

        # Chhath Puja.
        self._add_chhath_puja(tr("Chhath Puja"))


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
        2013: (
            (FEB, 14, name_shri_panchami),
            (FEB, 15, name_basant_panchami),
        ),
        2020: (AUG, 11, name_janmashtami_smarta),
        2021: (AUG, 30, name_janmashtami_smarta),
        2022: (AUG, 18, name_janmashtami_smarta),
        2023: (
            (JAN, 14, name_magh_bihu),
            (SEP, 6, name_janmashtami_smarta),
        ),
        2025: (AUG, 15, name_janmashtami_smarta),
    }

    special_as_public_holidays = {
        2023: (JAN, 14, name_magh_bihu),
    }

    special_dh_public_holidays = {
        2023: (JAN, 14, name_magh_bihu),
    }

    special_la_optional_holidays = {
        # Eid al-Ghadir.
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
