import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_single_positive():
    assert longest_positive_streak([1]) == 1

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_zeros():
    assert longest_positive_streak([0, 0, 0]) == 0

def test_mixed_positive_and_negative():
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3

def test_mixed_with_zeros():
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6, 7]) == 3

def test_streak_at_the_end():
    assert longest_positive_streak([-1, 0, 1, 2, 3]) == 3

def test_streak_at_the_beginning():
    assert longest_positive_streak([1, 2, 3, 0, -1]) == 3

def test_long_list():
    assert longest_positive_streak([1] * 100 + [-1] + [1] * 50) == 100

def test_provided_example():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
