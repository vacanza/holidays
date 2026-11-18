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
            * [2021](https://web.archive.org/web/20261121100809/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2021/10/202110170730-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-the-occasion-of-the)
            * 2022:
                * <https://web.archive.org/web/20260422200945/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2022/07/202207260758-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-the-new-hijri-year>
                * <https://web.archive.org/web/20250505095228/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2022/10/202210041300-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-the-occasion-of-the>
            * 2023:
                * <https://web.archive.org/web/20251014225045/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2023/02/202302120730-cbk-will-be-closed-to-the-public-on-19th-of-february-for-al-israa-and-al-miraj>
                * <https://web.archive.org/web/20261121101033/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2023/09/202309270900-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-the-occasion-of-the>
            * 2025:
                * <https://web.archive.org/web/20251223214533/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2025/01/202501260730-cbk-will-be-closed-to-the-public-on-30th-of-january-for-al-israa-and-al-miraj-holiday>
                * <https://web.archive.org/web/20250727031139/https://www.arabtimesonline.com/news/eid-al-fitr-around-the-world>
            * 2026:
                * <https://web.archive.org/web/20260208074324/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2026/01/202601120800-cbk-will-be-closed-to-the-public-on-18th-january-2026-for-al-israa-and-al-miraj>
                * <https://web.archive.org/web/20261031153058/https://gulfnews.com/uae/eid-al-fitr-2026-in-uae-shawwal-crescent-moon-sighting-across-the-world-1.500478348>
                * <https://web.archive.org/web/20261121101430/https://www.arabtimesonline.com/news/16th-june-marks-start-of-islamic-new-year-in-kuwait/>
                * <https://web.archive.org/web/20261121101143/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2026/08/202608190900-cbk-will-be-closed-to-the-public-for-the-occasion-of-the-prophets-birthday>
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
        * [2020](https://web.archive.org/web/20261121100408/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2020/07/202007300734-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-arafat-day-and-eid)
        * 2021:
            * <https://web.archive.org/web/20261121100624/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2021/05/the-central-bank-of-kuwait-will-be-closed-to-the-public-for-eid-al-fitr-holiday>
            * <https://web.archive.org/web/20261121100718/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2021/08/202108040955-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-the-new-hijri-year>
        * 2022:
            * <https://web.archive.org/web/20250508192909/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2022/04/202204261000-the-central-bank-of-kuwait-will-be-closed-to-the-public-sunday-1st-of-may-for-eid>
            * <https://web.archive.org/web/20251212225520/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2022/07/202207070755-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-arafat-day-and-eid>
        * 2023:
            * <https://web.archive.org/web/20260610031317/https://www.moroccoworldnews.com/2023/04/34270/kuwait-announces-friday-as-eid-al-fitr-2023/>
            * <https://web.archive.org/web/20261121101251/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2023/06/202306250700-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-arafat-day-and-eid>
            * <https://web.archive.org/web/20230830055511/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2023/07/202307180800-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-the-new-hijri-year>
        * [2024](https://web.archive.org/web/20260314084851/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2024/04/202404071000-the-central-bank-of-kuwait-will-be-closed-to-the-public-tuesday-9th-of-april-for)
        * [2025](https://web.archive.org/web/20261121101405/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2025/06/202506010700-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-arafat-day-and-eid)
        * 2026:
            * <https://web.archive.org/web/20260810141047/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2026/03/202603170800-cbk-will-be-closed-to-the-public-for-eid-al-fitr-holidays>
            * <https://web.archive.org/web/20260616155234/https://www.cbk.gov.kw/en/cbk-news/announcements-and-press-releases/announcements/2026/05/202605210700-the-central-bank-of-kuwait-will-be-closed-to-the-public-for-arafat-day-and-eid>
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
            (AUG, 8, islamic_new_year),
        ),
        2022: (
            (MAY, 1, eid_al_fitr_holiday),
            (JUL, 12, eid_al_adha_holiday),
            (JUL, 13, eid_al_adha_holiday),
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
