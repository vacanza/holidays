#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

"""
References:

    - https://en.wikipedia.org/wiki/Public_holidays_in_Laos
    - https://juristact.weebly.com/uploads/1/0/9/9/109947087/d17_386.pdf

    - https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf
    - https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf
    - https://www.timeanddate.com/holidays/laos/
    - https://www.bcel.com.la/bcel/bcel-calendar.html?y=2022
    - https://www.bcel.com.la/bcel/bcel-calendar.html?year=2023
    - http://www.lsx.com.la/cal/getStockCalendar.do?lang=lo (from 2011 onwards)

!!! If Public Holiday falls on weekends, (in lieu) on workday !!!
Despite the wording, this usually only applies to Monday only for holidays,
consecutive holidays all have their own special in lieu declared separately.

As featured in Decree on Holidays No. 386 / Rev. 15.12.2017;
    - Saturdays and Sundays shall be restdays each week.
    - In-Lieu holidays shall be given if it fall on the weekends.

Limitations:
    - Laotian holidays only works from 1976 onwards, and are only 100% accurate from 2018 onwards.
    - Laotian Lunar Calendar Holidays only work from 1941 (B.E. 2485) onwards until 2057
      (B.E. 2601) as we only have Thai year-type data for cross-checking until then.
"""

from gettext import gettext as tr

from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUL, OCT, DEC
from holidays.calendars.thai import KHMER_CALENDAR
from holidays.constants import BANK, PUBLIC, SCHOOL, WORKDAY
from holidays.groups import InternationalHolidays, ThaiCalendarHolidays, StaticHolidays
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    THU_FRI_TO_NEXT_MON,
    FRI_TO_NEXT_TUE,
    SAT_TO_NEXT_TUE,
    SAT_SUN_TO_NEXT_MON,
    SAT_SUN_TO_NEXT_WED,
)


class LaHolidays(ObservedHolidayBase, InternationalHolidays, StaticHolidays, ThaiCalendarHolidays):
    """A class to represent holidays for Laos."""

    country = "LA"
    name = "Laos"
    supported_categories = (BANK, PUBLIC, SCHOOL, WORKDAY)
    default_language = "lo"
    # %s (in lieu).
    observed_label = tr("ພັກຊົດເຊີຍ%s")
    supported_languages = ("en_US", "lo", "th")

    def __init__(self, *args, **kwargs):
        InternationalHolidays.__init__(self)
        ThaiCalendarHolidays.__init__(self, KHMER_CALENDAR)
        StaticHolidays.__init__(self, cls=LaStaticHolidays)
        kwargs.setdefault("observed_rule", SAT_SUN_TO_NEXT_MON)
        kwargs.setdefault("observed_since", 2018)
        super().__init__(*args, **kwargs)

    def _populate_bank_holidays(self):
        # Based on both LSX and BCEL calendar.
        # Available post-Lao PDR proclamation on Dec 2, 1975.
        if self._year <= 1975:
            return None

        # ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ
        # Status: In-Use.
        # Celebrated the creation of the Bank of the Lao PDR on Oct 7, 1968.
        # In-Lieus are available in LSX calendar.

        # Establishment Day of the BOL.
        self._add_observed(self._add_holiday_oct_7(tr("ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ")))

        # ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ
        # Status: In-Use.
        # Financial Institution in Laos are closed on last 3 weekdays of the year.
        # Assume [WEEKDAY] is Dec 31:
        #   - CASE MON: (THU)-(FRI)-MON
        #   - CASE TUE: (FRI)-MON-TUE
        #   - CASE WED: MON-TUE-WED
        #   - CASE THU: TUE-WED-THU
        #   - CASE FRI/SAT/SUN: WED-THU-FRI

        # Lao Year-End Bank Holiday.
        name = tr("ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ")

        last_workday = self._add_holiday(
            name, self._get_next_workday(self._next_year_new_years_day, -1)
        )
        second_to_last_workday = self._add_holiday(name, self._get_next_workday(last_workday, -1))
        self._add_holiday(name, self._get_next_workday(second_to_last_workday, -1))

    def _populate_public_holidays(self):
        # Available post-Lao PDR proclamation on Dec 2, 1975.
        if self._year <= 1975:
            return None

        # ວັນປີໃໝ່ສາກົນ
        # Status: In-Use.

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("ວັນປີໃໝ່ສາກົນ")))

        # ວັນແມ່ຍິງສາກົນ
        # Status: In-Use.
        # Only acts as day off for Women.

        # International Women's Rights Day.
        self._add_observed(self._add_womens_day(tr("ວັນແມ່ຍິງສາກົນ")))

        # ບຸນປີໃໝ່ລາວ
        # Status: In-Use.
        # Celebrated for 3 days from 14-16 April annualy.
        # Observed dates prior to 2018 are assigned manually.
        #   - CASE 1: THU-FRI-SAT -> in lieu on MON.
        #   - CASE 2: FRI-SAT-SUN -> in lieu on MON-TUE.
        #   - CASE 3: SAT-SUN-MON -> in lieu on TUE-WED.
        #   - CASE 4: SUN-MON-TUE -> in lieu on WED.

        # Lao New Year's Day.
        name = tr("ບຸນປີໃໝ່ລາວ")
        dt = self._add_holiday_apr_14(name)
        self._add_holiday_apr_15(name)
        self._add_holiday_apr_16(name)

        self._add_observed(dt, rule=THU_FRI_TO_NEXT_MON + SAT_TO_NEXT_TUE)
        self._add_observed(dt, rule=FRI_TO_NEXT_TUE + SAT_SUN_TO_NEXT_WED)

        # ວັນກຳມະກອນສາກົນ
        # Status: In-Use.

        # International Labor Day.
        self._add_observed(self._add_labor_day(tr("ວັນກຳມະກອນສາກົນ")))

        # ວັນເດັກສາກົນ (`PUBLIC`)
        # Status: Defunct, Still Observed.
        # Starts as public holiday after Lao PDR joined UN Convention on the
        # Rights of the Child in 1989 (de-facto start as holiday in 1990).
        # Became defunct from 2018 onwards. Still accessible in `WORKDAY` category.

        if 1990 <= self._year <= 2017:
            # International Children Day.
            self._add_childrens_day(tr("ວັນເດັກສາກົນ"))

        # ວັນຊາດ
        # Status: In-Use.
        # Celebrated the establishment of Lao PDR on Dec 2, 1975.

        # Lao National Day.
        self._add_observed(self._add_holiday_dec_2(tr("ວັນຊາດ")))

    def _populate_school_holidays(self):
        # Laotian Lunar Calendar Holidays
        # See `_ThaiLunisolar` in holidays/utils.py for more details.
        # Unofficial, but observed by schools and most business holidays;
        # As such, no in lieu observance are in place for these holidays.

        # Laotian Lunar Calendar Holidays only work from 1941 to 2057.
        if self._year <= 1975:
            return None

        # ວັນບຸນມາຂະບູຊາ
        # Status: In-Use.
        # 15th Waxing Day of Month 3.
        # Also denoted as festival days for Sikhottabong Stupa Festival and
        # Wat Phou Champasack Festival in BCEL calendar.

        # Makha Bousa Festival.
        self._add_makha_bucha(tr("ວັນບຸນມາຂະບູຊາ"))

        # ວັນບຸນວິສາຂະບູຊາ
        # Status: In-Use.
        # 15th Waxing Day of Month 6.
        # This utilizes Thai calendar as a base, though are calculated to always happen
        # in the Traditional Visakhamas month (May).
        # In Laos Calendar, the day after marks the traditional Buddhist Calendar Year change.

        # Visakha Bousa Festival.
        self._add_visakha_bucha(tr("ວັນບຸນວິສາຂະບູຊາ"))

        # ວັນບຸນເຂົ້າພັນສາ
        # Status: In-Use.
        # 15th Waxing Day of Month 8 (Asarnha Bucha for Thailand and Cambodia).

        # Boun Khao Phansa (Begin of Buddhist Lent).
        self._add_asarnha_bucha(tr("ວັນບຸນເຂົ້າພັນສາ"))

        # ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ
        # Status: In-Use.
        # 14th Waning Day of Month 9.

        # Boun Haw Khao Padapdin (Rice Growing Festival).
        self._add_boun_haw_khao_padapdin(tr("ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"))

        # ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ
        # Status: In-Use.
        # 15th Waxing Day of Month 10.

        # Boun Haw Khao Salark (Ancestor Festival).
        self._add_boun_haw_khao_salark(tr("ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"))

        # ວັນບຸນອອກພັນສາ
        # Status: In-Use.
        # 15th Waxing Day of Month 11.

        # Boun Awk Phansa (End of Buddhist Lent).
        self._add_ok_phansa(tr("ວັນບຸນອອກພັນສາ"))

        # ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ
        # Status: In-Use.
        # 1st Waning Day of Month 11.

        # Boun Suang Heua (Vientiane Boat Racing Festival).
        self._add_boun_suang_heua(tr("ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"))

        # ວັນບຸນທາດຫລວງ
        # Status: In-Use.
        # 15th Waxing Day of Month 12.

        # Boun That Luang Festival.
        self._add_loy_krathong(tr("ວັນບຸນທາດຫລວງ"))

        # ວັນຄູແຫ່ງຊາດ
        # Status: In-Use.
        # In recognition of First Lao Teacher, Kham, as started in Oct 7, 1994.

        if self._year >= 1994:
            # National Teacher Day.
            self._add_holiday_oct_7(tr("ວັນຄູແຫ່ງຊາດ"))

    def _populate_workday_holidays(self):
        # No Public Holidays are issued, though still observed by the government.

        # Available post-Lao PDR proclamation on Dec 2, 1975.
        if self._year <= 1975:
            return None

        # ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ
        # Status: In-Use.
        # Celebrated the creation of the independent Lao army on Jan 20, 1949.

        # Lao People's Armed Force Day.
        self._add_holiday_jan_20(tr("ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"))

        # ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ
        # Status: In-Use.
        # Celebrated the creation of Lao Federation of Trade Unions on Feb 1, 1966.

        # Lao Federation of Trade Union's Day.
        self._add_holiday_feb_1(tr("ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"))

        # ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ
        # Status: In-Use.
        # Celebrated the creation of the Lao People's Revolutionary Party on Mar 22, 1955.

        # Establishment Day of the Lao People's Revolutionary Party.
        self._add_holiday_mar_22(tr("ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"))

        # ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ
        # Status: In-Use.
        # Celebrated the creation of the Lao People's Revolutionary Youth Union on Apr 14, 1955.

        # Lao People's Revolutionary Youth Union Day.
        self._add_holiday_apr_14(tr("ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"))

        # ວັນເດັກສາກົນ (`WORKDAY`)
        # Status: Defunct, Still Observed.
        # Starts as public holiday after Lao PDR joined UN Convention on the
        # Rights of the Child in 1989 (de-facto start as holiday in 1990).
        # Became defunct from 2018 onwards. Still accessible in `WORKDAY` category.

        if self._year >= 2018:
            # International Children Day.
            self._add_childrens_day(tr("ວັນເດັກສາກົນ"))

        # ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ
        # Status: In-Use.
        # Assumed to first observed in 1989 following the National Forestry Conference in May.

        if self._year >= 1989:
            # National Arbor Day.
            self._add_holiday_jun_1(tr("ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"))

        # ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ
        # Status: In-Use.
        # Celebrated President Souphanouvong's Birthday Anniversary on Jul 13, 1909.

        # President Souphanouvong's Birthday.
        self._add_holiday_jul_13(tr("ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ"))

        # ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ
        # Status: In-Use.
        # First designated in 1997 to concide with Souphanouvong's Birthday anniversary.

        if self._year >= 1997:
            # The National Day for Wildlife and Aquatic Animal Conservation.
            self._add_holiday_jul_13(tr("ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"))

        # ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ
        # Status: In-Use.
        # Celebrated the creation of Lao Women's Union on Jul 20, 1955.

        # Establishment Day of the Lao Women's Union.
        self._add_holiday_jul_20(tr("ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"))

        # ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ
        # Status: In-Use.
        # Celebrated the creation of LPRP's Party Newspaper on Aug 13, 1950.

        # Lao National Mass Media and Publishing Day.
        self._add_holiday_aug_13(tr("ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"))

        # ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ
        # Status: In-Use.
        # Celebrated the adoption of the 1991 Constitution on Aug 15, 1991.

        if self._year >= 1991:
            # Lao National Constitution Day.
            self._add_holiday_aug_15(tr("ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"))

        # ວັນຍຶດອຳນາດທົ່ວປະເທດ
        # Status: In-Use.
        # Celebrated the Liberation of Vientiane by Pathet Lao forces on Aug 23, 1975.

        # National Uprising Day.
        self._add_holiday_aug_23(tr("ວັນຍຶດອຳນາດທົ່ວປະເທດ"))

        # ວັນປະກາດເອກະລາດ
        # Status: In-Use.
        # Celebrated the Declaration of Independence on Oct 12, 1945.

        # Indepedence Declaration Day.
        self._add_holiday_oct_12(tr("ວັນປະກາດເອກະລາດ"))

        # ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ
        # Status: In-Use.
        # Celebrated President Kaysone Phomvihane's Birthday Anniversary on Dec 13, 1920.

        if self._year >= 1991:
            # President Kaysone Phomvihane's Birthday.
            self._add_holiday_dec_13(tr("ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"))


class LaStaticHolidays:
    # Special Cases.

    # Special Bank Holiday.
    special_bank_day_off = tr("ມື້ປິດການໃຫ້ບໍລິການຂອງທະນາຄານຕົວແທນ")

    # New Year's Day.
    new_year_day = tr("ວັນປີໃໝ່ສາກົນ")

    # International Women's Rights Day.
    international_womens_rights_day = tr("ວັນແມ່ຍິງສາກົນ")

    # Lao New Year's Day.
    lao_new_year = tr("ບຸນປີໃໝ່ລາວ")

    # Lao New Year's Day (Special).
    lao_new_year_special = tr("ພັກບຸນປີໃໝ່ລາວ")

    # International Labor Day.
    international_labor_day = tr("ວັນກຳມະກອນສາກົນ")

    # Establishment Day of the Lao Women's Union.
    lao_womens_union = tr("ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ")

    # Establishment Day of the BOL.
    establishment_day_of_bol = tr("ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ")

    # Lao National Day.
    lao_national_day = tr("ວັນຊາດ")

    special_bank_holidays = {
        2015: (JAN, 2, special_bank_day_off),
    }

    special_bank_holidays_observed = {
        2017: (OCT, 9, establishment_day_of_bol),
    }

    special_public_holidays = {
        2015: (APR, 17, lao_new_year_special),
        2016: (
            (APR, 13, lao_new_year_special),
            (APR, 18, lao_new_year_special),
        ),
        2020: (
            (APR, 13, lao_new_year_special),
            (APR, 17, lao_new_year_special),
        ),
    }

    special_public_holidays_observed = {
        2011: (APR, 13, lao_new_year),
        2012: (
            (JAN, 2, new_year_day),
            (APR, 13, lao_new_year),
            (APR, 17, lao_new_year),
            (DEC, 3, lao_national_day),
        ),
        2013: (APR, 17, lao_new_year),
        2015: (MAR, 9, international_womens_rights_day),
        2016: (MAY, 2, international_labor_day),
        2017: (
            (JAN, 2, new_year_day),
            (APR, 13, lao_new_year),
            (APR, 17, lao_new_year),
            (DEC, 4, lao_national_day),
        ),
    }

    special_workday_holidays_observed = {
        2019: (JUL, 22, lao_womens_union),
    }
