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
from gettext import gettext as tr
from typing import Optional

from holidays.calendars import _CustomHinduHolidays
from holidays.calendars.gregorian import (
    MAR,
    JUL,
    OCT,
    NOV,
)
from holidays.groups.christian import ChristianHolidays
from holidays.groups.hindu import HinduCalendarHolidays
from holidays.groups.islamic import IslamicHolidays
from holidays.observed_holiday_base import SAT_TO_NONE, SUN_TO_NONE, ObservedHolidayBase

BAKRI_ID = "BAKRI_ID"
CHRISTMAS_DAY = "CHRISTMAS_DAY"
DIWALI_BALIPRATIPADA = "DIWALI_BALIPRATIPADA"
DIWALI_LAXMI_PUJAN = "DIWALI_LAXMI_PUJAN"
DUSSEHRA = "DUSSEHRA"
DR_BABA_SAHEB_AMBEDKAR_JAYANTI = "DR_BABA_SAHEB_AMBEDKAR_JAYANTI"
GANESH_CHATURTHI = "GANESH_CHATURTHI"
GOOD_FRIDAY = "GOOD_FRIDAY"
GURU_NANAK_JAYANTI = "GURU_NANAK_JAYANTI"
HOLI = "HOLI"
ID_UL_FITR = "ID_UL_FITR"
INDEPENDENCE_DAY = "INDEPENDENCE_DAY"
MAHARASHTRA_DAY = "MAHARASHTRA_DAY"
MAHA_SHIVARATRI = "MAHA_SHIVARATRI"
MAHATMA_GANDHI_JAYANTI = "MAHATMA_GANDHI_JAYANTI"
MAHAVIR_JAYANTI = "MAHAVIR_JAYANTI"
MUHARRAM = "MUHARRAM"
RAM_NAVAMI = "RAM_NAVAMI"
REPUBLIC_DAY = "REPUBLIC_DAY"


class NationalStockExchangeOfIndia(
    ObservedHolidayBase, HinduCalendarHolidays, ChristianHolidays, IslamicHolidays
):
    """National Stock Exchange of India (NSE) holidays.

    References:
        * <https://web.archive.org/web/20250821175252/https://www.nseindia.com/resources/exchange-communication-circulars>

    Historical data:
        * [2022](https://web.archive.org/web/20250821071611/https://nsearchives.nseindia.com/content/circulars/CMTR50560.pdf)
        * [2023](https://web.archive.org/web/20250821071635/https://nsearchives.nseindia.com/content/circulars/CMTR54757.pdf)
        * [2024](https://web.archive.org/web/20250821071650/https://nsearchives.nseindia.com/content/circulars/CMTR59722.pdf)
        * [2025](https://web.archive.org/web/20250624132016/https://nsearchives.nseindia.com/content/circulars/CMTR65587.pdf)
    """

    market = "XNSE"
    default_language = "en_IN"
    supported_languages = ("en_IN", "en_US", "hi")
    estimated_label = tr("%s")
    # NSE launched its services in 1994.
    start_year = 1995

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("observed_rule", SAT_TO_NONE + SUN_TO_NONE)
        HinduCalendarHolidays.__init__(self, cls=NationalStockExchangeOfIndiaHinduHolidays)
        ChristianHolidays.__init__(self)
        IslamicHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    DIWALI_BALIPRATIPADA_DATES = {
        2023: (NOV, 14),
        2025: (OCT, 22),
    }

    DIWALI_LAXMI_PUJAN_DATES = {
        2024: (NOV, 1),
        2025: (OCT, 21),
    }

    MUHARRAM_DATES = {
        2024: (JUL, 17),
    }

    def _populate_public_holidays(self):
        # No fixed annual closures that apply every year on the same date.

        # Republic Day.
        self._move_holiday(self._add_holiday_jan_26(tr("Republic Day")))

        # Dr. Baba Saheb Ambedkar Jayanti.
        self._move_holiday(self._add_holiday_apr_14(tr("Dr. Baba Saheb Ambedkar Jayanti")))

        # Maharashtra Day.
        self._move_holiday(self._add_holiday_may_1(tr("Maharashtra Day")))

        # Independence Day.
        self._move_holiday(self._add_holiday_aug_15(tr("Independence Day")))

        # Mahatma Gandhi Jayanti.
        self._move_holiday(self._add_holiday_oct_2(tr("Mahatma Gandhi Jayanti")))

        # Christmas Day.
        self._move_holiday(self._add_christmas_day(tr("Christmas Day")))

        # Bakri Id
        if self._year == 2023:
            self._traverse_set(self._add_eid_al_adha_day(tr("Bakri Id")))
        else:
            self._traverse_set(self._add_eid_al_adha_day_two(tr("Bakri Id")))

        # Diwali Balipratipada
        self._get_holiday(tr("Diwali Balipratipada"), DIWALI_BALIPRATIPADA, self._year)

        # Diwali Laxmi Pujan
        self._get_holiday(tr("Diwali Laxmi Pujan"), DIWALI_LAXMI_PUJAN, self._year)

        # Dussehra
        self._move_holiday(self._add_dussehra(tr("Dussehra")))

        # Ganesh Chaturthi
        self._move_holiday(self._add_ganesh_chaturthi(tr("Ganesh Chaturthi")))

        # Good Friday
        self._move_holiday(self._add_good_friday(tr("Good Friday")))

        # Guru Nanak Jayanti
        self._move_holiday(self._add_guru_nanak_jayanti(tr("Guru Nanak Jayanti")))

        # Holi
        self._move_holiday(self._add_holi(tr("Holi")))

        # Id Ul Fitr (Ramadan Eid)
        self._traverse_set(self._add_eid_al_fitr_day_two(tr("Id-Ul-Fitr (Ramadan Eid)")))

        # Maha Shivaratri
        self._move_holiday(self._add_maha_shivaratri(tr("Maha Shivaratri")))

        # Mahavir Jayanti
        self._move_holiday(self._add_mahavir_jayanti(tr("Mahavir Jayanti")))

        # Muharram
        self._get_holiday(tr("Muharram"), MUHARRAM, self._year)

        # Ram Navami
        self._move_holiday(self._add_ram_navami(tr("Ram Navami")))

    def _get_holiday(self, name, holiday: str, year: int) -> Optional[date]:
        exact_date = getattr(self, f"{holiday}_DATES", {})
        dt = exact_date.get(year)
        return self._add_holiday(name, date(year, *dt)) if dt else None

    def _traverse_set(self, dts: set[date]) -> set[date]:
        for dt in dts:
            self._move_holiday(dt)
        return dts


class NSE(NationalStockExchangeOfIndia):
    """Alias of NationalStockExchangeOfIndia"""

    pass


class XNSE(NationalStockExchangeOfIndia):
    """Alias of NationalStockExchangeOfIndia"""

    pass


class NationalStockExchangeOfIndiaHinduHolidays(_CustomHinduHolidays):
    HOLI_DATES = {
        2023: (MAR, 7),
    }
