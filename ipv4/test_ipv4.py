import pytest

from ipv4 import int_to_ip, ip_to_int


def test_ip_to_int_basic():
    assert ip_to_int("0.0.0.0") == 0
    assert ip_to_int("255.255.255.255") == 0xFFFFFFFF
    assert ip_to_int("192.168.1.1") == 0xC0A80101
    assert ip_to_int("10.0.0.1") == 10 * 2 ** 24 + 1


def test_int_to_ip_basic():
    assert int_to_ip(0) == "0.0.0.0"
    assert int_to_ip(0xFFFFFFFF) == "255.255.255.255"
    assert int_to_ip(0xC0A80101) == "192.168.1.1"


def test_round_trip():
    for address in ("0.0.0.0", "127.0.0.1", "192.168.1.100", "255.255.255.255"):
        assert int_to_ip(ip_to_int(address)) == address


def test_ip_to_int_invalid_raises():
    for bad in ("1.2.3", "1.2.3.4.5", "256.0.0.0", "abc", "1.2.3.x"):
        with pytest.raises(ValueError):
            ip_to_int(bad)


def test_int_to_ip_out_of_range_raises():
    with pytest.raises(ValueError):
        int_to_ip(-1)
    with pytest.raises(ValueError):
        int_to_ip(0x100000000)
