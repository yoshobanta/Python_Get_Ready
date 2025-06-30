def add():
    a = int(input('enter the number:'))
    b = int(input('enter the number:'))
    c = a + b
    print(c)

name = 'steve'
# print('mr',name)

def greet():
    return 'hii Good morning..'

def add(a, b):
    return a + b

def wish(name):
    return 'Hiiii ' + name + ' Good Morning'

def length(a):
    c = 0
    for i in a:
        c += 1
    return c

def divs(n):
    res = []
    for i in range(1, n//2+1):
        if n % i == 0:
            res += [i]
    return res

# WAP to extract all the divisors of a given number
a = int(input('enter the number'))
print(divs(a))

# WAP to check whether the entered number is prime number or not.
def is_prime(n):
    return len(divs(n)) == 1


# WAP to extract all the prime numbers in between the user entered limits.
def primes(s, e):
    res = []
    for i in range(s, e+1):
        if is_prime(i):
            res += [i]
    return res

