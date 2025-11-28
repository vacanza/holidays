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

from holidays.constants import WORKDAY
from holidays.countries.nepal import Nepal
from tests.common import CommonCountryTests


class TestNepal(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2010, 2050)
        super().setUpClass(Nepal, years=years)
        cls.no_estimated_holidays = Nepal(years=years, islamic_show_estimated=False)
        cls.workday_holidays = Nepal(categories=WORKDAY, years=years)

    def test_special_holidays(self):
        name_day_of_national_mourning = "Day of National Mourning"
        name_tihar_holiday = "Tihar Holiday"

        for dt, name in (
            ("2011-03-06", name_day_of_national_mourning),
            ("2016-02-10", name_day_of_national_mourning),
            ("2021-11-07", name_tihar_holiday),
            ("2022-10-28", name_tihar_holiday),
            ("2023-01-16", name_day_of_national_mourning),
            ("2023-02-13", "People War's Day"),
            ("2023-09-14", name_day_of_national_mourning),
            ("2023-11-16", name_tihar_holiday),
            ("2024-11-04", name_tihar_holiday),
            ("2025-10-24", name_tihar_holiday),
        ):
            self.assertHolidayName(name, dt)

    def test_prithvi_jayanti(self):
        name = "Prithvi Jayanti"
        self.assertHolidayName(name, (f"{year}-01-11" for year in range(2023, 2050)))
        self.assertNoHolidayName(name, range(2010, 2023))

    def test_martyrs_day(self):
        name = "Martyr's Day"
        dt = (
            "2021-01-29",
            "2022-01-30",
            "2023-01-30",
            "2024-01-30",
            "2025-01-29",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2034))
        self.assertNoHolidayName(name, range(2019, 2021), range(2034, 2050))
        dt = (
            "2019-01-30",
            "2020-01-30",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_national_democracy_day(self):
        name = "National Democracy Day"
        dt = (
            "2021-02-19",
            "2022-02-19",
            "2023-02-19",
            "2024-02-19",
            "2025-02-19",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2034))
        self.assertNoHolidayName(name, range(2019, 2021), range(2034, 2050))
        dt = (
            "2019-02-19",
            "2020-02-19",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_womens_day(self):
        self.assertHolidayName(
            "International Women's Day", (f"{year}-03-08" for year in range(2010, 2050))
        )

    def test_nepali_new_year(self):
        name = "Nepali New Year"
        dt = (
            "2019-04-14",
            "2020-04-13",
            "2021-04-14",
            "2022-04-14",
            "2023-04-14",
            "2024-04-13",
            "2025-04-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_labour_day(self):
        self.assertHolidayName(
            "International Labour Day", (f"{year}-05-01" for year in range(2010, 2050))
        )

    def test_republic_day(self):
        name = "Republic Day"
        dt = (
            "2021-05-29",
            "2022-05-29",
            "2023-05-29",
            "2024-05-28",
            "2025-05-28",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2033))
        self.assertNoHolidayName(name, range(2019, 2021), range(2033, 2050))
        dt = (
            "2019-05-29",
            "2020-05-28",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_constitution_day(self):
        name = "Constitution Day"
        dt = (
            "2019-09-20",
            "2020-09-19",
            "2021-09-19",
            "2022-09-19",
            "2023-09-20",
            "2024-09-19",
            "2025-09-19",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2016, 2033))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2010, 2050)))

    def test_maghe_sankranti(self):
        name = "Maghe Sankranti"
        dt = (
            "2019-01-15",
            "2020-01-15",
            "2021-01-14",
            "2022-01-15",
            "2023-01-15",
            "2024-01-15",
            "2025-01-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_sonam_lhochhar(self):
        name = "Sonam Lhochhar"
        dt = (
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-02",
            "2023-01-22",
            "2024-02-10",
            "2025-01-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_gyalpo_lhosar(self):
        name = "Gyalpo Lhosar"
        dt = (
            "2019-03-07",
            "2020-02-24",
            "2021-03-14",
            "2022-03-03",
            "2023-02-21",
            "2024-03-11",
            "2025-02-28",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_maha_shivaratri(self):
        name = "Maha Shivaratri"
        dt = (
            "2019-03-04",
            "2020-02-21",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-03-08",
            "2025-02-26",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_holi_hilly(self):
        name = "Fagu Poornima"
        dt = (
            "2019-03-20",
            "2020-03-09",
            "2021-03-28",
            "2022-03-17",
            "2023-03-06",
            "2024-03-24",
            "2025-03-13",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_holi_terai(self):
        name = "Fagu Poornima (Terai)"
        dt = (
            "2019-03-21",
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-07",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_ram_navami(self):
        name = "Ram Navami"
        dt = (
            "2021-04-21",
            "2022-04-10",
            "2023-03-30",
            "2024-04-17",
            "2025-04-06",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2036))
        self.assertNoHolidayName(name, range(2019, 2021))
        dt = (
            "2019-04-13",
            "2020-04-02",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_buddha_jayanti(self):
        name = "Buddha Jayanti"
        dt = (
            "2019-05-18",
            "2020-05-07",
            "2021-05-26",
            "2022-05-16",
            "2023-05-05",
            "2024-05-23",
            "2025-05-12",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_janai_poornima(self):
        name = "Janai Poornima"
        dt = (
            "2021-08-22",
            "2022-08-12",
            "2023-08-31",
            "2024-08-19",
            "2025-08-09",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2036))
        self.assertNoHolidayName(name, range(2019, 2021))
        dt = (
            "2019-08-15",
            "2020-08-03",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_janmashtami(self):
        name = "Shree Krishna Janmashtami"
        dt = (
            "2021-08-30",
            "2022-08-19",
            "2023-09-06",
            "2024-08-26",
            "2025-08-16",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2036))
        self.assertNoHolidayName(name, range(2019, 2021))
        dt = (
            "2019-08-24",
            "2020-08-12",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_ghatasthapana(self):
        name = "Ghatasthapana"
        dt = (
            "2021-10-07",
            "2022-09-26",
            "2023-10-15",
            "2024-10-03",
            "2025-09-22",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2036))
        self.assertNoHolidayName(name, range(2019, 2021))
        dt = (
            "2019-09-29",
            "2020-10-17",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_fulpati(self):
        name = "Fulpati"
        dt = (
            "2019-10-05",
            "2020-10-23",
            "2021-10-12",
            "2022-10-02",
            "2023-10-21",
            "2024-10-10",
            "2025-09-29",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_maha_ashtami(self):
        name = "Maha Ashtami"
        dt = (
            "2019-10-06",
            "2020-10-24",
            "2021-10-13",
            "2022-10-03",
            "2023-10-22",
            "2024-10-11",
            "2025-09-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_maha_navami(self):
        name = "Maha Navami"
        dt = (
            "2019-10-06",
            "2020-10-25",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
            "2025-10-01",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_vijayadashami(self):
        name = "Bijaya Dashami"
        dt = (
            "2019-10-08",
            "2020-10-26",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_ekadashi(self):
        name = "Ekadashi (Dashain)"
        dt = (
            "2019-10-09",
            "2020-10-27",
            "2021-10-16",
            "2022-10-06",
            "2023-10-25",
            "2024-10-13",
            "2025-10-03",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_duwadashi(self):
        name = "Duwadashi (Dashain)"
        dt = (
            "2021-10-17",
            "2022-10-07",
            "2023-10-26",
            "2024-10-14",
            "2025-10-04",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2019), range(2021, 2036))
        self.assertNoHolidayName(name, range(2019, 2021))
        dt = (
            "2019-10-10",
            "2020-10-28",
        )
        self.assertHolidayName(name, self.workday_holidays, dt)
        self.assertNoHolidayName(name, self.workday_holidays, range(2010, 2019), range(2021, 2050))

    def test_laxmi_pooja(self):
        name = "Laxmi Pooja"
        dt = (
            "2019-10-27",
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_gai_tihar(self):
        name = "Gai Tihar"
        dt = (
            "2019-10-27",
            "2020-11-15",
            "2021-11-04",
            "2022-10-25",
            "2023-11-13",
            "2024-11-01",
            "2025-10-21",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_gobardhan_pooja(self):
        name = "Gobardhan Pooja"
        dt = (
            "2019-10-28",
            "2020-11-16",
            "2021-11-05",
            "2022-10-26",
            "2023-11-14",
            "2024-11-02",
            "2025-10-22",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_mha_pooja(self):
        name = "Mha Pooja"
        dt = (
            "2019-10-28",
            "2020-11-16",
            "2021-11-05",
            "2022-10-26",
            "2023-11-14",
            "2024-11-02",
            "2025-10-22",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_bhai_tika(self):
        name = "Bhai Tika"
        dt = (
            "2019-10-29",
            "2020-11-17",
            "2021-11-06",
            "2022-10-27",
            "2023-11-15",
            "2024-11-03",
            "2025-10-23",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_chhath_parwa(self):
        name = "Chhath Parva"
        dt = (
            "2019-11-02",
            "2020-11-20",
            "2021-11-10",
            "2022-10-30",
            "2023-11-19",
            "2024-11-07",
            "2025-10-27",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2036))

    def test_tamu_lhochhar(self):
        name = "Tamu Lhochhar"
        dt = (
            "2019-12-31",
            "2020-12-30",
            "2021-12-30",
            "2022-12-30",
            "2023-12-31",
            "2024-12-30",
            "2025-12-30",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2010, 2033))

    def test_id_ul_fitr(self):
        name = "Id-ul-Fitr"
        dt = (
            "2019-06-05",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.no_estimated_holidays, range(2010, 2050))

    def test_bakrid(self):
        name = "Bakrid"
        dt = (
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, self.no_estimated_holidays, range(2010, 2050))

    def test_2025(self):
        self.assertHolidays(
            Nepal(years=2025),
            ("2025-01-11", "Prithvi Jayanti"),
            ("2025-01-14", "Maghe Sankranti"),
            ("2025-01-29", "Martyr's Day"),
            ("2025-01-30", "Sonam Lhochhar"),
            ("2025-02-19", "National Democracy Day"),
            ("2025-02-26", "Maha Shivaratri"),
            ("2025-02-28", "Gyalpo Lhosar"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-13", "Fagu Poornima"),
            ("2025-03-14", "Fagu Poornima (Terai)"),
            ("2025-03-31", "Id-ul-Fitr"),
            ("2025-04-06", "Ram Navami"),
            ("2025-04-14", "Nepali New Year"),
            ("2025-05-01", "International Labour Day"),
            ("2025-05-12", "Buddha Jayanti"),
            ("2025-05-28", "Republic Day"),
            ("2025-06-07", "Bakrid"),
            ("2025-08-09", "Janai Poornima"),
            ("2025-08-16", "Shree Krishna Janmashtami"),
            ("2025-09-19", "Constitution Day"),
            ("2025-09-22", "Ghatasthapana"),
            ("2025-09-29", "Fulpati"),
            ("2025-09-30", "Maha Ashtami"),
            ("2025-10-01", "Maha Navami"),
            ("2025-10-02", "Bijaya Dashami"),
            ("2025-10-03", "Ekadashi (Dashain)"),
            ("2025-10-04", "Duwadashi (Dashain)"),
            ("2025-10-20", "Laxmi Pooja"),
            ("2025-10-21", "Gai Tihar"),
            ("2025-10-22", "Gobardhan Pooja; Mha Pooja"),
            ("2025-10-23", "Bhai Tika"),
            ("2025-10-24", "Tihar Holiday"),
            ("2025-10-27", "Chhath Parva"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-30", "Tamu Lhochhar"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-11", "Prithvi Jayanti"),
            ("2024-01-15", "Maghe Sankranti"),
            ("2024-01-30", "Martyr's Day"),
            ("2024-02-10", "Sonam Lhochhar"),
            ("2024-02-19", "National Democracy Day"),
            ("2024-03-08", "International Women's Day; Maha Shivaratri"),
            ("2024-03-11", "Gyalpo Lhosar"),
            ("2024-03-24", "Fagu Poornima"),
            ("2024-03-25", "Fagu Poornima (Terai)"),
            ("2024-04-11", "Id-ul-Fitr"),
            ("2024-04-13", "Nepali New Year"),
            ("2024-04-17", "Ram Navami"),
            ("2024-05-01", "International Labour Day"),
            ("2024-05-23", "Buddha Jayanti"),
            ("2024-05-28", "Republic Day"),
            ("2024-06-17", "Bakrid"),
            ("2024-08-19", "Janai Poornima"),
            ("2024-08-26", "Shree Krishna Janmashtami"),
            ("2024-09-19", "Constitution Day"),
            ("2024-10-03", "Ghatasthapana"),
            ("2024-10-10", "Fulpati"),
            ("2024-10-11", "Maha Ashtami; Maha Navami"),
            ("2024-10-12", "Bijaya Dashami"),
            ("2024-10-13", "Ekadashi (Dashain)"),
            ("2024-10-14", "Duwadashi (Dashain)"),
            ("2024-10-31", "Laxmi Pooja"),
            ("2024-11-01", "Gai Tihar"),
            ("2024-11-02", "Gobardhan Pooja; Mha Pooja"),
            ("2024-11-03", "Bhai Tika"),
            ("2024-11-04", "Tihar Holiday"),
            ("2024-11-07", "Chhath Parva"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-30", "Tamu Lhochhar"),
        )

    def test_l10n_ne(self):
        self.assertLocalizedHolidays(
            "ne",
            ("2024-01-11", "पृथ्वी जयन्ती"),
            ("2024-01-15", "माघे संक्रान्ति"),
            ("2024-01-30", "शहीद दिवस"),
            ("2024-02-10", "सोनम ल्होछार"),
            ("2024-02-19", "राष्ट्रिय प्रजातन्त्र दिवस"),
            ("2024-03-08", "अन्तर्राष्ट्रिय महिला दिवस; महाशिवरात्रि"),
            ("2024-03-11", "ग्याल्पो ल्होसार"),
            ("2024-03-24", "फागुपुर्णिमा"),
            ("2024-03-25", "फागुपूर्णिमा (तराई)"),
            ("2024-04-11", "इद उल फित्र"),
            ("2024-04-13", "नेपाली नयाँ वर्ष"),
            ("2024-04-17", "राम नवमी"),
            ("2024-05-01", "अन्तर्राष्ट्रिय श्रम दिवस"),
            ("2024-05-23", "बुद्ध जयन्ती"),
            ("2024-05-28", "गणतन्त्र दिवस"),
            ("2024-06-17", "बकरिद"),
            ("2024-08-19", "जनै पूर्णिमा"),
            ("2024-08-26", "श्रीकृष्ण जन्माष्टमी"),
            ("2024-09-19", "संविधान दिवस"),
            ("2024-10-03", "घटस्थापना"),
            ("2024-10-10", "फुलपाती"),
            ("2024-10-11", "महा अष्टमी; महा नवमी"),
            ("2024-10-12", "विजया दशमी"),
            ("2024-10-13", "एकादशी (दशैं)"),
            ("2024-10-14", "दुवादशी (दशैं)"),
            ("2024-10-31", "लक्ष्मी पुजा"),
            ("2024-11-01", "गाई तिहार"),
            ("2024-11-02", "गोवर्धन पूजा; म्ह पूजा"),
            ("2024-11-03", "भाइटीका"),
            ("2024-11-04", "तिहार बिदा"),
            ("2024-11-07", "छठ पर्व"),
            ("2024-12-25", "क्रिसमसको दिन"),
            ("2024-12-30", "तमु ल्हाेसार"),
        )
