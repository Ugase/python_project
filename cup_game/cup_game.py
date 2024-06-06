def invert(x):
    if x:
        return 0
    return 1

def check_win(var:list, loi:list):
    for i in var:
        if not i:
            return 0
    print("You win")
    print("Your list of moves:")
    for o in loi:
        print(o)
    quit()


def main(list_of_moves=[], amount_of_cups=4):
    cups:list[str] = []
    for cup_num in range(1, amount_of_cups+1):
        exec(f"cup_{cup_num} = 0")
    loi = []
    casesi:str = "match i:\n"
    for i in range(1, amount_of_cups+1):
        casesi += f"    case {i}:\n        cup_{i} = invert(cup_{i})\n"
    caseso:str = "match o:\n"
    for i in range(1, amount_of_cups+1):
        caseso += f"    case {i}:\n        cup_{i} = invert(cup_{i})\n"
    if list_of_moves:
        for i in list_of_moves:
            for o in i:
                exec(caseso)
    for k in range(1, amount_of_cups+1):
        print(f"{eval(f"cup_{k}")}", end="")
    print("")
    while True:
        for k in range(1, amount_of_cups+1):
            cups.append(eval(f"cup_{k}"))
        check_win(cups, loi)
        cups.clear()
        cup_list:list[int] = []
        while len(cup_list) != amount_of_cups-1:
            cup = input("What cup: ")
            if not cup or not cup.isdigit():
                continue
            cup_list.append(int(cup))
        loi.append(cup_list)
        for i in cup_list:
            exec(casesi)
        for k in range(1, amount_of_cups+1):
            print(f"{eval(f"cup_{k}")}", end="")
        print("")
main()
