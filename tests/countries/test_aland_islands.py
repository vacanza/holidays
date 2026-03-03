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

from holidays.constants import UNOFFICIAL
from holidays.countries.aland_islands import AlandIslands
from tests.common import CommonCountryTests


class TestAland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AlandIslands)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(
            AlandIslands(categories=UNOFFICIAL, years=range(self.start_year, 1950))
        )

    def test_alands_autonomy_day(self):
        name = "Ahvenanmaan itsehallintopäivä"
        self.assertHolidayName(name, (f"{year}-06-09" for year in range(1993, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1993))

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
            ("2022-06-09", "Ahvenanmaan itsehallintopäivä"),
            ("2022-06-24", "Juhannusaatto"),
            ("2022-06-25", "Juhannuspäivä; Suomen lipun päivä"),
            ("2022-07-06", "Eino Leinon päivä, runon ja suven päivä"),
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
            ("2022-05-08", "Mother's Day"),
            ("2022-05-09", "Europe Day"),
            ("2022-05-12", "J. V. Snellman Day, Day of Finnish Heritage"),
            ("2022-05-15", "Remembrance Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Flag Day of the Finnish Defense Forces"),
            ("2022-06-09", "Åland's Autonomy Day"),
            ("2022-06-24", "Midsummer Eve"),
            ("2022-06-25", "Day of the Finnish Flag; Midsummer Day"),
            ("2022-07-06", "Eino Leino Day, Day of Summer and Poetry"),
            ("2022-10-01", "Miina Sillanpää Day, Day of Civic Participation"),
            ("2022-10-10", "Aleksis Kivi Day, Day of Finnish Literature"),
            ("2022-10-24", "United Nations Day"),
            ("2022-11-05", "All Saints' Day"),
            ("2022-11-06", "Finnish Swedish Heritage Day, svenska dagen"),
            ("2022-11-13", "Father's Day"),
            ("2022-11-20", "Day of Children's Rights"),
            ("2022-12-06", "Independence Day"),
            ("2022-12-08", "Jean Sibelius Day, Day of Finnish Music"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
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
            ("2022-06-09", "Ålands självstyrelsedag"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-06-25", "Finlands flaggas dag; Midsommardagen"),
            ("2022-07-06", "Eino Leino-dagen, diktens och sommarens dag"),
            ("2022-10-01", "Miina Sillanpää-dagen, medborgarinflytandets dag"),
            ("2022-10-10", "Aleksis Kivi-dagen, den finska litteraturens dag"),
            ("2022-10-24", "FN-dagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-11-06", "Svenska dagen, Gustav Adolfsdagen"),
            ("2022-11-13", "Fars dag"),
            ("2022-11-20", "Barnkonventionens dag"),
            ("2022-12-06", "Självständighetsdagen"),
            ("2022-12-08", "Sibeliusdagen, den finländska musikens dag"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-02-05", "วันรูนแบร์ก"),
            ("2022-02-28", "วันกาเลวาลา, วันวัฒนธรรมฟินแลนด์"),
            ("2022-03-19", "วันมินน่า คานท์, วันแห่งความเสมอภาค"),
            ("2022-04-09", "วันมิคาเอล อากริโคลา, วันภาษาฟินแลนด์"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-27", "วันทหารผ่านศึกแห่งชาติ"),
            ("2022-05-01", "วันเมย์เดย์ (วันแรงงาน)"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-09", "วันยุโรป"),
            ("2022-05-12", "วันเจ.วี. สเนลล์มาน, วันมรดกฟินแลนด์"),
            ("2022-05-15", "วันรำลึก"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันกองกำลังป้องกันฟินแลนด์"),
            ("2022-06-09", "วันปกครองตนเองหมู่เกาะโอลันด์"),
            ("2022-06-24", "วันมิดซัมเมอร์อีฟ (วันก่อนวันกลางฤดูร้อน)"),
            ("2022-06-25", "วันธงชาติฟินแลนด์; วันมิดซัมเมอร์ (วันกลางฤดูร้อน)"),
            ("2022-07-06", "วันไอนอ ไลโน, วันแห่งบทกวีและฤดูร้อน"),
            ("2022-10-01", "วันมีนา ซิลลันแป, วันส่งเสริมการมีส่วนร่วมของพลเมือง"),
            ("2022-10-10", "วันอเล็กซิส กีวี, วันวรรณกรรมฟินแลนด์"),
            ("2022-10-24", "วันสหประชาชาติ"),
            ("2022-11-05", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-06", "วันมรดกสวีเดน-ฟินแลนด์, วันกุสตาฟวัส อดอลฟัส"),
            ("2022-11-13", "วันพ่อ"),
            ("2022-11-20", "วันสิทธิเด็ก"),
            ("2022-12-06", "วันประกาศอิสรภาพฟินแลนด์"),
            ("2022-12-08", "วันฌอง ซิเบลิอุส, วันดนตรีฟินแลนด์"),
            ("2022-12-24", "วันคริสต์มาสอีฟ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
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
            ("2022-06-09", "День автономії Аландських островів"),
            ("2022-06-24", "Переддень літнього сонцестояння"),
            ("2022-06-25", "День літнього сонцестояння; День прапора Фінляндії"),
            ("2022-07-06", "День Ейно Лейно, День літа та поезії"),
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
