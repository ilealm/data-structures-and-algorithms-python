import pytest
from dsa.challenges.hashtable.hashtable import Hashtable


def test_hashtable_hash():
    myTH = Hashtable(5)
    key = 'test'
    actual = myTH.hash(key)

    expected = myTH.hash(key)

    assert actual == expected, 'The hash should return the same value for the same index.'


def test_hashtable_create():
    myTH = Hashtable(5)
    actual = len(myTH.table)

    expected = 5

    assert actual == expected, 'The hash table should have 5 empty elements.'

def test_hashtable_add_one():
    myTH = Hashtable(5)
    key = 'First'
    value = '1'
    myTH.add(key, value)

    expected = '1'

    actual = myTH.get('First')

    assert actual == expected, 'Error adding one value.'

def test_hashtable_add_two():
    myTH = Hashtable(5)
    key = 'First'
    value = '1'
    myTH.add(key, value)
    key = 'Second'
    value = '2'
    myTH.add(key, value)

    expected = '1'

    actual = myTH.get('First')

    assert actual == expected, 'Error adding two values.'


def test_hashtable_add_colision():
    myTH = Hashtable(5)
    key = 'First'
    value = '1'
    myTH.add(key, value)
    key = 'Second'
    value = '2'
    myTH.add(key, value)
    key = 'dnoceS'
    value = '20'
    myTH.add(key, value)

    expected = '20'

    actual = myTH.get('dnoceS')

    assert actual == expected, 'Error adding in colision values.'



def test_hashtable_update_value():
    myTH = Hashtable(5)
    key = 'First'
    value = '1'
    myTH.add(key, value)
    key = 'Second'
    value = '2'
    myTH.add(key, value)
    key = 'dnoceS'
    value = '20'
    myTH.add(key, value)
    key = 'Second'
    value = 'the new value is 2nd'
    myTH.add(key, value)


    expected = 'the new value is 2nd'

    actual = myTH.get('Second')

    assert actual == expected, 'Error updating the value of an exiting key.'


def test_hashtable_get_value():
    myTH = Hashtable(5)
    key = 'First'
    value = '1'
    myTH.add(key, value)
    key = 'Second'
    value = '2'
    myTH.add(key, value)
    key = 'Third'
    value = '3'
    myTH.add(key, value)

    expected = '2'

    actual = myTH.get('Second')

    assert actual == expected, 'Error getting a value.'



def test_hashtable_get_value_with_colision():
    myTH = Hashtable(5)
    key = 'First'
    value = '1'
    myTH.add(key, value)
    key = 'Second'
    value = '2'
    myTH.add(key, value)
    key = 'dnoceS'
    value = '20'
    myTH.add(key, value)
    key = 'ondSec'
    value = '200'
    myTH.add(key, value)

    expected = '200'

    actual = myTH.get('ondSec')

    assert actual == expected, 'Error gettin the value from colisions.'
