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

import importlib
from contextlib import AbstractContextManager, nullcontext
from typing import Any


def _normalize_arguments(cls, value):
    """Normalize arguments.

    :param cls:
        A type of arguments to normalize.

    :param value:
        Either a single item or an iterable of `cls` type.

    :return:
        A set created from `value` argument.

    """
    if value is None:
        return set()

    if isinstance(value, str):
        return {cls(value)}

    try:
        return {cls(v) for v in value}
    except TypeError:  # non-iterable
        return {cls(value)}


def _normalize_tuple(value):
    """Normalize tuple.

    :param data:
        Either a tuple or a tuple of tuples.

    :return:
        An unchanged object for tuple of tuples, e.g., ((JAN, 10), (DEC, 31)).
        An object put into a tuple otherwise, e.g., ((JAN, 10),).
    """
    return value if not value or isinstance(value[0], tuple) else (value,)


def tr(message: str) -> str:
    """Mark a string for translation while returning it unchanged at runtime."""
    return message


def _load_lazily(
    scope: dict[str, Any],
    modules: dict[str, tuple[str, ...]],
    lock: AbstractContextManager = nullcontext(),
) -> None:
    """Set up lazy (PEP 562) loading of a package's names from its submodules.

    :param scope:
        The package `globals()`.

    :param modules:
        A mapping of submodule names to the names they provide.

    :param lock:
        An optional lock to hold while importing a submodule.
    """
    package = scope["__name__"]
    name_modules = {name: module for module, names in modules.items() for name in names}

    def getattr_(name: str) -> Any:
        if name in modules:
            with lock:
                return importlib.import_module(f"{package}.{name}")
        if name not in name_modules:
            raise AttributeError(f"module {package!r} has no attribute {name!r}")
        with lock:
            module = importlib.import_module(f"{package}.{name_modules[name]}")
        scope[name] = getattr(module, name)
        return scope[name]

    def dir_() -> list[str]:
        return sorted({*scope, *modules, *name_modules})

    scope["__all__"] = [name for name in (*modules, *name_modules) if not name.startswith("_")]
    scope["__dir__"] = dir_
    scope["__getattr__"] = getattr_
