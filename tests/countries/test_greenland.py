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

from holidays.countries.greenland import Greenland
from tests.common import CommonCountryTests


class TestGreenland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Greenland)

    def test_1982(self):
        self.assertHolidaysInYear(
            1982,
            ("1982-01-01", "Ukiortaaq"),
            ("1982-04-08", "Sisamanngortoq illernartoq"),
            ("1982-04-09", "Tallimanngorneq tannaartoq"),
            ("1982-04-11", "Poorskip ullua"),
            ("1982-04-12", "Poorskip-aappaa"),
            ("1982-05-07", "Ulloq qinuffiusoq"),
            ("1982-05-20", "Qilaliarfik"),
            ("1982-05-30", "Piinsip ullua"),
            ("1982-05-31", "Piinsip-aappaa"),
            ("1982-12-25", "Juullip ullua"),
            ("1982-12-26", "Juullip-aappaa"),
        )

    def test_1982_optional(self):
        self.assertOptionalHolidaysInYear(
            1982,
            ("1982-01-06", "Kunngit pingasut ulluat"),
            ("1982-05-01", "Sulisartut ulluat"),
            ("1982-12-24", "Juulliaraq"),
            ("1982-12-31", "Ukiortaami"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Ukiortaaq"),
            ("2022-04-14", "Sisamanngortoq illernartoq"),
            ("2022-04-15", "Tallimanngorneq tannaartoq"),
            ("2022-04-17", "Poorskip ullua"),
            ("2022-04-18", "Poorskip-aappaa"),
            ("2022-05-13", "Ulloq qinuffiusoq"),
            ("2022-05-26", "Qilaliarfik"),
            ("2022-06-05", "Piinsip ullua"),
            ("2022-06-06", "Piinsip-aappaa"),
            ("2022-12-25", "Juullip ullua"),
            ("2022-12-26", "Juullip-aappaa"),
        )

    def test_2022_optional(self):
        self.assertOptionalHolidaysInYear(
            2022,
            ("2022-01-06", "Kunngit pingasut ulluat"),
            ("2022-05-01", "Sulisartut ulluat"),
            ("2022-06-21", "Ullortuneq"),
            ("2022-12-24", "Juulliaraq"),
            ("2022-12-31", "Ukiortaami"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Ukiortaaq"),
            ("2022-01-06", "Kunngit pingasut ulluat"),
            ("2022-04-14", "Sisamanngortoq illernartoq"),
            ("2022-04-15", "Tallimanngorneq tannaartoq"),
            ("2022-04-17", "Poorskip ullua"),
            ("2022-04-18", "Poorskip-aappaa"),
            ("2022-05-01", "Sulisartut ulluat"),
            ("2022-05-13", "Ulloq qinuffiusoq"),
            ("2022-05-26", "Qilaliarfik"),
            ("2022-06-05", "Piinsip ullua"),
            ("2022-06-06", "Piinsip-aappaa"),
            ("2022-06-21", "Ullortuneq"),
            ("2022-12-24", "Juulliaraq"),
            ("2022-12-25", "Juullip ullua"),
            ("2022-12-26", "Juullip-aappaa"),
            ("2022-12-31", "Ukiortaami"),
        )

    def test_l10n_da(self):
        self.assertLocalizedHolidays(
            "da",
            ("2022-01-01", "Nytårsdag"),
            ("2022-01-06", "Helligtrekongersdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-01", "Arbejdernes kampdag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-06-21", "Nationaldag"),
            ("2022-12-24", "Juleaftensdag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
            ("2022-12-31", "Nytårsaften"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-13", "Great Prayer Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-21", "National Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_fi(self):
        self.assertLocalizedHolidays(
            "fi",
            ("2022-01-01", "Uudenvuodenpäivä"),
            ("2022-01-06", "Loppiainen"),
            ("2022-04-14", "Kiirastorstai"),
            ("2022-04-15", "Pitkäperjantai"),
            ("2022-04-17", "Pääsiäispäivä"),
            ("2022-04-18", "Toinen pääsiäispäivä"),
            ("2022-05-01", "Kansainvälinen työn päivä"),
            ("2022-05-13", "Suuri rukouspäivä"),
            ("2022-05-26", "Helatorstai"),
            ("2022-06-05", "Helluntaipäivä"),
            ("2022-06-06", "Toinen helluntaipäivä"),
            ("2022-06-21", "Kansallispäivä"),
            ("2022-12-24", "Jouluaatto"),
            ("2022-12-25", "Joulupäivä"),
            ("2022-12-26", "Tapaninpäivä"),
            ("2022-12-31", "Uudenvuodenaatto"),
        )

    def test_l10n_is(self):
        self.assertLocalizedHolidays(
            "is",
            ("2022-01-01", "Nýársdagur"),
            ("2022-01-06", "Þrettándinn"),
            ("2022-04-14", "Skírdagur"),
            ("2022-04-15", "Föstudagurinn langi"),
            ("2022-04-17", "Páskadagur"),
            ("2022-04-18", "Annar í páskum"),
            ("2022-05-01", "Frídagur verkalýðsins"),
            ("2022-05-13", "Kóngsbænadagur"),
            ("2022-05-26", "Uppstigningardagur"),
            ("2022-06-05", "Hvítasunnudagur"),
            ("2022-06-06", "Annar í hvítasunnu"),
            ("2022-06-21", "Þjóðhátíðardagur"),
            ("2022-12-24", "Aðfangadagur"),
            ("2022-12-25", "Jóladagur"),
            ("2022-12-26", "Annar í jólum"),
            ("2022-12-31", "Gamlársdagur"),
        )

    def test_l10n_no(self):
        self.assertLocalizedHolidays(
            "no",
            ("2022-01-01", "Nyttårsdag"),
            ("2022-01-06", "Helligtrekongersdag"),
            ("2022-04-14", "Skjærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Første påskedag"),
            ("2022-04-18", "Andre påskedag"),
            ("2022-05-01", "Arbeidernes internasjonale kampdag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Første pinsedag"),
            ("2022-06-06", "Andre pinsedag"),
            ("2022-06-21", "Nasjonaldag"),
            ("2022-12-24", "Julaften"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Andre juledag"),
            ("2022-12-31", "Nyttårsaften"),
        )

    def test_l10n_sv(self):
        self.assertLocalizedHolidays(
            "sv",
            ("2022-01-01", "Nyårsdagen"),
            ("2022-01-06", "Trettondedag jul"),
            ("2022-04-14", "Skärtorsdagen"),
            ("2022-04-15", "Långfredagen"),
            ("2022-04-17", "Påskdagen"),
            ("2022-04-18", "Annandag påsk"),
            ("2022-05-01", "Internationella arbetardagen"),
            ("2022-05-13", "Stora bönedagen"),
            ("2022-05-26", "Kristi himmelsfärdsdag"),
            ("2022-06-05", "Pingstdagen"),
            ("2022-06-06", "Annandag pingst"),
            ("2022-06-21", "Nationaldag"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
            ("2022-12-31", "Nyårsafton"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День трудящих"),
            ("2022-05-13", "День загальної молитви"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-21", "Національне свято"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Переддень Нового року"),
        )
