#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.canada import Canada, CA, CAN
from tests.common import TestCase


class TestCanada(TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1900, 2050)
        super().setUpClass(Canada, years=years)
        cls.prov_hols = {prov: CA(subdiv=prov, years=years) for prov in CA.subdivisions}

    def test_country_aliases(self):
        self.assertCountryAliases(Canada, CA, CAN)

    def test_no_holidays(self):
        self.assertNoHolidays(Canada(years=1866))

    def test_new_years(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1900, 2050))
        self.assertHoliday("2011-01-03", "2017-01-02")
        self.assertNoNonObservedHoliday("2011-01-03", "2017-01-02")

    def test_islander_day(self):
        dt = (
            "2010-02-15",
            "2011-02-21",
            "2012-02-20",
            "2013-02-18",
            "2014-02-17",
            "2015-02-16",
            "2016-02-15",
            "2020-02-17",
        )
        self.assertHoliday(self.prov_hols["PE"], dt, "2009-02-09")
        for d in dt:
            self.assertNotEqual(self.holidays[d], "Islander Day")

    def test_yukon_heritage_day(self):
        # https://www.timeanddate.com/holidays/canada/heritage-day-yukon
        dt = (
            "2017-02-24",
            "2018-02-23",
            "2019-02-22",
            "2020-02-21",
            "2021-02-26",
            "2022-02-25",
        )
        self.assertHoliday(self.prov_hols["YT"], dt)

    def test_family_day(self):
        ab_holidays = self.prov_hols["AB"]
        bc_holidays = self.prov_hols["BC"]
        mb_holidays = self.prov_hols["MB"]
        sk_holidays = self.prov_hols["SK"]
        nb_holidays = self.prov_hols["NB"]
        ns_holidays = self.prov_hols["NS"]
        dt = (
            "1990-02-19",
            "1999-02-15",
            "2000-02-21",
            "2006-02-20",
        )
        self.assertNoHoliday(dt)
        self.assertHoliday(ab_holidays, dt)
        self.assertNoHoliday(bc_holidays, dt)
        self.assertNoHoliday(mb_holidays, dt)
        self.assertNoHoliday(sk_holidays, dt)
        d = "2007-02-19"
        self.assertNoHoliday(d)
        self.assertHoliday(ab_holidays, d)
        self.assertNoHoliday(bc_holidays, d)
        self.assertNoHoliday(mb_holidays, d)
        self.assertHoliday(sk_holidays, d)
        dt = (
            "2008-02-18",
            "2012-02-20",
            "2014-02-17",
            "2018-02-19",
        )
        self.assertHoliday(dt)
        self.assertHoliday(ab_holidays, dt)
        self.assertNoHoliday(bc_holidays, dt)
        self.assertHoliday(mb_holidays, dt)
        self.assertHoliday(sk_holidays, dt)
        self.assertHoliday(nb_holidays, "2018-02-19")
        dt = ("2019-02-18", "2020-02-17")
        self.assertHoliday(dt)
        self.assertHoliday(ab_holidays, dt)
        self.assertHoliday(bc_holidays, dt)
        self.assertHoliday(mb_holidays, dt)
        self.assertHoliday(sk_holidays, dt)
        dt = ("2013-02-11", "2016-02-08")
        self.assertNoHoliday(dt)
        self.assertNoHoliday(ab_holidays, dt)
        self.assertHoliday(bc_holidays, dt)
        self.assertNoHoliday(mb_holidays, dt)
        self.assertNoHoliday(sk_holidays, dt)
        self.assertHolidayName("Louis Riel Day", mb_holidays, "2014-02-17")
        self.assertHolidayName("Heritage Day", ns_holidays, "2015-02-16")

    def test_st_patricks_day(self):
        nl_holidays = self.prov_hols["NL"]
        dt = (
            "1900-03-19",
            "1999-03-15",
            "2000-03-20",
            "2012-03-19",
            "2013-03-18",
            "2014-03-17",
            "2015-03-16",
            "2016-03-14",
            "2020-03-16",
        )
        self.assertNoHoliday(dt)
        self.assertHoliday(nl_holidays, dt)
        self.assertNoHoliday(nl_holidays, "1899-03-20")

    def test_good_friday(self):
        self.assertHoliday(
            "1900-04-13",
            "1901-04-05",
            "1902-03-28",
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
        )

    def test_easter_monday(self):
        self.assertHoliday(
            "1900-04-16",
            "1901-04-08",
            "1902-03-31",
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
        )

    def test_st_georges_day(self):
        dt = (
            "1990-04-23",
            "1999-04-26",
            "2010-04-19",
            "2016-04-25",
            "2020-04-20",
        )
        self.assertNoHoliday(dt)
        self.assertHoliday(self.prov_hols["NL"], dt)

    def test_victoria_day(self):
        dt = ("1953-05-18", "1999-05-24", "2000-05-22")
        self.assertHoliday(dt)
        for prov, holidays in self.prov_hols.items():
            if prov in {"NL", "NS", "PE", "QC"}:
                self.assertNoHoliday(holidays, dt)
            else:
                self.assertHoliday(holidays, dt)

        dt = ("2010-05-24", "2015-05-18", "2020-05-18")
        self.assertHoliday(dt)
        for prov, holidays in self.prov_hols.items():
            if prov in {"NL", "NS", "PE"}:
                self.assertNoHoliday(holidays, dt)
            else:
                self.assertHoliday(holidays, dt)

    def test_national_patriots_day(self):
        self.assertHolidayName(
            "National Patriots' Day",
            self.prov_hols["QC"],
            "2010-05-24",
            "2015-05-18",
            "2020-05-18",
            "2021-05-24",
            "2022-05-23",
        )

    def test_national_aboriginal_day(self):
        nt_holidays = self.prov_hols["NT"]
        self.assertNoHoliday(nt_holidays, "1995-06-21")
        self.assertNoHoliday(f"{year}-06-21" for year in range(1996, 2050))
        self.assertHoliday(nt_holidays, (f"{year}-06-21" for year in range(1996, 2050)))

    def test_st_jean_baptiste_day(self):
        qc_holidays = self.prov_hols["QC"]
        self.assertNoHoliday(qc_holidays, "1924-06-24")
        self.assertNoHoliday(f"{year}-06-24" for year in range(1925, 2050))
        self.assertHoliday(qc_holidays, (f"{year}-06-24" for year in range(1925, 2050)))
        self.assertHoliday(qc_holidays, "2001-06-25")
        self.assertNoNonObservedHoliday(Canada(subdiv="QC", observed=False), "2001-06-25")

    def test_discovery_day(self):
        nl_holidays = self.prov_hols["NL"]
        yt_holidays = self.prov_hols["YT"]
        dt = (
            "1997-06-23",
            "1999-06-21",
            "2000-06-26",
            "2010-06-21",
            "2016-06-27",
            "2020-06-22",
        )
        self.assertNoHoliday(dt)
        self.assertHoliday(nl_holidays, dt)
        self.assertNoHoliday(yt_holidays, dt)

        dt = (
            "1912-08-19",
            "1999-08-16",
            "2000-08-21",
            "2006-08-21",
            "2016-08-15",
            "2020-08-17",
        )
        self.assertNoHoliday(dt)
        self.assertNoHoliday(nl_holidays, dt)
        self.assertHoliday(yt_holidays, dt)

    def test_canada_day(self):
        self.assertHoliday(f"{year}-07-01" for year in range(1900, 2050))
        self.assertHoliday("2006-07-03", "2007-07-02")
        self.assertNoNonObservedHoliday("2006-07-03", "2007-07-02")

    def test_nunavut_day(self):
        nu_holidays = self.prov_hols["NU"]
        self.assertNoHoliday(nu_holidays, "1999-07-09", "2000-07-09")
        self.assertHoliday(nu_holidays, "2000-04-01")
        self.assertNoHoliday(f"{year}-07-09" for year in range(2001, 2050))
        self.assertHoliday(nu_holidays, (f"{year}-07-09" for year in range(2001, 2050)))
        self.assertHoliday(nu_holidays, "2017-07-10")
        self.assertNoNonObservedHoliday(Canada(subdiv="NU", observed=False), "2017-07-10")

    def test_civic_holiday_bc(self):
        bc_holidays = self.prov_hols["BC"]
        dt = (
            "1974-08-05",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertHoliday(bc_holidays, dt)
        self.assertNoHoliday(bc_holidays, "1973-08-06")

    def test_civic_holiday_mb(self):
        mb_holidays = self.prov_hols["MB"]
        dt = (
            "1900-08-06",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertHoliday(mb_holidays, dt)
        self.assertNoHoliday(mb_holidays, "1899-08-07")
        old_name = "Civic Holiday"
        new_name = "Terry Fox Day"
        self.assertHolidayName(old_name, mb_holidays, "2014-08-04")
        self.assertHolidayName(new_name, mb_holidays, "2015-08-03")
        self.assertNoHolidayName(old_name, mb_holidays, 2015)
        self.assertNoHolidayName(new_name, mb_holidays, 2014)

    def test_civic_holiday_nb_nt_sk(self):
        nb_holidays = self.prov_hols["NB"]
        nt_holidays = self.prov_hols["NT"]
        sk_holidays = self.prov_hols["SK"]
        dt = (
            "1900-08-06",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertHoliday(nb_holidays, dt)
        self.assertHoliday(nt_holidays, dt)
        self.assertHoliday(sk_holidays, dt)
        self.assertNoHoliday(nb_holidays, "1899-08-07")
        self.assertNoHoliday(nt_holidays, "1899-08-07")
        self.assertNoHoliday(sk_holidays, "1899-08-07")

    def test_labour_day(self):
        self.assertNoHoliday("1893-09-04")
        self.assertHoliday(
            "1894-09-03",
            "1900-09-03",
            "1999-09-06",
            "2000-09-04",
            "2014-09-01",
            "2015-09-07",
        )

    def test_national_day_for_truth_and_reconciliation(self):
        bc_holidays = self.prov_hols["BC"]
        mb_holidays = self.prov_hols["MB"]
        ns_holidays = self.prov_hols["NS"]

        dt = ("1991-09-30", "2020-09-30")
        self.assertNoHoliday(dt)
        self.assertNoHoliday(mb_holidays, dt)
        self.assertNoHoliday(ns_holidays, dt)

        dt = ("2021-09-30", "2022-09-30")
        self.assertHoliday(mb_holidays, dt)
        self.assertHoliday(ns_holidays, dt)
        self.assertNoHoliday(dt)

        dt = ("2023-09-30", "2024-09-30", "2030-09-30")
        self.assertHoliday(mb_holidays, dt)
        self.assertHoliday(ns_holidays, dt)
        self.assertHoliday(bc_holidays, dt)
        self.assertNoHoliday(dt)

    def test_thanksgiving(self):
        nb_holidays = self.prov_hols["NB"]
        nl_holidays = self.prov_hols["NL"]
        ns_holidays = self.prov_hols["NS"]
        pe_holidays = self.prov_hols["PE"]

        dt = (
            "1931-10-12",
            "1935-10-25",
            "1990-10-08",
            "1999-10-11",
            "2000-10-09",
            "2013-10-14",
            "2020-10-12",
        )
        self.assertHoliday(dt)
        self.assertNoHoliday(nb_holidays, dt)
        self.assertNoHoliday(nl_holidays, dt)
        self.assertNoHoliday(ns_holidays, dt)
        self.assertNoHoliday(pe_holidays, dt)

    def test_remembrance_day(self):
        ab_holidays = self.prov_hols["AB"]
        nl_holidays = self.prov_hols["NL"]
        self.assertNoHoliday(nl_holidays, "1930-11-11")
        self.assertNoHoliday(ab_holidays, "1930-11-11")

        self.assertNoHoliday(f"{year}-11-11" for year in range(1931, 2050))
        self.assertHoliday(ab_holidays, (f"{year}-11-11" for year in range(1931, 2050)))
        self.assertHoliday(nl_holidays, (f"{year}-11-11" for year in range(1931, 2050)))

        self.assertNoHoliday(ab_holidays, "2007-11-12")
        self.assertHoliday(nl_holidays, "2007-11-12")
        self.assertNoNonObservedHoliday(Canada(subdiv="AB", observed=False), "2007-11-12")
        self.assertNoNonObservedHoliday(Canada(subdiv="NL", observed=False), "2007-11-12")

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1900, 2050))
        self.assertHoliday("2010-12-27", "2011-12-27")
        self.assertNoNonObservedHoliday("2010-12-27", "2011-12-27")
        self.assertNotIn("Christmas Day (Observed)", self.holidays["2011-12-26"])
        self.assertHolidayName("Christmas Day (Observed)", "2011-12-27")

    def test_boxing_day(self):
        self.assertHoliday(f"{year}-12-26" for year in range(1900, 2050))
        self.assertHoliday("2009-12-28", "2010-12-27")
        self.assertNoNonObservedHoliday("2009-12-28", "2010-12-27")

    def test_queens_funeral(self):
        for prov, holidays in self.prov_hols.items():
            if prov in {"BC", "NB", "NL", "NS", "PE", "YT"}:
                self.assertHoliday(holidays, "2022-09-19")
            else:
                self.assertNoHoliday(holidays, "2022-09-19")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (Observed)"),
            ("2022-02-21", "Family Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-23", "Victoria Day"),
            ("2022-07-01", "Canada Day"),
            ("2022-08-01", "Civic Holiday"),
            ("2022-09-05", "Labour Day"),
            ("2022-10-10", "Thanksgiving"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (Observed)"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-01", "يوم السنة الجديدة"),
            ("2022-01-03", "(تمت ملاحظته) يوم السنة الجديدة"),
            ("2022-02-21", "يوم العائلة"),
            ("2022-04-15", "جمعة جيدة"),
            ("2022-04-18", "عيد الفصح الاثنين"),
            ("2022-05-23", "يوم فيكتوريا"),
            ("2022-07-01", "يوم كندا"),
            ("2022-08-01", "عطلة المدنية"),
            ("2022-09-05", "عيد العمال"),
            ("2022-10-10", "عيد الشكر"),
            ("2022-12-25", "عيد الميلاد"),
            ("2022-12-26", "يوم الملاكمة"),
            ("2022-12-27", "(تمت ملاحظته) عيد الميلاد"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Jour de l'an"),
            ("2022-01-03", "Jour de l'an (Observé)"),
            ("2022-02-21", "Fête de la famille"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-23", "Fête de la Reine"),
            ("2022-07-01", "Fête du Canada"),
            ("2022-08-01", "Premier lundi d'août"),
            ("2022-09-05", "Fête du Travail"),
            ("2022-10-10", "Action de grâce"),
            ("2022-12-25", "Jour de Noël"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Jour de Noël (Observé)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-03", "ชดเชยวันขึ้นปีใหม่"),
            ("2022-02-21", "วันครอบครัว"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-23", "วันวิคตอเรีย"),
            ("2022-07-01", "วันชาติแคนาดา"),
            ("2022-08-01", "วันหยุดราชการ"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันขอบคุณพระเจ้า"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "วันเปิดกล่องของขวัญ"),
            ("2022-12-27", "ชดเชยวันคริสต์มาส"),
        )
