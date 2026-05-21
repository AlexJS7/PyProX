# Exercise 38 - Random Shuffle

"""
    A random shuffle algorithm puts the values in a list
    into a random order, like shuffling a deck of cards.
    
    This algorithm produces a new permutation, or ordering,
    of the values in the list. The algorithm works by looping over
    each value in the list and randomly determining a new index
    with which to swap it. As a result, the values in the list are in random order.
    
    For a list of n values, there are n! (n factorial‖) possible permutations.
    For example, a 10-value list has 10! or 10*9*8*7*6*5*4*3*2*1
    or 3,628,800 possible ways to order them.
"""

import random


def shuffle(values: list) -> None:
    """
    Shuffle a list in place using the Fisher-Yates algorithm.

    Note:
        random.shuffle() is forbidden to use.

    Parameters:
        values (list): List to shuffle.

    Raises:
        TypeError: If values is not a list.
    """

    if not isinstance(values, list):
        raise TypeError(f'values must be a list, got {type(values).__name__}')

    if not values:
        return None

    # The unbiased Fisher–Yates shuffle algorithm
    # guarantees every permutation is equally likely.
    for idx in range(len(values) - 1, 0, -1):
        rnd_idx = random.randint(0, idx)
        values[rnd_idx], values[idx] = values[idx], values[rnd_idx]

    return None


random.seed(42)
# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
