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

from holidays.constants import BANK, GOVERNMENT, PUBLIC, WORKDAY
from holidays.countries.sri_lanka import SriLanka, LK, LKA
from tests.common import CommonCountryTests


class TestSriLanka(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SriLanka, years=range(2003, 2025))

    def test_country_aliases(self):
        self.assertAliases(SriLanka, LK, LKA)

    def test_no_holidays(self):
        self.assertNoHolidays(
            SriLanka(years=(2002, 2026), categories=(BANK, GOVERNMENT, PUBLIC, WORKDAY))
        )

    def test_special(self):
        self.assertHoliday(
            # 2020 Covid-19 Lockdowns.
            "2020-03-16",
            "2020-03-17",
            "2020-03-18",
            "2020-03-19",
            # Other Special Public Holidays.
            "2012-05-07",
            "2013-04-15",
            "2016-04-15",
            "2019-05-20",
            "2022-04-11",
            "2022-04-12",
            "2022-05-02",
            "2024-04-15",
            "2024-09-29",
            # Adhi [MONTH] Full Moon Day.
            "2004-07-31",
            "2007-05-31",
            "2010-04-28",
            "2012-08-31",
            "2015-07-01",
            "2018-05-29",
            "2020-10-01",
            "2023-07-03",
        )

    def test_special_bank(self):
        dt = (
            # Special Bank Holidays.
            "2005-05-02",
            "2005-12-26",
            "2007-02-05",
            "2007-04-03",
            "2008-04-18",
            "2011-05-02",
            "2011-12-26",
            "2012-01-16",
            "2012-02-10",
            "2012-05-07",
            "2013-04-15",
            "2014-04-15",
            "2015-01-05",
            "2016-05-02",
            "2016-05-23",
            "2016-12-26",
            "2018-01-15",
            "2018-02-05",
            "2019-04-15",
            # 2019-05-20 got upgraded to Special Public Holiday.
            "2019-11-11",
            "2020-04-14",
            # 2022-05-02 got upgraded to Special Public Holiday.
            "2022-10-10",
            "2022-12-26",
            "2023-01-16",
            "2025-04-15",
        )
        dt_half = (
            # Half-Day Special Bank Holidays.
            "2021-04-30",
            "2021-12-24",
        )
        self.assertHoliday(SriLanka(categories=BANK), dt, dt_half)

    def test_special_government(self):
        # 2020 Covid Lockdowns
        # https://www.adaderana.lk/news.php?nid=64367
        # 2022 Sri Lankan Fuel Crisis
        # https://www.adaderana.lk/news.php?nid=82979
        # https://www.adaderana.lk/news.php?nid=83082
        # https://www.adaderana.lk/news.php?nid=84035
        self.assertHoliday(
            SriLanka(categories=GOVERNMENT),
            "2020-06-04",
            "2022-06-13",
            "2022-06-17",
            "2022-06-24",
            "2022-07-01",
            "2022-07-08",
            "2022-07-15",
            "2022-07-22",
            "2022-07-29",
        )

    def test_special_workday(self):
        # 2003 Deepavali.
        self.assertHoliday(SriLanka(categories=WORKDAY), "2003-10-24")

    def test_deepavali(self):
        name = "දීපවාලි උත්සව දිනය"
        self.assertHolidayName(
            name,
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertNoHolidayName(name, 2003)

    def test_2023_all(self):
        # https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2023
        self.assertHolidays(
            SriLanka(categories=(BANK, GOVERNMENT, PUBLIC, WORKDAY), years=2023),
            ("2023-01-06", "දුරුතු පුර පසළොස්වක පෝය දිනය"),
            ("2023-01-15", "දෙමළ තෛපොංැලල් දිනය"),
            ("2023-01-16", "විශේෂ බැංකු නිවාඩු දිනය"),
            ("2023-02-04", "නිදහස් සමරු දිනය"),
            ("2023-02-05", "නවම් පුර පසළොස්වක පෝය දිනය"),
            ("2023-02-18", "මහ සිවරාත්රි දිනය"),
            ("2023-03-06", "මැදින් පුර පසළොස්වක පෝය දිනය"),
            ("2023-04-05", "බක් පුර පසළොස්වක පෝය දිනය"),
            ("2023-04-07", "මහ සිකුරාදා දිනය"),
            ("2023-04-13", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය"),
            ("2023-04-14", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනය"),
            ("2023-04-22", "ඊදුල් ෆීතර්"),
            ("2023-05-01", "ලොක කම්කරු දිනය"),
            ("2023-05-05", "වෙසක් පුර පසළොස්වක පෝය දිනය"),
            ("2023-05-06", "වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය"),
            ("2023-06-03", "පොසොන් පුර පසළොස්වක පෝය දිනය"),
            ("2023-06-29", "ඊදුල් අල්හා"),
            ("2023-07-03", "අධි ඇසල පුර පසළොස්වක පෝය දිනය"),
            ("2023-08-01", "ඇසල පුර පසළොස්වක පෝය දිනය"),
            ("2023-08-30", "නිකිණි පුර පසළොස්වක පෝය දිනය"),
            ("2023-09-28", "නබි නායකතුමාගේ උපන් දිනය"),
            ("2023-09-29", "බිනර පුර පසළොස්වක පෝය දිනය"),
            ("2023-10-28", "වප් පුර පසළොස්වක පෝය දිනය"),
            ("2023-11-12", "දීපවාලි උත්සව දිනය"),
            ("2023-11-26", "ඉල් පුර පසළොස්වක පෝය දිනය"),
            ("2023-12-25", "නත්තල් උත්සව දිනය"),
            ("2023-12-26", "උඳුවප් පුර පසළොස්වක පෝය දිනය"),
        )

    def test_2024_all(self):
        # https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2024
        self.assertHolidays(
            SriLanka(categories=(BANK, GOVERNMENT, PUBLIC, WORKDAY), years=2024),
            ("2024-01-15", "දෙමළ තෛපොංැලල් දිනය"),
            ("2024-01-25", "දුරුතු පුර පසළොස්වක පෝය දිනය"),
            ("2024-02-04", "නිදහස් සමරු දිනය"),
            ("2024-02-23", "නවම් පුර පසළොස්වක පෝය දිනය"),
            ("2024-03-08", "මහ සිවරාත්රි දිනය"),
            ("2024-03-24", "මැදින් පුර පසළොස්වක පෝය දිනය"),
            ("2024-03-29", "මහ සිකුරාදා දිනය"),
            ("2024-04-11", "ඊදුල් ෆීතර්"),
            ("2024-04-12", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය"),
            ("2024-04-13", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනය"),
            ("2024-04-15", "විශේෂ රජයේ නිවාඩු දිනය"),
            ("2024-04-23", "බක් පුර පසළොස්වක පෝය දිනය"),
            ("2024-05-01", "ලොක කම්කරු දිනය"),
            ("2024-05-23", "වෙසක් පුර පසළොස්වක පෝය දිනය"),
            ("2024-05-24", "වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය"),
            ("2024-06-17", "ඊදුල් අල්හා"),
            ("2024-06-21", "පොසොන් පුර පසළොස්වක පෝය දිනය"),
            ("2024-07-20", "ඇසල පුර පසළොස්වක පෝය දිනය"),
            ("2024-08-19", "නිකිණි පුර පසළොස්වක පෝය දිනය"),
            ("2024-09-16", "නබි නායකතුමාගේ උපන් දිනය"),
            ("2024-09-17", "බිනර පුර පසළොස්වක පෝය දිනය"),
            ("2024-09-29", "විශේෂ රජයේ නිවාඩු දිනය"),
            ("2024-10-17", "වප් පුර පසළොස්වක පෝය දිනය"),
            ("2024-10-31", "දීපවාලි උත්සව දිනය"),
            ("2024-11-15", "ඉල් පුර පසළොස්වක පෝය දිනය"),
            ("2024-12-14", "උඳුවප් පුර පසළොස්වක පෝය දිනය"),
            ("2024-12-25", "නත්තල් උත්සව දිනය"),
        )

    def test_l10_default(self):
        # https://www.cbsl.gov.lk/en/about/about-the-bank/bank-holidays-2025
        self.assertLocalizedHolidays(
            ("2022-01-14", "දෙමළ තෛපොංැලල් දිනය"),
            ("2022-01-17", "දුරුතු පුර පසළොස්වක පෝය දිනය"),
            ("2022-02-04", "නිදහස් සමරු දිනය"),
            ("2022-02-16", "නවම් පුර පසළොස්වක පෝය දිනය"),
            ("2022-03-01", "මහ සිවරාත්රි දිනය"),
            ("2022-03-17", "මැදින් පුර පසළොස්වක පෝය දිනය"),
            ("2022-04-11", "විශේෂ රජයේ නිවාඩු දිනය"),
            ("2022-04-12", "විශේෂ රජයේ නිවාඩු දිනය"),
            ("2022-04-13", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය"),
            ("2022-04-14", "සිංහල හා දෙමළ අලුත් අවුරුදු දිනය"),
            ("2022-04-15", "මහ සිකුරාදා දිනය"),
            ("2022-04-16", "බක් පුර පසළොස්වක පෝය දිනය"),
            ("2022-05-01", "ලොක කම්කරු දිනය"),
            ("2022-05-02", "විශේෂ රජයේ නිවාඩු දිනය"),
            ("2022-05-03", "ඊදුල් ෆීතර්"),
            ("2022-05-15", "වෙසක් පුර පසළොස්වක පෝය දිනය"),
            ("2022-05-16", "වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය"),
            ("2022-06-13", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-06-14", "පොසොන් පුර පසළොස්වක පෝය දිනය"),
            ("2022-06-17", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-06-24", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-07-01", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-07-08", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-07-10", "ඊදුල් අල්හා"),
            ("2022-07-13", "ඇසල පුර පසළොස්වක පෝය දිනය"),
            ("2022-07-15", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-07-22", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-07-29", "රාජ්ය අංශයේ නිවාඩු දිනය"),
            ("2022-08-11", "නිකිණි පුර පසළොස්වක පෝය දිනය"),
            ("2022-09-10", "බිනර පුර පසළොස්වක පෝය දිනය"),
            ("2022-10-09", "නබි නායකතුමාගේ උපන් දිනය; වප් පුර පසළොස්වක පෝය දිනය"),
            ("2022-10-10", "විශේෂ බැංකු නිවාඩු දිනය"),
            ("2022-10-24", "දීපවාලි උත්සව දිනය"),
            ("2022-11-07", "ඉල් පුර පසළොස්වක පෝය දිනය"),
            ("2022-12-07", "උඳුවප් පුර පසළොස්වක පෝය දිනය"),
            ("2022-12-25", "නත්තල් උත්සව දිනය"),
            ("2022-12-26", "විශේෂ බැංකු නිවාඩු දිනය"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-14", "Tamil Thai Pongal Day"),
            ("2022-01-17", "Duruthu Full Moon Poya Day"),
            ("2022-02-04", "Independence Day"),
            ("2022-02-16", "Nawam Full Moon Poya Day"),
            ("2022-03-01", "Maha Sivarathri Day"),
            ("2022-03-17", "Medin Full Moon Poya Day"),
            ("2022-04-11", "Special Public Holiday"),
            ("2022-04-12", "Special Public Holiday"),
            ("2022-04-13", "Day Before Sinhala and Tamil New Year"),
            ("2022-04-14", "Sinhala and Tamil New Year"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Bak Full Moon Poya Day"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-02", "Special Public Holiday"),
            ("2022-05-03", "Eid al-Fitr"),
            ("2022-05-15", "Vesak Full Moon Poya Day"),
            ("2022-05-16", "Day Following Vesak Full Moon Poya Day"),
            ("2022-06-13", "Public Sector Holiday"),
            ("2022-06-14", "Poson Full Moon Poya Day"),
            ("2022-06-17", "Public Sector Holiday"),
            ("2022-06-24", "Public Sector Holiday"),
            ("2022-07-01", "Public Sector Holiday"),
            ("2022-07-08", "Public Sector Holiday"),
            ("2022-07-10", "Eid al-Adha"),
            ("2022-07-13", "Esala Full Moon Poya Day"),
            ("2022-07-15", "Public Sector Holiday"),
            ("2022-07-22", "Public Sector Holiday"),
            ("2022-07-29", "Public Sector Holiday"),
            ("2022-08-11", "Nikini Full Moon Poya Day"),
            ("2022-09-10", "Binara Full Moon Poya Day"),
            ("2022-10-09", "The Prophet's Birthday; Vap Full Moon Poya Day"),
            ("2022-10-10", "Special Bank Holiday"),
            ("2022-10-24", "Deepavali Festival Day"),
            ("2022-11-07", "Il Full Moon Poya Day"),
            ("2022-12-07", "Unduvap Full Moon Poya Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Special Bank Holiday"),
        )

    def test_l10n_ta_lk(self):
        self.assertLocalizedHolidays(
            "ta_LK",
            ("2022-01-14", "தமிழ் தைப்பொங்கல் தினம்"),
            ("2022-01-17", "துருத்து முழு நோன்மதி தினம்"),
            ("2022-02-04", "சுதந்திர தினம்"),
            ("2022-02-16", "நவம் முழு நோன்மதி தினம்"),
            ("2022-03-01", "மகா சிவராத்திரி தினம்"),
            ("2022-03-17", "மெதின் முழு நோன்மதி தினம்"),
            ("2022-04-11", "விசேட பொது விடுமுறை"),
            ("2022-04-12", "விசேட பொது விடுமுறை"),
            ("2022-04-13", "சிங்கள, தமிழ் புத்தாண்டிற்கு முன்னைய தினம்"),
            ("2022-04-14", "சிங்கள, தமிழ் புத்தாண்டு தினம்"),
            ("2022-04-15", "பெரிய வெள்ளிக்கிழமை"),
            ("2022-04-16", "பக் முழு நோன்மதி தினம்"),
            ("2022-05-01", "சர்வதேச தொழிலாளர்கள் தினம்"),
            ("2022-05-02", "விசேட பொது விடுமுறை"),
            ("2022-05-03", "ஈதுல் பித்ர்"),
            ("2022-05-15", "வெசாக் முழு நோன்மதி தினம்"),
            ("2022-05-16", "வெசாக் முழு நோன்மதி தினத்திற்கு அடுத்த நாள்"),
            ("2022-06-13", "பொதுத்துறை விடுமுறை"),
            ("2022-06-14", "பொசொன் முழு நோன்மதி தினம்"),
            ("2022-06-17", "பொதுத்துறை விடுமுறை"),
            ("2022-06-24", "பொதுத்துறை விடுமுறை"),
            ("2022-07-01", "பொதுத்துறை விடுமுறை"),
            ("2022-07-08", "பொதுத்துறை விடுமுறை"),
            ("2022-07-10", "ஈதுல் அழ்ஹா"),
            ("2022-07-13", "எசல முழு நோன்மதி தினம்"),
            ("2022-07-15", "பொதுத்துறை விடுமுறை"),
            ("2022-07-22", "பொதுத்துறை விடுமுறை"),
            ("2022-07-29", "பொதுத்துறை விடுமுறை"),
            ("2022-08-11", "நிக்கினி முழு நோன்மதி தினம்"),
            ("2022-09-10", "பினர முழு நோன்மதி தினம்"),
            ("2022-10-09", "நபிகள் நாயகத்தின் பிறந்த தினம்; வப் முழு நோன்மதி தினம்"),
            ("2022-10-10", "விசேட வங்கி விடுமுறை"),
            ("2022-10-24", "தீபாவளிப் பண்டிகை தினம்"),
            ("2022-11-07", "இல் முழு நோன்மதி தினம்"),
            ("2022-12-07", "உந்துவப் முழு நோன்மதி தினம்"),
            ("2022-12-25", "நத்தார் பண்டிகை"),
            ("2022-12-26", "விசேட வங்கி விடுமுறை"),
        )
