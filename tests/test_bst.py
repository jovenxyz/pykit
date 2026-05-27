from pytoolkit.structures.binary_search_tree import BinarySearchTree


def test_inorder_is_sorted():
    tree = BinarySearchTree()
    for key in (5, 3, 8, 1, 4):
        tree.insert(key)
    assert tree.inorder() == [1, 3, 4, 5, 8]


def test_contains():
    tree = BinarySearchTree()
    tree.insert(10)
    assert tree.contains(10) is True
    assert tree.contains(99) is False
