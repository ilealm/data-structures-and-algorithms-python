
from dsa.challenges.quick_sort.quick_sort import quick_sort


def test_quick_sort_one():
    array = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]

    actual = quick_sort(array, 0, len(array)-1)

    assert actual == expected

def test_quick_sort_two():
    array = []
    expected = []

    actual = quick_sort(array, 0, 0)

    assert actual == expected

def test_quick_sort_tre():
    array = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]

    actual = quick_sort(array, 0, len(array)-1)

    assert actual == expected


def test_quick_sort_four():
    array = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]

    actual = quick_sort(array, 0, len(array)-1)

    assert actual == expected

def test_quick_sort_five():
    array = ['d','e','a','f','i']
    expected = ['a','d','e','f','i']

    actual = quick_sort(array, 0, len(array)-1)

    assert actual == expected
