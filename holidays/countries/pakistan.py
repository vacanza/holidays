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
from holidays.constants import OPTIONAL, PUBLIC, CHRISTIAN
from holidays.groups import (
    InternationalHolidays,
    IslamicHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    BuddhistCalendarHolidays,
)
from holidays.holiday_base import HolidayBase


class Pakistan(
    HolidayBase,
    InternationalHolidays,
    IslamicHolidays,
    ChristianHolidays,
    HinduCalendarHolidays,
    BuddhistCalendarHolidays,
):
    """Pakistan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Pakistan>
        * <https://ur.wikipedia.org/wiki/تعطیلات_پاکستان>
        * [Public and optional holidays](https://web.archive.org/web/20250118105814/https://cabinet.gov.pk/Detail/OTE2ODBiYmItZmI0MS00NDAwLWE5NGUtYmE1MGVjYzllMzAz)
        * [No.10-01/2024-Min-II](https://web.archive.org/web/20241103080918/https://cabinet.gov.pk/SiteImage/Misc/files/Holidays/28-5-24.pdf)
        * [Public and optional holidays, 2026](https://cabinet.gov.pk/SiteImage/Misc/files/Holidays/2026/Public-Holidays-2026.pdf)
    """

    country = "PK"
    default_language = "en_PK"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # Achieved Independence on August 14th, 1947.
    start_year = 1948
    supported_languages = ("en_PK", "en_US", "ur_PK")
    supported_categories = (OPTIONAL, PUBLIC, CHRISTIAN)

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=PakistanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self)
        BuddhistCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1990:
            # Kashmir Solidarity Day.
            self._add_holiday_feb_5(tr("Kashmir Solidarity Day"))

        if self._year >= 1956:
            # Pakistan Day.
            self._add_holiday_mar_23(tr("Pakistan Day"))

        if self._year >= 1972:
            # Labor Day.
            self._add_labor_day(tr("Labour Day"))

        if self._year >= 2024:
            # Youm-e-Takbeer.
            self._add_holiday_may_28(tr("Youm-e-Takbeer"))

        # Independence Day.
        self._add_holiday_aug_14(tr("Independence Day"))

        if self._year <= 2014 or self._year >= 2022:
            # Iqbal Day.
            self._add_holiday_nov_9(tr("Iqbal Day"))

        # Quaid-e-Azam Day.
        self._add_holiday_dec_25(tr("Quaid-e-Azam Day"))

        # Eid al-Fitr.
        name = tr("Eid-ul-Fitr")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Eid-ul-Adha")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Eid Milad-un-Nabi"))

        # Ashura.
        name = tr("Ashura")
        self._add_ashura_eve(name)
        self._add_ashura_day(name)

    def _populate_optional_holidays(self):

        # New Year's Day
        self._add_new_years_day(tr("New Year's Day"))

        # Islamic optional holidays (estimated)
        if self._year == 2026:
            self._add_holiday(tr("Shab-e-Meraj (estimated)"), JAN, 17)
            self._add_holiday(tr("Shab-e-Barat (estimated)"), FEB, 4)
            self._add_holiday(tr("Chehlum (estimated)"), AUG, 4)
            self._add_holiday(tr("Giyarvee Shareef (estimated)"), SEP, 23)

        # Hindu & Sikh holidays
        self._add_holiday(tr("Basant Panchami"), JAN, 23)
        self._add_holiday(tr("Shiv Ratri"), FEB, 16)
        self._add_holiday(tr("Dulhandi"), MAR, 3)
        self._add_holiday(tr("Holi"), MAR, 4)

        # Christian holidays

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Easter Sunday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # Sikh holidays
        self._add_holiday(tr("Baisakhi"), APR, 14)

        # Bahai holidays
        self._add_holiday(tr("Eid-e-Rizwan (Bahai)"), APR, 21)

        # Buddhist holidays
        self._add_holiday(tr("Buddha Purnima"), MAY, 24)

        # Parsi holidays
        self._add_holiday(tr("Nauroze (Parsi New Year)"), AUG, 15)
        self._add_holiday(tr("Birthday of Lord Zoroaster (Khordad Sal)"), AUG, 20)

        # Hindu holidays
        self._add_holiday(tr("Krishna Janmashtami"), SEP, 4)
        self._add_holiday(tr("Durga Puja"), OCT, 19)
        self._add_holiday(tr("Dussehra"), OCT, 20)
        self._add_holiday(tr("Dussehra Holiday"), OCT, 26)
        self._add_diwali(tr("Diwali"))

        # Sikh holidays
        self._add_holiday(tr("Birthday of Guru Nanak Dev Ji"), NOV, 24)
        self._add_holiday(tr("Birthday of Guru Valmiki Ji"), NOV, 30)

    def _populate_christian_holidays(self):
        # Christmas Day.
        self._add_christmas_day(tr("Christmas Day"))

        # Day after Christmas
        self._add_holiday_dec_26(tr("Day after Christmas"))


class PK(Pakistan):
    pass


class PAK(Pakistan):
    pass


class PakistanIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20250724060822/https://www.timeanddate.com/holidays/pakistan/ashura
    ASHURA_DATES_CONFIRMED_YEARS = (2005, 2025)
    ASHURA_DATES = {
        2005: (FEB, 18),
        2006: (FEB, 8),
        2007: (JAN, 28),
        2008: (JAN, 18),
        2009: ((JAN, 6), (DEC, 26)),
        2012: (NOV, 23),
        2018: (SEP, 21),
        2022: (AUG, 9),
        2025: (JUL, 6),
        2026: ((JUN, 24), (JUN, 25)),
    }

    # https://web.archive.org/web/20250724060629/https://www.timeanddate.com/holidays/pakistan/eid-ul-azha
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2005, 2025)
    EID_AL_ADHA_DATES = {
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2014: (OCT, 6),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
        2026: (MAY, 27),
    }

    # https://web.archive.org/web/20250724060834/https://www.timeanddate.com/holidays/pakistan/eid-ul-fitr-1
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2005, 2025)
    EID_AL_FITR_DATES = {
        2005: (NOV, 4),
        2006: (OCT, 24),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2011: (AUG, 31),
        2014: (JUL, 29),
        2017: (JUN, 26),
        2018: (JUN, 16),
        2019: (JUN, 5),
        2022: (MAY, 3),
        2023: (APR, 22),
        2025: (MAR, 31),
        2026: (MAR, 21),
    }

    # https://web.archive.org/web/20250724061027/https://www.timeanddate.com/holidays/pakistan/eid-milad-un-nabi
    MAWLID_DATES_CONFIRMED_YEARS = (2005, 2024)
    MAWLID_DATES = {
        2005: (APR, 22),
        2006: (APR, 11),
        2008: (MAR, 21),
        2010: (MAR, 1),
        2011: (FEB, 17),
        2012: (FEB, 5),
        2014: (JAN, 14),
        2015: (JAN, 4),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 30),
        2021: (OCT, 19),
        2022: (OCT, 9),
        2023: (SEP, 29),
        2024: (SEP, 17),
        2026: (AUG, 25),
    }
