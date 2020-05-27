import pytest
from dsa.challenges.queue_with_stacks.queue_with_stacks import PseudoCode


def test_enqueue_four(dummy_four_nodes_queue):
    expected = "The top is four -> three -> two -> one -> None"

    actual = dummy_four_nodes_queue.__str__()

    assert actual == expected, "Error on enqueue four values."


def test_dequeue_one(dummy_four_nodes_queue):
    expected = "one"

    actual = dummy_four_nodes_queue.dequeue()

    assert actual == expected, "Error on dequeue one value."

def test_dequeue_all(dummy_four_nodes_queue):
    expected = "four"

    dummy_four_nodes_queue.dequeue()
    dummy_four_nodes_queue.dequeue()
    dummy_four_nodes_queue.dequeue()
    actual = dummy_four_nodes_queue.dequeue()

    assert actual == expected, "Error on dequeue all values."

@pytest.fixture
def dummy_four_nodes_queue():
    pc = PseudoCode()
    pc.enqueue("one")
    pc.enqueue("two")
    pc.enqueue("three")
    pc.enqueue("four")
    return pc
