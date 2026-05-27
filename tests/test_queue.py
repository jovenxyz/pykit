import pytest

from pytoolkit.structures.queue import Queue


def test_enqueue_dequeue_is_fifo():
    queue: Queue[int] = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_dequeue_empty_raises():
    with pytest.raises(IndexError):
        Queue().dequeue()
