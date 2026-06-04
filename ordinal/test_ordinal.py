import pytest

from ordinal import ordinal, ordinal_suffix


@pytest.mark.parametrize("number,expected", [
    (1, "1st"), (2, "2nd"), (3, "3rd"), (4, "4th"),
    (10, "10th"), (11, "11th"), (12, "12th"), (13, "13th"),
    (14, "14th"), (20, "20th"), (21, "21st"), (22, "22nd"),
    (23, "23rd"), (24, "24th"), (100, "100th"), (101, "101st"),
    (111, "111th"), (112, "112th"), (113, "113th"), (121, "121st"),
])
def test_ordinal_examples(number, expected):
    assert ordinal(number) == expected


def test_zero():
    assert ordinal(0) == "0th"


def test_negative_numbers_use_absolute_value_for_suffix():
    assert ordinal(-1) == "-1st"
    assert ordinal(-11) == "-11th"
    assert ordinal(-22) == "-22nd"


def test_suffix_only():
    assert ordinal_suffix(1) == "st"
    assert ordinal_suffix(11) == "th"
    assert ordinal_suffix(22) == "nd"
