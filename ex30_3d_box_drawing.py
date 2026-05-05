# Exercise 30 - 3D Box Drawing


def draw_3d_box(size: int = 1) -> str:
    """
    Generate an ASCII representation of a 3D box.

    The box is drawn using:
        '-' for horizontal edges.
        '|' for vertical edges.
        '/' for diagonals.
        '+' for corners.

          +--+
         /  /|
        +--+ +
        |  |/
        +--+

    Parameters:
        size (int): An Integer for the width, length, and height of the box (must be between 1 and 5 inclusive).
                    The upper bound is enforced to keep output readable.

    Returns:
        str: A multi-line string representation of the 3D box.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is out of range [1, 5].
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not 1 <= size <= 5:
        raise ValueError('size must be in range [1, 5]')

    width = '--' * size
    inner_space = '  ' * size

    top = ' ' * (size + 1) + '+' + width + '+'
    bottom = top[::-1]
    # middle horizontal edge connecting front and back faces
    middle = bottom[:-1] + '+'
    top_diagonal = [
        ' ' * i + '/' + inner_space + '/' + ' ' * (size - i) + '|'
        for i in range(size, 0, -1)
    ]
    bottom_diagonal = [
        '|' + inner_space + '|' + ' ' * (i - 1) + '/'
        for i in range(size, 0, -1)
    ]

    return '\n'.join((top, *top_diagonal, middle, *bottom_diagonal, bottom))


print(draw_3d_box(1))
print(draw_3d_box(2))
print(draw_3d_box(3))
print(draw_3d_box(4))
print(draw_3d_box(5))
