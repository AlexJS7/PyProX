# Exercise 7 - ASCII Table

"""
ASCII stands for American Standard Code for Information Interchange. 

Computers can only store numbers, so each letter, numeral, punctuation mark,
and every other character is assigned a number called a code point.

However, ASCII is an old and somewhat limited standard: it doesn't have numbers assigned for
Cyrillic or Chinese characters, for example.
And it is an American standard: it has a code point for the dollar sign (code point 36) but not the British pound sign.

ASCII is no longer enough now that the internet has made global communication commonplace.

The newer Unicode character set provides code points for every character and is what Python uses for
its string values.
Unicode's code points are backward compatible with ASCII, so we can still easily use Python to display an ASCII table.

`print_ASCII_table()` fn displays ASCII number and its corresponding text character,
from 32 to 126. (These are called the printable ASCII characters.)
"""


def print_ASCII_table():
    for n in range(32, 127):
        print(n, ' ', chr(n))


print_ASCII_table()
