# Exercise 10 - Find & Replace

"""
Find-and-replace is a standard feature in text editors, IDEs, and word processor software. Even
the Python language comes with a replace() string method since programs often use it. In this
exercise, we will reimplement this common string operation.
"""


def find_and_replace(text, old_text, new_text):
    if text == old_text:
        return new_text

    if old_text not in text:
        return text

    result = ''
    text_len = len(text)
    old_text_len = len(old_text)

    i = 0
    while i < text_len:
        if text[i] == old_text[0] and text[i:i + old_text_len] == old_text:
            result += new_text
            i += old_text_len
        else:
            result += text[i]
            i += 1

    return result


assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
