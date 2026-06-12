import pytest

from tarjan import strongly_connected_components


def _normalize(components):
    return sorted([sorted(c) for c in components])


def test_single_node():
    assert strongly_connected_components(["A"], []) == [["A"]]


def test_simple_cycle():
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    assert _normalize(strongly_connected_components(nodes, edges)) == [
        ["A", "B", "C"]
    ]


def test_dag_each_node_alone():
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C")]
    assert _normalize(strongly_connected_components(nodes, edges)) == [
        ["A"], ["B"], ["C"]
    ]


def test_classic_example():
    nodes = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B"), ("B", "C"), ("C", "A"),    # {A, B, C} cycle
        ("C", "D"),
        ("D", "E"), ("E", "D"),                  # {D, E} cycle
    ]
    assert _normalize(strongly_connected_components(nodes, edges)) == [
        ["A", "B", "C"], ["D", "E"]
    ]


def test_returns_in_reverse_topological_order():
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("B", "C"), ("C", "B"), ("C", "D")]
    result = strongly_connected_components(nodes, edges)
    flat = [sorted(c) for c in result]
    assert flat[0] == ["D"]
    assert flat[1] == ["B", "C"]
    assert flat[2] == ["A"]


def test_disconnected_graph():
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("C", "D")]
    assert _normalize(strongly_connected_components(nodes, edges)) == [
        ["A"], ["B"], ["C"], ["D"]
    ]


def test_unknown_node_in_edge_raises():
    with pytest.raises(ValueError):
        strongly_connected_components(["A"], [("A", "B")])
