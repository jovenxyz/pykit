from pytoolkit.structures.min_heap import MinHeap


def test_pop_returns_ascending():
    heap = MinHeap()
    for value in (5, 1, 3, 2, 4):
        heap.push(value)
    assert [heap.pop() for _ in range(5)] == [1, 2, 3, 4, 5]
