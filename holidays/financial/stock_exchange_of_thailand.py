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

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, DEC
from holidays.countries.thailand import Thailand
from holidays.groups import InternationalHolidays, StaticHolidays, ThaiCalendarHolidays
from holidays.helpers import tr
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_NEXT_MON,
    SUN_TO_NEXT_TUE,
    FRI_SAT_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class StockExchangeOfThailand(
    ObservedHolidayBase, InternationalHolidays, StaticHolidays, ThaiCalendarHolidays
):
    """Stock Exchange of Thailand (SET) holidays.

    SET is closed on the financial institutions holidays announced by the Bank of Thailand.
    They follow Thailand's public holidays with a few differences. Buddhist Lent Day was a
    holiday until 2006 and was replaced by Asarnha Bucha from 2007. The Mid-Year Closing Day
    was a holiday until 2018. Holidays falling on a weekend share a single in-lieu day on the
    next workday, while Songkran Festival has an in-lieu day only when two of its days fall
    on a weekend. Special holidays declared by the government are adopted case by case.

    References:
        * [Financial Institutions Holiday](https://web.archive.org/web/20260618053922/https://www.bot.or.th/en/financial-institutions-holiday.html)
        * [SET Calendar 2023](https://web.archive.org/web/20240706095617/https://media.set.or.th/set/Documents/2023/Jan/SET-calendar-2023-EN.pdf)
        * [SET Calendar 2024](https://web.archive.org/web/20240815183915/https://media.set.or.th/set/Documents/2023/Dec/SET-calendar-2024-EN.pdf)
        * [SET Calendar 2025](https://web.archive.org/web/20251026190523/https://media.set.or.th/set/Documents/2024/Dec/SET_Calendar_2025_EN.pdf)
        * [SET Calendar 2026](https://web.archive.org/web/20251207123941/https://media.set.or.th/set/Documents/2025/Nov/SET-Calendar-2026-EN.pdf)

    Historical data:
        * [1992](https://web.archive.org/web/20220131052956/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1992.aspx)
        * [1993](https://web.archive.org/web/20220131052949/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1993.aspx)
        * [1994](https://web.archive.org/web/20220131052942/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1994.aspx)
        * [1995](https://web.archive.org/web/20220131041336/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1995.aspx)
        * [1996](https://web.archive.org/web/20220131024208/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1996.aspx)
        * [1997](https://web.archive.org/web/20220131024202/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1997.aspx)
        * [1998](https://web.archive.org/web/20220131024155/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1998.aspx)
        * [1999](https://web.archive.org/web/20220131024148/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/1999.aspx)
        * [2000](https://web.archive.org/web/20220131024135/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2000.aspx)
        * [2001](https://web.archive.org/web/20220131024128/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2001.aspx)
        * [2002](https://web.archive.org/web/20220131024121/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2002.aspx)
        * [2003](https://web.archive.org/web/20220131024113/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2003.aspx)
        * [2004](https://web.archive.org/web/20220131024106/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2004.aspx)
        * [2005](https://web.archive.org/web/20220131004742/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2005.aspx)
        * [2006](https://web.archive.org/web/20220131004734/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2006.aspx)
        * [2007](https://web.archive.org/web/20220131004726/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2007.aspx)
        * [2008](https://web.archive.org/web/20220131004719/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2008.aspx)
        * [2009](https://web.archive.org/web/20220130230107/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2009.aspx)
        * [2010](https://web.archive.org/web/20220130230101/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2010.aspx)
        * [2011](https://web.archive.org/web/20220130230052/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2011.aspx)
        * [2012](https://web.archive.org/web/20220130213733/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2012.aspx)
        * [2013](https://web.archive.org/web/20220130213726/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2013.aspx)
        * [2014](https://web.archive.org/web/20220130213717/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2014.aspx)
        * [2015](https://web.archive.org/web/20220130213710/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2015.aspx)
        * [2016](https://web.archive.org/web/20220130200358/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2016.aspx)
        * [2017](https://web.archive.org/web/20221129043453/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2017.aspx)
        * [2018](https://web.archive.org/web/20230404071418/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2018.aspx)
        * [2019](https://web.archive.org/web/20221202125213/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2019.aspx)
        * [2020](https://web.archive.org/web/20221204184130/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2020.aspx)
        * [2021](https://web.archive.org/web/20230322223136/https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2021.aspx)
    """

    market = "XBKK"
    default_language = "th"
    # %s (in lieu).
    observed_label = tr("ชดเชย%s")
    parent_entity = Thailand
    # First year in the Bank of Thailand's financial institutions holidays records.
    start_year = 1992
    supported_languages = ("en_US", "th", "uk")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, StockExchangeOfThailandStaticHolidays)
        ThaiCalendarHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_WORKDAY)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        dts_observed = set()

        # New Year's Day.
        dts_observed.add(self._add_new_years_day(tr("วันขึ้นปีใหม่")))

        # Makha Bucha.
        dt = self._add_makha_bucha(tr("วันมาฆบูชา"))
        # The in-lieu day for 1996 was moved to February 29, 1996.
        if self._year != 1996:
            dts_observed.add(dt)

        dts_observed.add(
            self._add_holiday_apr_6(
                # Chakri Memorial Day.
                tr("วันพระบาทสมเด็จพระพุทธยอดฟ้าจุฬาโลกมหาราช และวันที่ระลึกมหาจักรีบรมราชวงศ์")
            )
        )

        # Songkran Festival was postponed in 2020.
        if self._year != 2020:
            # Songkran Festival.
            name = tr("วันสงกรานต์")
            if self._year <= 1997:
                dt = self._add_holiday_apr_12(name)
                self._add_holiday_apr_13(name)
                self._add_holiday_apr_14(name)
            else:
                dt = self._add_holiday_apr_13(name)
                self._add_holiday_apr_14(name)
                self._add_holiday_apr_15(name)
            self._add_observed(dt, rule=FRI_SAT_TO_NEXT_WORKDAY)

        # National Labor Day.
        dts_observed.add(self._add_labor_day(tr("วันแรงงานแห่งชาติ")))

        # Coronation Day.
        name = tr("วันฉัตรมงคล")
        if self._year >= 2020:
            dts_observed.add(self._add_holiday_may_4(name))
        elif self._year <= 2016:
            dts_observed.add(self._add_holiday_may_5(name))

        if self._year >= 2019:
            dts_observed.add(
                self._add_holiday_jun_3(
                    # HM Queen Suthida's Birthday.
                    tr("วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี")
                )
            )

        if self._year <= 2018:
            self._add_holiday_jul_1(
                # Mid-Year Closing Day.
                tr("วันหยุดภาคครึ่งปีของสถาบันการเงินและสถาบันการเงินเฉพาะกิจ")
            )

        if self._year >= 2017:
            dts_observed.add(
                self._add_holiday_jul_28(
                    # HM King Maha Vajiralongkorn's Birthday.
                    tr(
                        "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดี"
                        "ศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว"
                    )
                )
            )

        dts_observed.add(
            self._add_holiday_aug_12(
                # HM Queen Sirikit the Queen Mother's Birthday.
                tr("วันเฉลิมพระชนมพรรษาสมเด็จพระบรมราชชนนีพันปีหลวง")
                if self._year >= 2017
                # HM Queen Sirikit's Birthday.
                else tr("วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสิริกิติ์ พระบรมราชินีนาถ")
            )
        )

        # National Mother's Day.
        self._add_holiday_aug_12(tr("วันแม่แห่งชาติ"))

        if self._year >= 2017:
            if self._year >= 2023:
                # HM King Bhumibol Adulyadej Memorial Day.
                name = tr("วันนวมินทรมหาราช")
            elif self._year >= 2019:
                # Anniversary for the Death of King Bhumibol Adulyadej the Great.
                name = tr(
                    "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
                )
            else:
                # Anniversary for the Death of King Bhumibol Adulyadej.
                name = tr("วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร")
            dts_observed.add(self._add_holiday_oct_13(name))

        # HM King Chulalongkorn Memorial Day.
        dt = self._add_holiday_oct_23(tr("วันปิยมหาราช"))
        # The in-lieu day for 2021 was moved to October 22, 2021.
        if self._year != 2021:
            dts_observed.add(dt)

        if self._year >= 2019:
            # HM King Bhumibol Adulyadej the Great's Birthday Anniversary.
            name = tr(
                "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
            )
        elif self._year >= 2016:
            # HM King Bhumibol Adulyadej Birthday Anniversary.
            name = tr("วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร")
        else:
            # HM King Bhumibol Adulyadej Birthday Anniversary.
            name = tr("วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร")
        dts_observed.add(self._add_holiday_dec_5(name))

        # National Day.
        self._add_holiday_dec_5(tr("วันชาติ"))

        # National Father's Day.
        self._add_holiday_dec_5(tr("วันพ่อแห่งชาติ"))

        # Constitution Day.
        dts_observed.add(self._add_holiday_dec_10(tr("วันรัฐธรรมนูญ")))

        if self._year >= 2007:
            # Asarnha Bucha.
            dts_observed.add(self._add_asarnha_bucha(tr("วันอาสาฬหบูชา")))
        else:
            # Buddhist Lent Day.
            dts_observed.add(self._add_khao_phansa(tr("วันเข้าพรรษา")))

        # Visakha Bucha.
        dts_observed.add(self._add_visakha_bucha(tr("วันวิสาขบูชา")))

        if self.observed:
            self._populate_observed(dts_observed)

        # New Year's Eve.
        name = tr("วันสิ้นปี")
        # New Year's Eve was moved to January 2 of the next year in 1997 and 2003.
        if self._year not in {1997, 2003}:
            self._add_new_years_eve(name)
        # The in-lieu day for New Year's Eve 2023 was moved to December 29, 2023.
        if self._year != 2024:
            self._add_observed(
                date(self._year - 1, DEC, 31), name=name, rule=SAT_TO_NEXT_MON + SUN_TO_NEXT_TUE
            )


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
    # Thai Election Day.
    thai_election = tr("วันเลือกตั้ง")
    # HM King Bhumibol Adulyadej's 60th Anniversary of Accession Event.
    rama_ix_sixty_accession = tr("พระราชพิธีฉลองสิริราชสมบัติครบ 60 ปี พ.ศ. 2549")
    # Makha Bucha.
    makha_bucha = tr("วันมาฆบูชา")
    # Songkran Festival.
    songkran_festival = tr("วันสงกรานต์")
    # HM King Chulalongkorn Memorial Day.
    chulalongkorn_memorial = tr("วันปิยมหาราช")
    # New Year's Eve.
    new_years_eve = tr("วันสิ้นปี")

    special_public_holidays = {
        1996: (
            (MAR, 1, thai_bridge_public_holiday),
            # HM King Bhumibol Adulyadej's Golden Jubilee.
            (JUN, 10, tr("พระราชพิธีกาญจนาภิเษก พ.ศ. 2539")),
        ),
        1998: (JAN, 2, new_years_eve),
        2002: (DEC, 30, thai_bridge_public_holiday),
        2006: (
            (APR, 19, thai_election),
            (JUN, 12, rama_ix_sixty_accession),
            (JUN, 13, rama_ix_sixty_accession),
        ),
        2009: (
            (JAN, 2, thai_bridge_public_holiday),
            (JUL, 6, thai_bridge_public_holiday),
        ),
        2010: (
            (MAY, 20, thai_bridge_public_holiday),
            (MAY, 21, thai_bridge_public_holiday),
            (AUG, 13, thai_bridge_public_holiday),
        ),
        2011: (MAY, 16, thai_bridge_public_holiday),
        2012: (
            (JAN, 3, thai_bridge_public_holiday),
            (APR, 9, thai_bridge_public_holiday),
        ),
        2013: (DEC, 30, thai_bridge_public_holiday),
        2014: (AUG, 11, thai_bridge_public_holiday),
        2015: (
            (JAN, 2, thai_bridge_public_holiday),
            (MAY, 4, thai_bridge_public_holiday),
        ),
        2016: (
            (MAY, 6, thai_bridge_public_holiday),
            (JUL, 18, thai_bridge_public_holiday),
        ),
        2017: (
            (JAN, 3, thai_bridge_public_holiday),
            # HM King Bhumibol Adulyadej's Royal Cremation Ceremony.
            (OCT, 26, tr("วันพระราชพิธีถวายพระเพลิงพระบรมศพพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช")),
        ),
        # HM King Maha Vajiralongkorn's Coronation Celebrations.
        2019: (MAY, 6, tr("พระราชพิธีบรมราชาภิเษก พระบาทสมเด็จพระวชิรเกล้าเจ้าอยู่หัว")),
        2020: (DEC, 11, thai_bridge_public_holiday),
        2021: (
            (FEB, 12, thai_bridge_public_holiday),
            (SEP, 24, thai_bridge_public_holiday),
        ),
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

    special_public_holidays_observed = {
        1996: (FEB, 29, makha_bucha),
        2004: (JAN, 2, new_years_eve),
        2007: (DEC, 24, thai_election),
        2020: (
            (JUL, 27, songkran_festival),
            (SEP, 4, songkran_festival),
            (SEP, 7, songkran_festival),
        ),
        2021: (OCT, 22, chulalongkorn_memorial),
    }
