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

from holidays.constants import PUBLIC
from holidays.groups import TibetanCalendarHolidays
from holidays.holiday_base import HolidayBase


class Bhutan(HolidayBase, TibetanCalendarHolidays):
    """Bhutan holidays.

    References:
        * <https://www.wipo.int/wipolex/en/legislation/details/16762>
        * <https://www.bhutan.travel/travel-guide/bhutanese-holidays-and-festivals>
    """

    country = "BT"
    supported_categories = (PUBLIC,)
    default_language = "dz_BT"
    supported_languages = ("dz_BT", "en_US")
    start_year = 1970

    def __init__(self, *args, **kwargs):
        TibetanCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Nyilo.
        self._add_holiday_jan_2(tr("ཉི་ལོག་"))

        # King's Birthday (Day 1).
        self._add_holiday_feb_21(tr("རྒྱལ་པོའི་འཁྲུངས་སྐར།༼ཉིན༡༽།"))

        # King's Birthday (Day 2).
        self._add_holiday_feb_22(tr("རྒྱལ་པོའི་འཁྲུངས་སྐར།༼ཉིནམ་གཉིས་པ།༽"))

        # King's Birthday (Day 3).
        self._add_holiday_feb_23(tr("རྒྱལ་པོའི་འཁྲུངས་སྐར།༼ཉིན་གསུམ་པ།༽"))

        # Birth Anniversary of Third Druk Gyalpo.
        self._add_holiday_may_2(tr("གསུམ་པ་དབུ་མའི་འཁྲུངས་སྐར་དུས་ཆེན།"))

        # Jigme Khesar Namgyel's Coronation
        self._add_holiday_nov_1(tr("རྒྱལ་པོ་འཇིགས་མེད་ཁེ་སར་རྣམ་རྒྱལ།ཀོ་རོ་ན་ཤི་ཡ།"))

        # Birth Anniversary of the Fourth Druk Gyalpo.
        self._add_holiday_nov_11(tr("དྲུག་རྒྱལ་བཞི་པའི་འཁྲུངས་སྐར་དུས་ཆེན།"))

        # National Day.
        self._add_holiday_dec_17(tr("རྒྱལ་ཡོངས་དུས་ཆེན།"))

        # Day of Offering.
        self._add_day_of_offering(tr("བུ་ལྭ་ཕེུ་ཝི་ཉིམ"))

        # Blessed Rainy Day.
        self._add_blessed_rainy_day(tr("ཁྲུས་འབབས་ཀྱི་ཉིནམ།"))

        # Losar.
        self._add_losar(tr("ལལོ་གསར་"))

        # Buddha Parinirvana.
        self._add_buddha_parinirvana(tr("།སངས་རྒྱས་པ་རི་ནིར་ཝན།"))

        # Buddha's First Sermon.
        self._add_buddha_first_sermon(tr("སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་གསུང་ཆོས་དང་པོ།"))

        # Birth of Guru Rinpoche.
        self._add_birth_of_guru_rinpoche(tr("སྐྱབས་རྗེ་གུ་རུ་རིན་པོ་ཆེའི་འཁྲུངས་སྐར།"))

        # Death of Zhabdrung.
        self._add_death_of_zhabdrung(tr("ཞབས་དྲུང་གི་འདས་དུས།"))

        # Dashain.
        self._add_dashain(tr("དྲང་བའི་བདུད་རྩིའི་ཉིམ།"))


class BT(Bhutan):
    pass


class BTN(Bhutan):
    pass
