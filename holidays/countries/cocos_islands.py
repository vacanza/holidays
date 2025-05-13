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
from holidays.groups import (
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


class CocosIslands(
    ObservedHolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Cocos (Keeling) Islands holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Cocos_(Keeling)_Islands>
        * <https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/community-bulletins>
        * <https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/gazettes-bulletins>

        * [2007](https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2006/02_2006_Public_Holidays_2007_CKI.doc)
        * [2008](https://web.archive.org/web/20240718120923/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2007/06-2007_Public_Holidays_CKI.pdf)
        * [2008 Eid al-Fitr](https://web.archive.org/web/20240331104649/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2008/03_2008_Observance_of_Hari_Raya_Puasa_2008.pdf)
        * [2009](https://web.archive.org/web/20231208153529/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2008/01-2008-2009-public-holiday-CKI-gazette.pdf)
        * [2010](https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2009/2009-Gazette_6-2009-CKI-Proclamation_of_2010_Special_Public_Bank_Holidays.pdf)
        * [2013](https://web.archive.org/web/20240805055409/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2012/2012-Gazette_8-2012-CKI-Proclamation_of_2013_Public_Holidays_for_Cocos_(Keeling)_Islands.pdf)
        * [2014](https://web.archive.org/web/20240718123844/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2013/2013-Gazette_3-2013-Cocos_K_Islands_2014_Public_Holidays.pdf)
        * [2016](https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2015/2015-Gazette_4-2015-CKI-Proclamation_of_2016_Special_Public_Bank_Holidays.pdf)
        * [2016 Eid al-Fitr](https://web.archive.org/web/20231208203746/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2016/2016-Gazette_3-2016-CKI-Proclamation_Special_Public_and_Bank_Holidays_2016.pdf)
        * [2017](https://web.archive.org/web/20240303203132/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_gazette/files/2016/2016-Gazette_2-2016-CKI-Proclamation_Special_Public_and_Bank_Holidays_2017.pdf)
        * [2019](https://web.archive.org/web/20241123131420/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_bulletins/2018/files/A38-2018.pdf)
        * [2019 Act of Self Determination Day](https://web.archive.org/web/20220518200522/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_bulletins/2019/files/A10-2019-bank-holidays.pdf)
        * [2020](https://web.archive.org/web/20240521203357/https://www.infrastructure.gov.au/sites/default/files/migrated/territories/indian_ocean/iot_bulletins/2019/files/A53-2019.pdf)
        * [2021](https://web.archive.org/web/20250502204052/https://www.infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins/2020/A041-2020-cki-public-holidays)
        * [2022](https://web.archive.org/web/20250429071240/https://www.infrastructure.gov.au/sites/default/files/documents/a33-2021-2022-public-holidays-cocos-keeling-islands.pdf)
        * [2022 Eid al-Fitr](https://web.archive.org/web/20220810061351/https://www.infrastructure.gov.au/sites/default/files/documents/Gazette-Change-to-CKI-Hari-Raya-Puasa-2022.pdf)
        * [2023](https://web.archive.org/web/20240711221156/https://www.infrastructure.gov.au/sites/default/files/documents/a19-2022-community-bulletin-2023-kings-birthday-cocos-keeling-islands.pdf)
        * [2023 Eid al-Adha](https://web.archive.org/web/20240804112114/https://www.infrastructure.gov.au/sites/default/files/documents/a06-2023_community_bulletin_-_change_of_public_holiday_date_for_hari_raya_haji_2023.pdf)
        * [2024](https://web.archive.org/web/20250207203100/https://www.infrastructure.gov.au/sites/default/files/documents/a12-2023-2024-public-holidays-cocos-k-islands.pdf)
        * [2025](https://web.archive.org/web/20250413083314/https://www.infrastructure.gov.au/sites/default/files/documents/a21-2024-administrator-community-bulletin-cki-public-holidays-2025.pdf)
    """

    country = "CC"
    default_language = "en_CC"
    # %s (observed).
    observed_label = tr("%s (observed)")
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (observed, estimated)")
    supported_languages = ("coa_CC", "en_CC", "en_US")
    # Act of Self Determination 1984.
    start_year = 1985

    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=CocosIslandsIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, CocosIslandsStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("New Year's Day")))

        # Australia Day.
        self._add_observed(self._add_holiday_jan_26(tr("Australia Day")))

        act_of_self_determination_dates = {
            2007: (APR, 5),
        }
        # Act of Self Determination Day.
        name = tr("Act of Self Determination Day")
        if self._year in act_of_self_determination_dates:
            self._add_holiday(name, act_of_self_determination_dates[self._year])
        else:
            dt = self._add_holiday_apr_6(name)
            if self._year != 2019:
                self._add_observed(dt)

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Easter Monday.
        self._add_easter_monday(tr("Easter Monday"))

        # ANZAC Day.
        self._add_observed(self._add_holiday_apr_25(tr("ANZAC Day")))

        queens_kings_birthday_dates = {
            2021: (JUN, 7),
            2022: (JUN, 6),
            2023: (JUN, 6),
            2024: (JUN, 6),
        }
        name = (
            # King's Birthday.
            tr("King's Birthday")
            if self._year >= 2023
            # Queen's Birthday.
            else tr("Queen's Birthday")
        )
        if self._year in queens_kings_birthday_dates:
            self._add_holiday(name, queens_kings_birthday_dates[self._year])
        else:
            self._add_holiday_2nd_mon_of_jun(name)

        # Placed before Christmas Day for proper observed calculation.
        self._add_observed(
            # Boxing Day.
            self._add_christmas_day_two(tr("Boxing Day")),
            rule=SAT_SUN_TO_NEXT_MON_TUE + MON_TO_NEXT_TUE,
        )

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Christmas Day")))

        # Islamic holidays.

        if self._year <= 2019:
            # Islamic New Year.
            for dt in self._add_islamic_new_year_day(tr("Islamic New Year")):
                self._add_observed(dt)

        # Prophet's Birthday.
        for dt in self._add_mawlid_day(tr("Prophet's Birthday")):
            self._add_observed(dt)

        # Eid al-Fitr.
        for dt in self._add_eid_al_fitr_day(tr("Eid al-Fitr")):
            self._add_observed(dt)

        # Eid al-Adha.
        for dt in self._add_eid_al_adha_day(tr("Eid al-Adha")):
            if self._year != 2025:
                self._add_observed(dt)


class CocosIslandsIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 30),
        2010: (NOV, 16),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2016: (SEP, 13),
        2017: (SEP, 1),
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
        2013: (AUG, 8),
        2014: (JUL, 28),
        2016: (JUL, 6),
        2017: (JUN, 24),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    HIJRI_NEW_YEAR_DATES = {
        2007: (JAN, 22),
        2008: (JAN, 10),
        2009: (DEC, 18),
        2010: (DEC, 7),
        2013: (NOV, 4),
        2014: (OCT, 25),
        2016: (OCT, 3),
        2017: (SEP, 22),
        2019: (SEP, 1),
    }

    MAWLID_DATES = {
        2007: (APR, 2),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2013: (JAN, 24),
        2014: (JAN, 13),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 27),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }


class CC(CocosIslands):
    pass


class CCK(CocosIslands):
    pass


class CocosIslandsStaticHolidays:
    """Cocos (Keeling) Islands special holidays.

    References:
        * [National Day of Mourning 2022](https://web.archive.org/web/20240712213751/https://www.infrastructure.gov.au/sites/default/files/documents/04-2022-proclamation-cki-day-of-mourning.pdf)
    """

    special_public_holidays = {
        # National Day of Mourning for Queen Elizabeth II.
        2022: (SEP, 22, tr("National Day of Mourning for Queen Elizabeth II")),
    }

    special_public_holidays_observed = {
        2019: (APR, 10, tr("Act of Self Determination Day")),
        2025: (JUN, 6, tr("Eid al-Adha")),
    }
