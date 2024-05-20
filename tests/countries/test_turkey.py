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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.constants import HALF_DAY, PUBLIC
from holidays.countries.turkey import Turkey, TR, TUR
from tests.common import CommonCountryTests


class TestTurkey(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Turkey, years=range(1936, 2050))

    def test_country_aliases(self):
        self.assertAliases(Turkey, TR, TUR)

    def test_no_holidays(self):
        self.assertNoHolidays(Turkey(categories=(HALF_DAY, PUBLIC), years=1935))

    def test_special_holidays(self):
        self.assertHoliday("1999-12-31")

    def test_new_years_day(self):
        self.assertHolidayName("Yılbaşı", (f"{year}-01-01" for year in range(1936, 2050)))

    def test_national_sovereignty_and_childrens_day(self):
        name_1 = "Ulusal Egemenlik Bayramı"
        name_2 = "Ulusal Egemenlik ve Çocuk Bayramı"
        self.assertHolidayName(name_1, (f"{year}-04-23" for year in range(1936, 1981)))
        self.assertHolidayName(name_2, (f"{year}-04-23" for year in range(1981, 2050)))
        self.assertNoHolidayName(name_1, range(1981, 2050))
        self.assertNoHolidayName(name_2, range(1936, 1981))

    def test_labor_day(self):
        name = "Emek ve Dayanışma Günü"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2009, 2050)))
        self.assertNoHolidayName(name, range(1936, 2009))

    def test_ataturk_youth_and_sports_day(self):
        name_1 = "Gençlik ve Spor Bayramı"
        name_2 = "Atatürk'ü Anma, Gençlik ve Spor Bayramı"
        self.assertHolidayName(name_1, (f"{year}-05-19" for year in range(1936, 1981)))
        self.assertHolidayName(name_2, (f"{year}-05-19" for year in range(1981, 2050)))
        self.assertNoHolidayName(name_1, range(1981, 2050))
        self.assertNoHolidayName(name_2, range(1936, 1981))

    def test_freedom_and_constitution_day(self):
        name = "Hürriyet ve Anayasa Bayramı"
        self.assertHolidayName(name, (f"{year}-05-27" for year in range(1963, 1981)))
        self.assertNoHolidayName(name, range(1936, 1963), range(1981, 2050))

    def test_democracy_and_national_unity_day(self):
        name = "Demokrasi ve Millî Birlik Günü"
        self.assertHolidayName(name, (f"{year}-07-15" for year in range(2017, 2050)))
        self.assertNoHolidayName(name, range(1936, 2017))

    def test_victory_day(self):
        self.assertHolidayName("Zafer Bayramı", (f"{year}-08-30" for year in range(1936, 2050)))

    def test_republic_day(self):
        name = "Cumhuriyet Bayramı"
        self.assertHolidayName(name, (f"{year}-10-29" for year in range(1936, 2050)))
        self.assertHolidayName(name, (f"{year}-10-30" for year in range(1936, 1981)))

        self.assertHolidayName(
            f"{name} (saat 13.00'ten)",
            Turkey(categories=HALF_DAY, years=range(1936, 2050)),
            (f"{year}-10-28" for year in range(1936, 2050)),
        )

    def test_eid_al_fitr(self):
        name = "Ramazan Bayramı"
        half_day_holidays = Turkey(categories=HALF_DAY, years=range(1936, 2050))
        for ymd in (
            (2000, 1, 8),
            (2000, 12, 27),
            (2010, 9, 9),
            (2018, 6, 15),
            (2019, 6, 4),
            (2020, 5, 24),
            (2021, 5, 13),
            (2022, 5, 2),
            (2023, 4, 21),
        ):
            dt = date(*ymd)
            self.assertHolidayName(name, dt, _timedelta(dt, +1), _timedelta(dt, +2))
            self.assertHolidayName(
                f"{name} (saat 13.00'ten)", half_day_holidays, _timedelta(dt, -1)
            )

    def test_eid_al_adha(self):
        name = "Kurban Bayramı"
        half_day_holidays = Turkey(categories=HALF_DAY, years=range(1936, 2050))
        for ymd in (
            (2006, 1, 10),
            (2006, 12, 31),
            (2010, 11, 16),
            (2018, 8, 21),
            (2019, 8, 11),
            (2020, 7, 31),
            (2021, 7, 20),
            (2022, 7, 9),
            (2023, 6, 28),
        ):
            dt = date(*ymd)
            self.assertHolidayName(
                name, dt, _timedelta(dt, +1), _timedelta(dt, +2), _timedelta(dt, +3)
            )
            self.assertHolidayName(
                f"{name} (saat 13.00'ten)", half_day_holidays, _timedelta(dt, -1)
            )

    def test_2022(self):
        self.assertHolidays(
            Turkey(years=2022),
            ("2022-01-01", "Yılbaşı"),
            ("2022-04-23", "Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2022-05-01", "Emek ve Dayanışma Günü"),
            ("2022-05-02", "Ramazan Bayramı"),
            ("2022-05-03", "Ramazan Bayramı"),
            ("2022-05-04", "Ramazan Bayramı"),
            ("2022-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2022-07-09", "Kurban Bayramı"),
            ("2022-07-10", "Kurban Bayramı"),
            ("2022-07-11", "Kurban Bayramı"),
            ("2022-07-12", "Kurban Bayramı"),
            ("2022-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2022-08-30", "Zafer Bayramı"),
            ("2022-10-29", "Cumhuriyet Bayramı"),
        )

    def test_2022_half_day(self):
        self.assertHolidays(
            Turkey(categories=HALF_DAY, years=2022),
            ("2022-05-01", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2022-07-08", "Kurban Bayramı (saat 13.00'ten)"),
            ("2022-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Yılbaşı"),
            ("2023-04-20", "Ramazan Bayramı (saat 13.00'ten)"),
            ("2023-04-21", "Ramazan Bayramı"),
            ("2023-04-22", "Ramazan Bayramı"),
            ("2023-04-23", "Ramazan Bayramı; Ulusal Egemenlik ve Çocuk Bayramı"),
            ("2023-05-01", "Emek ve Dayanışma Günü"),
            ("2023-05-19", "Atatürk'ü Anma, Gençlik ve Spor Bayramı"),
            ("2023-06-27", "Kurban Bayramı (saat 13.00'ten)"),
            ("2023-06-28", "Kurban Bayramı"),
            ("2023-06-29", "Kurban Bayramı"),
            ("2023-06-30", "Kurban Bayramı"),
            ("2023-07-01", "Kurban Bayramı"),
            ("2023-07-15", "Demokrasi ve Millî Birlik Günü"),
            ("2023-08-30", "Zafer Bayramı"),
            ("2023-10-28", "Cumhuriyet Bayramı (saat 13.00'ten)"),
            ("2023-10-29", "Cumhuriyet Bayramı"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-04-20", "Eid al-Fitr (from 1pm)"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr; National Sovereignty and Children's Day"),
            ("2023-05-01", "Labour and Solidarity Day"),
            ("2023-05-19", "Commemoration of Atatürk, Youth and Sports Day"),
            ("2023-06-27", "Eid al-Adha (from 1pm)"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-06-30", "Eid al-Adha"),
            ("2023-07-01", "Eid al-Adha"),
            ("2023-07-15", "Democracy and National Unity Day"),
            ("2023-08-30", "Victory Day"),
            ("2023-10-28", "Republic Day (from 1pm)"),
            ("2023-10-29", "Republic Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-04-20", "Рамазан-байрам (з 13:00)"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-22", "Рамазан-байрам"),
            ("2023-04-23", "День національної незалежності та дітей; Рамазан-байрам"),
            ("2023-05-01", "День праці та солідарності"),
            ("2023-05-19", "День вшанування памʼяті Ататюрка, молоді та спорту"),
            ("2023-06-27", "Курбан-байрам (з 13:00)"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Курбан-байрам"),
            ("2023-06-30", "Курбан-байрам"),
            ("2023-07-01", "Курбан-байрам"),
            ("2023-07-15", "День демократії та національної єдності"),
            ("2023-08-30", "День Перемоги"),
            ("2023-10-28", "День Республіки (з 13:00)"),
            ("2023-10-29", "День Республіки"),
        )
