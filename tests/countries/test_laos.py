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

from unittest import TestCase

from holidays.countries.laos import Laos
from tests.common import CommonCountryTests


class TestLaos(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Laos)

    def test_special_bank_holidays(self):
        self.assertBankHoliday("2015-01-02")
        self.assertNoBankNonObservedHoliday(
            "2012-10-08",
            "2017-10-09",
            "2018-10-08",
            "2023-10-09",
        )

    def test_special_public_holidays(self):
        dts = ("2015-04-17",)
        obs_dts = (
            "2011-04-13",
            "2020-04-17",
        )
        self.assertHoliday(dts, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_special_workdays(self):
        self.assertWorkdayHoliday("2019-07-22")
        self.assertNoWorkdayNonObservedHoliday("2019-07-22")

    def test_establishment_day_of_the_bol(self):
        name = "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-10-07" for year in self.full_range))

        obs_dts = (
            "2012-10-08",
            "2017-10-09",
            "2018-10-08",
            "2023-10-09",
        )
        self.assertBankHolidayName(f"ພັກຊົດເຊີຍ{name}", obs_dts)
        self.assertNoBankNonObservedHoliday(obs_dts)

    def test_lao_year_end_bank_holiday(self):
        name = "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-12-29",
            "2020-12-30",
            "2020-12-31",
            "2021-12-29",
            "2021-12-30",
            "2021-12-31",
            "2022-12-28",
            "2022-12-29",
            "2022-12-30",
            "2023-12-27",
            "2023-12-28",
            "2023-12-29",
            "2024-12-27",
            "2024-12-30",
            "2024-12-31",
            "2025-12-29",
            "2025-12-30",
            "2025-12-31",
        )
        self.assertBankHolidayNameCount(name, 3, self.full_range)

    def test_new_years_day(self):
        name = "ວັນປີໃໝ່ສາກົນ"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))

        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"ພັກຊົດເຊີຍ{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_women_rights_day(self):
        name = "ວັນແມ່ຍິງສາກົນ"
        self.assertHolidayName(name, (f"{year}-03-08" for year in self.full_range))

        obs_dts = (
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"ພັກຊົດເຊີຍ{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_laos_new_year_day(self):
        name = "ບຸນປີໃໝ່ລາວ"
        songkran_years_apr_13_15 = {2012, 2017}
        songkran_years_apr_13_16 = {2016, 2020, 2024}
        for year in self.full_range:
            if year in songkran_years_apr_13_15:
                self.assertHolidayName(name, f"{year}-04-13", f"{year}-04-14", f"{year}-04-15")
            elif year in songkran_years_apr_13_16:
                self.assertHolidayName(
                    name,
                    f"{year}-04-13",
                    f"{year}-04-14",
                    f"{year}-04-15",
                    f"{year}-04-16",
                )
            else:
                self.assertHolidayName(name, f"{year}-04-14", f"{year}-04-15", f"{year}-04-16")

        obs_dts = (
            "2012-04-16",
            "2012-04-17",
            "2013-04-17",
            "2016-04-18",
            "2017-04-17",
            "2018-04-17",
            "2018-04-18",
            "2019-04-17",
            "2022-04-18",
            "2023-04-17",
            "2023-04-18",
            "2024-04-17",
            "2024-04-18",
        )
        self.assertHolidayName(f"ພັກຊົດເຊີຍ{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_labor_day(self):
        name = "ວັນກຳມະກອນສາກົນ"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))

        obs_dts = (
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"ພັກຊົດເຊີຍ{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_childrens_day(self):
        name = "ວັນເດັກສາກົນ"
        # PUBLIC.
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(1990, 2018)))
        self.assertNoHolidayName(name, range(self.start_year, 1990), range(2018, self.end_year))
        # WORKDAY.
        self.assertWorkdayHolidayName(
            name, (f"{year}-06-01" for year in range(2018, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2018))

    def test_lao_national_day(self):
        name = "ວັນຊາດ"
        self.assertHolidayName(name, (f"{year}-12-02" for year in self.full_range))

        obs_dts = (
            "2012-12-03",
            "2017-12-04",
            "2018-12-03",
            "2023-12-04",
        )
        self.assertHolidayName(f"ພັກຊົດເຊີຍ{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_makha_bousa_festival(self):
        name = "ວັນບຸນມາຂະບູຊາ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-02-08",
            "2021-01-28",
            "2022-02-16",
            "2023-02-05",
            "2024-02-24",
            "2025-02-12",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_visakha_bousa_festival(self):
        name = "ວັນບຸນວິສາຂະບູຊາ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-05-06",
            "2021-04-26",
            "2022-05-15",
            "2023-05-04",
            "2024-05-22",
            "2025-05-11",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_boun_khao_phansa_begin_of_buddhist_lent(self):
        name = "ວັນບຸນເຂົ້າພັນສາ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-07-05",
            "2021-07-24",
            "2022-07-13",
            "2023-08-01",
            "2024-07-20",
            "2025-07-10",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_boun_haw_khao_padapdin_rice_growing_festival(self):
        name = "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-08-18",
            "2021-09-06",
            "2022-08-26",
            "2023-09-14",
            "2024-09-02",
            "2025-08-23",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_boun_haw_khao_salark_ancestor_festival(self):
        name = "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-09-02",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
            "2024-09-17",
            "2025-09-07",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_boun_awk_phansa_end_of_buddhist_lent(self):
        name = "ວັນບຸນອອກພັນສາ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-10-02",
            "2021-10-21",
            "2022-10-10",
            "2023-10-29",
            "2024-10-17",
            "2025-10-07",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_boun_suang_huea_vientiane_boat_racing_festival(self):
        name = "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-10-03",
            "2021-10-22",
            "2022-10-11",
            "2023-10-30",
            "2024-10-18",
            "2025-10-08",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_boun_that_luang_festival(self):
        name = "ວັນບຸນທາດຫລວງ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name,
            "2020-10-31",
            "2021-11-19",
            "2022-11-08",
            "2023-11-27",
            "2024-11-15",
            "2025-11-05",
        )
        self.assertSchoolHolidayName(name, self.full_range)

    def test_national_teacher_day(self):
        name = "ວັນຄູແຫ່ງຊາດ"
        self.assertNoHolidayName(name)
        self.assertSchoolHolidayName(
            name, (f"{year}-10-07" for year in range(1994, self.end_year))
        )
        self.assertNoSchoolHolidayName(name, range(self.start_year, 1994))

    def test_lao_peoples_armed_force_day(self):
        name = "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-01-20" for year in self.full_range))

    def test_lao_federation_of_trade_unions_day(self):
        name = "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-02-01" for year in self.full_range))

    def test_establishment_day_of_the_lao_peoples_revolutionary_party(self):
        name = "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-03-22" for year in self.full_range))

    def test_lao_peoples_revolutionary_youth_union_day(self):
        name = "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-04-14" for year in self.full_range))

    def test_national_arbor_day(self):
        name = "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-06-01" for year in range(1989, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1989))

    def test_president_souphanouvongs_birthday(self):
        name = "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-07-13" for year in self.full_range))

    def test_the_national_day_for_wildlife_and_aquatic_animal_conservation(self):
        name = "ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-07-13" for year in range(1997, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1997))

    def test_establishment_day_of_the_lao_womens_union(self):
        name = "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-07-20" for year in self.full_range))

    def test_lao_national_mass_media_and_publishing_day(self):
        name = "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-08-13" for year in self.full_range))

    def test_lao_national_constitution_day(self):
        name = "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-08-15" for year in range(1991, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1991))

    def test_national_uprising_day(self):
        name = "ວັນຍຶດອຳນາດທົ່ວປະເທດ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-08-23" for year in self.full_range))

    def test_independence_declaration_day(self):
        name = "ວັນປະກາດເອກະລາດ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-10-12" for year in self.full_range))

    def test_president_kaysone_promvihanes_birthday(self):
        name = "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-12-13" for year in range(1991, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1991))

    def test_2023_public_holiday(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2023-01-02", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2023-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2023-04-14", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2023-04-17", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2023-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2023-12-02", "ວັນຊາດ"),
            ("2023-12-04", "ພັກຊົດເຊີຍວັນຊາດ"),
        )

    def test_2023_bank_holidays(self):
        # Dec 31 is Sunday.
        self.assertBankHolidaysInYear(
            2023,
            ("2023-10-07", "ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2023-10-09", "ພັກຊົດເຊີຍວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2023-12-27", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2023-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2023-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_2023_school_holidays(self):
        self.assertSchoolHolidaysInYear(
            2023,
            ("2023-02-05", "ວັນບຸນມາຂະບູຊາ"),
            ("2023-05-04", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2023-08-01", "ວັນບຸນເຂົ້າພັນສາ"),
            ("2023-09-14", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2023-09-29", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2023-10-07", "ວັນຄູແຫ່ງຊາດ"),
            ("2023-10-29", "ວັນບຸນອອກພັນສາ"),
            ("2023-10-30", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2023-11-27", "ວັນບຸນທາດຫລວງ"),
        )

    def test_2023_workdays(self):
        self.assertWorkdayHolidaysInYear(
            2023,
            ("2023-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2023-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2023-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2023-04-14", "ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2023-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ; ວັນເດັກສາກົນ"),
            ("2023-07-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ"),
            ("2023-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2023-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2023-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2023-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2023-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2023-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "ວັນປີໃໝ່ສາກົນ"),
            ("2022-01-03", "ພັກຊົດເຊີຍວັນປີໃໝ່ສາກົນ"),
            ("2022-01-20", "ວັນສ້າງຕັ້ງກອງທັບປະຊາຊົນລາວ"),
            ("2022-02-01", "ວັນສ້າງຕັ້ງສະຫະພັນກໍາມະບານລາວ"),
            ("2022-02-16", "ວັນບຸນມາຂະບູຊາ"),
            ("2022-03-08", "ວັນແມ່ຍິງສາກົນ"),
            ("2022-03-22", "ວັນສ້າງຕັ້ງພັກປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-04-14", "ບຸນປີໃໝ່ລາວ; ວັນສ້າງຕັ້ງສູນກາງຊາວໜຸ່ມປະຊາຊົນປະຕິວັດລາວ"),
            ("2022-04-15", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-16", "ບຸນປີໃໝ່ລາວ"),
            ("2022-04-18", "ພັກຊົດເຊີຍບຸນປີໃໝ່ລາວ"),
            ("2022-05-01", "ວັນກຳມະກອນສາກົນ"),
            ("2022-05-02", "ພັກຊົດເຊີຍວັນກຳມະກອນສາກົນ"),
            ("2022-05-15", "ວັນບຸນວິສາຂະບູຊາ"),
            ("2022-06-01", "ວັນປູກຕົ້ນໄມ້ແຫ່ງຊາດ; ວັນເດັກສາກົນ"),
            (
                "2022-07-13",
                "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ສຸພານຸວົງ; ວັນບຸນເຂົ້າພັນສາ; ວັນປ່ອຍປາ ແລະ ວັນອະນຸລັກສັດນ້ຳ-ສັດປ່າແຫ່ງຊາດ",
            ),
            ("2022-07-20", "ວັນສ້າງຕັ້ງສະຫະພັນແມ່ຍິງລາວ"),
            ("2022-08-13", "ວັນສື່ມວນຊົນແຫ່ງຊາດ ແລະ ວັນພິມຈໍາໜ່າຍ"),
            ("2022-08-15", "ວັນລັດຖະທໍາມະນູນແຫ່ງຊາດ"),
            ("2022-08-23", "ວັນຍຶດອຳນາດທົ່ວປະເທດ"),
            ("2022-08-26", "ວັນບຸນຫໍ່ເຂົ້າປະດັບດິນ"),
            ("2022-09-10", "ວັນບຸນຫໍ່ເຂົ້າສະຫຼາກ"),
            ("2022-10-07", "ວັນຄູແຫ່ງຊາດ; ວັນສ້າງຕັ້ງທະນາຄານແຫ່ງ ສປປ ລາວ"),
            ("2022-10-10", "ວັນບຸນອອກພັນສາ"),
            ("2022-10-11", "ວັນບຸນຊ່ວງເຮືອ ນະຄອນຫຼວງວຽງຈັນ"),
            ("2022-10-12", "ວັນປະກາດເອກະລາດ"),
            ("2022-11-08", "ວັນບຸນທາດຫລວງ"),
            ("2022-12-02", "ວັນຊາດ"),
            ("2022-12-13", "ວັນຄ້າຍວັນເກີດ ທ່ານ ປະທານ ໄກສອນ ພົມວິຫານ"),
            ("2022-12-28", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-29", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
            ("2022-12-30", "ສາມວັນລັດຖະການສຸດທ້າຍຂອງທຸກໆປີ"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-01-20", "Lao People's Armed Force Day"),
            ("2022-02-01", "Lao Federation of Trade Union's Day"),
            ("2022-02-16", "Makha Bousa Festival"),
            ("2022-03-08", "International Women's Rights Day"),
            ("2022-03-22", "Establishment Day of the Lao People's Revolutionary Party"),
            ("2022-04-14", "Lao New Year's Day; Lao People's Revolutionary Youth Union Day"),
            ("2022-04-15", "Lao New Year's Day"),
            ("2022-04-16", "Lao New Year's Day"),
            ("2022-04-18", "Lao New Year's Day (in lieu)"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "International Labor Day (in lieu)"),
            ("2022-05-15", "Visakha Bousa Festival"),
            ("2022-06-01", "International Children's Day; National Arbor Day"),
            (
                "2022-07-13",
                "Begin of Buddhist Lent; President Souphanouvong's Birthday; "
                "The National Day for Wildlife and Aquatic Animal Conservation",
            ),
            ("2022-07-20", "Establishment Day of the Lao Women's Union"),
            ("2022-08-13", "Lao National Mass Media and Publishing Day"),
            ("2022-08-15", "Lao National Constitution Day"),
            ("2022-08-23", "National Uprising Day"),
            ("2022-08-26", "Boun Haw Khao Padapdin"),
            ("2022-09-10", "Boun Haw Khao Salark"),
            ("2022-10-07", "Establishment Day of the BOL; National Teacher Day"),
            ("2022-10-10", "End of Buddhist Lent"),
            ("2022-10-11", "Vientiane Boat Racing Festival"),
            ("2022-10-12", "Indepedence Declaration Day"),
            ("2022-11-08", "Boun That Luang Festival"),
            ("2022-12-02", "Lao National Day"),
            ("2022-12-13", "President Kaysone Phomvihane's Birthday"),
            ("2022-12-28", "Lao Year-End Bank Holiday"),
            ("2022-12-29", "Lao Year-End Bank Holiday"),
            ("2022-12-30", "Lao Year-End Bank Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-03", "ชดเชยวันปีใหม่สากล"),
            ("2022-01-20", "วันก่อตั้งกองทัพประชาชนลาว"),
            ("2022-02-01", "วันก่อตั้งสหพันธ์กำมะบานลาว"),
            ("2022-02-16", "วันมาฆบูชา"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-03-22", "วันก่อตั้งพรรคประชาชนปฏิวัติลาว"),
            ("2022-04-14", "วันก่อตั้งศูนย์ซาวหนุ่มประชาชนปฏิวัติลาว; วันปีใหม่ลาว"),
            ("2022-04-15", "วันปีใหม่ลาว"),
            ("2022-04-16", "วันปีใหม่ลาว"),
            ("2022-04-18", "ชดเชยวันปีใหม่ลาว"),
            ("2022-05-01", "วันแรงงานสากล"),
            ("2022-05-02", "ชดเชยวันแรงงานสากล"),
            ("2022-05-15", "วันวิสาขบูชา"),
            ("2022-06-01", "วันปลูกต้นไม้แห่งชาติ; วันเด็กสากล"),
            (
                "2022-07-13",
                "วันคล้ายวันเกิดท่านประธานสุภานุวงศ์; วันอนุรักษ์สัตว์น้ำ สัตว์ป่า และวันปล่อยปลาแห่งชาติ; วันเข้าพรรษา",
            ),
            ("2022-07-20", "วันก่อตั้งสหภาพแม่หญิงลาว"),
            ("2022-08-13", "วันสื่อสารมวลชนและการพิมพ์แห่งชาติ"),
            ("2022-08-15", "วันรัฐธรรมนูญแห่งชาติ"),
            ("2022-08-23", "วันยึดอำนาจทั่วประเทศ"),
            ("2022-08-26", "วันบุญข้าวประดับดิน"),
            ("2022-09-10", "วันข้าวบุญข้าวสาก"),
            ("2022-10-07", "วันก่อตั้งธนาคารแห่ง สปป. ลาว; วันครูแห่งชาติ"),
            ("2022-10-10", "วันออกพรรษา"),
            ("2022-10-11", "วันงานบุญแข่งเรือ นครหลวงเวียงจันทน์"),
            ("2022-10-12", "วันประกาศเอกราช"),
            ("2022-11-08", "วันงานพระธาตุหลวง"),
            ("2022-12-02", "วันชาติ สปป. ลาว"),
            ("2022-12-13", "วันคล้ายวันเกิดท่านประธานไกสอน พมวิหาน"),
            ("2022-12-28", "วันหยุดสิ้นปีของสถาบันการเงิน"),
            ("2022-12-29", "วันหยุดสิ้นปีของสถาบันการเงิน"),
            ("2022-12-30", "วันหยุดสิ้นปีของสถาบันการเงิน"),
        )
