import random
import itertools

num_cups = 4

def ramam(list_of_things:list):
    global num_cups
    ccc = []
    for i in itertools.permutations(list_of_things, r=num_cups-1):
        ccc.append(i)
    print(len(ccc))
    return ccc

def invert(x):
    if x:
        return 0
    return 1


def fitness(game_state):
    global num_cups
    game_state = list(game_state)
    gslen = len(game_state)
    noo = 0
    for i in game_state:
        if i:
            noo += 1
    fit = noo
    if noo == num_cups-1:
        fit -= 0.4
    if noo == 1:
        fit = "win"
    return fit


def tom(lom:list[list], ss:list[int]):
    for cup_num in range(1, len(ss)+1):
        exec(f"cup_{cup_num} = 0")
    cup_fitness = []
    caseso:str = "match o:\n"
    for i in range(1, len(ss)+1):
        caseso += f"    case {i}:\n        cup_{i} = invert(cup_{i})\n"
    if lom:
        for i in lom:
            for o in i:
                exec(caseso)
            if fitness(i) == "win":
                cup_list:list[int] = []
            cup_fitness.append(fitness(i))
    return [sum(cup_fitness), lom]


def pre(num):
    sa = list(range(1, num+1))
    return ramam(sa)


def algo():
    global num_cups
    ll = pre(num_cups)
    lm = []
    com = []
    fit_list = []
    move_list = []
    best_move = 0
    for _ in range(4):
        lm.append(random.choices(ll ,k=4))
    for i in lm:
        com.append(tom(i, [0, 0, 0, 0]))
    for k in com:
        fit_list.append(k[0])
        move_list.append(k[1])
    best_move = max(fit_list)
    index = fit_list.index(best_move)
    final_result = com[index]
    return final_result
print(algo())