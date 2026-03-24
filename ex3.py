# Exercise 3 - Odd & Even

def is_odd(n):
    if isinstance(n, float):
        return False

    return n % 2 == 1


def is_even(n):
    if isinstance(n, float):
        return False

    return n % 2 == 0


assert is_odd(42) == False
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False
