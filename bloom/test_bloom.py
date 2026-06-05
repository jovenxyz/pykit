import pytest

from bloom import BloomFilter


def test_added_items_are_present():
    bf = BloomFilter(expected_items=100)
    for word in ("apple", "banana", "cherry"):
        bf.add(word)
    for word in ("apple", "banana", "cherry"):
        assert word in bf


def test_missing_item_usually_absent():
    bf = BloomFilter(expected_items=100, false_positive_rate=0.001)
    bf.add("apple")
    # With a 0.1% FP rate and only one item present, this should not match.
    assert "banana" not in bf


def test_no_false_negatives_for_many_items():
    bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)
    items = [f"item-{i}" for i in range(500)]
    for item in items:
        bf.add(item)
    # A Bloom filter must never produce a false negative.
    for item in items:
        assert item in bf


def test_len_counts_add_operations():
    bf = BloomFilter(expected_items=10)
    bf.add("a")
    bf.add("b")
    bf.add("a")            # duplicate still counts as an add operation
    assert len(bf) == 3


def test_invalid_params_raise():
    with pytest.raises(ValueError):
        BloomFilter(expected_items=0)
    with pytest.raises(ValueError):
        BloomFilter(expected_items=10, false_positive_rate=0)
    with pytest.raises(ValueError):
        BloomFilter(expected_items=10, false_positive_rate=1.0)


def test_optimal_parameters_are_reasonable():
    bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)
    # Classic guidance: ~9.6 bits per item and ~7 hashes for a 1% FP rate.
    assert 8 <= bf.bit_size / 1000 <= 12
    assert 5 <= bf.hash_count <= 9
