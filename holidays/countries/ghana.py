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
from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, JUL, AUG, SEP, DEC
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class Ghana(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """Ghana holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Ghana>
        * [Public Holidays Act, 2001 (Act 601)](https://web.archive.org/web/20260418042037/https://ghalii.org/akn/gh/act/2001/601/eng@2001-06-01)
        * [Public Holidays (Amendment) Act, 2002 (Act 626)](https://archive.org/details/public-holidays-amendment-act_2002)
        * [Public Holidays (Amendment) Act, 2019 (Act 986)](https://archive.org/details/public-holidays-amendment-act_2019)
        * [Founder's Day history](https://web.archive.org/web/20260730221237/https://repository.parliament.gh/server/api/core/bitstreams/7c2b97d5-a492-43e3-9fb0-999c7a7aadbd/content)
        * [2020 Farmers' Day](https://web.archive.org/web/20260413024626/https://www.mint.gov.gh/declaration-of-monday-7th-december-2020-as-public-holiday-by-substitution-of-the-4th-december-2020-holiday-farmers-day/)
        * [2025](https://web.archive.org/web/20250915194425/https://www.mint.gov.gh/statutory-public-holidays/)
        * [2026](https://web.archive.org/web/20260526175503/https://www.mint.gov.gh/statutory-public-holidays/)

    Islamic holidays exact dates:
        * [Eid al-Fitr 2017](https://web.archive.org/web/20260207014840/https://www.mint.gov.gh/declaration-of-monday-26th-june-2017-as-a-public-holiday/)
        * [Eid al-Adha 2017](https://web.archive.org/web/20260421162520/https://www.mint.gov.gh/declaration-of-friday-1st-september-2017-as-a-public-holiday/)
        * [Eid al-Fitr 2018](https://web.archive.org/web/20260217002901/https://www.mint.gov.gh/declaration-of-friday-15th-june-2018-as-a-statutory-public-holiday/)
        * [Eid al-Adha 2018](https://web.archive.org/web/20260410123822/https://www.mint.gov.gh/declaration-of-tuesday-21st-august-2018-as-a-statutory-public-holiday/)
        * [Eid al-Fitr 2019](https://web.archive.org/web/20260421175024/https://www.mint.gov.gh/declaration-of-wednesday-5th-june-2019-as-a-statutory-public-holiday/)
        * [Eid al-Adha 2019](https://web.archive.org/web/20260412234950/https://www.mint.gov.gh/declaration-of-monday-12th-august-2019-as-a-public-holiday/)
        * [Eid al-Fitr 2020](https://web.archive.org/web/20260419235525/https://www.mint.gov.gh/declaration-of-monday-25th-may-2020-as-a-public-holiday/)
        * [Eid al-Adha 2020](https://web.archive.org/web/20260412234522/https://www.mint.gov.gh/declaration-of-friday-july-31-2020-as-public-holiday-eid-al-adha/)
        * [Eid al-Fitr 2021](https://web.archive.org/web/20260413104455/https://www.mint.gov.gh/declaration-of-thursday-13th-may-2021-as-a-statutory-public-holiday/)
        * [Eid al-Adha 2021](https://web.archive.org/web/20260413031358/https://www.mint.gov.gh/declaration-of-tuesday-20th-july-2021-as-a-statutory-public-holiday/)
        * [Eid al-Fitr 2022](https://web.archive.org/web/20260519094152/https://www.mint.gov.gh/declaration-of-tuesday-3rd-may-2022-as-a-statutory-public-holiday/)
        * [Eid al-Adha 2022](https://web.archive.org/web/20260519103218/https://www.mint.gov.gh/declaration-of-monday-11th-july-2022-as-a-public-holiday/)
        * [Eid al-Fitr 2023](https://web.archive.org/web/20260511210513/https://www.mint.gov.gh/declaration-of-monday-24th-april-2023-as-a-public-holiday/)
        * [Eid al-Adha 2023](https://web.archive.org/web/20260216224230/https://www.mint.gov.gh/declaration-of-wednesday-28th-june-2023-as-a-statutory-public-holiday/)
        * [Eid al-Fitr 2024](https://web.archive.org/web/20260216233856/https://www.mint.gov.gh/declaration-of-thursday-11th-april-2024-as-a-statutory-public-holiday/)
        * [Eid al-Adha 2024](https://web.archive.org/web/20260511204439/https://www.mint.gov.gh/declaration-of-monday-17th-june-2024-as-a-public-holiday/)
        * [Eid al-Adha 2025](https://web.archive.org/web/20260413113948/https://www.mint.gov.gh/declaration-of-friday-6th-june-2025-as-a-public-holiday/)
        * [Eid al-Adha 2026](https://web.archive.org/web/20260730221245/https://www.mint.gov.gh/declaration-of-wednesday-27th-may-2026-as-a-public-holiday/)
    """

    country = "GH"
    estimated_label = "%s (estimated)"
    # Public Holidays Act, 2001.
    start_year = 2002

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=GhanaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=GhanaStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day("New Year's Day")

        # In 2019 declared as additional holiday by President Executive Instrument.
        # Since 2020 statutory holiday by Public Holidays (Amendment) Act, 2019.

        # Constitution Day.
        if self._year >= 2019:
            self._add_holiday_jan_7("Constitution Day")

        # Independence Day.
        self._add_holiday_mar_6("Independence Day")

        # Good Friday.
        self._add_good_friday("Good Friday")

        # Easter Monday.
        self._add_easter_monday("Easter Monday")

        # Renamed by Public Holidays and Commemorative Days (Amendment) Act, 2025.

        # Labour Day / Workers' Day.
        self._add_labor_day("Labour Day" if self._year >= 2026 else "Workers' Day")

        # Established by Public Holidays (Amendment) Act, 2002.
        # Abolished by Public Holidays (Amendment) Act, 2019.

        # African Union Day.
        if 2002 <= self._year <= 2019:
            self._add_africa_day("African Union Day")

        # Abolished by Public Holidays (Amendment) Act, 2019.
        # Restored by Public Holidays and Commemorative Days (Amendment) Act, 2025.

        # Republic Day.
        if self._year <= 2018 or self._year >= 2025:
            self._add_holiday_jul_1("Republic Day")

        # Established by Public Holidays (Amendment) Act, 2019.
        # Abolished by Public Holidays and Commemorative Days (Amendment) Act, 2025.

        # Founders' Day.
        if 2019 <= self._year <= 2024:
            self._add_holiday_aug_4("Founders' Day")

        # Since 2009 declared as additional holiday by President Executive Instrument.
        # Established with new name by Public Holidays (Amendment) Act, 2019.
        # Renamed by Public Holidays and Commemorative Days (Amendment) Act, 2025.

        if self._year >= 2009:
            self._add_holiday_sep_21(
                "Kwame Nkrumah Memorial Day" if 2019 <= self._year <= 2024 else "Founder's Day"
            )

        # Farmers' Day.
        name = "Farmers' Day"
        dates = {
            2020: (DEC, 7),
        }
        if dt := dates.get(self._year):
            self._add_holiday(name, dt)
        else:
            self._add_holiday_1st_fri_of_dec(name)

        # Christmas Day.
        self._add_christmas_day("Christmas Day")

        # Boxing Day.
        self._add_christmas_day_two("Boxing Day")

        # Eid al-Fitr.
        self._add_eid_al_fitr_day("Eid-ul-Fitr")

        # Established by Public Holidays and Commemorative Days (Amendment) Act, 2025.

        if self._year >= 2026:
            # Shaqq Day.
            self._add_eid_al_fitr_day_two("Shaqq Day")

        # Eid al-Adha.
        self._add_eid_al_adha_day("Eid-ul-Adha")


class GH(Ghana):
    pass


class GHA(Ghana):
    pass


class GhanaIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2017, 2026)

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2017, 2026)
    EID_AL_FITR_DATES = {
        2017: (JUN, 26),
        2019: (JUN, 5),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 11),
    }


class GhanaStaticHolidays:
    """Ghana special holidays.

    References:
        * [Jul 3, 2017 holiday](https://web.archive.org/web/20260415221610/https://www.mint.gov.gh/declaration-of-monday-july-3-2017-as-public-holiday-republic-day/)
        * [Jul 2, 2018 holiday](https://web.archive.org/web/20260420002730/https://www.mint.gov.gh/declaration-of-monday-july-2-2018-as-a-public-holiday/)
        * [Aug 5, 2019 holiday](https://web.archive.org/web/20260216165635/https://www.mint.gov.gh/declaration-of-monday-5th-august-2019-as-a-public-holiday/)
        * [Aug 12, 2019 holiday](https://web.archive.org/web/20260412234950/https://www.mint.gov.gh/declaration-of-monday-12th-august-2019-as-a-public-holiday/)
        * [Sep 23, 2019 holiday](https://web.archive.org/web/20260412232606/https://www.mint.gov.gh/declaration-of-monday-23rd-september-2019-as-a-public-holiday/)
        * [May 25, 2020 holiday](https://web.archive.org/web/20260419235525/https://www.mint.gov.gh/declaration-of-monday-25th-may-2020-as-a-public-holiday/)
        * [Dec 28, 2020 holiday](https://web.archive.org/web/20260412231557/https://www.mint.gov.gh/declaration-of-friday-25th-december-2020-monday-28th-december-2020-and-friday-1st-january-2021-as-public-holidays/)
        * [Mar 8, 2021 holiday](https://web.archive.org/web/20260413111222/https://www.mint.gov.gh/declaration-of-monday-8th-march-2021-as-a-public-holiday/)
        * [May 3, 2021 holiday](https://web.archive.org/web/20260519103903/https://www.mint.gov.gh/declaration-of-monday-3rd-may-2021-as-a-public-holiday/)
        * [Dec 27 & 28, 2021 holiday](https://web.archive.org/web/20260413104530/https://www.mint.gov.gh/declaration-of-monday-27th-december-and-tuesday-28th-december-2021-as-a-public-holiday/)
        * [Jan 3, 2022 holiday](https://web.archive.org/web/20260421165622/https://www.mint.gov.gh/declaration-of-monday-3rd-january-2022-as-a-public-holiday/)
        * [Mar 7, 2022 holiday](https://web.archive.org/web/20260513062303/https://www.mint.gov.gh/declaration-of-monday-march-7-2022-as-a-public-holiday/)
        * [May 2, 2022 holiday](https://web.archive.org/web/20260413012055/https://www.mint.gov.gh/declaration-of-monday-2nd-may-2022-as-a-public-holiday/)
        * [Jul 11, 2022 holiday](https://web.archive.org/web/20260519103218/https://www.mint.gov.gh/declaration-of-monday-11th-july-2022-as-a-public-holiday/)
        * [Dec 27, 2022 holiday](https://web.archive.org/web/20260519092510/https://www.mint.gov.gh/declaration-of-tuesday-27th-december-2022-as-a-public-holiday/)
        * [Jan 2, 2023 holiday](https://web.archive.org/web/20260217000202/https://www.mint.gov.gh/declaration-of-monday-2nd-january-2023-as-a-public-holiday/)
        * [Jan 9, 2023 holiday](https://web.archive.org/web/20260216170322/https://www.mint.gov.gh/declaration-of-monday-9th-january-2023-as-a-public-holiday/)
        * [Apr 24, 2023 holiday](https://web.archive.org/web/20260511210513/https://www.mint.gov.gh/declaration-of-monday-24th-april-2023-as-a-public-holiday/)
        * [Jan 8, 2024 holiday](https://web.archive.org/web/20260120115839/https://www.mint.gov.gh/declaration-of-monday-8th-january-2024-as-a-public-holiday/)
        * [Jun 17, 2024 holiday](https://web.archive.org/web/20260511204439/https://www.mint.gov.gh/declaration-of-monday-17th-june-2024-as-a-public-holiday/)
        * [Aug 5, 2024 holiday](https://web.archive.org/web/20260519100836/https://www.mint.gov.gh/declaration-of-monday-5th-august-2024-as-a-public-holiday/)
        * [Sep 23, 2024 holiday](https://web.archive.org/web/20260310100519/https://www.mint.gov.gh/declaration-of-monday-23rd-september-2024-as-a-public-holiday/)
        * [Mar 31 & Apr 1, 2025 holiday](https://web.archive.org/web/20260306060842/https://www.mint.gov.gh/declaration-of-monday-31st-march-2025-and-tuesday-1st-april-2025-as-public-holidays/)
        * [Jul 4, 2025 holiday](https://web.archive.org/web/20260513224136/https://www.mint.gov.gh/declaration-of-friday-4th-july-2025-as-a-public-holiday/)
        * [Sep 22, 2025 holiday](https://web.archive.org/web/20260124124232/https://www.mint.gov.gh/declaration-of-monday-22nd-september-2025-as-a-public-holiday/)
        * [Jan 9, 2026 holiday](https://web.archive.org/web/20260510090514/https://www.mint.gov.gh/declaration-of-friday-9th-january2026-as-a-public-holiday/)
        * [Jul 3, 2026 holiday](https://web.archive.org/web/20260717133104/https://www.mint.gov.gh/declaration-of-friday-3rd-july-2026-as-a-public-holiday/)
    """

    # Public Holiday.
    public_holiday = "Public Holiday"

    special_public_holidays = {
        2017: (JUL, 3, public_holiday),
        2018: (JUL, 2, public_holiday),
        2019: (
            (AUG, 5, public_holiday),
            (AUG, 12, public_holiday),
            (SEP, 23, public_holiday),
        ),
        2020: (
            (MAY, 25, public_holiday),
            (DEC, 28, public_holiday),
        ),
        2021: (
            (MAR, 8, public_holiday),
            (MAY, 3, public_holiday),
            (DEC, 27, public_holiday),
            (DEC, 28, public_holiday),
        ),
        2022: (
            (JAN, 3, public_holiday),
            (MAR, 7, public_holiday),
            (MAY, 2, public_holiday),
            (JUL, 11, public_holiday),
            (DEC, 27, public_holiday),
        ),
        2023: (
            (JAN, 2, public_holiday),
            (JAN, 9, public_holiday),
            (APR, 24, public_holiday),
        ),
        2024: (
            (JAN, 8, public_holiday),
            (JUN, 17, public_holiday),
            (AUG, 5, public_holiday),
            (SEP, 23, public_holiday),
        ),
        2025: (
            (MAR, 31, public_holiday),
            (APR, 1, public_holiday),
            (JUL, 4, public_holiday),
            (SEP, 22, public_holiday),
        ),
        2026: (
            (JAN, 9, public_holiday),
            (JUL, 3, public_holiday),
        ),
    }
