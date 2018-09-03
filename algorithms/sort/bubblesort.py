
def bubblesort(a_list):
    """
    The Bubble sort algorithm is the most naive one that we can create. The idea around this algorithm
    is comparing each two elements on the list and swapping them in case one is bigger than the other.
    If any swap is executed, we need to rerun it, since these swapped elements might need to be swapped
    again.
    .. example::
        original list: [3, 5, 1, 4, 2]
        1st round: [3, 1, 4, 2, 5]
        2nd round: [1, 3, 2, 4, 5]
        3rd round: [1, 2, 3, 4, 5]
    .. best case::
        O(N)
        If the list is already sorted, we pass it once and since no swap will happen, we return it as is.
    .. worst case::
        O(N^2)
        If the list is inverted (e.g. [4, 3, 2, 1]) we need to pass the N elements N times.
        original list: [4, 3, 2, 1]
        1st round: [3, 2, 1, 4]
        2nd round: [2, 1, 3, 4]
        3rd round: [1, 2, 3, 4]
        So we can see that its the number of elements (N) times the number of swaps (N-1). N^2-1 rounds.
    :param a_list: a list with numbers.
    :return: a list with the elements sorted (asc -> desc).
    """
    updated = False
    for i in range(0, len(a_list) - 1):
        if a_list[i] > a_list[i + 1]:
            a_list[i + 1], a_list[i] = a_list[i], a_list[i + 1]
            updated = True
    return a_list if not updated else bubblesort(a_list)
