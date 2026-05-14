# Exercise 35 - Title Case

import random


def get_title_case(text: str) -> str:
    """
    Convert text to title case where each word starts with
    an uppercase letter and remaining letters are lowercase ('hOlA!' -> 'Hola!').

    Non-letter characters (not only spaces) separate words in the string,
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
        str: The title-cased string.

    Raises:
        TypeError: If text is not a str.
    """

    if not isinstance(text, str):
        raise TypeError(f'text must be a str, got {type(text).__name__}')

    if text == '':
        return ''

    chars = []
    new_word = True

    for char in text:
        if char.isalpha():
            chars.append(char.upper() if new_word else char.lower())
            new_word = False
        else:
            chars.append(char)
            new_word = True

    return ''.join(chars)


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
