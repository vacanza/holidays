from datetime import date
import holidays
from holidays.utils import get_holidays_in_range


def test_range_query_with_filter():
    us = holidays.US()

    result = get_holidays_in_range(
        us,
        date(2024, 1, 1),
        date(2024, 12, 31),
        keyword="New Year"
    )

    assert any("New Year" in name for name in result.values())