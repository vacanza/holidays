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

from holidays.constants import PUBLIC
from holidays.countries.indonesia import Indonesia
from holidays.helpers import tr


class IndonesiaStockExchange(Indonesia):
    """Indonesia Stock Exchange (IDX) holidays.

    IDX is closed on Indonesia public holidays and joint holidays (Cuti Bersama), and
    on December 31 for the year-end exchange holiday (Libur Bursa). Holidays falling on
    weekends are excluded.

    References:
        * [2022](https://web.archive.org/web/20261107155552/https://www.idx.co.id/StaticData/Annoder/Announcement/2022/4/11/241191/1.%20pengumuman-perubahan-kalender-libur-bursa-tahun-2022.pdf)
        * [2023](https://web.archive.org/web/20230531203020/https://utrade.co.id/ViewImportantNotice.aspx?idNotice=1091)
        * [2023 Eid al-Adha changes](https://web.archive.org/web/20230628132610/https://economy.okezone.com/read/2023/06/27/278/2837678/perdagangan-bei-dan-layanan-bank-indonesia-besok-libur-berikut-jadwal-lengkapnya)
        * [2024](https://web.archive.org/web/20261107154003/https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/Exchange/Peng-00233-No.%20Peng-00233BEI.POP11-2024.pdf)
        * [2025](https://web.archive.org/web/20261107154527/https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/Exchange/Peng-00213-No.%20Peng-00213BEI.POP10-2024.pdf)
        * [2025 Independence Day Joint Holiday](https://web.archive.org/web/20251204205405/https://www.idxcarbon.co.id/document/share/143/cf878b0d-87c1-45e2-98a5-4c54d6efc8c2)
        * [2026](https://web.archive.org/web/20261107155341/https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/Exchange/Peng-00171%20Libur%20Bursa%202026-No.%20Peng-00171BEI.POP09-2025.pdf)
        * [2027](https://web.archive.org/web/20261107161932/https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/Exchange/Libur%20Bursa%20Peng-00169%20ID-No.%20Peng-00169BEI.POP09-2026.pdf)
    """

    country = None  # type: ignore[assignment]
    market = "XIDX"
    parent_entity = Indonesia
    supported_categories: tuple[str, ...] = (PUBLIC,)  # type: ignore[assignment]
    start_year = 2022

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        # Joint Holidays.
        self._add_special_holidays(("special_government_holidays",))

        # Exchange Holiday.
        self._add_holiday_dec_31(tr("Libur Bursa"))

        for dt in tuple(self.keys()):
            if self._is_weekend(dt):
                self.pop(dt)


class XIDX(IndonesiaStockExchange):
    pass


class IDX(IndonesiaStockExchange):
    pass
