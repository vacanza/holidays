#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class VaticanCity(HolidayBase, ChristianHolidays, InternationalHolidays):
    """Vatican City holidays.

    References:
        * <https://www.vatican.va/roman_curia/labour_office/docs/documents/ulsa_b18_7_it.html>
        * <https://cdn.restorethe54.com/media/pdf/1917-code-of-canon-law-english.pdf>
        * <https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib4-cann1244-1253_en.html>
        * <https://en.wikipedia.org/wiki/Public_holidays_in_Vatican_City>
        * <https://en.wikipedia.org/wiki/Holy_day_of_obligation>
        * <https://www.ewtn.com/catholicism/library/solemnity-of-mary-mother-of-god-5826>
        * <https://www.franciscanmedia.org/saint-of-the-day/saint-joseph-the-worker/>

    Cross-checked With:
        * <https://www.vaticanstate.va/images/pdf/CALENDARIO_2020.pdf>
        * <https://www.farmaciavaticana.va/images/pdf/calendario_2021.pdf>
        * <https://www.farmaciavaticana.va/images/pdf/calendario_2022.pdf>
        * <https://www.farmaciavaticana.va/images/pdf/calendario_2023.pdf>
        * <https://www.farmaciavaticana.va/media/attachments/2024/01/02/calendario_2024.pdf>
        * <https://www.farmaciavaticana.va/media/attachments/2025/01/02/calendario-2025.pdf>
    """

    country = "VA"
    default_language = "it"
    supported_languages = ("en_US", "it", "th")
    # Lateran Treaty, FEB 11, 2029.
    start_year = 1929

    def __init__(self, *args, **kwargs) -> None:
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self) -> None:
        # This is supposedly the same as International New Year.
        # Modern adoption across the entire Latin Church in 1931 though this
        # was already celebrated in Rome as the Octave day of Christmas.

        # Solemnity of Mary, Mother of God.
        self._add_holiday_jan_1(tr("Solennità di Maria Santissima Madre di Dio"))

        # Epiphany.
        self._add_epiphany_day(tr("Epifania del Signore"))

        self._add_holiday_feb_11(
            # Anniversary of the Foundation of Vatican City.
            tr("Anniversario della istituzione dello Stato della Città del Vaticano")
        )

        # Anniversary of the Election of the Holy Father.
        name_election = tr("Anniversario dell'Elezione del Santo Padre")

        # Name Day of the Holy Father.
        name_day = tr("Onomastico del Santo Padre")

        if self._year >= 2013:
            # Pope Francis (Jorge Mario Bergoglio).
            # Name Day: Saint George's Day (APR 23).
            self._add_holiday_mar_13(name_election)
            self._add_saint_georges_day(name_day)
        elif self._year >= 2005:
            # Pope Benedict XVI (Josef Aloisius Ratzinger).
            # Name Day: Saint Joseph's Day (MAR 19).
            self._add_holiday_apr_19(name_election)
            self._add_saint_josephs_day(name_day)
        elif self._year >= 1978:
            # Pope John Paul II (Karol Józef Wojtyła).
            # Name Day: Saint Charles Borromeo Day (NOV 4).
            self._add_holiday_oct_16(name_election)
            self._add_holiday_nov_4(name_day)

            if self._year == 1978:
                # Pope John Paul I (Albino Luciani).
                # Name Day: Saint Albinus of Angers (MAR 1)?
                self._add_holiday_aug_26(name_election)

                # Pope Paul VI (cont.).
                self._add_holiday_jun_21(name_election)
        elif self._year >= 1963:
            # Pope Paul VI (Giovanni Battista Enrico Antonio Maria Montini).
            # Name Day: Saint John's Day (JUN 24)?
            self._add_holiday_jun_21(name_election)
        elif self._year >= 1958:
            # Pope John XXIII (Angelo Giuseppe Roncalli).
            # Name Day: Saint Angelus of Jerusalem (MAY 5)?
            self._add_holiday_oct_28(name_election)

            if self._year == 1958:
                # Pope Pius XII (cont.).
                self._add_holiday_mar_2(name_election)
        elif self._year >= 1939:
            # Pope Pius XII (Eugenio Maria Giuseppe Giovanni Pacelli).
            # Name Day: Saint Eugene (JUN 2)?
            self._add_holiday_mar_2(name_election)

            if self._year == 1939:
                # Pope Pius XI (cont.).
                self._add_holiday_feb_6(name_election)
        else:
            # Pope Pius XI (Achille Ambrogio Damiano Ratti).
            # Name Day: Saint Nereus and Achilleus (MAY 12)?
            self._add_holiday_feb_6(name_election)

        # Saint Joseph's Day.
        self._add_saint_josephs_day(tr("San Giuseppe"))

        # Maundy Thursday.
        self._add_holy_thursday(tr("Giovedì Santo"))

        # Good Friday.
        self._add_good_friday(tr("Venerdì Santo"))

        # Holy Saturday.
        self._add_holy_saturday(tr("Sabato Santo"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pasqua di Resurrezione"))

        # Easter Monday.
        self._add_easter_monday(tr("Lunedì dell'Angelo"))

        # Easter Tuesday.
        self._add_easter_tuesday(tr("Martedì in Albis"))

        # Created in response to May Day holidays by Pope Pius XII in 1955.
        if self._year >= 1955:
            # Saint Joseph the Worker.
            self._add_holiday_may_1(tr("San Giuseppe Artigiano"))

        # Solemnity of Pentecost.
        self._add_whit_sunday(tr("Solennità della Pentecoste"))

        # Solemnity of Holy Trinity.
        self._add_trinity_sunday(tr("Solennità della Santissima Trinità"))

        # Ascension Day.
        self._add_ascension_thursday(tr("Ascensione del Signore"))

        # Corpus Domini.
        self._add_corpus_christi_day(tr("Corpus Domini"))

        # Saints Peter and Paul's Day.
        self._add_saints_peter_and_paul_day(tr("Santi Pietro e Paolo"))

        # Day Before Assumption of Mary.
        self._add_holiday_aug_14(tr("Vigilia dell'Assunzione di Maria Santissima"))

        # Assumption of Mary Day.
        self._add_assumption_of_mary_day(tr("Assunzione di Maria Santissima"))

        # Day After Assumption of Mary.
        self._add_holiday_aug_16(tr("Giorno Successivo all'Assunzione di Maria Santissima"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Tutti i Santi"))

        # All Souls' Day.
        self._add_all_souls_day(tr("Tutti i Fedeli Defunti"))

        # Immaculate Conception.
        self._add_immaculate_conception_day(tr("Immacolata Concezione"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Vigilia di Natale"))

        # Christmas Day.
        self._add_christmas_day(tr("Natale"))

        # Saint Stephen's Day.
        self._add_christmas_day_two(tr("Santo Stefano"))

        # Saint John the Evangelist's Day.
        self._add_christmas_day_three(tr("San Giovanni"))

        # Last Day of the Year.
        self._add_new_years_eve(tr("Ultimo giorno dell'anno"))


class VA(VaticanCity):
    pass


class VAT(VaticanCity):
    pass
