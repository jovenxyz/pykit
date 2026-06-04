import pytest

from jsonpointer import parse_pointer, resolve


DOC = {
    "foo": ["bar", "baz"],
    "": 0,
    "a/b": 1,
    "m~n": 8,
}


def test_parse_root():
    assert parse_pointer("") == []


def test_parse_single_token():
    assert parse_pointer("/foo") == ["foo"]


def test_parse_escapes():
    assert parse_pointer("/a~1b") == ["a/b"]
    assert parse_pointer("/m~0n") == ["m~n"]


def test_parse_invalid_raises():
    with pytest.raises(ValueError):
        parse_pointer("foo")


def test_resolve_rfc_examples():
    assert resolve(DOC, "") == DOC
    assert resolve(DOC, "/foo") == ["bar", "baz"]
    assert resolve(DOC, "/foo/0") == "bar"
    assert resolve(DOC, "/") == 0
    assert resolve(DOC, "/a~1b") == 1
    assert resolve(DOC, "/m~0n") == 8


def test_resolve_missing_raises_without_default():
    with pytest.raises(KeyError):
        resolve(DOC, "/missing")
    with pytest.raises(KeyError):
        resolve(DOC, "/foo/99")


def test_resolve_missing_returns_default():
    assert resolve(DOC, "/missing", default=None) is None
    assert resolve(DOC, "/foo/99", default="x") == "x"


def test_resolve_through_non_container_returns_default():
    assert resolve({"a": 1}, "/a/b", default=None) is None
