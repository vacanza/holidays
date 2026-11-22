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

"""Check that lazy calendars/groups imports cannot deadlock with EntityLoader.

Thread B imports a country module directly (calendars/groups load lazily in its
body). Thread A loads the same country through `EntityLoader`, which holds
`IMPORT_LOCK` while waiting for B's module import lock. B must not need that
lock. Sync on A holding `IMPORT_LOCK`, and fail if either thread raises.
"""

from __future__ import annotations

import importlib
import sys
import threading

import holidays
import holidays.registry as registry

b_started = threading.Event()
a_holding = threading.Event()
errors: list[str] = []
_lock = registry.IMPORT_LOCK


class SignalLock:
    def __enter__(self):
        result = _lock.__enter__()
        if threading.current_thread().name == "A":
            a_holding.set()
        return result

    def __exit__(self, *args):
        return _lock.__exit__(*args)


class Finder:
    def find_spec(self, name, path=None, target=None):
        if name == "holidays.countries.albania" and threading.current_thread().name == "B":
            b_started.set()
            if not a_holding.wait(5):
                raise TimeoutError("A did not acquire IMPORT_LOCK")


def run(name: str, fn) -> None:
    try:
        fn()
    except Exception as exc:
        errors.append(f"{name}:{type(exc).__name__}:{exc}")


def load_entity() -> None:
    if not b_started.wait(5):
        raise TimeoutError("B did not start importing")
    holidays.country_holidays("AL")


def main() -> None:
    registry.IMPORT_LOCK = SignalLock()  # type: ignore[assignment]
    sys.meta_path.insert(0, Finder())

    threads = (
        threading.Thread(target=run, args=("A", load_entity), name="A", daemon=True),
        threading.Thread(
            target=run,
            args=("B", lambda: importlib.import_module("holidays.countries.albania")),
            name="B",
            daemon=True,
        ),
    )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(10)

    if any(thread.is_alive() for thread in threads):
        print("deadlock")
    elif errors:
        print("error:" + ";".join(errors))
    else:
        print("ok")


if __name__ == "__main__":
    main()
