# Exercise 28 - Border Drawing


def draw_border(width: int, height: int) -> str:
    """
    Return a string representation of a rectangle border.

    The border uses:
        '+' for corners,
        '--' for horizontal edges,
        '|' for vertical edges,
        and spaces for the interior.

    Parameters:
        width (int): Number of columns (2-50).
        height (int): Number of rows (2-50).

    Returns:
        str: A string representation of the rectangle border. Returns an empty string
        if either width or height is outside the range [2, 50].

    Raises:
        TypeError: If width or height is not an integer.
    """

    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError('width and height must be integers.')

    if not 2 <= width <= 50 or not 2 <= height <= 50:
        return ''

    top_bottom = '+' + '--' * (width - 2) + '+'
    middle = '|' + '  ' * (width - 2) + '|'

    return '\n'.join([top_bottom, *([middle] * (height - 2)), top_bottom])


print(draw_border(width=10, height=5))
