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
    Sets each value in the list to a random index,
    as a result shuffling the values list mutating it in place.

    The exercise implements a fn identical to Python's random.shuffle().

    Parameters:
        values (list): The list of values to shuffle.

    Returns:
        None: 
            The function changes the values list in place.

    Raises:
        TypeError: If values is not a list.
    """

    if not isinstance(list):
        raise TypeError(f'values must be a list, got {type(values).__name__}')

    if not values:
        return values

    # todo: implement shuffle fn
    return values


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
