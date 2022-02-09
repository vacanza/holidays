# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Provinces completed by Henrik Sozzi <henrik_sozzi@hotmail.com>
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import (
    relativedelta as rd,
    MO,
    TU,
    WE,
    TH,
    FR,
    SA,
    SU,
)

from holidays.constants import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
)
from holidays.holiday_base import HolidayBase


class Italy(HolidayBase):
    country = "IT"
    # Reference: https://it.wikipedia.org/wiki/Province_d%27Italia
    # Please maintain in alphabetical order for easy updating in the future
    # The alphabetical order is except cities of provinces with multiple head
    # cities that directly follows the main province id like BT, Barletta,
    # Andria, Trani, for easily grouping them.
    # In that case if you use the 2 char id you'll take the first Santo
    # Patrono defined. If you want one specific you'll have to use
    # the full name of the city like "Andria" instead of "BT".
    subdivisions = [
        "AG",
        "AL",
        "AN",
        "AO",
        "AP",
        "AQ",
        "AR",
        "AT",
        "AV",
        "BA",
        "BG",
        "BI",
        "BL",
        "BN",
        "BO",
        "BR",
        "BS",
        "BT",
        "Barletta",
        "Andria",
        "Trani",
        "BZ",
        "CA",
        "CB",
        "CE",
        "CH",
        "CL",
        "CN",
        "CO",
        "CR",
        "CS",
        "CT",
        "CZ",
        "EN",
        "FC",
        "Forlì",
        "Cesena",
        "FE",
        "FG",
        "FI",
        "FM",
        "FR",
        "GE",
        "GO",
        "GR",
        "IM",
        "IS",
        "KR",
        "LC",
        "LE",
        "LI",
        "LO",
        "LT",
        "LU",
        "MB",
        "MC",
        "ME",
        "MI",
        "MN",
        "MO",
        "MS",
        "MT",
        "NA",
        "NO",
        "NU",
        "OR",
        "PA",
        "PC",
        "PD",
        "PE",
        "PG",
        "PI",
        "PN",
        "PO",
        "PR",
        "PT",
        "PU",
        "Pesaro",
        "Urbino",
        "PV",
        "PZ",
        "RA",
        "RC",
        "RE",
        "RG",
        "RI",
        "RM",
        "RN",
        "RO",
        "SA",
        "SI",
        "SO",
        "SP",
        "SR",
        "SS",
        "SU",
        "SV",
        "TA",
        "TE",
        "TN",
        "TO",
        "TP",
        "TR",
        "TS",
        "TV",
        "UD",
        "VA",
        "VB",
        "VC",
        "VE",
        "VI",
        "VR",
        "VT",
        "VV",
    ]

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        self[date(year, JAN, 1)] = "Capodanno"
        self[date(year, JAN, 6)] = "Epifania del Signore"
        self[easter(year)] = "Pasqua di Resurrezione"
        self[easter(year) + rd(weekday=MO)] = "Lunedì dell'Angelo"
        if year >= 1946:
            self[date(year, APR, 25)] = "Festa della Liberazione"
        self[date(year, MAY, 1)] = "Festa dei Lavoratori"
        if year >= 1948:
            self[date(year, JUN, 2)] = "Festa della Repubblica"
        self[date(year, AUG, 15)] = "Assunzione della Vergine"
        self[date(year, NOV, 1)] = "Tutti i Santi"
        self[date(year, DEC, 8)] = "Immacolata Concezione"
        self[date(year, DEC, 25)] = "Natale"
        self[date(year, DEC, 26)] = "Santo Stefano"

        # Provinces holidays
        # Reference from:
        # https://it.wikipedia.org/wiki/Santi_patroni_cattolici_delle_citt%C3%A0_capoluogo_di_provincia_italiane
        # Please maintain in alphabetical order for easy updating in the future
        if self.subdiv:
            if self.subdiv == "AG":
                self[date(year, FEB, 25)] = "San Gerlando"
            elif self.subdiv == "AL":
                self[date(year, NOV, 10)] = "San Baudolino"
            elif self.subdiv == "AN":
                self[date(year, MAY, 4)] = "San Ciriaco"
            elif self.subdiv == "AO":
                self[date(year, SEP, 7)] = "San Grato"
            elif self.subdiv == "AP":
                self[date(year, AUG, 5)] = "Sant'Emidio"
            elif self.subdiv == "AQ":
                self[date(year, JUN, 10)] = "San Massimo D'Aveia"
            elif self.subdiv == "AR":
                self[date(year, AUG, 7)] = "San Donato D'Arezzo"
            elif self.subdiv == "AT":
                self[
                    date(year, MAY, 1) + rd(weekday=TU)
                ] = "San Secondo di Asti"  # <--- First Tuesday in May
            elif self.subdiv == "AV":
                self[date(year, FEB, 14)] = "San Modestino"
            elif self.subdiv == "BA":
                self[date(year, DEC, 6)] = "San Nicola"
            elif self.subdiv == "BG":
                self[date(year, AUG, 26)] = "Sant'Alessandro di Bergamo"
            elif self.subdiv == "BI":
                self[date(year, DEC, 26)] = "Santo Stefano"
            elif self.subdiv == "BL":
                self[date(year, NOV, 11)] = "San Martino"
            elif self.subdiv == "BN":
                self[date(year, AUG, 24)] = "San Bartolomeo apostolo"
            elif self.subdiv == "BO":
                self[date(year, OCT, 4)] = "San Petronio"
            elif self.subdiv == "BR":
                # first Sunday of September
                self[
                    date(year, SEP, 1) + rd(weekday=SU)
                ] = "San Teodoro d'Amasea e San Lorenzo da Brindisi"
            elif self.subdiv == "BS":
                self[date(year, FEB, 15)] = "Santi Faustino e Giovita"
            elif self.subdiv in ("BT", "Barletta"):
                self[date(year, DEC, 30)] = "San Ruggero"
            if self.subdiv in ("BT", "Andria"):
                self[
                    date(year, SEP, 1) + rd(weekday=SU(+3))
                ] = "San Riccardo di Andria"  # <--- Third sunday in September
            if self.subdiv in ("BT", "Trani"):
                self[date(year, MAY, 3)] = "San Nicola Pellegrino"
            elif self.subdiv == "BZ":
                self[date(year, AUG, 15)] = "Maria Santissima Assunta"
            elif self.subdiv == "CA":
                self[date(year, OCT, 30)] = "San Saturnino di Cagliari"
            elif self.subdiv == "CB":
                self[date(year, APR, 23)] = "San Giorgio"
            elif self.subdiv == "CE":
                self[date(year, JAN, 20)] = "San Sebastiano"
            elif self.subdiv == "CH":
                self[date(year, MAY, 11)] = "San Giustino di Chieti"
            elif self.subdiv == "CL":
                self[date(year, SEP, 29)] = "San Michele Arcangelo"
            elif self.subdiv == "CN":
                self[date(year, SEP, 29)] = "San Michele Arcangelo"
            elif self.subdiv == "CO":
                self[date(year, AUG, 31)] = "Sant'Abbondio"
            elif self.subdiv == "CR":
                self[date(year, NOV, 13)] = "Sant'Omobono"
            elif self.subdiv == "CS":
                self[date(year, FEB, 12)] = "Madonna del Pilerio"
            elif self.subdiv == "CT":
                self[date(year, FEB, 5)] = "Sant'Agata"
            elif self.subdiv == "CZ":
                self[date(year, JUL, 16)] = "San Vitaliano"
            elif self.subdiv == "EN":
                self[date(year, JUL, 2)] = "Madonna della Visitazione"
            elif self.subdiv in ("FC", "Cesena"):
                self[date(year, JUN, 24)] = "San Giovanni Battista"
            if self.subdiv in ("FC", "Forlì"):
                self[date(year, FEB, 4)] = "Madonna del Fuoco"
            elif self.subdiv == "FE":
                self[date(year, APR, 23)] = "San Giorgio"
            elif self.subdiv == "FG":
                self[date(year, MAR, 22)] = "Madonna dei Sette Veli"
            elif self.subdiv == "FI":
                self[date(year, JUN, 24)] = "San Giovanni Battista"
            elif self.subdiv == "FM":
                self[date(year, AUG, 15)] = "Maria Santissima Assunta"
                self[date(year, AUG, 16)] = "Maria Santissima Assunta"
            elif self.subdiv == "FR":
                self[date(year, JUN, 20)] = "San Silverio"
            elif self.subdiv == "GE":
                self[date(year, JUN, 24)] = "San Giovanni Battista"
            elif self.subdiv == "GO":
                self[date(year, MAR, 16)] = "Santi Ilario e Taziano"
            elif self.subdiv == "GR":
                self[date(year, AUG, 10)] = "San Lorenzo"
            elif self.subdiv == "IM":
                self[date(year, NOV, 26)] = "San Leonardo da Porto Maurizio"
            elif self.subdiv == "IS":
                self[date(year, MAY, 19)] = "San Pietro Celestino"
            elif self.subdiv == "KR":
                self[date(year, OCT, 9)] = "San Dionigi"
            elif self.subdiv == "LC":
                self[date(year, DEC, 6)] = "San Nicola"
            elif self.subdiv == "LE":
                self[date(year, AUG, 26)] = "Sant'Oronzo"
            elif self.subdiv == "LI":
                self[date(year, MAY, 22)] = "Santa Giulia"
            elif self.subdiv == "LO":
                self[date(year, JAN, 19)] = "San Bassiano"
            elif self.subdiv == "LT":
                self[date(year, APR, 25)] = "San Marco evangelista"
            elif self.subdiv == "LU":
                self[date(year, JUL, 12)] = "San Paolino di Lucca"
            elif self.subdiv == "MB":
                self[date(year, JUN, 24)] = "San Giovanni Battista"
            elif self.subdiv == "MC":
                self[date(year, AUG, 31)] = "San Giuliano l'ospitaliere"
            elif self.subdiv == "ME":
                self[date(year, JUN, 3)] = "Madonna della Lettera"
            elif self.subdiv == "MI":
                self[date(year, DEC, 7)] = "Sant'Ambrogio"
            elif self.subdiv == "MN":
                self[date(year, MAR, 18)] = "Sant'Anselmo da Baggio"
            elif self.subdiv == "MO":
                self[date(year, JAN, 31)] = "San Geminiano"
            elif self.subdiv == "MS":
                self[date(year, OCT, 4)] = "San Francesco d'Assisi"
            elif self.subdiv == "MT":
                self[date(year, JUL, 2)] = "Madonna della Bruna"
            elif self.subdiv == "NA":
                self[date(year, SEP, 19)] = "San Gennaro"
            elif self.subdiv == "NO":
                self[date(year, JAN, 22)] = "San Gaudenzio"
            elif self.subdiv == "NU":
                self[date(year, AUG, 5)] = "Nostra Signora della Neve"
            elif self.subdiv == "OR":
                self[date(year, FEB, 13)] = "Sant'Archelao"
            elif self.subdiv == "PA":
                self[date(year, JUL, 15)] = "San Giovanni"
            elif self.subdiv == "PC":
                self[date(year, JUL, 4)] = "Sant'Antonino di Piacenza"
            elif self.subdiv == "PD":
                self[date(year, JUN, 13)] = "Sant'Antonio di Padova"
            elif self.subdiv == "PE":
                self[date(year, OCT, 10)] = "San Cetteo"
            elif self.subdiv == "PG":
                self[date(year, JAN, 29)] = "Sant'Ercolano e San Lorenzo"
            elif self.subdiv == "PI":
                self[date(year, JUN, 17)] = "San Ranieri"
            elif self.subdiv == "PN":
                self[date(year, APR, 25)] = "San Marco Evangelista"
                self[date(year, SEP, 8)] = "Madonna delle Grazie"
            elif self.subdiv == "PO":
                self[date(year, DEC, 26)] = "Santo Stefano"
            elif self.subdiv == "PR":
                self[date(year, JAN, 13)] = "Sant'Ilario di Poitiers"
            elif self.subdiv == "PT":
                self[date(year, JUL, 25)] = "San Jacopo"
            elif self.subdiv in ("PU", "Pesaro"):
                self[date(year, SEP, 24)] = "San Terenzio di Pesaro"
            if self.subdiv in ("PU", "Urbino"):
                self[date(year, JUN, 1)] = "San Crescentino"
            elif self.subdiv == "PV":
                self[date(year, DEC, 9)] = "San Siro"
            elif self.subdiv == "PZ":
                self[date(year, MAY, 30)] = "San Gerardo di Potenza"
            elif self.subdiv == "RA":
                self[date(year, JUL, 23)] = "Sant'Apollinare"
            elif self.subdiv == "RC":
                self[date(year, APR, 23)] = "San Giorgio"
            elif self.subdiv == "RE":
                self[date(year, NOV, 24)] = "San Prospero Vescovo"
            elif self.subdiv == "RG":
                self[date(year, APR, 23)] = "San Giorgio"
            elif self.subdiv == "RI":
                self[date(year, DEC, 4)] = "Santa Barbara"
            elif self.subdiv == "RM":
                self[date(year, JUN, 29)] = "Santi Pietro e Paolo"
            elif self.subdiv == "RN":
                self[date(year, OCT, 14)] = "San Gaudenzio"
            elif self.subdiv == "RO":
                self[date(year, NOV, 26)] = "San Bellino"
            elif self.subdiv == "SA":
                self[date(year, SEP, 21)] = "San Matteo Evangelista"
            elif self.subdiv == "SI":
                self[date(year, DEC, 1)] = "Sant'Ansano"
            elif self.subdiv == "SO":
                self[date(year, JUN, 19)] = "San Gervasio e San Protasio"
            elif self.subdiv == "SP":
                self[date(year, MAR, 19)] = "San Giuseppe"
            elif self.subdiv == "SR":
                self[date(year, DEC, 13)] = "Santa Lucia"
            elif self.subdiv == "SS":
                self[date(year, DEC, 6)] = "San Nicola"
            elif self.subdiv == "SU":
                self[
                    date(year, MAY, 1) + rd(weekday=SU(+2)) + rd(weekday=TH)
                ] = "San Ponziano"  # <--- Thursday after second sunday in May
            elif self.subdiv == "SV":
                self[date(year, MAR, 18)] = "Nostra Signora della Misericordia"
            elif self.subdiv == "TA":
                self[date(year, MAY, 10)] = "San Cataldo"
            elif self.subdiv == "TE":
                self[date(year, DEC, 19)] = "San Berardo da Pagliara"
            elif self.subdiv == "TN":
                self[date(year, JUN, 26)] = "San Vigilio"
            elif self.subdiv == "TO":
                self[date(year, JUN, 24)] = "San Giovanni Battista"
            elif self.subdiv == "TP":
                self[date(year, AUG, 7)] = "Sant'Alberto degli Abati"
            elif self.subdiv == "TR":
                self[date(year, FEB, 14)] = "San Valentino"
            elif self.subdiv == "TS":
                self[date(year, NOV, 3)] = "San Giusto"
            elif self.subdiv == "TV":
                self[date(year, APR, 27)] = "San Liberale"
            elif self.subdiv == "UD":
                self[date(year, JUL, 12)] = "Santi Ermacora e Fortunato"
            elif self.subdiv == "VA":
                self[date(year, MAY, 8)] = "San Vittore il Moro"
            elif self.subdiv == "VB":
                self[date(year, MAY, 8)] = "San Vittore il Moro"
            elif self.subdiv == "VC":
                self[date(year, AUG, 1)] = "Sant'Eusebio di Vercelli"
            elif self.subdiv == "VE":
                self[date(year, APR, 25)] = "San Marco Evangelista"
            elif self.subdiv == "VI":
                self[date(year, APR, 25)] = "San Marco"
            elif self.subdiv == "VR":
                self[date(year, MAY, 21)] = "San Zeno"
            elif self.subdiv == "VT":
                self[date(year, SEP, 4)] = "Santa Rosa da Viterbo"
            elif self.subdiv == "VV":
                self[date(year, MAR, 1)] = "San Leoluca"


class IT(Italy):
    pass


class ITA(Italy):
    pass
