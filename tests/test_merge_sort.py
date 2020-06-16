
from dsa.challenges.merge_sort.merge_sort import merge_sort

def test_merge_sort_one():
    array = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]

    actual = merge_sort(array)

    assert actual == expected

def test_merge_sort_two():
    array = []
    expected = []

    actual = merge_sort(array)

    assert actual == expected

def test_merge_sort_tre():
    array = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]

    actual = merge_sort(array)

    assert actual == expected


def test_merge_sort_four():
    array = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]

    actual = merge_sort(array)

    assert actual == expected

def test_merge_sort_five():
    array = ['d','e','a','f','i']
    expected = ['a','d','e','f','i']

    actual = merge_sort(array)

    assert actual == expected
