# Exercise 27 - Rectangle Drawing


def draw_rectangle(width: int, height: int, char: str = '#') -> str:
    """
    Return a string representation of a rectangle.

    Parameters:
        width (int): The width of the rectangle (number of characters per line).
        height (int): The height of the rectangle (number of lines).
        char (str): A single character used to draw the rectangle.

    Returns:
        str: A string representation of the rectangle. Returns an empty string
        if either width or height is outside the range [1, 50].

    Raises:
        TypeError: If either `width` or `height` are not integers.
        TypeError: If `char` is not a string of length 1.
    """

    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError('`width` and `height` must be integers.')

    if not isinstance(char, str) or len(char) != 1:
        raise TypeError('`char` must be a string of length 1.')

    if not 1 <= width <= 50 or not 1 <= height <= 50:
        return ''

    return '\n'.join(char * width for _ in range(height))


print(draw_rectangle(width=25, height=10))
