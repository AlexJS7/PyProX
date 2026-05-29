# Exercise 41 - ROT 13 Encryption

"""
    ROT 13 is a simple encryption cipher. The name ROT 13 is short for ―rotate 13.‖ It encrypts by
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


def rot13(text: str) -> str:
    """
    Encrypt text with by ROT13 algorithm.
    Case sensitive.
    Non-letter characters are left unencrypted.

    Args:
        text: A str to encrypt.

    Returns:
        Encrypted text.

    Example:
        rot13('HELLO, world!') → 'URYYB, jbeyq!'
    """

    pass
