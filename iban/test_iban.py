import pytest

from iban import country_of, is_valid, normalize


@pytest.mark.parametrize("iban", [
    "GB82WEST12345698765432",
    "DE89370400440532013000",
    "NL91ABNA0417164300",
    "FR1420041010050500013M02606",
    "GB82 WEST 1234 5698 7654 32",       # with spaces
    "gb82west12345698765432",            # lowercase
])
def test_known_valid_ibans(iban):
    assert is_valid(iban)


@pytest.mark.parametrize("iban", [
    "GB82WEST12345698765433",            # last digit flipped
    "DE00370400440532013000",            # check digits zeroed
    "GB82WEST123456987654",              # wrong length for GB
    "",
    "GB",
])
def test_invalid_ibans(iban):
    assert not is_valid(iban)


def test_normalize_strips_and_uppercases():
    assert normalize("  gb82  west 1234  ") == "GB82WEST1234"


def test_country_of():
    assert country_of("GB82WEST12345698765432") == "GB"
    assert country_of("de89 3704 0044") == "DE"


def test_country_of_invalid_raises():
    with pytest.raises(ValueError):
        country_of("12")
    with pytest.raises(ValueError):
        country_of("")
