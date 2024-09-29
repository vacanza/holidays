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

from holidays.constants import OPTIONAL
from holidays.countries.greenland import Greenland, GL, GRL
from tests.common import CommonCountryTests


class TestGreenland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Greenland)

    def test_country_aliases(self):
        self.assertAliases(Greenland, GL, GRL)

    def test_2018(self):
        # https://www.officeholidays.com/countries/greenland/2018
        self.assertHolidays(
            ("2018-01-01", "Ukioq nutaaq"),
            ("2018-03-29", "Sisamanngornermi illernartumi"),
            ("2018-03-30", "Tallimanngorneq ajortorsiorneq"),
            ("2018-04-01", "Poorskimi"),
            ("2018-04-02", "Poorskimi ullut aappaat"),
            ("2018-04-27", "Ulloq qinuffiusoq"),
            ("2018-05-10", "Ulloq Kristusip qilaliarnera"),
            ("2018-05-20", "Piinsip ullua"),
            ("2018-05-21", "Piinsip ulluisa aappaanni"),
            ("2018-12-25", "Juulli"),
            ("2018-12-26", "Juullip aappaa"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Ukioq nutaaq"),
            ("2022-04-14", "Sisamanngornermi illernartumi"),
            ("2022-04-15", "Tallimanngorneq ajortorsiorneq"),
            ("2022-04-17", "Poorskimi"),
            ("2022-04-18", "Poorskimi ullut aappaat"),
            ("2022-05-13", "Ulloq qinuffiusoq"),
            ("2022-05-26", "Ulloq Kristusip qilaliarnera"),
            ("2022-06-05", "Piinsip ullua"),
            ("2022-06-06", "Piinsip ulluisa aappaanni"),
            ("2022-12-25", "Juulli"),
            ("2022-12-26", "Juullip aappaa"),
        )

    def test_2022_optional(self):
        self.assertHolidays(
            Greenland(categories=OPTIONAL, years=2022),
            ("2022-01-06", "Mitaarneq"),
            ("2022-05-01", "Sulisartut ulluat"),
            ("2022-06-21", "Ullortuneq"),
            ("2022-12-24", "Juulliaqqami"),
            ("2022-12-31", "Ukiortaami"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Ukioq nutaaq"),
            ("2022-01-06", "Mitaarneq"),
            ("2022-04-14", "Sisamanngornermi illernartumi"),
            ("2022-04-15", "Tallimanngorneq ajortorsiorneq"),
            ("2022-04-17", "Poorskimi"),
            ("2022-04-18", "Poorskimi ullut aappaat"),
            ("2022-05-01", "Sulisartut ulluat"),
            ("2022-05-13", "Ulloq qinuffiusoq"),
            ("2022-05-26", "Ulloq Kristusip qilaliarnera"),
            ("2022-06-05", "Piinsip ullua"),
            ("2022-06-06", "Piinsip ulluisa aappaanni"),
            ("2022-06-21", "Ullortuneq"),
            ("2022-12-24", "Juulliaqqami"),
            ("2022-12-25", "Juulli"),
            ("2022-12-26", "Juullip aappaa"),
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
