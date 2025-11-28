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

from holidays.countries.djibouti import Djibouti
from tests.common import CommonCountryTests


class TestDjibouti(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Djibouti)

    def test_2019(self):
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "Nouvel an"),
            ("2019-04-03", "Al Isra et Al Mirague (estimé)"),
            ("2019-05-01", "Fête du travail"),
            ("2019-06-04", "Eid al-Fitr (estimé)"),
            ("2019-06-05", "Eid al-Fitr deuxième jour (estimé)"),
            ("2019-06-27", "Fête de l'indépendance"),
            ("2019-06-28", "Fête de l'indépendance deuxième jour"),
            ("2019-08-10", "Arafat (estimé)"),
            ("2019-08-11", "Eid al-Adha (estimé)"),
            ("2019-08-12", "Eid al-Adha deuxième jour (estimé)"),
            ("2019-08-31", "Nouvel an musulman (estimé)"),
            ("2019-11-09", "Anniversaire du prophète Muhammad (estimé)"),
            ("2019-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nouvel an"),
            ("2022-02-28", "Al Isra et Al Mirague (estimé)"),
            ("2022-05-01", "Fête du travail"),
            ("2022-05-02", "Eid al-Fitr (estimé)"),
            ("2022-05-03", "Eid al-Fitr deuxième jour (estimé)"),
            ("2022-06-27", "Fête de l'indépendance"),
            ("2022-06-28", "Fête de l'indépendance deuxième jour"),
            ("2022-07-08", "Arafat (estimé)"),
            ("2022-07-09", "Eid al-Adha (estimé)"),
            ("2022-07-10", "Eid al-Adha deuxième jour (estimé)"),
            ("2022-07-30", "Nouvel an musulman (estimé)"),
            ("2022-10-08", "Anniversaire du prophète Muhammad (estimé)"),
            ("2022-12-25", "Noël"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-01", "يوم السنة الجديدة"),
            ("2022-02-28", "الإسراء والمعراج (المقدرة)"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "عيد الفطر (المقدرة)"),
            ("2022-05-03", "عطلة عيد الفطر (المقدرة)"),
            ("2022-06-27", "عيد الإستقلال"),
            ("2022-06-28", "عطلة عيد الاستقلال"),
            ("2022-07-08", "يوم عرفة (المقدرة)"),
            ("2022-07-09", "عيد الأضحى (المقدرة)"),
            ("2022-07-10", "عطلة عيد الأضحى (المقدرة)"),
            ("2022-07-30", "رأس السنة الهجرية (المقدرة)"),
            ("2022-10-08", "عيد المولد النبوي (المقدرة)"),
            ("2022-12-25", "عيد الميلاد المجيد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Isra' and Mi'raj (estimated)"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr (estimated)"),
            ("2022-05-03", "Eid al-Fitr Holiday (estimated)"),
            ("2022-06-27", "Independence Day"),
            ("2022-06-28", "Independence Day Holiday"),
            ("2022-07-08", "Arafat Day (estimated)"),
            ("2022-07-09", "Eid al-Adha (estimated)"),
            ("2022-07-10", "Eid al-Adha Holiday (estimated)"),
            ("2022-07-30", "Islamic New Year (estimated)"),
            ("2022-10-08", "Prophet Muhammad's Birthday (estimated)"),
            ("2022-12-25", "Christmas Day"),
        )
