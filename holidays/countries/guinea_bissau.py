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

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT
from holidays.groups import ChristianHolidays, InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class GuineaBissau(HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays):
    """Guinea-Bissau holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Guinea-Bissau>
    """

    country = "GW"
    default_language = "pt_GW"
    # %s (estimated).
    estimated_label = tr("%s (prevista)")
    # %s (observed).
    observed_label = tr("%s (ponte)")
    # %s (estimated, observed).
    observed_estimated_label = tr("%s (prevista, ponte)")
    supported_languages = ("en_US", "pt_GW")
    start_year = 1975

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=GuineaIslamicHolidays, show_estimated=islamic_show_estimated
        )
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Ano Novo"))

        # National Heroes' Day.
        self._add_holiday_jan_20(tr("Dia dos Heróis Nacionais"))

        # International Women's Day.
        self._add_womens_day(tr("Dia Internacional da Mulher"))

        # Good Friday.
        self._add_good_friday(tr("Sexta-feira Santa"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Páscoa"))

        # Labor Day.
        self._add_labor_day(tr("Dia do Trabalhador"))

        # Independence Day.
        self._add_holiday_sep_24(tr("Dia da Independência"))

        # All Souls' Day.
        self._add_all_souls_day(tr("Dia dos Finados"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Véspera de Natal"))

        # Christmas Day.
        self._add_christmas_day(tr("Dia de Natal"))

        # New Year's Eve.
        self._add_new_years_eve(tr("Véspera de Ano Novo"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Korité"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Tabaski"))


class GW(GuineaBissau):
    pass


class GNB(GuineaBissau):
    pass


class GuineaIslamicHolidays(_CustomIslamicHolidays):
    # https://www.timeanddate.com/holidays/guinea-bissau/eid-al-adha
    EID_AL_ADHA_DATES = {
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 13),
        2017: (SEP, 2),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 21),
        2022: (JUL, 9),
        2023: (JUN, 28),
        2024: (JUN, 16),
        2025: (JUN, 6),
    }

    # https://www.timeanddate.com/holidays/guinea-bissau/eid-al-fitr
    EID_AL_FITR_DATES = {
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 4),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 21),
        2024: (APR, 10),
        2025: (MAR, 30),
    }
