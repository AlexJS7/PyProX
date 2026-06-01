# Exercise 42 - Bubble Sort

"""
    Bubble sort is often the first sorting algorithm taught to computer science students.
    While it is too inefficient for use in real-world software, the algorithm is easy to understand.

    The bubble sort algorithm compares every pair of indexes and swaps their values so that the
    larger value comes later in the list. As the algorithm runs, the larger numbers "bubble up" towards the
    end, hence the algorithm's name.

    Note: While it can quickly sort lists of a few dozen or few hundred values,
    it becomes infeasible for sorting lists of thousands or millions of values.
    For this reason, real-world applications never use bubble sort.
"""


def bubble_sort(numbers: list[int | float]) -> list[int | float]:
    """
    Sort a list in ascending order in place.

    Args:
        numbers: List of numbers.

    Returns:
        The same list object, sorted in ascending order.

    Raises:
        TypeError: If numbers is not a list.

    Notes:
        This function modifies the input list directly.
        The built-in sort() and sorted() functions are not used.
    """

    if not isinstance(numbers, list):
        raise TypeError(
            f'numbers must be a list, got {type(numbers).__name__}')

    length = len(numbers)

    if length < 2:
        return numbers

    for i in range(length - 1):
        swapped = False

        for j in range(length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


assert bubble_sort([]) == []
assert bubble_sort([1]) == [1]
assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort([-3, 10, -1, 5]) == [-3, -1, 5, 10]
