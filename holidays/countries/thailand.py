#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import ARMED_FORCES, BANK, GOVERNMENT, PUBLIC, SCHOOL, WORKDAY
from holidays.groups import InternationalHolidays, StaticHolidays, ThaiCalendarHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    SAT_TO_NEXT_MON,
    THU_FRI_TO_NEXT_WORKDAY,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON_TUE,
    SAT_SUN_TO_NEXT_WORKDAY,
)


class Thailand(ObservedHolidayBase, InternationalHolidays, StaticHolidays, ThaiCalendarHolidays):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays in Thailand.

    References:
        - Based on: https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
        - Checked with: `Bank of Thailand lists <http://tiny.cc/wa_bot_2023>`_
        - [In Lieus]
            - `isranews.org <http://tiny.cc/wa_isranews_inlieu_hist>`_
            - https://resolution.soc.go.th/?prep_id=99159317
            - https://resolution.soc.go.th/?prep_id=196007
            - https://github.com/vacanza/holidays/pull/929
            - https://www.thairath.co.th/lifestyle/life/2812118
        - [New Year's Day]
            `wikisource.org <http://tiny.cc/wa_wiki_thai_newyear_2483>`_
        - [National Children's Day]
            https://thainews.prd.go.th/banner/th/children'sday/
        - [Chakri Memorial Day]
            `ocac.got.th <http://tiny.cc/wa_ocac_chakri>`_
        - [Songkran Festival]
            - `museumsiam.org <http://tiny.cc/wa_museumsiam_songkran>`_
            - https://resolution.soc.go.th/?prep_id=123659
        - [National Labour Day]
            https://www.thairath.co.th/lifestyle/culture/1832869
        - [National Day (24 June: Defunct)]
            `Ministry of Culture <http://tiny.cc/wa_mincul_nat_day>`_
        - [Coronation Day]
            https://www.matichon.co.th/politics/news_526200
            https://workpointtoday.com/news1-5/
        - [HM Queen Suthida's Birthday]
            https://www.thairath.co.th/news/politic/1567418
        - [HM Maha Vajiralongkorn's Birthday]
            https://www.matichon.co.th/politics/news_526200
        - [HM Queen Sirikit the Queen Mother's Birthday]
            https://hilight.kapook.com/view/14164
        - [National Mother's Day]
            https://www.brh.go.th/index.php/2019-02-27-04-11-52/542-12-2564
        - [HM King Bhumibol Adulyadej Memorial Day]
            https://www.matichon.co.th/politics/news_526200
        - [HM King Chulalongkorn Memorial Day]
            `<https://th.wikipedia.org/wiki/วันปิยมหาราช>`_
        - [HM King Bhumibol Adulyadej's Birthday]
            - `Ministry of Culture <http://tiny.cc/wa_mincul_nat_day>`_
            - https://hilight.kapook.com/view/148862
        - [National Father's Day]
            https://www.brh.go.th/index.php/2019-02-27-04-12-21/594-5-5
        - [Constitution Day]
            - https://hilight.kapook.com/view/18208
            - `Bank of Thailand <http://tiny.cc/wa_bot_1992>`_
            - `<https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2475.aspx>`_
        - [New Year's Eve]
            - `Bank of Thailand`_
            - https://resolution.soc.go.th/?prep_id=205799
            - https://resolution.soc.go.th/?prep_id=210744
        - [Makha Bucha]
            https://www.onab.go.th/th/content/category/detail/id/73/iid/3403
        - [Visakha Bucha]
            https://www.onab.go.th/th/content/category/detail/id/73/iid/3401
        - [Asarnha Bucha]
            https://www.onab.go.th/th/content/category/detail/id/73/iid/3397
        - [Buddhist Lent Day]
            https://www.onab.go.th/th/content/category/detail/id/73/iid/3395
        - [Royal Ploughing Ceremony]
            https://en.wikipedia.org/wiki/Royal_Ploughing_Ceremony
            https://www.lib.ru.ac.th/journal/may/may_phauchmongkol.html
            https://dl.parliament.go.th/handle/20.500.13072/103428
            https://dl.parliament.go.th/handle/20.500.13072/92816
            https://e-manage.mju.ac.th/timeline_detail.aspx?key=MTk4
            https://resolution.soc.go.th/PDF_UPLOAD/2510/932141.pdf
            https://www.myhora.com/ปฏิทิน/วันพืชมงคล.aspx
        - [Royal Thai Armed Forces Day]
            `<https://th.wikipedia.org/wiki/วันกองทัพไทย>`_
        - [Teacher's Day]
            https://www.cabinet.soc.go.th/doc_image/2500/718941.pdf

            !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
            Despite the wording, this usually only applies to Monday only for
            holidays, consecutive holidays all have their own special in lieu
            declared separately.
            Data from 1992-1994 and 1998-2000 are declared discretely in
            special_holidays declarations above.
            Applied Automatically for Monday if on Weekends: 1961-1973
            **NOTE**: No New Year's Eve (in lieu) for this period
            No In Lieu days available: 1974-1988
            Case-by-Case application for Workday if on Weekends: 1989-1994
            Applied Automatically for Workday if on Weekends: 1995-1997
            Case-by-Case application for Workday if on Weekends: 1998-2000
            Applied Automatically for Workday if on Weekends: 2001-Present

    Limitations:
        - This is only 100% accurate for 1997-2025; any future dates are up to the
          Royal Thai Government Gazette which updates on a year-by-year basis.

        - Approx. date only goes as far back as 1941 (B.E. 2484) as the Thai
          calendar for B.E. 2483 as we only have nine months from switching
          New Year Date (April 1st to January 1st).

        - Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
          until 2157 (B.E. 2700) as we only have Thai year-type data for
          cross-checking until then.

        - Royal Ploughing Ceremony Day is date is announced on an annual basis
          by the Court Astrologers, thus need an annual update to the library here

    Country created by: `arkid15r <https://github.com/arkid15r>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """

    country = "TH"
    supported_categories = (ARMED_FORCES, BANK, GOVERNMENT, PUBLIC, SCHOOL, WORKDAY)
    default_language = "th"
    # %s (in lieu).
    observed_label = tr("ชดเชย%s")
    supported_languages = ("en_US", "th")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        StaticHolidays.__init__(self, ThailandStaticHolidays)
        ThaiCalendarHolidays.__init__(self)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        super().__init__(*args, **kwargs)

    def _is_observed(self, dt: date) -> bool:
        return 1961 <= self._year <= 1973 or 1995 <= self._year <= 1997 or self._year >= 2001

    def _populate_public_holidays(self):
        # Due to Thai Calendar Migration, this is capped off at 1941.
        # But certain holidays were implemented before 1941.
        if self._year <= 1940:
            return None

        # Fixed Date Holidays

        # วันขึ้นปีใหม่
        # Status: In-Use.
        # Starts in the present form in 1941 (B.E. 2484).
        # TODO: Add check for 1941 if we support earlier dates.

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("วันขึ้นปีใหม่")))

        # วันเด็กแห่งชาติ
        # Status: In-Use.
        # Starts in 1955 as the 1st Monday of October.
        # No event was held in 1964 due to date changes came into effect too late.
        # Moved to 2nd Saturday of January since 1965.
        # No in-lieus are observed, and still remain a Public Holidays than just Observed.

        if self._year >= 1955 and self._year != 1964:
            # National Children's Day
            childrens_day = tr("วันเด็กแห่งชาติ")
            if self._year <= 1963:
                self._add_holiday_1st_mon_of_oct(childrens_day)
            else:
                self._add_holiday_2nd_sat_of_jan(childrens_day)

        # วันจักรี
        # Status: In-Use.
        # Starts in present form in 1918 (B.E. 2461).
        # TODO: Add check for 1918 if we support earlier dates.

        # Chakri Memorial Day.
        self._add_observed(self._add_holiday_apr_6(tr("วันจักรี")))

        # วันสงกรานต์
        # Status: In-Use.
        # Used to be April 1st as Thai New Year Day.
        # Initially abandoned in 1941 (B.E. 2484), declared again as
        #   public holidays in 1948 (2491 B.E).
        #  - 1948-1953, celebrated on Apr 13-15
        #  - 1954-1956, abandoned as a public holiday
        #  - 1957-1988, only celebrated on Apr 13
        #  - 1989-1997, celebrated on Apr 12-14
        #  - 1998-Present, celebrated on Apr 13-15
        #    (Except for 2020 due to Covid-19 outbreaks)
        # This has its own in-lieu trigger.

        if 1948 <= self._year <= 1953 or 1957 <= self._year != 2020:
            # Songkran Festival.
            songkran_festival = tr("วันสงกรานต์")
            if 1957 <= self._year <= 1988:
                self._add_observed(self._add_holiday_apr_13(songkran_festival))
            elif 1989 <= self._year <= 1997:
                dt = self._add_holiday_apr_12(songkran_festival)
                self._add_holiday_apr_13(songkran_festival)
                self._add_holiday_apr_14(songkran_festival)
            else:
                dt = self._add_holiday_apr_13(songkran_festival)
                self._add_holiday_apr_14(songkran_festival)
                self._add_holiday_apr_15(songkran_festival)

            # วันหยุดชดเชยวันสงกรานต์
            # If Songkran happened to be held on the weekends, only one in-lieu
            #   public holiday is added.
            #   - CASE 1: THU-FRI-SAT -> 1 in-lieu on MON
            #   - CASE 2: FRI-SAT-SUN -> 1 in-lieu on MON
            #   - CASE 3: SAT-SUN-MON -> 1 in-lieu on TUE
            #   - CASE 4: SUN-MON-TUE -> 1 in-lieu on WED
            # See in lieu logic in `_add_observed(dt: date)`.
            # Status: In Use.

            if self._year >= 1995:
                self._add_observed(dt, rule=THU_FRI_TO_NEXT_WORKDAY + SAT_SUN_TO_NEXT_WORKDAY)

        # วันแรงงานแห่งชาติ
        # Status: In-Use.
        # Starts in the present form in 1974 (B.E. 2517).
        # Does existed officially since 1956 (B.E. 2499), but wasn't a public holiday until then.
        # *** NOTE: only observed by financial and private sectors.

        if self._year >= 1974:
            # National Labor Day.
            self._add_observed(self._add_labor_day(tr("วันแรงงานแห่งชาติ")))

        # วันชาติ
        # Status: In-Use.
        # Starts in 1939 (B.E. 2482) by Plaek Phibunsongkhram.
        # Replaced by Rama IX's birthday in 1960 (B.E. 2503) by Sarit Thanarat.
        # TODO: Add check for 1939 if we support earlier dates.

        # National Day.
        national_day = tr("วันชาติ")
        self._add_observed(
            self._add_holiday_jun_24(national_day)
            if self._year <= 1959
            else self._add_holiday_dec_5(national_day)
        )

        # วันฉัตรมงคล
        # Starts in 1958 (B.E. 2501) for Rama IX's Coronation: May 5th.
        # No celebration in 2017-2019 (B.E 2560-2562).
        # Reestablished with Rama X's Coronation in 2020: May 4th.

        # Coronation Day.
        coronation_day = tr("วันฉัตรมงคล")

        if 1958 <= self._year <= 2016:
            self._add_observed(self._add_holiday_may_5(coronation_day))
        elif self._year >= 2020:
            self._add_observed(self._add_holiday_may_4(coronation_day))

        # วันเฉลิมพระชนมพรรษา พระราชินี
        # Status: In-Use.
        # Starts in 2019 (B.E. 2562).

        if self._year >= 2019:
            self._add_observed(
                self._add_holiday_jun_3(
                    # HM Queen Suthida's Birthday.
                    tr("วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี")
                )
            )

        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 10
        # Status: In-Use.
        # Started in 2017 (B.E 2560).

        if self._year >= 2017:
            self._add_observed(
                self._add_holiday_jul_28(
                    # HM King Maha Vajiralongkorn's Birthday.
                    tr(
                        "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดี"
                        "ศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว"
                    )
                )
            )

        # วันเฉลิมพระชนมพรรษา พระบรมราชินีนาถ ( 1976-2017)
        # วันเฉลิมพระชนมพรรษา พระบรมราชชนนีพันปีหลวง (2017-Present)
        # Status: In-Use.
        # Started in 1976 (B.E. 2519) alongside Mother's Day.
        # Initial celebration as HM Queen Sirikit's Birthday.
        # Now acts as the Queen Mother from 2017 onwards.

        if self._year >= 1976:
            q_sirikit_bday = (
                # HM Queen Sirikit the Queen Mother's Birthday.
                tr("วันเฉลิมพระชนมพรรษาสมเด็จพระบรมราชชนนีพันปีหลวง")
                if self._year >= 2017
                # HM Queen Sirikit's Birthday.
                else tr("วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสิริกิติ์ พระบรมราชินีนาถ")
            )
            self._add_observed(self._add_holiday_aug_12(q_sirikit_bday))

        # วันแม่แห่งชาติ
        # Status: In-Use.
        # Started 1950 (B.E 2493) initially as April 15 and cancelled in
        #   1958 (B.E 2501) when the Min. of Culture was abolished.
        # Restarts again in 1976 (B.E. 2519) on Queen Sirikit's Birthday
        #   (August 12) and stay that way from that point onwards.

        # National Mother's Day.
        thai_mothers_day = tr("วันแม่แห่งชาติ")

        if 1950 <= self._year <= 1957:
            self._add_observed(self._add_holiday_apr_15(thai_mothers_day))
        elif self._year >= 1976:
            self._add_observed(self._add_holiday_aug_12(thai_mothers_day))

        # วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทร มหาภูมิพลอดุลยเดช บรมนาถบพิตร
        # Status: In-Use.
        # Started in 2017 (B.E 2560).
        # Got conferred with 'the Great' title in 2019 (B.E. 2562).

        if self._year >= 2017:
            if self._year >= 2023:
                # HM King Bhumibol Adulyadej Memorial Day.
                k_bhumibol_memorial = tr("วันนวมินทรมหาราช")
            elif self._year >= 2019:
                # Anniversary for the Death of King Bhumibol Adulyadej the Great.
                k_bhumibol_memorial = tr(
                    "วันคล้ายวันสวรรคตพระบาทสมเด็จพระบรมชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
                )
            else:
                # Anniversary for the Death of King Bhumibol Adulyadej.
                k_bhumibol_memorial = tr(
                    "วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร"
                )
            self._add_observed(self._add_holiday_oct_13(k_bhumibol_memorial))

        # วันปิยมหาราช
        # Status: In-Use.
        # Started in 1911 (B.E. 2454).
        # TODO: Add check for 1911 if we support earlier dates.

        # HM King Chulalongkorn Memorial Day.
        self._add_observed(self._add_holiday_oct_23(tr("วันปิยมหาราช")))

        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (1960-2016)
        # วันคล้ายวันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (2017-Present)
        # Status: In-Use.
        # Replaced Nataion Day (26 June) in 1960 (B.E. 2503) by Sarit Thanarat.
        # Confirmed as still in-use in 2017.
        # Got conferred with 'the Great' title in 2019 (B.E. 2562).

        if self._year >= 1960:
            if self._year >= 2019:
                k_bhumibol_bday = (
                    # HM King Bhumibol Adulyadej's the Great's Birthday Anniversary.
                    tr(
                        "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรม"
                        "ชนกาธิเบศร มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร"
                    )
                )
            elif self._year >= 2016:
                k_bhumibol_bday = (
                    # HM King Bhumibol Adulyadej Birthday Anniversary.
                    tr("วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร")
                )
            else:
                k_bhumibol_bday = (
                    # HM King Bhumibol Adulyadej Birthday Anniversary.
                    tr("วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช บรมนาถบพิตร")
                )
            self._add_observed(self._add_holiday_dec_5(k_bhumibol_bday))

        # วันพ่อแห่งชาติ
        # Status: In-Use.
        # Starts in 1980 (B.E 2523).
        # Technically, a replication of HM King Bhumibol Adulyadej's Birthday
        #   but it's in the official calendar, so may as well have this here.

        if self._year >= 1980:
            # National Father's Day.
            self._add_observed(self._add_holiday_dec_5(tr("วันพ่อแห่งชาติ")))

        # วันรัฐธรรมนูญ
        # Status: In-Use.
        # Presumed to starts in 1932 (B.E. 2475).
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535).
        # TODO: Add check for 1932 if we support earlier dates.

        # Constitution Day.
        self._add_observed(self._add_holiday_dec_10(tr("วันรัฐธรรมนูญ")))

        # วันสิ้นปี
        # Status: In-Use.
        # Presumed to start in the present form in 1941 (B.E. 2484).
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535).
        # TODO: Add check for 1941 if we support earlier dates.
        # This has its own in-lieu trigger.

        # New Year's Eve.
        name = tr("วันสิ้นปี")
        self._add_new_years_eve(name)

        # วันหยุดชดเชยวันสิ้นปี
        # Status: In-Use.
        # Added separately from New Year's Eve itself so that it would't
        #   go over the next year.
        #   - CASE 1: SAT-SUN -> 1 in-lieu on TUE.
        #   - CASE 2: SUN-MON -> 1 in-lieu on TUE.
        # See in lieu logic in `_add_observed(dt: date)`.

        if self._year >= 1995 and self._year != 2024:
            self._add_observed(date(self._year - 1, DEC, 31), name=name, rule=SAT_SUN_TO_NEXT_TUE)

        # Thai Lunar Calendar Holidays
        # See `_ThaiLunisolar` in holidays/utils.py for more details.
        # Thai Lunar Calendar Holidays only work from 1941 to 2057.

        # วันมาฆบูชา
        # Status: In-Use.

        # Makha Bucha.
        self._add_observed(self._add_makha_bucha(tr("วันมาฆบูชา")))

        # วันวิสาขบูชา
        # Status: In-Use.

        # Visakha Bucha.
        self._add_observed(self._add_visakha_bucha(tr("วันวิสาขบูชา")))

        # วันอาสาฬหบูชา
        # Status: In-Use.
        #  - CASE 1: FRI-SAT -> 1 in-lieu on MON
        #  - CASE 2: SAT-SUN -> 1 in-lieu on MON
        #  - CASE 3: SUN-MON -> 1 in-lieu on TUE

        self._add_observed(
            # Asarnha Bucha.
            self._add_asarnha_bucha(tr("วันอาสาฬหบูชา")),
            rule=SAT_SUN_TO_NEXT_MON_TUE,
        )

        # วันเข้าพรรษา
        # Status: In-Use.
        #  - CASE 1: FRI-SAT -> 1 in-lieu on MON
        #  - CASE 2: SAT-SUN -> 1 in-lieu on MON
        #  - CASE 3: SUN-MON -> 1 in-lieu on TUE

        # Buddhist Lent Day.
        self._add_observed(self._add_khao_phansa(tr("วันเข้าพรรษา")), rule=SAT_TO_NEXT_MON)

    def _populate_armed_forces_holidays(self):
        # วันกองทัพไทย
        # Status: In-Use.
        # First started in 1959 on the foundation of Ministry of Defense Day (APR 8).
        # Moved to JAN 25 (Supposedly King Naresuan's Decisive Battle) in 1980.
        # Corrected to the battle's actual date (JAN 18) in 2007.
        # Only applys to members of the Royal Thai Armed Forces.

        if self._year >= 1959:
            # Royal Thai Armed Forces Day
            armed_forces_day = tr("วันกองทัพไทย")
            if self._year >= 2007:
                self._add_holiday_jan_18(armed_forces_day)
            elif self._year >= 1980:
                self._add_holiday_jan_25(armed_forces_day)
            else:
                self._add_holiday_apr_8(armed_forces_day)

    def _populate_bank_holidays(self):
        # Bank of Thailand, the ones who decreed this wasn't found until December 10, 1942
        # So it's safe to assume with that as our start date.
        if self._year <= 1942:
            return None

        # Bank Holidays

        # วันหยุดเพิ่มเติมสำหรับการปิดบัญชีประจำปีของธนาคารเพื่อการเกษตรและสหกรณ์การเกษตร
        # Status: Defunct.
        # If held on the weekends, no in-lieus.
        # Abandoned in 2022.

        if self._year <= 2021:
            self._add_holiday_apr_1(
                # Additional Closing Day for Bank for Agriculture and Agricultural Cooperatives
                tr("วันหยุดเพิ่มเติมสำหรับการปิดบัญชีประจำปีของธนาคารเพื่อการเกษตรและสหกรณ์การเกษตร"),
            )

        # วันหยุดภาคครึ่งปีของสถาบันการเงินและสถาบันการเงินเฉพาะกิจ
        # Status: Defunct.
        # If held on the weekends, no in-lieus.
        # Abandoned in 2019.

        if self._year <= 2018:
            self._add_holiday_jul_1(
                # Mid-Year Closing Day
                tr("วันหยุดภาคครึ่งปีของสถาบันการเงินและสถาบันการเงินเฉพาะกิจ"),
            )

    def _populate_government_holidays(self):
        # No Future Fixed Date Holidays

        # วันพืชมงคล
        # Restarts in 1947 (B.E. 2490), wouldn't become an holiday again until 1960 (B.E. 2503).
        # Removed as an holiday in 1999 due to financial crisis, reinstated in 2000.
        # No event was held in 2021 due to local Covid-19 situation, though it stays a day off.
        # Is dated on an annual basis by the Royal Palace, always on weekdays.
        # For historic research, วันเกษตรแห่งชาติ (National Agricultural Day) also concides with
        #   this from 1966 onwards. For earlier records the date was refered as วันแรกนาขวัญ.
        # This isn't even fixed even by the Thai Lunar Calendar besides being in Month 6
        #   to concides with the rainy season, but instead by Court Astrologers; All chosen dates
        #   so far are all in the first three weeks of May.
        # *** NOTE: only observed by government sectors.
        # TODO: Update this annually around Dec of each year.

        # Got only 1 source for 1992 and 1993, might need some recheck later.
        raeknakhwan_dates = {
            1960: (MAY, 2),
            1961: (MAY, 11),
            1962: (MAY, 7),
            1963: (MAY, 10),
            1964: (MAY, 8),
            1965: (MAY, 13),
            1966: (MAY, 13),
            1967: (MAY, 11),
            1968: (MAY, 10),
            1969: (MAY, 9),
            1970: (MAY, 8),
            1971: (MAY, 7),
            1972: (MAY, 8),
            1973: (MAY, 7),
            1974: (MAY, 8),
            1975: (MAY, 7),
            1976: (MAY, 10),
            1977: (MAY, 12),
            1978: (MAY, 11),
            1979: (MAY, 7),
            1980: (MAY, 14),
            1981: (MAY, 7),
            1982: (MAY, 19),
            1983: (MAY, 11),
            1984: (MAY, 10),
            1985: (MAY, 9),
            1986: (MAY, 9),
            1987: (MAY, 8),
            1988: (MAY, 11),
            1989: (MAY, 11),
            1990: (MAY, 11),
            1991: (MAY, 10),
            1992: (MAY, 14),
            1993: (MAY, 17),
            1994: (MAY, 11),
            1995: (MAY, 10),
            1996: (MAY, 16),
            1997: (MAY, 9),
            1998: (MAY, 8),
            # Not a holiday in 1999 date, was held on MAY, 14.
            2000: (MAY, 15),
            2001: (MAY, 16),
            2002: (MAY, 9),
            2003: (MAY, 8),
            2004: (MAY, 7),
            2005: (MAY, 11),
            2006: (MAY, 11),
            2007: (MAY, 10),
            2008: (MAY, 9),
            2009: (MAY, 11),
            2010: (MAY, 13),
            2011: (MAY, 13),
            2012: (MAY, 9),
            2013: (MAY, 13),
            2014: (MAY, 9),
            2015: (MAY, 13),
            2016: (MAY, 9),
            2017: (MAY, 12),
            2018: (MAY, 14),
            2019: (MAY, 9),
            2020: (MAY, 11),
            2021: (MAY, 10),
            2022: (MAY, 13),
            2023: (MAY, 17),
            2024: (MAY, 10),
            2025: (MAY, 9),
        }
        if 1960 <= self._year <= 2025 and self._year != 1999:
            self._add_observed(
                # Royal Ploughing Ceremony.
                self._add_holiday(tr("วันพืชมงคล"), raeknakhwan_dates.get(self._year, (MAY, 13)))
            )

    def _populate_school_holidays(self):
        # วันครู
        # Status: In-Use.
        # Started in 1957.
        # Only applies to Ministry of Education (Students, Teachers, etc.), no in-lieus are given.

        if self._year >= 1957:
            # Teacher's Day
            self._add_holiday_jan_16(tr("วันครู"))

    def _populate_workday_holidays(self):
        # These are classes as "วันสำคัญ" (Date of National Observance) by the government
        # but are not holidays.

        if self._year >= 1948:
            # วันทหารผ่านศึก
            # Status: In-Use.
            # Started in 1948.

            # Thai Veterans Day
            self._add_holiday_feb_3(tr("วันทหารผ่านศึก"))

        if self._year >= 1982:
            # วันวิทยาศาสตร์แห่งชาติ
            # Status: In-Use.
            # Started in 1982.

            # National Science Day
            self._add_holiday_aug_18(tr("วันวิทยาศาสตร์แห่งชาติ"))

        if self._year >= 1985:
            # วันศิลปินแห่งชาติ
            # Status: In-Use.
            # Started in 1985.

            # National Artist Day
            self._add_holiday_feb_26(tr("วันศิลปินแห่งชาติ"))

        if self._year >= 1989:
            # วันสตรีสากล
            # Status: In-Use.
            # Started in 1989.

            # International Women's Day
            self._add_womens_day(tr("วันสตรีสากล"))

        if self._year >= 1990:
            # วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ
            # Status: In-Use.
            # Started in 1990.

            # National Forest Conservation Day
            self._add_holiday_jan_14(tr("วันอนุรักษ์ทรัพยากรป่าไม้ของชาติ"))

            # วันพ่อขุนรามคำแหงมหาราช
            # Status: In-Use.
            # Started in 1990.

            # HM King Ramkamhaeng Memorial Day
            self._add_holiday_jan_17(tr("วันพ่อขุนรามคำแหงมหาราช"))

        if self._year >= 1995:
            # วันการบินแห่งชาติ
            # Status: In-Use.
            # Started in 1995.

            # National Aviation Day
            self._add_holiday_jan_13(tr("วันการบินแห่งชาติ"))

        if self._year >= 2017:
            # วันพระราชทานธงชาติไทย
            # Status: In-Use.
            # Started in 2017.

            # Thai National Flag Day
            self._add_holiday_sep_28(tr("วันพระราชทานธงชาติไทย"))

        # วันลอยกระทง
        # Status: In-Use.

        if self._year >= 1941:
            # Loy Krathong
            self._add_loy_krathong(tr("วันลอยกระทง"))


class TH(Thailand):
    pass


class THA(Thailand):
    pass


class ThailandStaticHolidays:
    # วันหยุดพิเศษ (เพิ่มเติม) - see Bank of Thailand's DB for Cross-Check.

    # Special In Lieu Holiday.
    thai_special_in_lieu_holidays = tr("วันหยุดชดเชย")
    # Thai Election Day.
    thai_election = tr("วันเลือกตั้ง")
    # Bridge Public Holiday.
    thai_bridge_public_holiday = tr("วันหยุดพิเศษ (เพิ่มเติม)")

    # Special Cases.

    # HM King Bhumibol Adulyadej's Golden Jubilee.
    rama_ix_golden_jubilee = tr("พระราชพิธีกาญจนาภิเษก พ.ศ. 2539")
    # HM King Bhumibol Adulyadej's 60th Anniversary of Accession Event.
    rama_ix_sixty_accession = tr("พระราชพิธีฉลองสิริราชสมบัติครบ 60 ปี พ.ศ. 2549")
    # Emergency Lockdown (Thai Military Coup d'état).
    thai_military_emergency_lockdown = tr("วันหยุดพิเศษ (คมช.)")
    # Emergency Lockdown (Thai Political Unrest).
    thai_political_emergency_lockdown = tr("วันหยุดพิเศษ (การเมือง)")
    # Emergency Lockdown (2011 Thailand Floods).
    thai_flood_2011_emergency_lockdown = tr("วันหยุดพิเศษ (มหาอุทกภัย พ.ศ. 2554)")
    # Day of Mourning for HM King Bhumibol Adulyadej.
    rama_ix_mourning = tr("วันหยุดพิเศษ (ร่วมถวายอาลัย ส่งดวงพระวิญญาณพระบรมศพ)")
    # HM King Bhumibol Adulyadej's Royal Cremation Ceremony.
    rama_ix_cremation = tr("วันพระราชพิธีถวายพระเพลิงพระบรมศพพระบาทสมเด็จพระปรมินทรมหาภูมิพลอดุลยเดช")
    # HM King Maha Vajiralongkorn's Coronation Celebrations.
    rama_x_coronation_celebrations = tr("พระราชพิธีบรมราชาภิเษก พระบาทสมเด็จพระวชิรเกล้าเจ้าอยู่หัว")
    # Songkran Festival.
    songkran_festival = tr("วันสงกรานต์")

    special_public_holidays = {
        # 1992-1994 (include In Lieus, Checked with Bank of Thailand Data).
        1992: (
            (MAY, 18, thai_special_in_lieu_holidays),
            (DEC, 7, thai_special_in_lieu_holidays),
        ),
        1993: (
            (MAR, 8, thai_special_in_lieu_holidays),
            (MAY, 3, thai_special_in_lieu_holidays),
            (OCT, 25, thai_special_in_lieu_holidays),
            (DEC, 6, thai_special_in_lieu_holidays),
        ),
        1994: (
            (JAN, 3, thai_special_in_lieu_holidays),
            (MAY, 2, thai_special_in_lieu_holidays),
            (JUL, 25, thai_special_in_lieu_holidays),
            (OCT, 24, thai_special_in_lieu_holidays),
            (DEC, 12, thai_special_in_lieu_holidays),
        ),
        # 1995-1997 (Bank of Thailand Data).
        1996: (JUN, 10, rama_ix_golden_jubilee),
        # 1998-2000 (include In Lieus, Checked with Bank of Thailand Data).
        1998: (
            (MAY, 11, thai_special_in_lieu_holidays),
            (DEC, 7, thai_special_in_lieu_holidays),
        ),
        1999: (
            (MAY, 3, thai_special_in_lieu_holidays),
            (MAY, 31, thai_special_in_lieu_holidays),
            (OCT, 25, thai_special_in_lieu_holidays),
            (DEC, 6, thai_special_in_lieu_holidays),
        ),
        2000: (
            (JAN, 3, thai_special_in_lieu_holidays),
            (FEB, 21, thai_special_in_lieu_holidays),
            (AUG, 14, thai_special_in_lieu_holidays),
            (DEC, 11, thai_special_in_lieu_holidays),
            (DEC, 29, thai_election),
        ),
        # From 2001 Onwards (Checked with Bank of Thailand Data).
        2006: (
            (APR, 19, thai_election),
            (JUN, 9, rama_ix_sixty_accession),
            (JUN, 12, rama_ix_sixty_accession),
            (JUN, 13, rama_ix_sixty_accession),
            (SEP, 20, thai_military_emergency_lockdown),
        ),
        2009: (
            (JAN, 2, thai_bridge_public_holiday),
            (APR, 10, thai_political_emergency_lockdown),
            (APR, 16, thai_political_emergency_lockdown),
            (APR, 17, thai_political_emergency_lockdown),
            (JUL, 6, thai_bridge_public_holiday),
        ),
        2010: (
            (MAY, 20, thai_bridge_public_holiday),
            (MAY, 21, thai_bridge_public_holiday),
            (AUG, 13, thai_bridge_public_holiday),
        ),
        2011: (
            (MAY, 16, thai_bridge_public_holiday),
            (OCT, 27, thai_flood_2011_emergency_lockdown),
            (OCT, 28, thai_flood_2011_emergency_lockdown),
            (OCT, 29, thai_flood_2011_emergency_lockdown),
            (OCT, 30, thai_flood_2011_emergency_lockdown),
            (OCT, 31, thai_flood_2011_emergency_lockdown),
        ),
        2012: (APR, 9, thai_bridge_public_holiday),
        2013: (DEC, 30, thai_bridge_public_holiday),
        2014: (AUG, 11, thai_bridge_public_holiday),
        2015: (
            (JAN, 2, thai_bridge_public_holiday),
            (MAY, 4, thai_bridge_public_holiday),
        ),
        2016: (
            (MAY, 6, thai_bridge_public_holiday),
            (JUL, 18, thai_bridge_public_holiday),
            (OCT, 14, rama_ix_mourning),
        ),
        2017: (OCT, 26, rama_ix_cremation),
        2019: (MAY, 6, rama_x_coronation_celebrations),
        2020: (
            (NOV, 19, thai_bridge_public_holiday),
            (NOV, 20, thai_bridge_public_holiday),
            (DEC, 11, thai_bridge_public_holiday),
        ),
        2021: (
            (FEB, 12, thai_bridge_public_holiday),
            (APR, 12, thai_bridge_public_holiday),
            (SEP, 24, thai_bridge_public_holiday),
        ),
        2022: (
            (JUL, 15, thai_bridge_public_holiday),
            (JUL, 29, thai_bridge_public_holiday),
            (OCT, 14, thai_bridge_public_holiday),
            (DEC, 30, thai_bridge_public_holiday),
        ),
        2023: (
            (MAY, 5, thai_bridge_public_holiday),
            (JUL, 31, thai_bridge_public_holiday),
            (DEC, 29, thai_bridge_public_holiday),
        ),
        2024: (
            (APR, 12, thai_bridge_public_holiday),
            (DEC, 30, thai_bridge_public_holiday),
        ),
    }
    special_workday_holidays = {1999: (MAY, 14, tr("วันพืชมงคล"))}

    special_public_holidays_observed = {
        2007: (DEC, 24, thai_election),
        2020: (
            (JUL, 27, songkran_festival),
            (SEP, 4, songkran_festival),
            (SEP, 7, songkran_festival),
        ),
    }
