import pytest
from vacanza_holidays import parse_year_range, validate_country_code, get_categories

def test_get_categories():
    supported_categories = ("public", "bank", "school", "observance")
    category = "public"
    country_code = "US"
    assert get_categories(category, country_code, supported_categories) == ["public"]
    category = None
    assert get_categories(category, country_code, supported_categories) == ["public", "bank", "school", "observance"]


def test_parse_year_range():
    assert parse_year_range("2027") == range(2027, 2028)
    assert parse_year_range("2027-2030") == range(2027, 2031)
    assert parse_year_range("1901-2011") == range(1901, 2012)

def test_parse_year_range_invalid():
    with pytest.raises(ValueError): 
        assert parse_year_range("Twenty-Twenty-six")
    with pytest.raises(ValueError):
        assert parse_year_range("1/1/2029")

def test_validate_country_code():
    # Valid country code
    assert validate_country_code("RU") == "RU"
    assert validate_country_code("RUS") == "RU"
    assert validate_country_code("Russia") == "RU"
    assert validate_country_code("us") == "US"
    assert validate_country_code("USA") == "US"

    # Invalid country_code
    with pytest.raises(ValueError): 
        assert validate_country_code("america")
    with pytest.raises(ValueError): 
        assert validate_country_code("idk")