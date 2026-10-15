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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays, StaticHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Pakistan(HolidayBase, InternationalHolidays, IslamicHolidays, StaticHolidays):
    """Pakistan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Pakistan>
        * <https://ur.wikipedia.org/wiki/تعطیلات_پاکستان>
        * [Public and optional holidays](https://web.archive.org/web/20250118105814/https://cabinet.gov.pk/Detail/OTE2ODBiYmItZmI0MS00NDAwLWE5NGUtYmE1MGVjYzllMzAz)
        * [No.10-01/2024-Min-II](https://web.archive.org/web/20241103080918/https://cabinet.gov.pk/SiteImage/Misc/files/Holidays/28-5-24.pdf)
        * [2016 Ashura](https://web.archive.org/web/20260219000903/https://www.sbp.org.pk/bprd/2016/CL32.htm)
        * [2017 Ashura](https://web.archive.org/web/20260207170949/https://www.sbp.org.pk/bprd/2017/CL26.htm)
        * [2019 Ashura](https://web.archive.org/web/20260217233627/https://www.sbp.org.pk/bprd/2019/CL20.htm)
        * [2020 Ashura](https://web.archive.org/web/20260207201644/https://www.sbp.org.pk/bprd/2020/CL39.htm)
        * [2021 Ashura](https://web.archive.org/web/20260219005125/https://www.sbp.org.pk/bprd/2021/CL27.htm)
        * [2023 Ashura](https://web.archive.org/web/20260208115606/https://www.sbp.org.pk/bprd/2023/CL14.htm)
        * [2024 Ashura](https://web.archive.org/web/20260207195440/https://www.sbp.org.pk/bprd/2024/CL14.htm)
        * [2026 Ashura](https://web.archive.org/web/20261009165128/https://www.sbp.org.pk/assets/documents/press-release/Pr-23-Jun-2026.pdf)
    """

    country = "PK"
    default_language = "en_PK"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # Achieved Independence on August 14th, 1947.
    start_year = 1948
    supported_languages = ("en_PK", "en_US", "ur_PK")

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
        StaticHolidays.__init__(self, PakistanStaticHolidays)
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
        if self._year != 2026:
            self._add_eid_al_fitr_day_two(name)
            self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Eid-ul-Adha")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        if self._year not in {2018, 2021, 2026}:
            self._add_eid_al_adha_day_three(name)

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Eid Milad-un-Nabi"))

        # Ashura.
        name = tr("Ashura")
        self._add_ashura_eve(name)
        self._add_ashura_day(name)


class PK(Pakistan):
    pass


class PAK(Pakistan):
    pass


class PakistanIslamicHolidays(_CustomIslamicHolidays):
    # https://web.archive.org/web/20250724060822/https://www.timeanddate.com/holidays/pakistan/ashura
    ASHURA_DATES_CONFIRMED_YEARS = (2005, 2026)
    ASHURA_DATES = {
        2005: (FEB, 18),
        2006: (FEB, 8),
        2007: (JAN, 28),
        2008: (JAN, 18),
        2009: ((JAN, 6), (DEC, 26)),
        2012: (NOV, 23),
        2016: (OCT, 12),
        2017: (OCT, 1),
        2018: (SEP, 21),
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 19),
        2022: (AUG, 9),
        2023: (JUL, 29),
        2024: (JUL, 17),
        2025: (JUL, 6),
        2026: (JUN, 26),
    }

    # https://web.archive.org/web/20250724060629/https://www.timeanddate.com/holidays/pakistan/eid-ul-azha
    # https://web.archive.org/web/20260715114627/https://cabinet.gov.pk/SiteImage/Misc/files/Holidays/2026/Eid-ul-Azha-holidays-Notification-20_05_2026.pdf
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2005, 2026)
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
    # https://web.archive.org/web/20260318213743/https://www.sbp.org.pk/bprd/2026/CL6.htm
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2005, 2026)
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

    # https://dps.psx.com.pk/download/attachment/268947-1.pdf
    JUMUATUL_WIDA_DATES_CONFIRMED_YEARS = (2016, 2026)
    JUMUATUL_WIDA_DATES = {
        2026: (MAR, 20),
    }

    # https://web.archive.org/web/20250724061027/https://www.timeanddate.com/holidays/pakistan/eid-milad-un-nabi
    # https://web.archive.org/web/20261009182535/https://www.sbp.org.pk/circulars/bprd-circular-letter-no-19-of-2025
    # https://web.archive.org/web/20261009165136/https://www.sbp.org.pk/assets/documents/press-release/PR-25-August-2026.pdf
    MAWLID_DATES_CONFIRMED_YEARS = (2005, 2026)
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
        2025: (SEP, 6),
        2026: (AUG, 26),
    }


class PakistanStaticHolidays:
    """Pakistan special holidays.

    References:
        * [2016 Eid-ul-Fitr](https://web.archive.org/web/20200117041303/https://www.sbp.org.pk/bprd/2016/CL23.htm)
        * [2017 Eid-ul-Adha](https://web.archive.org/web/20260208051653/https://www.sbp.org.pk/bprd/2017/CL25.htm)
        * [2018 Eid-ul-Fitr](https://web.archive.org/web/20260207194920/https://www.sbp.org.pk/bprd/2018/CL9.htm)
        * [2018 General Election](https://web.archive.org/web/20260207193245/https://www.sbp.org.pk/bprd/2018/CL11.htm)
        * [2018 Eid-ul-Adha](https://web.archive.org/web/20260208050855/https://www.sbp.org.pk/bprd/2018/CL13.htm)
        * [2019 Eid-ul-Fitr](https://web.archive.org/web/20260208042127/https://www.sbp.org.pk/bprd/2019/CL14.htm)
        * [2019 Eid-ul-Adha](https://web.archive.org/web/20260208105808/https://www.sbp.org.pk/bprd/2019/CL19.htm)
        * [2020 Eid-ul-Fitr](https://web.archive.org/web/20260207202442/https://www.sbp.org.pk/bprd/2020/CL23.htm)
        * [2021 Eid-ul-Fitr](https://web.archive.org/web/20250328235734/https://www.sbp.org.pk/bprd/2021/CL13.htm)
        * [2021 Eid-ul-Adha](https://web.archive.org/web/20260208050427/https://www.sbp.org.pk/bprd/2021/CL25.htm)
        * [2022 Eid-ul-Fitr](https://web.archive.org/web/20260207194649/https://www.sbp.org.pk/bprd/2022/CL14.htm)
        * [2022 Eid-ul-Adha](https://web.archive.org/web/20260208112751/https://www.sbp.org.pk/bprd/2022/CL22.htm)
        * [2023 Eid-ul-Fitr](https://web.archive.org/web/20230427164919/https://www.sbp.org.pk/bprd/2023/CL8.htm)
        * [2023 Eid-ul-Adha](https://web.archive.org/web/20260208054309/https://www.sbp.org.pk/bprd/2023/CL12.htm)
        * [2024 General Election](https://web.archive.org/web/20260219000630/https://www.sbp.org.pk/bprd/2024/CL2.htm)
        * [2025 Eid-ul-Adha](https://web.archive.org/web/20250602130728/https://cabinet.gov.pk/SiteImage/Misc/files/Press%20Release/Eid-ul-Azha-Holidays-02_06_25.pdf)
        * [2026 Eid-ul-Fitr](https://web.archive.org/web/20260318213743/https://www.sbp.org.pk/bprd/2026/CL6.htm)
        * [2026 Eid-ul-Adha](https://web.archive.org/web/20260715114627/https://cabinet.gov.pk/SiteImage/Misc/files/Holidays/2026/Eid-ul-Azha-holidays-Notification-20_05_2026.pdf)
    """

    # Eid al-Adha.
    eid_al_adha = tr("Eid-ul-Adha")

    # Eid al-Fitr.
    eid_al_fitr = tr("Eid-ul-Fitr")

    # General Election Day.
    general_election_day = tr("General Election Day")

    special_public_holidays = {
        2016: (JUL, 5, eid_al_fitr),
        2017: (SEP, 1, eid_al_adha),
        2018: (
            (JUN, 15, eid_al_fitr),
            (JUL, 25, general_election_day),
            (AUG, 21, eid_al_adha),
        ),
        2019: (
            (JUN, 4, eid_al_fitr),
            (AUG, 15, eid_al_adha),
        ),
        2020: (
            (MAY, 22, eid_al_fitr),
            (MAY, 23, eid_al_fitr),
            (MAY, 27, eid_al_fitr),
        ),
        2021: (
            (MAY, 10, eid_al_fitr),
            (MAY, 11, eid_al_fitr),
            (MAY, 12, eid_al_fitr),
            (JUL, 20, eid_al_adha),
        ),
        2022: (
            (MAY, 2, eid_al_fitr),
            (JUL, 8, eid_al_adha),
            (JUL, 9, eid_al_adha),
        ),
        2023: (
            (APR, 21, eid_al_fitr),
            (APR, 25, eid_al_fitr),
            (JUN, 28, eid_al_adha),
        ),
        2024: (FEB, 8, general_election_day),
        2025: (JUN, 6, eid_al_adha),
        2026: (
            (MAR, 20, eid_al_fitr),
            (MAY, 26, eid_al_adha),
        ),
    }
