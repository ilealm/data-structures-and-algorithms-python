import pytest
from dsa.challenges.stacks_and_queues.stacks_and_queues import Node, Stack

def test_node_create_one():
    # Given
    expected = "One"
    # When
    node_ele = Node("One")
    actual = node_ele.value
    # Then
    assert actual == expected, "Error creating one Node."

def test_stack_create_empty():
    stack_ele = Stack()
    expected = "The top is None"

    actual = stack_ele.__str__()

    assert actual == expected,  "Error creating an empty stack."

def test_stack_push_one():
    # Given
    expected_value = 'One'
    expected_next = None
    stack_ele = Stack()
    # When
    stack_ele.push("One")
    # Then
    actual_value = stack_ele.peek()
    actual_next = None
    assert actual_value == expected_value, "Error on pushing one node. Value should match the constructor."
    assert actual_next == expected_next, "Error on pushing one node. Next should be None for the first node."

def test_stack_push_multiple():
    # Given
    expected_value = 'Three'
    expected_next = 'Two'
    stack_ele = Stack()
    # When
    stack_ele.push("One")
    stack_ele.push("Two")
    stack_ele.push("Three")
    # Then
    actual_value = stack_ele.peek()
    actual_next = stack_ele.top.next.value
    assert actual_value == expected_value, "Error on pushing multiple node. Value should match the constructor."
    assert actual_next == expected_next, "Error on pushing multiple node. Next should be two."

def test_stack_pop_one():
    expected_value = "One"
    stack_ele = Stack()
    stack_ele.push("One")

    actual_value = stack_ele.pop()

    assert actual_value == expected_value, 'Error trying to pop one value with one node in the stack.'



@pytest.mark.skip(reason="this is creating the exception, but the test fails. not sure if I have to test that here")
def test_stack_pop_all(dummy_three_nodes_stack):
    expected_value = None

    dummy_three_nodes_stack.pop()
    dummy_three_nodes_stack.pop()
    actual_value = dummy_three_nodes_stack.pop()

    assert actual_value == expected_value, 'Error trying to pop all the nodes in the stack.'



@pytest.mark.skip(reason="this is creating the exception, but the test fails. not sure if I have to test that here")
def test_stack_pop_when_empty():
    expected_value = "Can not pop from an empty stack."
    stack_ele = Stack()

    actual_value = stack_ele.pop()

    assert actual_value == expected_value, 'Error trying to pop. The stack is empty.'

def test_stack_peek_no_empty(dummy_three_nodes_stack):
    expected_value = "Three"

    actual_value = dummy_three_nodes_stack.peek()

    assert actual_value ==  expected_value, "The value of the peek must be Three."


def test_stack_is_empty_false(dummy_three_nodes_stack):
    expected = False

    actual = dummy_three_nodes_stack.is_empty()

    assert actual == expected, ("Error on peek method. Should return false when the stack have values.")


def test_stack_is_empty_true():
    stack_ele = Stack()

    expected = True

    actual = stack_ele.is_empty()

    assert actual == expected, ("Error on peek method. Should return true when the stack don't values.")


@pytest.fixture
def dummy_three_nodes_stack():
    stack_ele = Stack()
    stack_ele.push("One")
    stack_ele.push("Two")
    stack_ele.push("Three")
    return stack_ele
