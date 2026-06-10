import pytest

from bitstream import BitReader, BitWriter


def test_writer_single_byte():
    w = BitWriter()
    for bit in (1, 0, 1, 0, 1, 0, 1, 0):
        w.write_bit(bit)
    assert w.to_bytes() == bytes([0b10101010])


def test_writer_partial_byte_is_padded():
    w = BitWriter()
    for bit in (1, 0, 1):
        w.write_bit(bit)
    assert w.to_bytes() == bytes([0b10100000])
    assert w.total_bits == 3


def test_writer_write_bits():
    w = BitWriter()
    w.write_bits(0b1010, 4)
    w.write_bits(0b1111, 4)
    assert w.to_bytes() == bytes([0b10101111])


def test_writer_value_out_of_range_raises():
    w = BitWriter()
    with pytest.raises(ValueError):
        w.write_bits(16, 4)        # max for 4 bits is 15
    with pytest.raises(ValueError):
        w.write_bits(-1, 4)


def test_writer_invalid_bit_raises():
    w = BitWriter()
    with pytest.raises(ValueError):
        w.write_bit(2)


def test_reader_basic():
    r = BitReader(bytes([0b10101010]))
    assert [r.read_bit() for _ in range(8)] == [1, 0, 1, 0, 1, 0, 1, 0]


def test_reader_read_bits():
    r = BitReader(bytes([0b10101111]))
    assert r.read_bits(4) == 0b1010
    assert r.read_bits(4) == 0b1111


def test_reader_eof_raises():
    r = BitReader(bytes([0xFF]))
    for _ in range(8):
        r.read_bit()
    with pytest.raises(EOFError):
        r.read_bit()


def test_round_trip():
    w = BitWriter()
    values = [(5, 3), (12345, 16), (1, 1), (0xDEAD, 16)]
    for value, width in values:
        w.write_bits(value, width)
    r = BitReader(w.to_bytes())
    for value, width in values:
        assert r.read_bits(width) == value


def test_bits_remaining():
    r = BitReader(bytes([0xFF, 0x00]))
    assert r.bits_remaining == 16
    r.read_bits(5)
    assert r.bits_remaining == 11
