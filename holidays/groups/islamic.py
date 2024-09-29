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
from typing import Iterable, Set, Tuple

from holidays.calendars import _IslamicLunar
from holidays.calendars.gregorian import _timedelta


class IslamicHolidays:
    """
    Islamic holidays.

    The Hijri calendar also known as Islamic calendar, is a lunar
    calendar consisting of 12 lunar months in a year of 354 or 355 days.
    """

    def __init__(self, cls=None) -> None:
        self._islamic_calendar = cls() if cls else _IslamicLunar()

    def _add_ali_al_rida_death_day(self, name) -> Set[date]:
        """
        Add death of Ali al-Rida day (last (29th or 30th) day of 2nd month).

        https://en.wikipedia.org/wiki/Ali_al-Rida
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.ali_al_rida_death_dates(self._year)
        )

    def _add_ali_birthday_day(self, name) -> Set[date]:
        """
        Add birthday of Ali ibn Abu Talib day (13th day of 7th month).

        https://en.wikipedia.org/wiki/Ali
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.ali_birthday_dates(self._year)
        )

    def _add_ali_death_day(self, name) -> Set[date]:
        """
        Add death of Ali ibn Abu Talib day (21st day of 9th month).

        https://en.wikipedia.org/wiki/Ali
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.ali_death_dates(self._year)
        )

    def _add_arbaeen_day(self, name) -> Set[date]:
        """
        Add Arbaeen day (20th day of 2nd month).

        https://en.wikipedia.org/wiki/Arbaeen
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.arbaeen_dates(self._year)
        )

    def _add_arafah_day(self, name) -> Set[date]:
        """
        Add Day of Arafah (9th day of 12th month).

        At dawn of this day, Muslim pilgrims will make their way from Mina
        to a nearby hillside and plain called Mount Arafat and the Plain of
        Arafat.
        https://en.wikipedia.org/wiki/Day_of_Arafah
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_adha_dates(self._year), days_delta=-1
        )

    def _add_ashura_day(self, name) -> Set[date]:
        """
        Add Ashura Day (10th day of 1st month).

        Ashura is a day of commemoration in Islam. It occurs annually on the
        10th of Muharram, the first month of the Islamic calendar.
        https://en.wikipedia.org/wiki/Ashura
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.ashura_dates(self._year)
        )

    def _add_ashura_eve(self, name) -> Set[date]:
        """
        Add Ashura Eve (Day before the 10th day of 1st month).

        Ashura is a day of commemoration in Islam. It occurs annually on the
        10th of Muharram, the first month of the Islamic calendar.
        https://en.wikipedia.org/wiki/Ashura
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.ashura_dates(self._year), days_delta=-1
        )

    def _add_eid_al_adha_day(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day (10th day of the 12th month of Islamic calendar).

        Feast of the Sacrifice. It honours the willingness of Ibrahim
        (Abraham) to sacrifice his son Ismail (Ishmael) as an act of obedience
        to Allah's command.
        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_adha_dates(self._year)
        )

    def _add_eid_al_adha_day_two(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day Two.

        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_adha_dates(self._year), days_delta=+1
        )

    def _add_eid_al_adha_day_three(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day Three.

        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_adha_dates(self._year), days_delta=+2
        )

    def _add_eid_al_adha_day_four(self, name) -> Set[date]:
        """
        Add Eid al-Adha Day Four.

        https://en.wikipedia.org/wiki/Eid_al-Adha
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_adha_dates(self._year), days_delta=+3
        )

    def _add_eid_al_fitr_day(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day (1st day of 10th month of Islamic calendar).

        Holiday of Breaking the Fast. The religious holiday is celebrated
        by Muslims worldwide because it marks the end of the month-long
        dawn-to-sunset fasting of Ramadan.
        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_fitr_dates(self._year)
        )

    def _add_eid_al_fitr_day_two(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day Two.

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_fitr_dates(self._year), days_delta=+1
        )

    def _add_eid_al_fitr_day_three(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day Three.

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_fitr_dates(self._year), days_delta=+2
        )

    def _add_eid_al_fitr_day_four(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Day Four.

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_fitr_dates(self._year), days_delta=+3
        )

    def _add_eid_al_fitr_eve(self, name) -> Set[date]:
        """
        Add Eid al-Fitr Eve (last day of 9th month of Islamic calendar).

        https://en.wikipedia.org/wiki/Eid_al-Fitr
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_fitr_dates(self._year), days_delta=-1
        )

    def _add_eid_al_ghadir_day(self, name) -> Set[date]:
        """
        Add Eid al-Ghadir Day (18th day of 12th month).

        https://en.wikipedia.org/wiki/Eid_al-Ghadeer
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.eid_al_ghadir_dates(self._year)
        )

    def _add_fatima_death_day(self, name) -> Set[date]:
        """
        Add death of Fatima day (3rd day of 6th month).

        https://en.wikipedia.org/wiki/Fatima
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.fatima_death_dates(self._year)
        )

    def _add_hari_hol_johor(self, name) -> Set[date]:
        """
        Hari Hol Johor.

        https://publicholidays.com.my/hari-hol-almarhum-sultan-iskandar/
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.hari_hol_johor_dates(self._year)
        )

    def _add_hasan_al_askari_death_day(self, name) -> Set[date]:
        """
        Add death of Hasan_al-Askari day (8th day of 3rd month).

        https://en.wikipedia.org/wiki/Hasan_al-Askari
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.hasan_al_askari_death_dates(self._year)
        )

    def _add_imam_mahdi_birthday_day(self, name) -> Set[date]:
        """
        Add birthday of Muhammad al-Mahdi day (15th day of 8th month).

        https://en.wikipedia.org/wiki/Muhammad_al-Mahdi
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.imam_mahdi_birthday_dates(self._year)
        )

    def _add_islamic_calendar_holiday(
        self, name: str, dates: Iterable[Tuple[date, bool]], days_delta: int = 0
    ) -> Set[date]:
        """
        Add lunar calendar holiday.

        Appends customizable estimation label at the end of holiday name if
        holiday date is an estimation.
        """
        added_dates = set()
        estimated_label = getattr(self, "estimated_label", "%s (estimated)")
        for dt, is_estimated in dates:
            if days_delta != 0:
                dt = _timedelta(dt, days_delta)

            dt = self._add_holiday(
                self.tr(estimated_label) % self.tr(name) if is_estimated else name, dt
            )
            if dt:
                added_dates.add(dt)

        return added_dates

    def _add_islamic_new_year_day(self, name) -> Set[date]:
        """
        Add Islamic New Year Day (last day of Dhu al-Hijjah).

        The Islamic New Year, also called the Hijri New Year, is the day that
        marks the beginning of a new lunar Hijri year, and is the day on which
        the year count is incremented. The first day of the Islamic year is
        observed by most Muslims on the first day of the month of Muharram.
        https://en.wikipedia.org/wiki/Islamic_New_Year
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.hijri_new_year_dates(self._year)
        )

    def _add_isra_and_miraj_day(self, name):
        """
        Add Isra' and Mi'raj Day (27th day of 7th month).

        The Prophet's Ascension.
        https://en.wikipedia.org/wiki/Isra%27_and_Mi%27raj
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.isra_and_miraj_dates(self._year)
        )

    def _add_maldives_embraced_islam_day(self, name) -> Set[date]:
        """
        Add Maldives Embraced Islam Day (1st day of 4th month).

        https://en.wikipedia.org/wiki/Islam_in_Maldives
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.maldives_embraced_islam_day_dates(self._year)
        )

    def _add_mawlid_day(self, name) -> Set[date]:
        """
        Add Mawlid Day (12th day of 3rd month).

        Mawlid is the observance of the birthday of the Islamic prophet
        Muhammad.
        https://en.wikipedia.org/wiki/Mawlid
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.mawlid_dates(self._year)
        )

    def _add_mawlid_day_two(self, name) -> Set[date]:
        """
        Add Mawlid Day Two.

        Mawlid is the observance of the birthday of the Islamic prophet
        Muhammad.
        https://en.wikipedia.org/wiki/Mawlid
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.mawlid_dates(self._year), days_delta=+1
        )

    def _add_nuzul_al_quran_day(self, name) -> Set[date]:
        """
        Add Nuzul Al Quran (17th day of 9th month).

        Nuzul Al Quran is a Muslim festival to remember the day when Prophet
        Muhammad received his first revelation of Islam's sacred book,
        the holy Quran.
        https://zamzam.com/blog/nuzul-al-quran/
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.nuzul_al_quran_dates(self._year)
        )

    def _add_prophet_death_day(self, name) -> Set[date]:
        """
        Add death of Prophet Muhammad and Hasan ibn Ali day (28th day of 2nd month).

        https://en.wikipedia.org/wiki/Hasan_ibn_Ali
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.prophet_death_dates(self._year)
        )

    def _add_quamee_dhuvas_day(self, name) -> Set[date]:
        """
        Add Quamee Dhuvas (1st day of 3rd month).

        https://en.wikipedia.org/wiki/Qaumee_Dhuvas_(Maldives_National_Day)
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.quamee_dhuvas_dates(self._year)
        )

    def _add_ramadan_beginning_day(self, name) -> Set[date]:
        """
        Add First Day of Ramadan (1st day of 9th month).

        Ramadan is the ninth month of the Islamic calendar, observed by Muslims
        worldwide as a month of fasting, prayer, reflection, and community
        https://en.wikipedia.org/wiki/Ramadan
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.ramadan_beginning_dates(self._year)
        )

    def _add_sadiq_birthday_day(self, name) -> Set[date]:
        """
        Add birthday of Prophet Muhammad and Ja'far al-Sadiq day (17th day of 3rd month).

        https://en.wikipedia.org/wiki/Ja%27far_al-Sadiq
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.sadiq_birthday_dates(self._year)
        )

    def _add_sadiq_death_day(self, name) -> Set[date]:
        """
        Add death of Ja'far al-Sadiq day (25th day of 10th month).

        https://en.wikipedia.org/wiki/Ja%27far_al-Sadiq
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.sadiq_death_dates(self._year)
        )

    def _add_tasua_day(self, name) -> Set[date]:
        """
        Add Tasua day (9th day of 1st month).

        https://en.wikipedia.org/wiki/Tasua
        """
        return self._add_islamic_calendar_holiday(
            name, self._islamic_calendar.tasua_dates(self._year)
        )
