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
from holidays.calendars.gregorian import DEC, FEB, JAN, MAR, APR, MAY, JUN, JUL, AUG, NOV, OCT, SEP
from holidays.groups import ChristianHolidays, HinduCalendarHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase, SAT_TO_NONE, SUN_TO_NONE


class NationalStockExchangeOfIndia(
    ObservedHolidayBase, HinduCalendarHolidays, ChristianHolidays, IslamicHolidays
):
    """National Stock Exchange of India (NSE) holidays.

    References:
        * <https://web.archive.org/web/20250821175252/https://www.nseindia.com/resources/exchange-communication-circulars>

    Historical data:
        * [2001](https://nsearchives.nseindia.com/content/circulars/cmtr2189.wri)
        * [2002](https://nsearchives.nseindia.com/content/circulars/cmtr3058.wri)
        * [2003](https://nsearchives.nseindia.com/content/circulars/cmtr3809.htm)
        * [2004](https://nsearchives.nseindia.com/content/circulars/cmtr4645.htm)
        * [2005](https://nsearchives.nseindia.com/content/circulars/cmtr5633.htm)
        * [2006](https://nsearchives.nseindia.com/content/circulars/cmtr6946.htm)
        * [2007](https://nsearchives.nseindia.com/content/circulars/cmtr8182.htm)
        * [2008](https://nsearchives.nseindia.com/content/circulars/cmtr9909.htm)
        * [2009](https://nsearchives.nseindia.com/content/circulars/cmtr11733.htm)
        * [2010](https://nsearchives.nseindia.com/content/circulars/cmtr13713.pdf)
        * [2011](https://nsearchives.nseindia.com/content/circulars/cmtr16348.pdf)
        * [2012](https://nsearchives.nseindia.com/content/circulars/CMTR19539.pdf)
        * [2013](https://nsearchives.nseindia.com/content/circulars/CMTR22317.pdf)
        * [2014](https://nsearchives.nseindia.com/content/circulars/CMTR25326.pdf)
        * [2015](https://nsearchives.nseindia.com/content/circulars/CMTR28337.pdf)
        * [2016](https://nsearchives.nseindia.com/content/circulars/CMTR31297.pdf)
        * [2017](https://nsearchives.nseindia.com/content/circulars/CMTR33746.pdf)
        * [2018](https://nsearchives.nseindia.com/content/circulars/CMTR36475.pdf)
        * [2019](https://nsearchives.nseindia.com/content/circulars/CMTR39612.pdf)
        * [2020](https://nsearchives.nseindia.com/content/circulars/CMTR42877.pdf)
        * [2021](https://nsearchives.nseindia.com/content/circulars/CMTR46623.pdf)
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
        # New Year.
        if self._year in {2010}:
            self._move_holiday(self._add_holiday_jan_1(tr("New Year")))

        # Republic Day.
        self._move_holiday(self._add_holiday_jan_26(tr("Republic Day")))

        # Good Friday.
        self._add_good_friday(tr("Good Friday"))

        # Dr. Baba Saheb Ambedkar Jayanti.
        self._move_holiday(self._add_holiday_apr_14(tr("Dr. Baba Saheb Ambedkar Jayanti")))

        # Maharashtra Day or May Day.
        if self._year > 2009 and self._year < 2015:
            self._move_holiday(self._add_holiday_may_1(tr("May Day")))
        else:
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
            if self._year in {2001, 2002, 2020, 2022, 2023}
            else self._add_govardhan_puja(name)
        )

        # Guru Nanak Jayanti.
        self._move_holiday(self._add_guru_nanak_jayanti(tr("Guru Nanak Jayanti")))

        # Bhai Bhij.
        if self._year in {2006}:
            self._move_holiday(self._add_holiday_oct_24(tr("Bhai bhij")))
        if self._year > 2002 and self._year < 2010:
            self._move_holiday(self._add_bhai_dooj(tr("Bhai bhij")))

        # Buddha Purnima.
        if self._year in {2007, 2008}:
            self._move_holiday(self._add_buddha_purnima(tr("Buddha Purnima")))

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

        # Eid-E-Milad
        if self._year in {2008, 2009}:
            for dt in self._add_mawlid_day(tr("Id-E-Milad-Un-Nabi")):
                self._move_holiday(dt)


class XNSE(NationalStockExchangeOfIndia):
    pass


class NSE(NationalStockExchangeOfIndia):
    pass


class NationalStockExchangeOfIndiaHinduHolidays(_CustomHinduHolidays):
    HOLI_DATES = {
        2023: (MAR, 7),
    }

    DUSSEHRA_DATES = {
        2018: (OCT, 18),
    }

    MAHAVIR_JAYANTI_DATES = {
        2016: (APR, 19),
    }

    BUDDHA_PURNIMA_DATES = {
        2008: (MAY, 19),
    }

    RAM_NAVAMI_DATES = {
        2007: (MAR, 27),
    }

    GOVARDHAN_PUJA_DATES = {2006: (OCT, 21)}


class NationalStockExchangeOfIndiaIslamicHolidays(_CustomIslamicHolidays):
    ASHURA_DATES_CONFIRMED_YEARS = (2001, 2025)
    ASHURA_DATES = {
        2001: (APR, 5),
        2002: (MAR, 25),
        2004: (MAR, 2),
        2007: (JAN, 30),
        2009: ((JAN, 8), (DEC, 28)),
        2010: (DEC, 17),
        2011: (DEC, 6),
        2013: (NOV, 14),
        2014: (NOV, 4),
        2016: (OCT, 12),
        2019: (SEP, 10),
        2021: (AUG, 19),
        2022: (AUG, 9),
        2023: (JUL, 29),
        2024: (JUL, 17),
        2025: (JUL, 6),
    }

    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (2001, 2025)
    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2003: (FEB, 13),
        2004: (FEB, 2),
        2006: (JAN, 11),
        2007: ((JAN, 1), (DEC, 21)),
        2008: (DEC, 9),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2013: (OCT, 16),
        2014: (OCT, 6),
        2015: (SEP, 25),
        2016: (SEP, 13),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES_CONFIRMED_YEARS = (2001, 2025)
    EID_AL_FITR_DATES = {
        2001: (DEC, 17),
        2003: (NOV, 26),
        2004: (NOV, 15),
        2005: (NOV, 5),
        2006: (OCT, 25),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2011: (AUG, 31),
        2012: (AUG, 20),
        2013: (AUG, 9),
        2014: (JUL, 29),
        2017: (JUN, 26),
        2019: (JUN, 5),
        2020: (MAY, 25),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 11),
        2025: (MAR, 31),
    }

    MAWLID_DATES_CONFIRMED_YEARS = (2001, 2025)
    MAWLID_DATES = {
        2006: (APR, 11),
        2009: (MAR, 10),
    }
