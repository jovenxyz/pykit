from pytoolkit.algorithms.graph import bfs, dfs

GRAPH = {1: [2, 3], 2: [4], 3: [4], 4: []}


def test_bfs_order():
    assert bfs(GRAPH, 1) == [1, 2, 3, 4]


def test_dfs_order():
    assert dfs(GRAPH, 1) == [1, 2, 4, 3]
