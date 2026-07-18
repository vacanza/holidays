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

# mypy: disable-error-code=attr-defined

import warnings
from calendar import isleap
from collections.abc import Iterable
from unittest import TestCase

from holidays.countries.india import India
from tests.common import CommonCountryTests


class TestIndia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", category=UserWarning)
        cls.hindu_start_year = 2001
        cls.hindu_end_year = 2035
        cls.hindu_full_range = range(cls.hindu_start_year, cls.hindu_end_year + 1)
        super().setUpClass(India, with_subdiv_categories=True)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_deprecated(self):
        # Deprecated Code, Remapped Code.
        for subdiv1, subdiv2 in (
            ("DD", "DH"),
            ("OR", "OD"),
        ):
            self.assertEqual(
                India(subdiv=subdiv1, years=2023).keys(),
                India(subdiv=subdiv2, years=2023).keys(),
            )

    def test_hindu_calendar_out_of_range_warning(self):
        with warnings.catch_warnings():
            warnings.simplefilter("default", UserWarning)
            for year in (
                *range(self.start_year, self.hindu_start_year),
                *range(self.hindu_end_year + 1, self.end_year),
            ):
                with self.assertWarns(UserWarning):
                    India(years=year)

    def _assertHinduHolidayHelper(  # noqa: N802
        self,
        name: str,
        dts: tuple[str, ...],
        *,
        category_optional: bool = False,
        subdivs: set | None = None,
        hindu_range: Iterable[int] | None = None,
        skip_years: set[int] | None = None,
    ):
        """Once HinduHolidays properly supports full Hindu calendar range,
        update the following section in your code to the following format:

            name = "Holiday Name"
            self.assertHolidayName(
                name,
                "2020-XX-XX",
                "2021-XX-XX",
                "2022-XX-XX",
                "2023-XX-XX",
                "2024-XX-XX",
                "2025-XX-XX",
            )
            self.assertHolidayName(name, self.full_range)

        hindu_range can be:
            - None (defaults to self.hindu_full_range)
            - range(2000, 2005)
            - (2002, 2007, 2010)

        skip_years may be used to skip holiday assertion,works for both public & optional assertion

        """
        effective_range = hindu_range or self.hindu_full_range
        if skip_years:
            effective_range = [y for y in effective_range if y not in skip_years]

        if category_optional is False and subdivs is None:
            self.assertHolidayName(name, dts)
            self.assertHolidayName(name, effective_range)

            self.assertNoHolidayName(
                name,
                range(self.start_year, self.hindu_start_year),
                range(self.hindu_end_year + 1, self.end_year),
            )
        # This assumes there's no subdiv-level optional holidays yet.
        elif category_optional is True:
            if skip_years:
                # holiday skipped from optional holidays for skip_years (may be present in public),
                # assert optional absence for those
                self.assertNoOptionalHolidayName(name, skip_years)
            else:
                # holiday never in public, assert absence for full range
                self.assertNoHolidayName(name)
            self.assertOptionalHolidayName(name, dts)
            self.assertOptionalHolidayName(name, effective_range)
            self.assertNoOptionalHolidayName(
                name,
                range(self.start_year, self.hindu_start_year),
                range(self.hindu_end_year + 1, self.end_year),
            )
        elif subdivs is not None:
            self.assertNoHolidayName(name)
            for subdiv, holidays in self.subdiv_holidays.items():
                if subdiv in subdivs:
                    self.assertHolidayName(name, holidays, dts)
                    self.assertNoHolidayName(
                        name,
                        holidays,
                        range(self.start_year, self.hindu_start_year),
                        range(self.hindu_end_year + 1, self.end_year),
                    )
                else:
                    self.assertNoHolidayName(name, holidays)

    # PUBLIC HOLIDAYS.

    def test_republic_day(self):
        name = "Republic Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(1950, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1950))

    def test_dr_b_r_ambedkars_jayanti(self):
        name = "Dr. B. R. Ambedkar's Jayanti"
        self.assertHolidayName(name, (f"{year}-04-14" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-08-15" for year in self.full_range))

    def test_gandhi_jayanti(self):
        self.assertHolidayName(
            "Mahatma Gandhi's Jayanti", (f"{year}-10-02" for year in self.full_range)
        )

    # Hindu holidays.

    def test_maha_shivaratri(self):
        name = "Maha Shivaratri"
        skip_years = {
            2003,
            2009,
            2010,
            2013,
            2014,
            2015,
            2016,
            2020,
            2021,
            2023,
            2024,
            2026,
        }
        dts = (
            "2022-03-01",
            "2025-02-26",
        )
        self._assertHinduHolidayHelper(name, dts, skip_years=skip_years)
        # OPTIONAL.
        dts = (
            "2020-02-21",
            "2021-03-11",
            "2023-02-18",
            "2024-03-08",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, skip_years=set(self.hindu_full_range) - skip_years
        )

    def test_holi(self):
        name = "Holi"
        skip_years = {2002, 2011}
        dts = (
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-08",
            "2024-03-25",
            "2025-03-14",
        )
        self._assertHinduHolidayHelper(name, dts, skip_years=skip_years)
        # OPTIONAL.
        dts = (
            "2002-03-29",
            "2011-03-20",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, skip_years=set(self.hindu_full_range) - skip_years
        )

    def test_ram_navami(self):
        name = "Ram Navami"
        skip_years = {2002, 2012, 2018, 2022, 2025, 2029}
        dts = (
            "2020-04-02",
            "2021-04-21",
            "2023-03-30",
            "2024-04-17",
        )
        self._assertHinduHolidayHelper(name, dts, skip_years=skip_years)
        # OPTIONAL.
        dts = (
            "2002-04-21",
            "2012-04-01",
            "2018-03-25",
            "2022-04-10",
            "2025-04-06",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, skip_years=set(self.hindu_full_range) - skip_years
        )

    def test_mahavir_jayanti(self):
        name = "Mahavir Jayanti"
        dts = (
            "2020-04-06",
            "2021-04-25",
            "2022-04-14",
            "2023-04-04",
            "2024-04-21",
            "2025-04-10",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_buddha_purnima(self):
        name = "Buddha Purnima"
        dts = (
            "2020-05-07",
            "2021-05-26",
            "2022-05-16",
            "2023-05-05",
            "2024-05-23",
            "2025-05-12",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_janmashtami(self):
        name_vaishnava = "Janmashtami (Vaishnava)"
        name_smarta = "Janmashtami (Smarta)"
        self.assertNoHolidayName(name_smarta)
        skip_years = {2008, 2017}
        dts = (
            "2020-08-12",
            "2021-08-30",
            "2022-08-19",
            "2023-09-07",
            "2024-08-26",
            "2025-08-16",
        )
        self._assertHinduHolidayHelper(name_vaishnava, dts, skip_years=skip_years)
        # OPTIONAL.
        dts = (
            "2008-08-24",
            "2017-08-15",
        )
        self._assertHinduHolidayHelper(
            name_vaishnava,
            dts,
            category_optional=True,
            skip_years=set(self.hindu_full_range) - skip_years,
        )
        dts = (
            "2007-09-03",
            "2008-08-28",
            "2020-08-11",
            "2021-08-30",
            "2022-08-18",
            "2023-09-06",
            "2025-08-15",
        )
        self.assertOptionalHolidayName(name_smarta, dts)
        self.assertNoOptionalHolidayName(
            name_smarta, set(self.hindu_full_range) - {2007, 2008, 2020, 2021, 2022, 2023, 2025}
        )

    def test_dussehra(self):
        name = "Dussehra"
        dts = (
            "2020-10-25",
            "2021-10-15",
            "2022-10-05",
            "2023-10-24",
            "2024-10-12",
            "2025-10-02",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_diwali(self):
        name = "Diwali (Deepavali)"
        dts = (
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self._assertHinduHolidayHelper(name, dts)

    def test_guru_nanak_jayanti(self):
        name = "Guru Nanak's Jayanti"
        dts = (
            "2020-11-30",
            "2021-11-19",
            "2022-11-08",
            "2023-11-27",
            "2024-11-15",
            "2025-11-05",
        )
        self._assertHinduHolidayHelper(name, dts)

    # Islamic holidays.

    def test_ashura(self):
        name = "Muharram"
        self.assertHolidayName(
            name,
            "2020-08-30",
            "2021-08-19",
            "2022-08-09",
            "2023-07-29",
            "2024-07-17",
            "2025-07-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "Milad-un-Nabi"
        self.assertHolidayName(
            name,
            "2020-10-30",
            "2021-10-19",
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "Id-ul-Fitr"
        self.assertHolidayName(
            name,
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-04-11",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Id-ul-Zuha (Bakrid)"
        self.assertHolidayName(
            name,
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-07",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    # Christian holidays.

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas(self):
        self.assertHolidayName("Christmas", (f"{year}-12-25" for year in self.full_range))

    # OPTIONAL HOLIDAYS.

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-01-01" for year in self.full_range))

    # Hindu holidays.

    def test_guru_gobind_singh_birthday(self):
        name = "Guru Gobind Singh's Jayanti"
        skip_years = {2018, 2023, 2026, 2031}
        fixed_years = range(2005, 2012)
        dts = (
            "2020-01-02",
            "2021-01-20",
            "2022-01-09",
            "2022-12-29",
            "2024-01-17",
            "2025-01-06",
            "2025-12-27",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True, skip_years=skip_years)
        self.assertOptionalHolidayName(name, (f"{year}-01-05" for year in fixed_years))
        self.assertOptionalHolidayName(name, "2011-12-31")
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"CH", "PB"})

    def test_lohri(self):
        name = "Lohri"
        dts = (
            "2020-01-14",
            "2021-01-13",
            "2022-01-13",
            "2024-01-13",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, hindu_range=(2020, 2021, 2022, 2024)
        )
        # SUBDIVS.
        self.assertSubdivPbOptionalHolidayName(name, dts)

    def test_makar_sankranti(self):
        name = "Makar Sankranti"
        name_as = "Magh Bihu"
        name_gj = "Uttarayan"
        dts = (
            "2020-01-15",
            "2021-01-14",
            "2022-01-14",
            "2023-01-14",
            "2024-01-14",
            "2025-01-14",
        )
        # OPTIONAL.
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_as, dts, subdivs={"AS"})
        self._assertHinduHolidayHelper(name_gj, dts, subdivs={"GJ"})

    def test_pongal(self):
        name_pongal = "Pongal"
        name_magh_bihu = "Magh Bihu"
        dts = (
            "2020-01-15",
            "2021-01-14",
            "2022-01-14",
            "2023-01-15",
            "2024-01-15",
            "2025-01-14",
        )
        self._assertHinduHolidayHelper(name_pongal, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_pongal, dts, subdivs={"TN"})
        dts = (
            "2021-01-14",
            "2022-01-14",
            "2023-01-14",
            "2024-01-15",
            "2025-01-14",
        )
        self._assertHinduHolidayHelper(
            name_magh_bihu,
            dts,
            category_optional=True,
            hindu_range=range(2021, self.hindu_end_year + 1),
        )

    def test_basant_panchami(self):
        name = "Basant Panchami / Shri Panchami"
        name_hr = "Sir Chottu Ram's Jayanti"
        dts = (
            "2020-01-29",
            "2021-02-16",
            "2022-02-05",
            "2023-01-26",
            "2024-02-14",
            "2025-02-02",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True, skip_years={2013})
        self.assertOptionalHolidayName("Shri Panchami", "2013-02-14")
        self.assertOptionalHolidayName("Basant Panchami", "2013-02-15")
        self.assertNoHolidayName("Shri Panchami")
        self.assertNoHolidayName("Basant Panchami")
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_hr, dts, subdivs={"HR"})
        self.assertSubdivPbOptionalHolidayName("Satguru Ram Singh's Jayanti", dts)

    def test_guru_ravidas_birthday(self):
        name = "Guru Ravi Das's Jayanti"
        dts = (
            "2020-02-09",
            "2021-02-27",
            "2022-02-16",
            "2023-02-05",
            "2024-02-24",
            "2025-02-12",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"HP"})

    def test_chhatrapati_shivaji_maharaj_jayanti(self):
        name = "Shivaji's Jayanti"
        name_full = "Chhatrapati Shivaji Maharaj Jayanti"
        self.assertNoHolidayName(name)
        self.assertNoHolidayName(name_full)
        self.assertOptionalHolidayName(name, (f"{year}-02-19" for year in self.full_range))
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MH":
                self.assertHolidayName(
                    name_full, holidays, (f"{year}-02-19" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name_full, holidays)

    def test_swami_dayanand_saraswati_jayanti(self):
        name = "Swami Dayanand Saraswati's Jayanti"
        dts = (
            "2020-02-18",
            "2021-03-08",
            "2022-02-26",
            "2023-02-15",
            "2024-03-06",
            "2025-02-23",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_holika_dahan(self):
        name_holika_dahan = "Holika Dahan"
        name_dolyatra = "Dolyatra"
        dts = (
            "2020-03-09",
            "2021-03-28",
            "2022-03-17",
            "2023-03-07",
            "2024-03-24",
            "2025-03-13",
        )
        self._assertHinduHolidayHelper(name_holika_dahan, dts, category_optional=True)
        self._assertHinduHolidayHelper(
            name_dolyatra, dts, category_optional=True, skip_years={2012, 2013, 2014, 2015}
        )
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_holika_dahan, dts, subdivs={"RJ", "UK"})

    def test_gudi_padwa(self):
        name_chaitra_sukladi = "Chaitra Sukladi"
        name_cheti_chand = "Cheti Chand"
        name_gudi_padwa = "Gudi Padwa"
        name_ugadi = "Ugadi"
        dts = (
            "2020-03-25",
            "2021-04-13",
            "2022-04-02",
            "2023-03-22",
            "2024-04-09",
            "2025-03-30",
        )
        self._assertHinduHolidayHelper(name_chaitra_sukladi, dts, category_optional=True)
        self._assertHinduHolidayHelper(name_cheti_chand, dts, category_optional=True)
        self._assertHinduHolidayHelper(name_gudi_padwa, dts, category_optional=True)
        self._assertHinduHolidayHelper(name_ugadi, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_gudi_padwa, dts, subdivs={"GA", "MH"})
        self._assertHinduHolidayHelper(name_ugadi, dts, subdivs={"AP", "KA", "TS"})

    def test_maharshi_kashyap_graha_jayanti(self):
        name = "Maharshi Kashyap and Maharaj Nishad Raj's Graha Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivUpOptionalHolidayName(name, (f"{year}-04-05" for year in self.full_range))

    def test_meshadi(self):
        name = "Meshadi (Tamil New Year's Day)"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-04-14" for year in self.full_range))

    def test_chandrashekhar_jayanti(self):
        name = "Chandrashekhar's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivUpOptionalHolidayName(name, (f"{year}-04-17" for year in self.full_range))

    def test_vaisakhadi(self):
        name_vaisakhadi = "Vaisakhadi"
        name_bahag_bihu = "Bahag Bihu"
        self.assertNoHolidayName(name_vaisakhadi)
        self.assertNoHolidayName(name_bahag_bihu)
        self.assertOptionalHolidayName(
            name_vaisakhadi,
            (f"{year}-04-14" for year in self.full_range if isleap(year)),
            (f"{year}-04-15" for year in self.full_range if not isleap(year)),
        )
        self.assertOptionalHolidayName(
            name_bahag_bihu,
            (f"{year}-04-14" for year in self.full_range if isleap(year)),
            (f"{year}-04-15" for year in self.full_range if not isleap(year)),
        )

    def test_vaisakhi(self):
        name = "Vaisakhi"
        dts = (
            "2020-04-13",
            "2021-04-14",
            "2022-04-14",
            "2023-04-14",
            "2024-04-13",
            "2025-04-13",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"HR", "PB"})
        self._assertHinduHolidayHelper("Baisakhi", dts, subdivs={"JK"})
        self.assertSubdivLaOptionalHolidayName(name, dts)
        self.assertSubdivLaOptionalHolidayName("Baisakhi", dts)

    def test_vishu(self):
        name = "Vishu"
        dts = (
            "2020-04-14",
            "2021-04-14",
            "2022-04-15",
            "2023-04-15",
            "2024-04-14",
            "2025-04-14",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_rabindranath_jayanti(self):
        name = "Guru Rabindranath's Jayanti"
        name_wb = "Rabindra Jayanti"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            (f"{year}-05-08" for year in range(2008, self.end_year) if isleap(year)),
            (f"{year}-05-09" for year in range(2008, self.end_year) if not isleap(year)),
        )
        self.assertNoOptionalHolidayName(name, range(self.start_year, 2008))
        # SUBDIVS.
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "WB":
                self.assertHolidayName(
                    name_wb, holidays, (f"{year}-05-09" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name_wb, holidays)

    def test_rath_yatra(self):
        name = "Rath Yatra"
        dts = (
            "2020-06-23",
            "2021-07-12",
            "2022-07-01",
            "2023-06-20",
            "2024-07-07",
            "2025-06-27",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_raksha_bandhan(self):
        name = "Raksha Bandhan"
        dts = (
            "2020-08-03",
            "2021-08-22",
            "2022-08-11",
            "2023-08-30",
            "2024-08-19",
            "2025-08-09",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self.assertSubdivHpWomenOptionalHolidayName(name, dts)
        self._assertHinduHolidayHelper(name, dts, subdivs={"GJ", "HR", "RJ", "UK", "UP"})

    def test_parsi_new_year_shahenshahi(self):
        name = "Parsi New Year"
        name_subdiv = "Parsi New Year (Shahenshahi)"
        self.assertNoHolidayName(name)
        self.assertNoHolidayName(name_subdiv)
        dts = (
            "1972-08-28",
            "2019-08-17",
            "2020-08-16",
            "2021-08-16",
            "2022-08-16",
            "2023-08-16",
            "2024-08-15",
            "2025-08-15",
        )
        self.assertOptionalHolidayName(name, dts)
        self.assertOptionalHolidayName(name, self.full_range)
        # SUBDIVS.
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"GJ", "MH"}:
                self.assertHolidayName(name_subdiv, holidays, dts)
                self.assertHolidayName(name_subdiv, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name_subdiv, holidays)

    def test_onam(self):
        name = "Onam"
        dts = (
            "2020-08-31",
            "2021-08-21",
            "2022-09-08",
            "2023-08-29",
            "2024-09-15",
            "2025-09-05",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"AN", "KL"})

    def test_ganesh_chaturthi(self):
        name = "Ganesh Chaturthi / Vinayak Chaturthi"
        dts = (
            "2020-08-22",
            "2021-09-10",
            "2022-08-31",
            "2024-09-07",
            "2025-08-27",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True, skip_years={2012, 2023})
        name_ganesh_chaturthi = "Ganesh Chaturthi"
        self.assertNoHolidayName(name_ganesh_chaturthi)
        self.assertOptionalHolidayName(
            name_ganesh_chaturthi,
            "2012-09-19",
            "2023-09-19",
        )
        name = "Vinayak Chaturthi"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2012-08-21",
            "2023-08-20",
        )
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_ganesh_chaturthi, dts, subdivs={"GA", "MH"})
        dts = (
            "2020-08-23",
            "2021-09-11",
            "2022-09-01",
            "2024-09-08",
            "2025-08-28",
        )
        self._assertHinduHolidayHelper("Ganesh Chaturthi (2nd Day)", dts, subdivs={"GA"})

    def test_dussehra_saptami(self):
        name = "Dussehra (Saptami)"
        dts = (
            "2020-10-22",
            "2021-10-12",
            "2022-10-02",
            "2023-10-21",
            "2024-10-10",
            "2025-09-29",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_dussehra_mahashtami(self):
        name = "Dussehra (Mahashtami)"
        name_rj = "Durgashtami"
        dts = (
            "2020-10-23",
            "2021-10-13",
            "2022-10-03",
            "2023-10-22",
            "2024-10-11",
            "2025-09-30",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_rj, dts, subdivs={"RJ"})

    def test_dussehra_mahanavami(self):
        name = "Dussehra (Mahanavami)"
        name_jk = "Mahanavami"
        self._assertHinduHolidayHelper(
            name, "2002-10-14", skip_years=set(self.hindu_full_range) - {2002}
        )
        # OPTIONAL.
        dts = (
            "2020-10-24",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
            "2025-10-01",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True, skip_years={2002})
        # SUBDIVS.
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "JK":
                self.assertHolidayName(name_jk, holidays, dts)
            else:
                self.assertNoHolidayName(name_jk, holidays)

    def test_maharshi_valmiki_jayanti(self):
        name = "Maharshi Valmiki's Jayanti"
        dts = (
            "2020-10-31",
            "2021-10-20",
            "2022-10-09",
            "2023-10-28",
            "2024-10-17",
            "2025-10-07",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"CH", "HP", "HR", "PB", "UK"})

    def test_karwa_chouth(self):
        name = "Karaka Chaturthi (Karwa Chouth)"
        dts = (
            "2020-11-04",
            "2021-10-24",
            "2022-10-13",
            "2023-11-01",
            "2024-10-20",
            "2025-10-10",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, hindu_range=range(2012, self.hindu_end_year + 1)
        )
        # SUBDIVS.
        self.assertSubdivHpWomenOptionalHolidayName("Karwa Chouth", dts)

    def test_deepavali_south_india(self):
        name = "Deepavali (South India)"
        dts = (
            "2014-10-22",
            "2015-11-10",
            "2016-10-29",
            "2017-10-18",
            "2018-11-06",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, hindu_range=range(self.hindu_start_year, 2019)
        )

    def test_naraka_chaturdashi(self):
        name = "Naraka Chaturdashi"
        dts = (
            "2020-11-14",
            "2021-11-04",
            "2022-10-24",
            "2023-11-12",
            "2024-10-31",
            "2025-10-20",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)

    def test_govardhan_puja(self):
        name_bali_pratipada = "Diwali (Bali Pratipada)"
        name = "Govardhan Puja"
        name_vishwakarma_day = "Vishwakarma Day"
        dts = (
            "2020-11-15",
            "2021-11-05",
            "2022-10-25",
            "2023-11-13",
            "2024-11-02",
            "2025-10-22",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_bali_pratipada, dts, subdivs={"MH"})
        self._assertHinduHolidayHelper(name, dts, subdivs={"UP", "RJ"})
        self._assertHinduHolidayHelper(name_vishwakarma_day, dts, subdivs={"HR", "PB"})

    def test_bhai_duj(self):
        name = "Bhai Duj"
        dts = (
            "2020-11-16",
            "2021-11-06",
            "2022-10-26",
            "2023-11-14",
            "2024-11-03",
            "2025-10-23",
        )
        self._assertHinduHolidayHelper(name, dts, category_optional=True)
        # SUBDIVS.
        self._assertHinduHolidayHelper(name, dts, subdivs={"GJ", "UP", "RJ"})
        self._assertHinduHolidayHelper("Chitragupt's Jayanti", dts, subdivs={"UP"})
        self.assertSubdivHpWomenOptionalHolidayName(name, dts)

    def test_chhath_puja(self):
        name = "Pratihar Shashthi or Surya Shashthi (Chhat Puja)"
        name_subdiv = "Chhath Puja"
        dts = (
            "2020-11-20",
            "2021-11-10",
            "2022-10-30",
            "2023-11-19",
            "2024-11-07",
            "2025-10-28",
        )
        self._assertHinduHolidayHelper(
            name, dts, category_optional=True, hindu_range=range(2011, self.hindu_end_year + 1)
        )
        # SUBDIVS.
        self._assertHinduHolidayHelper(name_subdiv, dts, subdivs={"BR", "DL", "JH"})

    def test_guru_tegh_bahadurs_martyrdom_day(self):
        name = "Guru Tegh Bahadur's Shaheedi Diwas"
        dts = (
            "2002-12-08",
            "2003-11-28",
        )
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, dts)
        self.assertOptionalHolidayName(
            name, (f"{year}-11-24" for year in range(2004, self.end_year))
        )
        self.assertNoOptionalHolidayName(name, range(self.start_year, 2002))
        # SUBDIVS.
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in ("PB", "UK"):
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-24" for year in range(2004, self.end_year))
                )
            else:
                self.assertNoHolidayName(name, holidays)

    # Islamic holidays.

    def test_ali_birthday(self):
        name = "Hazarat Ali's Birthday"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-03-09",
            "2021-02-26",
            "2022-02-15",
            "2023-02-05",
            "2024-01-25",
            "2025-01-14",
        )
        self.assertOptionalIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_jumuatul_wida(self):
        name = "Jamat-Ul-Vida"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-05-22",
            "2021-05-07",
            "2022-04-29",
            "2023-04-21",
            "2024-04-05",
            "2025-03-28",
        )
        self.assertOptionalIslamicNoEstimatedHolidayName(name, self.full_range)

    # Christian holidays.

    def test_christmas_eve(self):
        name = "Christmas Eve"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name, (f"{year}-12-24" for year in range(2003, self.end_year))
        )
        self.assertNoOptionalHolidayName(name, range(self.start_year, 2003))

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertOptionalHolidayName(name, range(2007, self.end_year))
        self.assertNoOptionalHolidayName(range(self.start_year, 2007))

    # SUBDIV PUBLIC HOLIDAYS.

    def test_thiruvalluvar_day_mattu_pongal(self):
        name = "Thiruvalluvar Day / Mattu Pongal"
        dts = (
            "2020-01-16",
            "2021-01-15",
            "2022-01-15",
            "2023-01-16",
            "2024-01-16",
            "2025-01-15",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"TN"})

    def test_uzhavar_thirunal(self):
        name = "Uzhavar Thirunal"
        dts = (
            "2020-01-17",
            "2021-01-16",
            "2022-01-16",
            "2023-01-17",
            "2024-01-17",
            "2025-01-16",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"TN"})

    def test_feast_of_st_joseph_vaz(self):
        name = "Feast of St. Joseph Vaz"
        self.assertNoHolidayName(name)
        self.assertSubdivGaOptionalHolidayName(name, (f"{year}-01-16" for year in self.full_range))

    def test_karpuri_thakur_jayanti(self):
        name = "Karpuri Thakur's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivUpOptionalHolidayName(name, (f"{year}-01-24" for year in self.full_range))

    def test_statehood_day(self):
        name = "Statehood Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-25" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_mizoram_state_day(self):
        name = "Mizoram State Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MZ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-20" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_gadge_maharaj_jayanti(self):
        name = "Gadge Maharaj's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivRjOptionalHolidayName(name, (f"{year}-02-23" for year in self.full_range))

    def test_hola_mohalla(self):
        name = "Hola Mohalla"
        dts = (
            "2020-03-10",
            "2021-03-29",
            "2022-03-18",
            "2023-03-11",
            "2024-03-25",
            "2025-03-14",
        )
        self.assertSubdivPbOptionalHolidayName(name, dts)
        self.assertNoHolidayName(name)

    def test_cheti_chand(self):
        name = "Cheti Chand"
        dts = (
            "2020-03-26",
            "2021-04-13",
            "2022-04-02",
            "2023-03-23",
            "2024-04-10",
            "2025-03-30",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"GJ", "RJ", "UK"})
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_chaitra_navratri(self):
        name = "1st Navratra"
        dts = (
            "2020-03-25",
            "2021-04-13",
            "2022-04-02",
            "2023-03-22",
            "2024-04-09",
            "2025-03-30",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"JK"})
        self.assertSubdivLaOptionalHolidayName(name, dts)

    def test_nauroz(self):
        name = "Nauroz"
        self.assertNoHolidayName(name)
        dts = (
            "2020-03-20",
            "2021-03-21",
            "2022-03-21",
            "2023-03-21",
            "2024-03-20",
            "2025-03-21",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in ("JK", "LA"):
                self.assertHolidayName(name, holidays, dts)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bihar_day(self):
        name = "Bihar Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-22" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_shaheedi_diwas(self):
        name = "Shaheed-e-Azam Bhagat Singh, Sukhdev and Rajguru's Shaheedi Diwas"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in ("HR", "PB"):
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-23" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_odisha_day(self):
        name = "Odisha Day (Utkala Dibasa)"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "OD":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_guru_nabha_das_birthday(self):
        name = "Guru Nabha Dass's Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-08" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_jyotiba_phule_birthday(self):
        name = "Mahatma Jyotiba Phule's Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-11" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertNoHolidayName(name)
        self.assertSubdivUkOptionalHolidayName(name, dts)
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_puthandu(self):
        name = "Puthandu (Tamil New Year)"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-14" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_himachal_day(self):
        name = "Himachal Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maha_vishuva_sankranti(self):
        name = "Maha Vishuva Sankranti / Pana Sankranti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "OD":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pohela_boishakh(self):
        name = "Pohela Boishakh"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "WB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maundy_thursday(self):
        name = "Maundy Thursday"
        dts = (
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertNoHolidayName(name)
        self.assertSubdivGaOptionalHolidayName(name, dts)

    def test_parshuram_jayanti(self):
        name = "Bhagvan Shri Parshuram's Jayanti"
        name_akshay_tritiya = "Akshay Tritiya"
        dts = (
            "2020-04-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
            "2024-05-10",
            "2025-04-29",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"GJ", "HP", "HR", "PB", "RJ"})
        self._assertHinduHolidayHelper(name_akshay_tritiya, dts, subdivs={"HR"})
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_maharashtra_day(self):
        name = "Maharashtra Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)
                self.assertNoHolidayName(name, holidays)

    def test_kesari_chand_martyrdom_day(self):
        name = "Veer Kesari Chand's Shaheedi Diwas"
        self.assertNoHolidayName(name)
        self.assertSubdivUkOptionalHolidayName(name, (f"{year}-05-03" for year in self.full_range))

    def test_sikkim_state_day(self):
        name = "Sikkim State Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SK":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maharana_pratap_jayanti(self):
        name = "Maharana Pratap's Jayanti"
        dts = (
            "2020-05-25",
            "2021-06-13",
            "2022-06-02",
            "2023-05-22",
            "2024-06-09",
            "2025-05-29",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"HP", "HR", "RJ"})
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_guru_arjun_dev_martyrdom_day(self):
        name = "Guru Arjun Dev's Shaheedi Diwas"
        dts = (
            "2020-05-26",
            "2021-06-14",
            "2022-06-03",
            "2023-05-23",
            "2024-06-10",
            "2025-05-30",
        )
        self.assertSubdivChOptionalHolidayName(name, dts)
        self.assertSubdivHrOptionalHolidayName(name, dts)
        self.assertSubdivJkOptionalHolidayName(name, dts)
        self.assertSubdivLaOptionalHolidayName(name, dts)
        self._assertHinduHolidayHelper(name, dts, subdivs={"PB"})

    def test_kabir_jayanti(self):
        name = "Sant Kabir's Jayanti"
        dts = (
            "2020-06-05",
            "2021-06-24",
            "2022-06-14",
            "2023-06-04",
            "2024-06-22",
            "2025-06-11",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"HP", "HR", "PB"})
        self.assertSubdivChOptionalHolidayName(name, dts)

    def test_telangana_formation_day(self):
        name = "Telangana Formation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-02" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_feast_sacred_heart(self):
        name = "Feast of Sacred Heart of Jesus"
        self.assertNoHolidayName(name)
        self.assertSubdivGaOptionalHolidayName(name, (f"{year}-06-12" for year in self.full_range))

    def test_bonalu(self):
        name = "Bonalu"
        dts = (
            "2018-08-06",
            "2019-07-29",
            "2020-07-20",
            "2021-08-02",
            "2022-07-25",
            "2023-07-17",
            "2024-07-29",
            "2025-07-21",
            "2026-08-10",
            "2027-08-02",
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(2018, 2028))
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 2018), range(2028, self.end_year)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_harela(self):
        name = "Harela"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in ("UK"):
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_udham_singh_martyrdom_day(self):
        name = "Shaheed Udham Singh's Shaheedi Diwas"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in ("HR", "PB"):
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-31" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_samvatsari_day(self):
        name = "Samvatsari Day"
        dts = (
            "2020-08-23",
            "2021-09-11",
            "2022-09-01",
            "2023-09-20",
            "2024-09-08",
            "2025-08-28",
        )
        self.assertSubdivPbOptionalHolidayName(name, dts)
        self.assertNoHolidayName(name)

    def test_indigenous_peoples_day(self):
        name = "International Day of Adivasi Peoples"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-09" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_puducherry_de_jure_transfer_day(self):
        name = "Puducherry De Jure Transfer Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PY":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_khejarli_martyrdom_day(self):
        name = "Khejarli's Shaheedi Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-11" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_hari_singh_birthday(self):
        name = "Maharaja Hari Singh's Jayanti"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "JK":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-23" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_haryana_war_heroes_martyrdom_day(self):
        name = "Haryana War Heroes's Shaheedi Diwas"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-23" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maharaj_agrasen_jayanti(self):
        name = "Maharaj Agrasen's Jayanti"
        dts = (
            "2020-10-17",
            "2021-10-07",
            "2022-09-26",
            "2023-10-15",
            "2024-10-03",
            "2025-09-22",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"HR", "PB", "RJ"})
        self.assertSubdivChOptionalHolidayName(name, dts)
        self.assertSubdivUkOptionalHolidayName(name, dts)
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_bathukamma_festival(self):
        name = "Bathukamma Festival"
        dts = (
            "2020-10-16",
            "2021-10-06",
            "2022-09-25",
            "2023-10-14",
            "2024-10-02",
            "2025-09-21",
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(2010, self.hindu_end_year + 1))
                self.assertNoHolidayName(
                    name,
                    holidays,
                    range(self.start_year, 2010),
                    range(self.hindu_end_year + 1, self.end_year),
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_accession_day(self):
        name = "Accession Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "JK":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-26" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sardar_vallabhbhai_patel_jayanti(self):
        name = "Sardar Vallabhbhai Patel's Jayanti"
        name_narendra_dev_jayanti = "Acharya Narendra Dev's Jayanti"
        self.assertNoHolidayName(name)
        self.assertNoHolidayName(name_narendra_dev_jayanti)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GJ":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)
        self.assertSubdivUpOptionalHolidayName(name, (f"{year}-10-31" for year in self.full_range))
        self.assertSubdivUpOptionalHolidayName(
            name_narendra_dev_jayanti, (f"{year}-10-31" for year in self.full_range)
        )

    def test_andhra_pradesh_foundation_day(self):
        name = "Andhra Pradesh Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_chhattisgarh_foundation_day(self):
        name = "Chhattisgarh Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CG":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_haryana_foundation_day(self):
        name = "Haryana Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "HR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_karnataka_rajyotsava(self):
        name = "Karnataka Rajyotsava"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_kerala_foundation_day(self):
        name = "Kerala Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "KL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_madhya_pradesh_foundation_day(self):
        name = "Madhya Pradesh Foundation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MP":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_puducherry_liberation_day(self):
        name = "Puducherry Liberation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PY":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_all_souls_day(self):
        name = "All Souls Day"
        self.assertNoHolidayName(name)
        self.assertSubdivGaOptionalHolidayName(name, (f"{year}-11-02" for year in self.full_range))

    def test_jharkhand_formation_day(self):
        name = "Jharkhand Formation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "JH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_kartar_singh_martyrdom_day(self):
        name = "Kartar Singh Sarabha's Shaheedi Diwas"
        name_uda_devi_shaheedi_diwas = "Veerangana Uda Devi's Shaheedi Diwas"
        self.assertNoHolidayName(name)
        self.assertNoHolidayName(name_uda_devi_shaheedi_diwas)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-16" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)
        self.assertSubdivUpOptionalHolidayName(
            name_uda_devi_shaheedi_diwas, (f"{year}-11-16" for year in self.full_range)
        )

    def test_nagaland_state_inauguration_day(self):
        name = "Nagaland State Inauguration Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_assam_day(self):
        name = "Assam Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "AS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-02" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_feast_of_st_francois_xavier(self):
        name = "Feast of St. Francis Xavier"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-03" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_feast_of_immaculate_conception_of_mary(self):
        name = "Feast of Immaculate Conception of Mary"
        self.assertNoHolidayName(name)
        self.assertSubdivGaOptionalHolidayName(name, (f"{year}-12-08" for year in self.full_range))

    def test_goa_liberation_day(self):
        name = "Goa Liberation Day"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-19" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    # SUBDIV OPTIONAL HOLIDAYS.

    def test_womens_day(self):
        name = "International Women's Day"
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, (f"{year}-03-08" for year in self.full_range))

    def test_ranjit_singh_death_anniversary(self):
        name = "Maharaja Ranjit Singh's Death Anniversary"
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, (f"{year}-06-27" for year in self.full_range))

    def test_anant_chaturdashi(self):
        name = "Anant Chaturdashi"
        dts = (
            "2020-09-01",
            "2021-09-20",
            "2022-09-09",
            "2023-09-28",
            "2024-09-17",
            "2025-09-06",
        )
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, dts)
        self.assertSubdivRjOptionalHolidayName(name, dts)
        self.assertSubdivUkOptionalHolidayName(name, dts)
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_vishwakarma_puja(self):
        name = "Vishwakarma Puja"
        dts = (
            "2020-09-16",
            "2021-09-17",
            "2022-09-17",
            "2023-09-17",
            "2024-09-16",
            "2025-09-17",
        )
        self._assertHinduHolidayHelper(name, dts, subdivs={"UK"})
        self.assertSubdivUpOptionalHolidayName(name, dts)

    def test_saragarhi_day(self):
        name = "Saragarhi Day"
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, (f"{year}-09-12" for year in self.full_range))

    def test_bhagat_singh_birthday(self):
        name = "Bhagat Singh's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, (f"{year}-09-28" for year in self.full_range))

    def test_banda_singh_birthday(self):
        name = "Baba Banda Singh Bahadur's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, (f"{year}-10-16" for year in self.full_range))

    def test_new_punjab_day(self):
        name = "New Punjab Day"
        self.assertNoHolidayName(name)
        self.assertSubdivPbOptionalHolidayName(name, (f"{year}-11-01" for year in self.full_range))

    def test_chaudhary_charan_singh_jayanti(self):
        name = "Chaudhary Charan Singh's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivUpOptionalHolidayName(name, (f"{year}-12-23" for year in self.full_range))

    def test_udham_singh_jayanti(self):
        name = "Shaheed Udham Singh's Jayanti"
        self.assertNoHolidayName(name)
        self.assertSubdivHrOptionalHolidayName(name, (f"{year}-12-26" for year in self.full_range))

    def test_jor_mela_fatehgarh_sahib(self):
        name = "Jor Mela Fatehgarh Sahib"
        self.assertNoHolidayName(name)
        self.assertSubdivChOptionalHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        self.assertSubdivChOptionalHolidayName(name, (f"{year}-12-27" for year in self.full_range))
        self.assertSubdivChOptionalHolidayName(name, (f"{year}-12-28" for year in self.full_range))
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-28" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_new_years_eve(self):
        name = "New Year's Eve"
        self.assertNoHolidayName(name)
        self.assertSubdivGaOptionalHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_2018(self):
        self.assertHolidayDatesInYear(
            2018,
            "2018-01-26",
            "2018-02-13",
            "2018-03-02",
            "2018-03-29",
            "2018-03-30",
            "2018-04-14",
            "2018-04-30",
            "2018-06-16",
            "2018-08-15",
            "2018-08-22",
            "2018-09-03",
            "2018-09-21",
            "2018-10-02",
            "2018-10-19",
            "2018-11-07",
            "2018-11-21",
            "2018-11-23",
            "2018-12-25",
        )

        subdiv_holidays_mapping = {
            "AN": (
                "2018-04-14",
                "2018-08-24",
            ),
            "AP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "AS": (
                "2018-01-14",
                "2018-12-02",
            ),
            "BR": (
                "2018-03-22",
                "2018-04-14",
                "2018-11-13",
            ),
            "CG": (
                "2018-04-14",
                "2018-11-01",
            ),
            "CH": ("2018-04-14",),
            "DL": ("2018-11-13",),
            "GA": (
                "2018-04-14",
                "2018-12-19",
            ),
            "GJ": (
                "2018-01-14",
                "2018-04-14",
                "2018-05-01",
                "2018-10-31",
            ),
            "HP": (
                "2018-04-14",
                "2018-04-15",
            ),
            "HR": (
                "2018-04-14",
                "2018-11-01",
            ),
            "JH": (
                "2018-04-14",
                "2018-11-13",
                "2018-11-15",
            ),
            "JK": ("2018-04-14",),
            "KA": (
                "2018-04-14",
                "2018-11-01",
            ),
            "KL": (
                "2018-04-14",
                "2018-08-24",
                "2018-11-01",
            ),
            "LA": ("2018-04-14",),
            "MH": (
                "2018-02-19",
                "2018-03-18",
                "2018-04-14",
                "2018-05-01",
            ),
            "MP": (
                "2018-04-14",
                "2018-11-01",
            ),
            "MZ": ("2018-02-20",),
            "NL": ("2018-12-01",),
            "OD": (
                "2018-04-01",
                "2018-04-14",
                "2018-04-15",
            ),
            "PB": (
                "2018-01-13",
                "2018-04-14",
                "2018-11-01",
            ),
            "PY": (
                "2018-04-14",
                "2018-08-16",
                "2018-11-01",
            ),
            "RJ": (
                "2018-03-30",
                "2018-04-14",
                "2018-06-16",
            ),
            "SK": (
                "2018-04-14",
                "2018-05-16",
            ),
            "TN": (
                "2018-01-14",
                "2018-01-15",
                "2018-01-16",
                "2018-04-14",
            ),
            "TS": (
                "2018-04-14",
                "2018-06-02",
                "2018-10-08",
            ),
            "UK": ("2018-04-14",),
            "UP": (
                "2018-01-24",
                "2018-04-14",
                "2018-11-13",
            ),
            "WB": (
                "2018-04-14",
                "2018-04-15",
                "2018-05-09",
            ),
        }

        for subdiv, dates in subdiv_holidays_mapping.items():
            self.assertHoliday(self.subdiv_holidays[subdiv], dates)

    def test_2018_optional(self):
        self.assertOptionalHolidayDatesInYear(
            2018,
            "2018-01-01",
            "2018-01-14",
            "2018-01-22",
            "2018-01-31",
            "2018-02-10",
            "2018-02-19",
            "2018-03-01",
            "2018-03-18",
            "2018-03-25",
            "2018-04-01",
            "2018-04-14",
            "2018-04-15",
            "2018-05-09",
            "2018-06-15",
            "2018-07-14",
            "2018-08-17",
            "2018-08-24",
            "2018-08-26",
            "2018-09-13",
            "2018-10-16",
            "2018-10-17",
            "2018-10-24",
            "2018-10-27",
            "2018-11-06",
            "2018-11-08",
            "2018-11-09",
            "2018-11-13",
            "2018-11-24",
            "2018-12-24",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "New Year's Day"),
            ("2018-01-13", "Lohri"),
            ("2018-01-14", "Magh Bihu; Makar Sankranti; Pongal; Uttarayan"),
            ("2018-01-15", "Thiruvalluvar Day / Mattu Pongal"),
            ("2018-01-16", "Uzhavar Thirunal"),
            ("2018-01-22", "Basant Panchami / Shri Panchami"),
            ("2018-01-24", "UP Formation Day"),
            ("2018-01-26", "Republic Day"),
            ("2018-01-31", "Guru Ravi Das's Jayanti"),
            ("2018-02-10", "Swami Dayanand Saraswati's Jayanti"),
            ("2018-02-13", "Maha Shivaratri"),
            ("2018-02-19", "Chhatrapati Shivaji Maharaj Jayanti; Shivaji's Jayanti"),
            ("2018-02-20", "Mizoram State Day"),
            ("2018-03-01", "Dolyatra; Holika Dahan"),
            ("2018-03-02", "Holi"),
            ("2018-03-18", "Chaitra Sukladi; Cheti Chand; Gudi Padwa; Ugadi"),
            ("2018-03-22", "Bihar Day"),
            ("2018-03-25", "Ram Navami"),
            ("2018-03-29", "Mahavir Jayanti"),
            ("2018-03-30", "Good Friday; Rajasthan Day"),
            ("2018-04-01", "Easter Sunday; Hazarat Ali's Birthday; Odisha Day (Utkala Dibasa)"),
            (
                "2018-04-14",
                "Dr. B. R. Ambedkar's Jayanti; "
                "Meshadi (Tamil New Year's Day); "
                "Puthandu (Tamil New Year); "
                "Vaisakhi; "
                "Vishu",
            ),
            (
                "2018-04-15",
                "Bahag Bihu; "
                "Himachal Day; "
                "Maha Vishuva Sankranti / Pana Sankranti; "
                "Pohela Boishakh; "
                "Vaisakhadi",
            ),
            ("2018-04-30", "Buddha Purnima"),
            ("2018-05-01", "Gujarat Day; Maharashtra Day"),
            ("2018-05-09", "Guru Rabindranath's Jayanti; Rabindra Jayanti"),
            ("2018-05-16", "Sikkim State Day"),
            ("2018-06-02", "Telangana Formation Day"),
            ("2018-06-15", "Jamat-Ul-Vida"),
            ("2018-06-16", "Id-ul-Fitr; Maharana Pratap Jayanti"),
            ("2018-07-14", "Rath Yatra"),
            ("2018-08-06", "Bonalu"),
            ("2018-08-15", "Independence Day"),
            ("2018-08-16", "Puducherry De Jure Transfer Day"),
            ("2018-08-17", "Parsi New Year; Parsi New Year (Shahenshahi)"),
            ("2018-08-22", "Id-ul-Zuha (Bakrid)"),
            ("2018-08-24", "Onam"),
            ("2018-08-26", "Raksha Bandhan"),
            ("2018-09-03", "Janmashtami (Vaishnava)"),
            ("2018-09-13", "Ganesh Chaturthi / Vinayak Chaturthi"),
            ("2018-09-21", "Muharram"),
            ("2018-10-02", "Mahatma Gandhi's Jayanti"),
            ("2018-10-08", "Bathukamma Festival"),
            ("2018-10-16", "Dussehra (Saptami)"),
            ("2018-10-17", "Dussehra (Mahanavami); Dussehra (Mahashtami)"),
            ("2018-10-19", "Dussehra"),
            ("2018-10-24", "Maharishi Valmiki's Jayanti"),
            ("2018-10-27", "Karaka Chaturthi (Karwa Chouth)"),
            ("2018-10-31", "Sardar Vallabhbhai Patel Jayanti"),
            (
                "2018-11-01",
                "Andhra Pradesh Foundation Day; "
                "Chhattisgarh Foundation Day; "
                "Haryana Foundation Day; "
                "Karnataka Rajyotsava; "
                "Kerala Foundation Day; "
                "Madhya Pradesh Foundation Day; "
                "New Punjab Day; "
                "Puducherry Liberation Day",
            ),
            ("2018-11-06", "Deepavali (South India); Naraka Chaturdashi"),
            ("2018-11-07", "Diwali (Deepavali)"),
            ("2018-11-08", "Govardhan Puja"),
            ("2018-11-09", "Bhai Duj"),
            ("2018-11-13", "Chhath Puja; Pratihar Shashthi or Surya Shashthi (Chhat Puja)"),
            ("2018-11-15", "Jharkhand Formation Day"),
            ("2018-11-21", "Milad-un-Nabi"),
            ("2018-11-23", "Guru Nanak's Jayanti"),
            ("2018-11-24", "Guru Tegh Bahadur's Martyrdom Day"),
            ("2018-12-01", "Nagaland State Inauguration Day"),
            ("2018-12-02", "Assam Day"),
            ("2018-12-19", "Goa Liberation Day"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas"),
        )

    def test_l10n_bn(self):
        self.assertLocalizedHolidays(
            "bn",
            ("2018-01-01", "নববর্ষের দিন"),
            ("2018-01-13", "লোহরি"),
            ("2018-01-14", "উত্তরায়ণ; পোঙ্গল; মকর সংক্রান্তি; মাঘ বিহু"),
            ("2018-01-15", "তিরুভাল্লুভার দিবস / মাট্টু পোঙ্গল"),
            ("2018-01-16", "উঝাভার থিরুনাল"),
            ("2018-01-22", "বসন্ত পঞ্চমী / শ্রী পঞ্চমী"),
            ("2018-01-24", "উত্তরপ্রদেশ গঠন দিবস"),
            ("2018-01-26", "প্রজাতন্ত্র দিবস"),
            ("2018-01-31", "গুরু রবি দাসের জন্মদিন"),
            ("2018-02-10", "স্বামী দয়ানন্দ সরস্বতী জয়ন্তী"),
            ("2018-02-13", "মহাশিবরাত্রি"),
            ("2018-02-19", "ছত্রপতি শিবাজী মহারাজ জয়ন্তী; শিবাজীর জয়ন্তী"),
            ("2018-02-20", "মিজোরাম প্রতিষ্ঠা দিবস"),
            ("2018-03-01", "দোলযাত্রা; হোলিকা দহন"),
            ("2018-03-02", "হোলি"),
            ("2018-03-18", "উগাদি; গুড়ি পাড়ওয়া; চেতি চাঁদ; চৈত্র শুক্লাদি"),
            ("2018-03-22", "বিহার দিবস"),
            ("2018-03-25", "রাম নবমী"),
            ("2018-03-29", "মহাবীর জয়ন্তী"),
            ("2018-03-30", "গুড ফ্রাইডে; রাজস্থান দিবস"),
            ("2018-04-01", "ইস্টার রবিবার; ওড়িশা দিবস (উৎকল দিবস); হযরত আলীর জন্মদিন"),
            (
                "2018-04-14",
                "ড. বি. আর. আম্বেদকর জয়ন্তী; "
                "পুত্থান্ডু (তামিল নববর্ষ); "
                "বিশু; "
                "বৈশাখী; "
                "মেশাদি (তামিল নববর্ষের দিন)",
            ),
            (
                "2018-04-15",
                "পহেলা বৈশাখ; বহাগ বিহু; বৈশাখাদি; মহা বিষুব সংক্রান্তি / পানা সংক্রান্তি; হিমাচল দিবস",
            ),
            ("2018-04-30", "বুদ্ধ পূর্ণিমা"),
            ("2018-05-01", "গুজরাট দিবস; মহারাষ্ট্র দিবস"),
            ("2018-05-09", "গুরু রবীন্দ্রনাথের জয়ন্তী; রবীন্দ্র জয়ন্তী"),
            ("2018-05-16", "সিকিম প্রতিষ্ঠা দিবস"),
            ("2018-06-02", "তেলেঙ্গানা গঠন দিবস"),
            ("2018-06-15", "জামাত-উল-ভিদা"),
            ("2018-06-16", "ঈদ-উল-ফিতর; মহারানা প্রতাপ জয়ন্তী"),
            ("2018-07-14", "রথযাত্রা"),
            ("2018-08-06", "বোনালু"),
            ("2018-08-15", "স্বাধীনতা দিবস"),
            ("2018-08-16", "পুদুচেরি আইনি হস্তান্তর দিবস"),
            ("2018-08-17", "পারসি নববর্ষ (শাহেনশাহী); পার্সি নববর্ষ"),
            ("2018-08-22", "ঈদ-উল-জুহা (বকরিদ)"),
            ("2018-08-24", "ওনাম"),
            ("2018-08-26", "রাখি বন্ধন"),
            ("2018-09-03", "জন্মাষ্টমী (বৈষ্ণব)"),
            ("2018-09-13", "গণেশ চতুর্থী / বিনায়ক চতুর্থী"),
            ("2018-09-21", "মহরম"),
            ("2018-10-02", "মহাত্মা গান্ধী জয়ন্তী"),
            ("2018-10-08", "বাথুকাম্মা উৎসব"),
            ("2018-10-16", "দশেরা (সপ্তমী)"),
            ("2018-10-17", "দশেরা (মহানবমী); দশেরা (মহাষ্টমী)"),
            ("2018-10-19", "বিজয়া দশমী"),
            ("2018-10-24", "মহার্ষি বাল্মীকি জয়ন্তী"),
            ("2018-10-27", "কারাকা চতুর্থী (কারওয়া চৌথ)"),
            ("2018-10-31", "সরদার বল্লভভাই প্যাটেল জয়ন্তী"),
            (
                "2018-11-01",
                "অন্ধ্রপ্রদেশ প্রতিষ্ঠা দিবস; "
                "কর্ণাটক রাজ্যোৎসব; "
                "কেরালা প্রতিষ্ঠা দিবস; "
                "ছত্তিশগড় প্রতিষ্ঠা দিবস; "
                "নতুন পাঞ্জাব দিবস; "
                "পুদুচেরি মুক্তি দিবস; "
                "মধ্যপ্রদেশ প্রতিষ্ঠা দিবস; "
                "হরিয়ানা প্রতিষ্ঠা দিবস",
            ),
            ("2018-11-06", "দীপাবলি (দক্ষিণ ভারত); নরক চতুর্দশী"),
            ("2018-11-07", "দীপাবলি"),
            ("2018-11-08", "গোবর্ধন পূজা"),
            ("2018-11-09", "ভাই দুজ"),
            ("2018-11-13", "ছঠ পূজা; প্রতিহার ষষ্ঠী বা সূর্য ষষ্ঠী (ছট পূজা)"),
            ("2018-11-15", "ঝাড়খণ্ড গঠন দিবস"),
            ("2018-11-21", "মিলাদ-উন-নবী"),
            ("2018-11-23", "গুরু নানক জয়ন্তী"),
            ("2018-11-24", "গুরু তেগ বাহাদুরের শাহাদত দিবস"),
            ("2018-12-01", "নাগাল্যান্ড প্রতিষ্ঠা দিবস"),
            ("2018-12-02", "অসম দিবস"),
            ("2018-12-19", "গোয়া মুক্তি দিবস"),
            ("2018-12-24", "বড়দিনের আগের দিন"),
            ("2018-12-25", "বড়দিন"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-01-13", "Lohri"),
            ("2018-01-14", "Magh Bihu; Makar Sankranti; Pongal; Uttarayan"),
            ("2018-01-15", "Thiruvalluvar Day / Mattu Pongal"),
            ("2018-01-16", "Uzhavar Thirunal"),
            ("2018-01-22", "Basant Panchami / Shri Panchami"),
            ("2018-01-24", "UP Formation Day"),
            ("2018-01-26", "Republic Day"),
            ("2018-01-31", "Guru Ravi Das's Birthday"),
            ("2018-02-10", "Swami Dayanand Saraswati's Birthday"),
            ("2018-02-13", "Maha Shivaratri"),
            ("2018-02-19", "Chhatrapati Shivaji Maharaj Jayanti; Shivaji's Birthday"),
            ("2018-02-20", "Mizoram State Day"),
            ("2018-03-01", "Dolyatra; Holika Dahan"),
            ("2018-03-02", "Holi"),
            ("2018-03-18", "Chaitra Sukladi; Cheti Chand; Gudi Padwa; Ugadi"),
            ("2018-03-22", "Bihar Day"),
            ("2018-03-25", "Ram Navami"),
            ("2018-03-29", "Mahavira's Birthday"),
            ("2018-03-30", "Good Friday; Rajasthan Day"),
            ("2018-04-01", "Ali's Birthday; Easter Sunday; Odisha Day (Utkala Dibasa)"),
            (
                "2018-04-14",
                "Dr. B. R. Ambedkar's Birthday; "
                "Meshadi (Tamil New Year's Day); "
                "Puthandu (Tamil New Year); "
                "Vaisakhi; "
                "Vishu",
            ),
            (
                "2018-04-15",
                "Bahag Bihu; "
                "Himachal Day; "
                "Maha Vishuva Sankranti / Pana Sankranti; "
                "Pohela Boishakh; "
                "Vaisakhadi",
            ),
            ("2018-04-30", "Buddha Purnima"),
            ("2018-05-01", "Gujarat Day; Maharashtra Day"),
            ("2018-05-09", "Guru Rabindranath's Birthday; Rabindra Jayanti"),
            ("2018-05-16", "Sikkim State Day"),
            ("2018-06-02", "Telangana Formation Day"),
            ("2018-06-15", "Jumu'atul-Wida"),
            ("2018-06-16", "Eid al-Fitr; Maharana Pratap Jayanti"),
            ("2018-07-14", "Rath Yatra"),
            ("2018-08-06", "Bonalu"),
            ("2018-08-15", "Independence Day"),
            ("2018-08-16", "Puducherry De Jure Transfer Day"),
            ("2018-08-17", "Parsi New Year; Parsi New Year (Shahenshahi)"),
            ("2018-08-22", "Eid al-Adha"),
            ("2018-08-24", "Onam"),
            ("2018-08-26", "Raksha Bandhan"),
            ("2018-09-03", "Janmashtami (Vaishnava)"),
            ("2018-09-13", "Ganesh Chaturthi / Vinayak Chaturthi"),
            ("2018-09-21", "Ashura"),
            ("2018-10-02", "Mahatma Gandhi's Birthday"),
            ("2018-10-08", "Bathukamma Festival"),
            ("2018-10-16", "Dussehra (Saptami)"),
            ("2018-10-17", "Dussehra (Mahanavami); Dussehra (Mahashtami)"),
            ("2018-10-19", "Dussehra"),
            ("2018-10-24", "Maharishi Valmiki's Birthday"),
            ("2018-10-27", "Karaka Chaturthi (Karwa Chouth)"),
            ("2018-10-31", "Sardar Vallabhbhai Patel Jayanti"),
            (
                "2018-11-01",
                "Andhra Pradesh Foundation Day; "
                "Chhattisgarh Foundation Day; "
                "Haryana Foundation Day; "
                "Karnataka Rajyotsava; "
                "Kerala Foundation Day; "
                "Madhya Pradesh Foundation Day; "
                "New Punjab Day; "
                "Puducherry Liberation Day",
            ),
            ("2018-11-06", "Diwali (South India); Naraka Chaturdashi"),
            ("2018-11-07", "Diwali (Deepavali)"),
            ("2018-11-08", "Govardhan Puja"),
            ("2018-11-09", "Bhai Duj"),
            ("2018-11-13", "Chhath Puja; Pratihar Shashthi or Surya Shashthi (Chhat Puja)"),
            ("2018-11-15", "Jharkhand Formation Day"),
            ("2018-11-21", "Prophet's Birthday"),
            ("2018-11-23", "Guru Nanak's Birthday"),
            ("2018-11-24", "Guru Tegh Bahadur's Martyrdom Day"),
            ("2018-12-01", "Nagaland State Inauguration Day"),
            ("2018-12-02", "Assam Day"),
            ("2018-12-19", "Goa Liberation Day"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas"),
        )

    def test_l10n_gu(self):
        self.assertLocalizedHolidays(
            "gu",
            ("2018-01-01", "નવા વર્ષનો દિવસ"),
            ("2018-01-13", "લોહરી"),
            ("2018-01-14", "ઉત્તરાયણ; પોંગલ; મકરસંક્રાંતિ; માઘ બિહુ"),
            ("2018-01-15", "તિરુવલ્લુવર દિવસ / મટ્ટુ પોંગલ"),
            ("2018-01-16", "ઉઝાવર થિરુનલ"),
            ("2018-01-22", "વસંત પંચમી / શ્રી પંચમી"),
            ("2018-01-24", "યુપી સ્થાપના દિવસ"),
            ("2018-01-26", "પ્રજાસત્તાક દિવસ"),
            ("2018-01-31", "ગુરુ રવિદાસનો જન્મદિવસ"),
            ("2018-02-10", "સ્વામી દયાનંદ સરસ્વતી જયંતિ"),
            ("2018-02-13", "મહાશિવરાત્રી"),
            ("2018-02-19", "છત્રપતિ શિવાજી મહારાજ જયંતિ; શિવાજીની જયંતિ"),
            ("2018-02-20", "મિઝોરમ રાજ્ય દિવસ"),
            ("2018-03-01", "Dolyatra; હોલિકા દહન"),
            ("2018-03-02", "હોળી"),
            ("2018-03-18", "ઉગાડી; ગુડી પડવો; ચેતી ચંદ; ચૈત્ર શુક્લાડી"),
            ("2018-03-22", "બિહાર દિવસ"),
            ("2018-03-25", "રામ નવમી"),
            ("2018-03-29", "મહાવીર જયંતિ"),
            ("2018-03-30", "ગુડ ફ્રાઈડે; રાજસ્થાન દિવસ"),
            ("2018-04-01", "ઈસ્ટર સન્ડે; ઓડિશા દિવસ (ઉત્કલ દિવસ); હઝરત અલીનો જન્મદિવસ"),
            (
                "2018-04-14",
                "ડૉ. બી. આર. આંબેડકર જયંતિ; "
                "પુથંડુ (તમિલ નવું વર્ષ); "
                "મેશાદી (તમિલ નવા વર્ષનો દિવસ); "
                "વિશુ; "
                "વૈશાખી",
            ),
            (
                "2018-04-15",
                "પોહેલા બોઈશાખ; બહાગ બિહુ; મહા વિષુવ સંક્રાંતિ / પાના સંક્રાંતિ; વૈશાખડી; હિમાચલ દિવસ",
            ),
            ("2018-04-30", "બુદ્ધ પૂર્ણિમા"),
            ("2018-05-01", "ગુજરાત સ્થાપના દિવસ; મહારાષ્ટ્ર દિવસ"),
            ("2018-05-09", "ગુરુ રવીન્દ્રનાથ જયંતિ; રવીન્દ્ર જયંતિ"),
            ("2018-05-16", "સિક્કિમ રાજ્ય દિવસ"),
            ("2018-06-02", "તેલંગાણા સ્થાપના દિવસ"),
            ("2018-06-15", "જમાત-ઉલ-વિદા"),
            ("2018-06-16", "ઈદ-ઉલ-ફિત્ર; મહારાણા પ્રતાપ જયંતિ"),
            ("2018-07-14", "રથ યાત્રા"),
            ("2018-08-06", "બોનાલુ"),
            ("2018-08-15", "સ્વતંત્રતા દિવસ"),
            ("2018-08-16", "પુડુચેરી ડી જ્યુર ટ્રાન્સફર દિવસ"),
            ("2018-08-17", "પારસી નવું વર્ષ; પારસી નવું વર્ષ (શાહેનશાહી)"),
            ("2018-08-22", "ઈદ-ઉલ-ઝુહા (બકરી ઈદ)"),
            ("2018-08-24", "ઓણમ"),
            ("2018-08-26", "રક્ષાબંધન"),
            ("2018-09-03", "જન્માષ્ટમી (વૈષ્ણવ)"),
            ("2018-09-13", "ગણેશ ચતુર્થી / વિનાયક ચતુર્થી"),
            ("2018-09-21", "મોહરમ"),
            ("2018-10-02", "મહાત્મા ગાંધી જયંતિ"),
            ("2018-10-08", "બથુકમ્મા ઉત્સવ"),
            ("2018-10-16", "દશેરા (સપ્તમી)"),
            ("2018-10-17", "દશેરા (મહાનવમી); દશેરા (મહાષ્ટમી)"),
            ("2018-10-19", "દશેરા"),
            ("2018-10-24", "મહર્ષિ વાલ્મિકી જયંતિ"),
            ("2018-10-27", "કરકા ચતુર્થી (કરવા ચોથ)"),
            ("2018-10-31", "સરદાર વલ્લભભાઈ પટેલ જયંતિ"),
            (
                "2018-11-01",
                "આંધ્ર પ્રદેશ સ્થાપના દિવસ; "
                "કર્ણાટક રાજ્યોત્સવ; "
                "કેરળ સ્થાપના દિવસ; "
                "છત્તીસગઢ સ્થાપના દિવસ; "
                "નવો પંજાબ દિવસ; "
                "પુડુચેરી મુક્તિ દિવસ; "
                "મધ્ય પ્રદેશ સ્થાપના દિવસ; "
                "હરિયાણા સ્થાપના દિવસ",
            ),
            ("2018-11-06", "દીપાવલી (દક્ષિણ ભારત); નરક ચતુર્દશી"),
            ("2018-11-07", "દિવાળી (દીપાવલી)"),
            ("2018-11-08", "ગોવર્ધન પૂજા"),
            ("2018-11-09", "ભાઈ દૂજ"),
            ("2018-11-13", "છઠ પૂજા; પ્રતિહાર ષષ્ઠી અથવા સૂર્ય ષષ્ઠી (છટ પૂજા)"),
            ("2018-11-15", "ઝારખંડ સ્થાપના દિવસ"),
            ("2018-11-21", "મિલાદ-ઉન-નબી"),
            ("2018-11-23", "ગુરુ નાનક જયંતિ"),
            ("2018-11-24", "ગુરુ તેગ બહાદુરનો શહીદ દિવસ"),
            ("2018-12-01", "નાગાલેન્ડ રાજ્ય ઉદ્ઘાટન દિવસ"),
            ("2018-12-02", "આસામ દિવસ"),
            ("2018-12-19", "ગોવા મુક્તિ દિવસ"),
            ("2018-12-24", "નાતાલની પૂર્વસંધ્યાએ"),
            ("2018-12-25", "નાતાલ"),
        )

    def test_l10n_hi(self):
        self.assertLocalizedHolidays(
            "hi",
            ("2018-01-01", "नए साल का दिन"),
            ("2018-01-13", "लोहड़ी"),
            ("2018-01-14", "उत्तरायण; पोंगल; मकर संक्रांति; माघ बिहू"),
            ("2018-01-15", "तिरुवल्लुवर दिवस / मट्टू पोंगल"),
            ("2018-01-16", "उझावर थिरुनल"),
            ("2018-01-22", "बसंत पंचमी / श्री पंचमी"),
            ("2018-01-24", "यूपी स्थापना दिवस"),
            ("2018-01-26", "गणतंत्र दिवस"),
            ("2018-01-31", "गुरु रवि दास का जन्मदिन"),
            ("2018-02-10", "स्वामी दयानंद सरस्वती जयंती"),
            ("2018-02-13", "महाशिवरात्रि"),
            ("2018-02-19", "छत्रपति शिवाजी महाराज जयंती; शिवाजी जयंती"),
            ("2018-02-20", "मिज़ोरम राज्य दिवस"),
            ("2018-03-01", "दोलयात्रा; होलिका दहन"),
            ("2018-03-02", "होली"),
            ("2018-03-18", "उगादि; गुडी पाडवा; चेटी चंड; चैत्र शुक्लादि"),
            ("2018-03-22", "बिहार दिवस"),
            ("2018-03-25", "रामनवमी"),
            ("2018-03-29", "महावीर जयंती"),
            ("2018-03-30", "गुड फ्राइडे; राजस्थान दिवस"),
            ("2018-04-01", "ईस्टर रविवार; ओडिशा दिवस (उत्कल दिवस); हज़रत अली का जन्मदिन"),
            (
                "2018-04-14",
                "डॉ. बी.आर. आम्बेडकर जयंती; "
                "पुत्ताण्डु (तमिल नव वर्ष); "
                "मेषदी (तमिल नव वर्ष दिवस); "
                "विशु; "
                "वैसाखी",
            ),
            (
                "2018-04-15",
                "पोहेला बोइशाख; बहाग बिहु; महा विषुव संक्रांति / पण संक्रांति; वैसाखडी; हिमाचल दिवस",
            ),
            ("2018-04-30", "बुद्ध पूर्णिमा"),
            ("2018-05-01", "गुजरात दिवस; महाराष्ट्र दिवस"),
            ("2018-05-09", "गुरु रवींद्रनाथ जयंती; रवींद्र जयंती"),
            ("2018-05-16", "सिक्किम राज्य दिवस"),
            ("2018-06-02", "तेलंगाना स्थापना दिवस"),
            ("2018-06-15", "जमात-उल-विदा"),
            ("2018-06-16", "ईद-उल-फितर; महाराणा प्रताप जयंती"),
            ("2018-07-14", "रथ यात्रा"),
            ("2018-08-06", "बोनालु"),
            ("2018-08-15", "स्वतंत्रता दिवस"),
            ("2018-08-16", "पुडुचेरी डी ज्यूर स्थानांतरण दिवस"),
            ("2018-08-17", "पारसी नव वर्ष; पारसी नव वर्ष (शहंशाही)"),
            ("2018-08-22", "ईद-उल-ज़ुहा (बकरीद)"),
            ("2018-08-24", "ओणम"),
            ("2018-08-26", "रक्षाबंधन"),
            ("2018-09-03", "जन्माष्टमी (वैष्णव)"),
            ("2018-09-13", "गणेश चतुर्थी / विनायक चतुर्थी"),
            ("2018-09-21", "मुहर्रम"),
            ("2018-10-02", "महात्मा गांधी जयंती"),
            ("2018-10-08", "बतुकम्मा महोत्सव"),
            ("2018-10-16", "दशहरा (सप्तमी)"),
            ("2018-10-17", "दशहरा (महानवमी); दशहरा (महाष्टमी)"),
            ("2018-10-19", "दशहरा"),
            ("2018-10-24", "महर्षि वाल्मीकि जयंती"),
            ("2018-10-27", "कराका चतुर्थी (करवा चौथ)"),
            ("2018-10-31", "सरदार वल्लभभाई पटेल जयंती"),
            (
                "2018-11-01",
                "आंध्र प्रदेश स्थापना दिवस; "
                "कर्नाटक राज्योत्सव; "
                "केरल स्थापना दिवस; "
                "छत्तीसगढ़ स्थापना दिवस; "
                "नया पंजाब दिवस; "
                "पुडुचेरी मुक्ति दिवस; "
                "मध्य प्रदेश स्थापना दिवस; "
                "हरियाणा स्थापना दिवस",
            ),
            ("2018-11-06", "दीपावली (दक्षिण भारत); नरक चतुर्दशी"),
            ("2018-11-07", "दिवाली (दीपावली)"),
            ("2018-11-08", "गोवर्धन पूजा"),
            ("2018-11-09", "भाई दूज"),
            ("2018-11-13", "छठ पूजा; प्रतिहार षष्ठी या सूर्य षष्ठी (छठ पूजा)"),
            ("2018-11-15", "झारखंड स्थापना दिवस"),
            ("2018-11-21", "मिलाद-उन-नबी"),
            ("2018-11-23", "गुरु नानक जयंती"),
            ("2018-11-24", "गुरु तेग बहादुर का शहीदी दिवस"),
            ("2018-12-01", "नागालैंड राज्य उद्घाटन दिवस"),
            ("2018-12-02", "असम दिवस"),
            ("2018-12-19", "गोवा मुक्ति दिवस"),
            ("2018-12-24", "क्रिसमस की पूर्व संध्या"),
            ("2018-12-25", "क्रिसमस"),
        )

    def test_l10n_kn(self):
        self.assertLocalizedHolidays(
            "kn",
            ("2018-01-01", "ಹೊಸ ವರ್ಷದ ದಿನ"),
            ("2018-01-13", "ಲೋಹ್ರಿ"),
            ("2018-01-14", "ಉತ್ತರಾಯಣ; ಪೊಂಗಲ್; ಮಕರ ಸಂಕ್ರಾಂತಿ; ಮಾಘ್ ಬಿಹು"),
            ("2018-01-15", "ತಿರುವಳ್ಳುವರ್ ದಿನೋತ್ಸವ / ಮಟ್ಟು ಪೊಂಗಲ್"),
            ("2018-01-16", "ಉಳವರ್ ತಿರುನಾಲ್"),
            ("2018-01-22", "ವಸಂತ ಪಂಚಮಿ / ಶ್ರೀ ಪಂಚಮಿ"),
            ("2018-01-24", "ಉತ್ತರ ಪ್ರದೇಶ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-01-26", "ಗಣರಾಜ್ಯೋತ್ಸವ"),
            ("2018-01-31", "ಗುರು ರವಿದಾಸರ ಜನ್ಮದಿನ"),
            ("2018-02-10", "ಸ್ವಾಮಿ ದಯಾನಂದ ಸರಸ್ವತಿ ಜಯಂತಿ"),
            ("2018-02-13", "ಮಹಾ ಶಿವರಾತ್ರಿ"),
            ("2018-02-19", "ಛತ್ರಪತಿ ಶಿವಾಜಿ ಮಹಾರಾಜ್ ಜಯಂತಿ; ಶಿವಾಜಿ ಜಯಂತಿ"),
            ("2018-02-20", "ಮಿಜೋರಾಂ ರಾಜ್ಯ ದಿನೋತ್ಸವ"),
            ("2018-03-01", "ದೋಲಯಾತ್ರೆ; ಹೋಲಿಕಾ ದಹನ್"),
            ("2018-03-02", "ಹೋಳಿ ಹಬ್ಬ"),
            ("2018-03-18", "ಗುಡಿ ಪಾಡ್ವ; ಚೇಟಿ ಚಂದ್; ಚೈತ್ರ ಸುಕ್ಲಾಡಿ; ಯುಗಾದಿ ಹಬ್ಬ"),
            ("2018-03-22", "ಬಿಹಾರ್ ದಿನೋತ್ಸವ"),
            ("2018-03-25", "ಶ್ರೀ ರಾಮನವಮಿ"),
            ("2018-03-29", "ಮಹಾವೀರ ಜಯಂತಿ"),
            ("2018-03-30", "ಗುಡ್ ಫ್ರೈಡೆ; ರಾಜಸ್ಥಾನ ದಿನೋತ್ಸವ"),
            ("2018-04-01", "ಈಸ್ಟರ್ ಭಾನುವಾರ; ಒಡಿಶಾ ದಿನೋತ್ಸವ (ಉತ್ಕಲ ದಿವಸ); ಹಜರತ್ ಅಲಿಯವರ ಜನ್ಮದಿನ"),
            (
                "2018-04-14",
                "ಡಾ ಬಿ.ಆರ್.ಅಂಬೇಡ್ಕರ್ ಜಯಂತಿ; ಪುತ್ತಾಂಡು (ತಮಿಳು ಹೊಸ ವರ್ಷ); ಮೇಷಾದಿ (ತಮಿಳು ಹೊಸ ವರ್ಷದ ದಿನ); ವಿಷು; ವೈಶಾಖಿ",
            ),
            (
                "2018-04-15",
                "ಪೊಹೆಲಾ ಬೊಯಿಶಾಖ್; ಭಾಗ ಬಿಹು; ಮಹಾ ವಿಷುವ ಸಂಕ್ರಾಂತಿ / ಪನ ಸಂಕ್ರಾಂತಿ; ವೈಶಾಖಾದಿ; ಹಿಮಾಚಲ್ ದಿನೋತ್ಸವ",
            ),
            ("2018-04-30", "ಬುದ್ಧ ಪೂರ್ಣಿಮ"),
            ("2018-05-01", "ಗುಜರಾತ್ ದಿನೋತ್ಸವ; ಮಹಾರಾಷ್ಟ್ರ ದಿನೋತ್ಸವ"),
            ("2018-05-09", "ಗುರು ರವೀಂದ್ರನಾಥ್ ಜಯಂತಿ; ರವೀಂದ್ರ ಜಯಂತಿ"),
            ("2018-05-16", "ಸಿಕ್ಕಿಂ ರಾಜ್ಯ ದಿನೋತ್ಸವ"),
            ("2018-06-02", "ತೆಲಂಗಾಣ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-06-15", "ಜಮಾತ್-ಉಲ್-ವಿದಾ"),
            ("2018-06-16", "ಈದ್-ಉಲ್-ಫಿತರ್; ಮಹಾರಾಣಾ ಪ್ರತಾಪ್ ಜಯಂತಿ"),
            ("2018-07-14", "ರಥ ಯಾತ್ರೆ"),
            ("2018-08-06", "ಬೋನಾಲು"),
            ("2018-08-15", "ಸ್ವಾತಂತ್ರ್ಯ ದಿನಾಚರಣೆ"),
            ("2018-08-16", "ಪುದುಚ್ಚೇರಿ ಕಾನೂನು ಹಸ್ತಾಂತರ ದಿನೋತ್ಸವ"),
            ("2018-08-17", "ಪಾರ್ಸಿ ಹೊಸ ವರ್ಷ; ಪಾರ್ಸಿ ಹೊಸ ವರ್ಷ (ಶಹನ್ಶಾಹಿ)"),
            ("2018-08-22", "ಈದ್-ಉಲ್-ಜುಹಾ (ಬಕ್ರೀದ್)"),
            ("2018-08-24", "ಓಣಂ"),
            ("2018-08-26", "ರಕ್ಷಾ ಬಂಧನ"),
            ("2018-09-03", "ಜನ್ಮಾಷ್ಟಮಿ (ವೈಷ್ಣವ)"),
            ("2018-09-13", "ಗಣೇಶ ಚತುರ್ಥಿ / ವಿನಾಯಕ ಚತುರ್ಥಿ"),
            ("2018-09-21", "ಮೊಹರಂ ಕಡೆ ದಿನ"),
            ("2018-10-02", "ಮಹಾತ್ಮ ಗಾಂಧಿ ಜಯಂತಿ"),
            ("2018-10-08", "ಬತುಕಮ್ಮ ಹಬ್ಬ"),
            ("2018-10-16", "ದಸರಾ (ಸಪ್ತಮಿ)"),
            ("2018-10-17", "ದಸರಾ (ಮಹಾನವಮಿ); ದಸರಾ (ಮಹಾಷ್ಟಮಿ)"),
            ("2018-10-19", "ವಿಜಯದಶಮಿ"),
            ("2018-10-24", "ಮಹರ್ಷಿ ವಾಲ್ಮೀಕಿ ಜಯಂತಿ"),
            ("2018-10-27", "ಕರಕ ಚತುರ್ಥಿ (ಕರ್ವಾ ಚೌತ್)"),
            ("2018-10-31", "ಸರ್ದಾರ್ ವಲ್ಲಭಭಾಯಿ ಪಟೇಲ್ ಜಯಂತಿ"),
            (
                "2018-11-01",
                "ಆಂಧ್ರ ಪ್ರದೇಶ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ; "
                "ಕೇರಳ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಛತ್ತೀಸ್‌ಗಢ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಪುದುಚ್ಚೇರಿ ವಿಮೋಚನ ದಿನೋತ್ಸವ; "
                "ಮಧ್ಯ ಪ್ರದೇಶ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಹರ್ಯಾಣ ಸ್ಥಾಪನಾ ದಿನ; "
                "ಹೊಸ ಪಂಜಾಬ್ ದಿನೋತ್ಸವ",
            ),
            ("2018-11-06", "ದೀಪಾವಳಿ (ದಕ್ಷಿಣ ಭಾರತ); ನರಕ ಚತುರ್ದಶಿ"),
            ("2018-11-07", "ದೀಪಾವಳಿ"),
            ("2018-11-08", "ಗೋವರ್ಧನ ಪೂಜೆ"),
            ("2018-11-09", "ಭಾಯಿ ದೂಜ್"),
            ("2018-11-13", "ಛಠ್ ಪೂಜೆ; ಪ್ರತಿಹಾರ್ ಷಷ್ಠಿ ಅಥವಾ ಸೂರ್ಯ ಷಷ್ಠಿ (ಛತ್ ಪೂಜೆ)"),
            ("2018-11-15", "ಜಾರ್ಖಂಡ್ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-11-21", "ಈದ್-ಮಿಲಾದ್"),
            ("2018-11-23", "ಗುರು ನಾನಕ್ ಜಯಂತಿ"),
            ("2018-11-24", "ಗುರು ತೇಜ್ ಬಹದ್ದೂರ್ ಅವರ ಹುತಾತ್ಮ ದಿನ"),
            ("2018-12-01", "ನಾಗಾಲ್ಯಾಂಡ್ ರಾಜ್ಯ ಸ್ಥಾಪನಾ ದಿನ"),
            ("2018-12-02", "ಅಸ್ಸಾಂ ದಿನೋತ್ಸವ"),
            ("2018-12-19", "ಗೋವಾ ವಿಮೋಚನ ದಿನೋತ್ಸವ"),
            ("2018-12-24", "ಕ್ರಿಸ್ಮಸ್ ಈವ್"),
            ("2018-12-25", "ಕ್ರಿಸ್‌ಮಸ್"),
        )

    def test_l10n_ml(self):
        self.assertLocalizedHolidays(
            "ml",
            ("2018-01-01", "പുതുവത്സര ദിനം"),
            ("2018-01-13", "ലോഹരി"),
            ("2018-01-14", "ഉത്തരായൻ; പൊങ്കൽ; മകര സംക്രാന്തി; മാഘ് ബിഹു"),
            ("2018-01-15", "തിരുവള്ളുവർ ദിനം / മട്ടു പൊങ്കൽ"),
            ("2018-01-16", "ഉഴവർ തിരുനാൾ"),
            ("2018-01-22", "വസന്ത പഞ്ചമി / ശ്രീ പഞ്ചമി"),
            ("2018-01-24", "ഉത്തർപ്രദേശ് രൂപീകരണദിനം"),
            ("2018-01-26", "റിപ്പബ്ലിക് ദിനം"),
            ("2018-01-31", "ഗുരു രവി ദാസിന്റെ ജന്മദിനം"),
            ("2018-02-10", "സ്വാമി ദയാനന്ദ സരസ്വതി ജയന്തി"),
            ("2018-02-13", "മഹാ ശിവരാത്രി"),
            ("2018-02-19", "ചത്രപതി ശിവാജി മഹാരാജ ജയന്തി; ശിവാജി ജയന്തി"),
            ("2018-02-20", "മിസോരം സംസ്ഥാനദിനം"),
            ("2018-03-01", "ദോലയാത്ര; ഹോളിക ദഹൻ"),
            ("2018-03-02", "ഹോളി"),
            ("2018-03-18", "ഉഗാദി; ഗുഡി പദ്വ; ചേതി ചന്ദ്; ചൈത്ര ശുക്ലദി"),
            ("2018-03-22", "ബിഹാർ ദിനം"),
            ("2018-03-25", "രാമ നവമി"),
            ("2018-03-29", "മഹാവീർ ജയന്തി"),
            ("2018-03-30", "ദുഃഖവെള്ളി; രാജസ്ഥാൻ ദിനം"),
            ("2018-04-01", "ഈസ്റ്റർ; ഉത്കൽ ദിവസ്; ഹസ്രത്ത് അലിയുടെ ജന്മദിനം"),
            (
                "2018-04-14",
                "ഡോ. ബി. ആർ. അംബേദ്കർ ജയന്തി; "
                "പുത്താണ്ട് (തമിഴ് പുതുവർഷം); "
                "മേഷാദി (തമിഴ് പുതുവത്സര ദിനം); "
                "വിഷു; "
                "വൈശാഖി",
            ),
            (
                "2018-04-15",
                "പൊഹേലാ ബൈശാഖ്; ഭാഗം ബിഹു; മഹാ വിഷുവ സംക്രാന്തി / പനാ സംക്രാന്തി; വൈശാഖാദി; ഹിമാചൽ ദിനം",
            ),
            ("2018-04-30", "ബുദ്ധ പൂർണ്ണിമ"),
            ("2018-05-01", "ഗുജറാത്ത് ദിനം; മഹാരാഷ്ട്ര ദിനം"),
            ("2018-05-09", "ഗുരു രവീന്ദ്രനാഥ് ജയന്തി; രബീന്ദ്ര ജയന്തി"),
            ("2018-05-16", "സിക്കിം സംസ്ഥാനദിനം"),
            ("2018-06-02", "തെലങ്കാന രൂപീകരണദിനം"),
            ("2018-06-15", "ജമാഅത്ത്-ഉൽ-വിദ"),
            ("2018-06-16", "ഈദ്-ഉൽ-ഫിത്തർ; മഹാരാണ പ്രതാപ് ജയന്തി"),
            ("2018-07-14", "രഥയാത്ര"),
            ("2018-08-06", "ബോനാലു"),
            ("2018-08-15", "സ്വാതന്ത്ര്യദിനം"),
            ("2018-08-16", "പുതുച്ചേരി നിയമപരമായ കൈമാറ്റദിനം"),
            ("2018-08-17", "പാർസി പുതുവർഷം; പാർസി പുതുവർഷം (ഷഹൻഷാഹി)"),
            ("2018-08-22", "ഈദുൽ സുഹ (ബക്രീദ്)"),
            ("2018-08-24", "ഓണം"),
            ("2018-08-26", "രക്ഷാ ബന്ധൻ"),
            ("2018-09-03", "ജന്മാഷ്ടമി (വൈഷ്ണവ)"),
            ("2018-09-13", "ഗണേശ ചതുർത്ഥി / വിനായക ചതുർത്ഥി"),
            ("2018-09-21", "മുഹറം"),
            ("2018-10-02", "മഹാത്മാ ഗാന്ധി ജയന്തി"),
            ("2018-10-08", "ബത്തുകമ്മ ഉത്സവം"),
            ("2018-10-16", "ദസറ (സപ്തമി)"),
            ("2018-10-17", "ദസറ (മഹാനവമി); ദസറ (മഹാഷ്ടമി)"),
            ("2018-10-19", "ദശര"),
            ("2018-10-24", "മഹർഷി വാൽമീകി ജയന്തി"),
            ("2018-10-27", "കാരക ചതുർത്ഥി (കർവാ ചൗത്ത്)"),
            ("2018-10-31", "സർദാർ വല്ലഭായി പട്ടേൽ ജയന്തി"),
            (
                "2018-11-01",
                "ആന്ധ്രാപ്രദേശ് സ്ഥാപനദിനം; "
                "കേരളപ്പിറവി; "
                "കർണാടക രാജ്യോത്സവം; "
                "ഛത്തീസ്ഗഢ് സ്ഥാപനദിനം; "
                "പുതിയ പഞ്ചാബ് ദിനം; "
                "പുതുച്ചേരി മോചനദിനം; "
                "മധ്യപ്രദേശ് സ്ഥാപനദിനം; "
                "ഹരിയാന സ്ഥാപനദിനം",
            ),
            ("2018-11-06", "ദീപാവലി (ദക്ഷിണേന്ത്യ); നരക ചതുർദസി"),
            ("2018-11-07", "ദീപാവലി"),
            ("2018-11-08", "ഗോവർധന പൂജ"),
            ("2018-11-09", "ഭായ് ദൂജ്"),
            ("2018-11-13", "ഛഠ് പൂജ; പ്രതിഹാർ ഷഷ്ഠി അല്ലെങ്കിൽ സൂര്യ ഷഷ്ഠി (ഛത് പൂജ)"),
            ("2018-11-15", "ഝാർഖണ്ഡ് രൂപീകരണദിനം"),
            ("2018-11-21", "മിലാദ്-ഉന്നബി"),
            ("2018-11-23", "ഗുരു നാനക് ജയന്തി"),
            ("2018-11-24", "ഗുരു തേജ് ബഹാദൂറിൻ്റെ രക്തസാക്ഷിത്വ ദിനം"),
            ("2018-12-01", "നാഗാലാൻഡ് സംസ്ഥാനാരംഭദിനം"),
            ("2018-12-02", "അസം ദിനം"),
            ("2018-12-19", "ഗോവ മോചനദിനം"),
            ("2018-12-24", "ക്രിസ്മസ് തലേന്ന്"),
            ("2018-12-25", "ക്രിസ്തുമസ്"),
        )

    def test_l10n_mr(self):
        self.assertLocalizedHolidays(
            "mr",
            ("2018-01-01", "नवीन वर्षाचा दिवस"),
            ("2018-01-13", "लोहरी"),
            ("2018-01-14", "उत्तरायण; पोंगल; मकर संक्रांत; माघ बिहू"),
            ("2018-01-15", "तिरुवल्लुवर दिन / मट्टू पोंगल"),
            ("2018-01-16", "उझावर थिरुनल"),
            ("2018-01-22", "बसंत पंचमी / श्री पंचमी"),
            ("2018-01-24", "यूपी स्थापना दिन"),
            ("2018-01-26", "प्रजासत्ताक दिन"),
            ("2018-01-31", "गुरु रविदास जयंती"),
            ("2018-02-10", "स्वामी दयानंद सरस्वती जयंती"),
            ("2018-02-13", "महाशिवरात्री"),
            ("2018-02-19", "छत्रपती शिवाजी महाराज जयंती; शिवाजी जयंती"),
            ("2018-02-20", "मिझोराम राज्य दिन"),
            ("2018-03-01", "दोलयात्रा; होलिका दहन"),
            ("2018-03-02", "होळी"),
            ("2018-03-18", "उगाडी; गुढीपाडवा; चेटी चंड; चैत्र शुक्लादि"),
            ("2018-03-22", "बिहार दिन"),
            ("2018-03-25", "रामनवमी"),
            ("2018-03-29", "महावीर जन्म कल्याणक"),
            ("2018-03-30", "गुड फ्रायडे; राजस्थान दिन"),
            ("2018-04-01", "ईस्टर रविवार; ओडिशा दिन (उत्कल दिन); हजरत अली यांचा वाढदिवस"),
            (
                "2018-04-14",
                "डॉ. बाबासाहेब आंबेडकर जयंती; "
                "पुथंडू (तमिळ नववर्ष); "
                "मेशादी (तमिळ नववर्षाचा दिवस); "
                "विशू; "
                "वैशाखी",
            ),
            (
                "2018-04-15",
                "पोहेला बैशाख; बहाग बिहू; महाविश्व संक्रांती / पण संक्रांती; वैशाखाडी; हिमाचल दिन",
            ),
            ("2018-04-30", "बुध्द पौर्णिमा"),
            ("2018-05-01", "गुजरात दिन; महाराष्ट्र दिन"),
            ("2018-05-09", "गुरु रवींद्रनाथ जयंती; रवींद्र जयंती"),
            ("2018-05-16", "सिक्कीम राज्य दिन"),
            ("2018-06-02", "तेलंगणा स्थापना दिन"),
            ("2018-06-15", "जमात-उल-विदा"),
            ("2018-06-16", "महाराणा प्रताप जयंती; रमझान ईद (ईद-उल-फितर)"),
            ("2018-07-14", "रथ यात्रा"),
            ("2018-08-06", "बोनालू"),
            ("2018-08-15", "स्वातंत्र्य दिन"),
            ("2018-08-16", "पुदुचेरी कायदेशीर हस्तांतरण दिन"),
            ("2018-08-17", "पारशी नववर्ष; पारसी नवीन वर्ष (शहेनशाही)"),
            ("2018-08-22", "ईद-उल-जुहा (बकरीद)"),
            ("2018-08-24", "ओणम"),
            ("2018-08-26", "रक्षाबंधन"),
            ("2018-09-03", "गोकुळाष्टमी (वैष्णव)"),
            ("2018-09-13", "गणेश चतुर्थी / विनायक चतुर्थी"),
            ("2018-09-21", "मोहरम"),
            ("2018-10-02", "महात्मा गांधी जयंती"),
            ("2018-10-08", "बथुकम्मा उत्सव"),
            ("2018-10-16", "दसरा (सप्तमी)"),
            ("2018-10-17", "दसरा (महानवमी); दसरा (महाष्टमी)"),
            ("2018-10-19", "दसरा"),
            ("2018-10-24", "महर्षी वाल्मिकी जयंती"),
            ("2018-10-27", "करक चतुर्थी (करवा चौथ)"),
            ("2018-10-31", "सरदार वल्लभभाई पटेल जयंती"),
            (
                "2018-11-01",
                "आंध्र प्रदेश स्थापना दिन; "
                "कर्नाटक राज्योत्सव; "
                "केरळ स्थापना दिन; "
                "छत्तीसगड स्थापना दिन; "
                "नवीन पंजाब दिन; "
                "पुदुचेरी मुक्ती दिन; "
                "मध्य प्रदेश स्थापना दिन; "
                "हरियाणा स्थापना दिन",
            ),
            ("2018-11-06", "दीपावली (दक्षिण भारत); नरक चतुर्दशी"),
            ("2018-11-07", "दिवाळी (दीपवाली)"),
            ("2018-11-08", "गोवर्धन पूजा"),
            ("2018-11-09", "भाई दूज"),
            ("2018-11-13", "छठ पूजा; प्रतिहार षष्ठी किंवा सूर्य षष्ठी (छठ पूजा)"),
            ("2018-11-15", "झारखंड स्थापना दिन"),
            ("2018-11-21", "ईद-ए-मिलाद"),
            ("2018-11-23", "गुरुनानक जयंती"),
            ("2018-11-24", "गुरु तेग बहादूर यांचा हुतात्मा दिन"),
            ("2018-12-01", "नागालँड राज्य उद्घाटन दिन"),
            ("2018-12-02", "आसाम दिन"),
            ("2018-12-19", "गोवा मुक्ती दिन"),
            ("2018-12-24", "ख्रिसमसच्या पूर्व संध्याकाळ"),
            ("2018-12-25", "ख्रिसमस"),
        )

    def test_l10n_pa(self):
        self.assertLocalizedHolidays(
            "pa",
            ("2018-01-01", "ਨਵੇਂ ਸਾਲ ਦਾ ਦਿਨ"),
            ("2018-01-13", "ਲੋਹੜੀ"),
            ("2018-01-14", "ਉੱਤਰਾਯਣ; ਪੋਂਗਲ; ਮਕਰ ਸੰਕ੍ਰਾਂਤੀ; ਮਾਘ ਬਿਹੂ"),
            ("2018-01-15", "ਤਿਰੂਵੱਲੂਵਰ ਦਿਵਸ / ਮੱਟੂ ਪੋਂਗਲ"),
            ("2018-01-16", "ਉਝਾਵਰ ਥਿਰੂਨਲ"),
            ("2018-01-22", "ਬਸੰਤ ਪੰਚਮੀ / ਸ੍ਰੀ ਪੰਚਮੀ"),
            ("2018-01-24", "ਯੂਪੀ ਗਠਨ ਦਿਵਸ"),
            ("2018-01-26", "ਗਣਤੰਤਰ ਦਿਵਸ"),
            ("2018-01-31", "ਗੁਰੂ ਰਵਿਦਾਸ ਜੀ ਦਾ ਜਨਮ ਦਿਹਾੜਾ"),
            ("2018-02-10", "ਸਵਾਮੀ ਦਯਾਨੰਦ ਸਰਸਵਤੀ ਜਯੰਤੀ"),
            ("2018-02-13", "ਮਹਾ ਸ਼ਿਵਰਾਤਰੀ"),
            ("2018-02-19", "ਛਤਰਪਤੀ ਸ਼ਿਵਾਜੀ ਮਹਾਰਾਜ ਜਯੰਤੀ; ਸ਼ਿਵਾਜੀ ਜਯੰਤੀ"),
            ("2018-02-20", "ਮਿਜ਼ੋਰਮ ਰਾਜ ਦਿਵਸ"),
            ("2018-03-01", "ਦੋਲਯਾਤਰਾ; ਹੋਲਿਕਾ ਦਹਨ"),
            ("2018-03-02", "ਹੋਲੀ"),
            ("2018-03-18", "ਉਗਾਦੀ; ਗੁੜੀ ਪਦਵਾ; ਚੇਤੀ ਚੰਦ; ਚੈਤਰਾ ਸ਼ੁਕਲਦੀ"),
            ("2018-03-22", "ਬਿਹਾਰ ਦਿਵਸ"),
            ("2018-03-25", "ਰਾਮ ਨੌਮੀ"),
            ("2018-03-29", "ਮਹਾਵੀਰ ਜੈਯੰਤੀ"),
            ("2018-03-30", "ਗੁੱਡ ਫਰਾਈਡੇ; ਰਾਜਸਥਾਨ ਦਿਵਸ"),
            ("2018-04-01", "ਈਸਟਰ ਐਤਵਾਰ; ਓਡੀਸ਼ਾ ਦਿਵਸ (ਉਤਕਲ ਦਿਵਸ); ਹਜ਼ਰਤ ਅਲੀ ਦਾ ਜਨਮਦਿਨ"),
            (
                "2018-04-14",
                "ਜਨਮ ਦਿਨ ਡਾ: ਬੀ.ਆਰ. ਅੰਬੇਡਕਰ; "
                "ਪੁਥੰਡੂ (ਤਾਮਿਲ ਨਵਾਂ ਸਾਲ); "
                "ਮੇਸ਼ਾਦੀ (ਤਾਮਿਲ ਨਵੇਂ ਸਾਲ ਦਾ ਦਿਨ); "
                "ਵਿਸ਼ੂ; "
                "ਵਿਸਾਖੀ",
            ),
            (
                "2018-04-15",
                "ਪੋਹੇਲਾ ਬੋਸ਼ਾਖ; ਬਹਾਗ ਬਿਹੂ; ਮਹਾਂ ਵਿਸ਼ੁਵ ਸੰਕ੍ਰਾਂਤੀ / ਪਾਨਾ ਸੰਕ੍ਰਾਂਤੀ; ਵੈਸਾਖਦੀ; ਹਿਮਾਚਲ ਦਿਵਸ",
            ),
            ("2018-04-30", "ਬੁੱਧ ਪੂਰਨਿਮਾ"),
            ("2018-05-01", "ਗੁਜਰਾਤ ਦਿਵਸ; ਮਹਾਰਾਸ਼ਟਰ ਦਿਵਸ"),
            ("2018-05-09", "ਗੁਰੂ ਰਬਿੰਦਰਨਾਥ ਜਯੰਤੀ; ਰਬਿੰਦਰ ਜੈਅੰਤੀ"),
            ("2018-05-16", "ਸਿੱਕਮ ਰਾਜ ਦਿਵਸ"),
            ("2018-06-02", "ਤੇਲੰਗਾਨਾ ਗਠਨ ਦਿਵਸ"),
            ("2018-06-15", "ਜਮਾਤ-ਉਲ-ਵਿਦਾ"),
            ("2018-06-16", "ਈਦ-ਉੱਲ-ਫਿਤਰ; ਮਹਾਰਾਣਾ ਪ੍ਰਤਾਪ ਜਯੰਤੀ"),
            ("2018-07-14", "ਰੱਥ ਯਾਤਰਾ"),
            ("2018-08-06", "ਬੋਨਾਲੂ"),
            ("2018-08-15", "ਸੁਤੰਤਰਤਾ ਦਿਵਸ"),
            ("2018-08-16", "ਪੁਡੂਚੇਰੀ ਡੀ ਜਿਊਰ ਟ੍ਰਾਂਸਫਰ ਦਿਵਸ"),
            ("2018-08-17", "ਪਾਰਸੀ ਨਵਾਂ ਸਾਲ; ਪਾਰਸੀ ਨਵਾਂ ਸਾਲ (ਸ਼ਾਹਨਸ਼ਾਹੀ)"),
            ("2018-08-22", "ਈਦ-ਉਲ-ਜ਼ੁਹਾ (ਬਕਰੀਦ)"),
            ("2018-08-24", "ਓਨਮ"),
            ("2018-08-26", "ਰੱਖੜੀ"),
            ("2018-09-03", "ਜਨਮਾਸ਼ਟਮੀ (ਵੈਸ਼ਨਵ)"),
            ("2018-09-13", "ਗਣੇਸ਼ ਚਤੁਰਥੀ / ਵਿਨਾਇਕ ਚਤੁਰਥੀ"),
            ("2018-09-21", "ਮੁਹੱਰਮ"),
            ("2018-10-02", "ਜਨਮ ਦਿਵਸ ਮਹਾਤਮਾ ਗਾਂਧੀ ਜੀ"),
            ("2018-10-08", "ਬਾਥੁਕੰਮਾ ਤਿਉਹਾਰ"),
            ("2018-10-16", "ਦੁਸਹਿਰਾ (ਸਪਤਮੀ)"),
            ("2018-10-17", "ਦੁਸਹਿਰਾ (ਮਹਾਅਸ਼ਟਮੀ); ਦੁਸਹਿਰਾ (ਮਹਾਨਵਮੀ)"),
            ("2018-10-19", "ਦੁਸਹਿਰਾ"),
            ("2018-10-24", "ਮਹਾਰਿਸ਼ੀ ਵਾਲਮੀਕੀ ਜਯੰਤੀ"),
            ("2018-10-27", "ਕਰਕ ਚਤੁਰਥੀ (ਕਰਵਾ ਚੌਥ)"),
            ("2018-10-31", "ਸਰਦਾਰ ਵੱਲਭ ਭਾਈ ਪਟੇਲ ਜਯੰਤੀ"),
            (
                "2018-11-01",
                "ਆਂਧਰਾ ਪ੍ਰਦੇਸ਼ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਕਰਨਾਟਕ ਰਾਜਯੋਤਸਵ; "
                "ਕੇਰਲ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਛੱਤੀਸਗੜ੍ਹ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਨਵਾਂ ਪੰਜਾਬ ਦਿਵਸ; "
                "ਪੁਡੂਚੇਰੀ ਮੁਕਤੀ ਦਿਵਸ; "
                "ਮੱਧ ਪ੍ਰਦੇਸ਼ ਸਥਾਪਨਾ ਦਿਵਸ; "
                "ਹਰਿਆਣਾ ਸਥਾਪਨਾ ਦਿਵਸ",
            ),
            ("2018-11-06", "ਦੀਪਾਵਲੀ (ਦੱਖਣੀ ਭਾਰਤ); ਨਰਕ ਚਤੁਰਦਾਸੀ"),
            ("2018-11-07", "ਦੀਵਾਲੀ (ਦੀਪਵਾਲੀ)"),
            ("2018-11-08", "ਗੋਵਰਧਨ ਪੂਜਾ"),
            ("2018-11-09", "ਭਾਈ ਦੂਜ"),
            ("2018-11-13", "ਛੱਠ ਪੂਜਾ; ਪ੍ਰਤਿਹਾਰ ਸ਼ਸ਼ਠੀ ਜਾਂ ਸੂਰਜ ਸ਼ਸ਼ਠੀ (ਛਟ ਪੂਜਾ)"),
            ("2018-11-15", "ਝਾਰਖੰਡ ਗਠਨ ਦਿਵਸ"),
            ("2018-11-21", "ਮਿਲਾਦ-ਉੱਨ-ਨਬੀ"),
            ("2018-11-23", "ਗੁਰਪੁਰਬ ਸਾਹਿਬ ਸ੍ਰੀ ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਜੀ"),
            ("2018-11-24", "ਗੁਰੂ ਤੇਗ ਬਹਾਦਰ ਜੀ ਦਾ ਸ਼ਹੀਦੀ ਦਿਹਾੜਾ"),
            ("2018-12-01", "ਨਾਗਾਲੈਂਡ ਰਾਜ ਦਾ ਉਦਘਾਟਨ ਦਿਵਸ"),
            ("2018-12-02", "ਅਸਾਮ ਦਿਵਸ"),
            ("2018-12-19", "ਗੋਆ ਮੁਕਤੀ ਦਿਵਸ"),
            ("2018-12-24", "ਕ੍ਰਿਸਮਿਸ ਦੀ ਪੂਰਵ ਸੰਧਿਆ"),
            ("2018-12-25", "ਕ੍ਰਿਸਮਿਸ ਦਿਵਸ"),
        )

    def test_l10n_ta(self):
        self.assertLocalizedHolidays(
            "ta",
            ("2018-01-01", "புத்தாண்டு தினம்"),
            ("2018-01-13", "லோஹ்ரி"),
            ("2018-01-14", "உத்தராயண் நாள்; பொங்கல்; மகர சங்கராந்தி; மாக் பிஹூ"),
            ("2018-01-15", "திருவள்ளுவர் நாள் / மாட்டுப் பொங்கல்"),
            ("2018-01-16", "உழவர் திருநாள்"),
            ("2018-01-22", "வசந்த பஞ்சமி / ஸ்ரீ பஞ்சமி"),
            ("2018-01-24", "உத்தரப்பிரதேச உருவாக்க நாள்"),
            ("2018-01-26", "குடியரசு நாள்"),
            ("2018-01-31", "குரு ரவி தாஸின் பிறந்தநாள்"),
            ("2018-02-10", "சுவாமி தயானந்த சரஸ்வதி ஜெயந்தி"),
            ("2018-02-13", "மகா சிவராத்திரி"),
            ("2018-02-19", "சத்ரபதி சிவாஜி மகாராஜ் ஜெயந்தி; சிவாஜி ஜெயந்தி"),
            ("2018-02-20", "மிசோரம் மாநில நாள்"),
            ("2018-03-01", "தோலயாத்திரை; ஹோலிகா தஹான்"),
            ("2018-03-02", "ஹோலி"),
            ("2018-03-18", "உகாதி; குடி பாத்வா; செட்டி சந்த்; சைத்ரா சுக்லாடி"),
            ("2018-03-22", "பீகார் நாள்"),
            ("2018-03-25", "ராம நவமி"),
            ("2018-03-29", "மகாவீர் ஜெயந்தி"),
            ("2018-03-30", "புனித வெள்ளி; ராஜஸ்தான் நாள்"),
            ("2018-04-01", "ஈஸ்டர் ஞாயிறு; ஒடிசா நாள் (உத்கல திவசம்); ஹஸ்ரத் அலியின் பிறந்தநாள்"),
            (
                "2018-04-14",
                "டாக்டர் பி. ஆர். அம்பேத்கர் ஜெயந்தி; "
                "புத்தாண்டு (தமிழ் புத்தாண்டு); "
                "மேஷாடி (தமிழ் புத்தாண்டு தினம்); "
                "விசு; "
                "வைசாகி",
            ),
            (
                "2018-04-15",
                "இமாச்சல் நாள்; பஹாக் பிஹு; பொஹேலா பொய்ஷாக்; மகா விஷுவ சங்கராந்தி / பானா சங்கராந்தி; வைசாகதி",
            ),
            ("2018-04-30", "புத்தர் பௌர்ணமி"),
            ("2018-05-01", "குஜராத் நாள்; மகாராஷ்டிரா நாள்"),
            ("2018-05-09", "குரு ரவீந்திரநாத் ஜெயந்தி; ரபீந்திர ஜெயந்தி"),
            ("2018-05-16", "சிக்கிம் மாநில நாள்"),
            ("2018-06-02", "தெலுங்கானா உருவாக்க நாள்"),
            ("2018-06-15", "ஜமாத்-உல்-விடா"),
            ("2018-06-16", "ஈத் உல்-பித்ர்; மகாராணா பிரதாப் ஜெயந்தி"),
            ("2018-07-14", "ரத யாத்திரை"),
            ("2018-08-06", "போனாலு"),
            ("2018-08-15", "சுதந்திர தினம்"),
            ("2018-08-16", "புதுச்சேரி சட்டபூர்வ பரிமாற்ற நாள்"),
            ("2018-08-17", "பார்சி புத்தாண்டு; பார்சி புத்தாண்டு (ஷாஹென்ஷாஹி)"),
            ("2018-08-22", "ஈதுல் ஸுஹா (பக்ரீத்)"),
            ("2018-08-24", "ஓணம்"),
            ("2018-08-26", "ரக்ஷா பந்தன்"),
            ("2018-09-03", "ஜனமாஷ்டமி (வைஷ்ணவ)"),
            ("2018-09-13", "விநாயகர் சதுர்த்தி / விநாயக சதுர்த்தி"),
            ("2018-09-21", "முஹர்ரம்"),
            ("2018-10-02", "மகாத்மா காந்தி ஜெயந்தி"),
            ("2018-10-08", "பதுக்கம்மா திருவிழா"),
            ("2018-10-16", "தசரா (சப்தமி)"),
            ("2018-10-17", "தசரா (மகாநவமி); தசரா (மகாஷ்டமி)"),
            ("2018-10-19", "விஜயதசமி"),
            ("2018-10-24", "மகரிஷி வால்மீகி ஜெயந்தி"),
            ("2018-10-27", "காரக சதுர்த்தி (கர்வா சௌத்)"),
            ("2018-10-31", "சர்தார் வல்லபாய் படேல் ஜெயந்தி"),
            (
                "2018-11-01",
                "ஆந்திரப் பிரதேச நாள்; "
                "கர்நாடக ராஜ்யோற்சவம்; "
                "கேரள நாள்; "
                "சத்தீஸ்கர் நாள்; "
                "நியூ பஞ்சாப் நாள்; "
                "புதுச்சேரி விடுதலை நாள்; "
                "மத்திய பிரதேச நாள்; "
                "ஹரியானா நாள்",
            ),
            ("2018-11-06", "தீபாவளி (தென்னிந்தியா); நரக சதுர்தாசி"),
            ("2018-11-07", "தீபாவளி"),
            ("2018-11-08", "கோவர்தன் பூஜை"),
            ("2018-11-09", "பாய் தூஜ்"),
            ("2018-11-13", "சத் பூஜை; பிரதிஹார் ஷஷ்டி அல்லது சூர்ய ஷஷ்டி (சட் பூஜை)"),
            ("2018-11-15", "ஜார்கண்ட் உருவாக்க நாள்"),
            ("2018-11-21", "மீலாது உல் நபி"),
            ("2018-11-23", "குரு நானக் ஜெயந்தி"),
            ("2018-11-24", "குரு தேக் பகதூர் தியாகி தினம்"),
            ("2018-12-01", "நாகலாந்து மாநில தொடக்க நாள்"),
            ("2018-12-02", "அஸ்ஸாம் நாள்"),
            ("2018-12-19", "கோவா விடுதலை நாள்"),
            ("2018-12-24", "கிறிஸ்துமஸ் ஈவ்"),
            ("2018-12-25", "கிறிஸ்துமஸ்"),
        )

    def test_l10n_te(self):
        self.assertLocalizedHolidays(
            "te",
            ("2018-01-01", "కొత్త సంవత్సరం రోజు"),
            ("2018-01-13", "లోహ్రీ"),
            ("2018-01-14", "ఉత్తరాయణం; పొంగల్; భోగాలీ బిహు; మకర సంక్రాంతి"),
            ("2018-01-15", "తిరువళ్ళువర్ దినోత్సవం / మట్టు పొంగల్"),
            ("2018-01-16", "రైతుల పండుగ"),
            ("2018-01-22", "వసంత పంచమి / శ్రీ పంచమి"),
            ("2018-01-24", "ఉత్తర ప్రదేశ్ అవతరణ దినోత్సవం"),
            ("2018-01-26", "గణతంత్ర దినోత్సవం"),
            ("2018-01-31", "గురు రవిదాస్ పుట్టినరోజు"),
            ("2018-02-10", "స్వామి దయానంద్ సరస్వతి జయంతి"),
            ("2018-02-13", "మహాశివరాత్రి"),
            ("2018-02-19", "ఛత్రపతి శివాజీ మహారాజ్ జయంతి; శివాజీ జయంతి"),
            ("2018-02-20", "మిజోరాం రాష్ట్ర దినోత్సవం"),
            ("2018-03-01", "దోలయాత్ర; హోలికా దహన్"),
            ("2018-03-02", "హోలీ"),
            ("2018-03-18", "ఉగాది; గుడి పడ్వా; చెట్టి చంద్; చైత్ర శుక్లాది"),
            ("2018-03-22", "బీహార్ దినోత్సవం"),
            ("2018-03-25", "శ్రీరామనవమి"),
            ("2018-03-29", "మహావీర్ జయంతి"),
            ("2018-03-30", "గుడ్ ఫ్రైడే; రాజస్థాన్ దినోత్సవం"),
            ("2018-04-01", "ఈస్టర్ ఆదివారం; ఒడిశా దినోత్సవం (ఉత్కల దివస); హజ్రత్ అలీ జన్మదినం"),
            (
                "2018-04-14",
                "డా. బి.ఆర్. అంబేద్కర్ జయంతి; "
                "పుతండు (తమిళ నూతన సంవత్సరం); "
                "మేషాది (తమిళ్ నూతన సంవత్సరం); "
                "విషు; "
                "వైశాఖి",
            ),
            (
                "2018-04-15",
                "పొహెలా బొయిషాఖ్; బహగ్ బిహు; మహా విషువ సంక్రాంతి / పానా సంక్రాంతి; వైశాఖాది; హిమాచల్ దినోత్సవం",
            ),
            ("2018-04-30", "బుద్ధ పూర్ణిమ"),
            ("2018-05-01", "గుజరాత్ దినోత్సవం; మహారాష్ట్ర దినోత్సవం"),
            ("2018-05-09", "గురు రవీంద్రనాథ్ జయంతి; రవీంద్ర జయంతి"),
            ("2018-05-16", "సిక్కిం రాష్ట్ర దినోత్సవం"),
            ("2018-06-02", "తెలంగాణ అవతరణ దినోత్సవం"),
            ("2018-06-15", "జమాత్-ఉల్-విదా"),
            ("2018-06-16", "ఈద్-ఉల్-ఫితర్; మహారాణా ప్రతాప్ జయంతి"),
            ("2018-07-14", "రథ యాత్ర"),
            ("2018-08-06", "బోనాలు"),
            ("2018-08-15", "స్వాతంత్ర దినోత్సవం"),
            ("2018-08-16", "పుదుచ్చేరి చట్టబద్ధ బదిలీ దినోత్సవం"),
            ("2018-08-17", "పార్సీ నూతన సంవత్సరం; పార్సీ నూతన సంవత్సరం (షహన్‌షాహీ)"),
            ("2018-08-22", "ఈద్-ఉల్-జుహా (బక్రీద్)"),
            ("2018-08-24", "ఓణం"),
            ("2018-08-26", "రాఖీ పౌర్ణమి"),
            ("2018-09-03", "జన్మాష్టమి (వైష్ణవ)"),
            ("2018-09-13", "గణేశ చవితి / వినాయక చవితి"),
            ("2018-09-21", "మొహర్రం"),
            ("2018-10-02", "మహాత్మా గాంధీ జయంతి"),
            ("2018-10-08", "బతుకమ్మ పండుగ"),
            ("2018-10-16", "దసరా (సప్తమి)"),
            ("2018-10-17", "దసరా (మహానవమి); దసరా (మహాష్టమి)"),
            ("2018-10-19", "విజయదశమి"),
            ("2018-10-24", "మహర్షి వాల్మీకి జయంతి"),
            ("2018-10-27", "కరక చతుర్థి (కర్వా చౌత్)"),
            ("2018-10-31", "సర్దార్ వల్లభభాయి పటేల్ జయంతి"),
            (
                "2018-11-01",
                "ఆంధ్రప్రదేశ్ అవతరణ దినోత్సవం; "
                "కర్ణాటక రాజ్యోత్సవం; "
                "కేరళ అవతరణ దినోత్సవం; "
                "కొత్త పంజాబ్ దినోత్సవం; "
                "ఛత్తీస్‌గఢ్ అవతరణ దినోత్సవం; "
                "పుదుచ్చేరి విమోచన దినోత్సవం; "
                "మధ్యప్రదేశ్ అవతరణ దినోత్సవం; "
                "హర్యానా అవతరణ దినోత్సవం",
            ),
            ("2018-11-06", "దీపావళి (దక్షిణ భారతదేశం); నరక చతుర్దశి"),
            ("2018-11-07", "దీపావళి"),
            ("2018-11-08", "గోవర్ధన పూజ"),
            ("2018-11-09", "భాయ్ దూజ్"),
            ("2018-11-13", "ఛఠ్ పూజ; ప్రతిహార్ షష్ఠి లేదా సూర్య షష్ఠి (ఛత్ పూజ)"),
            ("2018-11-15", "ఝార్ఖండ్ అవతరణ దినోత్సవం"),
            ("2018-11-21", "మిలాద్-ఉన్-నబీ"),
            ("2018-11-23", "గురునానక్ జయంతి"),
            ("2018-11-24", "గురు తేగ్ బహదూర్ అమరవీర దినోత్సవం"),
            ("2018-12-01", "నాగాలాండ్ రాష్ట్ర ప్రారంభ దినోత్సవం"),
            ("2018-12-02", "అస్సాం దినోత్సవం"),
            ("2018-12-19", "గోవా విమోచన దినోత్సవం"),
            ("2018-12-24", "క్రిస్మస్ ఈవ్"),
            ("2018-12-25", "క్రిస్మస్"),
        )
