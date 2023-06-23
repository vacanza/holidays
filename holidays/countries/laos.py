#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import timedelta as td
from gettext import gettext as tr

from holidays.calendars import KHMER_CALENDAR
from holidays.constants import APR, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import InternationalHolidays, ThaiCalendarHolidays


class Laos(HolidayBase, InternationalHolidays, ThaiCalendarHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in Laos.

    References:

    - Based on: https://en.wikipedia.org/wiki/Public_holidays_in_Laos
                https://www.ayutthaya.go.th/5786-%20ข้อควรรู้และวันหยุดในประเทศลาว
                ດຳລັດວ່າດ້ວຍ ວັນພັກ ເລກທີ 386 /ລບ (15.12.2017)

    - Checked with: https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf
                    https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf
                    https://www.timeanddate.com/holidays/laos/

    Limitations:

    - Laotian holidays only works from 1976 onwards, and are only 100% accurate from 2018 onwards.

    - Laotian Lunar Calendar Holidays only work from 1941 (B.E. 2485) onwards until 2057
      (B.E. 2601) as we only have Thai year-type data for cross-checking until then.


    Country created by: `PPsyrius <https://github.com/PPsyrius>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """

    country = "LA"
    default_language = "lo"

    # Special Cases.

    # Lao New Year's Day (in-lieu)
    lao_new_year_in_lieu = tr("ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ")

    special_holidays = {
        2017: (
            (APR, 12, lao_new_year_in_lieu),
            (APR, 13, lao_new_year_in_lieu),
        ),
        2017: (
            (APR, 13, lao_new_year_in_lieu),
            (APR, 17, lao_new_year_in_lieu),
        ),
    }
    supported_languages = ("en_US", "lo", "th")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        ThaiCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # Available post-Lao PDR proclamation on Dec 2, 1975.
        if year <= 1975:
            return None

        def _add_observed(dt: date) -> None:
            """
            !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
            Despite the wording, this usually only applies to Monday only for holidays,
            consecutive holidays all have their own special in lieu declared separately.

            As featured in ດຳລັດວ່າດ້ວຍ ວັນພັກ ເລກທີ 386 /ລບ (15.12.2017);
            - Saturdays and Sundays shall be restdays each week.
            - In-Lieu holidays shall be given if it fall on the weekends.
            """
            if self.observed and self._is_weekend(dt) and year >= 2018:
                in_lieu = dt + td(days=+2 if self._is_saturday(dt) else +1)
                for name in self.get_list(dt):
                    self._add_holiday(self.tr("ພັກຊົດເຊີຍ%s") % name, in_lieu)

        super()._populate(year)

        # Fixed Date Official Holidays

        # ວັນປີໃໝ່ສາກົນ
        # Status: In-Use.

        # New Year's Day
        _add_observed(self._add_new_years_day(tr("ວັນປີໃໝ່ສາກົນ")))

        # ວັນແມ່ຍິງສາກົນ
        # Status: In-Use.
        # Only acts as day off for Women.

        # International Women's Rights Day
        _add_observed(self._add_womens_day(tr("ວັນແມ່ຍິງສາກົນ")))

        # ບຸນປີໃໝ່ລາວ
        # Status: In-Use.
        # Celebrated for 3 days from 14-16 April annualy.

        # Lao New Year's Day
        name = tr("ບຸນປີໃໝ່ລາວ")
        dt = self._add_holiday(name, APR, 14)
        self._add_holiday(name, dt + td(days=+1))
        self._add_holiday(name, dt + td(days=+2))

        # ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ
        # See in lieu logic in `_add_observed(dt: date)`.
        # Dates prior to 2018 are assigned manually
        # Status: In-Use.

        if self.observed and year >= 2018:
            if self._is_thursday(dt) or self._is_friday(dt) or self._is_saturday(dt):
                self._add_holiday(lao_new_year_in_lieu, dt + td(days=+4))
            if self._is_friday(dt) or self._is_saturday(dt) or self._is_sunday(dt):
                self._add_holiday(lao_new_year_in_lieu, dt + td(days=+3))

        # ວັນກຳມະກອນສາກົນ
        # Status: In-Use.

        # Labor Day
        _add_observed(self._add_labor_day(tr("ວັນກຳມະກອນສາກົນ")))

        # ວັນເດັກສາກົນ
        # Status: Defunct.
        # Starts as public holiday after Lao PDR joined UN Convention on the
        # Rights of the Child in 1989 (de-facto start as holiday in 1990).
        # Became defunct from 2018 onwards.

        if 1990 <= year <= 2017:
            # International Children Day
            self._add_childrens_day(tr("ວັນເດັກສາກົນ"))

        # ວັນຊາດ
        # Status: In-Use.
        # Celebrated the establishment of Lao PDR on Dec 2, 1975.

        # Lao National Day
        _add_observed(self._add_holiday(tr("ວັນຊາດ"), DEC, 2))

        # Laotian Lunar Calendar Holidays
        # See `_ThaiLunisolar` in holidays/utils.py for more details.
        # Laotian Lunar Calendar Holidays only work from 1941 to 2057.
        # Unofficial, but observed by schools and most business holidays;
        # As such, no in-lieu observance are in place for these holidays.

        # ບຸນທາດຫລວງ
        # Status: In-Use, Unofficial.
        # 15th Waxing Day of Month 12.

        # Boun That Luang Festival
        self._add_loy_krathong(tr("ບຸນທາດຫລວງ"))


class LA(Laos):
    pass


class LAO(Laos):
    pass
