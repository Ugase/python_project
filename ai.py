# def calc(num1: float, num2: float, operator: str):
#     return eval(f"{num1} {operator} {num2}")
# 
# def usr_input():
#     num = input("Number: ")
#     num2 = input("Number: ")
#     operator = input("Operator: ").strip(" ")
#     return [num, num2, operator]
# 
# def main():
#     while True:
#         usr = usr_input()
#         print(calc(usr[0], usr[1], usr[2]))

while True: print("Output:",  eval(input("Input: ")))