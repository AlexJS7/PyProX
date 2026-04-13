# Exercise 16 - Mode

"""
 The mode is the number that appears most frequently in a list of numbers. 
"""

import random


def mode(numbers: list[float | int]) -> float | int | None:
    """Finds the mode value from the provided list of numbers."""
    if not isinstance(numbers, list):
        return numbers

    if len(numbers) == 0:
        return None

    if len(numbers) == 1:
        return numbers[0]

    num_count_mapping = {}

    for n in numbers:
        if n in num_count_mapping.keys():
            num_count_mapping[n] += 1
        else:
            num_count_mapping[n] = 1

    return sorted(
        num_count_mapping.items(),
        key=lambda a: a[1],
        reverse=True
    )[0][0]


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1

random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(100):
    random.shuffle(testData)
    assert mode(testData) == 4
