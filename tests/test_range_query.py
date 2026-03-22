from datetime import date
import holidays
from holidays.utils import get_holidays_in_range


def test_range_query():
    us = holidays.US()

    result = get_holidays_in_range(
        us,
        date(2024, 1, 1),
        date(2024, 12, 31)
    )

    assert len(result) > 0