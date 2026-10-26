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

from holidays.calendars.ethiopian import ETHIOPIAN_CALENDAR
from holidays.constants import GOVERNMENT, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.helpers import tr
from holidays.holiday_base import HolidayBase


class Eritrea(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Eritrea holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Eritrea>
        * <https://web.archive.org/web/20230313234629/https://explore-eritrea.com/working-hours-and-holidays/>
        * <https://web.archive.org/web/20110903130335/http://www.eritrea.be/old/eritrea-religions.htm>
        * <https://web.archive.org/web/20250820085307/https://www.mintageworld.com/media/detail/11411-fenkil-day-in-eritrea/>
        * <https://web.archive.org/web/20261026035656/https://us.embassyeritrea.org/national-dates/>
        * <https://web.archive.org/web/20261026040637/https://asmara.embassy.qa/en/eritrea/official-holidays>
        * <https://web.archive.org/web/20261026040816/https://tigrigna.voanews.com/a/2960404.html>
        * <https://web.archive.org/web/20261026041041/https://tigrigna.voanews.com/a/martrys-day-in-eritrea/7663628.html>
        * <https://web.archive.org/web/20261026041227/https://www.erinewspapers.com/hadas-eritrea/haddas_eritra_28042026.pdf>
        * <https://web.archive.org/web/20260823000041/https://www2.census.gov/programs-surveys/decennial/2020/resources/language-materials/glossaries/Tigrinya-Glossary.pdf>
    """

    country = "ER"
    default_language = "ti"
    supported_languages = ("ar", "en_US", "ti")
    # %s (estimated).
    estimated_label = tr("%s (ግምት)")
    # On 28 May 1993, Eritrea was admitted into the United Nations as the 182nd member state.
    start_year = 1994
    supported_categories = (GOVERNMENT, PUBLIC)

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self, ETHIOPIAN_CALENDAR)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("ሓዲሽ ዓመት"))

        # Orthodox Christmas.
        self._add_christmas_day(tr("ልደት"))

        # Epiphany.
        self._add_epiphany_day(tr("ጥምቀት"))

        # Women's Day.
        self._add_womens_day(tr("መዓልቲ ኣነስቲ"))

        # Good Friday.
        self._add_good_friday(tr("ዓርቢ ስቅለት"))

        # Orthodox Easter.
        self._add_easter_sunday(tr("ፋሲካ"))

        # International Workers' Day.
        self._add_labor_day(tr("ዓለማዊ መዓልቲ ሰራሕተኛታት"))

        # Independence Day.
        self._add_holiday_may_24(tr("መዓልቲ ናጽነት"))

        # Martyrs' Day.
        self._add_holiday_jun_20(tr("መዓልቲ ስውኣት"))

        # Revolution Day.
        self._add_holiday_sep_1(tr("ባሕቲ መስከረም"))

        # Ethiopian New Year.
        self._add_ethiopian_new_year(tr("ሓድሽ ዓመት ግእዝ"))

        # Finding of the True Cross.
        self._add_finding_of_true_cross(tr("መስቀል"))

        # Prophet's Birthday.
        self._add_mawlid_day(tr("መውሊድ"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("ዒድ ኣልፈጥር"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("ዒድ ኣልኣድሓ"))

    def _populate_government_holidays(self):
        # Fenkil Day.
        self._add_holiday_feb_10(tr("ፈንቅል"))


class ER(Eritrea):
    pass


class ERI(Eritrea):
    pass
