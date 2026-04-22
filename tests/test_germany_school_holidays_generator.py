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

import sys
from pathlib import Path
from unittest import TestCase, mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "calendar"))

import germany_school_holidays_generator as generator


class _FakePDF:
    def __init__(self, table):
        self.pages = [mock.Mock(extract_table=mock.Mock(return_value=table))]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return None


class _FakePDFPlumber:
    def __init__(self, table):
        self._table = table

    def open(self, _path):
        return _FakePDF(self._table)


class TestGermanySchoolHolidaysGenerator(TestCase):
    def test_normalize_ranges_uses_symbolic_holiday_ids(self):
        data = generator.normalize_ranges(
            [(2025, {"BE": [("Herbst", "2025", "20.10.-21.10")]})]
        )

        self.assertEqual(
            data,
            {2025: {"BE": [(0, 10, 20, 0, 10, 21, generator.AUTUMN_BREAK)]}},
        )

    def test_parse_school_year_century_rollover(self):
        self.assertEqual(generator._parse_school_year("1999/00"), (1999, 2000))

    def test_resolve_school_year_ranges(self):
        self.assertEqual(
            tuple(dt.isoformat() for dt in generator._resolve_years("1998/99", (12, 21, 12, 31))),
            ("1998-12-21", "1998-12-31"),
        )
        self.assertEqual(
            tuple(dt.isoformat() for dt in generator._resolve_years("2003/2004", (1, 30, 1, 30))),
            ("2004-01-30", "2004-01-30"),
        )
        self.assertEqual(
            tuple(dt.isoformat() for dt in generator._resolve_years("2003/2004", (12, 22, 1, 3))),
            ("2003-12-22", "2004-01-03"),
        )

    def test_normalize_cell_handles_kmk_edge_cases(self):
        self.assertEqual(generator._normalize_cell("21.05. 3) / 11.06 3)"), "21.05/11.06")
        self.assertEqual(generator._normalize_cell("01.02. . - 10.02."), "01.02.-10.02")
        self.assertEqual(generator._normalize_cell("18.10. - 23-10."), "18.10.-23.10")
        self.assertEqual(
            generator._normalize_cell("31.10.\n02.11. – 4.11."),
            "31.10/02.11.-4.11",
        )

    def test_normalize_cell_handles_footnote_and_non_footnote_variants(self):
        cases = [
            ("21.05./11.06.", "21.05/11.06"),
            ("21.05. 3) / 11.06 3)", "21.05/11.06"),
            ("21.05.3)/11.06.3)", "21.05/11.06"),
            ("21.053)", "21.05"),
            ("30.01", "30.01"),
            ("11.06 3)", "11.06"),
            ("02.11.-04.11.", "02.11.-04.11"),
            ("02.11.-04.11.2", "02.11.-04.11"),
            ("24.06.-05.08.", "24.06.-05.08"),
            ("24.06.-05.08. 3", "24.06.-05.08"),
            ("20.07.-02.09.", "20.07.-02.09"),
            ("20.07.-02.09.4)", "20.07.-02.09"),
            ("11.10.-23.10.", "11.10.-23.10"),
            ("11.10.-23.10.3)", "11.10.-23.10"),
            ("14.04-17.04.", "14.04-17.04"),
            ("14.04-17.04.2", "14.04-17.04"),
            ("06.05/25.05.-28.05.", "06.05/25.05.-28.05"),
            ("06.05/25.05.-28.05.3)", "06.05/25.05.-28.05"),
            ("02.10/16.10.-28.10.", "02.10/16.10.-28.10"),
            ("02.10/16.10.-28.10.3)", "02.10/16.10.-28.10"),
            ("02.10/16.-30.10.", "02.10/16.-30.10"),
            ("02.10/16.-30.10.2)", "02.10/16.-30.10"),
            ("--", "--"),
            ("--2)", "--"),
            ("__", "__"),
            ("3)", ""),
        ]

        for raw, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(generator._normalize_cell(raw), expected)

    def test_parse_cell_ranges_handles_multi_date_formats(self):
        self.assertEqual(
            generator.parse_cell_ranges(generator._normalize_cell("29. + 30.01.")),
            [(1, 29, 1, 29), (1, 30, 1, 30)],
        )
        self.assertEqual(
            generator.parse_cell_ranges(generator._normalize_cell("20./21.06. - 03.08.")),
            [(6, 20, 6, 20), (6, 21, 8, 3)],
        )
        self.assertEqual(
            generator.parse_cell_ranges(generator._normalize_cell("31.10.\n02.11. – 4.11.")),
            [(10, 31, 10, 31), (11, 2, 11, 4)],
        )
        self.assertEqual(
            generator.parse_cell_ranges(generator._normalize_cell("22.12. - 03.01. / 30.01. 3)")),
            [(12, 22, 1, 3), (1, 30, 1, 30)],
        )

    def test_parse_cell_ranges_handles_footnote_and_non_footnote_variants(self):
        cases = [
            ("21.05./11.06.", [(5, 21, 5, 21), (6, 11, 6, 11)]),
            ("21.05. 3) / 11.06 3)", [(5, 21, 5, 21), (6, 11, 6, 11)]),
            ("21.05.", [(5, 21, 5, 21)]),
            ("21.053)", [(5, 21, 5, 21)]),
            ("30.01", [(1, 30, 1, 30)]),
            ("11.06", [(6, 11, 6, 11)]),
            ("11.06 3)", [(6, 11, 6, 11)]),
            ("02.11.-04.11.", [(11, 2, 11, 4)]),
            ("02.11.-04.11.2", [(11, 2, 11, 4)]),
            ("24.06.-05.08.", [(6, 24, 8, 5)]),
            ("24.06.-05.08. 3", [(6, 24, 8, 5)]),
            ("20.07.-02.09.", [(7, 20, 9, 2)]),
            ("20.07.-02.09.4)", [(7, 20, 9, 2)]),
            ("11.10.-23.10.", [(10, 11, 10, 23)]),
            ("11.10.-23.10.3)", [(10, 11, 10, 23)]),
            ("14.04-17.04.", [(4, 14, 4, 17)]),
            ("14.04-17.04.2", [(4, 14, 4, 17)]),
            ("06.05/25.05.-28.05.", [(5, 6, 5, 6), (5, 25, 5, 28)]),
            ("06.05/25.05.-28.05.3)", [(5, 6, 5, 6), (5, 25, 5, 28)]),
            ("02.10/16.10.-28.10.", [(10, 2, 10, 2), (10, 16, 10, 28)]),
            ("02.10/16.10.-28.10.3)", [(10, 2, 10, 2), (10, 16, 10, 28)]),
            ("02.10/16.-30.10.", [(10, 2, 10, 2), (10, 16, 10, 30)]),
            ("02.10/16.-30.10.2)", [(10, 2, 10, 2), (10, 16, 10, 30)]),
            ("--", []),
            ("--2)", []),
            ("__", []),
            ("3)", []),
        ]

        for raw, expected in cases:
            with self.subTest(raw=raw):
                self.assertEqual(
                    generator.parse_cell_ranges(generator._normalize_cell(raw)),
                    expected,
                )

    def test_parse_pdf_table_keeps_duplicate_columns(self):
        table = [
            [
                "Land 2)",
                "Sommer\n2001",
                "Herbst\n2001",
                "Weihnachten\n2001/2002",
                "Winter\n2002",
                "Ostern/Frühjahr\n2002",
                "Himmelfahrt/Pfingsten\n2002",
                "Sommer\n2002",
            ],
            [
                "Thüringen (3)",
                "28.06. - 08.08.",
                "15.10. - 20.10.",
                "21.12. - 05.01.",
                "04.02. - 09.02.",
                "25.03. - 06.04.",
                "17.05. - 21.05.",
                "20.06. - 31.07.",
            ],
        ]

        with (
            mock.patch.object(
                generator, "_require_pdfplumber", return_value=_FakePDFPlumber(table)
            ),
            mock.patch.object(generator, "EXPECTED_SUBDIVISIONS", frozenset({"TH"})),
        ):
            start_year, rows = generator._parse_pdf_table(Path("Ferien01_02.pdf"))

        self.assertEqual(start_year, 2001)
        self.assertEqual(
            rows["TH"],
            [
                ("Sommer", "2001", "28.06.-08.08"),
                ("Herbst", "2001", "15.10.-20.10"),
                ("Weihnachten", "2001/2002", "21.12.-05.01"),
                ("Winter", "2002", "04.02.-09.02"),
                ("Ostern/Frühjahr", "2002", "25.03.-06.04"),
                ("Himmelfahrt/Pfingsten", "2002", "17.05.-21.05"),
                ("Sommer", "2002", "20.06.-31.07"),
            ],
        )

    def test_render_python_module_uses_constants(self):
        rendered = generator.render_python_module(
            {2025: {"BE": [(0, 10, 20, 0, 10, 21, generator.AUTUMN_BREAK)]}}
        )

        self.assertIn("AUTUMN_BREAK", rendered)
        self.assertIn(") = range(6)", rendered)
        self.assertIn('(0, 10, 20, 0, 10, 21, AUTUMN_BREAK),', rendered)
        self.assertNotIn('"Herbstferien"', rendered)
