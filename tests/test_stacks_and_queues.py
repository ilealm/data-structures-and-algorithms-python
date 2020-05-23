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

def test_node_push_one():
    # Given
    expected_value = 'One'
    expected_next = None
    stack_ele = Stack()
    # When
    stack_ele.push("One")
    # Then
    actual_value = stack_ele.top.value
    actual_next = stack_ele.top.next
    assert actual_value == expected_value, "Error on pushing one node. Value should match the constructor."
    assert actual_next == expected_next, "Error on pushing one node. Next should be None for the first node."
