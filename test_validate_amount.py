from stk import validate_amount
import pytest


@pytest.mark.parametrize(
    "amount, expected", [("1", 1), ("150000", 150000), ("1000", 1000)]
)
def test_validate_amount(amount, expected):
    assert validate_amount(amount) == expected


@pytest.mark.parametrize(
    "amount", ["abc", "6566 4747", "6338'838", "0", "150001", "-5", "12.5", "١٢٣"]
)
def test_validate_amount_error(amount):
    with pytest.raises(ValueError):
        validate_amount(amount)
