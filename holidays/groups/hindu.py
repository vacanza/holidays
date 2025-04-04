#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from collections.abc import Iterable
from datetime import date
from typing import Optional

from holidays.calendars import _HinduLunisolar
from holidays.groups.eastern import EasternCalendarHolidays


class HinduCalendarHolidays(EasternCalendarHolidays):
    """
    Hindu lunisolar calendar holidays.
    """

    def __init__(self, cls=None, show_estimated=False) -> None:
        self._hindu_calendar = cls() if cls else _HinduLunisolar()
        self._hindu_calendar_show_estimated = show_estimated

    def _add_hindu_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool]
    ) -> Optional[date]:
        """
        Add Hindu calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """

        return self._add_eastern_calendar_holiday(
            name, dt_estimated, self._hindu_calendar_show_estimated
        )

    def _add_hindu_calendar_holiday_set(
        self, name: str, dts_estimated: Iterable[tuple[date, bool]], days_delta: int = 0
    ) -> set[date]:
        """
        Add Hindu calendar holidays.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        added_dates = set()
        for dt_estimated in dts_estimated:
            if dt := self._add_eastern_calendar_holiday(
                name, dt_estimated, self._hindu_calendar_show_estimated, days_delta=days_delta
            ):
                added_dates.add(dt)

        return added_dates

    def _add_buddha_purnima(self, name) -> Optional[date]:
        """
        Add Buddha Purnima.

        Buddha Purnima, also known as Vesak, commemorates the birth, enlightenment,
        and passing of Gautama Buddha. It falls on the full moon day of the
        Hindu month of Vaisakha (April-May).
        https://en.wikipedia.org/wiki/Vesak
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.buddha_purnima_date(self._year)
        )

    def _add_chhath_puja(self, name) -> Optional[date]:
        """
        Add Chhath Puja.

        Chhath Puja is a Hindu festival dedicated to the Sun God (Surya).
        It is observed six days after Diwali in the month of Kartika (October-November).
        https://en.wikipedia.org/wiki/Chhath
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.chhath_puja_date(self._year)
        )

    def _add_diwali(self, name) -> Optional[date]:
        """
        Add Diwali Festival.

        Diwali (Deepavali, Festival of Lights) is one of the most important
        festivals in Indian religions. It is celebrated during the Hindu
        lunisolar months of Ashvin and Kartika (between mid-October and
        mid-November).
        https://en.wikipedia.org/wiki/Diwali
        """
        return self._add_hindu_calendar_holiday(name, self._hindu_calendar.diwali_date(self._year))

    def _add_diwali_india(self, name) -> Optional[date]:
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.diwali_india_date(self._year)
        )

    def _add_dussehra(self, name) -> Optional[date]:
        """
        Add Dussehra Festival.

        Dussehra (Vijayadashami) is a major Hindu festival that marks the end
        of Navratri. It is celebrated on the 10th day of the Hindu lunisolar
        month of Ashvin (September-October).
        https://en.wikipedia.org/wiki/Vijayadashami
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.dussehra_date(self._year)
        )

    def _add_ganesh_chaturthi(self, name) -> Optional[date]:
        """
        Add Ganesh Chaturthi.

        Ganesh Chaturthi is a Hindu festival celebrating the birth of Lord Ganesha.
        It falls on the fourth day of the Hindu month of Bhadrapada (August/September).
        https://en.wikipedia.org/wiki/Ganesh_Chaturthi
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.ganesh_chaturthi_date(self._year)
        )

    def _add_govardhan_puja(self, name) -> Optional[date]:
        """
        Add Govardhan Puja.

        Govardhan Puja, also known as Annakut, is celebrated the day after Diwali
        to honor Lord Krishna. It falls on the first lunar day of the Hindu month of Kartika.
        https://en.wikipedia.org/wiki/Govardhan_Puja
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.govardhan_puja_date(self._year)
        )

    def _add_gudi_padwa(self, name) -> Optional[date]:
        """
        Add Gudi Padwa.

        Gudi Padwa is the traditional New Year festival for Maharashtrians.
        It falls on the first day of Chaitra (March-April).
        https://en.wikipedia.org/wiki/Gudi_Padwa
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.gudi_padwa_date(self._year)
        )

    def _add_guru_gobind_singh_jayanti(self, name) -> set[date]:
        """
        Add Guru Gobind Singh Jayanti.

        Guru Gobind Singh Jayanti commemorates the birth anniversary of
        Guru Gobind Singh, the tenth Sikh Guru. It follows the Nanakshahi calendar.
        https://en.wikipedia.org/wiki/Guru_Gobind_Singh
        """
        return self._add_hindu_calendar_holiday_set(
            name, self._hindu_calendar.guru_gobind_singh_jayanti_date(self._year)
        )

    def _add_guru_nanak_jayanti(self, name) -> Optional[date]:
        """
        Add Guru Nanak Jayanti.

        Guru Nanak Jayanti celebrates the birth anniversary of Guru Nanak,
        the founder of Sikhism. It is observed on the full moon day of
        Kartik (October-November).
        https://en.wikipedia.org/wiki/Guru_Nanak_Gurpurab
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.guru_nanak_jayanti_date(self._year)
        )

    def _add_holi(self, name) -> Optional[date]:
        """
        Add Holi Festival.

        Holi, known as the Festival of Colors, is a Hindu festival that marks
        the arrival of spring. It is celebrated on the full moon day of the
        Hindu month of Phalguna (February/March).
        https://en.wikipedia.org/wiki/Holi
        """
        return self._add_hindu_calendar_holiday(name, self._hindu_calendar.holi_date(self._year))

    def _add_janmashtami(self, name) -> Optional[date]:
        """
        Add Janmashtami.

        Janmashtami is a Hindu festival that celebrates the birth of Lord Krishna.
        It falls on the eighth day of the Hindu month of Bhadrapada (August/September).
        https://en.wikipedia.org/wiki/Krishna_Janmashtami
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.janmashtami_date(self._year)
        )

    def _add_maha_navami(self, name) -> Optional[date]:
        """
        Add Maha Navami.

        Maha Navami is the ninth day of Navratri, dedicated to Goddess Durga.
        It is observed in Ashvin (September-October).
        https://en.wikipedia.org/wiki/Navaratri
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.maha_navami_date(self._year)
        )

    def _add_maha_shivaratri(self, name) -> Optional[date]:
        """
        Add Maha Shivaratri.

        Maha Shivaratri is a Hindu festival dedicated to Lord Shiva. It is celebrated
        on the 14th night of the Hindu month of Phalguna (February/March).
        https://en.wikipedia.org/wiki/Maha_Shivaratri
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.maha_shivaratri_date(self._year)
        )

    def _add_mahavir_jayanti(self, name) -> Optional[date]:
        """
        Add Mahavir Jayanti.

        Mahavir Jayanti celebrates the birth of Lord Mahavira, the 24th
        Tirthankara of Jainism. It falls on the 13th day of Chaitra (March-April).
        https://en.wikipedia.org/wiki/Mahavir_Jayanti
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.mahavir_jayanti_date(self._year)
        )

    def _add_makar_sankranti(self, name) -> Optional[date]:
        """
        Add Makar Sankranti.

        Makar Sankranti is a Hindu festival that marks the transition of the Sun
        into Capricorn (Makar). It is celebrated on January 14th or 15th every year.
        https://en.wikipedia.org/wiki/Makar_Sankranti
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.makar_sankranti_date(self._year)
        )

    def _add_onam(self, name) -> Optional[date]:
        """
        Add Onam.

        Onam is a major festival in Kerala, celebrating the homecoming of
        King Mahabali. It falls in the month of Chingam (August-September).
        https://en.wikipedia.org/wiki/Onam
        """
        return self._add_hindu_calendar_holiday(name, self._hindu_calendar.onam_date(self._year))

    def _add_raksha_bandhan(self, name) -> Optional[date]:
        """
        Add Raksha Bandhan.

        Raksha Bandhan is a Hindu festival that celebrates the bond between
        brothers and sisters. It falls on the full moon day of the Hindu month
        of Shravana (July/August).
        https://en.wikipedia.org/wiki/Raksha_Bandhan
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.raksha_bandhan_date(self._year)
        )

    def _add_ram_navami(self, name) -> Optional[date]:
        """
        Add Ram Navami.

        Ram Navami is a Hindu festival celebrating the birth of Lord Rama.
        It is observed on the ninth day of the Hindu month of Chaitra (March/April).
        https://en.wikipedia.org/wiki/Rama_Navami
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.ram_navami_date(self._year)
        )

    def _add_sharad_navratri(self, name) -> Optional[date]:
        """
        Add Navratri / Sharad Navratri.

        Navratri is a Hindu festival dedicated to the worship of Goddess Durga.
        It is celebrated over nine nights and occurs in the lunar month of Ashvin
        (September/October).
        https://en.wikipedia.org/wiki/Navratri
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.sharad_navratri_date(self._year)
        )

    def _add_thaipusam(self, name) -> Optional[date]:
        """
        Add Thaipusam.

        Thaipusam is a Tamil Hindu festival celebrated on the full moon
        of the Tamil month of Thai (January/February).
        https://en.wikipedia.org/wiki/Thaipusam
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.thaipusam_date(self._year)
        )

    def _add_vaisakhi(self, name) -> Optional[date]:
        """
        Add Vaisakhi.

        Vaisakhi is a major Sikh festival marking the Sikh New Year and the
        founding of the Khalsa. It falls on April 13 or 14.
        https://en.wikipedia.org/wiki/Vaisakhi
        """
        return self._add_hindu_calendar_holiday(
            name, self._hindu_calendar.vaisakhi_date(self._year)
        )
