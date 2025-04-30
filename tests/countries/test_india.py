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

import warnings
from unittest import TestCase

from holidays.constants import OPTIONAL
from holidays.countries.india import India, IN, IND
from tests.common import CommonCountryTests


class TestIndia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(India)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore")

    def test_country_aliases(self):
        self.assertAliases(India, IN, IND)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_2018(self):
        self.assertHolidayDates(
            India(years=2018),
            "2018-01-26",
            "2018-02-13",
            "2018-03-29",
            "2018-03-30",
            "2018-04-30",
            "2018-06-16",
            "2018-08-15",
            "2018-08-22",
            "2018-09-03",
            "2018-09-21",
            "2018-10-02",
            "2018-10-19",
            "2018-11-07",
            "2018-11-21",
            "2018-11-23",
            "2018-12-25",
        )

        subdiv_holidays_mapping = {
            "AN": ("2018-04-14",),
            "AP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "AS": (
                "2018-01-14",
                "2018-12-02",
            ),
            "BR": (
                "2018-03-22",
                "2018-04-14",
                "2018-11-13",
            ),
            "CG": (
                "2018-04-14",
                "2018-11-01",
            ),
            "CH": ("2018-04-14",),
            "DL": ("2018-11-13",),
            "GA": (
                "2018-04-14",
                "2018-12-19",
            ),
            "GJ": (
                "2018-01-14",
                "2018-04-14",
                "2018-05-01",
                "2018-10-31",
            ),
            "HP": (
                "2018-04-14",
                "2018-04-15",
            ),
            "HR": (
                "2018-04-14",
                "2018-11-01",
            ),
            "JH": (
                "2018-04-14",
                "2018-11-13",
                "2018-11-15",
            ),
            "JK": ("2018-04-14",),
            "KA": (
                "2018-04-14",
                "2018-11-01",
            ),
            "KL": (
                "2018-04-14",
                "2018-08-24",
                "2018-11-01",
            ),
            "LA": ("2018-04-14",),
            "MH": (
                "2018-02-19",
                "2018-03-18",
                "2018-04-14",
                "2018-05-01",
            ),
            "MP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "MZ": ("2018-02-20",),
            "NL": ("2018-12-01",),
            "OD": (
                "2018-04-01",
                "2018-04-14",
                "2018-04-15",
            ),
            "PB": (
                "2018-01-13",
                "2018-04-14",
                "2018-11-01",
            ),
            "PY": (
                "2018-04-14",
                "2018-08-16",
                "2018-11-01",
            ),
            "RJ": (
                "2018-03-30",
                "2018-04-14",
                "2018-06-15",
            ),
            "SK": (
                "2018-04-14",
                "2018-05-16",
            ),
            "TN": (
                "2018-01-14",
                "2018-01-15",
                "2018-01-16",
                "2018-04-14",
            ),
            "TS": (
                "2018-04-14",
                "2018-06-02",
                "2018-10-06",
            ),
            "UK": ("2018-04-14",),
            "UP": (
                "2018-01-24",
                "2018-04-14",
                "2018-11-13",
            ),
            "WB": (
                "2018-04-14",
                "2018-04-15",
                "2018-05-09",
            ),
        }

        for subdiv, holidays in subdiv_holidays_mapping.items():
            self.assertHoliday(India(subdiv=subdiv), holidays)

    def test_2018_optional(self):
        self.assertHolidayDates(
            India(categories=OPTIONAL, years=2018),
            "2018-01-14",
            "2018-03-02",
            "2018-03-25",
            "2018-04-01",
            "2018-05-01",
            "2018-08-26",
            "2018-09-13",
            "2018-10-10",
            "2018-10-18",
            "2018-11-08",
            "2018-11-14",
        )

    def test_ranged_holidays(self):
        warnings.simplefilter("always")
        for year in (2000, 2036):  # Holidays out of range.
            with self.assertWarns(Warning):
                India(years=year)

        name = "Bakrid"
        dt = (
            "2001-03-06",
            "2010-11-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, dt)

        name = "Buddha Purnima"
        dt = (
            "2001-04-30",
            "2010-05-27",
            "2025-05-12",
            "2035-05-22",
        )
        self.assertHolidayName(name, dt)

        name = "Diwali"
        dt = (
            "2001-11-14",
            "2010-11-05",
            "2025-10-20",
            "2035-10-30",
        )
        self.assertHolidayName(name, dt)

        name = "Dussehra"
        dt = (
            "2001-10-26",
            "2010-10-17",
            "2025-10-02",
            "2035-10-11",
        )
        self.assertHolidayName(name, dt)

        name = "Guru Nanak Jayanti"
        dt = (
            "2001-11-30",
            "2010-11-21",
            "2025-11-05",
            "2035-11-15",
        )
        self.assertHolidayName(name, dt)

        name = "Id-ul-Fitr"
        dt = (
            "2001-12-17",
            "2010-09-10",
            "2025-03-31",
        )
        self.assertHolidayName(name, dt)

        name = "Janmashtami"
        dt = (
            "2001-08-12",
            "2010-09-02",
            "2025-08-16",
            "2035-08-26",
        )
        self.assertHolidayName(name, dt)

        name = "Mahavir Jayanti"
        dt = (
            "2001-04-06",
            "2010-04-28",
            "2025-04-10",
            "2035-04-20",
        )
        self.assertHolidayName(name, dt)

        name = "Maha Shivaratri"
        dt = (
            "2001-02-21",
            "2010-02-12",
            "2025-02-26",
            "2035-03-08",
        )
        self.assertHolidayName(name, dt)

        name = "Milad-un-Nabi"
        dt = (
            "2001-06-05",
            "2010-02-27",
            "2025-09-05",
        )
        self.assertHolidayName(name, dt)

        name = "Muharram"
        dt = (
            "2001-04-04",
            "2010-12-17",
            "2025-07-06",
        )
        self.assertHolidayName(name, dt)

    def test_ranged_subdiv_holidays(self):
        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        name = "Magh Bihu"
        for subdiv in India.subdivisions:
            if subdiv in {"AS"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        name = "Uttarayan"
        for subdiv in India.subdivisions:
            if subdiv in {"GJ"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-11-21",
            "2010-11-11",
            "2025-10-28",
            "2035-11-06",
        )
        name = "Chhath Puja"
        for subdiv in India.subdivisions:
            if subdiv in {"BR", "DL", "JH", "UP"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-08-31",
            "2010-08-23",
            "2025-09-05",
            "2035-09-14",
        )
        name = "Onam"
        for subdiv in India.subdivisions:
            if subdiv in {"KL"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-03-26",
            "2010-03-16",
            "2025-03-30",
            "2035-04-09",
        )
        name = "Gudi Padwa"
        for subdiv in India.subdivisions:
            if subdiv in {"MH"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-01-02",
            "2010-01-05",
            "2025-01-06",
            "2025-12-27",
            "2035-01-16",
        )
        name = "Guru Gobind Singh Jayanti"
        for subdiv in India.subdivisions:
            if subdiv in {"PB"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-04-13",
            "2010-04-14",
            "2025-04-13",
            "2035-04-14",
        )
        name = "Vaisakhi"
        for subdiv in India.subdivisions:
            if subdiv in {"PB"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        name = "Pongal"
        for subdiv in India.subdivisions:
            if subdiv in {"TN"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-01-15",
            "2010-01-15",
            "2025-01-15",
            "2035-01-16",
        )
        name = "Thiruvalluvar Day / Mattu Pongal"
        for subdiv in India.subdivisions:
            if subdiv in {"TN"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

        dt = (
            "2001-01-16",
            "2010-01-16",
            "2025-01-16",
            "2035-01-17",
        )
        name = "Uzhavar Thirunal"
        for subdiv in India.subdivisions:
            if subdiv in {"TN"}:
                self.assertHolidayName(name, India(subdiv=subdiv), dt)
            else:
                self.assertNoHolidayName(name, India(subdiv=subdiv), dt)

    def test_ranged_optional_holidays(self):
        opt_holidays = India(categories=OPTIONAL)

        name = "Holi"
        dt = (
            "2001-03-10",
            "2010-03-01",
            "2025-03-14",
            "2035-03-24",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Ganesh Chaturthi"
        dt = (
            "2001-08-22",
            "2010-09-11",
            "2025-08-27",
            "2035-09-05",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Govardhan Puja"
        dt = (
            "2001-11-15",
            "2010-11-06",
            "2025-10-22",
            "2035-10-31",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Maha Navami"
        dt = (
            "2001-10-25",
            "2010-10-16",
            "2025-10-01",
            "2035-10-10",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Makar Sankranti"
        dt = (
            "2001-01-14",
            "2010-01-14",
            "2025-01-14",
            "2035-01-15",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Navratri / Sharad Navratri"
        dt = (
            "2001-10-17",
            "2010-10-08",
            "2025-09-22",
            "2035-10-02",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Raksha Bandhan"
        dt = (
            "2001-08-04",
            "2010-08-24",
            "2025-08-09",
            "2035-08-18",
        )
        self.assertHolidayName(name, opt_holidays, dt)

        name = "Ram Navami"
        dt = (
            "2001-04-02",
            "2010-03-24",
            "2025-04-06",
            "2035-04-16",
        )
        self.assertHolidayName(name, opt_holidays, dt)

    def test_pre_1947(self):
        self.assertNoHoliday("1946-08-15")

    def test_pre_1950(self):
        self.assertNoHoliday("1949-01-26")

    def test_good_friday(self):
        self.assertHoliday(
            "1994-04-01",
            "2017-04-14",
            "2020-04-10",
        )

    def test_easter_sunday(self):
        self.assertHoliday(
            India(categories=OPTIONAL),
            "1994-04-03",
            "2017-04-16",
            "2020-04-12",
        )

    def test_palm_sunday(self):
        self.assertHoliday(
            India(categories=OPTIONAL),
            "1994-03-27",
            "2017-04-09",
            "2020-04-05",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-13", "Lohri"),
            ("2018-01-14", "Magh Bihu; Makar Sankranti; Pongal; Uttarayan"),
            ("2018-01-15", "Thiruvalluvar Day / Mattu Pongal"),
            ("2018-01-16", "Uzhavar Thirunal"),
            ("2018-01-24", "UP Formation Day"),
            ("2018-01-26", "Republic Day"),
            ("2018-02-13", "Maha Shivaratri"),
            ("2018-02-19", "Chhatrapati Shivaji Maharaj Jayanti"),
            ("2018-02-20", "Mizoram State Day"),
            ("2018-03-02", "Holi"),
            ("2018-03-18", "Gudi Padwa"),
            ("2018-03-22", "Bihar Day"),
            ("2018-03-25", "Palm Sunday; Ram Navami"),
            ("2018-03-29", "Mahavir Jayanti"),
            ("2018-03-30", "Good Friday; Rajasthan Day"),
            ("2018-04-01", "Easter Sunday; Odisha Day (Utkala Dibasa)"),
            ("2018-04-14", "Dr. B. R. Ambedkar's Jayanti; Puthandu (Tamil New Year); Vaisakhi"),
            (
                "2018-04-15",
                "Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh",
            ),
            ("2018-04-30", "Buddha Purnima"),
            ("2018-05-01", "Gujarat Day; Labour Day; Maharashtra Day"),
            ("2018-05-09", "Rabindra Jayanti"),
            ("2018-05-16", "Sikkim State Day"),
            ("2018-06-02", "Telangana Formation Day"),
            ("2018-06-15", "Maharana Pratap Jayanti"),
            ("2018-06-16", "Id-ul-Fitr"),
            ("2018-08-15", "Independence Day"),
            ("2018-08-16", "Puducherry De Jure Transfer Day"),
            ("2018-08-22", "Bakrid"),
            ("2018-08-24", "Onam"),
            ("2018-08-26", "Raksha Bandhan"),
            ("2018-09-03", "Janmashtami"),
            ("2018-09-13", "Ganesh Chaturthi"),
            ("2018-09-21", "Muharram"),
            ("2018-10-02", "Gandhi Jayanti"),
            ("2018-10-06", "Bathukamma Festival"),
            ("2018-10-10", "Navratri / Sharad Navratri"),
            ("2018-10-18", "Maha Navami"),
            ("2018-10-19", "Dussehra"),
            ("2018-10-31", "Sardar Vallabhbhai Patel Jayanti"),
            (
                "2018-11-01",
                "Andhra Pradesh Foundation Day; "
                "Chhattisgarh Foundation Day; "
                "Haryana Foundation Day; "
                "Karnataka Rajyotsava; Kerala Foundation Day; "
                "Madhya Pradesh Foundation Day; "
                "Puducherry Liberation Day; "
                "Punjab Day",
            ),
            ("2018-11-07", "Diwali"),
            ("2018-11-08", "Govardhan Puja"),
            ("2018-11-13", "Chhath Puja"),
            ("2018-11-14", "Children's Day"),
            ("2018-11-15", "Jharkhand Formation Day"),
            ("2018-11-21", "Milad-un-Nabi"),
            ("2018-11-23", "Guru Nanak Jayanti"),
            ("2018-12-01", "Nagaland State Inauguration Day"),
            ("2018-12-02", "Assam Day"),
            ("2018-12-19", "Goa Liberation Day"),
            ("2018-12-25", "Christmas"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2018-01-13", "लोहड़ी"),
            ("2018-01-14", "उत्तरायण; पोंगल; मकर संक्रांति; माघ बिहू"),
            ("2018-01-15", "तिरुवल्लुवर दिवस / मट्टू पोंगल"),
            ("2018-01-16", "उझावर थिरुनल"),
            ("2018-01-24", "यूपी स्थापना दिवस"),
            ("2018-01-26", "गणतंत्र दिवस"),
            ("2018-02-13", "महाशिवरात्रि"),
            ("2018-02-19", "छत्रपति शिवाजी महाराज जयंती"),
            ("2018-02-20", "मिज़ोरम राज्य दिवस"),
            ("2018-03-02", "होली"),
            ("2018-03-18", "गुडी पाडवा"),
            ("2018-03-22", "बिहार दिवस"),
            ("2018-03-25", "पाम संडे; रामनवमी"),
            ("2018-03-29", "महावीर जयंती"),
            ("2018-03-30", "गुड फ्राइडे; राजस्थान दिवस"),
            ("2018-04-01", "ईस्टर संडे; ओडिशा दिवस (उत्कल दिवस)"),
            ("2018-04-14", "डॉ. बी.आर. आम्बेडकर जयंती; पुत्ताण्डु (तमिल नव वर्ष); वैसाखी"),
            ("2018-04-15", "पोहेला बोइशाख; महा विषुव संक्रांति / पण संक्रांति; हिमाचल दिवस"),
            ("2018-04-30", "बुद्ध पूर्णिमा"),
            ("2018-05-01", "गुजरात दिवस; मजदूर दिवस; महाराष्ट्र दिवस"),
            ("2018-05-09", "रवींद्र जयंती"),
            ("2018-05-16", "सिक्किम राज्य दिवस"),
            ("2018-06-02", "तेलंगाना स्थापना दिवस"),
            ("2018-06-15", "महाराणा प्रताप जयंती"),
            ("2018-06-16", "ईद-उल-फितर"),
            ("2018-08-15", "स्वतंत्रता दिवस"),
            ("2018-08-16", "पुडुचेरी डी ज्यूर स्थानांतरण दिवस"),
            ("2018-08-22", "बकरीद"),
            ("2018-08-24", "ओणम"),
            ("2018-08-26", "रक्षाबंधन"),
            ("2018-09-03", "जन्माष्टमी"),
            ("2018-09-13", "गणेश चतुर्थी"),
            ("2018-09-21", "मुहर्रम"),
            ("2018-10-02", "गांधी जयंती"),
            ("2018-10-06", "बतुकम्मा महोत्सव"),
            ("2018-10-10", "नवरात्र/शरद नवरात्र"),
            ("2018-10-18", "महानवमी"),
            ("2018-10-19", "दशहरा"),
            ("2018-10-31", "सरदार वल्लभभाई पटेल जयंती"),
            (
                "2018-11-01",
                "आंध्र प्रदेश स्थापना दिवस; "
                "कर्नाटक राज्योत्सव; केरल स्थापना दिवस; "
                "छत्तीसगढ़ स्थापना दिवस; पंजाब दिवस; "
                "पुडुचेरी मुक्ति दिवस; मध्य प्रदेश स्थापना दिवस; "
                "हरियाणा स्थापना दिवस",
            ),
            ("2018-11-07", "दिवाली"),
            ("2018-11-08", "गोवर्धन पूजा"),
            ("2018-11-13", "छठ पूजा"),
            ("2018-11-14", "बाल दिवस"),
            ("2018-11-15", "झारखंड स्थापना दिवस"),
            ("2018-11-21", "मिलाद-उन-नबी"),
            ("2018-11-23", "गुरु नानक जयंती"),
            ("2018-12-01", "नागालैंड राज्य उद्घाटन दिवस"),
            ("2018-12-02", "असम दिवस"),
            ("2018-12-19", "गोवा मुक्ति दिवस"),
            ("2018-12-25", "क्रिसमस"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-13", "Lohri"),
            ("2018-01-14", "Magh Bihu; Makar Sankranti; Pongal; Uttarayan"),
            ("2018-01-15", "Thiruvalluvar Day / Mattu Pongal"),
            ("2018-01-16", "Uzhavar Thirunal"),
            ("2018-01-24", "UP Formation Day"),
            ("2018-01-26", "Republic Day"),
            ("2018-02-13", "Maha Shivaratri"),
            ("2018-02-19", "Chhatrapati Shivaji Maharaj Jayanti"),
            ("2018-02-20", "Mizoram State Day"),
            ("2018-03-02", "Holi"),
            ("2018-03-18", "Gudi Padwa"),
            ("2018-03-22", "Bihar Day"),
            ("2018-03-25", "Palm Sunday; Ram Navami"),
            ("2018-03-29", "Mahavir Jayanti"),
            ("2018-03-30", "Good Friday; Rajasthan Day"),
            ("2018-04-01", "Easter Sunday; Odisha Day (Utkala Dibasa)"),
            ("2018-04-14", "Dr. B. R. Ambedkar's Jayanti; Puthandu (Tamil New Year); Vaisakhi"),
            (
                "2018-04-15",
                "Himachal Day; Maha Vishuva Sankranti / Pana Sankranti; Pohela Boishakh",
            ),
            ("2018-04-30", "Buddha Purnima"),
            ("2018-05-01", "Gujarat Day; Labor Day; Maharashtra Day"),
            ("2018-05-09", "Rabindra Jayanti"),
            ("2018-05-16", "Sikkim State Day"),
            ("2018-06-02", "Telangana Formation Day"),
            ("2018-06-15", "Maharana Pratap Jayanti"),
            ("2018-06-16", "Eid al-Fitr"),
            ("2018-08-15", "Independence Day"),
            ("2018-08-16", "Puducherry De Jure Transfer Day"),
            ("2018-08-22", "Eid al-Adha"),
            ("2018-08-24", "Onam"),
            ("2018-08-26", "Raksha Bandhan"),
            ("2018-09-03", "Janmashtami"),
            ("2018-09-13", "Ganesh Chaturthi"),
            ("2018-09-21", "Ashura"),
            ("2018-10-02", "Gandhi Jayanti"),
            ("2018-10-06", "Bathukamma Festival"),
            ("2018-10-10", "Navratri / Sharad Navratri"),
            ("2018-10-18", "Maha Navami"),
            ("2018-10-19", "Dussehra"),
            ("2018-10-31", "Sardar Vallabhbhai Patel Jayanti"),
            (
                "2018-11-01",
                "Andhra Pradesh Foundation Day; "
                "Chhattisgarh Foundation Day; "
                "Haryana Foundation Day; "
                "Karnataka Rajyotsava; Kerala Foundation Day; "
                "Madhya Pradesh Foundation Day; "
                "Puducherry Liberation Day; "
                "Punjab Day",
            ),
            ("2018-11-07", "Diwali"),
            ("2018-11-08", "Govardhan Puja"),
            ("2018-11-13", "Chhath Puja"),
            ("2018-11-14", "Children's Day"),
            ("2018-11-15", "Jharkhand Formation Day"),
            ("2018-11-21", "Prophet's Birthday"),
            ("2018-11-23", "Guru Nanak Jayanti"),
            ("2018-12-01", "Nagaland State Inauguration Day"),
            ("2018-12-02", "Assam Day"),
            ("2018-12-19", "Goa Liberation Day"),
            ("2018-12-25", "Christmas"),
        )

    def test_deprecated(self):
        self.assertEqual(
            India(subdiv="DD", years=2023).keys(), India(subdiv="DH", years=2023).keys()
        )
        self.assertEqual(
            India(subdiv="OR", years=2023).keys(), India(subdiv="OD", years=2023).keys()
        )
