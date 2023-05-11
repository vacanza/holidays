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

from holidays.constants import FEB, MAY, JUL, OCT
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
    estimated_label = tr("anggaran")
    default_language = "ms"

    # Special Cases.

    golden_jubilee_hassanal_bolkiah = tr("Jubli Emas Sultan Hassanal Bolkiah")

    special_holidays = {
        2017: ((OCT, 5, golden_jubilee_hassanal_bolkiah),),
    }

    def __init__(self, *args, **kwargs):
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self)

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
        # 4: If Sat-Sun-Mon -> Fri (-1)
        # 5: If Sun-Mon-Tue -> Wed (+3)

        aidil_fitri_in_lieu = self.tr("%s - Diperhatikan") % name

        if self.observed:
            for dt in alfitr:
                if (
                    self._is_wednesday(dt)
                    or self._is_friday(dt)
                    or self._is_sunday(dt)
                ):
                    self._add_holiday(aidil_fitri_in_lieu, dt + td(days=+3))
                elif self._is_thursday(dt):
                    self._add_holiday(aidil_fitri_in_lieu, dt + td(days=+4))
                elif self._is_saturday(dt):
                    self._add_holiday(aidil_fitri_in_lieu, dt + td(days=-1))

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
