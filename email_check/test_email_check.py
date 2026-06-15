import pytest

from email_check import is_valid, normalize


@pytest.mark.parametrize("address", [
    "user@example.com",
    "first.last@example.co.uk",
    "alice+filter@example.org",
    "user_name@sub.example.com",
    "a@b.co",
    "user-123@example.com",
])
def test_valid_emails(address):
    assert is_valid(address)


@pytest.mark.parametrize("address", [
    "",
    "plainaddress",
    "@no-local.com",
    "no-domain@",
    "user@.com",
    "user@example",            # single-label domain
    "user@example.123",        # numeric TLD
    "user..name@example.com",  # consecutive dots
    ".user@example.com",
    "user.@example.com",
    "user@-example.com",       # label starts with hyphen
    "user@example-.com",       # label ends with hyphen
])
def test_invalid_emails(address):
    assert not is_valid(address)


def test_normalize_lowers_domain():
    assert normalize("User@Example.COM") == "User@example.com"


def test_normalize_missing_at_raises():
    with pytest.raises(ValueError):
        normalize("no-at-sign")


def test_local_part_length_limit():
    assert is_valid("a" * 64 + "@example.com")
    assert not is_valid("a" * 65 + "@example.com")


def test_address_length_limit():
    long_domain = "sub." * 60 + "example.com"
    assert not is_valid(f"user@{long_domain}")
