# Exercise 22 - Rock, Paper, Scissors


"""
Rock, paper, scissors is a popular hand game for two players.
The two players simultaneously choose one of the three possible moves
and determine the winner of the game:
- rock beats scissors
- paper beats rock
- scissors beats paper
"""


def rps_winner(player1: str, player2: str) -> str:
    """
    Determine the winner of a rock-paper-scissors round.

    Parameters:
        player1: Move of player one ('rock', 'paper', or 'scissors').
        player2: Move of player two ('rock', 'paper', or 'scissors').

    Returns:
        str: 'player one' | 'player two' | 'tie'.

    Raises:
        ValueError: If an invalid move is provided.
    """

    beats = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    }

    if player1 not in beats.keys() or player2 not in beats.keys():
        raise ValueError(f"Invalid move. Expected {', '.join(beats.keys())}.")

    if player1 == player2:
        return 'tie'

    if beats[player1] == player2:
        return 'player one'

    if beats[player2] == player1:
        return 'player two'


assert rps_winner('rock', 'paper') == 'player two'
assert rps_winner('rock', 'scissors') == 'player one'
assert rps_winner('paper', 'scissors') == 'player two'
assert rps_winner('paper', 'rock') == 'player one'
assert rps_winner('scissors', 'rock') == 'player two'
assert rps_winner('scissors', 'paper') == 'player one'
assert rps_winner('rock', 'rock') == 'tie'
assert rps_winner('paper', 'paper') == 'tie'
assert rps_winner('scissors', 'scissors') == 'tie'
