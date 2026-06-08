import pytest

from toposort import CycleError, topological_sort


def _is_valid_order(order, edges):
    position = {node: i for i, node in enumerate(order)}
    return all(
        u in position and v in position and position[u] < position[v]
        for u, v in edges
    )


def test_linear_chain():
    edges = [("a", "b"), ("b", "c"), ("c", "d")]
    assert topological_sort(edges) == ["a", "b", "c", "d"]


def test_diamond_is_a_valid_order():
    edges = [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")]
    order = topological_sort(edges)
    assert _is_valid_order(order, edges)
    assert set(order) == {"a", "b", "c", "d"}


def test_isolated_node_via_nodes_argument():
    edges = [("a", "b")]
    order = topological_sort(edges, nodes=["z"])
    assert set(order) == {"a", "b", "z"}
    assert _is_valid_order(order, edges)


def test_cycle_raises():
    with pytest.raises(CycleError):
        topological_sort([("a", "b"), ("b", "c"), ("c", "a")])


def test_self_loop_raises():
    with pytest.raises(CycleError):
        topological_sort([("a", "a")])


def test_empty_input():
    assert topological_sort([]) == []
    assert topological_sort([], nodes=["x", "y"]) == ["x", "y"]


def test_disconnected_components():
    edges = [("a", "b"), ("c", "d")]
    order = topological_sort(edges)
    assert _is_valid_order(order, edges)
    assert set(order) == {"a", "b", "c", "d"}


def test_works_with_arbitrary_hashable_items():
    edges = [(1, 2), ((3, 4), 5)]
    order = topological_sort(edges)
    assert _is_valid_order(order, edges)
