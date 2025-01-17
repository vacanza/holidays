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

from unittest import TestCase

from holidays.constants import BANK
from holidays.countries.sri_lanka import SriLanka, LK, LKA
from tests.common import CommonCountryTests


class TestSriLanka(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SriLanka, years=range(1948, 2050), years_non_observed=range(1948, 2050))

    def test_country_aliases(self):
        self.assertAliases(SriLanka, LK, LKA)

    def test_no_holidays(self):
        self.assertNoHolidays(SriLanka(years=1947))

    def test_thai_pongal(self):
        name = "தைப்பொங்கல்"
        self.assertHolidayName(name, (f"{year}-01-14" for year in range(1949, 2050)))

    def test_magh_puja(self):
        name = "මාඝ පූජා"

        dt = (
            "2022-02-16",
            "2023-03-06",
            "2024-02-24",
            "2025-02-12",
            "2026-03-03",
        )
        self.assertHolidayName(name, dt)

    def test_maha_shivratri(self):
        name = "මහා ශිවාත්‍රි"

        dt = (
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-03-08",
            "2025-02-26",
            "2026-02-15",
            "2027-03-06",
            "2028-02-23",
            "2029-02-11",
            "2030-03-02",
        )
        self.assertHolidayName(name, dt)

    def test_nikini_poya(self):
        name = "නිකිනි පොය"

        dt = (
            "2014-08-10",
            "2015-08-29",
            "2016-08-17",
            "2017-08-07",
            "2018-08-25",
            "2019-08-14",
            "2020-08-03",
            "2021-08-22",
            "2022-08-11",
            "2023-08-30",
            "2024-08-19",
            "2025-08-08",
        )
        self.assertHolidayName(name, dt)

    def test_binara_poya(self):
        name = "බිනර පොය"

        dt = (
            "2016-09-16",
            "2017-09-05",
            "2018-09-24",
            "2019-09-13",
            "2020-09-01",
            "2021-09-20",
            "2022-09-10",
            "2023-09-29",
            "2024-09-17",
            "2025-09-07",
        )
        self.assertHolidayName(name, dt)

    def test_wap_poya(self):
        name = "වප් පොය"

        dt = (
            "2014-10-08",
            "2015-10-27",
            "2016-10-15",
            "2018-10-24",
            "2019-10-13",
            "2020-10-30",
            "2021-10-20",
            "2022-10-09",
            "2023-10-28",
            "2024-10-17",
            "2025-10-06",
        )
        self.assertHolidayName(name, dt)

    def test_il_poya(self):
        name = "ඉල් පොය"

        dt = (
            "2015-09-28",
            "2017-10-05",
            "2019-09-14",
            "2020-10-01",
            "2021-10-20",
            "2023-11-27",
            "2024-11-15",
            "2025-11-03",
        )
        self.assertHolidayName(name, dt)

    def test_unduwap_poya(self):
        name = "උඳුවාප් පොය"

        dt = (
            "2020-12-29",
            "2021-12-18",
            "2022-12-07",
            "2023-12-26",
            "2024-12-14",
            "2025-12-04",
        )
        self.assertHolidayName(name, dt)

    def test_eid_al_fitr(self):
        name = "ඊද් අල්-ෆිතර්"
        self.assertHolidayName(
            name,
            "2014-07-29",
            "2014-07-30",
            "2014-07-31",
            "2015-07-18",
            "2015-07-19",
            "2015-07-20",
            "2016-07-07",
            "2016-07-08",
            "2016-07-09",
            "2017-06-26",
            "2017-06-27",
            "2017-06-28",
            "2018-06-15",
            "2018-06-16",
            "2018-06-17",
            "2019-06-04",
            "2019-06-05",
            "2019-06-06",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2024-04-10",
            "2024-04-11",
            "2024-04-12",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertEqual(set(range(1948, 2050)), years_found)

    def test_eid_al_adha(self):
        name = "ඊද් අල්-අදා"
        self.assertHolidayName(
            name,
            "2014-10-05",
            "2014-10-06",
            "2014-10-07",
            "2015-09-23",
            "2015-09-24",
            "2015-09-25",
            "2016-09-13",
            "2016-09-14",
            "2016-09-15",
            "2017-09-02",
            "2017-09-03",
            "2017-09-04",
            "2018-08-22",
            "2018-08-23",
            "2018-08-24",
            "2019-08-11",
            "2019-08-12",
            "2019-08-13",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertEqual(set(range(1948, 2050)), years_found)

    def test_mawlid(self):
        name = "නබිගේ උපන් දිනය"
        self.assertHolidayName(
            name,
            "2014-01-14",
            "2015-01-03",
            "2015-12-24",
            "2016-12-12",
            "2017-12-01",
            "2018-11-21",
            "2019-11-10",
            "2020-10-29",
            "2021-10-19",
            "2022-10-08",
            "2023-09-27",
            "2024-09-16",
        )
        years_found = {dt.year for dt in self.holidays.get_named(name, lookup="startswith")}
        self.assertEqual(set(range(1948, 2050)), years_found)

    def test_bank_holidays(self):
        holidays = SriLanka(categories=BANK, years=range(1948, 2050))
        self.assertHolidayName(
            "බැංකු නිවාඩු", holidays, (f"{year}-06-30" for year in range(1948, 2050))
        )
        self.assertHolidayName(
            "අලුත් අවුරුදු උදාව", holidays, (f"{year}-12-31" for year in range(1948, 2050))
        )
        self.assertHolidayName(
            "කම්කරු දිනය", holidays, (f"{year}-05-01" for year in range(1956, 2050))
        )

    def test_2021(self):
        self.assertHolidays(
            SriLanka(years=2021),
            ("2021-01-01", "දුරුතු පොය"),
            ("2021-01-14", "தைப்பொங்கல்"),
            ("2021-02-04", "ස්වාධීනත්ව දිනය"),
            ("2021-03-11", "මහා ශිවාත්‍රි"),
            ("2021-04-02", "හොඳ සිකුරාදා"),
            ("2021-04-13", "සිංහල හා දෙමළ අලුත් අවුරුද්දට පෙර දිනය"),
            ("2021-04-14", "සිංහල සහ දෙමළ නව වසර"),
            ("2021-05-13", "ඊද් අල්-ෆිතර්"),
            ("2021-05-14", "ඊද් අල්-ෆිතර්"),
            ("2021-05-15", "ඊද් අල්-ෆිතර්"),
            ("2021-05-26", "වෙසක් පොහොය"),
            ("2021-06-01", "පොසොන් පොහොය"),
            ("2021-07-01", "එසාල පොය"),
            ("2021-07-20", "ඊද් අල්-අදා"),
            ("2021-07-21", "ඊද් අල්-අදා"),
            ("2021-07-22", "ඊද් අල්-අදා"),
            ("2021-08-22", "නිකිනි පොය"),
            ("2021-09-20", "බිනර පොය"),
            ("2021-10-19", "නබිගේ උපන් දිනය"),
            ("2021-10-20", "ඉල් පොය; වප් පොය"),
            ("2021-11-03", "දීපාවලී"),
            ("2021-12-18", "උඳුවාප් පොය"),
            ("2021-12-25", "ක්‍රිස්මස්"),
        )

    def test_l10_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "දුරුතු පොය"),
            ("2022-01-14", "தைப்பொங்கல்"),
            ("2022-02-04", "ස්වාධීනත්ව දිනය"),
            ("2022-02-16", "මාඝ පූජා"),
            ("2022-03-01", "මහා ශිවාත්‍රි"),
            ("2022-04-13", "සිංහල හා දෙමළ අලුත් අවුරුද්දට පෙර දිනය"),
            ("2022-04-14", "සිංහල සහ දෙමළ නව වසර"),
            ("2022-04-15", "හොඳ සිකුරාදා"),
            ("2022-05-01", "ඊද් අල්-ෆිතර්; කම්කරු දිනය"),
            ("2022-05-02", "ඊද් අල්-ෆිතර්"),
            ("2022-05-03", "ඊද් අල්-ෆිතර්"),
            ("2022-05-15", "වෙසක් පොහොය"),
            ("2022-06-01", "පොසොන් පොහොය"),
            ("2022-06-30", "බැංකු නිවාඩු"),
            ("2022-07-01", "එසාල පොය"),
            ("2022-07-09", "ඊද් අල්-අදා"),
            ("2022-07-10", "ඊද් අල්-අදා"),
            ("2022-07-11", "ඊද් අල්-අදා"),
            ("2022-08-11", "නිකිනි පොය"),
            ("2022-09-10", "බිනර පොය"),
            ("2022-10-08", "නබිගේ උපන් දිනය"),
            ("2022-10-09", "වප් පොය"),
            ("2022-10-23", "දීපාවලී"),
            ("2022-12-07", "උඳුවාප් පොය"),
            ("2022-12-25", "ක්‍රිස්මස්"),
            ("2022-12-31", "අලුත් අවුරුදු උදාව"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Duruthu Poya"),
            ("2022-01-14", "Thai Pongal"),
            ("2022-02-04", "Independence Day"),
            ("2022-02-16", "Magh Puja"),
            ("2022-03-01", "Maha Shivatri"),
            ("2022-04-13", "Day before Sinhala and Tamil New Year"),
            ("2022-04-14", "Sinhala and Tamil New Year"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Eid al-Fitr; Labor Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-05-15", "Vesak Poya"),
            ("2022-06-01", "Poson Poya"),
            ("2022-06-30", "Bank Holidays"),
            ("2022-07-01", "Esala Poya"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-11", "Eid al-Adha"),
            ("2022-08-11", "Nikini Poya"),
            ("2022-09-10", "Binara Poya"),
            ("2022-10-08", "The Prophet's Birthday"),
            ("2022-10-09", "Wap Poya"),
            ("2022-10-23", "Deepavali"),
            ("2022-12-07", "Unduwap Poya"),
            ("2022-12-25", "Christmas"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_ta_lk(self):
        self.assertLocalizedHolidays(
            "ta_LK",
            ("2022-01-01", "துருது போயா"),
            ("2022-01-14", "தைப்பொங்கல்"),
            ("2022-02-04", "சுதந்திர தினம்"),
            ("2022-02-16", "மாக் பூஜை"),
            ("2022-03-01", "மகா சிவத்ரி"),
            ("2022-04-13", "சிங்கள, தமிழ் புத்தாண்டுக்கு முன்னைய தினம்"),
            ("2022-04-14", "சிங்கள, தமிழ் புத்தாண்டு நிகழ்வுகள்"),
            ("2022-04-15", "புனித வெள்ளி"),
            ("2022-05-01", "ஈதுல் பித்ர்; தொழிலாளர் தினம்"),
            ("2022-05-02", "ஈதுல் பித்ர்"),
            ("2022-05-03", "ஈதுல் பித்ர்"),
            ("2022-05-15", "வெசாக் போயா"),
            ("2022-06-01", "போசன் போயா"),
            ("2022-06-30", "வங்கி விடுமுறைகள்"),
            ("2022-07-01", "எசல போயா"),
            ("2022-07-09", "ஈதுல் அதா"),
            ("2022-07-10", "ஈதுல் அதா"),
            ("2022-07-11", "ஈதுல் அதா"),
            ("2022-08-11", "நிகினி போயா"),
            ("2022-09-10", "பினாரா போயா"),
            ("2022-10-08", "நபியின் பிறந்த நாள்"),
            ("2022-10-09", "வாப் போயா"),
            ("2022-10-23", "தீபாவளி"),
            ("2022-12-07", "உந்துவாப் போயா"),
            ("2022-12-25", "நத்தார்"),
            ("2022-12-31", "புத்தாண்டு கொண்டாட்டம்"),
        )
