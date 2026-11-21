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

from datetime import date

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    THU,
    FRI,
    SAT,
)
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Kuwait(HolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """Kuwait holidays.

    References:
        * <https://en.wikipedia.org/wiki/2024_in_Kuwait>
        * <https://web.archive.org/web/20250414072705/https://www.officeholidays.com/countries/kuwait>
        * <https://web.archive.org/web/20250414072609/https://www.timeanddate.com/holidays/kuwait/2024>
        * Islamic holidays:
            * [2021](https://web.archive.org/web/20211006090655/https://www.kuna.net.kw/ArticleDetails.aspx?id=3001029&language=en)
            * 2022:
                * <https://web.archive.org/web/20250725073343/https://www.arabtimesonline.com/news/hijri-new-year-holiday-on-sunday-31st-jul/>
                * <https://web.archive.org/web/20240718232955/https://www.kuna.net.kw/ArticleDetails.aspx?id=3055718&language=en>
            * 2023:
                * <https://web.archive.org/web/20230320191537/https://timeskuwait.com/news/kuwait-sets-feb-19-26-27-as-public-holidays-for-al-israa-wal-miraj-national-day-festivities/>
                * <https://web.archive.org/web/20240617071413/https://gulfnews.com/world/gulf/kuwait/3-day-long-weekend-kuwait-announces-public-holiday-for-prophet-mohammads-birthday-1.1695009657288>
            * 2025:
                * <https://web.archive.org/web/20250325054527/https://www.arabtimesonline.com/news/3-day-official-holiday-for-isra-and-miraj/>
                * <https://web.archive.org/web/20250727031139/https://www.arabtimesonline.com/news/eid-al-fitr-around-the-world>
            * 2026:
                * <https://web.archive.org/web/20260106075038/https://www.arabtimesonline.com/news/csc-announces-holiday-for-isra-and-miraj-on-18th-jan/>
                * <https://web.archive.org/web/20261031153058/https://gulfnews.com/uae/eid-al-fitr-2026-in-uae-shawwal-crescent-moon-sighting-across-the-world-1.500478348>
                * <https://web.archive.org/web/20261121101430/https://www.arabtimesonline.com/news/16th-june-marks-start-of-islamic-new-year-in-kuwait/>
                * <https://web.archive.org/web/20261121161130/https://kuwaittimes.com/article/48004/kuwait/kuwait-csc-declares-thursday-aug-27-official-holiday-for-prophets-birthday/>
    """

    country = "KW"
    default_language = "ar"
    # %s (estimated).
    estimated_label = tr("%s (تقديري)")
    supported_languages = ("ar", "en_US", "ur_PK")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=KuwaitIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, KuwaitStaticHolidays)
        super().__init__(*args, **kwargs)

    def _get_weekend(self, dt: date) -> set[int]:
        # The resting days are Friday and Saturday since Sep 1, 2007.
        # https://web.archive.org/web/20250414072729/https://www.arabnews.com/node/298933
        return {FRI, SAT} if dt >= date(2007, SEP, 1) else {THU, FRI}

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("رأس السنة الميلادية"))

        # National Day.
        self._add_holiday_feb_25(tr("اليوم الوطني"))

        # Liberation Day.
        self._add_holiday_feb_26(tr("يوم التحرير"))

        # Islamic New Year.
        self._add_islamic_new_year_day(tr("رأس السنة الهجرية"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("عيد المولد النبوي"))

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("ليلة المعراج"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("عيد الفطر"))
        # Eid al-Fitr Holiday.
        self._add_eid_al_fitr_day_two(tr("عطلة عيد الفطر"))
        self._add_eid_al_fitr_day_three(tr("عطلة عيد الفطر"))

        # Day of Arafah.
        self._add_arafah_day(tr("يوم عرفة"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عيد الأضحى"))
        # Eid al-Adha Holiday.
        self._add_eid_al_adha_day_two(tr("عطلة عيد الأضحى"))
        self._add_eid_al_adha_day_three(tr("عطلة عيد الأضحى"))


class KW(Kuwait):
    pass


class KWT(Kuwait):
    pass


class KuwaitIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2020, 2026)

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2021, 2026)

    HIJRI_NEW_YEAR_DATES_CONFIRMED_YEARS = (2020, 2026)
    HIJRI_NEW_YEAR_DATES = {
        2022: (JUL, 31),
    }

    ISRA_AND_MIRAJ_DATES_CONFIRMED_YEARS = (2023, 2026)
    ISRA_AND_MIRAJ_DATES = {
        2023: (FEB, 19),
        2025: (JAN, 30),
        2026: (JAN, 18),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (2020, 2026)
    MAWLID_DATES = {
        2021: (OCT, 21),
        2022: (OCT, 9),
        2023: (SEP, 28),
        2026: (AUG, 27),
    }


class KuwaitStaticHolidays:
    """Kuwait special holidays.

    References:
        * [2020](https://web.archive.org/web/20220522170636/https://gulfnews.com/world/gulf/kuwait/eid-al-adha-kuwait-announces-five-day-holiday-1.72729134)
        * 2021:
            * <https://web.archive.org/web/20210521053418/https://gulfnews.com/world/gulf/kuwait/kuwait-eid-al-fitr-holiday-for-5-days-beginning-on-may-12-for-public-sector-1.1620207163109>
            * <https://web.archive.org/web/20260717120656/https://www.arabtimesonline.com/news/islamic-new-year-holiday-on-8th-9th-aug/>
            * <https://web.archive.org/web/20240711190131/https://gulfnews.com/world/gulf/kuwait/kuwait-announces-9-day-holiday-for-eid-al-adha-1.80628033>
        * 2022:
            * <https://web.archive.org/web/20260719215818/https://www.thenationalnews.com/gulf-news/2022/04/15/kuwait-gives-week-long-eid-holiday-for-government-employees>
            * <https://web.archive.org/web/20250722050014/https://www.thenationalnews.com/gulf-news/2022/06/14/eid-al-adha-2022-kuwait-announces-a-nine-day-holiday>
        * 2023:
            * <https://web.archive.org/web/20260610031317/https://www.moroccoworldnews.com/2023/04/34270/kuwait-announces-friday-as-eid-al-fitr-2023/>
            * <https://web.archive.org/web/20250912212848/https://gulfnews.com/world/gulf/kuwait/eid-al-adha-2023-kuwait-announces-six-day-holiday-for-public-sector-1.96255315>
            * <https://web.archive.org/web/20260610125520/https://gulfnews.com/world/gulf/kuwait/kuwaitis-will-have-4-day-long-weekend-to-celebrate-islamic-new-year-1.96898604>
        * [2024](https://web.archive.org/web/20260516203315/https://www.arabtimesonline.com/news/eid-al-fitr-holiday-from-april-9th-work-to-begin-on-14th/)
        * [2025](https://web.archive.org/web/20250727081748/https://www.arabtimesonline.com/news/kuwait-cabinet-declares-eid-holidays-from-june-5-to-9/)
        * 2026:
            * <https://web.archive.org/web/20260311172405/https://www.arabtimesonline.com/news/eid-al-fitr-holiday-officially-set-in-kuwait/>
            * <https://web.archive.org/web/20261121161215/https://www.arabtimesonline.com/news/eid-al-adha-holidays-in-kuwait-from-may-26-31/>
    """

    # Eid al-Fitr Holiday.
    eid_al_fitr_holiday = tr("عطلة عيد الفطر")
    # Eid al-Adha Holiday.
    eid_al_adha_holiday = tr("عطلة عيد الأضحى")
    # Islamic New Year.
    islamic_new_year = tr("رأس السنة الهجرية")

    special_public_holidays = {
        2020: (AUG, 3, eid_al_adha_holiday),
        2021: (
            (MAY, 12, eid_al_fitr_holiday),
            (MAY, 16, eid_al_fitr_holiday),
            (JUL, 18, eid_al_adha_holiday),
            (AUG, 8, islamic_new_year),
        ),
        2022: (
            (MAY, 1, eid_al_fitr_holiday),
            (MAY, 5, eid_al_fitr_holiday),
            (JUL, 12, eid_al_adha_holiday),
            (JUL, 13, eid_al_adha_holiday),
            (JUL, 14, eid_al_adha_holiday),
        ),
        2023: (
            (APR, 24, eid_al_fitr_holiday),
            (APR, 25, eid_al_fitr_holiday),
            (JUL, 2, eid_al_adha_holiday),
            (JUL, 20, islamic_new_year),
        ),
        2024: (APR, 9, eid_al_fitr_holiday),
        2025: (JUN, 9, eid_al_adha_holiday),
        2026: (
            (MAR, 19, eid_al_fitr_holiday),
            (MAR, 23, eid_al_fitr_holiday),
            (MAY, 31, eid_al_adha_holiday),
        ),
    }
