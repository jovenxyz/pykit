import pytest

from kruskal import minimum_spanning_tree, total_weight


def test_simple_triangle():
    nodes = ["A", "B", "C"]
    edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3)]
    tree = minimum_spanning_tree(nodes, edges)
    assert total_weight(tree) == 3
    assert len(tree) == 2


def test_skips_cycle_creating_edge():
    nodes = ["A", "B", "C"]
    edges = [
        ("A", "B", 1),
        ("B", "C", 1),
        ("A", "C", 100),         # would close a cycle, skip
    ]
    tree = minimum_spanning_tree(nodes, edges)
    assert total_weight(tree) == 2
    assert ("A", "C", 100) not in tree


def test_disconnected_graph_returns_forest():
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B", 1), ("C", "D", 2)]
    tree = minimum_spanning_tree(nodes, edges)
    assert sorted(tree) == sorted([("A", "B", 1), ("C", "D", 2)])


def test_no_edges_for_single_node():
    assert minimum_spanning_tree(["A"], []) == []


def test_unknown_node_in_edge_raises():
    with pytest.raises(ValueError):
        minimum_spanning_tree(["A", "B"], [("A", "X", 1)])


def test_classic_example():
    nodes = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B", 1), ("A", "C", 7),
        ("B", "C", 5), ("B", "D", 4),
        ("C", "D", 6), ("C", "E", 3),
        ("D", "E", 2),
    ]
    tree = minimum_spanning_tree(nodes, edges)
    assert total_weight(tree) == 10        # 1 + 2 + 3 + 4
    assert len(tree) == 4
