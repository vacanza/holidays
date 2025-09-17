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

from holidays.countries.myanmar import Myanmar, MM, MMR
from tests.common import CommonCountryTests


class TestMyanmar(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1948, 2050)
        super().setUpClass(Myanmar, years=years)
        cls.no_estimated_holidays = Myanmar(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(Myanmar, MM, MMR)

    def test_no_holidays(self):
        self.assertNoHolidays(Myanmar(years=1947))

    def test_new_years_day(self):
        name = "နိုင်ငံတကာနှစ်သစ်ကူးနေ့"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1948, 2025))

    def test_independence_day(self):
        self.assertHolidayName("လွတ်လပ်ရေးနေ့", (f"{year}-01-04" for year in range(1948, 2050)))

    def test_union_day(self):
        self.assertHolidayName("ပြည်ထောင်စုနေ့", (f"{year}-02-12" for year in range(1948, 2050)))

    def test_peasants_day(self):
        self.assertHolidayName("တောင်သူလယ်သမားနေ့", (f"{year}-03-02" for year in range(1948, 2050)))

    def test_armed_forces_day(self):
        self.assertHolidayName("တော်လှန်ရေးနေ့", (f"{year}-03-27" for year in range(1948, 2050)))

    def test_may_day(self):
        self.assertHolidayName("မေဒေးနေ့", (f"{year}-05-01" for year in range(1948, 2050)))

    def test_martyrs_day(self):
        self.assertHolidayName("အာဇာနည်နေ့", (f"{year}-07-19" for year in range(1948, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("ခရစ္စမတ်နေ့", (f"{year}-12-25" for year in range(1948, 2050)))

    def test_eid_al_adha(self):
        name = "အီဒုလ်အဿွဟာနေ့"
        self.assertHolidayName(
            name,
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1948, 2050))

    def test_chinese_new_year(self):
        name = "တရုတ်နှစ်သစ်ကူးနေ့"
        self.assertHolidayName(
            name,
            "2025-01-29",
        )
        self.assertHolidayName(name, range(2025, 2050))
        self.assertNoHolidayName(name, range(1948, 2025))

    def test_myanmar_new_year(self):
        name = "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"
        self.assertHolidayName(
            name,
            "2021-04-13",
            "2021-04-14",
            "2021-04-15",
            "2021-04-16",
            "2022-04-09",
            "2022-04-10",
            "2022-04-11",
            "2022-04-12",
            "2022-04-13",
            "2022-04-14",
            "2022-04-15",
            "2022-04-16",
            "2023-04-09",
            "2023-04-10",
            "2023-04-11",
            "2023-04-12",
            "2023-04-13",
            "2023-04-14",
            "2023-04-15",
            "2023-04-16",
            "2024-04-13",
            "2024-04-14",
            "2024-04-15",
            "2024-04-16",
            "2024-04-17",
            "2024-04-18",
            "2024-04-19",
            "2024-04-20",
            "2024-04-21",
            "2025-04-13",
            "2025-04-14",
            "2025-04-15",
            "2025-04-16",
            "2025-04-17",
            "2025-04-18",
            "2025-04-19",
            "2025-04-20",
            "2025-04-21",
        )

        self.assertHolidayNameCount(
            name, 4, range(2011, 2004), range(2005, 2007), range(2017, 2020), 2021
        )
        self.assertHolidayNameCount(name, 5, 2004, 2020)
        self.assertHolidayNameCount(name, 10, range(2007, 2017))
        self.assertHolidayNameCount(name, 8, 2022, 2023)
        self.assertHolidayNameCount(name, 9, range(2024, 2050))

    def test_full_moon_day_of_tabaung(self):
        name = "တပေါင်းလပြည့်နေ့"
        self.assertHolidayName(
            name,
            "2020-03-08",
            "2021-03-27",
            "2022-03-16",
            "2023-03-05",
            "2024-03-24",
            "2025-03-13",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_full_moon_day_of_kason(self):
        name = "ကဆုန်လပြည့်နေ့"
        self.assertHolidayName(
            name,
            "2020-05-06",
            "2021-05-25",
            "2022-05-14",
            "2023-05-03",
            "2024-05-22",
            "2025-05-11",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_full_moon_day_of_waso(self):
        name = "ဝါတွင်းသုံးလ စတင်ခြင်း"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-07-23",
            "2022-07-12",
            "2023-08-01",
            "2024-07-20",
            "2025-07-09",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_thadingyut_holiday(self):
        name = "သီတင်းကျွတ်လပြည့်နေ့"
        self.assertHolidayName(
            name,
            "2020-10-30",
            "2020-10-31",
            "2020-11-01",
            "2021-10-19",
            "2021-10-20",
            "2021-10-21",
            "2022-10-08",
            "2022-10-09",
            "2022-10-10",
            "2023-10-28",
            "2023-10-29",
            "2023-10-30",
            "2024-10-16",
            "2024-10-17",
            "2024-10-18",
            "2025-10-05",
            "2025-10-06",
            "2025-10-07",
        )
        self.assertHolidayName(name, range(1948, 2050))
        self.assertHolidayNameCount(name, 3, range(1948, 2050))

    def test_diwali(self):
        name = "ဒီပါဝလီနေ့"
        self.assertHolidayName(
            name,
            "2020-11-15",
            "2021-11-04",
            "2022-10-24",
            "2023-11-13",
            "2024-11-01",
            "2025-10-21",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_full_moon_day_of_tazaungmon(self):
        name = "တန်ဆောင်တိုင်ပိတ်ရက်များ"
        self.assertHolidayName(
            name,
            "2020-11-29",
            "2021-11-18",
            "2022-11-07",
            "2023-11-27",
            "2024-11-15",
            "2025-11-04",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_national_day(self):
        name = "အမျိုးသားနေ့"
        self.assertHolidayName(
            name,
            "2020-12-09",
            "2021-11-28",
            "2022-11-17",
            "2023-12-07",
            "2024-11-25",
            "2025-11-14",
        )
        self.assertHolidayName(name, range(1948, 2050))

    def test_karen_new_year(self):
        name = "ကရင်နှစ်သစ်ကူးနေ့"
        self.assertHolidayName(
            name,
            "2019-01-06",
            "2019-12-26",
            "2021-01-13",
            "2022-01-02",
            "2022-12-22",
            "2024-01-11",
            "2024-12-30",
            "2025-12-19",
        )

    def test_2024(self):
        self.assertHolidays(
            Myanmar(years=2024),
            ("2024-01-04", "လွတ်လပ်ရေးနေ့"),
            ("2024-01-11", "ကရင်နှစ်သစ်ကူးနေ့"),
            ("2024-02-12", "ပြည်ထောင်စုနေ့"),
            ("2024-03-02", "တောင်သူလယ်သမားနေ့"),
            ("2024-03-24", "တပေါင်းလပြည့်နေ့"),
            ("2024-03-27", "တော်လှန်ရေးနေ့"),
            ("2024-04-13", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-14", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-15", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-16", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-17", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-18", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-19", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-20", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-04-21", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2024-05-01", "မေဒေးနေ့"),
            ("2024-05-22", "ကဆုန်လပြည့်နေ့"),
            ("2024-06-17", "အီဒုလ်အဿွဟာနေ့"),
            ("2024-07-19", "အာဇာနည်နေ့"),
            ("2024-07-20", "ဝါတွင်းသုံးလ စတင်ခြင်း"),
            ("2024-10-16", "သီတင်းကျွတ်လပြည့်နေ့"),
            ("2024-10-17", "သီတင်းကျွတ်လပြည့်နေ့"),
            ("2024-10-18", "သီတင်းကျွတ်လပြည့်နေ့"),
            ("2024-11-01", "ဒီပါဝလီနေ့"),
            ("2024-11-15", "တန်ဆောင်တိုင်ပိတ်ရက်များ"),
            ("2024-11-25", "အမျိုးသားနေ့"),
            ("2024-12-25", "ခရစ္စမတ်နေ့"),
            ("2024-12-30", "ကရင်နှစ်သစ်ကူးနေ့"),
            ("2024-12-31", "အလုပ်ပိတ်ရက် (11-01-2025 မှ ပြန်လဲထားသည်)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "နိုင်ငံတကာနှစ်သစ်ကူးနေ့"),
            ("2025-01-04", "လွတ်လပ်ရေးနေ့"),
            ("2025-01-29", "တရုတ်နှစ်သစ်ကူးနေ့"),
            ("2025-02-12", "ပြည်ထောင်စုနေ့"),
            ("2025-03-02", "တောင်သူလယ်သမားနေ့"),
            ("2025-03-12", "အလုပ်ပိတ်ရက် (22-03-2025 မှ ပြန်လဲထားသည်)"),
            ("2025-03-13", "တပေါင်းလပြည့်နေ့"),
            ("2025-03-14", "အလုပ်ပိတ်ရက် (29-03-2025 မှ ပြန်လဲထားသည်)"),
            ("2025-03-27", "တော်လှန်ရေးနေ့"),
            ("2025-04-13", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-14", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-15", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-16", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-17", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-18", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-19", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-20", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-04-21", "မြန်မာနှစ်သစ်ကူး ရုံးပိတ်ရက်များ"),
            ("2025-05-01", "မေဒေးနေ့"),
            ("2025-05-11", "ကဆုန်လပြည့်နေ့"),
            ("2025-06-07", "အီဒုလ်အဿွဟာနေ့"),
            ("2025-07-09", "ဝါတွင်းသုံးလ စတင်ခြင်း"),
            ("2025-07-19", "အာဇာနည်နေ့"),
            ("2025-10-05", "သီတင်းကျွတ်လပြည့်နေ့"),
            ("2025-10-06", "သီတင်းကျွတ်လပြည့်နေ့"),
            ("2025-10-07", "သီတင်းကျွတ်လပြည့်နေ့"),
            ("2025-10-21", "ဒီပါဝလီနေ့"),
            ("2025-11-03", "အလုပ်ပိတ်ရက် (08-11-2025 မှ ပြန်လဲထားသည်)"),
            ("2025-11-04", "တန်ဆောင်တိုင်ပိတ်ရက်များ"),
            ("2025-11-14", "အမျိုးသားနေ့"),
            ("2025-12-19", "ကရင်နှစ်သစ်ကူးနေ့"),
            ("2025-12-25", "ခရစ္စမတ်နေ့"),
            ("2025-12-26", "အလုပ်ပိတ်ရက် (03-01-2026 မှ ပြန်လဲထားသည်)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-04", "Independence Day"),
            ("2025-01-29", "Chinese New Year"),
            ("2025-02-12", "Union Day"),
            ("2025-03-02", "Peasants' Day"),
            ("2025-03-12", "Day off (substituted from 03/22/2025)"),
            ("2025-03-13", "Full Moon Day of Tabaung"),
            ("2025-03-14", "Day off (substituted from 03/29/2025)"),
            ("2025-03-27", "Armed Forces Day"),
            ("2025-04-13", "Myanmar New Year"),
            ("2025-04-14", "Myanmar New Year"),
            ("2025-04-15", "Myanmar New Year"),
            ("2025-04-16", "Myanmar New Year"),
            ("2025-04-17", "Myanmar New Year"),
            ("2025-04-18", "Myanmar New Year"),
            ("2025-04-19", "Myanmar New Year"),
            ("2025-04-20", "Myanmar New Year"),
            ("2025-04-21", "Myanmar New Year"),
            ("2025-05-01", "May Day"),
            ("2025-05-11", "Full Moon Day of Kason"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-07-09", "Full Moon Day of Waso"),
            ("2025-07-19", "Martyrs' Day"),
            ("2025-10-05", "Thadingyut Holiday"),
            ("2025-10-06", "Thadingyut Holiday"),
            ("2025-10-07", "Thadingyut Holiday"),
            ("2025-10-21", "Diwali"),
            ("2025-11-03", "Day off (substituted from 11/08/2025)"),
            ("2025-11-04", "Full Moon Day of Tazaungmon"),
            ("2025-11-14", "National Day"),
            ("2025-12-19", "Karen New Year"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day off (substituted from 01/03/2026)"),
        )
