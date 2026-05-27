from pytoolkit.algorithms.searching import binary_search, linear_search


def test_linear_search():
    assert linear_search([3, 1, 2], 2) == 2
    assert linear_search([3, 1, 2], 9) is None


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
    assert binary_search([1, 2, 3], 9) is None
