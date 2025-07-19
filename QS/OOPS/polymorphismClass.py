def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

# print(add(10, 20))


a = 29
b = 11
print(a + b)

class Demo:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

x = Demo(99)
y = Demo(11)
print(x + y)
