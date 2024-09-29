#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.groups import IslamicHolidays, PersianCalendarHolidays
from holidays.holiday_base import HolidayBase


class Iran(HolidayBase, IslamicHolidays, PersianCalendarHolidays):
    """
    References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Iran
    - https://fa.wikipedia.org/wiki/تعطیلات_عمومی_در_ایران
    """

    country = "IR"
    default_language = "fa"
    # %s (estimated).
    estimated_label = tr("(تخمین زده) %s")
    supported_languages = ("en_US", "fa")

    def __init__(self, *args, **kwargs):
        IslamicHolidays.__init__(self)
        PersianCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        if self._year <= 1979:
            return None

        # Persian New Year.
        name = tr("نوروز")
        self._add_nowruz_day(name)
        self._add_nowruz_day_two(name)
        self._add_nowruz_day_three(name)
        self._add_nowruz_day_four(name)

        # Islamic Republic Day.
        self._add_islamic_republic_day(tr("روز جمهوری اسلامی"))

        # Nature's Day.
        self._add_natures_day(tr("روز طبیعت"))

        # Death of Khomeini.
        self._add_death_of_khomeini_day(tr("درگذشت سید روح‌الله خمینی"))

        # Khordad National Uprising.
        self._add_khordad_uprising_day(tr("تظاهرات ۱۵ خرداد"))

        # Islamic Revolution Day.
        self._add_islamic_revolution_day(tr("پیروزی انقلاب ۵۷"))

        # Iranian Oil Industry Nationalization Day.
        self._add_oil_nationalization_day(tr("ملی‌شدن صنعت نفت"))

        # Tasua.
        self._add_tasua_day(tr("تاسوعا"))

        # Ashura.
        self._add_ashura_day(tr("کشته‌شدن حسین بن علی، عاشورا"))

        # Arbaeen.
        self._add_arbaeen_day(tr("چهلم حسین بن علی اربعین"))

        # Demise of Prophet Muhammad and Hasan ibn Ali.
        self._add_prophet_death_day(tr("کشته‌شدن حسن مجتبی و درگذشت محمد"))

        # Martyrdom of Ali al-Rida.
        self._add_ali_al_rida_death_day(tr("کشته‌شدن علی بن موسی الرضا"))

        # Martyrdom of Hasan al-Askari.
        self._add_hasan_al_askari_death_day(tr("کشته‌شدن حسن عسکری"))

        # Birthday of Muhammad and Ja'far al-Sadiq.
        self._add_sadiq_birthday_day(tr("زادروز محمد و جعفر صادق"))

        # Martyrdom of Fatima.
        self._add_fatima_death_day(tr("کشته‌شدن فاطمه زهرا"))

        # Birthday of Ali.
        self._add_ali_birthday_day(tr("زادروز علی بن ابی‌طالب"))

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("مبعث"))

        # Birthday of Mahdi.
        self._add_imam_mahdi_birthday_day(tr("زادروز حجت بن الحسن"))

        # Martyrdom of Ali.
        self._add_ali_death_day(tr("کشته‌شدن علی بن ابی‌طالب"))

        # Eid al-Fitr.
        name = tr("عید فطر")
        self._add_eid_al_fitr_day(name)
        self._add_eid_al_fitr_day_two(name)

        # Martyrdom of Ja'far al-Sadiq.
        self._add_sadiq_death_day(tr("کشته‌شدن جعفر صادق"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عید قربان"))

        # Eid al-Ghadeer.
        self._add_eid_al_ghadir_day(tr("عید غدیر"))


class IR(Iran):
    pass


class IRN(Iran):
    pass
