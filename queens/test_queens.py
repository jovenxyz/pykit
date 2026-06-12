import pytest

from queens import count_solutions, first_solution, solutions


# OEIS A000170: number of solutions for n = 0..10.
KNOWN_COUNTS = {
    0: 1, 1: 1, 2: 0, 3: 0, 4: 2, 5: 10,
    6: 4, 7: 40, 8: 92, 9: 352, 10: 724,
}


@pytest.mark.parametrize("n,expected", list(KNOWN_COUNTS.items()))
def test_known_counts(n, expected):
    assert count_solutions(n) == expected


def test_solutions_iterator_count_matches():
    for n in range(7):
        assert sum(1 for _ in solutions(n)) == KNOWN_COUNTS[n]


def _is_valid(placement):
    cols, diag1, diag2 = set(), set(), set()
    for row, col in enumerate(placement):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
    return True


def test_first_solution_is_valid():
    for n in (4, 5, 8):
        placement = first_solution(n)
        assert len(placement) == n
        assert _is_valid(placement)


def test_first_solution_raises_when_impossible():
    with pytest.raises(ValueError):
        first_solution(2)
    with pytest.raises(ValueError):
        first_solution(3)


def test_negative_n_raises():
    with pytest.raises(ValueError):
        count_solutions(-1)
    with pytest.raises(ValueError):
        list(solutions(-1))
