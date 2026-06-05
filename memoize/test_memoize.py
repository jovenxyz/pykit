import pytest

from memoize import memoize


def test_caches_within_ttl():
    clock = [0.0]
    calls = {"count": 0}

    @memoize(ttl=10, time_func=lambda: clock[0])
    def add(a, b):
        calls["count"] += 1
        return a + b

    assert add(1, 2) == 3
    assert add(1, 2) == 3
    assert calls["count"] == 1


def test_recomputes_after_ttl():
    clock = [0.0]
    calls = {"count": 0}

    @memoize(ttl=10, time_func=lambda: clock[0])
    def add(a, b):
        calls["count"] += 1
        return a + b

    add(1, 2)
    clock[0] = 5
    add(1, 2)
    assert calls["count"] == 1   # still cached
    clock[0] = 11
    add(1, 2)
    assert calls["count"] == 2   # recomputed


def test_distinct_args_cached_separately():
    clock = [0.0]
    calls = {"count": 0}

    @memoize(ttl=10, time_func=lambda: clock[0])
    def add(a, b):
        calls["count"] += 1
        return a + b

    add(1, 2)
    add(3, 4)
    assert calls["count"] == 2
    add(1, 2)
    add(3, 4)
    assert calls["count"] == 2


def test_kwargs_keyed_consistently():
    calls = {"count": 0}

    @memoize(ttl=10)
    def greet(name="world"):
        calls["count"] += 1
        return f"hello {name}"

    greet(name="alice")
    greet(name="alice")
    assert calls["count"] == 1


def test_clear_forces_recompute():
    clock = [0.0]
    calls = {"count": 0}

    @memoize(ttl=10, time_func=lambda: clock[0])
    def add(a, b):
        calls["count"] += 1
        return a + b

    add(1, 2)
    add.clear()
    add(1, 2)
    assert calls["count"] == 2


def test_ttl_must_be_positive():
    with pytest.raises(ValueError):
        memoize(ttl=0)


def test_preserves_function_metadata():
    @memoize(ttl=5)
    def example():
        """example docstring"""
        return 1

    assert example.__name__ == "example"
    assert example.__doc__ == "example docstring"
