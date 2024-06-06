import random
from cup_game_init import *
import itertools


def move_generator(hmpmg: int, possible_moves: list):
    return list(itertools.permutations(possible_moves, r=hmpmg))


def fitness_function(game_state: list, num_moves: int, prev_state=(), amz=0) -> int:
    """Calculate the fitness score based on the game state and number of moves."""
    remaining_zeros = game_state.count(0)
    if prev_state:
        rmzp = prev_state.count(0)
        if remaining_zeros == len(game_state) or rmzp == len(game_state):
            return remaining_zeros + num_moves + rmzp + 5000000000 + (amz * 10)
        return remaining_zeros + num_moves + rmzp + (amz * 10)
    return remaining_zeros + num_moves + (amz * 10)


def make_move(
    cup_state: list[int],
    moves: int,
    amount_of_moves_made: int,
    prev_state: list[int],
    aoz=0,
) -> tuple[list[int], list[int]]:
    """
    Make moves in the given cup state.

    Parameters
    ----------
    cup_state : List[int]
        The current state of the cups.
    moves : int
        The number of moves to be made.

    Returns
    -------
    Tuple[List[int], List[int]]
        The new state of the cups and the list of moves made.
    """
    possible_moves = move_generator(moves, range(1, moves + 1))
    game_states = []
    evaluated = []
    for i in possible_moves:
        game_states.append(move(i, cup_state))
    for t in game_states:
        print(t)
        evaluated.append(fitness_function(t, num_moves=amount_of_moves_made, amz=aoz))
    print(evaluated)
    evaluated = set(evaluated)
    evaluated = list(evaluated)
    print(evaluated)
    best_move = min(evaluated)
    index = evaluated.index(best_move)
    return possible_moves[index]


def list_of_moves(max_moves: int, amount: int) -> None:
    """
    Play the game for a specified number of moves.

    Parameters
    ----------
    max_moves : int
        The maximum number of moves to be made.
    """
    if not isinstance(max_moves, int):
        raise ValueError("The max_moves parameter must be of type int.")
    moves_made = []
    bad = 0
    cup_state = init(amount)
    temp = cup_state
    for o in range(1, max_moves + 1):
        best = make_move(cup_state, amount - 1, o, temp, bad)
        moves_made.append(best)
        cup_state = move(best, cup_state)
        if cup_state == init(amount):
            bad += 1
        temp = cup_state
    return moves_made


print(list_of_moves(4, 4))
