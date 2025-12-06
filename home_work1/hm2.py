def sum_num(num_1:int, num_2:int, sign:str):
    print(num_1, " + ", num_2, " = ", num_1 + num_2)

def min_num(num_1:int, num_2:int, sign:str):
    print(num_1, " - ", num_2, " = ", num_1 - num_2)

def mult_num(num_1:int, num_2:int, sign:str):
    print(num_1, " * ", num_2, " = ", num_1 * num_2)

def div_num(num_1:int, num_2:int, sign:str):
    print(num_1, " / ", num_2, " = ", num_1 / num_2)

num_1 = int(input("введите число 1 "))
num_2 = int(input("введите число 2"))
sign = str(input("что хотите сделать: +, -, *, /? "))

if sign == '+':
    sum_num(num_1,num_2,sign)
elif sign == '-':
    min_num(num_1,num_2,sign)
elif sign == '*':
    mult_num(num_1,num_2,sign)
elif sign == '/':
    div_num(num_1,num_2,sign)