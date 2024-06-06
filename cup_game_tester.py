casesi = "match i:\n"
for i in range(1, 5):
    casesi += f"    case {i}:\n        cup_{i} = invert(cup_{i})\n"


caseso = "match o:\n"
for i in range(1, 5):
    caseso += f"    case {i}:\n        cup_{i} = invert(cup_{i})\n"

cup_1 = 1
cup_2 = 1
cup_3 = 1
cup_4 = 1
def gc(x):
    return eval(x)
for k in range(1, 5):
    print(f"{eval(f"cup_{k}")}", end="")

loi = "kkkkk"
winn = "if"
for i in range(1, amount_of_cups-1):
    winn += f" cup{i} and"
winn += f" cup_{amount_of_cups}:\n"
print(winn)
winn += """    print("You win")
    for k in range(1, amount_of_cups+1):
        print(f"{eval(f"cup_{k}")}", end="")
    for p in loi:
        print(p)
    break"""
exec(winn)