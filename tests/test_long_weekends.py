#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)


def test_get_long_weekends_basic():
    from holidays.long_weekends import get_long_weekends

    weekends = get_long_weekends("US", years=2024)
    assert isinstance(weekends, list)
    for seq in weekends:
        assert len(seq) >= 3
