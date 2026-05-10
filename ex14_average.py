# Exercise 14 - Average

"""
Averages are an essential statistical tool, and computers make it easy to calculate the average of
millions or billions of numbers.

The average is the sum of a set of the numbers divided by the amount
of numbers.
"""

import random


def average(numbers):
    if not isinstance(numbers, list):
        return numbers

    if len(numbers) == 0:
        return None

    if len(numbers) == 1:
        return numbers[0]

    total = numbers[0]

    for i, n in enumerate(numbers):
        if i == 0:
            continue

        total += n

    return total / len(numbers)


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2
