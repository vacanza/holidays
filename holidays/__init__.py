#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
__all__ = [
    "country_holidays",
    "financial_holidays",
    "list_supported_countries",
    "list_supported_financial",
]

import importlib
import inspect
import sys
import warnings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from holidays.utils import country_holidays, financial_holidays
    from holidays.utils import list_supported_countries
    from holidays.utils import list_supported_financial

__version__ = "0.22"

# The below is the implementation of a transitional loading strategy to migrate
# from the legacy expensive and slow load-every-object architecture to one
# where subclasses are loaded only when needed.
#
# The new efficient loading is implemented through the `country_holidays` and
# `financial_holidays` functions, which return a :py:class:`Holidays` object.
#
# Backwards compatibility is maintained by loading every object in the library
# when this __init__.py  module is imported with `import holidays` or any other
# way except for `from holidays import country_holidays` or any function in
# __all__, which are the generic functions and which themselves load only
# the submodules needed.  We determine this by looking at the code object of
# the frame that called this module.
#
# TODO: This mechanism should be removed once all other ways of instantiating a
# :py:class:`Holidays` object are fully deprecated.

# BETA: For now available only on Python 3.11 due to not having done thorough
# testing with prior versions.

if sys.version_info >= (3, 11):
    loading_stack = inspect.stack()[-1]  # the frame that called this module
    loading_code = loading_stack.frame.f_code  # the frame's code object
    if loading_code and all(
        name in ([__name__] + __all__) for name in loading_code.co_names
    ):
        # Load only the function(s) from utils but not all objects, as the
        # necessary country or market submodule (and nothing more) will be
        # loaded by the function itself.
        module = importlib.import_module("holidays.utils")
        for object_name in loading_code.co_names[1:]:
            globals().update({object_name: module.__dict__[object_name]})
    else:
        # Load all objects from all submodules (legacy-compatible, deprecated)
        for submodule_name in {
            "constants",
            "countries",
            "financial",
            "holiday_base",
            "utils",
        }:
            module = importlib.import_module(f"holidays.{submodule_name}")
            globals().update(
                {
                    k: v
                    for k, v in module.__dict__.items()
                    if not k.startswith("_")
                }
            )
        warnings.warn(
            "Please use 'from holidays import country_holidays' and/or "
            "'from holidays import financial_holidays' and then use that "
            "function to instantiate the public holidays object. This will "
            "also speed up your program's loading.",
            PendingDeprecationWarning,
        )
else:
    # Load all objects from all submodules (legacy-compatible)
    for submodule_name in {
        "constants",
        "countries",
        "financial",
        "holiday_base",
        "utils",
    }:
        module = importlib.import_module(f"holidays.{submodule_name}")
        globals().update(
            {k: v for k, v in module.__dict__.items() if not k.startswith("_")}
        )
