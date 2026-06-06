import pytest

from life import run, step


def test_empty_board_stays_empty():
    assert step(set()) == frozenset()


def test_blinker_oscillates_with_period_two():
    horizontal = frozenset({(0, 0), (1, 0), (2, 0)})
    vertical = frozenset({(1, -1), (1, 0), (1, 1)})
    assert step(horizontal) == vertical
    assert step(vertical) == horizontal


def test_block_is_stable():
    block = frozenset({(0, 0), (1, 0), (0, 1), (1, 1)})
    assert step(block) == block


def test_single_cell_dies():
    assert step({(5, 5)}) == frozenset()


def test_isolated_pair_dies():
    assert step({(0, 0), (1, 0)}) == frozenset()


def test_glider_translates_after_four_steps():
    glider = frozenset({(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)})
    shifted = run(glider, 4)
    assert shifted == frozenset({(x + 1, y + 1) for (x, y) in glider})


def test_run_with_zero_generations_returns_input():
    state = {(0, 0), (1, 1)}
    assert run(state, 0) == frozenset(state)


def test_run_negative_generations_raises():
    with pytest.raises(ValueError):
        run(set(), -1)
