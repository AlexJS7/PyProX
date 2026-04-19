# Exercise 20 - Leap Year

"""
It takes about 365.25 days for the earth to revolve around the sun.
This slight offset would cause our 365-day calendar to become inaccurate over time.
Therefore, leap years have an extra day, February 29th.

A leap year occurs on all years divisible by four (e.g., 2016, 2020, 2024, and so on).
However, the exception to this rule is that years divisible by
 - one hundred (e.g., 2100, 2200, 2300, and so on) are NOT leap years.
 - four hundred (e.g., 2000, 2400, and so on) are leap years.
"""


def is_leap_year(year: int) -> bool:
    """
    Return True if the given year is a leap year, otherwise False.

    A leap year is divisible by 4, except for years divisible by 100
    unless they are also divisible by 400.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, otherwise False.
    """

    if not isinstance(year, int):
        raise TypeError('year must be an integer')

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0


assert is_leap_year(1999) == False
assert is_leap_year(2000) == True
assert is_leap_year(2001) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2400) == True
