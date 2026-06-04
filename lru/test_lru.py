import pytest

from lru import LRUCache


def test_basic_set_and_get():
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)
    assert cache.get("a") == 1
    assert cache.get("b") == 2


def test_default_when_missing():
    cache = LRUCache(2)
    assert cache.get("missing") is None
    assert cache.get("missing", "fallback") == "fallback"


def test_evicts_least_recently_used():
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.get("a")             # "a" is now most recent
    cache.set("c", 3)          # "b" should be evicted
    assert "a" in cache
    assert "c" in cache
    assert "b" not in cache


def test_set_existing_marks_recent():
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("a", 10)         # "a" is now most recent
    cache.set("c", 3)          # "b" should be evicted
    assert cache.get("a") == 10
    assert "b" not in cache


def test_capacity_must_be_positive():
    with pytest.raises(ValueError):
        LRUCache(0)


def test_dict_style_access():
    cache = LRUCache(2)
    cache["a"] = 1
    assert cache["a"] == 1
    assert "a" in cache
    with pytest.raises(KeyError):
        cache["missing"]


def test_len_and_stats():
    cache = LRUCache(3)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.get("a")             # hit
    cache.get("z")             # miss
    assert len(cache) == 2
    assert cache.stats == {"hits": 1, "misses": 1, "size": 2}
