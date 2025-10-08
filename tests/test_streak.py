# tests/test_streak.py
import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 1, 1]) == 3
    assert longest_positive_streak([5]) == 1

def test_single_zero_or_negative_breaks():
    assert longest_positive_streak([1, 2, 0, 3]) == 2
    assert longest_positive_streak([1, -1, 2, 3]) == 2

def test_multiple_streaks_choose_longest():
    # two streaks: length 2 and length 3 -> returns 3
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_negatives_edgecases():
    assert longest_positive_streak([0, 0, 0]) == 0
    assert longest_positive_streak([-1, -2, -3]) == 0
    assert longest_positive_streak([1, 2, 0, -1, 3, 4, 5, 0, 6]) == 3

def test_longer_and_longer():
    assert longest_positive_streak([1,2,3,0,1,2,3,4,0,1]) == 4

def test_mixed_values():
    assert longest_positive_streak([1, -1, 1, -1, 1]) == 1
