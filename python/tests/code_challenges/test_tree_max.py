import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_negatives():
    tree = BinaryTree()
    tree.root = Node(-37)
    tree.root.left = Node(-42)
    tree.root.right = Node(-7)
    tree.root.left.left = Node(-66)
    tree.root.right.right = Node(-314)

    actual = tree.find_maximum_value()
    expected = -7

    assert actual == expected
