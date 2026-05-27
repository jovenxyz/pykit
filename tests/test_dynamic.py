from pytoolkit.algorithms.dynamic import fibonacci, longest_common_subsequence


def test_fibonacci():
    assert [fibonacci(n) for n in range(7)] == [0, 1, 1, 2, 3, 5, 8]


def test_lcs():
    assert longest_common_subsequence("ABCBDAB", "BDCAB") == 4
