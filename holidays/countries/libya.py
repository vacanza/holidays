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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.holiday_base import HolidayBase


class Libya(HolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """Libya holidays.

    References:
        * [Law No. 4 of 1987](https://web.archive.org/web/20250629084625/https://lawsociety.ly/legislation/%d9%82%d8%a7%d9%86%d9%88%d9%86-%d8%b1%d9%82%d9%85-4-%d9%84%d8%b3%d9%86%d8%a9-1987-%d9%85-%d8%a8%d8%b4%d8%a3%d9%86-%d8%a7%d9%84%d8%b9%d8%b7%d9%84%d8%a7%d8%aa-%d8%a7%d9%84%d8%b1%d8%b3%d9%85%d9%8a%d8%a9/)
        * [Law No. 5 of 2012](https://web.archive.org/web/20250629084558/https://lawsociety.ly/legislation/%d8%a7%d9%84%d9%82%d8%a7%d9%86%d9%88%d9%86-%d8%b1%d9%82%d9%85-5-%d9%84%d8%b3%d9%86%d8%a9-2012-%d9%85-%d8%a8%d8%b4%d8%a3%d9%86-%d8%a7%d9%84%d8%b9%d8%b7%d9%84%d8%a7%d8%aa-%d8%a7%d9%84%d8%b1%d8%b3%d9%85/)
        * [National Environmental Sanitation Day](https://web.archive.org/web/20250629084547/https://lawsociety.ly/legislation/%D9%82%D8%B1%D8%A7%D8%B1-%D8%B1%D9%82%D9%85-414-%D9%84%D8%B3%D9%86%D8%A9-2021-%D9%85-%D8%A8%D8%A7%D8%B9%D8%AA%D8%A8%D8%A7%D8%B1-%D9%8A%D9%88%D9%85-14-%D8%A3%D8%BA%D8%B3%D8%B7%D8%B3-%D9%8A%D9%88/)
    """

    country = "LY"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("(تقدير) %s")
    start_year = 1988
    supported_languages = ("ar", "en_US")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=LibyaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=LibyaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year < 2012:
            # People's Authority Day.
            self._add_holiday_mar_2(tr("عید إعلان سلطة الشعب"))

        if self._year >= 2012:
            # Anniversary of the February 17 Revolution.
            self._add_holiday_feb_17(tr("ثورة 17 فبراير"))

            # Labor Day.
            self._add_labor_day(tr("عيد العمال"))

        if self._year < 2012:
            # American Forces Evacuation Day.
            self._add_holiday_jun_11(tr("عيد إجلاء القوات الأمريكية"))

            # Glorious July Revolution Day.
            self._add_holiday_jul_23(tr("عيد ثورة يوليو المجيدة"))

        if self._year >= 2022:
            # National Environmental Sanitation Day.
            self._add_holiday_aug_14(tr("يوم وطني للإصحاح البيئي"))

        if self._year < 2012:
            # Great Al-Fateh Revolution Day.
            self._add_holiday_sep_1(tr("عيد الفاتح العظيم"))

        if self._year >= 2012:
            # Martyrs' Day.
            self._add_holiday_sep_16(tr("يوم الشهيد"))

            # Liberation Day.
            self._add_holiday_oct_23(tr("يوم التحرير"))

            # Independence Day.
            self._add_holiday_dec_24(tr("عيد الاستقلال"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("ذكرى المولد النبوي الشريف"))

        if self._year >= 2012:
            # Islamic New Year.
            self._add_islamic_new_year_day(tr("عيد رأس السنة الهجرية"))

        # Eid al-Fitr.
        name = tr("عيد الفطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Day of Arafah.
        self._add_arafah_day(tr("يوم عرفة"))

        # Eid al-Adha.
        name = tr("عيد الأضحى")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)


class LY(Libya):
    pass


class LBY(Libya):
    pass


class LibyaIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20240908234803/https://www.timeanddate.com/holidays/libya/eid-al-adha
    # https://web.archive.org/web/20250629084537/https://lawsociety.ly/legislation/%d9%82%d8%b1%d8%a7%d8%b1-%d8%b1%d9%82%d9%85-773-%d9%84%d8%b3%d9%86%d8%a9-2017-%d9%85-%d8%a8%d8%b4%d8%a3%d9%86-%d8%aa%d8%ad%d8%af%d9%8a%d8%af-%d8%b9%d8%b7%d9%84%d8%a9-%d8%b9%d9%8a%d8%af-%d8%a7%d9%84/
    EID_AL_ADHA_DATES = {
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 23),
        2016: (SEP, 11),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }

    # https://web.archive.org/web/20241012125707/https://www.timeanddate.com/holidays/libya/eid-al-fitr
    EID_AL_FITR_DATES = {
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    # https://web.archive.org/web/20250418094505/https://www.timeanddate.com/holidays/libya/muharram-new-year
    HIJRI_NEW_YEAR_DATES = {
        2012: (NOV, 15),
        2013: (NOV, 5),
        2014: (OCT, 25),
        2015: (OCT, 15),
        2016: (OCT, 3),
        2017: (SEP, 22),
        2018: (SEP, 12),
        2019: (AUG, 31),
        2020: (AUG, 20),
        2021: (AUG, 10),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
        2025: (JUN, 26),
    }

    # https://web.archive.org/web/20241213175353/https://www.timeanddate.com/holidays/libya/prophet-birthday
    # https://web.archive.org/web/20250629084607/https://lawsociety.ly/legislation/%D9%82%D8%B1%D8%A7%D8%B1-%D8%B1%D9%82%D9%85-1299-%D9%84%D8%B3%D9%86%D8%A9-2019-%D9%85-%D8%A8%D8%B4%D8%A3%D9%86-%D8%B9%D8%B7%D9%84%D8%A9-%D8%B0%D9%83%D8%B1%D9%89-%D8%A7%D9%84%D9%85%D9%88%D9%84%D8%AF/
    MAWLID_DATES = {
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 23)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
    }


class LibyaStaticHolidays:
    """Libya static holidays.

    References:
        - <https://web.archive.org/web/20250629084721/https://lawsociety.ly/legislation/%d9%82%d8%b1%d8%a7%d8%b1-%d8%b1%d9%82%d9%85-555-%d9%84%d8%b3%d9%86%d8%a9-2023-%d9%85-%d8%a8%d9%85%d9%86%d8%ad-%d8%a5%d8%ac%d8%a7%d8%b2%d8%a9-%d8%b1%d8%b3%d9%85%d9%8a%d8%a9/>
    """

    SPECIAL_PUBLIC_HOLIDAYS = {
        # Public Holiday.
        2023: (DEC, 10, tr("عطلة رسمية"))
    }
