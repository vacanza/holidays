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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Pakistan(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Pakistan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Pakistan>
        * <https://ur.wikipedia.org/wiki/تعطیلات_پاکستان>
    """
    country = "PK"
    default_language = "en_PK"
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    start_year = 1948
    supported_languages = ("en_PK", "en_US", "ur_PK")

    subdivisions = {
    "PB": "Punjab",
    "SD": "Sindh",
    "KP": "Khyber Pakhtunkhwa",
    "BA": "Balochistan",
    "GB": "Gilgit-Baltistan",
    "AJK": "Azad Jammu & Kashmir",
    "ICT": "Islamabad Capital Territory",
    }
    
    
    def __init__(self, islamic_show_estimated: bool = True, *args, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=PakistanIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year >= 1990:
            # Kashmir Solidarity Day.
            self._add_holiday_feb_5(tr("Kashmir Solidarity Day"))

        if self._year >= 1956:
            # Pakistan Day.
            self._add_holiday_mar_23(tr("Pakistan Day"))

        if self._year >= 1972:
            # Labor Day.
            self._add_labor_day(tr("Labour Day"))

        # Independence Day.
        self._add_holiday_aug_14(tr("Independence Day"))

        if self._year <= 2014 or self._year >= 2022:
            # Iqbal Day.
            self._add_holiday_nov_9(tr("Iqbal Day"))

        # Quaid-e-Azam Day.
        self._add_holiday_dec_25(tr("Quaid-e-Azam Day"))

        # Eid al-Fitr.
        name = tr("Eid-ul-Fitr")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)
        self._add_eid_al_fitr_day_three(name)

        # Eid al-Adha.
        name = tr("Eid-ul-Adha")
        self._add_eid_al_adha_day(name)
        self._add_eid_al_adha_day_two(name)
        self._add_eid_al_adha_day_three(name)

        # Prophet's Birthday.
        self._add_mawlid_day(tr("Eid Milad-un-Nabi"))

        # Ashura.
        name = tr("Ashura")
        self._add_ashura_eve(name)
        self._add_ashura_day(name)

        self._populate_subdiv_holidays()

    def _populate_subdiv_holidays(self):
        # Adding province/city-specific holidays based on self.subdiv

        
        # Ensure self.subdiv is not None before checking specific values
        if not self.subdiv:
            return  # No subdivisions selected, so no need to add local holidays

        if self.subdiv == "PB":  # Punjab
            self._add_holiday_mar_29(tr("Mela Chiraghan"))  # Lahore Only

        if self.subdiv == "SD":  # Sindh
            self._add_holiday_dec_27(tr("Benazir Bhutto's Martyrdom Day"))

class PK(Pakistan):
    pass


class PAK(Pakistan):
    pass


class PakistanIslamicHolidays(_CustomIslamicHolidays):
    # https://www.timeanddate.com/holidays/pakistan/first-day-ashura

    ASHURA_DATES = {
        2005: (FEB, 18),
        2006: (FEB, 8),
        2007: (JAN, 28),
        2008: (JAN, 18),
        2009: ((JAN, 6), (DEC, 26)),
        2010: (DEC, 16),
        2011: (DEC, 5),
        2012: (NOV, 23),
        2013: (NOV, 13),
        2014: (NOV, 3),
        2015: (OCT, 23),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (SEP, 21),
        2019: (SEP, 9),
        2020: (AUG, 29),
        2021: (AUG, 18),
        2022: (AUG, 9),
        2023: (JUL, 28),
        2024: (JUL, 16),
    }

    # https://www.timeanddate.com/holidays/pakistan/eid-ul-azha
    EID_AL_ADHA_DATES = {
        2005: (JAN, 21),
        2006: ((JAN, 10), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 6),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }

    # https://www.timeanddate.com/holidays/pakistan/eid-ul-fitr-1
    EID_AL_FITR_DATES = {
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 2),
        2009: (SEP, 21),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 29),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 26),
        2018: (JUN, 16),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
    }

    # https://www.timeanddate.com/holidays/pakistan/eid-milad-un-nabi
    MAWLID_DATES = {
        2005: (APR, 22),
        2006: (APR, 11),
        2007: (MAR, 31),
        2008: (MAR, 21),
        2009: (MAR, 9),
        2010: (MAR, 1),
        2011: (FEB, 17),
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: (JAN, 4),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 21),
        2019: (NOV, 10),
        2020: (OCT, 30),
        2021: (OCT, 19),
        2022: (OCT, 9),
        2023: (SEP, 29),
        2024: (SEP, 17),
    }
