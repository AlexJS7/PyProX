# Exercise 41 - ROT 13 Encryption

"""
    ROT 13 is a simple encryption cipher. The name ROT 13 is short for rotate 13. It encrypts by
    replacing letters with letters that appear 13 characters down the alphabet: A is replaced with N, B is
    replaced with O, C is replaced with P, and so on. If this rotation of 13 letters goes passed the end of
    the alphabet, it ―wraps around‖ the Z and continues from the start of the alphabet. Thus, X is
    replaced with K, Y is replaced with L, Z is replaced with M, and so on. Non-letter characters are left
    unencrypted.

    ABCDEFGHIJKLM
    NOPQRSTUVWXYZ
    
    The benefit of ROT 13 is that you can decrypt the encrypted text by running it through ROT 13
    encryption again. This rotates the letter 26 times, returning us to the original letter. So ―Hello, world!‖
    encrypts to ―Uryyb, jbeyq!‖ which in turn encrypts to ―Hello, world!‖ There is no decryption
    algorithm; you decrypt encrypted text by encrypting it again. The ROT 13 algorithm isn't secure for
    real-world cryptography. But it can be used to obfuscate text to prevent spoiling joke punch lines or
    puzzle solutions.
"""

from string import ascii_lowercase


def rot13_char(char: str) -> str:
    """Return the ROT13-transformation of a lowercase ASCII letter."""
    return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))


def rot13(text: str) -> str:
    """
    Apply the ROT13 cipher to a string.

    Only ASCII letters A-Z and a-z are transformed.
    ASCII letters are rotated by 13 positions.
    Letter case is preserved.
    Non-letter chars are left unchanged.

    Args:
        text: Input string.

    Returns:
        The ROT13-transformed string.

    Raises:
        TypeError: If text is not a str.

    Examples:
        >>> rot13('HELLO, world!')
        'URYYB, jbeyq!'
    """

    if not isinstance(text, str):
        raise TypeError(f'text must be str, got {type(text).__name__}')

    result = []

    for char in text:
        lower_char = char.lower()

        if lower_char not in ascii_lowercase:
            result.append(char)
            continue

        encrypted = rot13_char(lower_char)
        result.append(encrypted.upper() if char.isupper() else encrypted)

    return ''.join(result)


assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
