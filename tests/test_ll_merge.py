import pytest
from dsa.challenges.linked_list.linked_list import LinkedList, Node
from dsa.challenges.ll_merge.ll_merge import merge_list

def test_merge_list_same_lenght(dummy_LinkedList_a, dummy_LinkedList_b):
    actual = str(merge_list(dummy_LinkedList_a,dummy_LinkedList_b))
    expected = "A -> 1 -> B -> 2 -> C -> 3 -> None"
    assert actual == expected, "Error on ziping two lilnked list of the same lenght."


def test_merge_list_diff_lenght(dummy_LinkedList_a):
    dummy_LinkedList_b = LinkedList()
    dummy_LinkedList_b.insert("1")
    actual = str(merge_list(dummy_LinkedList_a,dummy_LinkedList_b))
    expected = "A -> 1 -> B -> C -> None"
    assert actual == expected, "Error on ziping two lilnked list of different lenght."

def test_merge_list_empty_list():
    actual = str(merge_list(LinkedList(),LinkedList()))
    expected = "None"
    assert actual == expected, "Error on ziping two empty lilnked list."

def test_merge_list_empty_list(dummy_LinkedList_a):
    actual = str(merge_list(dummy_LinkedList_a,LinkedList()))
    expected = "A -> B -> C -> None"
    assert actual == expected, "Error on ziping two empty lilnked list."


@pytest.fixture
def dummy_LinkedList_a():
    ll = LinkedList()
    ll.insert("C")
    ll.insert("B")
    ll.insert("A")
    return ll

@pytest.fixture
def dummy_LinkedList_b():
    ll = LinkedList()
    ll.insert("3")
    ll.insert("2")
    ll.insert("1")
    return ll
