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

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC, MON, FRI, SAT, SUN
from holidays.holiday_base import HolidayBase


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
    thai_special_in_lieu_holidays_en = "Special In Lieu Holiday"
    thai_election_en = "Thai Election Day"
    thai_election_in_lieu_en = "Thai Election Day (in lieu)"
    thai_bridge_public_holiday_en = "Bridge Public Holiday"

    # Special Cases
    rama_ix_golden_jubilee_en = "HM King Bhumibol Adulyadej's Golden Jubilee"
    rama_ix_sixty_accession_en = (
        "HM King Bhumibol Adulyadej's 60th Anniversary of Accession Event"
    )
    thai_military_emergency_lockdown_en = (
        "Emergency Lockdown (Thai Military Coup d'état)"
    )
    thai_political_emergency_lockdown_en = (
        "Emergency Lockdown (Thai Political Unrest)"
    )
    thai_flood_2011_emergency_lockdown_en = (
        "Emergency Lockdown (2011 Thailand Floods)"
    )
    rama_ix_mourning_en = "Day of Mourning for HM King Bhumibol Adulyadej"
    rama_ix_cremation_en = (
        "HM King Bhumibol Adulyadej's Royal Cremation Ceremony"
    )
    rama_x_coronation_celebrations_en = (
        "HM King Maha Vajiralongkorn's Coronation Celebrations"
    )
    songkran_festival_in_lieu_covid_en = "Songkran Festival (in lieu)"

    special_holidays = {
        # 1992-1994 (include In Lieus, Checked /w Bank of Thailand Data)
        1992: (
            (MAY, 18, thai_special_in_lieu_holidays_en),
            (DEC, 7, thai_special_in_lieu_holidays_en),
        ),
        1993: (
            (MAR, 8, thai_special_in_lieu_holidays_en),
            (MAY, 3, thai_special_in_lieu_holidays_en),
            (OCT, 25, thai_special_in_lieu_holidays_en),
            (DEC, 6, thai_special_in_lieu_holidays_en),
        ),
        1994: (
            (JAN, 3, thai_special_in_lieu_holidays_en),
            (MAY, 2, thai_special_in_lieu_holidays_en),
            (JUL, 25, thai_special_in_lieu_holidays_en),
            (OCT, 24, thai_special_in_lieu_holidays_en),
            (DEC, 12, thai_special_in_lieu_holidays_en),
        ),
        # 1995-1997 (Bank of Thailand Data)
        1996: ((JUN, 10, rama_ix_golden_jubilee_en),),
        # 1998-2000 (include In Lieus, Checked /w Bank of Thailand Data)
        1998: (
            (MAY, 11, thai_special_in_lieu_holidays_en),
            (DEC, 7, thai_special_in_lieu_holidays_en),
        ),
        1999: (
            (MAY, 3, thai_special_in_lieu_holidays_en),
            (MAY, 31, thai_special_in_lieu_holidays_en),
            (OCT, 25, thai_special_in_lieu_holidays_en),
            (DEC, 6, thai_special_in_lieu_holidays_en),
        ),
        2000: (
            (JAN, 3, thai_special_in_lieu_holidays_en),
            (FEB, 21, thai_special_in_lieu_holidays_en),
            (AUG, 14, thai_special_in_lieu_holidays_en),
            (DEC, 11, thai_special_in_lieu_holidays_en),
            (DEC, 29, thai_election_en),
        ),
        # From 2001 Onwards (Checked /w Bank of Thailand Data)
        2006: (
            (APR, 19, thai_election_en),
            (JUN, 9, rama_ix_sixty_accession_en),
            (JUN, 12, rama_ix_sixty_accession_en),
            (JUN, 13, rama_ix_sixty_accession_en),
            (SEP, 20, thai_military_emergency_lockdown_en),
        ),
        2007: ((DEC, 24, thai_election_in_lieu_en),),
        2009: (
            (JAN, 2, thai_bridge_public_holiday_en),
            (APR, 10, thai_political_emergency_lockdown_en),
            (APR, 16, thai_political_emergency_lockdown_en),
            (APR, 17, thai_political_emergency_lockdown_en),
            (JUL, 6, thai_bridge_public_holiday_en),
        ),
        2010: (
            (MAY, 20, thai_bridge_public_holiday_en),
            (MAY, 21, thai_bridge_public_holiday_en),
            (AUG, 13, thai_bridge_public_holiday_en),
        ),
        2011: (
            (MAY, 16, thai_bridge_public_holiday_en),
            (OCT, 27, thai_flood_2011_emergency_lockdown_en),
            (OCT, 28, thai_flood_2011_emergency_lockdown_en),
            (OCT, 31, thai_flood_2011_emergency_lockdown_en),
        ),
        2012: ((APR, 9, thai_bridge_public_holiday_en),),
        2013: ((DEC, 30, thai_bridge_public_holiday_en),),
        2014: ((AUG, 11, thai_bridge_public_holiday_en),),
        2015: (
            (JAN, 2, thai_bridge_public_holiday_en),
            (MAY, 4, thai_bridge_public_holiday_en),
        ),
        2016: (
            (MAY, 6, thai_bridge_public_holiday_en),
            (JUL, 18, thai_bridge_public_holiday_en),
            (OCT, 14, rama_ix_mourning_en),
        ),
        2017: ((OCT, 26, rama_ix_cremation_en),),
        2019: ((MAY, 6, rama_x_coronation_celebrations_en),),
        2020: (
            (JUL, 27, songkran_festival_in_lieu_covid_en),
            (SEP, 4, songkran_festival_in_lieu_covid_en),
            (SEP, 7, songkran_festival_in_lieu_covid_en),
            (NOV, 19, thai_bridge_public_holiday_en),
            (NOV, 20, thai_bridge_public_holiday_en),
            (DEC, 11, thai_bridge_public_holiday_en),
        ),
        2021: (
            (FEB, 12, thai_bridge_public_holiday_en),
            (APR, 12, thai_bridge_public_holiday_en),
            (SEP, 24, thai_bridge_public_holiday_en),
        ),
        2022: (
            (JUL, 15, thai_bridge_public_holiday_en),
            (JUL, 29, thai_bridge_public_holiday_en),
            (OCT, 14, thai_bridge_public_holiday_en),
            (DEC, 30, thai_bridge_public_holiday_en),
        ),
        2023: ((MAY, 5, thai_bridge_public_holiday_en),),
    }

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

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

            # !!! If Public Holiday falls on weekends, (in lieu) on workday !!!
            # Despite the wording, this usually only applies to Monday only
            #   for consecutive holidays, with the sole exception being
            #   New Year's Eve (in lieu) <-- This is now it's own code instance
            # Data from 1992-1994 and 1998-2000 are declared discretely in
            #   special_holidays declarations above.
            # Sources:
            #   (isranews.org 's wbm) http://tiny.cc/wa_isranews_inlieu_hist
            #   https://resolution.soc.go.th/?prep_id=99159317
            #   https://resolution.soc.go.th/?prep_id=196007

            # Applied Automatically for Monday if on Weekends: 1961-1973
            #  **NOTE: No New Year's Eve (in lieu) for this period
            # No In Lieu days available: 1974-1988
            # Case-by-Case application for Workday if on Weekends: 1989-1994
            # Applied Automatically for Workday if on Weekends: 1995-1997
            # Case-by-Case application for Workday if on Weekends: 1998-2000
            # Applied Automatically for Workday if on Weekends: 2001-Present
            if 1961 <= year <= 1973 or 1995 <= year <= 1997 or year >= 2001:
                if self.observed and self._is_weekend(dt):
                    in_lieu = dt + td(days=2 if dt.weekday() == SAT else 1)
                    self[in_lieu] = f"{holiday_name} (in lieu)"

        super()._populate(year)

        ########################
        #
        # FIXED DATED HOLIDAYS
        #
        ########################

        # !!! New Year's Day !!!
        # วันขึ้นปีใหม่
        # Status: In-Use
        # Starts in the present form in 1941 (B.E. 2484)
        # Sources:
        #   (wikisource.org 's wbm) http://tiny.cc/wa_wiki_thai_newyear_2483
        new_years_day_en = "New Year's Day"

        if year >= 1941:
            add_holiday(date(year, JAN, 1), new_years_day_en)

        # !!! New Year's Eve (in lieu) !!!
        # วันหยุดชดเชยวันสิ้นปี
        # Status: In-Use
        # Added separately from New Year's Eve itself so that it would't
        #   go over the next year
        # Sources:
        #   https://github.com/dr-prodigy/python-holidays/pull/929
        #   https://resolution.soc.go.th/?prep_id=205799
        #   https://resolution.soc.go.th/?prep_id=210744
        new_years_eve_in_lieu_en = "New Year's Eve (in lieu)"

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
                self[date(year, JAN, 3)] = new_years_eve_in_lieu_en
            # CASE 2: SUN-MON -> 1 in-lieu on TUE
            elif date(year - 1, DEC, 31).weekday() == SUN:
                self[date(year, JAN, 2)] = new_years_eve_in_lieu_en

        # !!! Chakri Memorial Day !!!
        # วันจักรี
        # Status: In-Use
        # Starts in present form in 1918 (B.E. 2461)
        # Sources:
        #   (ocac.got.th 's wbm) http://tiny.cc/wa_ocac_chakri
        chakri_memorial_en = "Chakri Memorial Day"

        if year >= 1918:
            add_holiday(date(year, APR, 6), chakri_memorial_en)

        # !!! Songkran Festival !!!
        # วันสงกรานต์
        # Status: In-Use
        # Used to be April 1st as Thai New Year Day
        # Initially abandoned in 1941 (B.E. 2484), declared again as
        #   public holidays in 1948 (2491 B.E)
        # This has its own in-lieu trigger
        # Sources:
        #   (museumsiam.org 's wbm) http://tiny.cc/wa_museumsiam_songkran
        #   https://resolution.soc.go.th/?prep_id=123659
        songkran_festival_en = "Songkran Festival"

        # 1948-1953, celebrated on Apr 13-15
        if 1948 <= year <= 1953:
            self[date(year, APR, 13)] = songkran_festival_en
            self[date(year, APR, 14)] = songkran_festival_en
            self[date(year, APR, 15)] = songkran_festival_en
        # 1954-1956, abandoned as a public holiday
        # 1957-1988, only celebrated on Apr 13
        elif 1957 <= year <= 1988:
            add_holiday(date(year, APR, 13), songkran_festival_en)
        # 1989-1997, celebrated on Apr 12-14
        elif 1989 <= year <= 1997:
            self[date(year, APR, 12)] = songkran_festival_en
            self[date(year, APR, 13)] = songkran_festival_en
            self[date(year, APR, 14)] = songkran_festival_en
        # 1998-Present, celebrated on Apr 13-15
        # (Except for 2020 due to Covid-19 outbreaks)
        elif year >= 1998 and year != 2020:
            self[date(year, APR, 13)] = songkran_festival_en
            self[date(year, APR, 14)] = songkran_festival_en
            self[date(year, APR, 15)] = songkran_festival_en

        # !!! Songkran Festival (in lieu) !!!
        # วันหยุดชดเชยวันสงกรานต์
        # If Songkran happened to be held on the weekends, only one in-lieu
        #   public holiday is added, No in lieus for SUN-MON-TUE case
        # Status: In Use
        # Sources:
        #   https://github.com/dr-prodigy/python-holidays/pull/929
        songkran_festival_in_lieu_en = "Songkran Festival (in lieu)"

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
                self[dt + td(days=+2)] = songkran_festival_in_lieu_en
            # CASE 2: FRI-SAT-SUN -> 1 in-lieu on MON
            elif dt.weekday() == SUN:
                self[dt + td(days=+1)] = songkran_festival_in_lieu_en
            # CASE 3: SAT-SUN-MON -> 1 in-lieu on TUE
            elif dt.weekday() == MON:
                self[dt + td(days=+1)] = songkran_festival_in_lieu_en

        # !!! Labour day !!!
        # วันแรงงานแห่งชาติ
        # Status: In-Use
        # Starts in the present form in 1974 (B.E. 2517)
        # Does existed officially since 1956 (B.E. 2499),
        #   but wasn't a public holiday until then
        # *** NOTE: only observed by financial and private sectors
        # Sources:
        #   https://www.thairath.co.th/lifestyle/culture/1832869
        national_labour_day_en = "National Labour Day"

        if year >= 1974:
            add_holiday(date(year, MAY, 1), national_labour_day_en)

        # !!! National Day (24 June) !!!
        # วันชาติ
        # Status: Defunct (Historical)
        # Starts in 1939 (B.E. 2482) by Plaek Phibunsongkhram
        # Replaced by Rama IX's birthday in 1960 (B.E. 2503) by Sarit Thanarat
        # Sources:
        #   (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
        national_day_khana_ratsadon_en = "National Day"

        if 1939 <= year <= 1959:
            add_holiday(date(year, JUN, 24), national_day_khana_ratsadon_en)

        # !!! Coronation Day !!!
        # วันฉัตรมงคล
        # Starts in 1958 (B.E. 2501)
        # No celebration in 2017-2019 (B.E 2560-2562)
        # Reestablished with Rama X's Coronation in 2020
        # Sources:
        #   https://www.matichon.co.th/politics/news_526200
        #   https://workpointtoday.com/news1-5/
        coronation_day_en = "Coronation Day"

        # Rama IX's Coronation: May 5th
        if 1958 <= year <= 2016:
            add_holiday(date(year, MAY, 5), coronation_day_en)
        # In-Between Years: No Celebration
        # Rama X's Coronation: May 4th
        elif year >= 2020:
            add_holiday(date(year, MAY, 4), coronation_day_en)

        # !!! HM Queen Suthida's Birthday !!!
        # วันเฉลิมพระชนมพรรษา พระราชินี
        # Status: In-Use
        # Starts in 2019 (B.E. 2562)
        # Sources:
        #   https://www.thairath.co.th/news/politic/1567418
        queen_suthida_birthday_en = "HM Queen Suthida's Birthday"

        if year >= 2019:
            add_holiday(date(year, JUN, 3), queen_suthida_birthday_en)

        # !!! HM King Maha Vajiralongkorn's Birthday !!!
        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 10
        # Status: In-Use
        # Started in 2017 (B.E 2560)
        # Sources:
        #   https://www.matichon.co.th/politics/news_526200
        rama_x_birthday_en = "HM King Maha Vajiralongkorn's Birthday"

        if year >= 2017:
            add_holiday(date(year, JUL, 28), rama_x_birthday_en)

        # !!! HM Queen Sirikit the Queen Mother's Birthday !!!
        # วันเฉลิมพระชนมพรรษา พระบรมราชินีนาถ ( 1976-2017),
        # วันเฉลิมพระชนมพรรษา พระบรมราชชนนีพันปีหลวง (2017-Present)
        # Status: In-Use
        # Started in 1976 (B.E. 2519) alongside Mother's Day
        # Sources:
        #   https://hilight.kapook.com/view/14164
        queen_sirikit_birthday_rama_ix_en = "HM Queen Sirikit's Birthday"
        queen_sirikit_birthday_rama_x_en = (
            "HM Queen Sirikit The Queen Mother's Birthday"
        )

        # Initial celebration as HM Queen Sirikit's Birthday
        if 1976 <= year <= 2016:
            add_holiday(date(year, AUG, 12), queen_sirikit_birthday_rama_ix_en)
        # Now acts as the Queen Mother
        elif year >= 2017:
            add_holiday(date(year, AUG, 12), queen_sirikit_birthday_rama_x_en)

        # !!! Mother's Day !!!
        # วันแม่แห่งชาติ
        # Status: In-Use
        # Started 1950 (B.E 2493) initially as April 15 and cancelled in
        #   1958 (B.E 2501) when the Min. of Culture was abolished.
        # Restarts again in 1976 (B.E. 2519) on Queen Sirikit's Birthday
        #   (August 12) and stay that way from that point onwards.
        # Sources:
        #   https://www.brh.go.th/index.php/2019-02-27-04-11-52/542-12-2564
        thai_mothers_day_en = "Mother's Day"

        # Initial Celebration on April 15
        if 1950 <= year <= 1957:
            add_holiday(date(year, APR, 15), thai_mothers_day_en)
        # In-Between years while Min. of Culture was abolished
        # Restarts in 1976 on Queen Sirikit's Birthday
        elif year >= 1976:
            add_holiday(date(year, AUG, 12), thai_mothers_day_en)

        # !!! Anniversary for the Death of King Bhumibol Adulyadej !!!
        # วันคล้ายวันสวรรคตพระบาทสมเด็จพระปรมินทร มหาภูมิพลอดุลยเดช บรมนาถบพิตร
        # Status: In-Use
        # Started in 2017 (B.E 2560)
        # Sources:
        #   https://www.matichon.co.th/politics/news_526200
        rama_ix_memorial_en = "HM King Bhumibol Adulyadej Memorial Day"

        if year >= 2017:
            add_holiday(date(year, OCT, 13), rama_ix_memorial_en)

        # !!! Chulalongkorn Memorial Day !!!
        # วันปิยมหาราช
        # Status: In-Use
        # Started in 1911 (B.E. 2454)
        # Sources:
        #   https://th.wikipedia.org/wiki/วันปิยมหาราช
        rama_five_memorial_en = "Chulalongkorn Memorial Day"

        if year >= 1911:
            add_holiday(date(year, OCT, 23), rama_five_memorial_en)

        # !!! HM King Bhumibol Adulyadej's Birthday Anniversary !!!
        # วันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (1960-2016),
        # วันคล้ายยวันเฉลิมพระชนมพรรษา รัชกาลที่ 9 (2017-Present)
        # Status: In-Use
        # Replaced Nataion Day (26 June) in 1960 (B.E. 2503) by Sarit Thanarat
        # Confirmed as still in-use in 2017
        # Sources:
        #   (Ministry of Culture 's wbm) http://tiny.cc/wa_mincul_nat_day
        #   https://hilight.kapook.com/view/148862
        rama_ix_birthday_en = "HM King Bhumibol Adulyadej's Birthday"

        if year >= 1960:
            add_holiday(date(year, DEC, 5), rama_ix_birthday_en)

        # !!! Father's Day !!!
        # วันพ่อแห่งชาติ
        # Status: In-Use
        # Starts in 1980 (B.E 2523)
        # Technically, a replication of HM King Bhumibol Adulyadej's Birthday
        #   but it's in the official calendar, so may as well have this here
        # Sources:
        #   https://www.brh.go.th/index.php/2019-02-27-04-12-21/594-5-5
        thai_fathers_day_en = "Father's Day"

        if year >= 1980:
            add_holiday(date(year, DEC, 5), thai_fathers_day_en)

        # !!! Constitution Day !!!
        # วันรัฐธรรมนูญ
        # Status: In-Use
        # Presumed to starts in 1932 (B.E. 2475) ???
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535)
        # ** Due to Thai Calendar Migration, this is capped off at 1941
        # Sources:
        #   https://hilight.kapook.com/view/18208
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        #   https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2475.aspx
        constitution_day_en = "Constitution Day"

        if year >= 1941:
            add_holiday(date(year, DEC, 10), constitution_day_en)

        # !!! New Year's Eve !!!
        # วันสิ้นปี
        # Status: In-Use
        # Presumed to start in the present form in 1941 (B.E. 2484) ???
        # Last known official record is Bank of Thailand's in 1992 (B.E. 2535)
        # This has its own in-lieu trigger
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992
        new_years_eve_en = "New Year's Eve"

        if year >= 1941:
            self[date(year, DEC, 31)] = new_years_eve_en

        ################################
        #
        # THAI LUNAR CALENDAR HOLIDAYS
        #
        ################################
        """
        So here are the basics of the Thai Lunar Calendar
            3-year types for calendar intercalation:
                - Pakatimat (Normal Year):
                        consist of 12 months, has 354 days.
                - Athikawan (Extra-Day Year): a
                        add a day to the 7th month of the year, has 355 days
                        for the synodic month correction.
                - Athikamat (Extra-Month Year):
                        we have the 8th month twice, has 384 days for the
                        sidereal year correction.

            Each month either has 30 (Even months) or 29 (Odd months)
                - The waxing phase has 15 days until Full Moon and waning
                    phase 14 (Odd Months)/15 (Even Months/
                    Month 7 of Athikawan years) days for the New Moon.
                - The second "Month 8" for Athikamat years is called
                    "Month 8.8", with all observed holy days delayed from
                    the usual calendar by 1 month.

            List of public holidays dependent on the Thai Lunar Calendar:
                - Magha Puja/Makha Bucha:
                        15th Waxing Day (Full Moon) of Month 3
                        (On Month 4 for Athikamat Years).
                - Royal Ploughing Ceremony:
                        Based on this, though Court Astrologer picks the
                        auspicious dates, which sadly don't fall into a
                        predictable pattern; see its specific section below.
                - Vesak/Visakha Bucha Bucha:
                        15th Waxing Day (Full Moon) of Month 6
                        (On Month 7 for Athikamat Years).
                - Asalha Puja/Asarnha Bucha:
                        15th Waxing Day (Full Moon) of Month 8
                        (On Month 8/8 for Athikamat Years).
                - Buddhist Lent/Wan Khao Phansa:
                        1st Waning Day of Month 8
                        (On Month 8/8 for Athikamat Years).

        The following code is based on Ninenik Narkdee's PHP implementation,
        and we're thankful for his work.

        Please avoid touching the Athikawan and Athikamat declaration array
        at all costs unless you can find sources for them somewhere for 2057++

        Sources: (Ninenik.com 's wbm) http://tiny.cc/wa_ninenik_thluncal_php
                 https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2560.aspx
        """
        # Athikawan (Extra-Day Year) list goes from 1941-2057 C.E.
        # Copied off from 1757-2057 (B.E. 2300-2600) Thai Lunar Calendar
        athikawan_years_gregorian = {
            1945,
            1949,
            1952,
            1957,
            1963,
            1970,
            1973,
            1979,
            1987,
            1990,
            1997,
            2000,
            2006,
            2009,
            2016,
            2020,
            2025,
            2032,
            2035,
            2043,
            2046,
            2052,
        }

        # Athikamat (Extra-Month Year) list goes from 1941-2057 C.E.:
        # Copied off from 1757-2057 (B.E. 2300-2600) Thai Lunar Calendar
        # Approx formula as follows: (common_era-78)-0.45222)%2.7118886 < 1
        athikamat_years_gregorian = {
            1942,
            1944,
            1947,
            1950,
            1953,
            1956,
            1958,
            1961,
            1964,
            1966,
            1969,
            1972,
            1975,
            1977,
            1980,
            1983,
            1985,
            1988,
            1991,
            1994,
            1996,
            1999,
            2002,
            2004,
            2007,
            2010,
            2012,
            2015,
            2018,
            2021,
            2023,
            2026,
            2029,
            2031,
            2034,
            2037,
            2040,
            2042,
            2045,
            2048,
            2050,
            2053,
            2056,
        }

        # While Buddhist Holy Days have been observed since the 1900s
        #   Due to the calendar changes in 1941 (B.E. 2484) and that
        #   our array only goes up to B.E. 2600; We'll thus only populate
        #   the data for 1942-2057 (B.E. 2485-2600).
        # Sources: หนังสือเวียนกรมการปกครอง กระทรวงมหาดไทย ที่ มท 0310.1/ว4
        #                          ออกเมื่อ 5 กุมภาพันธ์ พ.ศ.2539

        thai_lun_cal_st_date = date(1940, NOV, 30)
        thai_lun_cal_st_year = 1941

        # Getting the start date of that particular Thai Lunar Calendar Year
        if 1941 <= year <= 2057:
            while thai_lun_cal_st_year < year:
                if thai_lun_cal_st_year in athikamat_years_gregorian:
                    thai_lun_cal_st_date += td(days=+384)
                elif thai_lun_cal_st_year in athikawan_years_gregorian:
                    thai_lun_cal_st_date += td(days=+355)
                else:
                    thai_lun_cal_st_date += td(days=+354)
                thai_lun_cal_st_year += 1

            # !!! Makha Bucha !!!
            # วันมาฆบูชา
            # Status: In-Use
            # Athikamat: 15th Waxing Day of Month 4
            #            or 29[1] + 30[2] + 29[3] + 15[4] -1 = 102
            # Athikawan: 15th Waxing Day of Month 3
            #            or 29[1] + 30[2] + 15[3] -1 = 73
            # Pakatimat: 15th Waxing Day of Month 3
            #            or 29[1] + 30[2] + 15[3] -1 = 73
            makha_bucha_en = "Makha Bucha"

            if year in athikamat_years_gregorian:
                add_holiday(
                    thai_lun_cal_st_date + td(days=+102),
                    makha_bucha_en,
                )
            else:
                add_holiday(
                    thai_lun_cal_st_date + td(days=+73),
                    makha_bucha_en,
                )

            # !!! Visakha Bucha !!!
            # วันวิสาขบูชา
            # Status: In-Use
            # Athikamat: 15th Waxing Day of Month 6
            #            or 177[1-6] + 15[7] -1 = 191
            # Athikawan: 15th Waxing Day of Month 6
            #            or 147[1-5] + 15[6] -1 = 161
            # Pakatimat: 15th Waxing Day of Month 6
            #            or 147[1-5] + 15[6] -1 = 161
            visakha_bucha_en = "Visakha Bucha"

            if year in athikamat_years_gregorian:
                add_holiday(
                    thai_lun_cal_st_date + td(days=+191),
                    visakha_bucha_en,
                )
            else:
                add_holiday(
                    thai_lun_cal_st_date + td(days=+161),
                    visakha_bucha_en,
                )

            # !!! Asarnha Bucha !!!
            # วันอาสาฬหบูชา
            # Status: In-Use
            # Athikamat: 15th Waxing Day of Month 8/8
            #            or 177[1-6] + 29[7] + 30[8] + 15[8.8] -1 = 250
            # Athikawan: 15th Waxing Day of Month 8
            #            or 177[1-6] + 30[7] + 15[8] -1 = 221
            # Pakatimat: 15th Waxing Day of Month 8
            #            or 177[1-6] + 29[7] + 15[8] -1 = 220
            # This has its own in-lieu trigger
            asarnha_bucha_en = "Asarnha Bucha"

            if year in athikamat_years_gregorian:
                asarnha_date = thai_lun_cal_st_date + td(days=+250)
            elif year in athikawan_years_gregorian:
                asarnha_date = thai_lun_cal_st_date + td(days=+221)
            else:
                asarnha_date = thai_lun_cal_st_date + td(days=+220)

            self[asarnha_date] = asarnha_bucha_en

            # !!! Buddhist Lent Day !!!
            # วันเข้าพรรษา
            # Status: In-Use
            # Athikamat: 1st Waning Day of Month 8.8
            #            or 177[1-6] + 29[7] + 30[8] + 16[8.8] -1 = 251
            # Athikawan: 1st Waning Day of Month 8 ]
            #            or 177[1-6] + 30[7] + 16[8] -1 = 222
            # Pakatimat: 1st Waning Day of Month 8
            #            or 177[1-6] + 29[7] + 16[8] -1 = 221
            # Or as in simpler terms: "Asarnha Bucha" +1
            # This has its own in-lieu trigger
            khao_phansa_en = "Buddhist Lent Day"

            self[asarnha_date + td(days=+1)] = khao_phansa_en

            # !!! Asarnha Bucha/Buddhist Lent Day (in lieu) !!!
            # วันหยุดชดเชยวันอาสาฬหบูชา
            # วันหยุดชดเชยวันเข้าพรรษา
            # Status: In Use
            # For clearer tooltip
            asarnha_bucha_in_lieu_en = "Asarnha Bucha (in lieu)"
            khao_phansa_in_lieu_en = "Buddhist Lent Day (in lieu)"

            # Applied Automatically for Monday if on Weekends: 1961-1973
            # No In Lieu days available: 1974-1988
            # Case-by-Case application for Workday if on Weekends: 1989-1994
            # Applied Automatically for Workday if on Weekends: 1995-1997
            # Case-by-Case application for Workday if on Weekends: 1998-2000
            # Applied Automatically for Workday if on Weekends: 2001-Present
            if self.observed and (
                1961 <= year <= 1973 or 1995 <= year <= 1997 or year >= 2001
            ):
                # CASE 1: FRI-SAT -> 1 in-lieu on MON
                if asarnha_date.weekday() == FRI:
                    self[asarnha_date + td(days=+3)] = khao_phansa_in_lieu_en
                # CASE 2: SAT-SUN -> 1 in-lieu on MON
                # CASE 3: SUN-MON -> 1 in-lieu on TUE
                elif self._is_weekend(asarnha_date):
                    self[asarnha_date + td(days=+2)] = asarnha_bucha_in_lieu_en

        ###########################
        #
        # THAI BANK HOLIDAYS STUB
        #
        ###########################

        # !!! Thai Agricultural Bank Holiday !!!
        # วันหยุดเพิ่มเติมสำหรับการปิดบัญชีประจำปีของ ธ.ก.ส.
        # Status: Defunct (Historical)
        # Earliest Record is from 1992 (B.E 2535)
        # Abandoned post-2022 (B.E 2565) by Bank of Thailand
        # *** NOTE: only observed by financial sectors
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_2023

        # !!! Thai Mid-Year Bank Holiday !!!
        # วันหยุดภาคครึ่งปีของสถาบันการเงิน
        # Status: Defunct (Historical)
        # Earliest Record is from 1992 (B.E 2535)
        # Abandoned post-2019 (B.E 2562) by Bank of Thailand
        # *** NOTE: only observed by financial sectors
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_2023

        ###########################################
        #
        # THAI REGIONAL HOLIDAYS PLACEHOLDER STUB
        #
        ###########################################

        # !!! Eid al-Fitr !!!
        # วันตรุษอีดิ้ลฟิตริ (วันรายอปอซอ)
        # Status: In-Use
        # Observed in Yala, Pattani, Narathiwat, Satun, and Songkhla from
        # 1992 (B.E 2535)onwards except 2012-2013 (B.E 2555-2556)
        # *** NOTE: no in-lieu dates available
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1992

        # !!! Eid al-Adha !!!
        # วันตรุษอีดิ้ลอัฎฮา (วันรายอฮัจยี)
        # Status: In-Use
        # Observed in Yala, Pattani, Narathiwat, Satun, and Songkhla from
        # 1994 (B.E 2537) onwards except 2012-2013 (B.E 2555-2556) for Songkhla
        # *** NOTE: no in-lieu dates available
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1994

        # !!! Lunar New Year !!!
        # วันตรุษจีน
        # Status: In-Use
        # Observed in Yala, Pattani, Narathiwat, Satun, and Songkhla from
        # 1994 (B.E 2537) onwards except 2012-2013 (B.E 2555-2556)
        # *** NOTE: no in-lieu dates available
        # Sources:
        #   (Bank of Thailand 's wbm) http://tiny.cc/wa_bot_1994

        #################################
        #
        # NO FUTURE FIXED DATE HOLIDAYS
        #
        #################################

        # !!! Royal Ploughing Ceremony !!!
        # วันพืชมงคล
        # Restarts in 1957 (B.E. 2500)
        # Is dated on an annual basis by the Royal Palace
        # This isn't even fixed even by the Thai Lunar Calendar, but instead
        #   by Court Astrologers; All chosen dates are all around May, so we
        #   can technically assign it to 13 May for years prior with no data.
        # *** NOTE: only observed by government sectors
        # [TODO]: Update this annually around Dec of each year
        # Sources:
        #   https://en.wikipedia.org/wiki/Royal_Ploughing_Ceremony
        #   https://www.lib.ru.ac.th/journal/may/may_phauchmongkol.html
        #   https://www.myhora.com/ปฏิทิน/ปฏิทิน-พ.ศ.2540.aspx
        raeknakhwan_en = "Royal Ploughing Ceremony"

        raeknakhwan = {
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
        if year in raeknakhwan:
            add_holiday(date(year, *raeknakhwan[year]), raeknakhwan_en)
        # Approx. otherwise for 1957-2013
        elif 1957 <= year <= 1996:
            add_holiday(date(year, MAY, 13), raeknakhwan_en)


class TH(Thailand):
    pass


class THA(Thailand):
    pass
