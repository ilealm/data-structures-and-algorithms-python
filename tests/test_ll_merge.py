import pytest
from dsa.challenges.linked_list.linked_list import LinkedList, Node
from dsa.challenges.ll_merge.ll_merge import merge_list

def test_merge_list_same_lenght(dummy_LinkedList_a, dummy_LinkedList_b):
    actual = str(merge_list(dummy_LinkedList_a,dummy_LinkedList_b))
    expected = "A -> 1 -> B -> 2 -> C -> 3 -> None"
    assert actual == expected, "Error on ziping two lilnked list of the same lenght."


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
