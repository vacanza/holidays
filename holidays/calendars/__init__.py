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

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Static analysis only. Runtime names are loaded lazily below.
    from holidays.calendars.balinese_saka import _BalineseSakaLunar
    from holidays.calendars.buddhist import _BuddhistLunisolar, _CustomBuddhistHolidays
    from holidays.calendars.burmese import _BurmeseLunisolar
    from holidays.calendars.chinese import _ChineseLunisolar, _CustomChineseHolidays
    from holidays.calendars.custom import _CustomCalendar
    from holidays.calendars.gregorian import GREGORIAN_CALENDAR
    from holidays.calendars.hebrew import _HebrewLunisolar
    from holidays.calendars.hindu import _CustomHinduHolidays, _HinduLunisolar
    from holidays.calendars.islamic import (
        _CustomIslamicHolidays,
        _CustomIslamicMabimsHolidays,
        _IslamicLunar,
        _IslamicMabimsLunar,
    )
    from holidays.calendars.julian import JULIAN_CALENDAR
    from holidays.calendars.julian_revised import JULIAN_REVISED_CALENDAR
    from holidays.calendars.mongolian import _CustomMongolianHolidays, _MongolianLunisolar
    from holidays.calendars.persian import _Persian
    from holidays.calendars.sinhala import _SinhalaLunar, _CustomSinhalaHolidays
    from holidays.calendars.thai import _ThaiLunisolar, KHMER_CALENDAR, THAI_CALENDAR
    from holidays.calendars.tibetan import _TibetanLunisolar, _CustomTibetanHolidays
else:
    from holidays.helpers import _load_lazily

    _load_lazily(
        globals(),
        {
            "balinese_saka": ("_BalineseSakaLunar",),
            "buddhist": ("_BuddhistLunisolar", "_CustomBuddhistHolidays"),
            "burmese": ("_BurmeseLunisolar",),
            "chinese": ("_ChineseLunisolar", "_CustomChineseHolidays"),
            "custom": ("_CustomCalendar",),
            "gregorian": ("GREGORIAN_CALENDAR",),
            "hebrew": ("_HebrewLunisolar",),
            "hindu": ("_CustomHinduHolidays", "_HinduLunisolar"),
            "islamic": (
                "_CustomIslamicHolidays",
                "_CustomIslamicMabimsHolidays",
                "_IslamicLunar",
                "_IslamicMabimsLunar",
            ),
            "julian": ("JULIAN_CALENDAR",),
            "julian_revised": ("JULIAN_REVISED_CALENDAR",),
            "mongolian": ("_CustomMongolianHolidays", "_MongolianLunisolar"),
            "persian": ("_Persian",),
            "sinhala": ("_SinhalaLunar", "_CustomSinhalaHolidays"),
            "thai": ("_ThaiLunisolar", "KHMER_CALENDAR", "THAI_CALENDAR"),
            "tibetan": ("_TibetanLunisolar", "_CustomTibetanHolidays"),
        },
    )
    del _load_lazily
