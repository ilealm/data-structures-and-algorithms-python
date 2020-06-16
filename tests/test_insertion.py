
from dsa.challenges.insertion.insertion import insertion

def test_insertion_one():
    array = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]

    actual = insertion(array)

    assert actual == expected

def test_insertion_two():
    array = []
    expected = []

    actual = insertion(array)

    assert actual == expected

def test_insertion_tre():
    array = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]

    actual = insertion(array)

    assert actual == expected


def test_insertion_four():
    array = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]

    actual = insertion(array)

    assert actual == expected

def test_insertion_five():
    array = ['d','e','a','f','i']
    expected = ['a','d','e','f','i']

    actual = insertion(array)

    assert actual == expected
