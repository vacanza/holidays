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

from holidays.countries.vatican_city import VaticanCity
from tests.common import CommonCountryTests


class TestVaticanCity(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(VaticanCity, years=range(1929, 2050))

    def test_solemnity_of_mary_mother_of_god(self):
        self.assertHolidayName(
            "Solennità di Maria Santissima Madre di Dio",
            (f"{year}-01-01" for year in range(1929, 2050)),
        )

    def test_epiphany(self):
        self.assertHolidayName(
            "Epifania del Signore", (f"{year}-01-06" for year in range(1929, 2050))
        )

    def test_anniversary_of_the_foundation_of_vatican_city(self):
        self.assertHolidayName(
            "Anniversario della istituzione dello Stato della Città del Vaticano",
            (f"{year}-02-11" for year in range(1929, 2050)),
        )

    def test_anniversary_election_of_holy_father(self):
        name = "Anniversario dell'Elezione del Santo Padre"
        self.assertHolidayName(name, (f"{year}-02-06" for year in range(1929, 1940)))
        self.assertHolidayName(name, (f"{year}-03-02" for year in range(1940, 1959)))
        self.assertHolidayName(name, (f"{year}-10-28" for year in range(1959, 1963)))
        self.assertHolidayName(name, (f"{year}-06-21" for year in range(1964, 1979)))
        self.assertHolidayName(name, (f"{year}-10-16" for year in range(1979, 2005)))
        self.assertHolidayName(name, (f"{year}-04-19" for year in range(2006, 2013)))
        self.assertHolidayName(name, (f"{year}-03-13" for year in range(2014, 2026)))
        self.assertHolidayName(name, (f"{year}-05-08" for year in range(2026, 2050)))
        self.assertNoHolidayName(name, 1963, 2005, 2013)

    def test_name_day_of_holy_father(self):
        name = "Onomastico del Santo Padre"
        self.assertHolidayName(name, (f"{year}-11-04" for year in range(1978, 2005)))
        self.assertHolidayName(name, (f"{year}-03-19" for year in range(2006, 2013)))
        self.assertHolidayName(name, (f"{year}-04-23" for year in range(2013, 2026)))
        self.assertHolidayName(name, (f"{year}-09-17" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1929, 1978), 2005)

    def test_saint_josephs_day(self):
        self.assertHolidayName("San Giuseppe", (f"{year}-03-19" for year in range(1929, 2050)))

    def test_maundy_thursday(self):
        name = "Giovedì Santo"
        self.assertHolidayName(
            name,
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_good_friday(self):
        name = "Venerdì Santo"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_holy_saturday(self):
        name = "Sabato Santo"
        self.assertHolidayName(
            name,
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_easter_sunday(self):
        name = "Pasqua di Resurrezione"
        self.assertHolidayName(
            name,
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_easter_monday(self):
        name = "Lunedì dell'Angelo"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_easter_tuesday(self):
        name = "Martedì in Albis"
        self.assertHolidayName(
            name,
            "2019-04-23",
            "2020-04-14",
            "2021-04-06",
            "2022-04-19",
            "2023-04-11",
            "2024-04-02",
            "2025-04-22",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_ascension_day(self):
        name = "Ascensione del Signore"
        self.assertHolidayName(
            name,
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_corpus_domini(self):
        name = "Corpus Domini"
        self.assertHolidayName(
            name,
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_saint_joseph_the_workers_day(self):
        name = "San Giuseppe Artigiano"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1955, 2050)))
        self.assertNoHolidayName(name, range(1929, 1955))

    def test_solemnity_of_pentecost(self):
        name = "Solennità della Pentecoste"
        self.assertHolidayName(
            name,
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_solemnity_of_holy_trinity(self):
        name = "Solennità della Santissima Trinità"
        self.assertHolidayName(
            name,
            "2019-06-16",
            "2020-06-07",
            "2021-05-30",
            "2022-06-12",
            "2023-06-04",
            "2024-05-26",
            "2025-06-15",
        )
        self.assertHolidayName(name, range(1929, 2050))

    def test_saints_peter_and_paul_day(self):
        self.assertHolidayName(
            "Santi Pietro e Paolo", (f"{year}-06-29" for year in range(1929, 2050))
        )

    def test_assumption_day(self):
        self.assertHolidayName(
            "Vigilia dell'Assunzione di Maria Santissima",
            (f"{year}-08-14" for year in range(1929, 2050)),
        )
        self.assertHolidayName(
            "Assunzione di Maria Santissima", (f"{year}-08-15" for year in range(1929, 2050))
        )
        self.assertHolidayName(
            "Giorno Successivo all'Assunzione di Maria Santissima",
            (f"{year}-08-16" for year in range(1929, 2050)),
        )

    def test_all_saints_day(self):
        self.assertHolidayName("Tutti i Santi", (f"{year}-11-01" for year in range(1929, 2050)))

    def test_all_souls_day(self):
        self.assertHolidayName(
            "Tutti i Fedeli Defunti", (f"{year}-11-02" for year in range(1929, 2050))
        )

    def test_immaculate_conception(self):
        self.assertHolidayName(
            "Immacolata Concezione", (f"{year}-12-08" for year in range(1929, 2050))
        )

    def test_christmas_days(self):
        self.assertHolidayName(
            "Vigilia di Natale", (f"{year}-12-24" for year in range(1929, 2050))
        )
        self.assertHolidayName("Natale", (f"{year}-12-25" for year in range(1929, 2050)))
        self.assertHolidayName("Santo Stefano", (f"{year}-12-26" for year in range(1929, 2050)))
        self.assertHolidayName("San Giovanni", (f"{year}-12-27" for year in range(1929, 2050)))

    def test_last_day_of_the_year(self):
        self.assertHolidayName(
            "Ultimo giorno dell'anno", (f"{year}-12-31" for year in range(1929, 2050))
        )

    def test_2020(self):
        # https://www.vaticanstate.va/images/pdf/CALENDARIO_2020.pdf
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "Solennità di Maria Santissima Madre di Dio"),
            ("2020-01-06", "Epifania del Signore"),
            ("2020-02-11", "Anniversario della istituzione dello Stato della Città del Vaticano"),
            ("2020-03-13", "Anniversario dell'Elezione del Santo Padre"),
            ("2020-03-19", "San Giuseppe"),
            ("2020-04-09", "Giovedì Santo"),
            ("2020-04-10", "Venerdì Santo"),
            ("2020-04-11", "Sabato Santo"),
            ("2020-04-12", "Pasqua di Resurrezione"),
            ("2020-04-13", "Lunedì dell'Angelo"),
            ("2020-04-14", "Martedì in Albis"),
            ("2020-04-23", "Onomastico del Santo Padre"),
            ("2020-05-01", "San Giuseppe Artigiano"),
            ("2020-05-21", "Ascensione del Signore"),
            ("2020-05-31", "Solennità della Pentecoste"),
            ("2020-06-07", "Solennità della Santissima Trinità"),
            ("2020-06-11", "Corpus Domini"),
            ("2020-06-29", "Santi Pietro e Paolo"),
            ("2020-08-14", "Vigilia dell'Assunzione di Maria Santissima"),
            ("2020-08-15", "Assunzione di Maria Santissima"),
            ("2020-08-16", "Giorno Successivo all'Assunzione di Maria Santissima"),
            ("2020-11-01", "Tutti i Santi"),
            ("2020-11-02", "Tutti i Fedeli Defunti"),
            ("2020-12-08", "Immacolata Concezione"),
            ("2020-12-24", "Vigilia di Natale"),
            ("2020-12-25", "Natale"),
            ("2020-12-26", "Santo Stefano"),
            ("2020-12-27", "San Giovanni"),
            ("2020-12-31", "Ultimo giorno dell'anno"),
        )

    def test_2021(self):
        # https://www.farmaciavaticana.va/images/pdf/calendario_2021.pdf
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Solennità di Maria Santissima Madre di Dio"),
            ("2021-01-06", "Epifania del Signore"),
            ("2021-02-11", "Anniversario della istituzione dello Stato della Città del Vaticano"),
            ("2021-03-13", "Anniversario dell'Elezione del Santo Padre"),
            ("2021-03-19", "San Giuseppe"),
            ("2021-04-01", "Giovedì Santo"),
            ("2021-04-02", "Venerdì Santo"),
            ("2021-04-03", "Sabato Santo"),
            ("2021-04-04", "Pasqua di Resurrezione"),
            ("2021-04-05", "Lunedì dell'Angelo"),
            ("2021-04-06", "Martedì in Albis"),
            ("2021-04-23", "Onomastico del Santo Padre"),
            ("2021-05-01", "San Giuseppe Artigiano"),
            ("2021-05-13", "Ascensione del Signore"),
            ("2021-05-23", "Solennità della Pentecoste"),
            ("2021-05-30", "Solennità della Santissima Trinità"),
            ("2021-06-03", "Corpus Domini"),
            ("2021-06-29", "Santi Pietro e Paolo"),
            ("2021-08-14", "Vigilia dell'Assunzione di Maria Santissima"),
            ("2021-08-15", "Assunzione di Maria Santissima"),
            ("2021-08-16", "Giorno Successivo all'Assunzione di Maria Santissima"),
            ("2021-11-01", "Tutti i Santi"),
            ("2021-11-02", "Tutti i Fedeli Defunti"),
            ("2021-12-08", "Immacolata Concezione"),
            ("2021-12-24", "Vigilia di Natale"),
            ("2021-12-25", "Natale"),
            ("2021-12-26", "Santo Stefano"),
            ("2021-12-27", "San Giovanni"),
            ("2021-12-31", "Ultimo giorno dell'anno"),
        )

    def test_2022(self):
        # https://www.farmaciavaticana.va/images/pdf/calendario_2022.pdf
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Solennità di Maria Santissima Madre di Dio"),
            ("2022-01-06", "Epifania del Signore"),
            ("2022-02-11", "Anniversario della istituzione dello Stato della Città del Vaticano"),
            ("2022-03-13", "Anniversario dell'Elezione del Santo Padre"),
            ("2022-03-19", "San Giuseppe"),
            ("2022-04-14", "Giovedì Santo"),
            ("2022-04-15", "Venerdì Santo"),
            ("2022-04-16", "Sabato Santo"),
            ("2022-04-17", "Pasqua di Resurrezione"),
            ("2022-04-18", "Lunedì dell'Angelo"),
            ("2022-04-19", "Martedì in Albis"),
            ("2022-04-23", "Onomastico del Santo Padre"),
            ("2022-05-01", "San Giuseppe Artigiano"),
            ("2022-05-26", "Ascensione del Signore"),
            ("2022-06-05", "Solennità della Pentecoste"),
            ("2022-06-12", "Solennità della Santissima Trinità"),
            ("2022-06-16", "Corpus Domini"),
            ("2022-06-29", "Santi Pietro e Paolo"),
            ("2022-08-14", "Vigilia dell'Assunzione di Maria Santissima"),
            ("2022-08-15", "Assunzione di Maria Santissima"),
            ("2022-08-16", "Giorno Successivo all'Assunzione di Maria Santissima"),
            ("2022-11-01", "Tutti i Santi"),
            ("2022-11-02", "Tutti i Fedeli Defunti"),
            ("2022-12-08", "Immacolata Concezione"),
            ("2022-12-24", "Vigilia di Natale"),
            ("2022-12-25", "Natale"),
            ("2022-12-26", "Santo Stefano"),
            ("2022-12-27", "San Giovanni"),
            ("2022-12-31", "Ultimo giorno dell'anno"),
        )

    def test_2023(self):
        # https://www.farmaciavaticana.va/images/pdf/calendario_2023.pdf
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "Solennità di Maria Santissima Madre di Dio"),
            ("2023-01-06", "Epifania del Signore"),
            ("2023-02-11", "Anniversario della istituzione dello Stato della Città del Vaticano"),
            ("2023-03-13", "Anniversario dell'Elezione del Santo Padre"),
            ("2023-03-19", "San Giuseppe"),
            ("2023-04-06", "Giovedì Santo"),
            ("2023-04-07", "Venerdì Santo"),
            ("2023-04-08", "Sabato Santo"),
            ("2023-04-09", "Pasqua di Resurrezione"),
            ("2023-04-10", "Lunedì dell'Angelo"),
            ("2023-04-11", "Martedì in Albis"),
            ("2023-04-23", "Onomastico del Santo Padre"),
            ("2023-05-01", "San Giuseppe Artigiano"),
            ("2023-05-18", "Ascensione del Signore"),
            ("2023-05-28", "Solennità della Pentecoste"),
            ("2023-06-04", "Solennità della Santissima Trinità"),
            ("2023-06-08", "Corpus Domini"),
            ("2023-06-29", "Santi Pietro e Paolo"),
            ("2023-08-14", "Vigilia dell'Assunzione di Maria Santissima"),
            ("2023-08-15", "Assunzione di Maria Santissima"),
            ("2023-08-16", "Giorno Successivo all'Assunzione di Maria Santissima"),
            ("2023-11-01", "Tutti i Santi"),
            ("2023-11-02", "Tutti i Fedeli Defunti"),
            ("2023-12-08", "Immacolata Concezione"),
            ("2023-12-24", "Vigilia di Natale"),
            ("2023-12-25", "Natale"),
            ("2023-12-26", "Santo Stefano"),
            ("2023-12-27", "San Giovanni"),
            ("2023-12-31", "Ultimo giorno dell'anno"),
        )

    def test_2024(self):
        # https://www.farmaciavaticana.va/media/attachments/2024/01/02/calendario_2024.pdf
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Solennità di Maria Santissima Madre di Dio"),
            ("2024-01-06", "Epifania del Signore"),
            ("2024-02-11", "Anniversario della istituzione dello Stato della Città del Vaticano"),
            ("2024-03-13", "Anniversario dell'Elezione del Santo Padre"),
            ("2024-03-19", "San Giuseppe"),
            ("2024-03-28", "Giovedì Santo"),
            ("2024-03-29", "Venerdì Santo"),
            ("2024-03-30", "Sabato Santo"),
            ("2024-03-31", "Pasqua di Resurrezione"),
            ("2024-04-01", "Lunedì dell'Angelo"),
            ("2024-04-02", "Martedì in Albis"),
            ("2024-04-23", "Onomastico del Santo Padre"),
            ("2024-05-01", "San Giuseppe Artigiano"),
            ("2024-05-09", "Ascensione del Signore"),
            ("2024-05-19", "Solennità della Pentecoste"),
            ("2024-05-26", "Solennità della Santissima Trinità"),
            ("2024-05-30", "Corpus Domini"),
            ("2024-06-29", "Santi Pietro e Paolo"),
            ("2024-08-14", "Vigilia dell'Assunzione di Maria Santissima"),
            ("2024-08-15", "Assunzione di Maria Santissima"),
            ("2024-08-16", "Giorno Successivo all'Assunzione di Maria Santissima"),
            ("2024-11-01", "Tutti i Santi"),
            ("2024-11-02", "Tutti i Fedeli Defunti"),
            ("2024-12-08", "Immacolata Concezione"),
            ("2024-12-24", "Vigilia di Natale"),
            ("2024-12-25", "Natale"),
            ("2024-12-26", "Santo Stefano"),
            ("2024-12-27", "San Giovanni"),
            ("2024-12-31", "Ultimo giorno dell'anno"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Solennità di Maria Santissima Madre di Dio"),
            ("2025-01-06", "Epifania del Signore"),
            ("2025-02-11", "Anniversario della istituzione dello Stato della Città del Vaticano"),
            ("2025-03-13", "Anniversario dell'Elezione del Santo Padre"),
            ("2025-03-19", "San Giuseppe"),
            ("2025-04-17", "Giovedì Santo"),
            ("2025-04-18", "Venerdì Santo"),
            ("2025-04-19", "Sabato Santo"),
            ("2025-04-20", "Pasqua di Resurrezione"),
            ("2025-04-21", "Lunedì dell'Angelo"),
            ("2025-04-22", "Martedì in Albis"),
            ("2025-04-23", "Onomastico del Santo Padre"),
            ("2025-05-01", "San Giuseppe Artigiano"),
            ("2025-05-29", "Ascensione del Signore"),
            ("2025-06-08", "Solennità della Pentecoste"),
            ("2025-06-15", "Solennità della Santissima Trinità"),
            ("2025-06-19", "Corpus Domini"),
            ("2025-06-29", "Santi Pietro e Paolo"),
            ("2025-08-14", "Vigilia dell'Assunzione di Maria Santissima"),
            ("2025-08-15", "Assunzione di Maria Santissima"),
            ("2025-08-16", "Giorno Successivo all'Assunzione di Maria Santissima"),
            ("2025-09-17", "Onomastico del Santo Padre"),
            ("2025-11-01", "Tutti i Santi"),
            ("2025-11-02", "Tutti i Fedeli Defunti"),
            ("2025-12-08", "Immacolata Concezione"),
            ("2025-12-24", "Vigilia di Natale"),
            ("2025-12-25", "Natale"),
            ("2025-12-26", "Santo Stefano"),
            ("2025-12-27", "San Giovanni"),
            ("2025-12-31", "Ultimo giorno dell'anno"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "Solemnity of Mary, Mother of God"),
            ("2025-01-06", "Epiphany"),
            ("2025-02-11", "Anniversary of the Foundation of Vatican City"),
            ("2025-03-13", "Anniversary of the Election of the Holy Father"),
            ("2025-03-19", "Saint Joseph's Day"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Holy Saturday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-22", "Easter Tuesday"),
            ("2025-04-23", "Name Day of the Holy Father"),
            ("2025-05-01", "Saint Joseph the Worker's Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-08", "Solemnity of Pentecost"),
            ("2025-06-15", "Solemnity of Holy Trinity"),
            ("2025-06-19", "Corpus Domini"),
            ("2025-06-29", "Saints Peter and Paul's Day"),
            ("2025-08-14", "Day Before Assumption of Mary"),
            ("2025-08-15", "Assumption of Mary Day"),
            ("2025-08-16", "Day After Assumption of Mary"),
            ("2025-09-17", "Name Day of the Holy Father"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-11-02", "All Souls' Day"),
            ("2025-12-08", "Immaculate Conception"),
            ("2025-12-24", "Christmas Eve"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Saint Stephen's Day"),
            ("2025-12-27", "Saint John the Evangelist's Day"),
            ("2025-12-31", "Last Day of the Year"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2025-01-01", "วันสมโภชพระนางมารีอา พระชนนีพระเป็นเจ้า"),
            ("2025-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2025-02-11", "วันครบรอบการสถาปนานครรัฐวาติกัน"),
            ("2025-03-13", "วันคล้ายวันเลือกตั้งสมเด็จพระสันตะปาปา"),
            ("2025-03-19", "วันสมโภชนักบุญโยเซฟ"),
            ("2025-04-17", "วันพฤหัสศักดิ์สิทธิ์"),
            ("2025-04-18", "วันศุกร์ประเสริฐ"),
            ("2025-04-19", "วันเสาร์ศักดิ์สิทธิ์"),
            ("2025-04-20", "วันอาทิตย์อีสเตอร์"),
            ("2025-04-21", "วันจันทร์อีสเตอร์"),
            ("2025-04-22", "วันอังคารอีสเตอร์"),
            ("2025-04-23", "วันฉลองพระนามเดิมสมเด็จพระสันตะปาปา"),
            ("2025-05-01", "วันฉลองนักบุญโยเซฟ กรรมกร"),
            ("2025-05-29", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2025-06-08", "วันสมโภชพระจิตเจ้า"),
            ("2025-06-15", "วันสมโภชพระตรีเอกภาพ"),
            ("2025-06-19", "วันสมโภชพระคริสตวรกาย"),
            ("2025-06-29", "วันสมโภชนักบุญเปโตรและเปาโล"),
            ("2025-08-14", "วันก่อนวันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2025-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2025-08-16", "วันหลังวันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2025-09-17", "วันฉลองพระนามเดิมสมเด็จพระสันตะปาปา"),
            ("2025-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2025-11-02", "วันภาวนาอุทิศแด่ผู้ล่วงลับ"),
            ("2025-12-08", "วันสมโภชแม่พระผู้ปฏิสนธินิรมล"),
            ("2025-12-24", "วันคริสต์มาสอีฟ"),
            ("2025-12-25", "วันคริสต์มาส"),
            ("2025-12-26", "วันสมโภชนักบุญสเตเฟน"),
            ("2025-12-27", "วันสมโภชนักบุญยอห์น"),
            ("2025-12-31", "วันสิ้นปี"),
        )
