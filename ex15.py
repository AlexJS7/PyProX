# Exercise 15 - Median

"""
If you put a list of numbers into sorted order, the median number is the number at the halfway point.

The median of an odd-length list is the number in the middlemost number when the list is in sorted order.
The median of an even length list is the average of the two middlemost numbers when the list is in sorted order.

Outliers can cause the statistical average to be much higher or smaller than the majority of numbers,
so that the median number may give you a better idea of the characteristics of the numbers in the list.
"""

import random


def median(numbers):
    if not isinstance(numbers, list):
        return numbers

    if len(numbers) == 0:
        return None

    if len(numbers) == 1:
        return numbers[0]

    numbers_len = len(numbers)
    sorted_numbers = sorted(numbers)

    if numbers_len % 2 == 0:
        idx1 = int(numbers_len / 2)
        print(idx1)
        return (sorted_numbers[idx1] + sorted_numbers[idx1 - 1]) / 2

    return sorted_numbers[numbers_len // 2]


assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6
