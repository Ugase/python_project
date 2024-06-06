import cup_game_init as cgi
import random
from icecream import ic


def percent_chance(percent:int):
    if percent <= 0:
        return 0
    elif percent >= 100:
        return 1
    elif percent > 50 and random.randint(1, 100) >= percent:
        return 1
    elif percent < 50 and random.randint(1, 100) <= percent:
        return 1
    return 0
def fitness(list_of_moves: list[list[int]], amount_of_cups):
    game_state = cgi.init(amount_of_cups)
    total_zeros = 0
    for move in list_of_moves:
        game_state = cgi.move(move, game_state)
        total_zeros += game_state.count(0)
    if cgi.check_win(game_state):
        return -1
    return total_zeros

def create_random_move(amount_of_cups: int, existing_moves: list = None):
    if existing_moves is None:
        existing_moves = []
    move = []
    available_num = list(range(1, amount_of_cups + 1))
    move_size = random.randint(amount_of_cups, amount_of_cups + 6)
    for _ in range(move_size):
        sample_move = random.sample(available_num, amount_of_cups - 1)
        move.append(sorted(sample_move))
    return move


def mutate(percent: int, amount_of_cups: int, best_move: list[list[int]], pop: int):
    if percent > 100 or percent < 0:
        raise ValueError("Percentage must be between 0 and 100")
    mutated_children = []
    for _ in range(pop):
        child = best_move.copy()
        for indmov, move in enumerate(child):
            for indnum, num in enumerate(move):
                if random.random() < percent / 100:
                    child[indmov][indnum] = random.randint(1, amount_of_cups)
    return mutated_children

def main(percent: int, population: int, amount_of_cups: int):
    children = []
    fitness_scores = []
    for _ in range(population):
        children.append(create_random_move(amount_of_cups))
    while True:
        for child in children:
            fitness_scores.append(fitness(child, amount_of_cups))
            print(fitness_scores)
        print(fitness_scores) 
        best_child_index = fitness_scores.index(min(fitness_scores))
        best_move = children[best_child_index]
        if fitness_scores[best_child_index] == -1:
            print(best_move)
            return 0
        children = mutate(percent, amount_of_cups, best_move, population)
        ic(children)
        ic(fitness_scores)
        fitness_scores = []  # Clear the fitness_scores list

ic(main(5, 10, 50))