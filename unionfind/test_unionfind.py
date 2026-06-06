from unionfind import UnionFind


def test_add_creates_singleton():
    uf = UnionFind()
    uf.add(1)
    assert uf.find(1) == 1
    assert uf.size(1) == 1
    assert uf.components == 1


def test_add_is_idempotent():
    uf = UnionFind()
    uf.add(1)
    uf.add(1)
    assert uf.components == 1


def test_union_merges_components():
    uf = UnionFind()
    for item in (1, 2, 3, 4):
        uf.add(item)
    assert uf.union(1, 2) is True
    assert uf.union(3, 4) is True
    assert uf.components == 2
    assert uf.size(1) == 2


def test_union_returns_false_for_same_component():
    uf = UnionFind()
    uf.add(1)
    uf.add(2)
    uf.union(1, 2)
    assert uf.union(2, 1) is False


def test_connected():
    uf = UnionFind()
    uf.union(1, 2)
    uf.union(3, 4)
    assert uf.connected(1, 2)
    assert not uf.connected(1, 3)
    uf.union(2, 3)
    assert uf.connected(1, 4)


def test_find_adds_unknown_item():
    uf = UnionFind()
    assert uf.find("hello") == "hello"
    assert "hello" in uf


def test_size_reflects_unions():
    uf = UnionFind()
    for i in range(5):
        uf.add(i)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(0, 2)
    assert uf.size(3) == 4
    assert uf.size(4) == 1


def test_works_with_arbitrary_hashable_items():
    uf = UnionFind()
    uf.union("a", "b")
    uf.union((1, 2), (3, 4))
    assert uf.connected("a", "b")
    assert uf.connected((1, 2), (3, 4))
    assert not uf.connected("a", (1, 2))


def test_len_and_contains():
    uf = UnionFind()
    uf.add(1)
    uf.add(2)
    assert len(uf) == 2
    assert 1 in uf
    assert 3 not in uf
