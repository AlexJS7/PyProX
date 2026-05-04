# Exercise 29 - Pyramid Drawing


def draw_pyramid(height: int, char: str = '#') -> str:
    """
    Return a centered pyramid pattern as a string.

    Each row consists of a repeated character forming a centered pyramid shape.

    Parameters:
        height (int): Number of rows in the pyramid (must be between 2 and 50 inclusive).
        char (str): A single character used to build the pyramid.

    Returns:
        str: A newline-separated pyramid pattern.

    Raises:
        TypeError: If height is not an int or char is not a str.
        ValueError: If char is not exactly one character long or height is out of range.
    """

    if not isinstance(height, int):
        raise TypeError('height must be int')
    if not isinstance(char, str):
        raise TypeError('char must be str')
    if len(char) != 1:
        raise ValueError('char must be a single character')
    if not 2 <= height <= 50:
        raise ValueError('height must be in range [2, 50]')

    row_widths = range(1, height * 2, 2)
    width = row_widths[-1]

    return '\n'.join(
        f'{char * i:^{width}}'
        for i in row_widths
    )


print(draw_pyramid(height=7))
