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
from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import CHRISTIAN, HEBREW, PUBLIC, SABIAN, YAZIDI
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    HebrewCalendarHolidays,
)
from holidays.holiday_base import HolidayBase


class Iraq(
    HolidayBase, ChristianHolidays, HebrewCalendarHolidays, InternationalHolidays, IslamicHolidays
):
    """Iraq holidays.

    References:
        - [Law No. 10 of 1963](https://web.archive.org/web/20200220135833/http://wiki.dorar-aliraq.net:80/iraqilaws/law/1447.html)
        - [1968 Amendment to Law No. 10 of 1963](https://web.archive.org/web/20250730075454/https://wiki.dorar-aliraq.net/iraqilaws/law/18741.html)
        - [Law No. 110 of 1972](https://web.archive.org/web/20240820010527/https://wiki.dorar-aliraq.net/iraqilaws/law/5663.html)
        - [1973 Amendment to Law No. 110 of 1973](https://web.archive.org/web/20250730080337/https://wiki.dorar-aliraq.net/iraqilaws/law/6165.html)
        - [Official Holiday Law 2024](https://web.archive.org/web/20250629123214/https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/116577/قانون%20العطل%20الرسمية%20-%20Copy%20-%20Copy_396.pdf)
    """

    country = "IQ"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (المقدرة)")
    start_year = 1964
    supported_categories = (CHRISTIAN, HEBREW, PUBLIC, SABIAN, YAZIDI)
    supported_languages = ("ar", "en_US")

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        HebrewCalendarHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=IraqIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1973:
            # New Year's Day.
            self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Army Day.
        self._add_holiday_jan_6(tr("عيد الجيش"))

        if self._year <= 2024:
            # February 8 Revolution.
            self._add_holiday_feb_8(tr("ثورة 8 شباط"))

        if self._year > 2024:
            # Commemoration of the Saddam Baath crimes against the Iraqi people.
            self._add_holiday_mar_16(tr("ذكرى جرائم البعث والأنفال والهجوم على حلبجة"))

        if self._year >= 1969:
            # Nowruz.
            self._add_holiday_mar_21(tr("عيد نوروز"))

        # Labor Day.
        self._add_labor_day(tr("عيد العمال العالمي"))

        if self._year <= 2023:
            # July 14 Revolution.
            self._add_holiday_jul_14(tr("ثورة 14 تموز"))

        if 1969 <= self._year <= 2023:
            # July 17 Revolution.
            self._add_holiday_jul_17(tr("ثورة 17 تموز"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Ashura.
        self._add_ashura_day(tr("عاشوراء"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("المولد النبوي الشريف"))

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

        if self._year >= 2024:
            # Eid al-Ghadir.
            self._add_eid_al_ghadir_day(tr("عيد الغدير"))

    def _populate_christian_holidays(self):
        if self._year <= 1972:
            # New Year’s Day.
            self._add_new_years_day(tr("رأس السنة الميلادية"))

        # Easter Sunday.
        self._add_easter_sunday(tr("أحد الفصح"))

        # Easter Monday.
        self._add_easter_monday(tr("إثنين الفصح"))

        # Christmas Day.
        self._add_christmas_day(tr("عيد الميلاد"))

    def _populate_hebrew_holidays(self):
        if self._year <= 2023:
            # Pesach.
            self._add_passover(tr("عيد الفصح"), range(2))

            # Yom Kippur.
            self._add_yom_kippur(tr("يوم الكفارة"))

            # Sukkot.
            self._add_sukkot(tr("عيد المظلة"), range(2))

    # 2024 law updates.

    def _populate_sabian_holidays(self):
        # Benja Festival.
        name = tr("يوما عيد البنجة")
        self._add_holiday_apr_5(name)
        self._add_holiday_apr_6(name)

        if self._year >= 2025:
            # Prophet Yahya's Birthday.
            self._add_holiday_may_1(tr("ميلاد النبي يحيى"))

        # Great Feast.
        name = tr("يوما العيد الكبير")
        self._add_holiday_aug_7(name)
        self._add_holiday_aug_8(name)

        # Little Feast.
        self._add_holiday_nov_23(tr("يوم العيد الصغير"))

        # todo: Dehwa Hanina. until 2024

    def _populate_yazidi_holidays(self):
        # todo: Yazidi New Year. 1st Wednesday of April (Julian calendar)

        # todo: Summer Festival. 18-21 Jul until 2023 and 20-21 July 2024 onwards.
        #  (Julian Calendar)

        # todo: Feast of the Assembly. 23-30 Sept (Julian calendar)

        # todo: Feast of Êzî. add First Friday of December (Julian Calendar)
        pass


class IQ(Iraq):
    pass


class IRQ(Iraq):
    pass


class IraqIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20240908214306/https://www.timeanddate.com/holidays/iraq/ashura
    ASHURA_DATES = {
        2013: (NOV, 14),
        2014: (NOV, 3),
        2015: (OCT, 24),
        2016: (OCT, 12),
        2017: (OCT, 1),
        2018: (SEP, 20),
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 19),
        2022: (AUG, 8),
        2023: (JUL, 29),
        2024: (JUL, 16),
        2025: (JUL, 5),
    }

    # https://web.archive.org/web/20250524093010/https://www.timeanddate.com/holidays/iraq/eid-al-adha
    EID_AL_ADHA_DATES = {
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }

    # https://web.archive.org/web/20250514061230/https://www.timeanddate.com/holidays/iraq/eid-al-fitr
    EID_AL_FITR_DATES = {
        2013: (AUG, 8),
        2014: (JUL, 28),
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

    # https://web.archive.org/web/20241009070642/https://www.timeanddate.com/holidays/iraq/eid-al-ghadeer
    EID_AL_GHADIR_DATES = {
        2024: (JUN, 24),
        2025: (JUN, 15),
    }

    # https://web.archive.org/web/20240720191242/https://www.timeanddate.com/holidays/iraq/islamic-new-year
    HIJRI_NEW_YEAR_DATES = {
        2013: (NOV, 5),
        2014: (OCT, 25),
        2015: (OCT, 15),
        2016: (OCT, 3),
        2017: (SEP, 22),
        2018: (SEP, 11),
        2019: (AUG, 31),
        2020: (AUG, 21),
        2021: (AUG, 9),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
        2025: (JUN, 26),
    }

    # https://web.archive.org/web/20240918050148/https://www.timeanddate.com/holidays/iraq/prophet-birthday
    MAWLID_DATES = {
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 23)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 18),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 15),
        2025: (SEP, 4),
    }
