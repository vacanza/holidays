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

from holidays.groups import InternationalHolidays, MongolianCalendarHolidays
from holidays.holiday_base import HolidayBase


class Mongolia(HolidayBase, InternationalHolidays, MongolianCalendarHolidays):
    """Mongolia holidays.

    References:
        * [Law on Public holidays and days of observation](https://web.archive.org/web/20250327062440/https://legalinfo.mn/mn/detail/399)
        * [Labor Law](https://web.archive.org/web/20250421093230/https://legalinfo.mn/mn/detail?lawId=16230709635751)
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Mongolia>
        * [Mongolian lunar calendar](https://web.archive.org/web/20230412171012/https://www.math.mcgill.ca/gantumur/cal/index_mn.html)
        * <https://www.timeanddate.com/holidays/mongolia>
        * <https://investmongolia.gov.mn/mongolia-at-a-glance/>
    """

    country = "MN"
    default_language = "mn"
    start_year = 2004
    supported_languages = ("en_US", "mn")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        MongolianCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Шинэ жилийн баяр"))

        # Tsagaan Sar.
        self._add_tsagaan_sar(tr("Цагаан сар"))

        # Tsagaan Sar Holiday.
        name = tr("Цагаан сарын баяр")
        self._add_tsagaan_sar_day_2(name)
        self._add_tsagaan_sar_day_3(name)

        # International Women's Day.
        self._add_womens_day(tr("Олон улсын эмэгтэйчүүдийн өдөр"))

        # Children's Day.
        self._add_childrens_day(tr("Хүүхдийн баяр"))

        # The Buddha's Birthday.
        self._add_buddha_day(tr("Бурхан багшийн Их дүйчин өдөр"))

        # Naadam.
        self._add_holiday_jul_11(tr("Наадам"))

        # Naadam Holiday.
        name = tr("Наадмын баяр")
        self._add_holiday_jul_12(name)
        self._add_holiday_jul_13(name)
        self._add_holiday_jul_14(name)
        self._add_holiday_jul_15(name)

        # Established on November 8th, 2012.
        if self._year >= 2012:
            # The Birthday of the great emperor Genghis Khan.
            self._add_genghis_khan_day(tr("Их Эзэн Чингис хааны өдөр"))

        # Established on November 8th, 2012.
        if self._year >= 2012:
            # Republic Day.
            self._add_holiday_nov_26(tr("Бүгд Найрамдах Улс тунхагласан өдөр"))

        # Established on August 16th, 2007.
        # Renamed on December 23rd, 2011.
        if self._year >= 2007:
            self._add_holiday_dec_29(
                # Restoration of Freedom and Independence Day.
                tr("Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр")
                if self._year >= 2011
                # Independence Day.
                else tr("Үндэсний эрх чөлөөний өдөр")
            )


class MN(Mongolia):
    pass


class MNG(Mongolia):
    pass
