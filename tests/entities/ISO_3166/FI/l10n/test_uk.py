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

from unittest import TestCase

from holidays.entities.ISO_3166.FI import FiHolidays
from tests.common import CommonCountryTests


class TestFiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FiHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
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
