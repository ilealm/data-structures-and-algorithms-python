import pytest
from dsa.challenges.tree.tree import BinarySearchTree
from dsa.challenges.tree_intersection.tree_intersection import tree_intersection



def test_tree_intersection_empty():
    # given
    expected = []
    # when
    actual = tree_intersection(BinarySearchTree(), BinarySearchTree())
    # then
    assert actual == expected, 'Error obtaining the values of empty trees.'


def test_tree_intersection_one(dummy_bst_six_nodes_v1,dummy_bst_six_nodes_v2):
    # given
    expected = [100, 125, 160, 350, 200, 500, 175]
    # when
    actual = tree_intersection(dummy_bst_six_nodes_v1, dummy_bst_six_nodes_v2)
    # then
    assert actual == expected, 'Error obtaining the values in both trees.'


def test_tree_intersection_duplicated(dummy_bst_six_nodes_v1,dummy_bst_six_nodes_v2):
    # given
    dummy_bst_six_nodes_v1.add(100)
    dummy_bst_six_nodes_v1.add(100)
    dummy_bst_six_nodes_v1.add(100)
    expected = [100, 125, 160, 350, 200, 500, 175]
    # when
    actual = tree_intersection(dummy_bst_six_nodes_v1, dummy_bst_six_nodes_v2)
    # then
    assert actual == expected, 'Error obtaining the values in both trees.'


def test_tree_intersection_no_duplicates(dummy_bst_six_nodes_v1):
    # given
    expected = []
    # when
    actual = tree_intersection(dummy_bst_six_nodes_v1, BinarySearchTree())
    # then
    assert actual == expected, 'Error obtaining the values where there are not duplicates.'



def test_tree_intersection_one_duplicates(dummy_bst_six_nodes_v1):
    # given
    dummy_bst_six_nodes_v1.add(1000)
    dummy_bst_six_nodes_v2 = BinarySearchTree()
    dummy_bst_six_nodes_v2.add(1000)
    expected = [1000]
    # when
    actual = tree_intersection(dummy_bst_six_nodes_v1,dummy_bst_six_nodes_v2 )
    # then
    assert actual == expected, 'Error obtaining the values where there only one duplicate.'



@pytest.fixture
def dummy_bst_six_nodes_v1():
    tree = BinarySearchTree()
    tree.add(150)
    tree.add(100)
    tree.add(250)
    tree.add(75)
    tree.add(160)
    tree.add(200)
    tree.add(350)
    tree.add(125)
    tree.add(175)
    tree.add(300)
    tree.add(500)
    return tree

@pytest.fixture
def dummy_bst_six_nodes_v2():
    tree = BinarySearchTree()
    tree.add(42)
    tree.add(100)
    tree.add(600)
    tree.add(15)
    tree.add(160)
    tree.add(200)
    tree.add(350)
    tree.add(125)
    tree.add(175)
    tree.add(4)
    tree.add(500)
    return tree
