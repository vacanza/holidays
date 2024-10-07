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

from holidays.constants import UNOFFICIAL
from holidays.countries.finland import Finland, FI, FIN
from tests.common import CommonCountryTests


class TestFinland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Finland)
        cls.unofficial_holidays = Finland(categories=UNOFFICIAL, years=range(1853, 2031))

    def test_country_aliases(self):
        self.assertAliases(Finland, FI, FIN)

    def test_fixed_holidays(self):
        for year in range(2010, 2030):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-01-06",
                f"{year}-05-01",
                f"{year}-12-06",
                f"{year}-12-24",
                f"{year}-12-25",
                f"{year}-12-26",
            )

    def test_epiphany(self):
        self.assertHolidayName(
            "Loppiainen",
            "1972-01-06",
            "1973-01-06",
            "1974-01-12",
            "1989-01-07",
            "1990-01-06",
            "1991-01-06",
        )
        self.assertNoHoliday(
            "1974-01-06",
            "1975-01-06",
            "1980-01-06",
            "1988-01-06",
            "1989-01-06",
        )

    def test_easter_holidays(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            # Easter Sunday
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            # Ascension Day
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            # Whit Sunday
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
        )

    def test_ascension_day(self):
        self.assertHoliday(
            "1971-05-20",
            "1972-05-11",
            "1973-05-26",
            "1974-05-18",
            "1989-04-29",
            "1990-05-19",
            "1991-05-09",
            "1992-05-28",
            "1993-05-20",
        )

        self.assertNoHoliday(
            "1973-05-31",
            "1974-05-23",
            "1980-05-15",
            "1988-05-12",
            "1989-05-04",
            "1990-05-24",
        )

    def test_midsummer_eve(self):
        name = "Juhannusaatto"
        self.assertHolidayName(
            name,
            "1953-06-23",
            "1954-06-23",
            "1955-06-24",
            "1956-06-22",
            "1957-06-21",
        )
        for dt in (
            "1955-06-23",
            "1956-06-23",
            "1957-06-23",
        ):
            self.assertNotIn(name, self.holidays.get(dt, ""))

    def test_midsummer_day(self):
        name = "Juhannuspäivä"
        self.assertHolidayName(
            name,
            "1953-06-24",
            "1954-06-24",
            "1955-06-25",
            "1956-06-23",
            "1957-06-22",
        )
        for dt in (
            "1955-06-24",
            "1956-06-24",
            "1957-06-24",
        ):
            self.assertNotIn(name, self.holidays.get(dt, ""))

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Pyhäinpäivä",
            "1952-11-01",
            "1953-11-01",
            "1954-11-01",
            "1955-11-05",
            "1956-11-03",
            "1957-11-02",
        )
        self.assertNoHoliday(
            "1955-11-01",
            "1956-11-01",
            "1957-11-01",
        )

    def _test_unofficial_holiday(self, name, since):
        start_year, month, day = (int(part) for part in since.split("-"))
        self.assertHolidayName(
            name,
            self.unofficial_holidays,
            (f"{year}-{month}-{day}" for year in range(start_year, 2031)),
        )
        self.assertNoHolidayName(name, self.unofficial_holidays, start_year - 1)

    def test_runeberg_day(self):
        self._test_unofficial_holiday("Runebergin päivä", "1854-02-05")

    def test_kalevala_day(self):
        self._test_unofficial_holiday(
            "Kalevalan päivä, suomalaisen kulttuurin päivä", "1860-02-28"
        )

    def test_minna_canth_day(self):
        self._test_unofficial_holiday("Minna Canthin päivä, tasa-arvon päivä", "2007-03-19")

    def test_agricola_day(self):
        self._test_unofficial_holiday("Mikael Agricolan päivä, suomen kielen päivä", "1978-04-09")

    def test_veterans_day(self):
        self._test_unofficial_holiday("Kansallinen veteraanipäivä", "1987-04-27")

    def test_europe_day(self):
        self._test_unofficial_holiday("Eurooppa-päivä", "2019-05-09")

    def test_mothers_day(self):
        self.assertHolidayName(
            "Äitienpäivä",
            self.unofficial_holidays,
            "1918-05-12",
            "1919-05-11",
            "2020-05-10",
            "2024-05-12",
        )
        self.assertNoHoliday(
            self.unofficial_holidays,
            "1917-05-13",
        )

    def test_finnish_identity_day(self):
        self._test_unofficial_holiday("J.V. Snellmanin päivä, suomalaisuuden päivä", "1952-05-12")

    def test_remembrance_day(self):
        self.assertHolidayName(
            "Kaatuneitten muistopäivä",
            self.unofficial_holidays,
            "1977-05-15",
            "1978-05-21",
            "1985-05-19",
            "2024-05-19",
            "2025-05-18",
        )
        self.assertNoHoliday(
            self.unofficial_holidays,
            "1976-05-16",
            "1975-05-18",
        )

    def test_defense_forces_day(self):
        self._test_unofficial_holiday("Puolustusvoimain lippujuhlan päivä", "1942-06-06")

    def test_eino_leino_day(self):
        self._test_unofficial_holiday("Eino Leinon päivä, runon ja suven päivä", "1992-07-06")

    def test_finnish_nature_day(self):
        self.assertHolidayName(
            "Suomen luonnon päivä",
            self.unofficial_holidays,
            "2013-08-31",
            "2014-08-30",
            "2024-08-31",
            "2025-08-30",
            "2026-08-29",
        )
        self.assertNoHoliday(
            self.unofficial_holidays,
            "2012-08-25",
            "2011-08-27",
        )

    def test_miina_sillanpaa_day(self):
        self._test_unofficial_holiday(
            "Miina Sillanpään ja kansalaisvaikuttamisen päivä", "2016-10-01"
        )

    def test_aleksis_kivi_day(self):
        self._test_unofficial_holiday(
            "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä", "1950-10-10"
        )

    def test_united_nations_day(self):
        self._test_unofficial_holiday("YK:n päivä", "1987-10-24")

    def test_finnish_swedish_heritage(self):
        self._test_unofficial_holiday("Ruotsalaisuuden päivä, Kustaa Aadolfin päivä", "1908-11-06")

    def test_fathers_day(self):
        self.assertHolidayName(
            "Isänpäivä",
            self.unofficial_holidays,
            "1949-11-13",
            "1950-11-12",
            "2020-11-08",
            "2024-11-10",
        )
        self.assertNoHoliday(
            self.unofficial_holidays,
            "1949-11-10",
        )

    def test_day_of_childrens_rights(self):
        self._test_unofficial_holiday("Lapsen oikeuksien päivä", "2020-11-20")

    def test_jean_sibelius_day(self):
        self._test_unofficial_holiday(
            "Jean Sibeliuksen päivä, suomalaisen musiikin päivä", "2007-12-08"
        )

    def test_unofficial_holidays(self):
        self.assertHolidays(
            Finland(categories=UNOFFICIAL, years=2024),
            ("2024-02-05", "Runebergin päivä"),
            ("2024-02-28", "Kalevalan päivä, suomalaisen kulttuurin päivä"),
            ("2024-03-19", "Minna Canthin päivä, tasa-arvon päivä"),
            ("2024-04-09", "Mikael Agricolan päivä, suomen kielen päivä"),
            ("2024-04-27", "Kansallinen veteraanipäivä"),
            ("2024-05-09", "Eurooppa-päivä"),
            ("2024-05-12", "J.V. Snellmanin päivä, suomalaisuuden päivä; Äitienpäivä"),
            ("2024-05-19", "Kaatuneitten muistopäivä"),
            ("2024-06-06", "Puolustusvoimain lippujuhlan päivä"),
            ("2024-07-06", "Eino Leinon päivä, runon ja suven päivä"),
            ("2024-08-31", "Suomen luonnon päivä"),
            ("2024-10-01", "Miina Sillanpään ja kansalaisvaikuttamisen päivä"),
            ("2024-10-10", "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä"),
            ("2024-10-24", "YK:n päivä"),
            ("2024-11-06", "Ruotsalaisuuden päivä, Kustaa Aadolfin päivä"),
            ("2024-11-10", "Isänpäivä"),
            ("2024-11-20", "Lapsen oikeuksien päivä"),
            ("2024-12-08", "Jean Sibeliuksen päivä, suomalaisen musiikin päivä"),
        )

    def test_2018(self):
        self.assertHolidays(
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
            ("2022-01-01", "Uudenvuodenpäivä"),
            ("2022-01-06", "Loppiainen"),
            ("2022-02-05", "Runebergin päivä"),
            ("2022-02-28", "Kalevalan päivä, suomalaisen kulttuurin päivä"),
            ("2022-03-19", "Minna Canthin päivä, tasa-arvon päivä"),
            ("2022-04-09", "Mikael Agricolan päivä, suomen kielen päivä"),
            ("2022-04-15", "Pitkäperjantai"),
            ("2022-04-17", "Pääsiäispäivä"),
            ("2022-04-18", "Toinen pääsiäispäivä"),
            ("2022-04-27", "Kansallinen veteraanipäivä"),
            ("2022-05-01", "Vappu"),
            ("2022-05-08", "Äitienpäivä"),
            ("2022-05-09", "Eurooppa-päivä"),
            ("2022-05-12", "J.V. Snellmanin päivä, suomalaisuuden päivä"),
            ("2022-05-15", "Kaatuneitten muistopäivä"),
            ("2022-05-26", "Helatorstai"),
            ("2022-06-05", "Helluntaipäivä"),
            ("2022-06-06", "Puolustusvoimain lippujuhlan päivä"),
            ("2022-06-24", "Juhannusaatto"),
            ("2022-06-25", "Juhannuspäivä"),
            ("2022-07-06", "Eino Leinon päivä, runon ja suven päivä"),
            ("2022-08-27", "Suomen luonnon päivä"),
            ("2022-10-01", "Miina Sillanpään ja kansalaisvaikuttamisen päivä"),
            ("2022-10-10", "Aleksis Kiven päivä, suomalaisen kirjallisuuden päivä"),
            ("2022-10-24", "YK:n päivä"),
            ("2022-11-05", "Pyhäinpäivä"),
            ("2022-11-06", "Ruotsalaisuuden päivä, Kustaa Aadolfin päivä"),
            ("2022-11-13", "Isänpäivä"),
            ("2022-11-20", "Lapsen oikeuksien päivä"),
            ("2022-12-06", "Itsenäisyyspäivä"),
            ("2022-12-08", "Jean Sibeliuksen päivä, suomalaisen musiikin päivä"),
            ("2022-12-24", "Jouluaatto"),
            ("2022-12-25", "Joulupäivä"),
            ("2022-12-26", "Tapaninpäivä"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-02-05", "Runeberg Day"),
            ("2022-02-28", "Kalevala Day, Day of Finnish Culture"),
            ("2022-03-19", "Minna Canth Day, Day of Equality"),
            ("2022-04-09", "Mikael Agricola Day, Day of the Finnish Language"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-27", "National War Veterans' Day"),
            ("2022-05-01", "May Day"),
            ("2022-05-08", "Mothers' Day"),
            ("2022-05-09", "Europe Day"),
            ("2022-05-12", "J. V. Snellman Day, Day of Finnish Heritage"),
            ("2022-05-15", "Remembrance Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Flag Day of the Finnish Defense Forces"),
            ("2022-06-24", "Midsummer Eve"),
            ("2022-06-25", "Midsummer Day"),
            ("2022-07-06", "Eino Leino Day, Day of Summer and Poetry"),
            ("2022-08-27", "Finland's Nature Day"),
            ("2022-10-01", "Miina Sillanpää Day, Day of Civic Participation"),
            ("2022-10-10", "Aleksis Kivi Day, Day of Finnish Literature"),
            ("2022-10-24", "United Nations Day"),
            ("2022-11-05", "All Saints' Day"),
            ("2022-11-06", "Finnish Swedish Heritage Day, svenska dagen"),
            ("2022-11-13", "Fathers' Day"),
            ("2022-11-20", "Day of Children's Rights"),
            ("2022-12-06", "Independence Day"),
            ("2022-12-08", "Jean Sibelius Day, Day of Finnish Music"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-02-05", "День Рунеберга"),
            ("2022-02-28", "День Калевали, День фінської культури"),
            ("2022-03-19", "День Мінни Кант, День рівності"),
            ("2022-04-09", "День Мікаеля Аґріколи, День фінської мови"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "Національний день ветеранів"),
            ("2022-05-01", "Ваппу"),
            ("2022-05-08", "День матері"),
            ("2022-05-09", "День Європи"),
            ("2022-05-12", "День Ю. В. Снелльмана, День фінської спадщини"),
            ("2022-05-15", "День ветеранів Національної війни"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День прапора фінських сил оборони"),
            ("2022-06-24", "Переддень літнього сонцестояння"),
            ("2022-06-25", "День літнього сонцестояння"),
            ("2022-07-06", "День Ейно Лейно, День літа та поезії"),
            ("2022-08-27", "День природи Фінляндії"),
            ("2022-10-01", "День Міїни Сілланпяя, День громадянської активності"),
            ("2022-10-10", "День Алексіса Ківі, День фінської літератури"),
            ("2022-10-24", "День ООН"),
            ("2022-11-05", "День усіх святих"),
            ("2022-11-06", "День фінської шведської спадщини, шведський день"),
            ("2022-11-13", "День батька"),
            ("2022-11-20", "День прав дитини"),
            ("2022-12-06", "День незалежності"),
            ("2022-12-08", "День Жана Сібеліуса, День фінської музики"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )

    def test_l10n_sv_fi(self):
        self.assertLocalizedHolidays(
            "sv_FI",
            ("2022-01-01", "Nyårsdagen"),
            ("2022-01-06", "Trettondag"),
            ("2022-02-05", "Runebergsdagen"),
            ("2022-02-28", "Kalevaladagen, den finska kulturens dag"),
            ("2022-03-19", "Minna Canth-dagen, jämställdhetsdagen"),
            ("2022-04-09", "Mikael Agricoladagen, finska språkets dag"),
            ("2022-04-15", "Långfredagen"),
            ("2022-04-17", "Påskdagen"),
            ("2022-04-18", "Annandag påsk"),
            ("2022-04-27", "Nationella veterandagen"),
            ("2022-05-01", "Första maj"),
            ("2022-05-08", "Mors dag"),
            ("2022-05-09", "Europadagen"),
            ("2022-05-12", "Snellmansdagen, finskhetens dag"),
            ("2022-05-15", "De stupades dag"),
            ("2022-05-26", "Kristi himmelsfärdsdag"),
            ("2022-06-05", "Pingst"),
            ("2022-06-06", "Dagen för försvarets fanfest"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-06-25", "Midsommardagen"),
            ("2022-07-06", "Eino Leino-dagen, diktens och sommarens dag"),
            ("2022-08-27", "Den finska naturens dag"),
            ("2022-10-01", "Miina Sillanpää-dagen, medborgarinflytandets dag"),
            ("2022-10-10", "Aleksis Kivi-dagen, den finska litteraturens dag"),
            ("2022-10-24", "FN-dagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-11-06", "Svenska dagen, Gustav Adolfsdagen"),
            ("2022-11-13", "Fars dag"),
            ("2022-11-20", "Barnkonventionens dag"),
            ("2022-12-06", "Självständigshetsdagen"),
            ("2022-12-08", "Sibeliusdagen, den finländska musikens dag"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
        )
