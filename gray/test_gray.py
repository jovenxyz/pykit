import pytest

from gray import from_gray, sequence, to_gray


def test_known_small_values():
    expected = {
        0: 0b000,
        1: 0b001,
        2: 0b011,
        3: 0b010,
        4: 0b110,
        5: 0b111,
        6: 0b101,
        7: 0b100,
    }
    for binary, gray in expected.items():
        assert to_gray(binary) == gray


def test_round_trip():
    for i in range(256):
        assert from_gray(to_gray(i)) == i


def test_sequence_length():
    assert len(sequence(3)) == 8


def test_sequence_consecutive_values_differ_by_one_bit():
    for n in range(5):
        seq = sequence(n)
        for a, b in zip(seq, seq[1:]):
            assert bin(a ^ b).count("1") == 1


def test_sequence_covers_full_range():
    for n in range(6):
        assert set(sequence(n)) == set(range(1 << n))


def test_negative_inputs_raise():
    with pytest.raises(ValueError):
        to_gray(-1)
    with pytest.raises(ValueError):
        from_gray(-1)
    with pytest.raises(ValueError):
        sequence(-1)


def test_zero_bits():
    assert sequence(0) == [0]
