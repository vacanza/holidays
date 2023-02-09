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

from datetime import date
from datetime import timedelta as td
from typing import Iterable, Optional, Union

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC, MON, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import _ThaiLuniSolar


class Thailand(HolidayBase):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Thailand. (Based on South Korean and Singaporean Implementation)


    Limitations:

    - This is only 100% accurate for 1997-2023; any future dates are up to the
      Royal Thai Government Gazette which updates on a year-by-year basis.

    - Approx. date only goes as far back as 1941 (B.E. 2484) as the Thai
      calendar for B.E. 2483 as we only have nine months from switching
      New Year Date (April 1st to January 1st).

    - Thai Lunar Calendar Holidays only work from 1941 (B.E. 2484) onwards
      until 2957 (B.E. 2600) as we only have Thai year-type data for
      cross-checking until then.

    - Royal Ploughing Ceremony Day is date is announced on an annual basis
      by the Court Astrologers, thus need an annual update to the library here

    - This doesn't cover Thai regional public holidays yet, only stubs added

    References:

    - Based on: https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    - Checked with: (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_2023
    - For individual data sources in detail, see the in-code comment below
      with copies available on Internet Archive's Wayback Machine
      other extra long links are shortened with tiny.cc to Wayback Machine

    Country created by: `arkid15r <https://github.com/arkid15r>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """

    country = "TH"

    # วันหยุดพิเศษ (เพิ่มเติม) - see Bank of Thailand's DB for Cross-Check
    thai_special_in_lieu_holidays = "Special In Lieu Holiday"
    thai_election = "Thai Election Day"
    thai_election_in_lieu = "Thai Election Day (in lieu)"
    thai_bridge_public_holiday = "Bridge Public Holiday"

    # Special Cases
    rama_ix_golden_jubilee = "HM King Bhumibol Adulyadej's Golden Jubilee"
    rama_ix_sixty_accession = (
        "HM King Bhumibol Adulyadej's 60th Anniversary of Accession Event"
    )
    thai_military_emergency_lockdown = (
        "Emergency Lockdown (Thai Military Coup d'état)"
    )
    thai_political_emergency_lockdown = (
        "Emergency Lockdown (Thai Political Unrest)"
    )
    thai_flood_2011_emergency_lockdown = (
        "Emergency Lockdown (2011 Thailand Floods)"
    )
    rama_ix_mourning = "Day of Mourning for HM King Bhumibol Adulyadej"
    rama_ix_cremation = "HM King Bhumibol Adulyadej's Royal Cremation Ceremony"
    rama_x_coronation_celebrations = (
        "HM King Maha Vajiralongkorn's Coronation Celebrations"
    )
    songkran_festival_in_lieu_covid = "Songkran Festival (in lieu)"

    special_holidays = {
        # 1992-1994 (include In Lieus, Checked /w Bank of Thailand Data)
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
        # 1995-1997 (Bank of Thailand Data)
        1996: ((JUN, 10, rama_ix_golden_jubilee),),
        # 1998-2000 (include In Lieus, Checked /w Bank of Thailand Data)
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
        # From 2001 Onwards (Checked /w Bank of Thailand Data)
        2006: (
            (APR, 19, thai_election),
            (JUN, 9, rama_ix_sixty_accession),
            (JUN, 12, rama_ix_sixty_accession),
            (JUN, 13, rama_ix_sixty_accession),
            (SEP, 20, thai_military_emergency_lockdown),
        ),
        2007: ((DEC, 24, thai_election_in_lieu),),
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
            (OCT, 31, thai_flood_2011_emergency_lockdown),
        ),
        2012: ((APR, 9, thai_bridge_public_holiday),),
        2013: ((DEC, 30, thai_bridge_public_holiday),),
        2014: ((AUG, 11, thai_bridge_public_holiday),),
        2015: (
            (JAN, 2, thai_bridge_public_holiday),
            (MAY, 4, thai_bridge_public_holiday),
        ),
        2016: (
            (MAY, 6, thai_bridge_public_holiday),
            (JUL, 18, thai_bridge_public_holiday),
            (OCT, 14, rama_ix_mourning),
        ),
        2017: ((OCT, 26, rama_ix_cremation),),
        2019: ((MAY, 6, rama_x_coronation_celebrations),),
        2020: (
            (JUL, 27, songkran_festival_in_lieu_covid),
            (SEP, 4, songkran_festival_in_lieu_covid),
            (SEP, 7, songkran_festival_in_lieu_covid),
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
        2023: ((MAY, 5, thai_bridge_public_holiday),),
    }

    def __init__(
        self,
        years: Optional[Union[int, Iterable[int]]] = None,
        expand: bool = True,
        observed: bool = True,
        subdiv: Optional[str] = None,
        prov: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        self.thls = _ThaiLuniSolar()
        super().__init__(years, expand, observed, subdiv, prov, state)

    def _populate(self, year):
        # Due to Thai Calendar Migration, this is capped off at 1941
        # But certain holidays were implemented before 1941
        if year <= 1940:
            return

        # DEFAULT
        def add_holiday(dt, holiday_name) -> None:
            # Only add if current year and year is 1941 (B.E. 2484) or later
            # This is here as a stub for future islamic consecutive holidays
            # Which can stradle across gregorian years in southern region
            if dt.year == year:
                self[dt] = holiday_name

            """
            !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
            Despite the wording, this usually only applies to Monday only for
            holidays, consecutive holidays all have their own special in lieu
            declared separately.

            Data from 1992-1994 and 1998-2000 are declared discretely in
              special_holidays declarations above.

            Sources:
              (isranews.org 's wbm) http://tiny.cc/wa_isranews_inlieu_hist
              https://resolution.soc.go.th/?prep_id=99159317
              https://resolution.soc.go.th/?prep_id=196007
            """
            # Applied Automatically for Monday if on Weekends: 1961-1973
            #  **NOTE: No New Year's Eve (in lieu) for this period
            # No In Lieu days available: 1974-1988
            # Case-by-Case application for Workday if on Weekends: 1989-1994
            # Applied Automatically for Workday if on Weekends: 1995-1997
            # Case-by-Case application for Workday if on Weekends: 1998-2000
            # Applied Automatically for Workday if on Weekends: 2001-Present
            if 1961 <= year <= 1973 or 1995 <= year <= 1997 or year >= 2001:
                if self.observed and self._is_weekend(dt):
                    in_lieu = dt + td(days=+2 if dt.weekday() == SAT else +1)
                    self[in_lieu] = f"{holiday_name} (in lieu)"

        super()._populate(year)

        ########################
        #
        # FIXED DATED HOLIDAYS
        #
        ########################

        # !!! New Year's Day !!!
        # Sources:
        #   (wikisource.org 's wbm) http://tiny.cc/wa_wiki_thai_newyear_2483
        # วันขึ้นปีใหม่
        # Status: In-Use
        # Starts in the present form in 1941 (B.E. 2484)
        new_years_day = "New Year's Day"

        if year >= 1941:
            add_holiday(date(year, JAN, 1), new_years_day)

        # !!! New Year's Eve (in lieu) !!!
        # Sources:
        #   https://github.com/dr-prodigy/python-holidays/pull/929
        #   https://resolution.soc.go.th/?prep_id=205799
        #   https://resolution.soc.go.th/?prep_id=210744
        # วันหยุดชดเชยวันสิ้นปี
        # Status: In-Use
        # Added separately from New Year's Eve itself so that it would't
        #   go over the next year
        new_years_eve_in_lieu = "New Year's Eve (in lieu)"

        # Applied Automatically for Monday if on Weekends: 1961-1973
        #  **NOTE: No New Year's Eve (in lieu) for this period
        # No In Lieu days available: 1974-1988
        # Case-by-Case application for Workday if on Weekends: 1989-1994
        # Applied Automatically for Workday if on Weekends: 1995-1997
        # Case-by-Case application for Workday if on Weekends: 1998-2000
        # Applied Automatically for Workday if on Weekends: 2001-Present
        if self.observed and (1995 <= year <= 1997 or year >= 2001):
            # CASE 1: SAT-SUN -> 1 in-lieu on TUE
            if date(year - 1, DEC, 31).weekday() == SAT:
                self[date(year, JAN, 3)] = new_years_eve_in_lieu
            # CASE 2: SUN-MON -> 1 in-lieu on TUE
            elif date(year - 1, DEC, 31).weekday() == SUN:
                self[date(year, JAN, 2)] = new_years_eve_in_lieu

        # !!! Chakri Memorial Day !!!
        # วันจักรี
        # Status: In-Use
        # Starts in present form in 1918 (B.E. 2461)
        # Sources:
        #   (ocac.got.th 's wbm) http://tiny.cc/wa_ocac_chakri
        chakri_memorial = "Chakri Memorial Day"

        if year >= 1918:
            add_holiday(date(year, APR, 6), chakri_memorial)

        # !!! Songkran Festival !!!
        # Sources:
        #   (museumsiam.org 's wbm) http://tiny.cc/wa_museumsiam_songkran
        #   https://resolution.soc.go.th/?prep_id=123659
        # วันสงกรานต์
        # Status: In-Use
        # Used to be April 1st as Thai New Year Day
        # Initially abandoned in 1941 (B.E. 2484), declared again as
        #   public holidays in 1948 (2491 B.E)
        # This has its own in-lieu trigger
        songkran_festival = "Songkran Festival"

        # 1948-1953, celebrated on Apr 13-15
        if 1948 <= year <= 1953:
            self[date(year, APR, 13)] = songkran_festival
            self[date(year, APR, 14)] = songkran_festival
            self[date(year, APR, 15)] = songkran_festival
        # 1954-1956, abandoned as a public holiday
        # 1957-1988, only celebrated on Apr 13
        elif 1957 <= year <= 1988:
            add_holiday(date(year, APR, 13), songkran_festival)
        # 1989-1997, celebrated on Apr 12-14
        elif 1989 <= year <= 1997:
            self[date(year, APR, 12)] = songkran_festival
            self[date(year, APR, 13)] = songkran_festival
            self[date(year, APR, 14)] = songkran_festival
        # 1998-Present, celebrated on Apr 13-15
        # (Except for 2020 due to Covid-19 outbreaks)
        elif year >= 1998 and year != 2020:
            self[date(year, APR, 13)] = songkran_festival
            self[date(year, APR, 14)] = songkran_festival
            self[date(year, APR, 15)] = songkran_festival

        # !!! Songkran Festival (in lieu) !!!
        # Sources:
        #   https://github.com/dr-prodigy/python-holidays/pull/929
        # วันหยุดชดเชยวันสงกรานต์
        # If Songkran happened to be held on the weekends, only one in-lieu
        #   public holiday is added, No in lieus for SUN-MON-TUE case
        # Status: In Use
        songkran_festival_in_lieu = "Songkran Festival (in lieu)"

        # Applied Automatically for Monday if on Weekends: 1961-1973
        # No In Lieu days available: 1974-1988
        # Case-by-Case application for Workday if on Weekends: 1989-1994
        # Applied Automatically for Workday if on Weekends: 1995-1997
        # Case-by-Case application for Workday if on Weekends: 1998-2000
        # Applied Automatically for Workday if on Weekends: 2001-Present
        if self.observed and (1995 <= year <= 1997 or year >= 2001):
            dt = date(year, APR, 15) if year >= 2001 else date(year, APR, 14)
            # CASE 1: THU-FRI-SAT -> 1 in-lieu on MON
            if dt.weekday() == SAT:
                self[dt + td(days=+2)] = songkran_festival_in_lieu
            # CASE 2: FRI-SAT-SUN -> 1 in-lieu on MON
            elif dt.weekday() == SUN:
                self[dt + td(days=+1)] = songkran_festival_in_lieu
            # CASE 3: SAT-SUN-MON -> 1 in-lieu on TUE
            elif dt.weekday() == MON:
                self[dt + td(days=+1)] = songkran_festival_in_lieu

        # !!! Labour day !!!
        # Sources:
        #   https://www.thairath.co.th/lifestyle/culture/1832869
        # วันแรงงานแห่งชาติ
        # Status: In-Use
        # Starts in the present form in 1974 (B.E. 2517)
        # Does existed officially since 1956 (B.E. 2499),
        #   but wasn't a public holiday until then
        # *** NOTE: only observed by financial and private sectors
        national_labour_day = "National Labour Day"

        if year >= 1974:
            add_holiday(date(year, MAY, 1), national_labour_day)

        # !!! National Day (24 June) !!!
        # Sources:
        #   (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
        # วันชาติ
        # Status: Defunct (Historical)
        # Starts in 1939 (B.E. 2482) by Plaek Phibunsongkhram
        # Replaced by Rama IX's birthday in 1960 (B.E. 2503) by Sarit Thanarat
        national_day_khana_ratsadon = "National Day"

        if 1939 <= year <= 1959:
            add_holiday(date(year, JUN, 24), national_day_khana_ratsadon)

        # !!! Coronation Day !!!
        # Sources:
        #   https://www.matichon.co.th/politics/news_526200
        #   https://workpointtoday.com/news1-5/
        # วันฉัตรมงคล
        # Starts in 1958 (B.E. 2501)
        # No celebration in 2017-2019 (B.E 2560-2562)
        # Reestablished with Rama X's Coronation in 2020
        coronation_day = "Coronation Day"

        # Rama IX's Coronation: May 5th
        if 1958 <= year <= 2016:
            add_holiday(date(year, MAY, 5), coronation_day)
        # In-Between Years: No Celebration
        # Rama X's Coronation: May 4th
        elif year >= 2020:
            add_holiday(date(year, MAY, 4), coronation_day)

        # !!! HM Queen Suthida's Birthday !!!
        # Sources:
        #   https://www.thairath.co.th/news/politic/1567418
        # วันเฉลิมพระชนมพรรษา พระราชินี
        # Status: In-Use
        # Starts in 2019 (B.E. 2562)
        queen_suthida_birthday = "HM Queen Suthida's Birthday"

        if year >= 2019:
            add_holiday(date(year, JUN, 3), queen_suthida_birthday)

        # !!! HM King Maha Vajiralongkorn's Birthday !!!
        # Sources:
        #   https://www.matichon.co.th/politics/news_526200
        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 10
        # Status: In-Use
        # Started in 2017 (B.E 2560)
        rama_x_birthday = "HM King Maha Vajiralongkorn's Birthday"

        if year >= 2017:
            add_holiday(date(year, JUL, 28), rama_x_birthday)

        # !!! HM Queen Sirikit the Queen Mother's Birthday !!!
        # Sources:
        #   https://hilight.kapook.com/view/14164
        # วันเฉลิมพระชนมพรรษา พระบรมราชินีนาถ ( 1976-2017),
        # วันเฉลิมพระชนมพรรษา พระบรมราชชนนีพันปีหลวง (2017-Present)
        # Status: In-Use
        # Started in 1976 (B.E. 2519) alongside Mother's Day
        queen_sirikit_birthday_rama_ix = "HM Queen Sirikit's Birthday"
        queen_sirikit_birthday_rama_x = (
            "HM Queen Sirikit The Queen Mother's Birthday"
        )

        # Initial celebration as HM Queen Sirikit's Birthday
        if 1976 <= year <= 2016:
            add_holiday(date(year, AUG, 12), queen_sirikit_birthday_rama_ix)
        # Now acts as the Queen Mother
        elif year >= 2017:
            add_holiday(date(year, AUG, 12), queen_sirikit_birthday_rama_x)

        # !!! Mother's Day !!!
        # Sources:
        #   https://www.brh.go.th/index.php/2019-02-27-04-11-52/542-12-2564
        # วันแม่แห่งชาติ
        # Status: In-Use
        # Started 1950 (B.E 2493) initially as April 15 and cancelled in
        #   1958 (B.E 2501) when the Min. of Culture was abolished.
        # Restarts again in 1976 (B.E. 2519) on Queen Sirikit's Birthday
        #   (August 12) and stay that way from that point onwards.
        thai_mothers_day = "Mother's Day"

        # Initial Celebration on April 15
        if 1950 <= year <= 1957:
            add_holiday(date(year, APR, 15), thai_mothers_day)
        # In-Between years while Min. of Culture was abolished
        # Restarts in 1976 on Queen Sirikit's Birthday
        elif year >= 1976:
            add_holiday(date(year, AUG, 12), thai_mothers_day)

        # !!! Anniversary for the Death of King Bhumibol Adulyadej !!!
        # Sources:
        #   https://www.matichon.co.th/politics/news_526200
        # วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทร มหาภูมิพลอดุลยเดช บรมนาถบพิตร
        # Status: In-Use
        # Started in 2017 (B.E 2560)
        rama_ix_memorial = "HM King Bhumibol Adulyadej Memorial Day"

        if year >= 2017:
            add_holiday(date(year, OCT, 13), rama_ix_memorial)

        # !!! Chulalongkorn Memorial Day !!!
        # Sources:
        #   https://th.wikipedia.org/wiki/วันปิยมหาราช
        # วันปิยมหาราช
        # Status: In-Use
        # Started in 1911 (B.E. 2454)
        rama_five_memorial = "Chulalongkorn Memorial Day"

        if year >= 1911:
            add_holiday(date(year, OCT, 23), rama_five_memorial)

        # !!! HM King Bhumibol Adulyadej's Birthday Anniversary !!!
        # Sources:
        #   (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
        #   https://hilight.kapook.com/view/148862
        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (1960-2016),
        # วันคล้ายยวันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (2017-Present)
        # Status: In-Use
        # Replaced Nataion Day (26 June) in 1960 (B.E. 2503) by Sarit Thanarat
        # Confirmed as still in-use in 2017
        rama_ix_birthday = "HM King Bhumibol Adulyadej's Birthday"

        if year >= 1960:
            add_holiday(date(year, DEC, 5), rama_ix_birthday)

        # !!! Father's Day !!!
        # Sources:
        #   https://www.brh.go.th/index.php/2019-02-27-04-12-21/594-5-5
        # วันพ่อแห่งชาติ
        # Status: In-Use
        # Starts in 1980 (B.E 2523)
        # Technically, a replication of HM King Bhumibol Adulyadej's Birthday
        #   but it's in the official calendar, so may as well have this here
        thai_fathers_day = "Father's Day"

        if year >= 1980:
            add_holiday(date(year, DEC, 5), thai_fathers_day)

        # !!! Constitution Day !!!
        # Sources:
        #   https://hilight.kapook.com/view/18208
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        #   https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2475.aspx
        # วันรัฐธรรมนูญ
        # Status: In-Use
        # Presumed to starts in 1932 (B.E. 2475) ???
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535)
        constitution_day = "Constitution Day"

        if year >= 1932:
            add_holiday(date(year, DEC, 10), constitution_day)

        # !!! New Year's Eve !!!
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        # วันสิ้นปี
        # Status: In-Use
        # Presumed to start in the present form in 1941 (B.E. 2484) ???
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535)
        # This has its own in-lieu trigger
        new_years_eve = "New Year's Eve"

        if year >= 1941:
            self[date(year, DEC, 31)] = new_years_eve

        ################################
        #
        # THAI LUNAR CALENDAR HOLIDAYS
        #
        ################################

        """
        See _ThaiLuniSolar in holidays/utils.py for more details
        """
        # !!! Makha Bucha !!!
        # Sources:
        #   https://www.onab.go.th/th/content/category/detail/id/73/iid/3403
        # วันมาฆบูชา
        # Status: In-Use
        makha_bucha = "Makha Bucha"

        add_holiday(self.thls.makha_bucha_date(year), makha_bucha)

        # !!! Visakha Bucha !!!
        # Sources:
        #   https://www.onab.go.th/th/content/category/detail/id/73/iid/3401
        # วันวิสาขบูชา
        # Status: In-Use
        visakha_bucha = "Visakha Bucha"

        add_holiday(self.thls.visakha_bucha_date(year), visakha_bucha)

        # !!! Asarnha Bucha !!!
        # Sources:
        #   https://www.onab.go.th/th/content/category/detail/id/73/iid/3397
        # วันอาสาฬหบูชา
        # Status: In-Use
        # This has its own in-lieu trigger
        asarnha_bucha = "Asarnha Bucha"

        self[self.thls.asarnha_bucha_date(year)] = asarnha_bucha

        # !!! Buddhist Lent Day !!!
        # Sources:
        #   https://www.onab.go.th/th/content/category/detail/id/73/iid/3395
        # วันเข้าพรรษา
        # Status: In-Use
        # This has its own in-lieu trigger
        khao_phansa = "Buddhist Lent Day"

        self[self.thls.khao_phansa_date(year)] = khao_phansa

        # !!! Asarnha Bucha/Buddhist Lent Day (in lieu) !!!
        # วันหยุดชดเชยวันอาสาฬหบูชา
        # วันหยุดชดเชยวันเข้าพรรษา
        # Status: In Use
        # For clearer tooltip
        asarnha_bucha_in_lieu = "Asarnha Bucha (in lieu)"
        khao_phansa_in_lieu = "Buddhist Lent Day (in lieu)"

        # Applied Automatically for Monday if on Weekends: 1961-1973
        # No In Lieu days available: 1974-1988
        # Case-by-Case application for Workday if on Weekends: 1989-1994
        # Applied Automatically for Workday if on Weekends: 1995-1997
        # Case-by-Case application for Workday if on Weekends: 1998-2000
        # Applied Automatically for Workday if on Weekends: 2001-Present
        asarnha_date = self.thls.asarnha_bucha_date(year)

        if self.observed and (
            1961 <= year <= 1973 or 1995 <= year <= 1997 or year >= 2001
        ):
            # CASE 1: FRI-SAT -> 1 in-lieu on MON
            if asarnha_date.weekday() == FRI:
                self[asarnha_date + td(days=+3)] = khao_phansa_in_lieu
            # CASE 2: SAT-SUN -> 1 in-lieu on MON
            # CASE 3: SUN-MON -> 1 in-lieu on TUE
            elif self._is_weekend(asarnha_date):
                self[asarnha_date + td(days=+2)] = asarnha_bucha_in_lieu

        #################################
        #
        # NO FUTURE FIXED DATE HOLIDAYS
        #
        #################################

        # !!! Royal Ploughing Ceremony !!!
        # Sources:
        #   https://en.wikipedia.org/wiki/Royal_Ploughing_Ceremony
        #   https://www.lib.ru.ac.th/journal/may/may_phauchmongkol.html
        #   https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2540.aspx
        # วันพืชมงคล
        # Restarts in 1957 (B.E. 2500)
        # Is dated on an annual basis by the Royal Palace
        # This isn't even fixed even by the Thai Lunar Calendar, but instead
        #   by Court Astrologers; All chosen dates are all around May, so we
        #   can technically assign it to 13 May for years prior with no data.
        # *** NOTE: only observed by government sectors
        # [TODO]: Update this annually around Dec of each year
        raeknakhwan = "Royal Ploughing Ceremony"

        raeknakhwan_dates = {
            1997: (MAY, 13),
            1998: (MAY, 13),
            # Not held in 1999 date
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
            2010: (MAY, 10),
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
            2021: (MAY, 13),
            2022: (MAY, 17),
            2023: (MAY, 11),
        }
        # For years with exact date data
        if year in raeknakhwan_dates:
            add_holiday(date(year, *raeknakhwan_dates[year]), raeknakhwan)
        # Approx. otherwise for 1957-2013
        elif 1957 <= year <= 1996:
            add_holiday(date(year, MAY, 13), raeknakhwan)


class TH(Thailand):
    pass


class THA(Thailand):
    pass
