num_1 = int(input("введите число 1 "))
num_2 = int(input("введите число 2"))
sign = str(input("что хотите сделать: +, -, *, /? "))
if sign == '+':
    print(num_1, ' + ', num_2, ' = ', num_1+num_2)
elif sign == '-':
    print(num_1, ' - ', num_2, ' = ', num_1 - num_2)
elif sign == '*':
    print(num_1, ' * ', num_2, ' = ', num_1 * num_2)
elif sign == '/':
    print(num_1, ' / ', num_2, ' = ', num_1 / num_2)