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
import pkgutil
from importlib.abc import MetaPathFinder, PathEntryFinder
from typing import Union

loader: Union[MetaPathFinder, PathEntryFinder]
module_name: str
is_pkg: bool

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(  # type: ignore[union-attr]
        module_name
    ).load_module(  # type: ignore[call-arg]
        module_name
    )
    globals()[module_name] = _module
