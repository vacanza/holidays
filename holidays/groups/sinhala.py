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

from collections.abc import Iterable
from datetime import date
from typing import Optional

from holidays.calendars import _SinhalaLunar
from holidays.groups.eastern import EasternCalendarHolidays


class SinhalaCalendarHolidays(EasternCalendarHolidays):
    """
    Sinhala holidays.

    Sinhala Buddhist Uposatha day calculation method is different from Thai LuniSolar
    and Buddhist (Mahayana) used in East Asia.

    Due to the fact that Poya (Uposatha) days are calculated astronomically
    based on how close a particular day is closest to full moon at noon, and that
    an extra month is added every 33 months interval, this is hardcoded for now.

    Adhi month dates are instead hardcoded in Sri Lanka country implementation.
    """

    def __init__(self, cls=None, show_estimated=False) -> None:
        self._sinhala_calendar = cls() if cls else _SinhalaLunar()
        self._sinhala_calendar_show_estimated = show_estimated

    def _add_sinhala_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool]
    ) -> Optional[date]:
        """
        Add Sinhala calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        return self._add_eastern_calendar_holiday(
            name, dt_estimated, self._sinhala_calendar_show_estimated
        )

    def _add_sinhala_calendar_holiday_set(
        self, name: str, dts_estimated: Iterable[tuple[date, bool]], days_delta: int = 0
    ) -> set[date]:
        """
        Add Sinhala calendar holidays.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        added_dates = set()
        for dt_estimated in dts_estimated:
            if dt := self._add_eastern_calendar_holiday(
                name, dt_estimated, self._sinhala_calendar_show_estimated, days_delta=days_delta
            ):
                added_dates.add(dt)

        return added_dates

    def _add_bak_poya(self, name) -> Optional[date]:
        """
        Add Bak Poya (first full moon day of the 5th lunar month).

        https://us.lakpura.com/pages/bak-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.bak_poya_date(self._year)
        )

    def _add_binara_poya(self, name) -> Optional[date]:
        """
        Add Binara Poya (first full moon day of the 10th lunar month).

        https://us.lakpura.com/pages/binara-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.binara_poya_date(self._year)
        )

    def _add_duruthu_poya(self, name) -> set[date]:
        """
        Add Duruthu Poya (first full moon day of the 2nd lunar month).

        https://us.lakpura.com/pages/duruthu-poya
        """
        return self._add_sinhala_calendar_holiday_set(
            name, self._sinhala_calendar.duruthu_poya_date(self._year)
        )

    def _add_esala_poya(self, name) -> Optional[date]:
        """
        Add Esala Poya (first full moon day of the 8th lunar month).

        https://us.lakpura.com/pages/esala-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.esala_poya_date(self._year)
        )

    def _add_il_poya(self, name) -> Optional[date]:
        """
        Add Il Poya (first full moon day of the 12th lunar month).

        Also known as "Ill Poya"
        https://us.lakpura.com/pages/il-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.il_poya_date(self._year)
        )

    def _add_medin_poya(self, name) -> Optional[date]:
        """
        Add Medin Poya (first full moon day of the 4th lunar month).

        https://us.lakpura.com/pages/medin-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.medin_poya_date(self._year)
        )

    def _add_nawam_poya(self, name) -> Optional[date]:
        """
        Add Nawam Poya (first full moon day of the 3rd lunar month).

        Also known as "Navam Poya" and "Magha Puja".
        https://us.lakpura.com/pages/navam-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.nawam_poya_date(self._year)
        )

    def _add_nikini_poya(self, name) -> Optional[date]:
        """
        Add Nikini Poya (first full moon day of the 9th lunar month).

        https://us.lakpura.com/pages/nikini-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.nikini_poya_date(self._year)
        )

    def _add_poson_poya(self, name) -> Optional[date]:
        """
        Add Poson Poya (first full moon day of the 7th lunar month).

        https://us.lakpura.com/pages/poson
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.poson_poya_date(self._year)
        )

    def _add_unduvap_poya(self, name) -> Optional[date]:
        """
        Add Unduvap Poya (first full moon day of the 1st lunar month).

        Also known as "Undawap Poya".
        https://us.lakpura.com/pages/unduvap-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.unduvap_poya_date(self._year)
        )

    def _add_vap_poya(self, name) -> Optional[date]:
        """
        Add Vap Poya (first full moon day of the 11th lunar month).

        https://us.lakpura.com/pages/vap-poya
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.vap_poya_date(self._year)
        )

    def _add_vesak_poya(self, name) -> Optional[date]:
        """
        Add Vesak Poya (first full moon day of the 6th lunar month).

        Also known as "Wesak Poya".
        https://us.lakpura.com/pages/vesak
        """
        return self._add_sinhala_calendar_holiday(
            name, self._sinhala_calendar.vesak_poya_date(self._year)
        )
