from stk import normalize_phone
import pytest


@pytest.mark.parametrize(
    "phone, expected", [("0712345678", "254712345678"), ("0112345678", "254112345678")]
)
def test_10_str(phone, expected):
    assert normalize_phone(phone) == expected


@pytest.mark.parametrize(
    "phone", ["07123abc78", "01-2345678", "07 2345678", "0212345678", "07١٢٣٤٥٦٧٨"]
)
def test_10_str_error(phone):
    with pytest.raises(ValueError):
        normalize_phone(phone)


@pytest.mark.parametrize(
    "phone, expected",
    [("254712345678", "254712345678"), ("254112345678", "254112345678")],
)
def test_12_str(phone, expected):
    assert normalize_phone(phone) == expected


@pytest.mark.parametrize(
    "phone", ["2547qwertyui", "2541-2345678", "2547 2345678", "123212345678"]
)
def test_12_str_error(phone):
    with pytest.raises(ValueError):
        normalize_phone(phone)


@pytest.mark.parametrize("phone", ["712345678", "+254712345678"])
def test_n_str_error(phone):
    with pytest.raises(ValueError):
        normalize_phone(phone)
