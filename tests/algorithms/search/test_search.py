import pytest

from algorithms.search.binarysearch import binary_search


def test_binary_search_last():
    assert binary_search([1, 3, 5, 7], 7) == 7


def test_binary_search_first():
    assert binary_search([1, 3, 5, 7], 1) == 1


def test_binary_search_middle():
    assert binary_search([1, 3, 4, 5, 7], 4) == 4


def test_binary_search_not_found():
    with pytest.raises(ValueError):
        binary_search([1, 3], 5)


def test_binary_search_empty():
    with pytest.raises(ValueError):
        binary_search([], 1)
