class Plus:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Plus(self.num + other.num)

a = Plus(7)
b = Plus(2)
c = a + b
print(c.num)

class Minus:
    def __init__(self, num):
        self.num = num

    def __sub__(self, other):
        return Minus(self.num - other.num)

a = Minus(1)
b = Minus(3)
c = a - b
print(c.num)

class Multi:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return Multi(self.num * other.num)

a = Multi(9)
b = Multi(2)
c = a * b
print(c.num)

class Div:
    def __init__(self, num):
        self.num = num

    def __truediv__(self, other):
        return Div(self.num / other.num)

a = Div(4)
b = Div(8)
c = a / b
print(c.num)