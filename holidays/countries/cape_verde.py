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

from holidays.constants import OPTIONAL, PUBLIC
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class CapeVerde(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Cape Verde holidays.

    References:
        * [Public holidays in Cape Verde] <https://en.wikipedia.org/wiki/Public_holidays_in_Cape_Verde>
        * [Today's and Upcoming Holidays in Tuvalu] <https://www.timeanddate.com/holidays/cape-verde/>
        * [Democracy Day] <https://www.officeholidays.com/holidays/cape-verde/cape-verde-democracy-day>
        * [National Heroes Day] <https://www.officeholidays.com/holidays/cape-verde/guinea-bissau-national-heroes-day>
    """

    country = "CV"
    default_language = "pt_PT"
    supported_languages = ("en_US", "pt_PT", "uk")
    supported_categories = (OPTIONAL, PUBLIC)
    start_year = 1973

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Ano Novo"))

        # Labour Day.
        self._add_labor_day(tr("Dia do Trabalhador"))

        # Assumption of Mary.
        self._add_assumption_of_mary_day(tr("Dia da Assunção"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Dia de Todos os Santos"))

        # Christmas Day.
        self._add_christmas_day(tr("Natal"))

        if self._year >= 1991:
            # Democracy Day.
            self._add_holiday_jan_13(tr("Dia da Liberdade e Democracia"))

        if self._year >= 1975:
            # Independence Day (From Portugal 1975)
            self._add_holiday_jul_5(tr("Dia da Independência Nacional"))

        # Heroes Day.
        self._add_holiday_jan_20(tr("Dia da Nacionalidade e dos Heróis Nacionais"))

        # Youth Day
        self._add_holiday_jun_1(tr("Dia Mundial da Criança"))

        # Good Friday.
        self._add_good_friday(tr("Sexta-feira Santa"))

    def _populate_optional_holidays(self):
        # March Equinox.
        self._add_holiday_mar_20(tr("Equinócio de Março"))

        # June Solstice
        self._add_holiday_jun_21(tr("Solstício de Junho"))

        # September Equinox
        self._add_holiday_sep_22(tr("Equinócio de Setembro"))

        # Winter Solstice.
        self._add_holiday_dec_21(tr("Solstício de Inverno"))

        # Ash Wednesday.
        self._add_ash_wednesday(tr("Dia das Cinzas"))

        # Holy Thursday.
        self._add_holy_thursday(tr("Quinta-Feira Santa"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Páscoa"))

        # Mother's Day.
        self._add_holiday_2nd_sun_of_may(tr("Dia das Mães"))


class CV(CapeVerde):
    pass


class CAV(CapeVerde):
    pass
