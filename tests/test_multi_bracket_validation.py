import pytest
from dsa.challenges.multi_bracket_validation.multi_bracket_validation import Node, Stack, Validator

def test_validator_one_word():
    # Given
    expected = True
    val = Validator()
    # When
    string = 'code_fellows'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a valid string."


def test_validator_valid_closing_brackets():
    # Given
    expected = True
    val = Validator()
    # When
    string = '(((code_fellows)))'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a valid pairs of brackets ."

def test_validator_valid_closing_brackets_two():
    # Given
    expected = True
    val = Validator()
    # When
    string = '([code_]fellows)[]'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a valid pairs of brackets ."


def test_validator_not_valid_closing_brackets_one():
    # Given
    expected = False
    val = Validator()
    # When
    string = '([code_fellows)[]'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a not valid pairs of brackets ."

def test_validator_not_valid_closing_brackets_two():
    # Given
    expected = False
    val = Validator()
    # When
    string = '([code_fellows]'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a not valid pairs of brackets ."

def test_validator_not_valid_closing_brackets_tree():
    # Given
    expected = False
    val = Validator()
    # When
    string = 'code ([fellows'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a not valid pairs of brackets ."

def test_validator_not_valid_closing_brackets_four():
    # Given
    expected = False
    val = Validator()
    # When
    string = 'code fellows)'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a not valid pairs of brackets ."

def test_validator_not_valid_closing_brackets_five():
    # Given
    expected = False
    val = Validator()
    # When
    string = 'code} fellows'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a not valid pairs of brackets ."

def test_validator_not_valid_closing_brackets_six():
    # Given
    expected = False
    val = Validator()
    # When
    string = '(code} {fellows]'
    actual = val.multi_bracket_validation(string)
    # Then
    assert actual == expected, "Error validating a not valid pairs of brackets ."
