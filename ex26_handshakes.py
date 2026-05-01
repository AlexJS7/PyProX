# Exercise 26 - Handshakes


"""
    There is only one handshake that can happen between two people.
    Between three people, there are three possible handshaking pairs.
    Between four people, there are six handshakes.
    Five people, ten handshakes, and so on.
        
    This exercise explores the full range of possible handshaking combinations.

    The combination math is: n(n-1)/2
"""

from collections.abc import Iterable


def get_handshake_combinations_number(people: Iterable[str]) -> tuple[int, list[str]]:
    """
    Calculates the number of unique handshakes and their descriptions.

    A handshake occurs between every unique pair of people.
    For n people, the number of handshakes is n * (n - 1) // 2.

    Parameters:
        people (Iterable[str]): An iterable object of person names.

    Returns:
        A tuple containing:
            - The number of unique handshakes.
            - A list of formatted handshake descriptions.

    Raises:
        TypeError: If `people` is not an iterable obj.
        TypeError: If any element in `people` is not a string.
        ValueError: If fewer than two people are provided.
    """

    # Create a list to check its length and items type.
    # Avoid one-pass iterable (i.e. generator) consumption.
    people = list(people)

    if not all(isinstance(i, str) for i in people):
        raise TypeError('All items in `people` must be strings.')

    if len(people) < 2:
        raise ValueError('At least two people are required.')

    def format_handshake(p1: str, p2: str) -> str:
        return f'{p1} shakes hands with {p2}'

    formatted_people = [p.title() for p in people]
    people_count = len(formatted_people)
    combinations = [
        format_handshake(formatted_people[i], formatted_people[j])
        for i in range(people_count - 1)
        for j in range(i + 1, people_count)
    ]

    return people_count * (people_count - 1) // 2, combinations


assert get_handshake_combinations_number(['Alice', 'Bob'])[0] == 1
assert get_handshake_combinations_number(['Alice', 'Bob', 'Carol'])[0] == 3
assert get_handshake_combinations_number(
    ['Alice', 'Bob', 'Carol', 'David'])[0] == 6
assert get_handshake_combinations_number(
    ['Alice', 'Bob', 'Carol', 'David', 'John'])[0] == 10
