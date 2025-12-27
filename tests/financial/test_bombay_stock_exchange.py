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

from holidays.financial.bombay_stock_exchange import BombayStockExchange
from tests.common import CommonFinancialTests


class TestBombayStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BombayStockExchange)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-26", "Republic Day"),
            ("2023-03-07", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. Baba Saheb Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-28", "Bakri Id"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Mahatma Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-14", "Diwali Balipratipada"),
            ("2023-11-27", "Guru Nanak Jayanti"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-26", "Republic Day"),
            ("2023-03-07", "Holi"),
            ("2023-03-30", "Ram Navami"),
            ("2023-04-04", "Mahavir Jayanti"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-14", "Dr. B. R. Ambedkar Jayanti"),
            ("2023-05-01", "Maharashtra Day"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-08-15", "Independence Day"),
            ("2023-09-19", "Ganesh Chaturthi"),
            ("2023-10-02", "Gandhi Jayanti"),
            ("2023-10-24", "Dussehra"),
            ("2023-11-14", "Diwali Balipratipada"),
            ("2023-11-27", "Guru Nanak Jayanti"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_gu(self):
        self.assertLocalizedHolidays(
            "gu",
            ("2023-01-26", "પ્રજાસત્તાક દિવસ"),
            ("2023-03-07", "હોળી"),
            ("2023-03-30", "રામ નવમી"),
            ("2023-04-04", "મહાવીર જયંતિ"),
            ("2023-04-07", "ગુડ ફ્રાઈડે"),
            ("2023-04-14", "ડૉ. બાબાસાહેબ આંબેડકર જયંતિ"),
            ("2023-05-01", "મહારાષ્ટ્ર દિવસ"),
            ("2023-06-28", "બકરી ઈદ"),
            ("2023-08-15", "સ્વતંત્રતા દિવસ"),
            ("2023-09-19", "ગણેશ ચતુર્થી"),
            ("2023-10-02", "મહાત્મા ગાંધી જયંતિ"),
            ("2023-10-24", "દશેરા"),
            ("2023-11-14", "દિવાળી બલિપ્રતિપદા"),
            ("2023-11-27", "ગુરુ નાનક જયંતિ"),
            ("2023-12-25", "નાતાલ"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2023-01-26", "गणतंत्र दिवस"),
            ("2023-03-07", "होली"),
            ("2023-03-30", "राम नवमी"),
            ("2023-04-04", "महावीर जयंती"),
            ("2023-04-07", "गुड फ्राइडे"),
            ("2023-04-14", "डॉ. बाबा साहेब अम्बेडकर जयंती"),
            ("2023-05-01", "महाराष्ट्र दिवस"),
            ("2023-06-28", "बकरी ईद"),
            ("2023-08-15", "स्वतंत्रता दिवस"),
            ("2023-09-19", "गणेश चतुर्थी"),
            ("2023-10-02", "महात्मा गांधी जयंती"),
            ("2023-10-24", "दशहरा"),
            ("2023-11-14", "दिवाली बलिप्रतिपदा"),
            ("2023-11-27", "गुरु नानक जयंती"),
            ("2023-12-25", "क्रिसमस डे"),
        )
