import pytest
from dsa.challenges.tree.tree import BinarySearchTree

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


def test_bst_preOrder(dummy_bst_six_nodes):
    expected = [100,50,25,75,120,110]

    actual = dummy_bst_six_nodes.preOrder()

    assert actual == expected, 'Error on pre-order method.'



def test_bst_inOrder(dummy_bst_six_nodes):
    expected = [25,50,75,100,110,120]

    actual = dummy_bst_six_nodes.inOrder()

    assert actual == expected, 'Error on in-order method.'


def test_bst_postOrder(dummy_bst_six_nodes):
    expected = [25,75,50,110,120,100]

    actual = dummy_bst_six_nodes.postOrder()

    assert actual == expected, 'Error on post-order method.'


def test_bst_contains_false(dummy_bst_six_nodes):
    expected = False

    actual = dummy_bst_six_nodes.contains(200)

    assert actual == expected, 'Error on contains method. The value is not in the tree.'



def test_bst_contains_true(dummy_bst_six_nodes):
    expected = True

    actual = dummy_bst_six_nodes.contains(75)

    assert actual == expected, 'Error on contains method. The value is not in the tree.'


def test_bst_bread_first_traverse(dummy_bst_six_nodes):
    tree = BinarySearchTree()
    expected=[100,50,120,25,75,110]

    actual = tree.BreadthFirst(dummy_bst_six_nodes)

    assert actual == expected, 'Error on method BreadthFirst.'

def test_bst_bread_first_traverse_root():
    tree = BinarySearchTree()
    expected= 'The Tree is empty.'

    actual = tree.BreadthFirst(BinarySearchTree())

    assert actual == expected, 'Error on method BreadthFirst.'

def test_bst_bread_first_traverse_two_nodes():
    tree = BinarySearchTree()
    tree.add('orange')
    tree.add('purple')
    tree.add('red')
    tree.add('blue')
    expected = ['orange', 'blue', 'purple', 'red']

    tree_actual = BinarySearchTree()

    actual = tree_actual.BreadthFirst(tree)

    assert actual == expected, 'Error on method BreadthFirst.'

def test_bst_text_nodes():
    # given
    bst = BinarySearchTree()
    expected = ['Alice in WL', 'Great Expectations', 'Lord of the flies','Moby Dick', 'Pride and Prejudice', 'Robinson Crusoe',  'The Odyssey']
    # when
    bst.add('Moby Dick')
    bst.add('Great Expectations')
    bst.add('Robinson Crusoe')
    bst.add('Alice in WL')
    bst.add('Lord of the flies')
    bst.add('Pride and Prejudice')
    bst.add('The Odyssey')
    actual = bst.inOrder()
    # then
    assert actual == expected, 'Error creating a Binary Search Tree with text.'



@pytest.fixture
def dummy_bst_six_nodes():
    dst = BinarySearchTree()
    dst.add(100)
    dst.add(50)
    dst.add(120)
    dst.add(25)
    dst.add(110)
    dst.add(75)
    return dst

