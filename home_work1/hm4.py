import math as m

class Calk():
    def __init__(self, num_1, num_2, sign):
        self.num_1 = num_1
        self.num_2 = num_2
        self.sign = sign

    def calk(self ):
        if self.sign == '+':
            print(self.num_1, ' + ', self.num_2, ' = ', self.num_1 + self.num_2)
        elif self.sign == '-':
            print(self.num_1, ' - ', self.num_2, ' = ', self.num_1 - self.num_2)
        elif self.sign == '*':
            print(self.num_1, ' * ', self.num_2, ' = ', self.num_1 * self.num_2)
        elif self.sign == '/':
            print(self.num_1, ' / ', self.num_2, ' = ', self.num_1 / self.num_2)

    def engin_calk(self):
        if self.sign == 'cos':
            print("cos(",self.num_1, ") = ", m.cos(self.num_1))
        if self.sign == 'sin':
            print("sin(",self.num_1, ") = ", m.sin(self.num_1))

kind = str(input("какой хотите использовать: engine, calk "))
if kind == "engine":
    num_1 = int(input("введите число 1 "))
    num_2 = int(0)
    sign = str(input("что хотите сделать: cos, sin "))
    fun_2 = Calk(num_1, num_2, sign)
    fun_2.engin_calk()
else:
    num_1 = int(input("введите число 1 "))
    num_2 = int(input("введите число 2"))
    sign = str(input("что хотите сделать: +, -, *, /? "))
    fun_1 = Calk(num_1, num_2, sign)
    fun_1.calk()





