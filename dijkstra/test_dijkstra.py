import pytest

from dijkstra import shortest_distances, shortest_path


GRAPH = {
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {},
}


def test_distances_from_source():
    assert shortest_distances(GRAPH, "A") == {"A": 0, "B": 1, "C": 3, "D": 4}


def test_unreachable_nodes_excluded():
    graph = {"A": {"B": 1}, "B": {}, "C": {"D": 1}, "D": {}}
    distances = shortest_distances(graph, "A")
    assert "C" not in distances
    assert "D" not in distances


def test_shortest_path_basic():
    assert shortest_path(GRAPH, "A", "D") == ["A", "B", "C", "D"]


def test_shortest_path_to_self():
    assert shortest_path(GRAPH, "A", "A") == ["A"]


def test_shortest_path_no_route_returns_none():
    graph = {"A": {"B": 1}, "B": {}, "C": {}}
    assert shortest_path(graph, "A", "C") is None


def test_negative_weights_raise():
    graph = {"A": {"B": -1}, "B": {}}
    with pytest.raises(ValueError):
        shortest_distances(graph, "A")
    with pytest.raises(ValueError):
        shortest_path(graph, "A", "B")


def test_isolated_source():
    assert shortest_distances({"A": {}}, "A") == {"A": 0}


def test_missing_source_treated_as_isolated():
    assert shortest_distances({"A": {"B": 1}}, "Z") == {"Z": 0}
