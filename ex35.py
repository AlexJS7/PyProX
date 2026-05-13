# Exercise 35 - Title Case

import random


def get_title_case(text: str) -> str:
    """
    Convert every word in text to title case where every word
    in the string begins with an uppercase letter: (e.g. 'hola!' -> 'Hola!').

    The remaining letters are lowercase.

    Non-letter characters (not only spaces,) separate words in the string,
    so 'Hello5World' and 'Hello@World' also have two words.

    Examples:
        'Hello, world!' -> 'Hello, World!'
        'HELLO' -> 'Hello'
        'hElLo' -> 'Hello'
        'ab123xy' -> 'Ab123Xy'

    Restricted Methods:
        - str.title()
        - str.split()

    Parameters:
        text (str): String to convert to title case.

    Returns:
        str: String converted to title case.

    Raises:
        TypeError: If text is not a str.
    """

    if not isinstance(text, str):
        raise TypeError(f'text must be a str, got {type(text).__name__}')

    # todo

    return ''


assert get_title_case('Hello, world!') == 'Hello, World!'
assert get_title_case('HELLO') == 'Hello'
assert get_title_case('hello') == 'Hello'
assert get_title_case('hElLo') == 'Hello'
assert get_title_case('') == ''
assert get_title_case('abc123xyz') == 'Abc123Xyz'
assert get_title_case('cat dog RAT') == 'Cat Dog Rat'
assert get_title_case('cat,dog,RAT') == 'Cat,Dog,Rat'

random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')

for i in range(1000):
    random.shuffle(chars)
    assert get_title_case(''.join(chars)) == ''.join(chars).title()
