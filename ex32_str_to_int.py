# Exercise 32 -  Strings to Integers

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def convert_str_to_int(string_num: str) -> int:
    """
    Convert a string to its integer representation without using int().

    Parameters:
        string_num (str): The string to convert (e.g. '42' -> 42).

    Returns:
        int: Parsed integer value.

    Raises:
        TypeError: If string_num is not a str.
        ValueError: If string_num is empty or contains invalid characters.
    """

    if not isinstance(string_num, str):
        raise TypeError('string_num must be a string')

    if not string_num or '.' in string_num:
        raise ValueError(
            'string_num must not be empty nor contain a decimal point.'
        )

    if string_num == '0':
        return 0

    is_negative = string_num[0] == '-'
    if is_negative:
        string_num = string_num[1:]

    if not string_num:
        raise ValueError(
            'string_num must contain digits.'
        )

    result = 0

    for char in string_num:
        try:
            result = result * 10 + DIGITS[char]
        except KeyError:
            raise ValueError(f'invalid character: {char!r}') from None

    return -result if is_negative else result


for i in range(-10000, 10000):
    assert convert_str_to_int(str(i)) == i
