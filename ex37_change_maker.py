# Exercise 37 - Change Maker

"""
    American currency has coins in the denominations of 1 (pennies),
    5 (nickels), 10 (dimes), and 25 cents (quarters).
    
    Imagine that we were programming a cash register to dispense correct change.
"""


def make_change(amount: int) -> dict[str, int]:
    """
    Calculate the minimal number of US coins for a given amount of change.

    Examples:
        make_change(5) -> {'nickels': 1}
        make_change(10) -> {'dimes': 1}
        make_change(30) -> {'quarters': 1, 'nickels': 1}

    Parameters:
        amount (int): The amount of change in cents.

    Returns:
        dict[str, int]: 
            A dictionary mapping coin names to their counts.
            Coins with a count of 0 are omitted.

    Raises:
        TypeError: If amount is not an int.
        ValueError: If amount is less than 1.
    """

    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError(f'amount must be an int, got {type(amount).__name__}')

    if amount < 1:
        raise ValueError('amount must be greater than 0.')

    coins = (
        ('quarters', 25),
        ('dimes', 10),
        ('nickels', 5),
        ('pennies', 1),
    )

    result = {}

    for k, v in coins:
        count, amount = divmod(amount, v)

        if count:
            result[k] = count

        if amount == 0:
            break

    return result


assert make_change(30) == {'quarters': 1, 'nickels': 1}
assert make_change(10) == {'dimes': 1}
assert make_change(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert make_change(100) == {'quarters': 4}
assert make_change(125) == {'quarters': 5}
