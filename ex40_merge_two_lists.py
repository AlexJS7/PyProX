# Exercise 40 - Merging Two Sorted Lists

"""
    One of the most efficient sorting algorithms is the merge sort algorithm.
    Merge sort has two phases: the dividing phase and the merge phase.
"""


def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merge two sorted lists in ascending order.

    Args:
        list1: A list sorted in ascending order.
        list2: A list sorted in ascending order.

    Returns:
        A merged sorted list.

    Example:
        merge_two_lists([1, 3, 6], [5, 7, 8, 9]) → [1, 3, 5, 6, 7, 8, 9]

    Note:
        sorted() is forbidden to use.
    """

    if not list1 and not list2:
        return []
    if not list2:
        return list1[:]
    if not list1:
        return list2[:]

    result = []

    len1 = len(list1)
    len2 = len(list2)
    idx1 = 0
    idx2 = 0

    while idx1 < len1 and idx2 < len2:
        a = list1[idx1]
        b = list2[idx2]

        if a <= b:
            result.append(a)
            idx1 += 1
        else:
            result.append(b)
            idx2 += 1

    result.extend(list1[idx1:])
    result.extend(list2[idx2:])

    return result


assert merge_two_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert merge_two_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_two_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_two_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert merge_two_lists([1, 2, 3], []) == [1, 2, 3]
assert merge_two_lists([], [1, 2, 3]) == [1, 2, 3]
