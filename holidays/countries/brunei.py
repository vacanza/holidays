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
from gettext import gettext as tr

from holidays.calendars import _CustomCalendar, _IslamicLunar
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from holidays.holiday_groups import ChineseCalendarHolidays, ChristianHolidays
from holidays.holiday_groups import InternationalHolidays, IslamicHolidays


class Brunei(
    HolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
):
    """
    A subclass of :py:class:`HolidayBase` representing public holidays
    in Brunei Darussalam.


    References:

    - Based on: http://www.labour.gov.bn/Lists/Upcomming%20events/AllItems.aspx
                http://www.labour.gov.bn/Download/GUIDE%20TO%20BRUNEI%20EMPLOYMENT%20LAWS%20-%20english%20version-3.pdf  # noqa: E501
    - Checked with: https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf  # noqa: E501
                    https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf  # noqa: E501
                    https://www.timeanddate.com/holidays/brunei/
    - [Jubli Emas Sultan Hassanal Bolkiah]
        https://www.brudirect.com/news.php?id=28316

    Limitations:

    - Brunei Darussalam holidays only works from 1984 onwards
    - Islamic holidays


    Country created by: `PPsyrius <https://github.com/PPsyrius>`__

    Country maintained by: `PPsyrius <https://github.com/PPsyrius>`__
    """

    country = "BN"
    default_language = "ms"
    estimated_label = tr("%s* (*anggaran)")
    supported_languages = ("en_US", "ms", "th")

    # Special Cases.

    golden_jubilee_hassanal_bolkiah = tr("Jubli Emas Sultan Hassanal Bolkiah")

    special_holidays = {
        2017: ((OCT, 5, golden_jubilee_hassanal_bolkiah),),
    }

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, calendar=BruneiIslamicCalendar())

        super().__init__(*args, **kwargs)

    def _populate(self, year):
        # Available post-Independence from 1984 afterwards
        if year <= 1983:
            return None

        def _add_observed(dt: date) -> None:
            """
            If Public Holiday falls on either Friday or Sunday, in-lieu
            observance are given out on the following Saturday or Monday.
            """
            if self.observed and (self._is_friday(dt) or self._is_sunday(dt)):
                for name in self.get_list(dt):
                    self._add_holiday(
                        self.tr("%s - Diperhatikan") % name, dt + td(days=+1)
                    )

        super()._populate(year)

        # New Year's Day.
        # Awal Tahun Masihi
        # Status: In-Use.

        _add_observed(self._add_new_years_day(tr("Awal Tahun Masihi")))

        # Lunar New Year
        # Tahun Baru Cina
        # Status: In-Use.

        _add_observed(self._add_chinese_new_years_day(tr("Tahun Baru Cina")))

        # Isra Mi'raj
        # Israk dan Mikraj
        # Status: In-Use.

        for dt in self._add_isra_and_miraj_day(tr("Israk dan Mikraj")):
            _add_observed(dt)

        # National Day
        # Hari Kebangsaan
        # Status: In-Use.
        # Starts in 1984.

        _add_observed(self._add_holiday(tr("Hari Kebangsaan"), FEB, 23))

        # First Day of Ramadan
        # Hari Pertama Berpuasa
        # Status: In-Use.

        for dt in self._add_ramadan_beginning_day(tr("Hari Pertama Berpuasa")):
            _add_observed(dt)

        # Anniversary of the revelation of the Quran
        # Hari Nuzul Al-Quran
        # Status: In-Use.

        for dt in self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")):
            _add_observed(dt)

        # Eid al-Fitr
        # Hari Raya Aidil Fitri
        # Status: In-Use.
        # This is celebrate for three days in Brunei.
        # Observed as 'Hari Raya Puasa' and only for 2 days at certain point.

        name = tr("Hari Raya Aidil Fitri")

        alfitr = self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Fitr (Observed)
        # Hari Raya Aidil Fitri - Diperhatikan
        # 1: If Wed-Thu-Fri -> Sat (+3)
        # 2: If Thu-Fri-Sat -> Mon (+4)
        # 3: If Fri-Sat-Sun -> Mon (+3)
        # 4: If Sat-Sun-Mon -> Tue (+3)
        # 5: If Sun-Mon-Tue -> Wed (+3)

        aidil_fitri_in_lieu = self.tr("%s - Diperhatikan") % self.tr(
                                "Hari Raya Aidil Fitri"
                              )

        if self.observed:
            for dt in alfitr:
                if (
                    self._is_wednesday(dt)
                    or self._is_friday(dt)
                    or self._is_saturday(dt)
                    or self._is_sunday(dt)
                ):
                    self._add_holiday(aidil_fitri_in_lieu, dt + td(days=+3))
                elif self._is_thursday(dt):
                    self._add_holiday(aidil_fitri_in_lieu, dt + td(days=+4))

        # Armed Forces Day
        # Hari Angkatan Bersenjata Diraja Brunei
        # Status: In-Use.
        # Starts in 1984.
        # Commemorates the formation of Royal Brunei Malay Regiment in 1961.

        _add_observed(
            self._add_holiday(
                tr("Hari Angkatan Bersenjata Diraja Brunei"), MAY, 31
            )
        )

        # Eid al-Adha
        # Hari Raya Aidil Adha
        # Status: In-Use.

        for dt in self._add_eid_al_adha_day(tr("Hari Raya Aidil Adha")):
            _add_observed(dt)

        # Sultan Hassanal Bolkiah's Birthday
        # Hari Keputeraan KDYMM Sultan Brunei
        # Status: In-Use.
        # Started in 1968.

        _add_observed(
            self._add_holiday(
                tr("Hari Keputeraan KDYMM Sultan Brunei"), JUL, 15
            )
        )

        # Islamic New Year
        # Awal Tahun Hijrah
        # Status: In-Use.

        for dt in self._add_islamic_new_year_day(tr("Awal Tahun Hijrah")):
            _add_observed(dt)

        # Birth of the Prophet
        # Maulidur Rasul
        # Status: In-Use.

        for dt in self._add_mawlid_day(tr("Maulidur Rasul")):
            _add_observed(dt)

        # Christmas Day.
        # Hari Natal
        # Status: In-Use.

        _add_observed(self._add_christmas_day(tr("Hari Natal")))

        # Former Holidays
        # This section is here should we extend our calendar coverage later on.

        # Good Friday
        # Good Friday
        # Status: No longer observed post-Independence.

        # Freedom Day
        # Hari Kebebasan
        # Status: No longer observed.
        # Commemorating the landing of the Allies in Muara to liberate Brunei
        #   on June 10, 1945. Presumed to be observed from 1946-1983.

        # Queen Elizabeth II's Birthday
        # Hari Lahir Queen
        # Status: No longer observed.
        # Observed on June, 12 from 1952-1983.

        # Sultan Omar Ali Saifuddien III's Birthday
        # Hari Lahir Duli Yang Maha Mulia
        # Status: No longer observed.
        # Observed on September, 23 from 1950-1967.

        # Safar Bath
        # Mandi Safar
        # Status: No longer observed.
        # Observed on last Wednesday on the month of Safar until around 1963.


class BN(Brunei):
    pass


class BRN(Brunei):
    pass


class BruneiIslamicCalendar(_CustomCalendar, _IslamicLunar):
    ISRA_AND_MIRAJ_DATES = {
        2000: ((OCT, 26),),
        2001: ((OCT, 15),),
        2002: ((OCT, 4),),
        2003: ((SEP, 24),),
        2004: ((SEP, 12),),
        2005: ((SEP, 1),),
        2006: ((AUG, 22),),
        2007: ((AUG, 11),),
        2008: ((JUL, 31),),
        2009: ((JUL, 20),),
        2010: ((JUL, 9),),
        2011: ((JUN, 29),),
        2012: ((JUN, 17),),
        2013: ((JUN, 6),),
        2014: ((MAY, 27),),
        2015: ((MAY, 16),),
        2016: ((MAY, 5),),
        2017: ((APR, 24),),
        2018: ((APR, 14),),
        2019: ((APR, 3),),
        2020: ((MAR, 22),),
        2021: ((MAR, 11),),
        2022: ((MAR, 1),),
        2023: ((FEB, 18),),
    }

    RAMADAN_BEGINNING_DATES = {
        2000: ((NOV, 28),),
        2001: ((NOV, 17),),
        2002: ((NOV, 6),),
        2003: ((OCT, 27),),
        2004: ((OCT, 16),),
        2005: ((OCT, 5),),
        2006: ((SEP, 24),),
        2007: ((SEP, 13),),
        2008: ((SEP, 2),),
        2009: ((AUG, 22),),
        2010: ((AUG, 11),),
        2011: ((AUG, 1),),
        2012: ((JUL, 20),),
        2013: ((JUL, 9),),
        2014: ((JUN, 29),),
        2015: ((JUN, 18),),
        2016: ((JUN, 7),),
        2017: ((MAY, 27),),
        2018: ((MAY, 16),),
        2019: ((MAY, 6),),
        2020: ((APR, 25),),
        2021: ((APR, 13),),
        2022: ((APR, 3),),
        2023: ((MAR, 23),),
    }

    NUZUL_AL_QURAN_DATES = {
        2000: ((DEC, 14),),
        2001: ((DEC, 3),),
        2002: ((NOV, 22),),
        2003: ((NOV, 12),),
        2004: ((NOV, 1),),
        2005: ((OCT, 21),),
        2006: ((OCT, 10),),
        2007: ((SEP, 29),),
        2008: ((SEP, 18),),
        2009: ((SEP, 7),),
        2010: ((AUG, 27),),
        2011: ((AUG, 17),),
        2012: ((AUG, 5),),
        2013: ((JUL, 25),),
        2014: ((JUL, 15),),
        2015: ((JUL, 4),),
        2016: ((JUN, 23),),
        2017: ((JUN, 12),),
        2018: ((JUN, 2),),
        2019: ((MAY, 23),),
        2020: ((MAY, 10),),
        2021: ((APR, 29),),
        2022: ((APR, 19),),
        2023: ((APR, 8),),
    }

    EID_AL_FITR_DATES = {
        2000: ((JAN, 8), (DEC, 28)),
        2001: ((DEC, 17),),
        2002: ((DEC, 6),),
        2003: ((NOV, 26),),
        2004: ((NOV, 14),),
        2005: ((NOV, 3),),
        2006: ((OCT, 24),),
        2007: ((OCT, 13),),
        2008: ((OCT, 1),),
        2009: ((SEP, 20),),
        2010: ((SEP, 10),),
        2011: ((AUG, 31),),
        2012: ((AUG, 19),),
        2013: ((AUG, 8),),
        2014: ((JUL, 29),),
        2015: ((JUL, 18),),
        2016: ((JUL, 7),),
        2017: ((JUN, 26),),
        2018: ((JUN, 15),),
        2019: ((JUN, 5),),
        2020: ((MAY, 24),),
        2021: ((MAY, 13),),
        2022: ((MAY, 3),),
        2023: ((APR, 22),),
    }

    EID_AL_ADHA_DATES = {
        2000: ((MAR, 16),),
        2001: ((MAR, 6),),
        2002: ((FEB, 23),),
        2003: ((FEB, 12),),
        2004: ((FEB, 2),),
        2005: ((JAN, 21),),
        2006: ((JAN, 10), (DEC, 31)),
        2007: ((DEC, 20),),
        2008: ((DEC, 9),),
        2009: ((NOV, 28),),
        2010: ((NOV, 17),),
        2011: ((NOV, 7),),
        2012: ((OCT, 26),),
        2013: ((OCT, 15),),
        2014: ((OCT, 5),),
        2015: ((SEP, 24),),
        2016: ((SEP, 13),),
        2017: ((SEP, 2),),
        2018: ((AUG, 22),),
        2019: ((AUG, 11),),
        2020: ((AUG, 1),),
        2021: ((JUL, 20),),
        2022: ((JUL, 10),),
        2023: ((JUN, 29),),
    }

    HIJRI_NEW_YEAR_DATES = {
        2000: ((APR, 6),),
        2001: ((MAR, 26),),
        2002: ((MAR, 15),),
        2003: ((MAR, 5),),
        2004: ((FEB, 22),),
        2005: ((FEB, 10),),
        2006: ((JAN, 31),),
        2007: ((JAN, 20),),
        2008: ((JAN, 10), (DEC, 29)),
        2009: ((DEC, 18),),
        2010: ((DEC, 8),),
        2011: ((NOV, 27),),
        2012: ((NOV, 15),),
        2013: ((NOV, 5),),
        2014: ((OCT, 25),),
        2015: ((OCT, 15),),
        2016: ((OCT, 3),),
        2017: ((SEP, 22),),
        2018: ((SEP, 12),),
        2019: ((SEP, 1),),
        2020: ((AUG, 20),),
        2021: ((AUG, 10),),
        2022: ((JUL, 30),),
        2023: ((JUL, 19),),
    }

    MAWLID_DATES = {
        2000: ((JUN, 15),),
        2001: ((JUN, 4),),
        2002: ((MAY, 24),),
        2003: ((MAY, 14),),
        2004: ((MAY, 2),),
        2005: ((APR, 21),),
        2006: ((APR, 11),),
        2007: ((MAR, 31),),
        2008: ((MAR, 20),),
        2009: ((MAR, 9),),
        2010: ((FEB, 26),),
        2011: ((FEB, 16),),
        2012: ((FEB, 5),),
        2013: ((JAN, 24),),
        2014: ((JAN, 14),),
        2015: ((JAN, 3), (DEC, 24)),
        2016: ((DEC, 12),),
        2017: ((DEC, 1),),
        2018: ((NOV, 21),),
        2019: ((NOV, 9),),
        2020: ((OCT, 29),),
        2021: ((OCT, 19),),
        2022: ((OCT, 8),),
        2023: ((SEP, 28),),
    }
