# Exercise 39 - Collatz Sequence

"""
    The Collatz Sequence also called the 3n + 1 problem,
    is a simple but mysterious numeric sequence that has
    remained unsolved by mathematicians. It has four rules:
    - Begin with a positive, nonzero integer called n
    - If n is 1, the sequence terminates
    - If n is even, the next value of n is n / 2
    - If n is odd, the next value of n is 3n + 1

    Example: collatz(10) → [10, 5, 16, 8, 4, 2, 1]

    Mathematicians have been unable to prove if every starting integer
    eventually terminates. This gives the Collatz Sequence the description of
    "the simplest impossible math problem".
"""


import random


def collatz(n: int) -> list[int]:
    """
    Calculate the Collatz sequence of numbers for a given starting integer.

    The Collatz sequence has four rules:
    - Begin with a positive, nonzero integer called n
    - If n is 1, the sequence terminates
    - If n is even, the next value of n is n / 2
    - If n is odd, the next value of n is 3n + 1

    Example:
        collatz(10) → [10, 5, 16, 8, 4, 2, 1]

    Parameters:
        n (int): Starting number for Collatz sequence.

    Returns:
        list[int]:
            A list containing the Collatz sequence starting from n.

    Raises:
        TypeError: If n is not an int.
        ValueError: if n is not a positive, nonzero integer.
    """

    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f'n must be an int, got {type(n).__name__}')

    if n < 1:
        raise ValueError('n must be a positive, nonzero integer')

    result = [n]

    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        result.append(n)

    return result


assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123

random.seed(42)
for i in range(1000):
    n = random.randint(1, 10000)
    seq = collatz(n)
    # # Make sure the last integer is 1.
    assert seq[0] == n
    # Make sure it includes the starting number.
    assert seq[-1] == 1
