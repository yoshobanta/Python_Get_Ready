# WAP to print "Hello World" for 5 time.
i = 0
while i < 5:
    print('Hello World')
    i += 1

# WAP to print all the numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# WAP to print the first n natural numbers.
n = int(input('enter the number:'))
i = 1
while i <= n:
    print(i)
    i += 1

# WAP to print all the numbers in between the user entered limits.
s = int(input('enter the string:'))
e = int(input('enter tje ending:'))
i = s
while i <= e:
    print(i)
    i = i + 1     # i += 1

# WAP to print all the even numbers in between the user entered limits.
s = int(input('enter the string:'))
e = int(input('enter tje ending:'))
i = s
while i <= e:
    if i % 2 == 0:
        print(i)
    i = i + 1     # i += 1

# WAP to print all the odd numbers in between the user entered limits.
s = int(input('enter the number:'))
e = int(input('enter the number:'))
i = s
while i <= e:
    if i % 2 != 0:
        print(i)
    i += 1

# WAP to print all the numbers which are divisible by 7&9 in between the user entered limits

s = int(input('enter the number:'))
e = int(input('enter the number:'))
i = s
while i <= e:
    if i % 7 == 0 and i % 9 == 0:
        print(i)
    i += 1

#-------------------------------String-----------------------------------------------
# WAP to print all the characters from the given string.
a = input('enter the string')
i = 0
while i < len(a):
    print(a[i])
    i += 1

# WAP to print only the uppercase alphabets from the given string.
a = input('enter the string')
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        print(a[i])
    i += 1

## WAP to print only the lowercase alphabets from the given string.
## WAP to print only the numerical characters from the given string.
## WAP to print only the Special characters from the given string.

# WAP to extract all the characters from one variable to another variable.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    res += a[i]
    i += 1
print(res)


# WAP to extract only the uppercase alphabets from the given string.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res += a[i]
    i += 1
print(res)

# WAP to Extract only the lowercase alphabets from the given string.
# WAP to Extract only the numerical characters from the given string.
# WAP to Extract only the Special characters from the given string.

# WAP to reverse a given string.
a = input('enter the string:')
i = -1
res = ''
while i >= -len(a):
    res += a[i]
    i -= 1
print(res)
#===================== or ========================

a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    res = a[i] + res
    i += 1
print(res)

# WAP to check whether the entered string is palindrome or not.(without using slicing)
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    res = a[i] + res
    i += 1
if res == a:
    print('the entered string is a palindrome')
else:
    print('the entered string is not a palindrome')

# WAP to separate all the characters from the given string.
a = input('enter the string:')
uc, lc, nc, sc = '', '', '', ''
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        uc += a[i]
    elif 'a' <= a[i] <= 'z':
        lc += a[i]
    elif '0' <= a[i] <= '9':
        nc += a[i]
    else:
        sc += a[i]
    i += 1

print('uppercase alphabets are:', uc)
print('lowercase alphabets are:', lc)
print('numerical characters are:', nc)
print('special characters are:', sc)

# WAP to convert all the uppercase characters of a string into lowercase.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res += chr(ord(a[i])+32)
    else:
        res += a[i]
    i += 1
print(res)

# WAP to convert all the lowercase characters of a string into uppercase.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if 'a' <= a[i] <= 'z':
        res += chr(ord(a[i])-32)
    else:
        res += a[i]
    i += 1
print(res)

# WAP to toggle the given string.
a = input('enter the string:')
i = 0
res = ''
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res += chr(ord(a[i])+32)
    elif 'a' <= a[i] <= 'z':
        res += chr(ord(a[i])-32)
    else:
        res += a[i]
    i += 1
print(res)
x = True
res = 0
while x:
    n = int(input('enter the number:'))
    if n != 0:
        res += n
    else:
        print(res)
        x = False

# WAP to find the sum of first n natural numbers.
n = int(input('enter the number:'))
i = 1
res = 0
while i <= n:
    res += i
    i += 1
print(res)

# WAP to find the factorial of a given number.
n = int(input('enter the number:'))
i = 1
res = 1
while i <= n:
    res *= i
    i += 1
print(res)

# WAP to print all the divisors of a given number
a = int(input('enter the number:'))
i = 1
res = []
while i < a:
    if a % i == 0:
        res += [i]
    i += 1

print(res)
# WAP to check whether the entered number is prime or not.
a = int(input('enter the number:'))
i = 1
res = []
while i < a:
    if a % i == 0:
        res += [i]
    i += 1
if len(res) == 1:
    print('the entered number is a prime numebr')
else:
    print('the entered number is not a prime number')

# WAP to check whether the entered number is perfect or not.
a = int(input('enter the number:'))
res = 0
i = 1
while i < a:
    if a % i == 0:
        res += i
    i += 1
if res == a:
    print('the entered number is a perfect number')
else:
    print('the entered number is not a perfect number')
print(res)

# WAP to check whether the entered numbers are amicable or not.
a = int(input('enter the number'))
b = int(input('enter the number'))
c = 0
d = 0
i = 1
while i < a:
    if a % i == 0:
        c += i
    i += 1

j = 1
while j < b:
    if b % j == 0:
        d += j
    j += 1
if a == d and b == c:
    print('both the entered numbers are amicable numbers')
else:
    print('both the entered numbers are not an amicable numbers.')

# WAP to print first n fibonacci numbers.
a = 0
b = 1
i = 0
res = []
while i < 15:
    res += [a]
    c = a + b
    a, b = b, c
    i += 1
print(res)

# WAP to find the sum of all the individual digits of a given integer.
a = int(input('enter the string:'))
i = a
res = 0
while i > 0:
    res += i%10
    i //= 10
print(res)

# WAP to extract all the even number digits from the entered number
a = 25687
res = []
i = a
while i > 0:
    if (i%10)%2==0:
        res += [i%10]
    i//=10
print(res)

# WAP to reverse a give integer  number.(without type casting & slicing)
a = int(input('enter the number:'))
res = 0
while a > 0:
    ld = a % 10
    res = res*10+ld
    a //=10
print(res)

# WAP to extract all the string items from the given list
a = ['python', 'steve', [1, 2, 3], 'allen']
res = []
i = 0
while i < len(a):
    if isinstance(a[i], str):
        res += [a[i]]
    i += 1
print(res)

# WAP to check whether the entered value is string or not.
a = eval(input('enter the value:'))
if isinstance(a, str):
    print('yes...string')
else:
    print('noo.....Not a string')


# WAP to extract all the mutable items from the given list
a = eval(input('enter the list:'))
res = ()
i = 0
while i < len(a):
    if isinstance(a[i], (list, set, dict)):
        res += (a[i],)
    i += 1

print(res)

# WAP to split the given string.
a = 'python is easy'
res = []
d = ''
i = 0
while i < len(a):
    if a[i] != ' ':
        d += a[i]
    else:
        res += [d]
        d = ''
    i += 1
if d:
    res += [d]
print(res)

a = int(input('enter the number:'))
if a % 3 == 0 and a % 5 == 0:
    print('fizzbuzz')
elif a % 5 == 0:
    print('buzz')
elif a % 3 == 0:
    print('fizz')
else:
    print('not divisible')


a = int(input('enter the number:'))
res = ('fizz'*(a%3==0))+('buzz'*(a%5==0))
if a%3==0:
    print(res)
else:
    print('not divisible')
# WAP to find the greatest number among the given list of integers.
a = eval(input('enter the list:'))
g = a[0]
i = 0
while i < len(a):
    if a[i] > g:
        g = a[i]
    i += 1
print(g)