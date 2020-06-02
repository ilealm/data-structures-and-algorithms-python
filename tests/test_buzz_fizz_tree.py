import pytest
from dsa.challenges.buzz_fizz_tree.buzz_fizz_tree import Node, Queue, BinarySearchTree, BinaryTree

def test_FizzBuzzTree_empty_tree():
    # given
    bst = BinaryTree()
    expected = "The Tree is empty."
    # when
    actual =  bst.FizzBuzzTree(None)
    # then
    assert actual == expected, 'Error trying to execute FizzBuzzTree method. The tree is empty.'


def test_FizzBuzzTree_one_buzz_node():
    # given
    bst = BinarySearchTree()
    bst.add(25)
    expected = ['Buzz']
    # when
    new_tree = bst.FizzBuzzTree(bst)
    actual = new_tree.inOrder()
    # then
    assert actual == expected, 'Error trying to execute FizzBuzzTree method. The value should be Buzz.'

def test_FizzBuzzTree_one_fizz_node():
    # given
    bst = BinarySearchTree()
    bst.add(3)
    expected = ['Fizz']
    # when
    new_tree = bst.FizzBuzzTree(bst)
    actual = new_tree.inOrder()
    # then
    assert actual == expected, 'Error trying to execute FizzBuzzTree method. The value should be Fizz.'

def test_FizzBuzzTree_one_fizzbuzz_node():
    # given
    bst = BinarySearchTree()
    bst.add(30)
    expected = ['FizzBuzz']
    # when
    new_tree = bst.FizzBuzzTree(bst)
    actual = new_tree.inOrder()
    # then
    assert actual == expected, 'Error trying to execute FizzBuzzTree method. The value should be FizzBuzz.'


def test_FizzBuzzTree_fizzbuzz_tree(dummy_bst_seven_nodes):
    # given
    bst = BinarySearchTree()
    expected = ['Buzz', 'Buzz', 'Fizz', '19', 'FizzBuzz', 'FizzBuzz', '41']
    # when
    new_tree = bst.FizzBuzzTree(dummy_bst_seven_nodes)
    actual = new_tree.preOrder()
    # then
    assert actual == expected, 'Error trying to execute FizzBuzzTree method.'



@pytest.fixture
def dummy_bst_seven_nodes():
    bst = BinarySearchTree()
    bst.add(25)
    bst.add(10)
    bst.add(30)
    bst.add(3)
    bst.add(19)
    bst.add(15)
    bst.add(41)
    return bst
