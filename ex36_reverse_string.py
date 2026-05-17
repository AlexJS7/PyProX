# Exercise 35 - Reverse string

"""
    Strings are immutable in the Python language, meaning you can't modify
    their characters the way you can modify the items in a list.

    For example, if you tried to change 'Rat' to 'Ram'
    with the assignment statement 'Rat'[2] = 'm',
    you would receive a TypeError: 'str' object does not support
    item assignment error message.
    On the other hand, if you store a string 'Rat' in a variable named animal,
    the assignment statement animal = 'Ram' isn't modifying the 'Rat' string
    but rather making animal refer to an entirely new string, 'Ram'.
"""


def reverse_string(text: str) -> str:
    """
    Return `text` reversed.

    Restricted approach:
        text[::-1]

    Parameters:
        text (str): String to reverse.

    Returns:
        str: Reversed string.

    Raises:
        TypeError: If text is not a str.
    """

    if not isinstance(text, str):
        raise TypeError(f'text must be a str, got {type(text).__name__}')

    return ''.join(text[i] for i in range(len(text) - 1, -1, -1))


assert reverse_string('Hello') == 'olleH'
assert reverse_string('') == ''
assert reverse_string('aaazzz') == 'zzzaaa'
assert reverse_string('xxxx') == 'xxxx'
