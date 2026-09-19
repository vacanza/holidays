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

from datetime import date

from holidays.constants import JAN, FEB, MAR, APR, MAY, OCT, NOV, DEC
from holidays.countries.sri_lanka import SriLanka, SriLankaStaticHolidays
from holidays.groups import StaticHolidays
from holidays.helpers import _normalize_arguments, _normalize_tuple, tr


class ColomboStockExchangeStaticHolidays:
    special_public_holidays = {
        **SriLankaStaticHolidays.special_public_holidays,
        2018: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2018, ())),
            # Special Bank Holiday.
            (JAN, 15, tr("විශේෂ බැංකු නිවාඩු දිනය")),
            # National Day Holiday.
            (FEB, 5, tr("ජාතික දින නිවාඩුව")),
            # Vesak Holiday.
            (APR, 30, tr("වෙසක් නිවාඩුව")),
        ),
        2019: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2019, ())),
            # CSE Customary Holiday.
            (JAN, 1, tr("CSE සාමාන්‍ය නිවාඩු දිනය")),
            (
                APR,
                15,
                # Special Bank Holiday on account of Sinhala & Tamil New Year Day
                # falling on a Sunday.
                tr("ඉරිදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව"),
            ),
            (
                MAY,
                20,
                # Special Bank Holiday on account of Day Following Vesak Full Moon Poya Day
                # falling on a Sunday.
                tr("ඉරිදා දිනක යෙදෙන වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව"),
            ),
            (
                NOV,
                11,
                # Special Bank Holiday on account of Holy Prophet's Birthday
                # falling on a Sunday.
                tr("ඉරිදා දිනක යෙදෙන නබි නායකතුමාගේ උපන් දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව"),
            ),
        ),
        2020: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2020, ())),
            # CSE Customary Holiday.
            (JAN, 1, tr("CSE සාමාන්‍ය නිවාඩු දිනය")),
            # Market closure due to COVID-19.
            (MAR, 20, tr("COVID-19 හේතුවෙන් වෙළඳපොළ වසා දැමීම")),
            (
                APR,
                14,
                # Special Bank Holiday on account of the Day prior to Sinhala & Tamil
                # New Year Day falling on a Sunday.
                tr("ඉරිදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය වෙනුවට විශේෂ බැංකු නිවාඩුව"),
            ),
        ),
        2021: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2021, ())),
            # CSE Customary Holiday.
            (JAN, 1, tr("CSE සාමාන්‍ය නිවාඩු දිනය")),
            # Additional holiday in lieu of May Day falling on Sunday.
            (MAY, 2, tr("ඉරිදා දිනක යෙදෙන මැයි දිනය වෙනුවට අතිරේක නිවාඩුව")),
            # Additional holiday in lieu of Christmas Day falling on Sunday.
            (DEC, 26, tr("ඉරිදා දිනක යෙදෙන නත්තල් උත්සව දිනය වෙනුවට අතිරේක නිවාඩුව")),
        ),
        2022: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2022, ())),
            # Additional holiday in lieu of May Day falling on Sunday.
            (MAY, 2, tr("ඉරිදා දිනක යෙදෙන මැයි දිනය වෙනුවට අතිරේක නිවාඩුව")),
            (
                OCT,
                10,
                # Additional holiday in lieu of Milad-Un-Nabi (Holy Prophet's Birthday)
                # falling on Sunday.
                tr("ඉරිදා දිනක යෙදෙන නබි නායකතුමාගේ උපන් දිනය වෙනුවට අතිරේක නිවාඩුව"),
            ),
            # Additional holiday in lieu of Christmas Day falling on Sunday.
            (DEC, 26, tr("ඉරිදා දිනක යෙදෙන නත්තල් උත්සව දිනය වෙනුවට අතිරේක නිවාඩුව")),
        ),
        2023: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2023, ())),
            (
                JAN,
                16,
                # Additional holiday in lieu of Tamil Thai Pongal Day falling on Sunday.
                tr("ඉරිදා දිනක යෙදෙන දෙමළ තෛපොංගල් දිනය වෙනුවට අතිරේක නිවාඩුව"),
            ),
        ),
        2024: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2024, ())),
            # CSE Customary Holiday.
            (JAN, 1, tr("CSE සාමාන්‍ය නිවාඩු දිනය")),
            # Additional holiday in lieu of Independence Day falling on Sunday.
            (FEB, 5, tr("ඉරිදා දිනක යෙදෙන නිදහස් සමරු දිනය වෙනුවට අතිරේක නිවාඩුව")),
        ),
        2025: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2025, ())),
            # Customary Holiday.
            (JAN, 1, tr("සාමාන්‍ය නිවාඩු දිනය")),
            # Special Bank Holiday.
            (APR, 15, tr("විශේෂ බැංකු නිවාඩු දිනය")),
        ),
        2026: (
            *_normalize_tuple(SriLankaStaticHolidays.special_public_holidays.get(2026, ())),
            # CSE Customary Holiday.
            (JAN, 1, tr("CSE සාමාන්‍ය නිවාඩු දිනය")),
        ),
    }

    special_half_day_holidays = {
        # Day prior to Sinhala & Tamil New Year day.
        2018: (APR, 13, tr("සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය")),
        2019: (
            APR,
            12,
            # Special Bank Half-holiday on account of Day prior to Sinhala & Tamil New Year Day
            # falling on a Saturday.
            tr("සෙනසුරාදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනට පෙර දිනය වෙනුවට විශේෂ බැංකු අර්ධ නිවාඩුව"),
        ),
        2021: (
            (
                APR,
                30,
                # Additional half-holiday on account of the May Day falling on a Saturday.
                tr("සෙනසුරාදා දිනක යෙදෙන මැයි දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව"),
            ),
            (
                DEC,
                24,
                # Additional half-holiday on account of the Christmas Day falling on a Saturday.
                tr("සෙනසුරාදා දිනක යෙදෙන නත්තල් උත්සව දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව"),
            ),
        ),
        2023: (
            (
                FEB,
                3,
                # Additional half holiday in lieu of the Independence Day falling on Saturday.
                tr("සෙනසුරාදා දිනක යෙදෙන නිදහස් සමරු දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව"),
            ),
            (
                MAY,
                4,
                # Additional half holiday in lieu of Day Following Vesak Full Moon Poya Day
                # falling on Saturday.
                tr("සෙනසුරාදා දිනක යෙදෙන වෙසක් පුර පසළොස්වක පෝය දිනට පසු දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව"),
            ),
        ),
        2024: (
            APR,
            10,
            # Additional half holiday in lieu of Sinhala & Tamil New Year Day
            # falling on Saturday.
            tr("සෙනසුරාදා දිනක යෙදෙන සිංහල හා දෙමළ අලුත් අවුරුදු දිනය වෙනුවට අතිරේක අර්ධ නිවාඩුව"),
        ),
    }


class ColomboStockExchange(SriLanka):
    """Colombo Stock Exchange (CSE) holidays."""

    country = None  # type: ignore[assignment]
    market = "XCOL"
    parent_entity = SriLanka
    supported_categories = ("public", "half_day")  # type: ignore[assignment]
    start_year = 2018

    def __init__(self, *args, **kwargs):
        years = kwargs.pop("years", None)
        if not years and len(args) > 0:
            years = args[0]
            args = (None,) + args[1:]
        super().__init__(*args, **kwargs)
        StaticHolidays.__init__(self, cls=ColomboStockExchangeStaticHolidays)
        if years is not None:
            self.years = set(_normalize_arguments(int, years))
            for year in self.years:
                self._populate(year)

    def _populate(self, year):
        super()._populate(year)

        for dt in tuple(self.keys()):
            if dt.year == year and self._is_weekend(dt):
                self.pop(dt)

    def _populate_public_holidays(self):
        super()._populate_public_holidays()

        if self._year == 2018:
            self.pop(date(2018, 4, 13), None)


class XCOL(ColomboStockExchange):
    pass


# References:
# 2026- https://cdn.cse.lk/cmt/upload_report_file/DXSvedMKDI9Qdp0J_20Apr2026114930GMT_1776685770276.pdf
# 2025- https://cdn.cse.lk/cmt/upload_report_file/Yc55Y9aEiyhAB71R_18Nov2024081707GMT_1731917827859.pdf
# 2024- https://cdn.cse.lk/cmt/upload_report_file/zM646FN086F69pB1_12Oct2023034430GMT_1697082270635.pdf
# 2023- https://cdn.cse.lk/cmt/report/HPtW1TbUWfysYSiH_28Sep2022105732GMT_1664362652950.pdf
# 2022- https://cdn.cse.lk/cmt/upload_cse_report_file/circulars_487_30-09-2021.pdf
# 2021- https://cdn.cse.lk/cmt/upload_cse_report_file/circulars_759_07-09-2020.pdf
# 2020- https://cdn.cse.lk/cmt/upload_cse_report_file/circulars_75_16-10-2019.pdf
# 2019- https://cdn.cse.lk/cmt/upload_cse_announcements/9501540465936_.pdf
# 2018- https://stockmarket-holidays.com/colombo-stock-exchange-holidays/133/
