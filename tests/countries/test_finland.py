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

from holidays.constants import UNOFFICIAL, WORKDAY
from holidays.countries.finland import Finland
from tests.common import CommonCountryTests


class TestFinland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Finland)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Finland(years=1918, categories=WORKDAY))
        self.assertNoHolidays(Finland(years=1949, categories=UNOFFICIAL))

    def test_epiphany(self):
        name = "Loppiainen"
        self.assertHolidayName(
            name,
            "1972-01-06",
            # 1973 - 1990 changes.
            "1973-01-06",
            "1974-01-12",
            "1989-01-07",
            "1990-01-06",
            # 1991 - Present.
            "1991-01-06",
        )
        self.assertNoHolidayName(
            name,
            "1974-01-06",
            "1975-01-06",
            "1980-01-06",
            "1988-01-06",
            "1989-01-06",
        )
        self.assertHolidayName(
            name,
            (
                f"{year}-01-06"
                for year in (*range(self.start_year, 1973), *range(1991, self.end_year))
            ),
        )
        self.assertHolidayName(name, range(1973, 1991))

    def test_good_friday(self):
        name = "Pitkäperjantai"
        self.assertHolidayName(
            name,
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Pääsiäispäivä"
        self.assertHolidayName(
            name,
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Toinen pääsiäispäivä"
        self.assertHolidayName(
            name,
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertHolidayName(name, self.full_range)

    def test_ascension_day(self):
        name = "Helatorstai"
        self.assertHolidayName(
            name,
            "1971-05-20",
            "1972-05-11",
            # 1973 - 1990 changes.
            "1973-05-26",
            "1974-05-18",
            "1989-04-29",
            "1990-05-19",
            # 1991 - Present.
            "1991-05-09",
            "1992-05-28",
            "1993-05-20",
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
        )
        self.assertNoHolidayName(
            name,
            "1973-05-31",
            "1974-05-23",
            "1980-05-15",
            "1988-05-12",
            "1989-05-04",
            "1990-05-24",
        )
        self.assertHolidayName(name, self.full_range)

    def test_may_day(self):
        name = "Vappu"
        # PUBLIC.
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1944, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1944))
        # WORKDAY.
        self.assertWorkdayHolidayName(
            name, (f"{year}-05-01" for year in range(1979, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1979))

    def test_whit_sunday(self):
        name = "Helluntaipäivä"
        self.assertHolidayName(
            name,
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )
        self.assertHolidayName(name, self.full_range)

    def test_midsummer_eve(self):
        name = "Juhannusaatto"
        self.assertHolidayName(
            name,
            "1953-06-23",
            "1954-06-23",
            "1955-06-24",
            # 1955 - Present.
            "1956-06-22",
            "1957-06-21",
        )
        self.assertNoHolidayName(
            name,
            "1955-06-23",
            "1956-06-23",
            "1957-06-23",
        )
        self.assertHolidayName(name, (f"{year}-06-23" for year in range(self.start_year, 1955)))
        self.assertHolidayName(name, range(1955, self.end_year))

    def test_midsummer_day(self):
        name = "Juhannuspäivä"
        name_workday = "Suomen lipun päivä"
        dt = (
            "1953-06-24",
            "1954-06-24",
            # 1955 - Present.
            "1955-06-25",
            "1956-06-23",
            "1957-06-22",
        )
        dt_no_obs = (
            "1955-06-24",
            "1956-06-24",
            "1957-06-24",
        )
        # PUBLIC.
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, dt_no_obs)
        self.assertHolidayName(name, (f"{year}-06-24" for year in range(self.start_year, 1955)))
        self.assertHolidayName(name, range(1955, self.end_year))
        # WORKDAY.
        self.assertNoHolidayName(name_workday)
        self.assertWorkdayHolidayName(name_workday, dt)
        self.assertNoWorkdayHolidayName(name_workday, dt_no_obs)
        self.assertWorkdayHolidayName(
            name_workday, (f"{year}-06-24" for year in range(1934, 1955))
        )
        self.assertWorkdayHolidayName(name_workday, range(1955, self.end_year))
        self.assertNoWorkdayHolidayName(name_workday, range(self.start_year, 1934))

    def test_all_saints_day(self):
        name = "Pyhäinpäivä"
        self.assertHolidayName(
            name,
            "1952-11-01",
            "1953-11-01",
            "1954-11-01",
            # 1955 - Present.
            "1955-11-05",
            "1956-11-03",
            "1957-11-02",
        )
        self.assertNoHolidayName(
            name,
            "1955-11-01",
            "1956-11-01",
            "1957-11-01",
        )
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(self.start_year, 1955)))
        self.assertHolidayName(name, range(1955, self.end_year))

    def test_independence_day(self):
        name = "Itsenäisyyspäivä"
        # PUBLIC.
        self.assertHolidayName(name, (f"{year}-12-06" for year in range(1919, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1919))
        # WORKDAY.
        self.assertWorkdayHolidayName(
            name, (f"{year}-12-06" for year in range(1919, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1919))

    def _test_categorized_holiday(self, name, holidays_list, since, end_year=None):
        if end_year is None:
            end_year = self.end_year
        start_year, month, day = (int(p) for p in since.split("-"))
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            holidays_list,
            (f"{year}-{month:02d}-{day:02d}" for year in range(start_year, end_year)),
        )
        self.assertNoHolidayName(name, holidays_list, range(self.start_year, start_year))
        if end_year != self.end_year:
            self.assertNoHolidayName(name, holidays_list, range(end_year, self.end_year))

    def _test_unofficial_holiday(self, name, since, end_year=None):
        self._test_categorized_holiday(name, self.holidays_unofficial, since, end_year)

    def _test_workday_holiday(self, name, since, end_year=None):
        self._test_categorized_holiday(name, self.holidays_workday, since, end_year)

    def test_runeberg_day(self):
        self._test_unofficial_holiday("Runebergin päivä", "1976-02-05")

    def test_kalevala_day_day_of_finnish_culture(self):
        self._test_workday_holiday("Kalevalan päivä, suomalaisen kulttuurin päivä", "1920-02-28")

    def test_minna_canth_day_day_of_equality(self):
        self._test_unofficial_holiday("Minna Canthin päivä, tasa-arvon päivä", "2007-03-19")

    def test_mikael_agricola_day_day_of_finnish_language(self):
        self._test_unofficial_holiday("Mikael Agricolan päivä, suomen kielen päivä", "1980-04-09")

    def test_national_war_veterans_day(self):
        self._test_unofficial_holiday("Kansallinen veteraanipäivä", "1987-04-27")

    def test_europe_day(self):
        self._test_unofficial_holiday("Eurooppa-päivä", "2019-05-09")

    def test_mothers_day(self):
        name = "Äitienpäivä"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name,
            "1947-05-11",
            "1948-05-09",
            "2020-05-10",
            "2024-05-12",
        )
        self.assertWorkdayHolidayName(name, range(1947, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 1947))

    def test_j_v_snellmans_day_day_of_finnish_heritage(self):
        self._test_unofficial_holiday("J.V. Snellmanin päivä", "1952-05-12", 1978)
        self._test_unofficial_holiday("J.V. Snellmanin päivä, suomalaisuuden päivä", "1978-05-12")

    def test_remembrance_day(self):
        name = "Kaatuneitten muistopäivä"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name,
            "1977-05-15",
            "1978-05-21",
            "1985-05-19",
            "2024-05-19",
            "2025-05-18",
        )
        self.assertUnofficialHolidayName(name, range(1977, self.end_year))
        self.assertNoUnofficialHolidayName(name, range(self.start_year, 1977))

    def test_flag_day_of_the_finnish_defense_forces(self):
        self._test_workday_holiday("Suomen marsalkan syntymäpäivä", "1942-06-06", 1950)
        self._test_workday_holiday("Puolustusvoimain lippujuhlan päivä", "1950-06-06")

    def test_eino_leino_day_day_of_summer_and_poetry(self):
        self._test_unofficial_holiday("Eino Leinon päivä, runon ja suven päivä", "1998-07-06")

    def test_finlands_nature_day(self):
        name = "Suomen luonnon päivä"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name,
            "2023-08-26",
            "2024-08-31",
            "2025-08-30",
            "2026-08-29",
        )
        self.assertUnofficialHolidayName(name, range(2023, self.end_year))
        self.assertNoUnofficialHolidayName(name, range(self.start_year, 2023))

    def test_miina_sillanpaa_day_day_of_civic_participation(self):
        self._test_unofficial_holiday(
            "Miina Sillanpään ja kansalaisvaikuttamisen päivä", "2016-10-01"
        )

    def test_aleksis_kivi_day_day_of_finnish_literature(self):
        self._test_unofficial_holiday("Aleksis Kiven päivä", "1950-10-10", 1978)
        self._test_unofficial_holiday(
            "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä", "1978-10-10"
        )

    def test_united_nations_day(self):
        self._test_unofficial_holiday("YK:n päivä", "1987-10-24")

    def test_finnish_swedish_heritage_day_svenska_dagen(self):
        self._test_unofficial_holiday("Ruotsalaisuuden päivä, Kustaa Aadolfin päivä", "1979-11-06")

    def test_fathers_day(self):
        name = "Isänpäivä"
        self.assertNoHolidayName(name)
        # UNOFFICIAL.
        self.assertUnofficialHolidayName(
            name,
            "1987-11-08",
            "1988-11-13",
            "2017-11-12",
            "2018-11-11",
        )
        self.assertUnofficialHolidayName(name, range(1987, 2019))
        self.assertNoUnofficialHolidayName(
            name, range(self.start_year, 1987), range(2019, self.end_year)
        )
        # WORKDAY.
        self.assertWorkdayHolidayName(
            name,
            "2019-11-10",
            "2020-11-08",
            "2021-11-14",
            "2024-11-10",
        )
        self.assertWorkdayHolidayName(name, range(2019, self.end_year))
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2019))

    def test_day_of_childrens_rights(self):
        self._test_unofficial_holiday("Lapsen oikeuksien päivä", "2020-11-20")

    def test_jean_sibelius_day_day_of_finnish_music(self):
        self._test_unofficial_holiday(
            "Jean Sibeliuksen päivä, suomalaisen musiikin päivä", "2011-12-08"
        )

    def test_alands_autonomy_day(self):
        name = "Ahvenanmaan itsehallintopäivä"
        self.assertNoHolidayName(name)
        self.assertSubdiv01HolidayName(
            name, (f"{year}-06-09" for year in range(1993, self.end_year))
        )
        self.assertNoSubdiv01HolidayName(name, range(self.start_year, 1993))

    def test_unofficial_holidays(self):
        self.assertHolidays(
            Finland(categories=UNOFFICIAL, years=2024),
            ("2024-02-05", "Runebergin päivä"),
            ("2024-03-19", "Minna Canthin päivä, tasa-arvon päivä"),
            ("2024-04-09", "Mikael Agricolan päivä, suomen kielen päivä"),
            ("2024-04-27", "Kansallinen veteraanipäivä"),
            ("2024-05-09", "Eurooppa-päivä"),
            ("2024-05-12", "J.V. Snellmanin päivä, suomalaisuuden päivä"),
            ("2024-05-19", "Kaatuneitten muistopäivä"),
            ("2024-07-06", "Eino Leinon päivä, runon ja suven päivä"),
            ("2024-08-31", "Suomen luonnon päivä"),
            ("2024-10-01", "Miina Sillanpään ja kansalaisvaikuttamisen päivä"),
            ("2024-10-10", "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä"),
            ("2024-10-24", "YK:n päivä"),
            ("2024-11-06", "Ruotsalaisuuden päivä, Kustaa Aadolfin päivä"),
            ("2024-11-20", "Lapsen oikeuksien päivä"),
            ("2024-12-08", "Jean Sibeliuksen päivä, suomalaisen musiikin päivä"),
        )

    def test_workday_holidays(self):
        self.assertHolidays(
            Finland(categories=WORKDAY, years=2024),
            ("2024-02-28", "Kalevalan päivä, suomalaisen kulttuurin päivä"),
            ("2024-05-01", "Vappu"),
            ("2024-05-12", "Äitienpäivä"),
            ("2024-06-06", "Puolustusvoimain lippujuhlan päivä"),
            ("2024-06-22", "Suomen lipun päivä"),
            ("2024-11-10", "Isänpäivä"),
            ("2024-12-06", "Itsenäisyyspäivä"),
        )

    def test_2018(self):
        self.assertHolidays(
            Finland(years=2018),
            ("2018-01-01", "Uudenvuodenpäivä"),
            ("2018-01-06", "Loppiainen"),
            ("2018-03-30", "Pitkäperjantai"),
            ("2018-04-01", "Pääsiäispäivä"),
            ("2018-04-02", "Toinen pääsiäispäivä"),
            ("2018-05-01", "Vappu"),
            ("2018-05-10", "Helatorstai"),
            ("2018-05-20", "Helluntaipäivä"),
            ("2018-06-22", "Juhannusaatto"),
            ("2018-06-23", "Juhannuspäivä"),
            ("2018-11-03", "Pyhäinpäivä"),
            ("2018-12-06", "Itsenäisyyspäivä"),
            ("2018-12-24", "Jouluaatto"),
            ("2018-12-25", "Joulupäivä"),
            ("2018-12-26", "Tapaninpäivä"),
        )

    def test_2022(self):
        self.assertHolidays(
            Finland(years=2022),
            ("2022-01-01", "Uudenvuodenpäivä"),
            ("2022-01-06", "Loppiainen"),
            ("2022-04-15", "Pitkäperjantai"),
            ("2022-04-17", "Pääsiäispäivä"),
            ("2022-04-18", "Toinen pääsiäispäivä"),
            ("2022-05-01", "Vappu"),
            ("2022-05-26", "Helatorstai"),
            ("2022-06-05", "Helluntaipäivä"),
            ("2022-06-24", "Juhannusaatto"),
            ("2022-06-25", "Juhannuspäivä"),
            ("2022-11-05", "Pyhäinpäivä"),
            ("2022-12-06", "Itsenäisyyspäivä"),
            ("2022-12-24", "Jouluaatto"),
            ("2022-12-25", "Joulupäivä"),
            ("2022-12-26", "Tapaninpäivä"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Uudenvuodenpäivä"),
            ("2024-01-06", "Loppiainen"),
            ("2024-02-05", "Runebergin päivä"),
            ("2024-02-28", "Kalevalan päivä, suomalaisen kulttuurin päivä"),
            ("2024-03-19", "Minna Canthin päivä, tasa-arvon päivä"),
            ("2024-03-29", "Pitkäperjantai"),
            ("2024-03-31", "Pääsiäispäivä"),
            ("2024-04-01", "Toinen pääsiäispäivä"),
            ("2024-04-09", "Mikael Agricolan päivä, suomen kielen päivä"),
            ("2024-04-27", "Kansallinen veteraanipäivä"),
            ("2024-05-01", "Vappu"),
            ("2024-05-09", "Eurooppa-päivä; Helatorstai"),
            ("2024-05-12", "J.V. Snellmanin päivä, suomalaisuuden päivä; Äitienpäivä"),
            ("2024-05-19", "Helluntaipäivä; Kaatuneitten muistopäivä"),
            ("2024-06-06", "Puolustusvoimain lippujuhlan päivä"),
            ("2024-06-09", "Ahvenanmaan itsehallintopäivä"),
            ("2024-06-21", "Juhannusaatto"),
            ("2024-06-22", "Juhannuspäivä; Suomen lipun päivä"),
            ("2024-07-06", "Eino Leinon päivä, runon ja suven päivä"),
            ("2024-08-31", "Suomen luonnon päivä"),
            ("2024-10-01", "Miina Sillanpään ja kansalaisvaikuttamisen päivä"),
            ("2024-10-10", "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä"),
            ("2024-10-24", "YK:n päivä"),
            ("2024-11-02", "Pyhäinpäivä"),
            ("2024-11-06", "Ruotsalaisuuden päivä, Kustaa Aadolfin päivä"),
            ("2024-11-10", "Isänpäivä"),
            ("2024-11-20", "Lapsen oikeuksien päivä"),
            ("2024-12-06", "Itsenäisyyspäivä"),
            ("2024-12-08", "Jean Sibeliuksen päivä, suomalaisen musiikin päivä"),
            ("2024-12-24", "Jouluaatto"),
            ("2024-12-25", "Joulupäivä"),
            ("2024-12-26", "Tapaninpäivä"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-06", "Epiphany"),
            ("2024-02-05", "Runeberg Day"),
            ("2024-02-28", "Kalevala Day, Day of Finnish Culture"),
            ("2024-03-19", "Minna Canth Day, Day of Equality"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-09", "Mikael Agricola Day, Day of the Finnish Language"),
            ("2024-04-27", "National War Veterans' Day"),
            ("2024-05-01", "May Day"),
            ("2024-05-09", "Ascension Day; Europe Day"),
            ("2024-05-12", "J. V. Snellman Day, Day of Finnish Heritage; Mother's Day"),
            ("2024-05-19", "Remembrance Day; Whit Sunday"),
            ("2024-06-06", "Flag Day of the Finnish Defense Forces"),
            ("2024-06-09", "Åland's Autonomy Day"),
            ("2024-06-21", "Midsummer Eve"),
            ("2024-06-22", "Day of the Finnish Flag; Midsummer Day"),
            ("2024-07-06", "Eino Leino Day, Day of Summer and Poetry"),
            ("2024-08-31", "Finland's Nature Day"),
            ("2024-10-01", "Miina Sillanpää Day, Day of Civic Participation"),
            ("2024-10-10", "Aleksis Kivi Day, Day of Finnish Literature"),
            ("2024-10-24", "United Nations Day"),
            ("2024-11-02", "All Saints' Day"),
            ("2024-11-06", "Finnish Swedish Heritage Day, svenska dagen"),
            ("2024-11-10", "Father's Day"),
            ("2024-11-20", "Day of Children's Rights"),
            ("2024-12-06", "Independence Day"),
            ("2024-12-08", "Jean Sibelius Day, Day of Finnish Music"),
            ("2024-12-24", "Christmas Eve"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Second Day of Christmas"),
        )

    def test_l10n_sv_fi(self):
        self.assertLocalizedHolidays(
            "sv_FI",
            ("2024-01-01", "Nyårsdagen"),
            ("2024-01-06", "Trettondag"),
            ("2024-02-05", "Runebergsdagen"),
            ("2024-02-28", "Kalevaladagen, den finska kulturens dag"),
            ("2024-03-19", "Minna Canth-dagen, jämställdhetsdagen"),
            ("2024-03-29", "Långfredagen"),
            ("2024-03-31", "Påskdagen"),
            ("2024-04-01", "Annandag påsk"),
            ("2024-04-09", "Mikael Agricoladagen, finska språkets dag"),
            ("2024-04-27", "Nationella veterandagen"),
            ("2024-05-01", "Första maj"),
            ("2024-05-09", "Europadagen; Kristi himmelsfärdsdag"),
            ("2024-05-12", "Mors dag; Snellmansdagen, finskhetens dag"),
            ("2024-05-19", "De stupades dag; Pingst"),
            ("2024-06-06", "Dagen för försvarets fanfest"),
            ("2024-06-09", "Ålands självstyrelsedag"),
            ("2024-06-21", "Midsommarafton"),
            ("2024-06-22", "Finlands flaggas dag; Midsommardagen"),
            ("2024-07-06", "Eino Leino-dagen, diktens och sommarens dag"),
            ("2024-08-31", "Den finska naturens dag"),
            ("2024-10-01", "Miina Sillanpää-dagen, medborgarinflytandets dag"),
            ("2024-10-10", "Aleksis Kivi-dagen, den finska litteraturens dag"),
            ("2024-10-24", "FN-dagen"),
            ("2024-11-02", "Alla helgons dag"),
            ("2024-11-06", "Svenska dagen, Gustav Adolfsdagen"),
            ("2024-11-10", "Fars dag"),
            ("2024-11-20", "Barnkonventionens dag"),
            ("2024-12-06", "Självständighetsdagen"),
            ("2024-12-08", "Sibeliusdagen, den finländska musikens dag"),
            ("2024-12-24", "Julafton"),
            ("2024-12-25", "Juldagen"),
            ("2024-12-26", "Annandag jul"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2024-02-05", "วันรูนแบร์ก"),
            ("2024-02-28", "วันกาเลวาลา, วันวัฒนธรรมฟินแลนด์"),
            ("2024-03-19", "วันมินน่า คานท์, วันแห่งความเสมอภาค"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-03-31", "วันอาทิตย์อีสเตอร์"),
            ("2024-04-01", "วันจันทร์อีสเตอร์"),
            ("2024-04-09", "วันมิคาเอล อากริโคลา, วันภาษาฟินแลนด์"),
            ("2024-04-27", "วันทหารผ่านศึกแห่งชาติ"),
            ("2024-05-01", "วันเมย์เดย์ (วันแรงงาน)"),
            ("2024-05-09", "วันยุโรป; วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2024-05-12", "วันเจ.วี. สเนลล์มาน, วันมรดกฟินแลนด์; วันแม่"),
            ("2024-05-19", "วันรำลึก; วันสมโภชพระจิตเจ้า"),
            ("2024-06-06", "วันกองกำลังป้องกันฟินแลนด์"),
            ("2024-06-09", "วันปกครองตนเองหมู่เกาะโอลันด์"),
            ("2024-06-21", "วันมิดซัมเมอร์อีฟ (วันก่อนวันกลางฤดูร้อน)"),
            ("2024-06-22", "วันธงชาติฟินแลนด์; วันมิดซัมเมอร์ (วันกลางฤดูร้อน)"),
            ("2024-07-06", "วันไอนอ ไลโน, วันแห่งบทกวีและฤดูร้อน"),
            ("2024-08-31", "วันสิ่งแวดล้อมฟินแลนด์"),
            ("2024-10-01", "วันมีนา ซิลลันแป, วันส่งเสริมการมีส่วนร่วมของพลเมือง"),
            ("2024-10-10", "วันอเล็กซิส กีวี, วันวรรณกรรมฟินแลนด์"),
            ("2024-10-24", "วันสหประชาชาติ"),
            ("2024-11-02", "วันสมโภชนักบุญทั้งหลาย"),
            ("2024-11-06", "วันมรดกสวีเดน-ฟินแลนด์, วันกุสตาฟวัส อดอลฟัส"),
            ("2024-11-10", "วันพ่อ"),
            ("2024-11-20", "วันสิทธิเด็ก"),
            ("2024-12-06", "วันประกาศอิสรภาพฟินแลนด์"),
            ("2024-12-08", "วันฌอง ซิเบลิอุส, วันดนตรีฟินแลนด์"),
            ("2024-12-24", "วันคริสต์มาสอีฟ"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-26", "วันคริสต์มาสวันที่สอง"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-06", "Богоявлення"),
            ("2024-02-05", "День Рунеберга"),
            ("2024-02-28", "День Калевали, День фінської культури"),
            ("2024-03-19", "День Мінни Кант, День рівності"),
            ("2024-03-29", "Страсна пʼятниця"),
            ("2024-03-31", "Великдень"),
            ("2024-04-01", "Великодній понеділок"),
            ("2024-04-09", "День Мікаеля Аґріколи, День фінської мови"),
            ("2024-04-27", "Національний день ветеранів"),
            ("2024-05-01", "Ваппу"),
            ("2024-05-09", "Вознесіння Господнє; День Європи"),
            ("2024-05-12", "День Ю. В. Снелльмана, День фінської спадщини; День матері"),
            ("2024-05-19", "День ветеранів Національної війни; Трійця"),
            ("2024-06-06", "День прапора фінських сил оборони"),
            ("2024-06-09", "День автономії Аландських островів"),
            ("2024-06-21", "Переддень літнього сонцестояння"),
            ("2024-06-22", "День літнього сонцестояння; День прапора Фінляндії"),
            ("2024-07-06", "День Ейно Лейно, День літа та поезії"),
            ("2024-08-31", "День природи Фінляндії"),
            ("2024-10-01", "День Міїни Сілланпяя, День громадянської активності"),
            ("2024-10-10", "День Алексіса Ківі, День фінської літератури"),
            ("2024-10-24", "День ООН"),
            ("2024-11-02", "День усіх святих"),
            ("2024-11-06", "День фінської шведської спадщини, шведський день"),
            ("2024-11-10", "День батька"),
            ("2024-11-20", "День прав дитини"),
            ("2024-12-06", "День незалежності"),
            ("2024-12-08", "День Жана Сібеліуса, День фінської музики"),
            ("2024-12-24", "Святий вечір"),
            ("2024-12-25", "Різдво Христове"),
            ("2024-12-26", "Другий день Різдва"),
        )
