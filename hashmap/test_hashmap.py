import pytest

from hashmap import HashMap


def test_set_and_get():
    h = HashMap()
    h["a"] = 1
    h["b"] = 2
    assert h["a"] == 1
    assert h["b"] == 2


def test_get_returns_default():
    h = HashMap()
    assert h.get("missing") is None
    assert h.get("missing", "fallback") == "fallback"


def test_missing_key_raises():
    h = HashMap()
    with pytest.raises(KeyError):
        h["missing"]


def test_overwrite_existing():
    h = HashMap()
    h["a"] = 1
    h["a"] = 2
    assert h["a"] == 2
    assert len(h) == 1


def test_delete():
    h = HashMap()
    h["a"] = 1
    del h["a"]
    assert "a" not in h
    assert len(h) == 0


def test_delete_missing_raises():
    h = HashMap()
    with pytest.raises(KeyError):
        del h["missing"]


def test_contains_and_len():
    h = HashMap()
    assert "a" not in h
    h["a"] = 1
    assert "a" in h
    assert len(h) == 1


def test_resizes_when_load_factor_exceeded():
    h = HashMap(initial_capacity=4, load_factor=0.75)
    for i in range(10):
        h[i] = i * i
    assert h.capacity > 4
    for i in range(10):
        assert h[i] == i * i


def test_iteration_yields_all_keys():
    h = HashMap()
    for k in ("a", "b", "c"):
        h[k] = ord(k)
    assert sorted(h) == ["a", "b", "c"]


def test_items_round_trip():
    h = HashMap()
    h["x"] = 1
    h["y"] = 2
    assert dict(h.items()) == {"x": 1, "y": 2}


def test_invalid_constructor_raises():
    with pytest.raises(ValueError):
        HashMap(initial_capacity=0)
    with pytest.raises(ValueError):
        HashMap(load_factor=0)
    with pytest.raises(ValueError):
        HashMap(load_factor=1.0)
