def invert(x):
    return 0 if x else 1


def check_win(game_state: list):
    return not any(cell == 0 for cell in game_state)


def move(moves: list, game_state: list):
    for i in moves:
        game_state[i - 1] = invert(game_state[i - 1])
    return game_state


def print_cups(game_state: list):
    print("".join(str(x) for x in game_state).replace(" ", ""))


def get_moves(amount: int):
    user_moves = []
    while len(user_moves) != amount - 1:
        cup = input("What cup to flip: ")
        if not cup or not cup.isdigit():
            continue
        if int(cup) > amount:
            for i in cup:
                if int(i) > amount:
                    user_moves.append(amount)
                    continue
                user_moves.append(int(i))
                if len(user_moves) == amount - 1:
                    return user_moves
        user_moves.append(int(cup))
    return user_moves


def init(amount: int):
    return [0] * amount
