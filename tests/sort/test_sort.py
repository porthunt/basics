import pytest
import random

from algorithms.sort.bubblesort import bubblesort
from algorithms.sort.mergesort import mergesort


@pytest.fixture
def random_list():
    return [random.randint(1, 999) for _ in range(0, random.randint(1, 100))]


def test_bubble_sort(random_list):
    assert bubblesort(random_list) == sorted(random_list)


def test_merge_sort(random_list):
    assert mergesort(random_list) == sorted(random_list)
