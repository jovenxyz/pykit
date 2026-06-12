import math

import pytest

from floyd import shortest_paths


def test_triangle():
    nodes = ["A", "B", "C"]
    edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 10)]
    dist = shortest_paths(nodes, edges)
    assert dist["A"]["A"] == 0
    assert dist["A"]["B"] == 1
    assert dist["A"]["C"] == 3       # via B
    assert dist["B"]["C"] == 2


def test_unreachable_is_infinity():
    nodes = ["A", "B", "C"]
    edges = [("A", "B", 1)]
    dist = shortest_paths(nodes, edges)
    assert math.isinf(dist["B"]["A"])
    assert math.isinf(dist["A"]["C"])


def test_self_distance_zero():
    nodes = ["A", "B"]
    edges = [("A", "B", 1)]
    dist = shortest_paths(nodes, edges)
    assert dist["A"]["A"] == 0
    assert dist["B"]["B"] == 0


def test_negative_weight_cycle_raises():
    with pytest.raises(ValueError):
        shortest_paths(["A", "B"], [("A", "B", 1), ("B", "A", -2)])


def test_negative_weight_no_cycle_ok():
    nodes = ["A", "B", "C"]
    edges = [("A", "B", 4), ("A", "C", 5), ("B", "C", -3)]
    dist = shortest_paths(nodes, edges)
    assert dist["A"]["C"] == 1       # A -> B -> C: 4 + (-3) = 1


def test_duplicate_nodes_raise():
    with pytest.raises(ValueError):
        shortest_paths(["A", "A"], [])


def test_empty_graph():
    assert shortest_paths([], []) == {}


def test_single_node():
    assert shortest_paths(["A"], []) == {"A": {"A": 0}}
