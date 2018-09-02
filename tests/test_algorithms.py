import random

from algorithms.sort.bubblesort import bubblesort


def test_bubble_sort():
    list_size = random.randint(1, 100)
    unsorted_list = []
    for _ in range(0, list_size):
        unsorted_list.append(random.randint(1, 999))
    assert bubblesort(unsorted_list) == sorted(unsorted_list)
