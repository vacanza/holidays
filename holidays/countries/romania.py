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

from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class Romania(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Romania holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Romania>
        * [Law No. 75 of Jul 12, 1996](https://web.archive.org/web/20260120033731/https://legislatie.just.ro/Public/DetaliiDocumentAfis/8417)
        * [Labor Code 2003](https://web.archive.org/web/20260309153044/https://legislatie.just.ro/Public/DetaliiDocumentAfis/304539)
        * [Law No. 202 of Oct 21, 2008](https://web.archive.org/web/20251207215906/https://legislatie.just.ro/Public/DetaliiDocumentAfis/98527)
        * [Law No. 147 of Jul 23, 2012](https://web.archive.org/web/20251007033324/https://legislatie.just.ro/Public/DetaliiDocumentAfis/139884)
        * [Law No. 176 of Oct 7, 2016](https://web.archive.org/web/20251011075049/https://legislatie.just.ro/Public/DetaliiDocumentAfis/182520)
        * [Law No. 220 of Nov 17, 2016](https://web.archive.org/web/20251117213440/https://legislatie.just.ro/Public/DetaliiDocumentAfis/183741)
        * [Law No. 64 of Mar 12, 2018](https://web.archive.org/web/20251018174920/https://legislatie.just.ro/Public/DetaliiDocumentAfis/198708)
        * [Law No. 52 of Mar 3, 2023](https://web.archive.org/web/20251205085234/https://legislatie.just.ro/Public/DetaliiDocumentAfis/265498)
    """

    country = "RO"
    default_language = "ro"
    # Law No. 75 of Jul 12, 1996.
    start_year = 1997
    supported_languages = ("en_US", "ro", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self, JULIAN_REVISED_CALENDAR)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        name = tr("Anul Nou")
        self._add_new_years_day(name)
        self._add_new_years_day_two(name)

        # Established by Law No. 52 of Mar 3, 2023.
        if self._year >= 2024:
            # Epiphany.
            self._add_epiphany_day(tr("Botezul Domnului - Boboteaza"))

            # Saint John the Baptist.
            self._add_holiday_jan_7(tr("Soborul Sfântului Proroc Ioan Botezătorul"))

        # Established by Law No. 176 of Oct 7, 2016.
        if self._year >= 2017:
            # Unification of the Romanian Principalities Day.
            self._add_holiday_jan_24(tr("Ziua Unirii Principatelor Române"))

        # Established by Law No. 64 of Mar 12, 2018.
        if self._year >= 2018:
            # Good Friday.
            self._add_good_friday(tr("Vinerea Mare"))

        # Easter.
        name = tr("Paștele")
        self._add_easter_sunday(name)
        self._add_easter_monday(name)

        # Labor Day.
        self._add_labor_day(tr("Ziua Muncii"))

        # Established by Law No. 220 of Nov 17, 2016.
        if self._year >= 2017:
            # Children's Day.
            self._add_childrens_day(tr("Ziua Copilului"))

        # Established by Law No. 202 of Oct 21, 2008.
        if self._year >= 2009:
            # Pentecost.
            name = tr("Rusaliile")
            self._add_whit_sunday(name)
            self._add_whit_monday(name)

            # Dormition of the Mother of God.
            self._add_assumption_of_mary_day(tr("Adormirea Maicii Domnului"))

        # Established by Law No. 147 of Jul 23, 2012.
        if self._year >= 2012:
            self._add_holiday_nov_30(
                # Saint Andrew's Day.
                tr("Sfântul Apostol Andrei, cel Întâi chemat, Ocrotitorul României")
            )

        # National Day.
        self._add_holiday_dec_1(tr("Ziua Națională a României"))

        # Christmas Day.
        name = tr("Crăciunul")
        self._add_christmas_day(name)
        self._add_christmas_day_two(name)


class RO(Romania):
    pass


class ROU(Romania):
    pass
