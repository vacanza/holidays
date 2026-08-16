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

from holidays.financial.nasdaq import NASDAQ
from tests.common import CommonFinancialTests


class TestNASDAQ(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NASDAQ)

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-09", "National Day of Mourning for former President Jimmy Carter"),
            ("2025-01-20", "Martin Luther King Jr. Day"),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2025-11-28", "Day after Thanksgiving Day (markets close at 1:00pm)"),
            ("2025-12-24", "Christmas Eve (markets close at 1:00pm)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Martin Luther King Jr. Day"),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-11-29", "Day after Thanksgiving Day (markets close at 1:00pm)"),
            ("2024-12-24", "Christmas Eve (markets close at 1:00pm)"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_gu(self):
        self.assertLocalizedHolidays(
            "gu",
            ("2024-01-01", "નવા વર્ષનો દિવસ"),
            ("2024-01-15", "માર્ટિન લ્યુથર કિંગ જુનિયર દિવસ"),
            ("2024-02-19", "વોશિંગ્ટનનો જન્મદિવસ"),
            ("2024-03-29", "ગુડ ફ્રાઇડે"),
            ("2024-05-27", "મેમોરિયલ ડે"),
            ("2024-06-19", "જુનટીન્થ રાષ્ટ્રીય સ્વતંત્રતા દિવસ"),
            ("2024-07-03", "સ્વતંત્રતા દિવસનો આગલો દિવસ (બજારો બપોરે 1:00 વાગ્યે બંધ થાય છે)"),
            ("2024-07-04", "સ્વતંત્રતા દિવસ"),
            ("2024-09-02", "શ્રમ દિવસ"),
            ("2024-11-28", "થેંક્સગિવિંગ ડે"),
            ("2024-11-29", "થેંક્સગિવિંગ ડે પછીનો દિવસ (બજારો બપોરે 1:00 વાગ્યે બંધ થાય છે)"),
            ("2024-12-24", "નાતાલ પૂર્વસંધ્યા (બજારો બપોરે 1:00 વાગ્યે બંધ થાય છે)"),
            ("2024-12-25", "નાતાલનો દિવસ"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2024-01-01", "नव वर्ष दिवस"),
            ("2024-01-15", "मार्टिन लूथर किंग जूनियर दिवस"),
            ("2024-02-19", "वाशिंगटन का जन्मदिन"),
            ("2024-03-29", "गुड फ्राइडे"),
            ("2024-05-27", "मेमोरियल डे"),
            ("2024-06-19", "जूनटीन्थ राष्ट्रीय स्वतंत्रता दिवस"),
            ("2024-07-03", "स्वतंत्रता दिवस से पहले का दिन (बाज़ार दोपहर 1:00 बजे बंद होते हैं)"),
            ("2024-07-04", "स्वतंत्रता दिवस"),
            ("2024-09-02", "श्रम दिवस"),
            ("2024-11-28", "थैंक्सगिविंग डे"),
            ("2024-11-29", "थैंक्सगिविंग डे के बाद का दिन (बाज़ार दोपहर 1:00 बजे बंद होते हैं)"),
            ("2024-12-24", "क्रिसमस की पूर्व संध्या (बाज़ार दोपहर 1:00 बजे बंद होते हैं)"),
            ("2024-12-25", "क्रिसमस दिवस"),
        )
