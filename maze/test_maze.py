import random

import pytest

from maze import generate, render


def test_dimensions():
    grid = generate(5, 4, rng=random.Random(0))
    assert len(grid) == 4
    assert all(len(row) == 5 for row in grid)


def test_invalid_dimensions_raise():
    with pytest.raises(ValueError):
        generate(0, 5)
    with pytest.raises(ValueError):
        generate(5, -1)


def test_deterministic_with_seed():
    assert generate(8, 8, rng=random.Random(42)) == generate(
        8, 8, rng=random.Random(42)
    )


def test_outer_walls_intact():
    grid = generate(5, 4, rng=random.Random(0))
    for x in range(5):
        assert grid[0][x]["N"] is True
        assert grid[3][x]["S"] is True
    for y in range(4):
        assert grid[y][0]["W"] is True
        assert grid[y][4]["E"] is True


def test_walls_are_symmetric():
    grid = generate(6, 6, rng=random.Random(1))
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if x + 1 < 6:
                assert cell["E"] == grid[y][x + 1]["W"]
            if y + 1 < 6:
                assert cell["S"] == grid[y + 1][x]["N"]


def test_maze_is_perfect():
    # A perfect maze on W*H cells has exactly W*H - 1 passages.
    width, height = 7, 5
    grid = generate(width, height, rng=random.Random(7))
    passages = 0
    for y in range(height):
        for x in range(width):
            if not grid[y][x]["E"] and x + 1 < width:
                passages += 1
            if not grid[y][x]["S"] and y + 1 < height:
                passages += 1
    assert passages == width * height - 1


def test_render_has_expected_shape():
    grid = generate(3, 2, rng=random.Random(0))
    output = render(grid)
    lines = output.split("\n")
    assert len(lines) == 2 * 2 + 1
    for line in lines:
        assert len(line) == 4 * 3 + 1
