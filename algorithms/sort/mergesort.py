
def merge(l_left, l_right):
    merged = []
    l_index = r_index = 0
    while l_index < len(l_left) and r_index < len(l_right):
        if l_left[l_index] < l_right[r_index]:
            merged.append(l_left[l_index])
            l_index += 1
        else:
            merged.append(l_right[r_index])
            r_index += 1
    merged += l_left[l_index:]
    merged += l_right[r_index:]
    return merged


def mergesort(a_list):
    """
    The Merge sort algorithm is based on a divide and conquer strategy. The algorithm involves splitting
    the lists by half till we have just lists with one element. Then, we rearrange the smaller chunks comparing
    them with the other ones that we've splitted. So if we have [1, 3] and [2, 4] we compare 1 to 2, then 2 to 3,
    then 3 to 4.
    .. example::
        original list: [3, 5, 1, 4, 2]
        1st split: [3, 5], [1, 4, 2] (it doesn't matter where we split, it could be [3, 5, 1], [4, 2] as well).
        2nd split: [3], [5], [1], [4, 2]
        3rd split: [3], [5], [1], [4], [2]
        ... now we reconstruct
        1st reconstruct: [3, 5], [1, 4], [2]
        2nd reconstruct: [3, 5], [1, 2, 4]
        3rd reconstruct: [1, 2, 3, 4, 5]
    .. best case:: n logn.
    .. worst case:: n logn.
    :param a_list: a list with numbers.
    :return: a list with the elements sorted (asc -> desc).
    """
    half = int(len(a_list) / 2)
    if len(a_list) <= 1:
        return a_list

    left = mergesort(a_list[:half])
    right = mergesort(a_list[half:])
    return merge(left, right)
