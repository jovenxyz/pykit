import pytest

from pytoolkit.structures.stack import Stack


def test_push_and_pop_is_lifo():
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_peek_does_not_remove():
    stack: Stack[int] = Stack()
    stack.push(42)
    assert stack.peek() == 42
    assert len(stack) == 1


def test_pop_empty_raises():
    with pytest.raises(IndexError):
        Stack().pop()
