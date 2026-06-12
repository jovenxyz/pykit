import pytest

from bipartite import is_bipartite, two_colour


def test_empty_graph():
    assert two_colour([], []) == {}
    assert is_bipartite([], [])


def test_single_node():
    assert two_colour(["A"], []) == {"A": 0}


def test_simple_bipartite_path():
    nodes = ["A", "B", "C", "D"]
    edges = [("A", "B"), ("B", "C"), ("C", "D")]
    colour = two_colour(nodes, edges)
    assert colour is not None
    for u, v in edges:
        assert colour[u] != colour[v]


def test_even_cycle_is_bipartite():
    nodes = list(range(4))
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    assert is_bipartite(nodes, edges)


def test_odd_cycle_is_not_bipartite():
    nodes = list(range(3))
    edges = [(0, 1), (1, 2), (2, 0)]
    assert not is_bipartite(nodes, edges)
    assert two_colour(nodes, edges) is None


def test_disconnected_components():
    assert is_bipartite(
        ["A", "B", "C", "D"],
        [("A", "B"), ("C", "D")],
    )


def test_disconnected_with_one_odd_cycle():
    nodes = ["A", "B", "C", "D", "E"]
    edges = [("A", "B"), ("C", "D"), ("D", "E"), ("E", "C")]
    assert not is_bipartite(nodes, edges)


def test_unknown_node_in_edge_raises():
    with pytest.raises(ValueError):
        two_colour(["A"], [("A", "B")])
