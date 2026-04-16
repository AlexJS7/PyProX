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

print(LOWER_LETTERS, UPPER_LETTERS, NUMBERS)


def generate_password(length: int) -> str:
    """
    Generates random password.
    ___________
    Parameters:
        length (int):
            Number of characters the generated password should have. 
    ___________
    Returns:
        out (str):
            Randomly generated password which includes at least
                - one lowercase letter
                - one uppercase letter
                - one number
                - one special character: ~!@#$%^&*()_+
    """

    min_password_length = 12
    final_length = length

    if (not isinstance(length, float) and not isinstance(length, int)) or length < min_password_length:
        final_length = min_password_length
    elif isinstance(length, float):
        final_length = round(length)

    result = ''

    for i in range(0, final_length + 1):
        # every fourth takes special
        if i % 4 == 0:
            random_idx = random.randint(0, len(SPECIAL))

        # every third takes number
            random_idx = random.randint(0, len(NUMBERS))

        # todo


# assert len(generate_password(8)) == 12
# pw = generate_password(14)
# assert len(pw) == 14
# hasLowercase = False
# hasUppercase = False
# hasNumber = False
# hasSpecial = False
# for character in pw:
#  if character in LOWER_LETTERS:
#     hasLowercase = True
#  if character in UPPER_LETTERS:
#     hasUppercase = True
#  if character in NUMBERS:
#     hasNumber = True
#  if character in SPECIAL:
#     hasSpecial = True
# assert hasLowercase and hasUppercase and hasNumber and hasSpecial
