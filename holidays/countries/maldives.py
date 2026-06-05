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

from holidays.calendars.gregorian import FRI, SAT
from holidays.groups import InternationalHolidays, IslamicHolidays
from holidays.holiday_base import HolidayBase


class Maldives(HolidayBase, InternationalHolidays, IslamicHolidays):
    """Maldives holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_the_Maldives>
        * <https://web.archive.org/web/20250317114653/https://www.timeanddate.com/holidays/maldives>
        * <https://web.archive.org/web/20250427131834/https://www.mma.gov.mv/>
    """

    country = "MV"
    default_language = "dv"
    supported_languages = ("dv", "en_US")
    # %s (estimated).
    estimated_label = tr("%s (estimated)")
    weekend = {FRI, SAT}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, show_estimated=islamic_show_estimated)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("މީލާދީ އާ އަހަރު ފެށޭ ދުވަސް"))

        # Labor Day.
        self._add_labor_day(tr("ބައިނަލްއަޤްވާމީ މަސައްކަތްތެރިންގެ ދުވަސް"))

        # Independence Day.
        self._add_holiday_jul_26(tr("މިނިވަން ދުވަސް"))

        # Victory Day.
        self._add_holiday_nov_3(tr("ނަޞްރުގެ ދުވަސް"))

        # Republic Day.
        self._add_holiday_nov_11(tr("ޖުމްހޫރީ ދުވަސް"))

        # Islamic holidays.
        # Start of Ramadan.
        self._add_ramadan_beginning_day(tr("ރަމަޟާން މަސް ފެށޭ ދުވަސް"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("ފިޠުރުޢީދު ދުވަސް"))

        # Eid al-Fitr (Day 2).
        eid_al_fitr = tr("ފިޠުރުޢީދުގެ މުނާސަބަތުގައި")
        self._add_eid_al_fitr_day_two(eid_al_fitr)

        # Eid al-Fitr (Day 3).
        self._add_eid_al_fitr_day_three(eid_al_fitr)

        # Hajj Day.
        self._add_arafah_day(tr("ޙައްޖުދުވަސް"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("އަޟްޙާޢީދު ދުވަސް"))

        # Eid al-Adha (Day 2).
        eid_al_adha = tr("އަޟްޙާޢީދުގެ މުނާސަބަތުގައި")
        self._add_eid_al_adha_day_two(eid_al_adha)

        # Eid al-Adha (Day 3).
        self._add_eid_al_adha_day_three(eid_al_adha)

        # Eid al-Adha (Day 4).
        self._add_eid_al_adha_day_four(eid_al_adha)

        # Muharram/Islamic New Year.
        self._add_islamic_new_year_day(tr("ހިޖުރީ އާ އަހަރު ފެށޭ ދުވަސް"))

        # National Day.
        self._add_quamee_dhuvas_day(tr("ޤައުމީ ދުވަސް"))

        # Prophet Muhammad's Birthday.
        self._add_mawlid_day(tr("ކީރިތި ރަސޫލާގެ ޢީދުމީލާދު"))

        # The Day Maldives Embraced Islam.
        self._add_maldives_embraced_islam_day(tr("ރާއްޖެ އިސްލާމްވީ ދުވަސް"))


class MV(Maldives):
    pass


class MDV(Maldives):
    pass
