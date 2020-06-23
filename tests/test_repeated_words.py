import pytest
from dsa.challenges.repeated_words.repeated_words import count_words

def test_count_one():
    text = ""
    actual = count_words(text)

    expected = {}

    assert actual == expected, 'Error trying to obtain the word count of an empty string..'

def test_count_two():
    text = "Once upon a time, there was a brave princess who..."
    actual = count_words(text)

    expected = {'Once': 1, 'upon': 1, 'a': 2, 'time': 1, 'there': 1, 'was': 1, 'brave': 1, 'princess': 1, 'who': 1}

    assert actual == expected, 'Error trying to obtain the word count of a text.'


def test_count_three():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = count_words(text)

    expected = {'It': 1, 'was': 11, 'the': 14, 'best': 1, 'of': 12, 'times': 2, 'it': 9, 'worst': 1, 'age': 2, 'wisdom': 1, 'foolishness': 1, 'epoch': 2, 'belief': 1, 'incredulity': 1, 'season': 2, 'Light': 1, 'Darkness': 1, 'spring': 1, 'hope': 1, 'winter': 1, 'despair': 1, 'we': 4, 'had': 2, 'everything': 1, 'before': 2, 'us': 2, 'nothing': 1, 'were': 2, 'all': 2, 'going': 2, 'direct': 2, 'to': 1, 'Heaven': 1, 'other': 1, 'way': 1, '–': 1, 'in': 2, 'short': 1, 'period': 2, 'so': 1, 'far': 1, 'like': 1, 'present': 1, 'that': 1, 'some': 1, 'its': 2, 'noisiest': 1, 'authorities': 1, 'insisted': 1, 'on': 1, 'being': 1, 'received': 1, 'for': 2, 'good': 1, 'or': 1, 'evil': 1, 'superlative': 1, 'degree': 1, 'comparison': 1, 'only': 1}

    assert actual == expected, 'Error trying to obtain the word count of a text.'


def test_count_four():
    text = "It"
    actual = count_words(text)

    expected = {'It': 1}

    assert actual == expected, 'Error trying to obtain the word count of a one word.'
