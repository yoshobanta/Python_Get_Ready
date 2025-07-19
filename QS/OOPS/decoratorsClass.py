# add is pointing to a memory location where a block of code has been stored
def add(a, b):
    return a + b

##print(add(10, 20))

# x is pointing to a memory  location where add is pointing to.
x = add


# a is pointing to a memory location where 25 has been stored.
a = 25

# b is pointing to a memory location where a is pointing to.
b = a


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def calc(opcode, a, b):
    if opcode == 'add':
        return add(a, b)
    elif opcode == 'sub':
        return sub(a, b)
    elif opcode == 'mul':
        return mul(a, b)
    elif opcode == 'div':
        return div(a, b)
    else:
        print('Invalid Opcode')

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div
    }

def calc(opcode, a, b):
    if opcode in operations:
        return operations[opcode](a, b)
    print('Invalid Opcode')
    





def add(a, b, c, d, e, f):
    return a + b + c + d + e + f

def sub(a, b, c, d, e):
    return a - b - c - d - e

def mul(a, b, c, d):
    return a * b * c * d

def div(a, b, c):
    return a / b / c
operations = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div
    }
def calc(opcode, *args):# packing the variable no of positional arguments
    if opcode in operations:
        return operations[opcode](*args) # unpacking the variable no of positional arguments
    print('Invalid Opcode')




def add(a, b, c, d, e, f):
    return a + b + c + d + e + f

def sub(a, b, c, d, e):
    return a - b - c - d - e

def mul(a, b, c, d):
    return a * b * c * d

def div(a, b, c):
    return a / b / c

def calc(func, *args):
    return func(*args)



import time
def add(a, b, c, d, e, f):
    st =  time.time()
    res = a + b + c + d + e + f
    et = time.time()
    print(f"The time taken to execute the function is {et-st}")
    return res


def add(a, b):
    time.sleep(3)
    return a + b

def sub(a, b):
    time.sleep(3)
    return a - b

def mul(a, b):
    time.sleep(3)
    return a * b

def div(a, b):
    time.sleep(3)
    return a / b

def delay(func, *args):
    time.sleep(5)
    return func(*args)



def delay(func):
    def inner(*args, **kwargs):
        time.sleep(10)
        return func(*args, **kwargs)
    return inner
        
@delay
def add(a, b):
    return a + b

@delay
def sub(a, b):
    return a - b

@delay
def mul(a, b):
    return a * b

@delay
def div(a, b):
    return a / b

def timer(func):
    def inner(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        print(f"The time taken to execute {func.__name__} is:- {et-st}")
        return res
    return inner

@timer
def add(a, b):
    return a + b

@timer
def sub(a, b):
    return a - b

@timer
def mul(a, b):
    return a * b

@timer
def div(a, b):
    return a / b

from collections import defaultdict
count = defaultdict(int)
def counter(func):
    def inner(*args, **kwargs):
        count[func.__name__] += 1
        return func(*args, **kwargs)
    return inner


@counter
def add(a, b):
    return a + b

@counter
def sub(a, b):
    return a - b

@counter
def mul(a, b):
    return a * b

@counter
def div(a, b):
    return a / b

count = {}
def restrict(func):
    def inner(*args, **kwargs):
        if func.__name__ in count:
            if count[func.__name__] <3:
                count[func.__name__] += 1
                return func(*args, **kwargs)
            return f"You called {func.__name__} function morethan 3 times"
        count[func.__name__]  = 1
        return func(*args, **kwargs)
    return inner


@restrict
def add(a, b):
    return a + b

@restrict
def sub(a, b):
    return a - b

@restrict
def mul(a, b):
    return a * b

@restrict
def div(a, b):
    return a / b














