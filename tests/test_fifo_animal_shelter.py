import pytest
from dsa.challenges.fifo_animal_shelter.fifo_animal_shelter import Animal, AnimalShelter

def test_animal_create_one():
    # Given
    expected = "Cat"
    # When
    node_ele = Animal("Cat")
    actual = node_ele.kind
    # Then
    assert actual == expected, "Error creating one Animal."


def test_queue_create_queue():
    expected = "The rear is None and the front is None"

    que = AnimalShelter()
    actual = que.__str__()

    assert actual == expected, "Error creating an instance of a Queue."

def test_queue_enqueue_one():
    que = AnimalShelter()
    expected = "Cat"

    que.enqueue("Cat")
    actual = que.peek()

    assert actual == expected, "Error inserting one first value to the Queue."

def test_queue_enqueue_multiple(dummy_three_animals_queue):
    expected = "Cat"

    actual = dummy_three_animals_queue.peek()

    assert actual == expected, "Error inserting multiple first value to the Queue."



def test_queue_dequeue_three(dummy_three_animals_queue):
    expected = "Cat"

    actual = dummy_three_animals_queue.dequeue('Cat')
    actual = dummy_three_animals_queue.dequeue('Cat')
    actual = dummy_three_animals_queue.dequeue('Dog')

    assert actual == expected, "Error on dequeue all the values from the Queue."



def test_queue_dequeue_not_cat_or_dog(dummy_three_animals_queue):
    expected = None

    actual = dummy_three_animals_queue.dequeue('Horse')

    assert actual == expected, "Error on method peek when the Queue have nodes."



@pytest.fixture
def dummy_three_animals_queue():
    ah = AnimalShelter()
    ah.enqueue("Cat")
    ah.enqueue("Dog")
    ah.enqueue("Cat")
    return ah
