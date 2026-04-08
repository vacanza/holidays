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

from holidays.calendars import _CustomHinduHolidays
from holidays.calendars.gregorian import SEP, OCT
from holidays.groups import HinduCalendarHolidays, TibetanCalendarHolidays
from holidays.holiday_base import HolidayBase


class Bhutan(HolidayBase, HinduCalendarHolidays, TibetanCalendarHolidays):
    """Bhutan holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Bhutan>
        * [The Bhutanese calendar](https://web.archive.org/web/20250707105447/http://www.kalacakra.org/calendar/bhutlist.htm)
        * [2007-2011](https://web.archive.org/web/20070730055559/http://www.rcsc.gov.bt/tmpFolder/CalendarOfEvent/holiday.htm)
        * [2010-2011](https://web.archive.org/web/20100127021618/http://www.mohca.gov.bt/?mode=READMORE&news_id=157)
        * [2014](https://web.archive.org/web/20141222122050/http://www.mohca.gov.bt/Publications/calander_2014-15.pdf)
        * [2015](https://web.archive.org/web/20151004161522/http://www.mohca.gov.bt/Publications/calander_2015-16.pdf)
        * [2016](https://web.archive.org/web/20170606131500/http://www.mohca.gov.bt/download/calander_2016-17.pdf)
        * [2017](https://web.archive.org/web/20180107115733/http://www.mohca.gov.bt/wp-content/uploads/2017/11/calander_2017-18.pdf)
        * [2018](https://web.archive.org/web/20180906031327/http://www.mohca.gov.bt/wp-content/uploads/2017/11/scan0126.pdf)
        * [2019](https://web.archive.org/web/20191221201614/http://www.mohca.gov.bt/downloads/scan0004.pdf)
        * [2020](https://web.archive.org/web/20200720030220/http://www.mohca.gov.bt/wp-content/uploads/2019/12/2020-Holiday-List0001.pdf)
        * [2021](https://web.archive.org/web/20230511011459/http://www.mohca.gov.bt/downloads/Holidays2021.pdf)
        * [2022](https://web.archive.org/web/20220619061040/https://www.mohca.gov.bt/wp-content/uploads/2021/11/HolidayList.pdf)
        * [2023](https://web.archive.org/web/20221210152039/https://www.mohca.gov.bt/wp-content/uploads/2022/11/Holidays-2023.pdf)
        * [2024](https://web.archive.org/web/20250407140158/https://www.moha.gov.bt/wp-content/uploads/2023/11/National-Holiday-List-for-2024-2-.pdf)
        * [2025](https://web.archive.org/web/20250703030226/https://www.moha.gov.bt/wp-content/uploads/2024/11/Calendar_2025.pdf)
    """

    country = "BT"
    default_language = "dz"
    # %s (estimated).
    estimated_label = tr("%s (ཚོད་དཔག་གི།)")
    supported_languages = ("dz", "en_US")
    # Jigme Khesar Namgyel Wangchuck ascended to the throne on December 9th, 2006.
    start_year = 2007
    subdivisions = (
        "11",  # Paro.
        "12",  # Chhukha.
        "13",  # Haa.
        "14",  # Samtse.
        "15",  # Thimphu.
        "21",  # Tsirang.
        "22",  # Dagana.
        "23",  # Punakha.
        "24",  # Wangdue Phodrang.
        "31",  # Sarpang.
        "32",  # Trongsa.
        "33",  # Bumthang.
        "34",  # Zhemgang.
        "41",  # Trashigang.
        "42",  # Monggar.
        "43",  # Pema Gatshel.
        "44",  # Lhuentse.
        "45",  # Samdrup Jongkhar.
        "GA",  # Gasa.
        "TY",  # Trashi Yangtse.
    )

    subdivisions_aliases = {
        "Paro": "11",
        "Chhukha": "12",
        "Haa": "13",
        "Samtse": "14",
        "Thimphu": "15",
        "Tsirang": "21",
        "Dagana": "22",
        "Punakha": "23",
        "Wangdue Phodrang": "24",
        "Sarpang": "31",
        "Trongsa": "32",
        "Bumthang": "33",
        "Zhemgang": "34",
        "Trashigang": "41",
        "Monggar": "42",
        "Pema Gatshel": "43",
        "Lhuentse": "44",
        "Samdrup Jongkhar": "45",
        "Gasa": "GA",
        "Trashi Yangtse": "TY",
    }

    def __init__(self, *args, hindu_show_estimated: bool = True, **kwargs):
        """
        Args:
            hindu_show_estimated:
                Whether to add "estimated" label to Hindu holidays name
                if holiday date is estimated.
        """
        HinduCalendarHolidays.__init__(
            self, cls=BhutanHinduHolidays, show_estimated=hindu_show_estimated
        )
        TibetanCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Birth Anniversary of His Majesty the King.
        name = tr("མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།")
        self._add_holiday_feb_21(name)
        self._add_holiday_feb_22(name)
        self._add_holiday_feb_23(name)

        # Birth Anniversary of the 3rd Druk Gyalpo.
        self._add_holiday_may_2(tr("མི་དབང་འབྲུག་རྒྱལ་གསུམ་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"))

        # Coronation of His Majesty the King.
        self._add_holiday_nov_1(tr("མི་དབང་མངའ་བདག་རིན་པོ་ཆེའི་གསེར་ཁྲི་མངའ་གསོལ་གྱི་དུས་ཆེན་ངལ་གསོལ།"))

        # Birth Anniversary of the 4th Druk Gyalpo - Constitution Day.
        self._add_holiday_nov_11(tr("མི་དབང་འབྲུག་རྒྱལ་བཞི་པའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོལ།"))

        # National Day.
        self._add_holiday_dec_17(tr("རྒྱལ་ཡོངས་དུས་ཆེན་གྱི་ངལ་གསོལ།"))

        # Winter Solstice.
        self._add_tibetan_winter_solstice(tr("དགུན་ཉི་ལྡོག་གི་ངལ་གསོལ།"))

        # Traditional Day of Offering.
        self._add_day_of_offering(tr("སྔར་སྲོལ་འབུལ་བའི་ལོ་གསར་གྱི་ངལ་གསོལ།"))

        # Losar.
        name = tr("གནམ་ལོ་གསར་ཚེས་ཀྱིས་དུས་སྟོན་ངལ་གསོལ།")
        self._add_losar(name)
        self._add_losar_day_two(name)

        # Death Anniversary of Zhabdrung.
        self._add_death_of_zhabdrung(tr("མཐུ་ཆེན་ཆོས་ཀྱི་རྒྱལ་པོའི་དུས་ཆེན་ངལ་གསོལ།"))

        # Lord Buddha's Parinirvana.
        self._add_buddha_parinirvana(tr("སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་དུས་ཆེན་ལྔ་འཛོམས་ངལ་གསོལ།"))

        # Birth Anniversary of Guru Rinpoche.
        self._add_birth_of_guru_rinpoche(tr("ཨོ་རྒྱན་གུ་རུ་རིན་པོ་ཆེའི་འཁྲུངས་སྐར་དུས་ཆེན་ངལ་གསོ།"))

        # First Sermon of Lord Buddha.
        self._add_buddha_first_sermon(tr("སྟོན་པ་མཆོག་ཝ་ར་ན་སིར་བདེན་བཞིའི་ཆོས་འཁོར་བསྐོར་བའི་དུས་ཆེན་ངལ་གསོ།"))

        # Blessed Rainy Day.
        self._add_blessed_rainy_day(tr("རྒྱལ་ཡོངས་ཁྲུས་བབས་ངལ་གསོ།"))

        # Dassain.
        self._add_dussehra(tr("ལྷོ་མཚམས་ད་སའིན་ངལ་གསོ།"))

        # Descending Day of Lord Buddha.
        self._add_descending_day_of_lord_buddha(tr("རྒྱལ་བ་ལྷ་ལས་བབས་པའི་དུས་ཆེན་ངལ་གསོ།"))

    def _populate_subdiv_15_public_holidays(self):
        # Thimphu Drubchoe.
        self._add_thimphu_drubchen_day(tr("ཐིམ་རྫོང་ལྷ་མོའི་དངོས་འཆམ་མཇལ་རྒྱུའི་ངལ་གསོ།"))

        # Thimphu Tshechu.
        name = tr("ཐིམ་ཕུ་ཚེས་བཅུའི་ངལ་གསོ།")
        self._add_thimphu_tshechu_day(name)
        self._add_thimphu_tshechu_day_two(name)
        self._add_thimphu_tshechu_day_three(name)


class BT(Bhutan):
    pass


class BTN(Bhutan):
    pass


class BhutanHinduHolidays(_CustomHinduHolidays):
    DUSSEHRA_DATES = {
        2007: (OCT, 21),
        2008: (OCT, 9),
        2009: (SEP, 28),
        2010: (OCT, 17),
        2011: (OCT, 6),
        2014: (OCT, 3),
        2015: (OCT, 22),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (OCT, 19),
        2019: (OCT, 8),
        2020: (OCT, 26),
        2021: (OCT, 15),
        2022: (OCT, 5),
        2023: (OCT, 24),
        2024: (OCT, 12),
        2025: (OCT, 2),
    }
