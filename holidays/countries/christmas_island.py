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

<<<<<<< HEAD
from holidays.calendars import _CustomChineseHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, JUN, JUL, AUG, SEP, OCT, NOV
=======
from holidays.calendars import _CustomIslamicHolidays
<<<<<<< HEAD
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
>>>>>>> b356221b (updated test cases and holidays)
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    MON_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_MON_TUE,
)


class ChristmasIsland(
    ObservedHolidayBase,
<<<<<<< HEAD
<<<<<<< HEAD
    ChineseCalendarHolidays,
=======
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
    ChineseCalendarHolidays,
>>>>>>> 63a330eb (fix)
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
<<<<<<< HEAD
<<<<<<< HEAD
):
    """Christmas Island holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Christmas_Island>
        * [2007](https://web.archive.org/web/20250612072036/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2006/01-2006_Public_Holidays_2007_CI.doc)
        * [2008](https://web.archive.org/web/20240224131231/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2007/05-2007_Public_Holidays_CI.pdf)
        * [2008 Hari Raya Puasa](https://web.archive.org/web/20240331104649/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2008/03_2008_Observance_of_Hari_Raya_Puasa_2008.pdf)
=======
    ChineseCalendarHolidays,
=======
>>>>>>> 63a330eb (fix)
):
    """Christmas Island holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Christmas_Island>
        * [2007](https://web.archive.org/web/20250612072036/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2006/01-2006_Public_Holidays_2007_CI.doc)
        * [2008](https://web.archive.org/web/20240224131231/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2007/05-2007_Public_Holidays_CI.pdf)
<<<<<<< HEAD
        * [2008 Hari Raya Puasa Moved](https://web.archive.org/web/20240331104649/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2008/03_2008_Observance_of_Hari_Raya_Puasa_2008.pdf)
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
        * [2008 Hari Raya Puasa](https://web.archive.org/web/20240331104649/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2008/03_2008_Observance_of_Hari_Raya_Puasa_2008.pdf)
>>>>>>> b356221b (updated test cases and holidays)
        * [2009](https://web.archive.org/web/20231211180406/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2008/02-2008_2009_public_holiday_CI_gazette.pdf)
        * [2010](https://web.archive.org/web/20250612051603/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2009/2009-Gazette_5-2009-CI-Proclamation_of_2010_Special_Public_and_Bank_Holidays.pdf)
        * [2013](https://web.archive.org/web/20240805060802/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2012/2012-Gazette_7-2012-CI-Proclamation_of_2013_Public_Holidays_for_Christmas_Island.pdf)
        * [2014](https://web.archive.org/web/20240718175750/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2013/2013-Gazette_2-2013-Christmas_Island_2014_Public_Holidays.pdf)
<<<<<<< HEAD
<<<<<<< HEAD
        * [2016 Hari Raya Puasa](https://web.archive.org/web/20240222235345/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2016/2016-Gazette_4-2016-CI-Proclamation_Special_Public_and_Bank_Holidays_2016.pdf)
<<<<<<< HEAD
=======
        * [2016](https://web.archive.org/web/20250513003407/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2015/2015-Gazette_3-2015-CI-Proclamation_of_2016_Special_Public_Bank_Holidays.pdf)
=======
        * [2016 Hari Raya Puasa](https://web.archive.org/web/20240222235345/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2016/2016-Gazette_4-2016-CI-Proclamation_Special_Public_and_Bank_Holidays_2016.pdf)
>>>>>>> b356221b (updated test cases and holidays)
        * [2016 Update](https://web.archive.org/web/20240222235345/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2016/2016-Gazette_4-2016-CI-Proclamation_Special_Public_and_Bank_Holidays_2016.pdf)
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
>>>>>>> 63a330eb (fix)
        * [2017](https://web.archive.org/web/20240226014639/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2016/2016-Gazette_1-2016-CI-Proclamation_Special_Public_and_Bank_Holidays_2017.pdf)
        * [2019](https://web.archive.org/web/20250517064053/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_bulletins/2018/files/A37-2018.pdf)
        * [2020](https://web.archive.org/web/20240830230128/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_bulletins/2019/files/A52-2019.pdf)
        * [2021](https://web.archive.org/web/20240713155232/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_bulletins/2020/files/a40-ci-public-holidays-2021-proclamation.pdf)
        * [2022](https://web.archive.org/web/20240626092850/https://www.infrastructure.gov.au/sites/default/files/documents/a32-2021-2022-public-holidays-christmas-island.pdf)
        * [2023](https://web.archive.org/web/20250612044842/https://www.infrastructure.gov.au/sites/default/files/documents/A06-2022-notice-proclamation-special-public-bank-holidays-2023-ci.pdf)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        * [2023 Hari Raya Haji](https://web.archive.org/web/20240804112114/https://www.infrastructure.gov.au/sites/default/files/documents/a06-2023_community_bulletin_-_change_of_public_holiday_date_for_hari_raya_haji_2023.pdf)
        * [2024](https://web.archive.org/web/20240519034837/https://www.infrastructure.gov.au/sites/default/files/documents/a11-2023-2024-public-holidays-christmas-island.pdf)
        * [2025](https://web.archive.org/web/20250610185153/https://www.infrastructure.gov.au/sites/default/files/documents/a20-2024-administrator-community-bulletin-ci-public-holidays-2025.pdf)
=======
        * [2024](https://web.archive.org/web/20240519034837/https://www.infrastructure.gov.au/sites/default/files/documents/a11-2023-2024-public-holidays-christmas-island.pdf)
        * [2025](https://web.archive.org/web/20250610185153/https://www.infrastructure.gov.au/sites/default/files/documents/a20-2024-administrator-community-bulletin-ci-public-holidays-2025.pdf)
<<<<<<< HEAD
    
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======

>>>>>>> a1cd8468 (Fix formatting issues and test cases)
=======
        * [2023 Hari Raya Haji](https://web.archiv  e.org/web/20240804112114/https://www.infrastructure.gov.au/sites/default/files/documents/a06-2023_community_bulletin_-_change_of_public_holiday_date_for_hari_raya_haji_2023.pdf)
=======
        * [2023 Hari Raya Haji](https://web.archive.org/web/20240804112114/https://www.infrastructure.gov.au/sites/default/files/documents/a06-2023_community_bulletin_-_change_of_public_holiday_date_for_hari_raya_haji_2023.pdf)
>>>>>>> 304f4511 (fix)
        * [2024](https://web.archive.org/web/20240519034837/https://www.infrastructure.gov.au/sites/default/files/documents/a11-2023-2024-public-holidays-christmas-island.pdf)
        * [2025](https://web.archive.org/web/20250610185153/https://www.infrastructure.gov.au/sites/default/files/documents/a20-2024-administrator-community-bulletin-ci-public-holidays-2025.pdf)
>>>>>>> b356221b (updated test cases and holidays)
    """

    country = "CX"
    default_language = "en_CX"
    # %s (observed).
    observed_label = tr("%s (observed)")
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    supported_languages = ("en_CX", "en_US")
    start_year = 2007

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
<<<<<<< HEAD
        ChineseCalendarHolidays.__init__(self, cls=ChristmasIslandChineseHolidays)
=======
        ChineseCalendarHolidays.__init__(self)
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=ChristmasIslandIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, ChristmasIslandStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Australia Day.
        self._add_observed(self._add_holiday_jan_26(tr("Australia Day")))

        # Chinese New Year.
        name = tr("Chinese New Year")
<<<<<<< HEAD
<<<<<<< HEAD
        if self._year != 2020:
            self._add_observed(self._add_chinese_new_years_day(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
            self._add_observed(
                self._add_chinese_new_years_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE
            )

        # Labor Day.
        name = tr("Labour Day")
        if self._year in {2009, 2010, 2014, 2021, 2025}:
=======
        self._add_observed(self._add_chinese_new_years_day(name))
        self._add_observed(self._add_chinese_new_years_day_two(name))

        # Labor Day.
        name = tr("Labour Day")
<<<<<<< HEAD
        if self._year in (2009, 2010, 2014, 2021, 2022, 2025):
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
        if self._year in {2009, 2010, 2014, 2021, 2022, 2025}:
>>>>>>> 314a5693 (fixed localization for labour day)
=======
        self._add_observed(self._add_chinese_new_years_day(name), rule=SAT_SUN_TO_NEXT_MON_TUE)
        self._add_observed(self._add_chinese_new_years_day_two(name), rule=SAT_SUN_TO_NEXT_MON_TUE)

        # Labor Day.
        name = tr("Labour Day")
        if self._year in {2009, 2010, 2014, 2021, 2025}:
>>>>>>> b356221b (updated test cases and holidays)
            self._add_holiday_4th_mon_of_mar(name)
        else:
            self._add_holiday_3rd_mon_of_mar(name)

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

<<<<<<< HEAD
<<<<<<< HEAD
=======
        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
>>>>>>> b356221b (updated test cases and holidays)
        # ANZAC Day.
        self._add_observed(self._add_anzac_day(tr("ANZAC Day")))

        # Territory Day.
<<<<<<< HEAD
<<<<<<< HEAD
        self._add_holiday_1st_mon_of_oct(tr("Territory Day"))

<<<<<<< HEAD
=======
        self._add_observed(self._add_holiday_oct_6(tr("Territory Day")))
=======
        self._add_holiday_1st_mon_of_oct(tr("Territory Day"))
>>>>>>> b356221b (updated test cases and holidays)

<<<<<<< HEAD
<<<<<<< HEAD
        # Christmas & Boxing Day.
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
        # Boxing Day.
>>>>>>> ab4deaa7 (fixed formatting issues)
=======
>>>>>>> 10239cc7 (formatting)
=======
        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

>>>>>>> 8eba1200 (suggested changes)
        self._add_observed(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE,
        )

<<<<<<< HEAD
        # Christmas Day.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

=======
        
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))
=======
>>>>>>> a1cd8468 (Fix formatting issues and test cases)

=======
>>>>>>> ab4deaa7 (fixed formatting issues)
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
>>>>>>> 8eba1200 (suggested changes)
        # Eid al-Fitr.
        for dt in self._add_eid_al_fitr_day(tr("Hari Raya Puasa")):
            self._add_observed(dt)

<<<<<<< HEAD
<<<<<<< HEAD
        # Eid al-Adha.
        for dt in self._add_eid_al_adha_day(tr("Hari Raya Haji")):
            if self._year not in {2014, 2025}:
                self._add_observed(dt)


class ChristmasIslandChineseHolidays(_CustomChineseHolidays):
    LUNAR_NEW_YEAR_DATES_CONFIRMED_YEARS = (2007, 2023)
    LUNAR_NEW_YEAR_DATES = {
        2007: (FEB, 19),
        2009: (JAN, 27),
        2010: (FEB, 15),
        2023: (JAN, 23),
    }


class ChristmasIslandIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = ((2007, 2010), (2019, 2025))
    EID_AL_ADHA_DATES = {
        2009: (NOV, 30),
=======

=======
>>>>>>> a1cd8468 (Fix formatting issues and test cases)
        # Eid al-Adha.
        for dt in self._add_eid_al_adha_day(tr("Hari Raya Haji")):
            if self._year not in {2014, 2025}:
                self._add_observed(dt)


class ChristmasIslandIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 30),
        2010: (NOV, 16),
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
        2013: (OCT, 15),
        2014: (OCT, 5),
        2016: (SEP, 13),
        2017: (SEP, 1),
<<<<<<< HEAD
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = ((2007, 2010), (2019, 2025))
    EID_AL_FITR_DATES = {
        2007: (OCT, 15),
        2009: (SEP, 21),
=======
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        2007: (OCT, 15),
        2008: (OCT, 1),
        2009: (SEP, 21),
        2010: (SEP, 10),
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
        2013: (AUG, 8),
        2014: (JUL, 28),
        2016: (JUL, 6),
        2017: (JUN, 24),
        2019: (JUN, 5),
<<<<<<< HEAD
        2023: (APR, 22),
        2025: (MAR, 31),
    }
=======
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }
<<<<<<< HEAD
    
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
>>>>>>> a1cd8468 (Fix formatting issues and test cases)


class CX(ChristmasIsland):
    pass


class CXR(ChristmasIsland):
    pass


class ChristmasIslandStaticHolidays:
<<<<<<< HEAD
<<<<<<< HEAD
    """Christmas Island special holidays.
=======
    """Christmas Islands special holidays.
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
    """Christmas Island special holidays.
>>>>>>> ab4deaa7 (fixed formatting issues)

    References:
        * [National Day of Mourning 2022](https://web.archive.org/web/20240712013008/https://www.infrastructure.gov.au/sites/default/files/documents/03-2022-proclamation-ci-day-of-mourning.pdf)
    """

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b356221b (updated test cases and holidays)
    # Chinese New Year.
    chinese_new_year = tr("Chinese New Year")

    # Eid al-Adha.
    eid_al_adha = tr("Hari Raya Haji")

<<<<<<< HEAD
=======
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
    # Eid al-Fitr.
    eid_al_fitr = tr("Hari Raya Puasa")

    # Australia Day.
    australia_day = tr("Australia Day")

    # Christmas Day.
    christmas_day = tr("Christmas Day")

    # Boxing Day.
    boxing_day = tr("Boxing Day")

    # New Year's Day.
    new_years_day = tr("New Year's Day")

>>>>>>> b356221b (updated test cases and holidays)
    special_public_holidays = {
        # National Day of Mourning for Queen Elizabeth II.
        2022: (SEP, 22, tr("National Day of Mourning for Queen Elizabeth II")),
    }
<<<<<<< HEAD

    special_public_holidays_observed = {
<<<<<<< HEAD
        2014: (OCT, 7, eid_al_adha),
        2020: (
            (JAN, 28, chinese_new_year),
            (JAN, 29, chinese_new_year),
        ),
        2025: (JUN, 6, eid_al_adha),
=======
    special_public_holidays_observed = {
<<<<<<< HEAD
        2025: (JUN, 6, tr("Hari Raya Haji")),
>>>>>>> f097c6b9 (Fixed Formatting Issues and tests)
=======
        2013: (
            (FEB, 11, chinese_new_year),
            (FEB, 12, chinese_new_year),
        ),
=======
        2013: (FEB, 12, chinese_new_year),
>>>>>>> 63a330eb (fix)
        2014: (
            (FEB, 3, chinese_new_year),
            (OCT, 7, eid_al_adha),
        ),
        2016: (
            (DEC, 26, christmas_day),
            (DEC, 27, boxing_day),
        ),
        2017: (
            (JAN, 2, new_years_day),
            (JAN, 30, chinese_new_year),
            (JAN, 31, chinese_new_year),
            (JUN, 26, eid_al_fitr),
        ),
        2019: (AUG, 12, eid_al_adha),
        2020: (
            (JAN, 28, chinese_new_year),
            (JAN, 29, chinese_new_year),
            (MAY, 25, eid_al_fitr),
        ),
        2022: (JUL, 11, eid_al_adha),
        2023: (APR, 24, eid_al_fitr),
        2024: (
            (FEB, 12, chinese_new_year),
            (FEB, 13, chinese_new_year),
        ),
        2025: (
            (JUN, 6, eid_al_adha),
            (JAN, 27, australia_day),
        ),
>>>>>>> b356221b (updated test cases and holidays)
    }
