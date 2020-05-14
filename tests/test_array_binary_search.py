from dsa.challenges.array_binary_search.array_binary_search import binary_search

def test_binary_search_one():
    array = [10,20,30,40,50,60,70,80,90,100]
    key = 90
    actual = binary_search(array,key)
    expected = 8
    assert actual == expected

def test_binary_search_two():
    array = [10]
    key = 10
    actual = binary_search(array,key)
    expected = 0
    assert actual == expected

def test_binary_search_three():
    array = array = [10,20,30,40,50,60,70,80,90,100]
    key = 1
    actual = binary_search(array,key)
    expected = -1
    assert actual == expected

def test_binary_search_four():
    array = array = []
    key = 1
    actual = binary_search(array,key)
    expected = -1
    assert actual == expected


def test_binary_search_five():
    array = [10,20,30,40,50,60]
    key = 60
    actual = binary_search(array,key)
    expected = 5
    assert actual == expected
