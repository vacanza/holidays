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

from holidays.financial.chicago_mercantile_exchange import ChicagoMercantileExchange
from tests.common import CommonFinancialTests


class TestChicagoMercantileExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ChicagoMercantileExchange)

    def test_special_holidays(self):
        self.assertHoliday(
            "2001-09-11",
            "2001-09-12",
            "2001-09-13",
            "2001-09-14",
            "2004-06-11",
            "2007-01-02",
            "2012-10-29",
            "2012-10-30",
            "2018-12-05",
            "2025-01-09",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertNoHoliday(
            "2004-12-31",
            "2010-12-31",
            "2021-12-31",
        )

    def test_dr_martin_luther_king_jr_day(self):
        name_1030 = "Dr. Martin Luther King, Jr. Day (markets pause at 10:30am CT)"
        name_1200 = "Dr. Martin Luther King, Jr. Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name_1030)
        self.assertNoHolidayName(name_1200)
        self.assertHalfDayHolidayName(
            name_1030,
            "2010-01-18",
            "2011-01-17",
            "2012-01-16",
            "2013-01-21",
            "2014-01-20",
        )
        self.assertHalfDayHolidayName(name_1030, range(self.start_year, 2015))
        self.assertNoHalfDayHolidayName(name_1030, range(2015, self.end_year))
        self.assertHalfDayHolidayName(
            name_1200,
            "2015-01-19",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
            "2024-01-15",
            "2025-01-20",
        )
        self.assertHalfDayHolidayName(name_1200, range(2015, self.end_year))
        self.assertNoHalfDayHolidayName(name_1200, range(self.start_year, 2015))

    def test_presidents_day(self):
        name_1030 = "President's Day (markets pause at 10:30am CT)"
        name_1200 = "President's Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name_1030)
        self.assertNoHolidayName(name_1200)
        self.assertHalfDayHolidayName(
            name_1030,
            "2010-02-15",
            "2011-02-21",
            "2012-02-20",
            "2013-02-18",
            "2014-02-17",
        )
        self.assertHalfDayHolidayName(name_1030, range(self.start_year, 2015))
        self.assertNoHalfDayHolidayName(name_1030, range(2015, self.end_year))
        self.assertHalfDayHolidayName(
            name_1200,
            "2015-02-16",
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHalfDayHolidayName(name_1200, range(2015, self.end_year))
        self.assertNoHalfDayHolidayName(name_1200, range(self.start_year, 2015))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_memorial_day(self):
        name_1030 = "Memorial Day (markets pause at 10:30am CT)"
        name_1200 = "Memorial Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name_1030)
        self.assertNoHolidayName(name_1200)
        self.assertHalfDayHolidayName(
            name_1030,
            "2010-05-31",
            "2011-05-30",
            "2012-05-28",
            "2013-05-27",
            "2014-05-26",
        )
        self.assertHalfDayHolidayName(name_1030, range(self.start_year, 2015))
        self.assertNoHalfDayHolidayName(name_1030, range(2015, self.end_year))
        self.assertHalfDayHolidayName(
            name_1200,
            "2015-05-25",
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHalfDayHolidayName(name_1200, range(2015, self.end_year))
        self.assertNoHalfDayHolidayName(name_1200, range(self.start_year, 2015))

    def test_juneteenth_day(self):
        name = "Juneteenth Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-06-19" for year in range(2022, self.end_year))
        )
        self.assertNoHalfDayNonObservedHolidayName(name, range(self.start_year, 2022))
        self.assertHalfDayHolidayName(
            name,
            "2022-06-20",
            "2023-06-19",
            "2024-06-19",
            "2025-06-19",
            "2027-06-18",
        )
        self.assertHalfDayHolidayName(name, range(2022, self.end_year))
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 2022))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertNonObservedHolidayName(name, (f"{year}-07-04" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2004-07-05",
            "2010-07-05",
            "2021-07-05",
        )
        self.assertNoHolidayName(
            name,
            "2008-07-03",
            "2014-07-03",
            "2025-07-03",
        )

    def test_day_before_independence_day(self):
        name_1030 = "Day before Independence Day (markets pause at 10:30am CT)"
        name_1200 = "Day before Independence Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name_1030)
        self.assertNoHolidayName(name_1200)
        self.assertHalfDayHolidayName(
            name_1030,
            "2001-07-03",
            "2002-07-03",
            "2007-07-03",
            "2009-07-03",
        )
        self.assertNoHalfDayHolidayName(name_1030, range(2015, self.end_year))
        self.assertHalfDayHolidayName(
            name_1200,
            "2015-07-03",
            "2017-07-03",
            "2018-07-03",
            "2019-07-03",
            "2020-07-03",
            "2023-07-03",
            "2024-07-03",
            "2025-07-03",
        )
        self.assertNoHalfDayHolidayName(name_1200, range(self.start_year, 2015))

    def test_labor_day(self):
        name_1030 = "Labor Day (markets pause at 10:30am CT)"
        name_1200 = "Labor Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name_1030)
        self.assertNoHolidayName(name_1200)
        self.assertHalfDayHolidayName(
            name_1030,
            "2010-09-06",
            "2011-09-05",
            "2012-09-03",
            "2013-09-02",
            "2014-09-01",
        )
        self.assertHalfDayHolidayName(name_1030, range(self.start_year, 2015))
        self.assertNoHalfDayHolidayName(name_1030, range(2015, self.end_year))
        self.assertHalfDayHolidayName(
            name_1200,
            "2015-09-07",
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )
        self.assertHalfDayHolidayName(name_1200, range(2015, self.end_year))
        self.assertNoHalfDayHolidayName(name_1200, range(self.start_year, 2015))

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
            "2024-11-28",
            "2025-11-27",
        )
        self.assertHolidayName(name, self.full_range)

    def test_day_after_thanksgiving(self):
        name = "Day after Thanksgiving Day (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-29",
            "2025-11-28",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_christmas_eve(self):
        name = "Christmas Eve (markets pause at 12:00pm CT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2001-12-24",
            "2002-12-24",
            "2007-12-24",
            "2014-12-24",
            "2018-12-24",
            "2020-12-24",
            "2024-12-24",
            "2025-12-24",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2022-12-24",
            "2023-12-24",
        )

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name,
            "2004-12-24",
            "2010-12-24",
            "2011-12-26",
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-02", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-07-04", "Independence Day"),
            ("2023-11-23", "Thanksgiving Day"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_half_day_2023(self):
        self.assertHalfDayHolidaysInYear(
            2023,
            ("2023-01-16", "Dr. Martin Luther King, Jr. Day (markets pause at 12:00pm CT)"),
            ("2023-02-20", "President's Day (markets pause at 12:00pm CT)"),
            ("2023-05-29", "Memorial Day (markets pause at 12:00pm CT)"),
            ("2023-06-19", "Juneteenth Day (markets pause at 12:00pm CT)"),
            ("2023-07-03", "Day before Independence Day (markets pause at 12:00pm CT)"),
            ("2023-09-04", "Labor Day (markets pause at 12:00pm CT)"),
            ("2023-11-24", "Day after Thanksgiving Day (markets pause at 12:00pm CT)"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-07-04", "Independence Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_half_day_2024(self):
        self.assertHalfDayHolidaysInYear(
            2024,
            ("2024-01-15", "Dr. Martin Luther King, Jr. Day (markets pause at 12:00pm CT)"),
            ("2024-02-19", "President's Day (markets pause at 12:00pm CT)"),
            ("2024-05-27", "Memorial Day (markets pause at 12:00pm CT)"),
            ("2024-06-19", "Juneteenth Day (markets pause at 12:00pm CT)"),
            ("2024-07-03", "Day before Independence Day (markets pause at 12:00pm CT)"),
            ("2024-09-02", "Labor Day (markets pause at 12:00pm CT)"),
            ("2024-11-29", "Day after Thanksgiving Day (markets pause at 12:00pm CT)"),
            ("2024-12-24", "Christmas Eve (markets pause at 12:00pm CT)"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-09", "National Day of Mourning for former President Jimmy Carter"),
            ("2025-04-18", "Good Friday"),
            ("2025-07-04", "Independence Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-01-20", "Dr. Martin Luther King, Jr. Day (markets pause at 12:00pm CT)"),
            ("2025-02-17", "President's Day (markets pause at 12:00pm CT)"),
            ("2025-05-26", "Memorial Day (markets pause at 12:00pm CT)"),
            ("2025-06-19", "Juneteenth Day (markets pause at 12:00pm CT)"),
            ("2025-07-03", "Day before Independence Day (markets pause at 12:00pm CT)"),
            ("2025-09-01", "Labor Day (markets pause at 12:00pm CT)"),
            ("2025-11-28", "Day after Thanksgiving Day (markets pause at 12:00pm CT)"),
            ("2025-12-24", "Christmas Eve (markets pause at 12:00pm CT)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Dr. Martin Luther King, Jr. Day (markets pause at 12:00pm CT)"),
            ("2024-02-19", "President's Day (markets pause at 12:00pm CT)"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-27", "Memorial Day (markets pause at 12:00pm CT)"),
            ("2024-06-19", "Juneteenth Day (markets pause at 12:00pm CT)"),
            ("2024-07-03", "Day before Independence Day (markets pause at 12:00pm CT)"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day (markets pause at 12:00pm CT)"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-11-29", "Day after Thanksgiving Day (markets pause at 12:00pm CT)"),
            ("2024-12-24", "Christmas Eve (markets pause at 12:00pm CT)"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_gu(self):
        self.assertLocalizedHolidays(
            "gu",
            ("2024-01-01", "નવા વર્ષનો દિવસ"),
            ("2024-01-15", "ડૉ. માર્ટિન લ્યુથર કિંગ, જુનિયર ડે (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-02-19", "પ્રેસિડેન્ટ્સ ડે (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-03-29", "ગુડ ફ્રાઇડે"),
            ("2024-05-27", "મેમોરિયલ ડે (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-06-19", "જુનટીન્થ ડે (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-07-03", "સ્વતંત્રતા દિવસનો આગલો દિવસ (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-07-04", "સ્વતંત્રતા દિવસ"),
            ("2024-09-02", "શ્રમ દિવસ (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-11-28", "થેંક્સગિવિંગ ડે"),
            ("2024-11-29", "થેંક્સગિવિંગ ડે પછીનો દિવસ (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-12-24", "નાતાલ પૂર્વસંધ્યા (બજારો બપોરે 12:00 વાગ્યે CT સમયે થોભે છે)"),
            ("2024-12-25", "નાતાલનો દિવસ"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2024-01-01", "नव वर्ष दिवस"),
            ("2024-01-15", "डॉ. मार्टिन लूथर किंग, जूनियर डे (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-02-19", "प्रेसिडेंट्स डे (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-03-29", "गुड फ्राइडे"),
            ("2024-05-27", "मेमोरियल डे (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-06-19", "जूनटीन्थ डे (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-07-03", "स्वतंत्रता दिवस से पहले का दिन (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-07-04", "स्वतंत्रता दिवस"),
            ("2024-09-02", "श्रम दिवस (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-11-28", "थैंक्सगिविंग डे"),
            ("2024-11-29", "थैंक्सगिविंग डे के बाद का दिन (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-12-24", "क्रिसमस की पूर्व संध्या (बाज़ार दोपहर 12:00 बजे CT पर रुकते हैं)"),
            ("2024-12-25", "क्रिसमस दिवस"),
        )
