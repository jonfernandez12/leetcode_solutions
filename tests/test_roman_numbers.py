import pytest
from utils.roman_numbers import roman_to_integer


@pytest.mark.parametrize(
    'roman_number, integer_number',
    [('MCMXCIV', 1994),
     ('LVIII', 58),])
def test_roman_to_integer(roman_number, integer_number) -> None:
    assert roman_to_integer(roman_number) == integer_number
