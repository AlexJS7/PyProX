# Exercise 19 - Password Generator

"""
A dictionary attack is when hackers program their computers to repeatedly try
logging in with every word in the dictionary as the password. A dictionary attack won't work if you
use randomly generated passwords. They may not be easy to remember, but they make hacking your
accounts more difficult.
"""

import random

LOWER_LETTERS = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
UPPER_LETTERS = LOWER_LETTERS.upper()
NUMBERS = ''.join(str(i) for i in range(0, 10))
SPECIAL = '~!@#$%^&*()_+'


def generate_password(length: int) -> str:
    """
    Generates random password.
    ___________
    Parameters:
        length (int):
            Number of characters of generated password. 
    ___________
    Returns:
        out (str):
            Randomly generated password which includes at least
                - one lowercase letter
                - one uppercase letter
                - one number
                - one special character: ~!@#$%^&*()_+
    """

    allowed_char_groups = (LOWER_LETTERS, UPPER_LETTERS, NUMBERS, SPECIAL)

    allowed_char_groups_len = len(allowed_char_groups)

    min_password_length = 12

    final_length = length

    if (not isinstance(length, float) and not isinstance(length, int)) or length < min_password_length:
        final_length = min_password_length
    elif isinstance(length, float):
        final_length = round(length)

    result = []

    for i in range(0, final_length):
        group_idx = i % allowed_char_groups_len
        group_chars_len = len(allowed_char_groups[group_idx])
        rand_char = allowed_char_groups[group_idx][random.randint(
            0, group_chars_len - 1)]
        result.append(rand_char)

    random.shuffle(result)

    return ''.join(result)


assert len(generate_password(8)) == 12
pw = generate_password(14)
assert len(pw) == 14

hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
