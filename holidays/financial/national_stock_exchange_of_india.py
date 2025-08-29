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

from gettext import gettext as tr

from holidays.calendars import _CustomHinduHolidays, _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG
from holidays.groups import ChristianHolidays, HinduCalendarHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_NONE, SUN_TO_NONE


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
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    supported_languages = ("en_IN", "en_US", "hi")
    start_year = 2001

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        HinduCalendarHolidays.__init__(self, cls=NationalStockExchangeOfIndiaHinduHolidays)
        IslamicHolidays.__init__(
            self,
            cls=NationalStockExchangeOfIndiaIslamicHolidays,
            show_estimated=islamic_show_estimated,
        )
        kwargs.setdefault("observed_rule", SAT_TO_NONE + SUN_TO_NONE)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Republic Day.
        self._move_holiday(self._add_holiday_jan_26(tr("Republic Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

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

        # Hindu Calendar Holidays.

        # Maha Shivaratri.
        self._move_holiday(self._add_maha_shivaratri(tr("Maha Shivaratri")))

        # Holi.
        self._move_holiday(self._add_holi(tr("Holi")))

        # Ram Navami.
        self._move_holiday(self._add_ram_navami(tr("Ram Navami")))

        # Mahavir Jayanti.
        self._move_holiday(self._add_mahavir_jayanti(tr("Mahavir Jayanti")))

        # Ganesh Chaturthi.
        self._move_holiday(self._add_ganesh_chaturthi(tr("Ganesh Chaturthi")))

        # Dussehra.
        self._move_holiday(self._add_dussehra(tr("Dussehra")))

        # Diwali Laxmi Pujan.
        self._move_holiday(self._add_gau_krida(tr("Diwali Laxmi Pujan")))

        # Diwali Balipratipada.
        name = tr("Diwali Balipratipada")
        # NSE's calendar adds an extra-day gap in 2022–2023
        # between Diwali Laxmi Pujan and Diwali Balipratipada.
        self._move_holiday(
            self._add_bhai_dooj(name)
            if self._year in {2022, 2023}
            else self._add_govardhan_puja(name)
        )

        # Guru Nanak Jayanti.
        self._move_holiday(self._add_guru_nanak_jayanti(tr("Guru Nanak Jayanti")))

        # Islamic Calendar Holidays.

        # Ashura.
        for dt in self._add_ashura_day(tr("Muharram")):
            self._move_holiday(dt)

        # Eid al-Fitr.
        for dt in self._add_eid_al_fitr_day(tr("Id-Ul-Fitr (Ramadan Eid)")):
            self._move_holiday(dt)

        # Eid al-Adha.
        for dt in self._add_eid_al_adha_day(tr("Bakri Id")):
            self._move_holiday(dt)


class XNSE(NationalStockExchangeOfIndia):
    pass


class NSE(NationalStockExchangeOfIndia):
    pass


class NationalStockExchangeOfIndiaHinduHolidays(_CustomHinduHolidays):
    HOLI_DATES = {
        2023: (MAR, 7),
    }


class NationalStockExchangeOfIndiaIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES_CONFIRMED_YEARS = (2022, 2025)
    ASHURA_DATES = {
        2022: (AUG, 9),
        2023: (JUL, 29),
        2024: (JUL, 17),
        2025: (JUL, 6),
    }

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2022, 2025)
    EID_AL_ADHA_DATES = {
        2022: (JUL, 10),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2022, 2025)
    EID_AL_FITR_DATES = {
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 11),
        2025: (MAR, 31),
    }
