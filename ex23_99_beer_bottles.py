# Exercise 23 - 99 Beer Bottles


"""
    99 bottles of beer on the wall,
    99 bottles of beer,
    Take one down,
    Pass it around,
    98 bottles of beer on the wall,...

    "99 Bottles of Beer on the Wall" is a cumulative song
    often sung to pass the time (and annoy anyone close to the singer).
"""


def get_99bottles_lyrics() -> str:
    """
    Return the lyrics to "99 Bottles of Beer.
    Each stanza of the song goes like this:
        X bottles of beer on the wall,
        X bottles of beer,
        Take one down,
        Pass it around,
        X - 1 bottles of beer on the wall,...

    Returns:
        str: Lyrics of "99 Bottles of Beer on the Wall" song.
    """

    lines = []

    for n in range(99, 0, -1):
        lines.append(
            f"{format_bottle_count(n)} of beer on the wall,\n"
            f"{format_bottle_count(n)} of beer,\n"
            'Take one down,\n'
            'Pass it around,\n'
        )
        if n == 1:
            lines.append('No more bottles of beer on the wall!')
        else:
            lines.append(
                f"{format_bottle_count(n - 1)} of beer on the wall,\n\n")

    return ''.join(lines)


def format_bottle_count(n: int) -> str:
    """
    Format a bottle count as a string with correct singular or plural form.

    Parameters:
        n (int): The number of bottles.

    Returns:
        str: A string in the form "<n> bottle" if n == 1,
             otherwise "<n> bottles".
    """

    return f"{n} bottle{'' if n == 1 else 's'}"


print(get_99bottles_lyrics())
