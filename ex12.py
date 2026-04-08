# Exercise 12 - Smallest & Biggest

"""
Python's built-in `min()` and `max()` functions return the smallest and biggest numbers in a list of
numbers passed, respectively.

In this exercise, we will reimplement the behavior of these functions.
"""


def get_smallest_or_biggest(numbers, is_smallest=True):
    if not isinstance(numbers, list):
        return numbers

    if len(numbers) == 0:
        return None

    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]

    for i, n in enumerate(numbers):
        if i == 0:
            continue
        if (is_smallest and n < result) or (not is_smallest and n > result):
            result = n

    return result


def get_smallest(numbers):
    return get_smallest_or_biggest(numbers, is_smallest=True)


def get_biggest(numbers):
    return get_smallest_or_biggest(numbers, is_smallest=False)


assert get_smallest([1, 2, 3]) == 1
assert get_smallest([3, 2, 1]) == 1
assert get_smallest([28, 25, 42, 2, 28]) == 2
assert get_smallest([1]) == 1
assert get_smallest([]) == None

assert get_biggest([1, 2, 3]) == 3
assert get_biggest([3, 2, 1]) == 3
assert get_biggest([28, 25, 42, 2, 28]) == 42
assert get_biggest([1]) == 1
assert get_biggest([]) == None
