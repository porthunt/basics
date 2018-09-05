
def binary_search(a_list: list, n: int) -> int:
    """
    The Binary Search algorithm is a search algorithm that looks splits
    the list into smaller ones till it finds the element.
    .. example::
        original list: [1, 3, 6, 10, 16], n=1
        1st split: [1, 3, 6]
        2nd split: [1, 3]
        3rd split: [1] <- found
    .. best case:: O(1). 'n' is exactly in the middle of the list.
    .. worst case:: O(logn). 'n' is the first or last element of the list.
    :param a_list: a sorted list of elements.
    :param n: the element 'n' that you want to find on the list.
    :return: the element itself.
    :raise ValueError: in case the element was not found.
    """
    half = len(a_list) // 2

    if a_list and a_list[half] == n:
        return a_list[half]
    if len(a_list) == 1 or not a_list:
        raise ValueError

    if a_list[half] > n:
        return binary_search(a_list[:half], n)
    elif a_list[half] < n:
        return binary_search(a_list[half:], n)
