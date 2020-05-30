import pytest
from dsa.challenges.tree.tree import BinaryTree, BinarySearchTree

def test_bst_create_root():
    # given
    bst = BinarySearchTree()
    expected = "The root is empty."
    # when
    actual = bst.__str__()
    # then
    assert actual == expected, 'Error creating an empty Binary Search Tree.'

def test_bst_add_root():
    # given
    bst = BinarySearchTree()
    expected = "The root is 100"
    # when
    bst.add(100)
    actual = bst.__str__()
    # then
    assert actual == expected, 'Error creating the root of the Binary Search Tree.'

def test_bst_add_child():
    # given
    bst = BinarySearchTree()
    expected = [50,100,120]
    # when
    bst.add(100)
    bst.add(50)
    bst.add(120)
    actual = bst.inOrder()
    # then
    assert actual == expected, 'Error adding child left and right to the root of the Binary Search Tree.'



# s
#
