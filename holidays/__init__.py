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

from typing import TYPE_CHECKING

from holidays.constants import *
from holidays.holiday_base import *
from holidays.registry import EntityLoader
from holidays.utils import *

if TYPE_CHECKING:  # Re-export for static analysis. Runtime names come from EntityLoader below.
    from holidays.countries import *
    from holidays.financial import *
    from holidays.version import __version__  # noqa: F401
else:

    def __getattr__(name: str):
        # `holidays.version` uses slow to import `importlib.metadata`: load it on demand.
        if name in {"__version__", "version"}:
            from importlib import import_module

            version = import_module("holidays.version")
            return version.__version__ if name == "__version__" else version
        if name == "__all__":
            # No static `__all__`: `import *` exports the public names, and `version` too.
            return sorted({*(attr for attr in globals() if not attr.startswith("_")), "version"})
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    def __dir__() -> list[str]:
        return sorted({*globals(), "__version__", "version"})


EntityLoader.load("countries", globals())
EntityLoader.load("financial", globals())
