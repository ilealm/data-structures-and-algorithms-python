import pytest
from dsa.challenges.linked_list.linked_list import LinkedList, Node


def test_LinkedList_one():
    actual = LinkedList()
    expected = None
    assert actual.head == expected

def test_LinkedList_two():
    ll = LinkedList()
    ll.insert("First")
    assert ll.head.value == "First"

def test_LinkedList_three(dummy_LinkedList):
    assert dummy_LinkedList.head.value == "Third"

def test_LinkedList_four(dummy_LinkedList):
    actual = dummy_LinkedList.includes("Five")
    assert actual == False

def test_LinkedList_five(dummy_LinkedList):
    actual = dummy_LinkedList.includes("First")
    assert actual


def test_LinkedList_six(dummy_LinkedList):
    actual = dummy_LinkedList.__str__()
    expected = "{ Third } -> { Second } -> { First } -> NULL"
    assert actual == expected

def test_LinkedList_six():
    ll = LinkedList()
    actual = ll.__str__()
    expected = "NULL"
    assert actual == expected

def test_append_one(dummy_LinkedList):
    dummy_LinkedList.append('Fourth')
    dummy_LinkedList.append('Fifth')
    actual = dummy_LinkedList.__str__()
    expected = "{ Third } -> { Second } -> { First } -> { Fourth } -> { Fifth } -> NULL"
    assert actual == expected


def test_insert_before_first_node():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert_before("Second", "Third")
    actual = ll.__str__()
    expected = "{ Third } -> { Second } -> { First } -> NULL"
    assert actual == expected

def test_insert_before_middle():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert_before("First", "1.5")
    actual = ll.__str__()
    expected = "{ Second } -> { 1.5 } -> { First } -> NULL"
    assert actual == expected


@pytest.fixture
def dummy_LinkedList():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert("Third")
    return ll

