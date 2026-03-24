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

from importlib.metadata import PackageNotFoundError, version as _get_version
from pathlib import Path

try:
    __version__ = _get_version("holidays")
except PackageNotFoundError:
    try:
        _version_file = Path(__file__).resolve().parent.parent / "VERSION"
        __version__ = _version_file.read_text(encoding="utf-8").strip()
    except OSError:
        # Fallback version if neither package metadata nor VERSION file is available.
        __version__ = "0.0.0"