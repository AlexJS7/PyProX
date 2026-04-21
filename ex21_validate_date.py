# Exercise 21 - Validate Date


"""
We can represent a date with three integers for the year, month, and day, but this doesn't mean
that any integers represent a valid date. There is no 13th month of the year or 32nd day of any
month. This exercise has you check if a year/month/day combination is valid, given that different
months have different numbers of days
"""

import datetime
from ex20_leap_year import is_leap_year


def is_valid_date(year: int, month: int, day: int) -> bool:
    """
    Return True if the integers provided for the parameters represent a valid date, otherwise False.

    Parameters:
        year (int): The year to check.
        month (int): The month to check.
        day (int): The day to check.

    Returns:
        bool: True if the parameters represent a valid date, otherwise False.
    """

    if not isinstance(year, int):
        raise TypeError('year must be an integer')
    if not isinstance(month, int):
        raise TypeError('month must be an integer')
    if not isinstance(day, int):
        raise TypeError('day must be integer')

    if day < 1 or month < 1 or month > 12:
        return False

    if month == 2:
        return day <= (29 if is_leap_year(year) else 28)

    if month in (4, 6, 9, 11):
        return day <= 30

    return day <= 31


assert is_valid_date(1999, 12, 31) == True
assert is_valid_date(2000, 2, 29) == True
assert is_valid_date(2001, 2, 29) == False
assert is_valid_date(2029, 13, 1) == False
assert is_valid_date(1000000, 1, 1) == True
assert is_valid_date(2015, 4, 31) == False
assert is_valid_date(1970, 5, 99) == False
assert is_valid_date(1981, 0, 3) == False
assert is_valid_date(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert is_valid_date(d.year, d.month, d.day) == True
    d += oneDay
