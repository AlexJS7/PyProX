# Exercise 34 - Uppercase Letters

ASCII_LOWER_A = ord('a')
ASCII_LOWER_Z = ord('z')
ASCII_CASE_OFFSET = ASCII_LOWER_A - ord('A')

LOWER_TO_UPPER_CHAR_MAPPING = {
    chr(i): chr(i - ASCII_CASE_OFFSET)
    for i in range(ASCII_LOWER_A, ASCII_LOWER_Z + 1)
}


def get_uppercase(text: str) -> str:
    """
    Convert ASCII lowercase letters in a string to uppercase (e.g. 'hola!' -> 'HOLA!').

    This is a custom implementation of `str.upper()` for
    lowercase English ASCII letters only.

    Non-ASCII letters and non-letter characters remain unchanged.

    Examples:
        'Hello' -> 'HELLO'
        'goodbye 123!' -> 'GOODBYE 123!'
        'ñ' -> 'ñ'

    Parameters:
        text (str): String to convert to uppercase.

    Returns:
        str: String with ASCII lowercase letters converted to uppercase.

    Raises:
        TypeError: If text is not a str.
    """

    if not isinstance(text, str):
        raise TypeError(f'text must be a str, got {type(text).__name__}')

    return ''.join(
        LOWER_TO_UPPER_CHAR_MAPPING.get(char, char)
        for char in text
    )


assert get_uppercase('Hello') == 'HELLO'
assert get_uppercase('hello') == 'HELLO'
assert get_uppercase('HELLO') == 'HELLO'
assert get_uppercase('Hello, world!') == 'HELLO, WORLD!'
assert get_uppercase('goodbye 123!') == 'GOODBYE 123!'
assert get_uppercase('12345') == '12345'
assert get_uppercase('!hola mundo!') == '!HOLA MUNDO!'
assert get_uppercase('') == ''
assert get_uppercase('.') == '.'
