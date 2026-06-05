import pytest

from retry import retry


def make_flaky(succeed_at, exception_type=ValueError):
    calls = {"count": 0}

    def func():
        calls["count"] += 1
        if calls["count"] < succeed_at:
            raise exception_type("flaky")
        return "ok"

    return func, calls


def test_returns_immediately_on_success():
    func, calls = make_flaky(succeed_at=1)
    decorated = retry(attempts=3)(func)
    assert decorated() == "ok"
    assert calls["count"] == 1


def test_retries_until_success():
    func, calls = make_flaky(succeed_at=3)
    sleeps = []
    decorated = retry(
        attempts=5, delay=0.1, backoff=2.0, sleep=sleeps.append
    )(func)
    assert decorated() == "ok"
    assert calls["count"] == 3
    assert sleeps == [0.1, 0.2]


def test_raises_after_exhausting_attempts():
    func, calls = make_flaky(succeed_at=99)
    decorated = retry(attempts=3, sleep=lambda _: None)(func)
    with pytest.raises(ValueError):
        decorated()
    assert calls["count"] == 3


def test_only_catches_listed_exceptions():
    def boom():
        raise TypeError("not retried")

    sleeps = []
    decorated = retry(
        attempts=3, exceptions=(ValueError,), sleep=sleeps.append
    )(boom)
    with pytest.raises(TypeError):
        decorated()
    assert sleeps == []


def test_zero_delay_skips_sleep():
    func, _ = make_flaky(succeed_at=2)
    sleeps = []
    decorated = retry(attempts=3, delay=0, sleep=sleeps.append)(func)
    decorated()
    assert sleeps == []


def test_attempts_must_be_positive():
    with pytest.raises(ValueError):
        retry(attempts=0)


def test_preserves_function_metadata():
    @retry(attempts=2)
    def example():
        """example docstring"""
        return 1

    assert example.__name__ == "example"
    assert example.__doc__ == "example docstring"
