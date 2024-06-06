from cup_game_init import *


def main(amount_of_cups=4, list_of_moves=[]):
    cup_state_list = init(amount_of_cups)
    user_moves = []
    if list_of_moves:
        for n in list_of_moves:
            cup_state_list = move(n, cup_state_list)
    print_cups(cup_state_list)  # noqa: F821
    while True:
        user_moves = get_moves(amount_of_cups)  # noqa: F821
        cup_state_list = move(user_moves, cup_state_list)
        print_cups(cup_state_list)  # noqa: F821
        check_win(cup_state_list)  # noqa: F821
        user_moves.clear()


main()
