# Exercise 9 - Chess Square Color

"""
A chess board has a checker-pattern of white and black tiles.
In this program, we'll determine a pattern to the color of the squares
based on their column and row.
"""


def get_chess_square_color(col, row):
    if not (1 <= col <= 8) or not (1 <= row <= 8):
        return ''

    if col % 2 == row % 2:
        return 'white'
    else:
        return 'black'


assert get_chess_square_color(0, 8) == ''
assert get_chess_square_color(2, 9) == ''

assert get_chess_square_color(1, 1) == 'white'
assert get_chess_square_color(2, 1) == 'black'
assert get_chess_square_color(3, 1) == 'white'
assert get_chess_square_color(4, 1) == 'black'
assert get_chess_square_color(5, 1) == 'white'
assert get_chess_square_color(6, 1) == 'black'
assert get_chess_square_color(7, 1) == 'white'
assert get_chess_square_color(8, 1) == 'black'

assert get_chess_square_color(1, 2) == 'black'
assert get_chess_square_color(2, 2) == 'white'
assert get_chess_square_color(3, 2) == 'black'
assert get_chess_square_color(4, 2) == 'white'
assert get_chess_square_color(5, 2) == 'black'
assert get_chess_square_color(6, 2) == 'white'
assert get_chess_square_color(7, 2) == 'black'
assert get_chess_square_color(8, 2) == 'white'

assert get_chess_square_color(1, 3) == 'white'
assert get_chess_square_color(2, 3) == 'black'
assert get_chess_square_color(3, 3) == 'white'
assert get_chess_square_color(4, 3) == 'black'
assert get_chess_square_color(5, 3) == 'white'
assert get_chess_square_color(6, 3) == 'black'
assert get_chess_square_color(7, 3) == 'white'
assert get_chess_square_color(8, 3) == 'black'

assert get_chess_square_color(1, 4) == 'black'
assert get_chess_square_color(2, 4) == 'white'
assert get_chess_square_color(3, 4) == 'black'
assert get_chess_square_color(4, 4) == 'white'
assert get_chess_square_color(5, 4) == 'black'
assert get_chess_square_color(6, 4) == 'white'
assert get_chess_square_color(7, 4) == 'black'
assert get_chess_square_color(8, 4) == 'white'

assert get_chess_square_color(1, 5) == 'white'
assert get_chess_square_color(2, 5) == 'black'
assert get_chess_square_color(3, 5) == 'white'
assert get_chess_square_color(4, 5) == 'black'
assert get_chess_square_color(5, 5) == 'white'
assert get_chess_square_color(6, 5) == 'black'
assert get_chess_square_color(7, 5) == 'white'
assert get_chess_square_color(8, 5) == 'black'

assert get_chess_square_color(1, 6) == 'black'
assert get_chess_square_color(2, 6) == 'white'
assert get_chess_square_color(3, 6) == 'black'
assert get_chess_square_color(4, 6) == 'white'
assert get_chess_square_color(5, 6) == 'black'
assert get_chess_square_color(6, 6) == 'white'
assert get_chess_square_color(7, 6) == 'black'
assert get_chess_square_color(8, 6) == 'white'

assert get_chess_square_color(1, 7) == 'white'
assert get_chess_square_color(2, 7) == 'black'
assert get_chess_square_color(3, 7) == 'white'
assert get_chess_square_color(4, 7) == 'black'
assert get_chess_square_color(5, 7) == 'white'
assert get_chess_square_color(6, 7) == 'black'
assert get_chess_square_color(7, 7) == 'white'
assert get_chess_square_color(8, 7) == 'black'

assert get_chess_square_color(1, 8) == 'black'
assert get_chess_square_color(2, 8) == 'white'
assert get_chess_square_color(3, 8) == 'black'
assert get_chess_square_color(4, 8) == 'white'
assert get_chess_square_color(5, 8) == 'black'
assert get_chess_square_color(6, 8) == 'white'
assert get_chess_square_color(7, 8) == 'black'
assert get_chess_square_color(8, 8) == 'white'
