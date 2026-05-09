# Exercise 31 - Integers To Strings

DIGITS = '0123456789'


def convert_int_to_str(integer_num: int) -> str:
    """
    Convert an integer to its string representation without using str().

    Parameters:
        integer_num (int): The integer to convert (e.g. 42 -> '42').

    Returns:
        str: The string representation of the integer.

    Raises:
        TypeError: If integer_num is not an int.
    """

    if not isinstance(integer_num, int):
        raise TypeError('integer_num must be an integer')

    if integer_num == 0:
        return '0'

    abs_integer_num = abs(integer_num)
    digits = []

    while abs_integer_num != 0:
        digits.append(DIGITS[abs_integer_num % 10])
        abs_integer_num = abs_integer_num // 10

    if integer_num < 0:
        digits.append('-')

    return ''.join(reversed(digits))


for i in range(-10000, 10000):
    assert convert_int_to_str(i) == str(i)
