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

from holidays.financial.tel_aviv_stock_exchange import TelAvivStockExchange
from tests.common import CommonFinancialTests


class TestTelAvivStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TelAvivStockExchange)

    def test_special_holidays(self):
        self.assertHoliday(
            "2013-01-22",
            "2015-03-17",
            "2018-10-30",
            "2021-03-23",
            "2022-11-01",
            "2023-10-31",
            "2026-10-27",
        )

    def test_purim(self):
        name = "פורים"
        dts = (
            "2020-03-10",
            "2021-02-26",
            "2022-03-17",
            "2023-03-07",
            "2024-03-24",
            "2025-03-14",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)

    def test_shushan_purim(self):
        name = "שושן פורים"
        dts = (
            "2022-03-18",
            "2023-03-08",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2022, 2024))
        self.assertNoHolidayName(name, range(self.start_year, 2022), range(2024, self.end_year))

    def test_passover(self):
        eve_name = "ערב פסח"
        name = "פסח"
        eve_7th_name = "ערב שביעי של פסח"
        name_7th = "שביעי של פסח"
        self.assertHolidayName(
            eve_name,
            "2019-04-19",
            "2020-04-08",
            "2022-04-15",
            "2023-04-05",
            "2024-04-22",
        )
        self.assertNoHolidayName(eve_name, "2021-03-27", "2025-04-12")
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-03-28",
            "2023-04-06",
            "2024-04-23",
            "2025-04-13",
        )
        self.assertNoHolidayName(name, "2019-04-20", "2022-04-16")
        self.assertHolidayName(
            eve_7th_name,
            "2019-04-25",
            "2020-04-14",
            "2021-04-02",
            "2022-04-21",
            "2023-04-11",
            "2024-04-28",
            "2025-04-18",
        )
        self.assertHolidayName(
            name_7th,
            "2019-04-26",
            "2020-04-15",
            "2022-04-22",
            "2023-04-12",
            "2024-04-29",
        )
        self.assertNoHolidayName(name_7th, "2021-04-03", "2025-04-19")

    def test_memorial_day(self):
        name = "יום הזיכרון"
        dts = (
            "2020-04-28",
            "2021-04-14",
            "2022-05-04",
            "2023-04-25",
            "2024-05-13",
            "2025-04-30",
        )
        non_obs_dts = (
            "2021-04-16",
            "2022-05-05",
            "2024-05-12",
            "2025-05-01",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)
        self.assertNoHolidayName(name, non_obs_dts)

    def test_independence_day(self):
        name = "יום העצמאות"
        dts = (
            "2020-04-29",
            "2021-04-15",
            "2022-05-05",
            "2023-04-26",
            "2024-05-14",
            "2025-05-01",
        )
        non_obs_dts = (
            "2021-04-17",
            "2022-05-06",
            "2024-05-13",
            "2025-05-02",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)
        self.assertNoHolidayName(name, non_obs_dts)

    def test_shavuot_eve(self):
        name = "ערב שבועות"
        dts = (
            "2013-05-14",
            "2014-06-03",
            "2017-05-30",
            "2020-05-28",
            "2021-05-16",
            "2023-05-25",
            "2024-06-11",
            "2025-06-01",
        )
        self.assertHolidayName(name, dts)
        self.assertNoHolidayName(
            name,
            "2015-05-23",
            "2016-06-11",
            "2018-05-19",
            "2019-06-08",
            "2022-06-04",
        )

    def test_shavuot(self):
        name = "שבועות"
        dts = (
            "2020-05-29",
            "2021-05-17",
            "2022-06-05",
            "2023-05-26",
            "2024-06-12",
            "2025-06-02",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)

    def test_tisha_bav(self):
        name = "תשעה באב"
        dts = (
            "2015-07-26",
            "2016-08-14",
            "2017-08-01",
            "2018-07-22",
            "2019-08-11",
            "2020-07-30",
            "2021-07-18",
            "2022-08-07",
            "2023-07-27",
            "2024-08-13",
            "2025-08-03",
        )
        non_obs_dts = (
            "2015-07-25",
            "2016-08-13",
            "2018-07-21",
            "2019-08-10",
            "2022-08-06",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)
        self.assertNoHolidayName(name, non_obs_dts)

    def test_rosh_hashanah(self):
        eve_name = "ערב ראש השנה"
        name = "ראש השנה"
        self.assertHolidayName(
            eve_name,
            "2020-09-18",
            "2021-09-06",
            "2022-09-25",
            "2023-09-15",
            "2024-10-02",
            "2025-09-22",
        )
        self.assertHolidayName(
            name,
            "2019-09-30",
            "2019-10-01",
            "2020-09-20",
            "2021-09-07",
            "2021-09-08",
            "2022-09-26",
            "2022-09-27",
            "2023-09-17",
            "2024-10-03",
            "2024-10-04",
            "2025-09-23",
            "2025-09-24",
        )
        self.assertNoHolidayName(name, "2020-09-19", "2023-09-16")

    def test_yom_kippur_eve(self):
        name = "ערב יום כיפור"
        dts = (
            "2020-09-27",
            "2021-09-15",
            "2022-10-04",
            "2023-09-24",
            "2024-10-11",
            "2025-10-01",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)

    def test_yom_kippur(self):
        eve_name = "ערב יום כיפור"
        name = "יום כיפור"
        self.assertHolidayName(
            eve_name,
            "2020-09-27",
            "2021-09-15",
            "2022-10-04",
            "2023-09-24",
            "2024-10-11",
            "2025-10-01",
        )
        self.assertHolidayName(eve_name, self.full_range)
        self.assertHolidayName(
            name,
            "2020-09-28",
            "2021-09-16",
            "2022-10-05",
            "2023-09-25",
            "2025-10-02",
        )
        self.assertNoHolidayName(name, "2024-10-12")

    def test_sukkot(self):
        eve_name = "ערב סוכות"
        name = "סוכות"
        self.assertHolidayName(
            eve_name,
            "2019-10-13",
            "2020-10-02",
            "2021-09-20",
            "2022-10-09",
            "2023-09-29",
            "2024-10-16",
            "2025-10-06",
        )
        self.assertHolidayName(
            name,
            "2019-10-14",
            "2021-09-21",
            "2022-10-10",
            "2024-10-17",
            "2025-10-07",
        )
        self.assertNoHolidayName(name, "2020-10-03", "2023-09-30")

    def test_simchat_torah(self):
        eve_name = "ערב שמחת תורה"
        name = "שמחת תורה/שמיני עצרת"
        self.assertHolidayName(
            eve_name,
            "2020-10-09",
            "2021-09-27",
            "2022-10-16",
            "2023-10-06",
            "2024-10-23",
            "2025-10-13",
        )
        self.assertHolidayName(
            name,
            "2014-10-16",
            "2019-10-21",
            "2021-09-28",
            "2022-10-17",
            "2024-10-24",
            "2025-10-14",
        )
        self.assertNoHolidayName(
            name,
            "2020-10-10",
            "2023-10-07",
            range(self.start_year, self.end_year),
        )

    def test_friday_before_holiday(self):
        yk_eve_bridge_name = "ערב יום כיפור (שישי לפני חג)"
        passover_bridge_name = "פסח (שישי לפני חג)"
        self.assertHolidayName(yk_eve_bridge_name, "2026-09-18")
        self.assertNoHolidayName(passover_bridge_name, "2021-03-26")

    def test_chol_hamoed(self):
        passover_name = "חול המועד פסח (חצי יום מסחר)"
        sukkot_name = "חול המועד סוכות (חצי יום מסחר)"
        self.assertNoHolidayName(passover_name)
        self.assertNoHolidayName(sukkot_name)
        self.assertHalfDayHolidayName(
            passover_name,
            "2020-04-12",
            "2020-04-13",
            "2021-03-29",
            "2021-03-30",
            "2021-03-31",
            "2021-04-01",
        )
        self.assertNoHalfDayHolidayName(
            passover_name,
            "2020-04-10",
            "2020-04-11",
        )
        self.assertHalfDayHolidayName(
            sukkot_name,
            "2019-10-15",
            "2019-10-16",
            "2019-10-17",
            "2020-10-04",
            "2020-10-05",
            "2020-10-06",
            "2020-10-07",
            "2020-10-08",
            "2021-09-22",
            "2021-09-23",
            "2021-09-26",
        )
        self.assertNoHalfDayHolidayName(
            sukkot_name,
            "2019-10-18",
            "2019-10-19",
            "2021-09-24",
            "2021-09-25",
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-03-24", "פורים"),
            ("2024-04-22", "ערב פסח"),
            ("2024-04-23", "פסח"),
            ("2024-04-28", "ערב שביעי של פסח"),
            ("2024-04-29", "שביעי של פסח"),
            ("2024-05-13", "יום הזיכרון"),
            ("2024-05-14", "יום העצמאות"),
            ("2024-06-11", "ערב שבועות"),
            ("2024-06-12", "שבועות"),
            ("2024-08-13", "תשעה באב"),
            ("2024-10-02", "ערב ראש השנה"),
            ("2024-10-03", "ראש השנה"),
            ("2024-10-04", "ראש השנה"),
            ("2024-10-11", "ערב יום כיפור"),
            ("2024-10-16", "ערב סוכות"),
            ("2024-10-17", "סוכות"),
            ("2024-10-23", "ערב שמחת תורה"),
            ("2024-10-24", "שמחת תורה/שמיני עצרת"),
        )

    def test_half_day_2024(self):
        self.assertHalfDayHolidaysInYear(
            2024,
            ("2024-04-24", "חול המועד פסח (חצי יום מסחר)"),
            ("2024-04-25", "חול המועד פסח (חצי יום מסחר)"),
            ("2024-10-20", "חול המועד סוכות (חצי יום מסחר)"),
            ("2024-10-21", "חול המועד סוכות (חצי יום מסחר)"),
            ("2024-10-22", "חול המועד סוכות (חצי יום מסחר)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-03-14", "פורים"),
            ("2025-04-13", "פסח"),
            ("2025-04-14", "חול המועד פסח (חצי יום מסחר)"),
            ("2025-04-15", "חול המועד פסח (חצי יום מסחר)"),
            ("2025-04-16", "חול המועד פסח (חצי יום מסחר)"),
            ("2025-04-17", "חול המועד פסח (חצי יום מסחר)"),
            ("2025-04-18", "ערב שביעי של פסח"),
            ("2025-04-30", "יום הזיכרון"),
            ("2025-05-01", "יום העצמאות"),
            ("2025-06-01", "ערב שבועות"),
            ("2025-06-02", "שבועות"),
            ("2025-08-03", "תשעה באב"),
            ("2025-09-22", "ערב ראש השנה"),
            ("2025-09-23", "ראש השנה"),
            ("2025-09-24", "ראש השנה"),
            ("2025-10-01", "ערב יום כיפור"),
            ("2025-10-02", "יום כיפור"),
            ("2025-10-06", "ערב סוכות"),
            ("2025-10-07", "סוכות"),
            ("2025-10-08", "חול המועד סוכות (חצי יום מסחר)"),
            ("2025-10-09", "חול המועד סוכות (חצי יום מסחר)"),
            ("2025-10-12", "חול המועד סוכות (חצי יום מסחר)"),
            ("2025-10-13", "ערב שמחת תורה"),
            ("2025-10-14", "שמחת תורה/שמיני עצרת"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-03-14", "Purim"),
            ("2025-04-13", "Passover"),
            ("2025-04-14", "Chol HaMoed Passover (Half trading day)"),
            ("2025-04-15", "Chol HaMoed Passover (Half trading day)"),
            ("2025-04-16", "Chol HaMoed Passover (Half trading day)"),
            ("2025-04-17", "Chol HaMoed Passover (Half trading day)"),
            ("2025-04-18", "Passover II Eve"),
            ("2025-04-30", "Memorial Day"),
            ("2025-05-01", "Independence Day"),
            ("2025-06-01", "Shavuot Eve"),
            ("2025-06-02", "Shavuot"),
            ("2025-08-03", "Tisha B'Av"),
            ("2025-09-22", "Jewish New Year Eve"),
            ("2025-09-23", "Jewish New Year"),
            ("2025-09-24", "Jewish New Year"),
            ("2025-10-01", "Yom Kippur Eve"),
            ("2025-10-02", "Yom Kippur"),
            ("2025-10-06", "Sukkoth Eve"),
            ("2025-10-07", "Sukkoth"),
            ("2025-10-08", "Chol HaMoed Sukkoth (Half trading day)"),
            ("2025-10-09", "Chol HaMoed Sukkoth (Half trading day)"),
            ("2025-10-12", "Chol HaMoed Sukkoth (Half trading day)"),
            ("2025-10-13", "Simchat Torah Eve"),
            ("2025-10-14", "Simchat Torah / Shemini Atzeret"),
        )
