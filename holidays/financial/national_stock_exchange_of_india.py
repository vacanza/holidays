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

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.observed_holiday_base import ObservedHolidayBase

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


class NationalStockExchangeOfIndia(ObservedHolidayBase):
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
    # %s (observed).
    observed_label = tr("%s (observed)")
    # NSE launched its services in 1994.
    start_year = 1995

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    BAKRI_ID_DATES = {
        2023: (JUN, 29),
        2024: (JUN, 17),
    }

    CHRISTMAS_DAY_DATES = {
        2023: (DEC, 25),
        2024: (DEC, 25),
        2025: (DEC, 25),
    }

    DIWALI_BALIPRATIPADA_DATES = {
        2023: (NOV, 14),
        2025: (OCT, 22),
    }

    DIWALI_LAXMI_PUJAN_DATES = {
        2024: (NOV, 1),
        2025: (OCT, 21),
    }

    DUSSEHRA_DATES = {
        2023: (OCT, 24),
        2024: (OCT, 12),
        2025: (OCT, 2),
    }

    DR_BABA_SAHEB_AMBEDKAR_JAYANTI_DATES = {
        2023: (APR, 14),
        2025: (APR, 14),
    }

    GANESH_CHATURTHI_DATES = {
        2023: (SEP, 19),
        2025: (AUG, 27),
    }

    GOOD_FRIDAY_DATES = {
        2023: (APR, 7),
        2024: (MAR, 29),
        2025: (APR, 18),
    }

    GURU_NANAK_JAYANTI_DATES = {
        2023: (NOV, 27),
        2024: (NOV, 15),
        2025: (NOV, 5),
    }

    HOLI_DATES = {
        2023: (MAR, 8),
        2024: (MAR, 25),
        2025: (MAR, 14),
    }

    ID_UL_FITR_DATES = {
        2024: (APR, 11),
        2025: (MAR, 31),
    }

    INDEPENDENCE_DAY_DATES = {
        2023: (AUG, 15),
        2024: (AUG, 15),
        2025: (AUG, 15),
    }

    MAHARASHTRA_DAY_DATES = {
        2023: (MAY, 1),
        2024: (MAY, 1),
        2025: (MAY, 1),
    }

    MAHA_SHIVARATRI_DATES = {
        2024: (MAR, 8),
        2025: (FEB, 26),
    }

    MAHATMA_GANDHI_JAYANTI_DATES = {
        2023: (OCT, 2),
        2024: (OCT, 2),
        2025: (OCT, 2),
    }

    MAHAVIR_JAYANTI_DATES = {
        2023: (APR, 4),
        2025: (APR, 10),
    }

    MUHARRAM_DATES = {
        2023: (JUL, 29),
    }

    RAM_NAVAMI_DATES = {
        2023: (MAR, 30),
        2024: (APR, 17),
    }

    REPUBLIC_DAY_DATES = {
        2023: (JAN, 26),
        2024: (JAN, 26),
        2025: (JAN, 26),
    }

    def _populate_public_holidays(self):
        # No fixed annual closures that apply every year on the same date.

        # Bakri Id
        self._get_holiday(tr("Bakri Id"), BAKRI_ID, self._year)

        # Christmas Day
        self._get_holiday(tr("Christmas Day"), CHRISTMAS_DAY, self._year)

        # Diwali Balipratipada
        self._get_holiday(tr("Diwali Balipratipada"), DIWALI_BALIPRATIPADA, self._year)

        # Diwali Laxmi Pujan
        self._get_holiday(tr("Diwali Laxmi Pujan"), DIWALI_LAXMI_PUJAN, self._year)

        # Dussehra
        self._get_holiday(tr("Dussehra"), DUSSEHRA, self._year)

        # Dr. Baba Saheb Ambedkar Jayanti
        self._get_holiday(
            tr("Dr. Baba Saheb Ambedkar Jayanti"), DR_BABA_SAHEB_AMBEDKAR_JAYANTI, self._year
        )

        # Ganesh Chaturthi
        self._get_holiday(tr("Ganesh Chaturthi"), GANESH_CHATURTHI, self._year)

        # Good Friday
        self._get_holiday(tr("Good Friday"), GOOD_FRIDAY, self._year)

        # Guru Nanak Jayanti
        self._get_holiday(tr("Guru Nanak Jayanti"), GURU_NANAK_JAYANTI, self._year)

        # Holi
        self._get_holiday(tr("Holi"), HOLI, self._year)

        # Id Ul Fitr (Ramadan Eid)
        self._get_holiday(tr("Id-Ul-Fitr (Ramadan Eid)"), ID_UL_FITR, self._year)

        # Independence Day
        self._get_holiday(tr("Independence Day"), INDEPENDENCE_DAY, self._year)

        # Maharashtra Day
        self._get_holiday(tr("Maharashtra Day"), MAHARASHTRA_DAY, self._year)

        # Maha Shivaratri
        self._get_holiday(tr("Maha Shivaratri"), MAHA_SHIVARATRI, self._year)

        # Mahatma Gandhi Jayanti
        self._get_holiday(tr("Mahatma Gandhi Jayanti"), MAHATMA_GANDHI_JAYANTI, self._year)

        # Mahavir Jayanti
        self._get_holiday(tr("Mahavir Jayanti"), MAHAVIR_JAYANTI, self._year)

        # Muharram
        self._get_holiday(tr("Muharram"), MUHARRAM, self._year)

        # Ram Navami
        self._get_holiday(tr("Ram Navami"), RAM_NAVAMI, self._year)

        # Republic Day
        self._get_holiday(tr("Republic Day"), REPUBLIC_DAY, self._year)

    def _get_holiday(self, name, holiday: str, year: int) -> Optional[date]:
        exact_date = getattr(self, f"{holiday}_DATES", {})
        dt = exact_date.get(year)
        return self._add_holiday(tr(name), date(year, *dt)) if dt else None


class NSE(NationalStockExchangeOfIndia):
    """Alias of NationalStockExchangeOfIndia"""

    pass


class XNSE(NationalStockExchangeOfIndia):
    """Alias of NationalStockExchangeOfIndia"""

    pass
