# Exercise 17 - Dice Roll

"""
This exercise uses `random.randint` number generating fn to simulate rolling any number
of six-sided dice and returning the total sum of the dice roll.
"""

import random


def roll_dice(number_of_dice: int) -> int | None:
    """Simulates rolling any number of six-sided dice(s) and returning the total sum of the dice roll."""
    if not isinstance(number_of_dice, int):
        return None

    if number_of_dice == 0:
        return 0

    result = 0
    for _ in range(number_of_dice):
        result += random.randint(1, 6)

    return result


assert roll_dice(0) == 0
assert roll_dice(1000) != roll_dice(1000)

for i in range(1000):
    assert 1 <= roll_dice(1) <= 6
    assert 2 <= roll_dice(2) <= 12
    assert 3 <= roll_dice(3) <= 18
    assert 100 <= roll_dice(100) <= 600
