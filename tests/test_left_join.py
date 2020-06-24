import pytest
from dsa.challenges.left_join.left_join import left_join
from dsa.challenges.hashtable.hashtable import Hashtable

def test_left_join_one(dummy_hashtable_one, dummy_hashtable_two):
    expected =['outfit, garb, None', 'fond, enamored, averse', 'wrath, anger, deligth', 'guide, usher, follow', 'diligent, employed, idle']

    actual = left_join(dummy_hashtable_one, dummy_hashtable_two)

    assert actual == expected, 'Error creating left-join with two hashtables.'


def test_left_join_two(dummy_hashtable_one):
    expected =['outfit, garb, None', 'fond, enamored, None', 'wrath, anger, None', 'guide, usher, None', 'diligent, employed, None']

    actual = left_join(dummy_hashtable_one, Hashtable(15))

    assert actual == expected, 'Error creating left-join with one empty hastable.'


def test_left_join_tree():
    expected =[]

    actual = left_join(Hashtable(15), Hashtable(15))

    assert actual == expected, 'Error creating left-join with two empty hastables.'


def test_left_join_four(dummy_hashtable_one):
    tbl = Hashtable(15)
    tbl.add('guide','follow')
    tbl.add('flow','jam')
    expected =['outfit, garb, None', 'fond, enamored, None', 'wrath, anger, None', 'guide, usher, follow', 'diligent, employed, None']

    actual = left_join(dummy_hashtable_one, tbl)

    assert actual == expected, 'Error creating left-join with two hastables.'

@pytest.fixture
def dummy_hashtable_one():
    tbl = Hashtable(15)
    tbl.add('fond','enamored')
    tbl.add('wrath','anger')
    tbl.add('diligent','employed')
    tbl.add('outfit','garb')
    tbl.add('guide','usher')
    return tbl


@pytest.fixture
def dummy_hashtable_two():
    tbl = Hashtable(10)
    tbl.add('fond','averse')
    tbl.add('wrath','deligth')
    tbl.add('diligent','idle')
    tbl.add('guide','follow')
    tbl.add('flow','jam')
    return tbl
