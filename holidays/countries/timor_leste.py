#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import GOVERNMENT, PUBLIC, WORKDAY
from holidays.groups import (
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.holiday_base import HolidayBase


class TimorLeste(
    HolidayBase, ChristianHolidays, InternationalHolidays, IslamicHolidays, StaticHolidays
):
    """
    References:
    - https://mj.gov.tl/jornal/lawsTL/RDTL-Law/RDTL-Laws/Law-2005-10.pdf  # 2005 Law
    - http://timor-leste.gov.tl/?p=14494&lang=en  # 2016 Amendment
    - http://timor-leste.gov.tl/?p=30266&lang=en  # 2022
    - http://timor-leste.gov.tl/?p=31750&lang=en  # 2023 (en_US)
    - http://timor-leste.gov.tl/?p=31750&lang=pt  # 2023 (pt_PT)
    - http://timor-leste.gov.tl/?p=31750&lang=tp  # 2023 (tet)
    - http://timor-leste.gov.tl/?p=35833&lang=en  # 2024

    Limitations:

    - Exact Islamic holidays dates are only available for 2011-2023; the rest are estimates.
    """

    country = "TL"
    supported_categories = (GOVERNMENT, PUBLIC, WORKDAY)
    default_language = "pt_TL"
    # %s (estimated).
    estimated_label = tr("%s (aproximada)")
    supported_languages = ("en_US", "pt_TL", "tet")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(self, cls=TimorLesteIslamicHolidays)
        StaticHolidays.__init__(self, TimorLesteStaticHolidays)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Law No. 10/2005 Of 10 August, Public Holidays and Official Commemorative Dates.
        if self._year <= 2005:
            return None

        # Fixed Date Public Holidays.

        # New Year's Day.
        self._add_new_years_day(tr("Dia de Ano Novo"))

        # Dia dos Veteranos.
        # First appeared in 2017.

        if self._year >= 2017:
            # Veteran's Day.
            self._add_holiday_mar_3(tr("Dia dos Veteranos"))

        # World Labor Day.
        self._add_labor_day(tr("Dia Mundial do Trabalhador"))

        # Restoration of Independence Day.
        self._add_holiday_may_20(tr("Dia da Restauração da Independência"))

        # Popular Consultation Day.
        self._add_holiday_aug_30(tr("Dia da Consulta Popular"))

        # All Saints' Day.
        self._add_all_saints_day(tr("Dia de Todos os Santos"))

        # All Souls' Day.
        self._add_all_souls_day(tr("Dia de Todos os Fiéis Defuntos"))

        # Dia Nacional da Mulher.
        # Originally classed as "Commemorative Date" only, reclassified in 2023.

        if self._year >= 2023:
            # National Women's Day.
            self._add_holiday_nov_3(tr("Dia Nacional da Mulher"))

        # National Youth Day.
        self._add_holiday_nov_12(tr("Dia Nacional da Juventude"))

        # Proclamation of Independence Day.
        self._add_holiday_nov_28(tr("Dia da Proclamação da Independência"))

        # Dia da Memória
        # Created to replaced the original National Heroes Day in 2017.

        if self._year >= 2017:
            # Memorial Day.
            self._add_holiday_dec_7(tr("Dia da Memória"))

        self._add_immaculate_conception_day(
            # Day of Our Lady of Immaculate Conception and Timor-Leste Patroness.
            tr("Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste")
        )

        # Christmas Day.
        self._add_christmas_day(tr("Dia de Natal"))

        # Dia dos Heróis Nacionais.
        # Moved to Dec 31 in 2017.

        # National Heroes Day.
        name = tr("Dia dos Heróis Nacionais")
        if self._year >= 2017:
            self._add_holiday_dec_31(name)
        else:
            self._add_holiday_dec_7(name)

        # Variable Date Public Holidays.

        # Holy Friday.
        self._add_good_friday(tr("Sexta-Feira Santa"))

        # Eid al-Fitr.
        self._add_eid_al_fitr_day(tr("Idul Fitri"))

        # Corpus Christi.
        self._add_corpus_christi_day(tr("Festa do Corpo de Deus"))

        # Eid al-Adha.
        self._add_eid_al_adha_day(tr("Idul Adha"))

    def _populate_workday_holidays(self):
        # Law No. 10/2005 Of 10 August, Public Holidays and Official Commemorative Dates.
        if self._year <= 2005:
            return None

        # Fixed Date Government Holidays.

        # World Children's Day.
        self._add_childrens_day(tr("Dia Mundial da Criança"))

        self._add_holiday_aug_20(
            # Day of the Armed Forces for the National Liberation of Timor-Leste (FALINTIL).
            tr("Dia das Forças Armadas de Libertação Nacional de Timor-Leste (FALINTIL)")
        )

        # Dia Nacional da Mulher.
        # Originally classed as "Commemorative Date" only, reclassified in 2023.
        # Prior to reclassification, this is usually only observed as half-day holiday.
        # i.e. http://timor-leste.gov.tl/?p=4183&lang=en (2010)
        #      http://timor-leste.gov.tl/?p=5979&lang=en (2011)
        if self._year <= 2022:
            # National Women's Day.
            self._add_holiday_nov_3(tr("Dia Nacional da Mulher"))

        # World Human Rights Day.
        self._add_holiday_dec_10(tr("Dia Mundial dos Direitos Humanos"))

        # Variable Date Government Holidays.

        # Ash Wednesday.
        self._add_ash_wednesday(tr("Quarta-Feira de Cinzas"))

        # Holy Thursday.
        self._add_holy_thursday(tr("Quinta-Feira Santa"))

        # The Day of Ascension of Jesus Christ into Heaven.
        self._add_ascension_thursday(tr("Dia da Ascensão de Jesus Cristo ao Céu"))


class TL(TimorLeste):
    pass


class TLS(TimorLeste):
    pass


class TimorLesteIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        2011: (NOV, 7),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 4),
        2015: (SEP, 24),
        2016: (SEP, 18),
        2017: (SEP, 1),
        2018: (AUG, 21),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 19),
        2022: (JUL, 9),
        2023: (JUN, 29),
        2024: (JUN, 17),
    }

    EID_AL_FITR_DATES = {
        2011: (AUG, 31),
        2012: (AUG, 20),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 7),
        2017: (JUN, 26),
        2018: (JUN, 15),
        2019: (JUN, 6),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
    }


class TimorLesteStaticHolidays:
    # Special Holidays.

    # National Holidays (Special).
    special_national_holidays = tr("Feriados Nacionais (Especiais)")

    # Presidential Election Day.
    presidential_election = tr("Dia da Eleição Presidencial")

    # Parliamentary Election Day.
    parliamentary_election = tr("Dia de Eleições Parlamentares")

    # Centenary of the Revolt of Dom Boaventura.
    dom_boaventura_centenary = tr("Centenário da Revolta de Dom Boaventura")

    # Funeral Ceremonies of Fernando 'La Sama' de Araújo.
    la_sama_funeral = tr("Cerimónias Fúnebres de Fernando 'La Sama' de Araújo")

    # 20th Anniversary Celebrations of the Popular Consultation.
    popular_consultation_20th = tr("Celebrações do 20.º Aniversário da Consulta Popular")

    special_government_holidays = {
        2010: (
            # http://timor-leste.gov.tl/?p=4183&lang=en
            (NOV, 3, special_national_holidays),
            # http://timor-leste.gov.tl/?p=4437&lang=en
            (DEC, 24, special_national_holidays),
            (DEC, 31, special_national_holidays),
        ),
        2011: (
            # http://timor-leste.gov.tl/?p=5496&lang=en
            (AUG, 15, special_national_holidays),
            # http://timor-leste.gov.tl/?p=5979&lang=en
            (NOV, 3, special_national_holidays),
            # http://timor-leste.gov.tl/?p=6264&lang=en
            (DEC, 26, special_national_holidays),
        ),
        2012: (
            # http://timor-leste.gov.tl/?p=6264&lang=en
            (JAN, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=6347&lang=en
            (JAN, 23, special_national_holidays),
            # http://timor-leste.gov.tl/?p=6471&lang=en
            (FEB, 22, special_national_holidays),
            # http://timor-leste.gov.tl/?p=6621&lang=en
            (MAR, 16, presidential_election),
            # http://timor-leste.gov.tl/?p=6760&lang=en
            (APR, 16, presidential_election),
            (APR, 17, presidential_election),
            # http://timor-leste.gov.tl/?p=7035&lang=en
            (JUL, 6, parliamentary_election),
            # http://timor-leste.gov.tl/?p=7046&lang=en
            (JUL, 9, parliamentary_election),
            # http://timor-leste.gov.tl/?p=7474&lang=en
            (NOV, 27, dom_boaventura_centenary),
            (NOV, 29, dom_boaventura_centenary),
            # http://timor-leste.gov.tl/?p=7550&lang=en
            (DEC, 24, special_national_holidays),
            (DEC, 26, special_national_holidays),
            (DEC, 31, special_national_holidays),
        ),
        2013: (
            # http://timor-leste.gov.tl/?p=7715&lang=en
            (FEB, 13, special_national_holidays),
            # http://timor-leste.gov.tl/?p=7918&lang=en
            (MAR, 28, special_national_holidays),
            (APR, 1, special_national_holidays),
            # http://timor-leste.gov.tl/?p=8664&lang=en
            (AUG, 20, special_national_holidays),
            # http://timor-leste.gov.tl/?p=9392&lang=en
            (NOV, 29, special_national_holidays),
            # http://timor-leste.gov.tl/?p=9475&lang=en
            (DEC, 24, special_national_holidays),
            (DEC, 26, special_national_holidays),
            (DEC, 31, special_national_holidays),
        ),
        2014: (
            # http://timor-leste.gov.tl/?p=9759&lang=en
            (MAR, 5, special_national_holidays),
            # http://timor-leste.gov.tl/?p=9964&lang=en
            (APR, 17, special_national_holidays),
            (APR, 21, special_national_holidays),
            # http://timor-leste.gov.tl/?p=10294&lang=en
            (JUL, 22, special_national_holidays),
            (JUL, 23, special_national_holidays),
            # http://timor-leste.gov.tl/?p=10524&lang=en
            (AUG, 15, special_national_holidays),
            (AUG, 20, special_national_holidays),
            # http://timor-leste.gov.tl/?p=11036&lang=en
            (DEC, 24, special_national_holidays),
            (DEC, 26, special_national_holidays),
            (DEC, 31, special_national_holidays),
        ),
        2015: (
            # http://timor-leste.gov.tl/?p=11036&lang=en
            (JAN, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=11247&lang=en
            (FEB, 18, special_national_holidays),
            # http://timor-leste.gov.tl/?p=11544&lang=en
            (APR, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=11966&lang=en
            (MAY, 13, special_national_holidays),
            # http://timor-leste.gov.tl/?p=12246&lang=en
            (JUN, 5, la_sama_funeral),
            # http://timor-leste.gov.tl/?p=13105&lang=en
            (AUG, 20, special_national_holidays),
            # http://timor-leste.gov.tl/?p=14271&lang=en
            (DEC, 24, special_national_holidays),
            (DEC, 31, special_national_holidays),
        ),
        2016: (
            # http://timor-leste.gov.tl/?p=14482&lang=en
            (FEB, 10, special_national_holidays),
            # http://timor-leste.gov.tl/?p=14827&lang=en
            (MAR, 24, special_national_holidays),
            # http://timor-leste.gov.tl/?p=15740&lang=en
            (JUL, 6, special_national_holidays),
            # http://timor-leste.gov.tl/?p=16626&lang=en
            (NOV, 3, special_national_holidays),
            # http://timor-leste.gov.tl/?p=16998&lang=en
            (DEC, 26, special_national_holidays),
        ),
        2017: (
            # http://timor-leste.gov.tl/?p=16998&lang=en
            (JAN, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=17428&lang=en
            (MAR, 1, special_national_holidays),
            # http://timor-leste.gov.tl/?p=17548&lang=en
            (MAR, 20, presidential_election),
            (MAR, 21, presidential_election),
            # http://timor-leste.gov.tl/?p=17698&lang=en
            (APR, 13, special_national_holidays),
            # http://timor-leste.gov.tl/?p=19189&lang=en
            (DEC, 26, special_national_holidays),
        ),
        2018: (
            # http://timor-leste.gov.tl/?p=19189&lang=en
            (JAN, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=19411&lang=en
            (FEB, 14, special_national_holidays),
            # http://timor-leste.gov.tl/?p=19452&lang=en
            (FEB, 16, special_national_holidays),
            # http://timor-leste.gov.tl/?p=19693&lang=en
            (MAR, 29, special_national_holidays),
            # http://timor-leste.gov.tl/?p=20199&lang=en
            (AUG, 22, special_national_holidays),
        ),
        2019: (
            # http://timor-leste.gov.tl/?p=21116&lang=en
            (FEB, 5, special_national_holidays),
            # http://timor-leste.gov.tl/?p=21207&lang=en
            (MAR, 6, special_national_holidays),
            # http://timor-leste.gov.tl/?p=21607&lang=en
            (APR, 18, special_national_holidays),
            # http://timor-leste.gov.tl/?p=22642&lang=en
            (AUG, 12, special_national_holidays),
            # http://timor-leste.gov.tl/?p=22681&lang=en
            (AUG, 20, special_national_holidays),
            # http://timor-leste.gov.tl/?p=22701&lang=en
            (AUG, 26, popular_consultation_20th),
            (AUG, 27, popular_consultation_20th),
            (AUG, 28, popular_consultation_20th),
            (AUG, 29, popular_consultation_20th),
            # http://timor-leste.gov.tl/?p=23277&lang=en
            (OCT, 31, special_national_holidays),
            # http://timor-leste.gov.tl/?p=23417&lang=en
            (DEC, 24, special_national_holidays),
            (DEC, 26, special_national_holidays),
            (DEC, 30, special_national_holidays),
        ),
        2020: (
            # http://timor-leste.gov.tl/?p=23417&lang=en
            (JAN, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=23607&lang=en
            (FEB, 26, special_national_holidays),
            # http://timor-leste.gov.tl/?p=25455&lang=en
            (AUG, 20, special_national_holidays),
            # http://timor-leste.gov.tl/?p=25502&lang=en
            (AUG, 31, special_national_holidays),
            # http://timor-leste.gov.tl/?p=26030&lang=en
            (NOV, 3, special_national_holidays),
            # http://timor-leste.gov.tl/?p=26365&lang=en
            (DEC, 24, special_national_holidays),
        ),
        2021: (
            # http://timor-leste.gov.tl/?p=26865&lang=en
            (FEB, 12, special_national_holidays),
            # http://timor-leste.gov.tl/?p=26896&lang=en
            (FEB, 17, special_national_holidays),
            # http://timor-leste.gov.tl/?p=29682&lang=en
            (NOV, 3, special_national_holidays),
        ),
        2022: (
            # http://timor-leste.gov.tl/?p=30029&lang=en
            (FEB, 1, special_national_holidays),
            # http://timor-leste.gov.tl/?p=30194&lang=en
            (MAR, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=30254&lang=en
            (MAR, 18, presidential_election),
            # http://timor-leste.gov.tl/?p=30429&lang=en
            (APR, 14, special_national_holidays),
            (APR, 18, presidential_election),
            (APR, 19, presidential_election),
            (APR, 20, presidential_election),
            # http://timor-leste.gov.tl/?p=31404&lang=en
            (OCT, 31, special_national_holidays),
            # http://timor-leste.gov.tl/?p=31574&lang=en
            (DEC, 9, special_national_holidays),
            # http://timor-leste.gov.tl/?p=31633&lang=en
            (DEC, 26, special_national_holidays),
        ),
        2023: (
            # http://timor-leste.gov.tl/?p=31641&lang=en
            (JAN, 2, special_national_holidays),
            # http://timor-leste.gov.tl/?p=31798&lang=en
            (JAN, 23, special_national_holidays),
            # http://timor-leste.gov.tl/?p=32191&lang=en
            (FEB, 22, special_national_holidays),
        ),
        2024: (
            # http://timor-leste.gov.tl/?p=36002&lang=en
            (FEB, 14, special_national_holidays),
        ),
    }
