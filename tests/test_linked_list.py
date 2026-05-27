from pytoolkit.structures.linked_list import LinkedList


def test_append_and_iterate():
    lst: LinkedList[int] = LinkedList()
    for value in (1, 2, 3):
        lst.append(value)
    assert list(lst) == [1, 2, 3]
    assert len(lst) == 3


def test_find():
    lst: LinkedList[int] = LinkedList()
    lst.append(7)
    assert lst.find(7) is True
    assert lst.find(8) is False
