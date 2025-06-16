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
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    FRI,
)
from holidays.groups import IslamicHolidays, PersianCalendarHolidays
from holidays.holiday_base import HolidayBase


class Iran(HolidayBase, IslamicHolidays, PersianCalendarHolidays):
    """Iran holidays.

    References:
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Iran>
        * <https://fa.wikipedia.org/wiki/تعطیلات_عمومی_در_ایران>
        * <https://web.archive.org/web/20250426102648/https://www.time.ir/>
        * <https://web.archive.org/web/20170222200759/http://www.hvm.ir/LawDetailNews.aspx?id=9017>
        * <https://en.wikipedia.org/wiki/Workweek_and_weekend>
    """

    country = "IR"
    default_language = "fa_IR"
    # %s (estimated).
    estimated_label = tr("(تخمین زده) %s")
    supported_languages = ("en_US", "fa_IR")
    start_year = 1980
    weekend = {FRI}

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        IslamicHolidays.__init__(
            self, cls=IranIslamicHolidays, show_estimated=islamic_show_estimated
        )
        PersianCalendarHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Persian calendar holidays.

        # Islamic Revolution Day.
        self._add_islamic_revolution_day(tr("پیروزی انقلاب اسلامی"))

        # Iranian Oil Industry Nationalization Day.
        self._add_oil_nationalization_day(tr("روز ملی شدن صنعت نفت ایران"))

        # Last Day of Year.
        self._add_last_day_of_year(tr("آخرین روز سال"))

        # Nowruz.
        self._add_nowruz_day(tr("جشن نوروز"))

        # Nowruz Holiday.
        name = tr("عیدنوروز")
        self._add_nowruz_day_two(name)
        self._add_nowruz_day_three(name)
        self._add_nowruz_day_four(name)

        # Islamic Republic Day.
        self._add_islamic_republic_day(tr("روز جمهوری اسلامی"))

        # Nature's Day.
        self._add_natures_day(tr("روز طبیعت"))

        # Death of Imam Khomeini.
        self._add_death_of_khomeini_day(tr("رحلت حضرت امام خمینی"))

        # 15 Khordad Uprising.
        self._add_khordad_uprising_day(tr("قیام 15 خرداد"))

        # Islamic holidays.

        # Tasua.
        self._add_tasua_day(tr("تاسوعای حسینی"))

        # Ashura.
        self._add_ashura_day(tr("عاشورای حسینی"))

        # Arbaeen.
        self._add_arbaeen_day(tr("اربعین حسینی"))

        # Death of Prophet Muhammad and Martyrdom of Hasan ibn Ali.
        self._add_prophet_death_day(tr("رحلت رسول اکرم؛شهادت امام حسن مجتبی علیه السلام"))

        # Martyrdom of Ali al-Rida.
        self._add_ali_al_rida_death_day(tr("شهادت امام رضا علیه السلام"))

        # Martyrdom of Hasan al-Askari.
        self._add_hasan_al_askari_death_day(tr("شهادت امام حسن عسکری علیه السلام"))

        # Birthday of Muhammad and Imam Ja'far al-Sadiq.
        self._add_sadiq_birthday_day(tr("میلاد رسول اکرم و امام جعفر صادق علیه السلام"))

        # Martyrdom of Fatima.
        self._add_fatima_death_day(tr("شهادت حضرت فاطمه زهرا سلام الله علیها"))

        # Birthday of Imam Ali.
        self._add_ali_birthday_day(tr("ولادت امام علی علیه السلام و روز پدر"))

        # Isra' and Mi'raj.
        self._add_isra_and_miraj_day(tr("مبعث رسول اکرم (ص)"))

        self._add_imam_mahdi_birthday_day(
            # Birthday of Mahdi.
            tr("ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان")
        )

        # Martyrdom of Imam Ali.
        self._add_ali_death_day(tr("شهادت حضرت علی علیه السلام"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("عید سعید فطر"))

        # Eid al-Fitr Holiday.
        self._add_eid_al_fitr_day_two(tr("تعطیل به مناسبت عید سعید فطر"))

        # Martyrdom of Imam Ja'far al-Sadiq.
        self._add_sadiq_death_day(tr("شهادت امام جعفر صادق علیه السلام"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("عید سعید قربان"))

        # Eid al-Ghadeer.
        self._add_eid_al_ghadir_day(tr("عید سعید غدیر خم"))


class IR(Iran):
    pass


class IRN(Iran):
    pass


class IranIslamicHolidays(_CustomIslamicHolidays):
    ALI_AL_RIDA_DEATH_DATES = {
        2001: (MAY, 24),
        2002: (MAY, 13),
        2003: (MAY, 2),
        2004: (APR, 20),
        2005: (APR, 9),
        2006: (MAR, 30),
        2007: (MAR, 20),
        2008: (MAR, 8),
        2009: (FEB, 26),
        2010: (FEB, 15),
        2011: (FEB, 4),
        2012: (JAN, 24),
        2013: (JAN, 12),
        2014: ((JAN, 2), (DEC, 23)),
        2015: (DEC, 12),
        2016: (NOV, 30),
        2017: (NOV, 19),
        2018: (NOV, 8),
        2019: (OCT, 29),
        2020: (OCT, 17),
        2021: (OCT, 7),
        2022: (SEP, 27),
        2023: (SEP, 16),
        2024: (SEP, 4),
        2025: (AUG, 24),
    }

    ALI_BIRTHDAY_DATES = {
        2001: (OCT, 1),
        2002: (SEP, 21),
        2003: (SEP, 10),
        2004: (AUG, 30),
        2005: (AUG, 19),
        2006: (AUG, 8),
        2007: (JUL, 28),
        2008: (JUL, 16),
        2009: (JUL, 6),
        2010: (JUN, 26),
        2011: (JUN, 16),
        2012: (JUN, 4),
        2013: (MAY, 24),
        2014: (MAY, 13),
        2015: (MAY, 2),
        2016: (APR, 21),
        2017: (APR, 11),
        2018: (MAR, 31),
        2019: (MAR, 20),
        2020: (MAR, 8),
        2021: (FEB, 25),
        2022: (FEB, 15),
        2023: (FEB, 4),
        2024: (JAN, 25),
        2025: (JAN, 14),
    }

    ALI_DEATH_DATES = {
        2001: (DEC, 7),
        2002: (NOV, 27),
        2003: (NOV, 16),
        2004: (NOV, 5),
        2005: (OCT, 25),
        2006: (OCT, 15),
        2007: (OCT, 3),
        2008: (SEP, 22),
        2009: (SEP, 11),
        2010: (SEP, 1),
        2011: (AUG, 21),
        2012: (AUG, 10),
        2013: (JUL, 30),
        2014: (JUL, 19),
        2015: (JUL, 8),
        2016: (JUN, 27),
        2017: (JUN, 16),
        2018: (JUN, 6),
        2019: (MAY, 27),
        2020: (MAY, 15),
        2021: (MAY, 4),
        2022: (APR, 23),
        2023: (APR, 12),
        2024: (APR, 1),
        2025: (MAR, 22),
    }

    ARBAEEN_DATES = {
        2001: (MAY, 14),
        2002: (MAY, 3),
        2003: (APR, 23),
        2004: (APR, 11),
        2005: (MAR, 31),
        2006: (MAR, 21),
        2007: (MAR, 10),
        2008: (FEB, 28),
        2009: (FEB, 16),
        2010: (FEB, 5),
        2011: (JAN, 25),
        2012: (JAN, 14),
        2013: ((JAN, 3), (DEC, 23)),
        2014: (DEC, 13),
        2015: (DEC, 2),
        2016: (NOV, 20),
        2017: (NOV, 9),
        2018: (OCT, 30),
        2019: (OCT, 19),
        2020: (OCT, 8),
        2021: (SEP, 27),
        2022: (SEP, 17),
        2023: (SEP, 6),
        2024: (AUG, 25),
        2025: (AUG, 14),
    }

    ASHURA_DATES = {
        2001: (APR, 5),
        2002: (MAR, 25),
        2003: (MAR, 14),
        2004: (MAR, 2),
        2005: (FEB, 20),
        2006: (FEB, 9),
        2007: (JAN, 30),
        2008: (JAN, 19),
        2009: ((JAN, 7), (DEC, 27)),
        2010: (DEC, 16),
        2011: (DEC, 6),
        2012: (NOV, 25),
        2013: (NOV, 14),
        2014: (NOV, 4),
        2015: (OCT, 24),
        2016: (OCT, 12),
        2017: (OCT, 1),
        2018: (SEP, 20),
        2019: (SEP, 10),
        2020: (AUG, 30),
        2021: (AUG, 19),
        2022: (AUG, 8),
        2023: (JUL, 28),
        2024: (JUL, 16),
        2025: (JUL, 6),
    }

    EID_AL_ADHA_DATES = {
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 11), (DEC, 31)),
        2007: (DEC, 21),
        2008: (DEC, 9),
        2009: (NOV, 28),
        2010: (NOV, 17),
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 16),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 12),
        2020: (JUL, 31),
        2021: (JUL, 21),
        2022: (JUL, 10),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 6),
    }

    EID_AL_FITR_DATES = {
        2001: (DEC, 16),
        2002: (DEC, 6),
        2003: (NOV, 26),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 31),
        2012: (AUG, 19),
        2013: (AUG, 9),
        2014: (JUL, 29),
        2015: (JUL, 18),
        2016: (JUL, 6),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 3),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    EID_AL_GHADIR_DATES = {
        2001: (MAR, 14),
        2002: (MAR, 3),
        2003: (FEB, 20),
        2004: (FEB, 10),
        2005: (JAN, 29),
        2006: (JAN, 19),
        2007: ((JAN, 8), (DEC, 29)),
        2008: (DEC, 17),
        2009: (DEC, 6),
        2010: (NOV, 25),
        2011: (NOV, 15),
        2012: (NOV, 3),
        2013: (OCT, 24),
        2014: (OCT, 13),
        2015: (OCT, 2),
        2016: (SEP, 20),
        2017: (SEP, 9),
        2018: (AUG, 30),
        2019: (AUG, 20),
        2020: (AUG, 8),
        2021: (JUL, 29),
        2022: (JUL, 18),
        2023: (JUL, 7),
        2024: (JUN, 25),
        2025: (JUN, 14),
    }

    FATIMA_DEATH_DATES = {
        2001: (AUG, 23),
        2002: (AUG, 12),
        2003: (AUG, 2),
        2004: (JUL, 21),
        2005: (JUL, 10),
        2006: (JUN, 29),
        2007: (JUN, 18),
        2008: (JUN, 7),
        2009: (MAY, 28),
        2010: (MAY, 17),
        2011: (MAY, 7),
        2012: (APR, 25),
        2013: (APR, 14),
        2014: (APR, 3),
        2015: (MAR, 24),
        2016: (MAR, 13),
        2017: (MAR, 2),
        2018: (FEB, 20),
        2019: (FEB, 9),
        2020: (JAN, 29),
        2021: (JAN, 17),
        2022: ((JAN, 6), (DEC, 27)),
        2023: (DEC, 17),
        2024: (DEC, 5),
        2025: (NOV, 24),
    }

    HASAN_AL_ASKARI_DEATH_DATES = {
        2001: (JUN, 1),
        2002: (MAY, 21),
        2003: (MAY, 10),
        2004: (APR, 28),
        2005: (APR, 17),
        2006: (APR, 7),
        2007: (MAR, 28),
        2008: (MAR, 16),
        2009: (MAR, 6),
        2010: (FEB, 23),
        2011: (FEB, 12),
        2012: (FEB, 1),
        2013: (JAN, 20),
        2014: ((JAN, 10), (DEC, 31)),
        2015: (DEC, 20),
        2016: (DEC, 8),
        2017: (NOV, 27),
        2018: (NOV, 16),
        2019: (NOV, 6),
        2020: (OCT, 25),
        2021: (OCT, 15),
        2022: (OCT, 5),
        2023: (SEP, 24),
        2024: (SEP, 12),
        2025: (SEP, 1),
    }

    IMAM_MAHDI_BIRTHDAY_DATES = {
        2001: (NOV, 1),
        2002: (OCT, 22),
        2003: (OCT, 12),
        2004: (OCT, 1),
        2005: (SEP, 20),
        2006: (SEP, 9),
        2007: (AUG, 29),
        2008: (AUG, 17),
        2009: (AUG, 7),
        2010: (JUL, 27),
        2011: (JUL, 17),
        2012: (JUL, 5),
        2013: (JUN, 24),
        2014: (JUN, 13),
        2015: (JUN, 3),
        2016: (MAY, 22),
        2017: (MAY, 12),
        2018: (MAY, 2),
        2019: (APR, 21),
        2020: (APR, 9),
        2021: (MAR, 29),
        2022: (MAR, 18),
        2023: (MAR, 8),
        2024: (FEB, 25),
        2025: (FEB, 14),
    }

    ISRA_AND_MIRAJ_DATES = {
        2001: (OCT, 15),
        2002: (OCT, 5),
        2003: (SEP, 24),
        2004: (SEP, 13),
        2005: (SEP, 2),
        2006: (AUG, 22),
        2007: (AUG, 11),
        2008: (JUL, 30),
        2009: (JUL, 20),
        2010: (JUL, 10),
        2011: (JUN, 30),
        2012: (JUN, 18),
        2013: (JUN, 7),
        2014: (MAY, 27),
        2015: (MAY, 16),
        2016: (MAY, 5),
        2017: (APR, 25),
        2018: (APR, 14),
        2019: (APR, 3),
        2020: (MAR, 22),
        2021: (MAR, 11),
        2022: (MAR, 1),
        2023: (FEB, 18),
        2024: (FEB, 8),
        2025: (JAN, 28),
    }

    PROPHET_DEATH_DATES = {
        2001: (MAY, 22),
        2002: (MAY, 11),
        2003: (MAY, 1),
        2004: (APR, 19),
        2005: (APR, 8),
        2006: (MAR, 29),
        2007: (MAR, 18),
        2008: (MAR, 7),
        2009: (FEB, 24),
        2010: (FEB, 13),
        2011: (FEB, 2),
        2012: (JAN, 22),
        2013: ((JAN, 11), (DEC, 31)),
        2014: (DEC, 21),
        2015: (DEC, 10),
        2016: (NOV, 28),
        2017: (NOV, 17),
        2018: (NOV, 7),
        2019: (OCT, 27),
        2020: (OCT, 16),
        2021: (OCT, 5),
        2022: (SEP, 25),
        2023: (SEP, 14),
        2024: (SEP, 2),
        2025: (AUG, 22),
    }

    SADIQ_BIRTHDAY_DATES = {
        2001: (JUN, 10),
        2002: (MAY, 30),
        2003: (MAY, 19),
        2004: (MAY, 7),
        2005: (APR, 26),
        2006: (APR, 16),
        2007: (APR, 6),
        2008: (MAR, 25),
        2009: (MAR, 15),
        2010: (MAR, 4),
        2011: (FEB, 21),
        2012: (FEB, 10),
        2013: (JAN, 29),
        2014: (JAN, 19),
        2015: ((JAN, 9), (DEC, 29)),
        2016: (DEC, 17),
        2017: (DEC, 6),
        2018: (NOV, 25),
        2019: (NOV, 15),
        2020: (NOV, 3),
        2021: (OCT, 24),
        2022: (OCT, 14),
        2023: (OCT, 3),
        2024: (SEP, 21),
        2025: (SEP, 10),
    }

    SADIQ_DEATH_DATES = {
        2001: (JAN, 20),
        2002: ((JAN, 9), (DEC, 30)),
        2003: (DEC, 20),
        2004: (DEC, 8),
        2005: (NOV, 28),
        2006: (NOV, 17),
        2007: (NOV, 6),
        2008: (OCT, 25),
        2009: (OCT, 14),
        2010: (OCT, 4),
        2011: (SEP, 24),
        2012: (SEP, 12),
        2013: (SEP, 2),
        2014: (AUG, 22),
        2015: (AUG, 11),
        2016: (JUL, 30),
        2017: (JUL, 20),
        2018: (JUL, 9),
        2019: (JUN, 29),
        2020: (JUN, 17),
        2021: (JUN, 6),
        2022: (MAY, 27),
        2023: (MAY, 16),
        2024: (MAY, 4),
        2025: (APR, 24),
    }

    TASUA_DATES = {
        2001: (APR, 4),
        2002: (MAR, 24),
        2003: (MAR, 13),
        2004: (MAR, 1),
        2005: (FEB, 19),
        2006: (FEB, 8),
        2007: (JAN, 29),
        2008: (JAN, 18),
        2009: ((JAN, 6), (DEC, 26)),
        2010: (DEC, 15),
        2011: (DEC, 5),
        2012: (NOV, 24),
        2013: (NOV, 13),
        2014: (NOV, 3),
        2015: (OCT, 23),
        2016: (OCT, 11),
        2017: (SEP, 30),
        2018: (SEP, 19),
        2019: (SEP, 9),
        2020: (AUG, 29),
        2021: (AUG, 18),
        2022: (AUG, 7),
        2023: (JUL, 27),
        2024: (JUL, 15),
        2025: (JUL, 5),
    }
