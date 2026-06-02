import pytest

from semver import parse


def test_parse_basic():
    v = parse("1.2.3")
    assert (v.major, v.minor, v.patch) == (1, 2, 3)
    assert v.prerelease is None
    assert v.build is None


def test_parse_prerelease_and_build():
    v = parse("1.0.0-rc.1+build.5")
    assert v.prerelease == "rc.1"
    assert v.build == "build.5"


def test_parse_invalid_raises():
    with pytest.raises(ValueError):
        parse("v1.0")
    with pytest.raises(ValueError):
        parse("1.2")


def test_str_round_trip():
    for text in ("1.2.3", "1.0.0-rc.1", "2.0.0+build.5", "1.0.0-rc.1+build.5"):
        assert str(parse(text)) == text


def test_ordering_core():
    assert parse("1.0.0") < parse("1.0.1")
    assert parse("1.0.1") < parse("1.1.0")
    assert parse("1.1.0") < parse("2.0.0")


def test_prerelease_is_lower_than_release():
    assert parse("1.0.0-rc.1") < parse("1.0.0")
    assert parse("1.0.0-alpha") < parse("1.0.0-beta")
    assert parse("1.0.0-alpha.1") < parse("1.0.0-alpha.2")
    # Numeric prerelease identifiers have lower precedence than alphanumeric.
    assert parse("1.0.0-2") < parse("1.0.0-alpha")


def test_bump():
    v = parse("1.2.3-rc.1")
    assert str(v.bump_patch()) == "1.2.4"
    assert str(v.bump_minor()) == "1.3.0"
    assert str(v.bump_major()) == "2.0.0"
