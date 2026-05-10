# Exercise 33 - Comma-formatted Numbers

"""
    In the US and UK, the digits of numbers are grouped with
    commas every three digits.

    For example, the number 79033516 is written as 79,033,516 for readability.
"""


def comma_format(n: int | float) -> str:
    """
    Format a number with commas as thousands separators.

    Preserves decimal digits if present.

    Examples:
        1234 -> '1,234'
        1234567.89 -> '1,234,567.89'
        -5000 -> '-5,000'

    Parameters:
        n (int | float): The number to format (e.g. 1234 -> '1,234').

    Returns:
        str: Formatted string value.

    Raises:
        TypeError: If n is neither int nor float.
    """

    if not isinstance(n, (int, float)):
        raise TypeError('number must be either int or float')

    def build_result(str_num: str, decimal_str: str, is_negative: bool) -> str:
        """Add decimal part and make it negative if needed."""
        if decimal_str:
            str_num += '.' + decimal_str
        if is_negative:
            str_num = '-' + str_num
        return str_num

    str_num = str(n)

    is_negative = str_num[0] == '-'
    if is_negative:
        str_num = str_num[1:]

    decimal_str = ''
    if '.' in str_num:
        str_num, decimal_str = str_num.split('.')

    if len(str_num) < 4:
        return build_result(str_num, decimal_str, is_negative)

    divider_count = (len(str_num) - 1) // 3

    digits = list(str_num)

    for i in range(divider_count, 0, -1):
        digits.insert(-3 * i, ',')

    return build_result(''.join(digits), decimal_str, is_negative)


assert comma_format(1) == '1'
assert comma_format(10) == '10'
assert comma_format(100) == '100'
assert comma_format(1000) == '1,000'
assert comma_format(10000) == '10,000'
assert comma_format(100000) == '100,000'
assert comma_format(1000000) == '1,000,000'
assert comma_format(1234567890) == '1,234,567,890'
assert comma_format(1000.123456) == '1,000.123456'
assert comma_format(-5123) == '-5,123'
assert comma_format(-5123.45) == '-5,123.45'
