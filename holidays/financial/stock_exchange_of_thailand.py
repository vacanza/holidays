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

from holidays.calendars.gregorian import JAN, APR, MAY, JUN, JUL, AUG, OCT, DEC
from holidays.countries.thailand import Thailand
from holidays.groups import InternationalHolidays, StaticHolidays, ThaiCalendarHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
    FRI_SAT_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_MON,
)


class StockExchangeOfThailand(
    ObservedHolidayBase, InternationalHolidays, StaticHolidays, ThaiCalendarHolidays
):
    """Stock Exchange of Thailand (SET) holidays.

    SET is closed on the financial institutions holidays announced by the Bank of Thailand.
    They follow Thailand's public holidays except Buddhist Lent Day. Holidays falling on a
    weekend share a single in-lieu day on the following Monday, while Songkran Festival has
    an in-lieu day only when two of its days fall on a weekend. Special holidays declared by
    the government are adopted case by case.

    References:
        * [Financial Institutions Holiday](https://web.archive.org/web/20260618053922/https://www.bot.or.th/en/financial-institutions-holiday.html)
        * [SET Calendar 2023](https://web.archive.org/web/20240706095617/https://media.set.or.th/set/Documents/2023/Jan/SET-calendar-2023-EN.pdf)
        * [SET Calendar 2024](https://web.archive.org/web/20240815183915/https://media.set.or.th/set/Documents/2023/Dec/SET-calendar-2024-EN.pdf)
        * [SET Calendar 2025](https://web.archive.org/web/20251026190523/https://media.set.or.th/set/Documents/2024/Dec/SET_Calendar_2025_EN.pdf)
        * [SET Calendar 2026](https://web.archive.org/web/20251207123941/https://media.set.or.th/set/Documents/2025/Nov/SET-Calendar-2026-EN.pdf)
    """

    market = "XBKK"
    default_language = "th"
    # %s (in lieu).
    observed_label = tr("ชดเชย%s")
    parent_entity = Thailand
    # First year listed on the Bank of Thailand's financial institutions holidays page.
    start_year = 2022
    supported_languages = ("en_US", "th", "uk")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, StockExchangeOfThailandStaticHolidays)
        ThaiCalendarHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("วันขึ้นปีใหม่")))

        self._add_observed(
            self._add_holiday_apr_6(
                # Chakri Memorial Day.
                tr("วันพระบาทสมเด็จพระพุทธยอดฟ้าจุฬาโลกมหาราช และวันที่ระลึกมหาจักรีบรมราชวงศ์")
            )
        )

        # Songkran Festival.
        name = tr("วันสงกรานต์")
        dt = self._add_holiday_apr_13(name)
        self._add_holiday_apr_14(name)
        self._add_holiday_apr_15(name)
        self._add_observed(dt, rule=FRI_SAT_TO_NEXT_WORKDAY)

        # National Labor Day.
        self._add_observed(self._add_labor_day(tr("วันแรงงานแห่งชาติ")))

        # Coronation Day.
        self._add_observed(self._add_holiday_may_4(tr("วันฉัตรมงคล")))

        self._add_observed(
            self._add_holiday_jun_3(
                # HM Queen Suthida's Birthday.
                tr("วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี")
            )
        )

        self._add_observed(
            self._add_holiday_jul_28(
                # HM King Maha Vajiralongkorn's Birthday.
                tr(
                    "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดี"
                    "ศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว"
                )
            )
        )

        self._add_observed(
            self._add_holiday_aug_12(
                # HM Queen Sirikit the Queen Mother's Birthday.
                tr("วันเฉลิมพระชนมพรรษาสมเด็จพระบรมราชชนนีพันปีหลวง")
            )
        )

        # National Mother's Day.
        self._add_observed(self._add_holiday_aug_12(tr("วันแม่แห่งชาติ")))

        self._add_observed(
            self._add_holiday_oct_13(
                # HM King Bhumibol Adulyadej Memorial Day.
                tr("วันนวมินทรมหาราช")
                if self._year >= 2023
                # Anniversary for the Death of King Bhumibol Adulyadej the Great.
                else tr("วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร")
            )
        )

        # HM King Chulalongkorn Memorial Day.
        self._add_observed(self._add_holiday_oct_23(tr("วันปิยมหาราช")))

        self._add_observed(
            self._add_holiday_dec_5(
                # HM King Bhumibol Adulyadej the Great's Birthday Anniversary.
                tr(
                    "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร "
                    "มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
                )
            )
        )

        # National Day.
        self._add_observed(self._add_holiday_dec_5(tr("วันชาติ")))

        # National Father's Day.
        self._add_observed(self._add_holiday_dec_5(tr("วันพ่อแห่งชาติ")))

        # Constitution Day.
        self._add_observed(self._add_holiday_dec_10(tr("วันรัฐธรรมนูญ")))

        # New Year's Eve.
        name = tr("วันสิ้นปี")
        self._add_new_years_eve(name)
        # The in-lieu day for New Year's Eve 2023 was moved to December 29, 2023.
        if self._year != 2024:
            self._add_observed(
                date(self._year - 1, DEC, 31), name=name, rule=SAT_TO_NEXT_MON + SUN_TO_NEXT_TUE
            )

        # Makha Bucha.
        self._add_observed(self._add_makha_bucha(tr("วันมาฆบูชา")))

        # Visakha Bucha.
        self._add_observed(self._add_visakha_bucha(tr("วันวิสาขบูชา")))

        # Asarnha Bucha.
        self._add_observed(self._add_asarnha_bucha(tr("วันอาสาฬหบูชา")))


class XBKK(StockExchangeOfThailand):
    pass


class SET(StockExchangeOfThailand):
    pass


class StockExchangeOfThailandStaticHolidays:
    """Stock Exchange of Thailand (SET) special holidays.

    References:
        * [Substitution for New Year's Eve 2023](https://web.archive.org/web/20260420192109/https://www.bot.or.th/en/news-and-media/news/news-20231102.html)
        * [Additional special holiday 2024](https://web.archive.org/web/20260422015758/https://www.bot.or.th/en/news-and-media/news/news-20240221.html)
        * [Additional special holidays 2025-2026](https://web.archive.org/web/20260618053205/https://www.bot.or.th/en/news-and-media/news/news-20241127.html)
        * [Additional special holiday in Bangkok 2026](https://www.bot.or.th/en/news-and-media/news/news-20260609.html)
    """

    # Special In-Lieu Holiday.
    thai_special_in_lieu_holidays = tr("วันหยุดชดเชย")
    # Bridge Public Holiday.
    thai_bridge_public_holiday = tr("วันหยุดพิเศษ (เพิ่มเติม)")

    special_public_holidays = {
        2022: (
            (JUL, 29, thai_bridge_public_holiday),
            (OCT, 14, thai_bridge_public_holiday),
        ),
        2023: (
            (MAY, 5, thai_bridge_public_holiday),
            (DEC, 29, thai_special_in_lieu_holidays),
        ),
        2024: (APR, 12, thai_bridge_public_holiday),
        2025: (
            (JUN, 2, thai_bridge_public_holiday),
            (AUG, 11, thai_bridge_public_holiday),
        ),
        2026: (
            (JAN, 2, thai_bridge_public_holiday),
            (OCT, 16, thai_bridge_public_holiday),
        ),
    }
