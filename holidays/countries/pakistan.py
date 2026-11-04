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

    Islamic holidays exact dates:
        * Ashura:
            * [2007](https://web.archive.org/web/20231119045121/https://www.sbp.org.pk/bprd/2007/cl2.htm)
            * [2008](https://web.archive.org/web/20191228084056/http://www.sbp.org.pk/bprd/2008/CL1.htm)
            * [2009 (January)](https://web.archive.org/web/20130419005536/http://www.sbp.org.pk/bprd/2009/CL1.htm)
            * [2009 (December)](https://web.archive.org/web/20130419010531/http://www.sbp.org.pk/bprd/2009/CL40.htm)
            * [2010](https://web.archive.org/web/20190805230624/http://www.sbp.org.pk/bprd/2010/CL30.htm)
            * [2011](https://web.archive.org/web/20190608005606/http://www.sbp.org.pk/bprd/2011/CL25.htm)
            * [2012](https://web.archive.org/web/20200223214918/http://www.sbp.org.pk/bprd/2012/CL26.htm)
            * [2013](https://web.archive.org/web/20200108084144/http://www.sbp.org.pk/bprd/2013/CL28.htm)
            * [2014](https://web.archive.org/web/20200218131658/http://www.sbp.org.pk/bprd/2014/CL32.htm)
            * [2015](https://web.archive.org/web/20180224012335/http://www.sbp.org.pk/bprd/2015/CL30.htm)
            * [2016](https://web.archive.org/web/20260219000903/https://www.sbp.org.pk/bprd/2016/CL32.htm)
            * [2017](https://web.archive.org/web/20260207170949/https://www.sbp.org.pk/bprd/2017/CL26.htm)
            * [2019](https://web.archive.org/web/20260217233627/https://www.sbp.org.pk/bprd/2019/CL20.htm)
            * [2020](https://web.archive.org/web/20260207201644/https://www.sbp.org.pk/bprd/2020/CL39.htm)
            * [2021](https://web.archive.org/web/20260219005125/https://www.sbp.org.pk/bprd/2021/CL27.htm)
            * [2023](https://web.archive.org/web/20260208115606/https://www.sbp.org.pk/bprd/2023/CL14.htm)
            * [2024](https://web.archive.org/web/20260207195440/https://www.sbp.org.pk/bprd/2024/CL14.htm)
            * [2026](https://web.archive.org/web/20261009165128/https://www.sbp.org.pk/assets/documents/press-release/Pr-23-Jun-2026.pdf)
        * Eid Milad-un-Nabi:
            * [2007](https://web.archive.org/web/20191228084641/http://www.sbp.org.pk/bprd/2007/CL12.htm)
            * [2009](https://web.archive.org/web/20130419010552/http://www.sbp.org.pk/bprd/2009/CL6.htm)
            * [2010](https://web.archive.org/web/20190928194525/http://www.sbp.org.pk/bprd/2010/CL4.htm)
            * [2011](https://web.archive.org/web/20190608005339/http://www.sbp.org.pk/bprd/2011/CL2.htm)
            * [2013](https://web.archive.org/web/20200108084024/http://www.sbp.org.pk/bprd/2013/CL1.htm)
            * [2015](https://web.archive.org/web/20180224012356/http://www.sbp.org.pk/bprd/2015/CL35.htm)
        * Eid-ul-Fitr:
            * [2012](https://web.archive.org/web/20200223215054/http://www.sbp.org.pk/bprd/2012/CL20.htm)
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

        In Pakistan, the dates of the Islamic calendar usually fall a day later than
        the corresponding dates in the Umm al-Qura calendar.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self,
            cls=PakistanIslamicHolidays,
            show_estimated=islamic_show_estimated,
            calendar_delta_days=+1,
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
        if self._year not in {2008, 2026}:
            self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Eid-ul-Adha")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        if self._year not in {2008, 2011, 2018, 2021, 2026}:
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
        2013: (NOV, 15),
    }

    # https://web.archive.org/web/20250724060629/https://www.timeanddate.com/holidays/pakistan/eid-ul-azha
    # https://web.archive.org/web/20260715114627/https://cabinet.gov.pk/SiteImage/Misc/files/Holidays/2026/Eid-ul-Azha-holidays-Notification-20_05_2026.pdf
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2005, 2026)
    EID_AL_ADHA_DATES = {
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 6),
        2020: (JUL, 31),
        2026: (MAY, 27),
    }

    # https://web.archive.org/web/20250724060834/https://www.timeanddate.com/holidays/pakistan/eid-ul-fitr-1
    # https://web.archive.org/web/20260318213743/https://www.sbp.org.pk/bprd/2026/CL6.htm
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2005, 2026)
    EID_AL_FITR_DATES = {
        2007: (OCT, 13),
        2010: (SEP, 10),
        2013: (AUG, 8),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2024: (APR, 10),
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
        2023: (SEP, 29),
        2024: (SEP, 17),
        2025: (SEP, 6),
    }


class PakistanStaticHolidays:
    """Pakistan special holidays.

    References:
        * [2007 Eid-ul-Fitr](https://web.archive.org/web/20191228084449/http://www.sbp.org.pk/bprd/2007/CL34.htm)
        * [2008 General Election](https://web.archive.org/web/20191228084203/http://www.sbp.org.pk/bprd/2008/CL3.htm)
        * [2008 Eid-ul-Fitr](https://web.archive.org/web/20191228085439/http://www.sbp.org.pk/bprd/2008/CL27.htm)
        * [2008 Eid-ul-Adha](https://web.archive.org/web/20191228084953/http://www.sbp.org.pk/bprd/2008/CL35.htm)
        * [2008 Benazir Bhutto's Martyrdom](https://web.archive.org/web/20191228084611/http://www.sbp.org.pk/bprd/2008/CL37.htm)
        * [2009 Eid-ul-Adha](https://web.archive.org/web/20130419010103/http://www.sbp.org.pk/bprd/2009/CL36.htm)
        * [2010 Eid-ul-Fitr](https://web.archive.org/web/20190909144700/http://www.sbp.org.pk/bprd/2010/CL22.htm)
        * [2011 Eid-ul-Fitr](https://web.archive.org/web/20190608005504/http://www.sbp.org.pk/bprd/2011/CL19.htm)
        * [2011 Eid-ul-Adha](https://web.archive.org/web/20190608005601/http://www.sbp.org.pk/bprd/2011/CL23.htm)
        * [2012 Youm-e-Ishq-e-Rasool](https://web.archive.org/web/20200223215059/http://www.sbp.org.pk/bprd/2012/CL22.htm)
        * [2012 Eid-ul-Adha](https://web.archive.org/web/20200223215109/http://www.sbp.org.pk/bprd/2012/CL24.htm)
        * [2013 Eid-ul-Adha](https://web.archive.org/web/20200108083310/http://www.sbp.org.pk/bprd/2013/CL25.htm)
        * [2014 Eid-ul-Fitr](https://web.archive.org/web/20180224025142/http://www.sbp.org.pk/bprd/2014/CL24.htm)
        * [2015 Eid-ul-Fitr](https://web.archive.org/web/20180224012254/http://www.sbp.org.pk/bprd/2015/CL21.htm)
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
        2007: (OCT, 16, eid_al_fitr),
        2008: (
            (FEB, 18, general_election_day),
            (OCT, 1, eid_al_fitr),
            (DEC, 8, eid_al_adha),
            # Benazir Bhutto's Martyrdom Day.
            (DEC, 27, tr("Benazir Bhutto's Martyrdom Day")),
        ),
        2009: (NOV, 27, eid_al_adha),
        2010: (SEP, 13, eid_al_fitr),
        2011: (SEP, 3, eid_al_fitr),
        2012: (
            # Love for the Prophet Day.
            (SEP, 21, tr("Youm-e-Ishq-e-Rasool")),
            (OCT, 29, eid_al_adha),
        ),
        2013: (OCT, 18, eid_al_adha),
        2014: (AUG, 1, eid_al_fitr),
        2015: (
            (JUL, 20, eid_al_fitr),
            (JUL, 21, eid_al_fitr),
        ),
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
