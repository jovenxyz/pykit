from astar import euclidean, find_path, manhattan


def test_heuristic_helpers():
    assert manhattan((0, 0), (3, 4)) == 7
    assert euclidean((0, 0), (3, 4)) == 5.0


def test_straight_path_on_open_grid():
    grid = [[0] * 5 for _ in range(5)]
    path = find_path(grid, (0, 0), (4, 0))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (4, 0)
    assert len(path) == 5


def test_routes_around_obstacle():
    # Wall down x = 2 with a gap at the top row.
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    path = find_path(grid, (0, 2), (4, 2))
    assert path is not None
    assert path[0] == (0, 2)
    assert path[-1] == (4, 2)
    for x, y in path:
        assert grid[y][x] == 0


def test_no_path_when_walled_off():
    grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    assert find_path(grid, (0, 0), (4, 0)) is None


def test_start_or_goal_blocked_returns_none():
    grid = [[0, 1], [0, 0]]
    assert find_path(grid, (1, 0), (0, 1)) is None       # start blocked
    assert find_path(grid, (0, 0), (1, 0)) is None       # goal blocked


def test_start_equals_goal():
    grid = [[0] * 3 for _ in range(3)]
    assert find_path(grid, (1, 1), (1, 1)) == [(1, 1)]


def test_diagonal_movement_takes_shorter_path():
    grid = [[0] * 5 for _ in range(5)]
    straight = find_path(grid, (0, 0), (4, 4))
    diagonal = find_path(grid, (0, 0), (4, 4), diagonal=True)
    assert straight is not None and diagonal is not None
    assert len(diagonal) < len(straight)


def test_empty_grid_returns_none():
    assert find_path([], (0, 0), (0, 0)) is None
    assert find_path([[]], (0, 0), (0, 0)) is None
