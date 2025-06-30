from collections import  defaultdict
# 1. WAP to print "Hello World" for 5 time.
i = 0
while i < 5:
    print('Hello World')
    i += 1

# 2. WAP to print all the numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# 3. WAP to print the first n natural numbers.
n = int(input('enter the number:'))
i = 1
while i <= n:
    print(i)
    i += 1

# 4. WAP to print all the numbers in between the user entered limits.
s = int(input('enter the string:'))
e = int(input('enter tje ending:'))
i = s
while i <= e:
    print(i)
    i = i + 1     # i += 1

# 5. WAP to print all the even numbers in between the user entered limits.
s = int(input('enter the string:'))
e = int(input('enter tje ending:'))
i = s
while i <= e:
    if i % 2 == 0:
        print(i)
    i = i + 1     # i += 1

# 6. WAP to print all the odd numbers in between the user entered limits.
s = int(input('enter the number:'))
e = int(input('enter the number:'))
i = s
while i <= e:
    if i % 2 != 0:
        print(i)
    i += 1

# 7. WAP to print all the numbers which are divisible by 7&9 in between the user entered limits

s = int(input('enter the number:'))
e = int(input('enter the number:'))
i = s
while i <= e:
    if i % 7 == 0 and i % 9 == 0:
        print(i)
    i += 1

#-------------------------------String-----------------------------------------------
# 8. WAP to print all the characters from the given string.
a = input('enter the string')
i = 0
while i < len(a):
    print(a[i])
    i += 1

# 9. WAP to print only the uppercase alphabets from the given string.
a = input('enter the string')
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        print(a[i])
    i += 1

# 10. WAP to print only the lowercase alphabets from the given string.
# 11. WAP to print only the numerical characters from the given string.
# 12. WAP to print only the Special characters from the given string.

# 13. WAP to extract all the characters from one variable to another variable.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    res += a[i]
    i += 1
print(res)


# 14. WAP to extract only the uppercase alphabets from the given string.
a = input('enter the string:')
res = ''
i = 0
while i < len(a):
    if 'A' <= a[i] <= 'Z':
        res += a[i]
    i += 1
print(res)

# 15. WAP to Extract only the lowercase alphabets from the given string.
# 16. WAP to Extract only the numerical characters from the given string.
# 17. WAP to Extract only the Special characters from the given string.

# 18. WAP to reverse a given string.
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

# 19. WAP to check whether the entered string is palindrome or not.(without using slicing)
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

# 20. WAP to separate all the characters from the given string.
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

# 21. WAP to convert all the uppercase characters of a string into lowercase.
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

# 22. WAP to convert all the lowercase characters of a string into uppercase.
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

# 23. WAP to toggle the given string.
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

# 24. WAP to find the sum of first n natural numbers.
n = int(input('enter the number:'))
i = 1
res = 0
while i <= n:
    res += i
    i += 1
print(res)

# 25. WAP to find the factorial of a given number.
n = int(input('enter the number:'))
i = 1
res = 1
while i <= n:
    res *= i
    i += 1
print(res)

# 26. WAP to print all the divisors of a given number
a = int(input('enter the number:'))
i = 1
res = []
while i < a:
    if a % i == 0:
        res += [i]
    i += 1

print(res)
# 27. WAP to check whether the entered number is prime or not.
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

# 28. WAP to check whether the entered number is perfect or not.
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

# 29. WAP to check whether the entered numbers are amicable or not.
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

# 30. WAP to print first n fibonacci numbers.
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

# 31. WAP to find the sum of all the individual digits of a given integer.
a = int(input('enter the string:'))
i = a
res = 0
while i > 0:
    res += i%10
    i //= 10
print(res)

# 32. WAP to extract all the even number digits from the entered number
a = 25687
res = []
i = a
while i > 0:
    if (i%10)%2==0:
        res += [i%10]
    i//=10
print(res)

# 33. WAP to reverse a give integer  number.(without type casting & slicing)
a = int(input('enter the number:'))
res = 0
while a > 0:
    ld = a % 10
    res = res*10+ld
    a //=10
print(res)

# 34. WAP to extract all the string items from the given list
a = ['python', 'steve', [1, 2, 3], 'allen']
res = []
i = 0
while i < len(a):
    if isinstance(a[i], str):
        res += [a[i]]
    i += 1
print(res)

# 35. WAP to check whether the entered value is string or not.
a = eval(input('enter the value:'))
if isinstance(a, str):
    print('yes...string')
else:
    print('noo.....Not a string')


# 36. WAP to extract all the mutable items from the given list
a = eval(input('enter the list:'))
res = ()
i = 0
while i < len(a):
    if isinstance(a[i], (list, set, dict)):
        res += (a[i],)
    i += 1

print(res)

# 37. WAP to split the given string.
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

# 38. Fizz buzz using elif
a = int(input('enter the number:'))
if a % 3 == 0 and a % 5 == 0:
    print('fizzbuzz')
elif a % 5 == 0:
    print('buzz')
elif a % 3 == 0:
    print('fizz')
else:
    print('not divisible')

# 39. fizz buzz without using elif
a = int(input('enter the number:'))
res = ('fizz'*(a%3==0))+('buzz'*(a%5==0))
if a%3==0:
    print(res)
else:
    print('not divisible')
# 40. WAP to find the greatest number among the given list of integers.
a = eval(input('enter the list:'))
g = a[0]
i = 0
while i < len(a):
    if a[i] > g:
        g = a[i]
    i += 1
print(g)

# break, pass, continue

# 41. WAP to extract all the divisors of a given number.
a = int(input('enter the number:'))
res = []
i = 1
while i <= a//2:
    if a % i == 0:
        res += [i]
    i += 1
print(res)
res = 0

# 42.
while True:
    a = int(input('enter the number:'))
    if a == 0:
        print(res)
        break
    res += a


# 43. WAP to print all the odd numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
while True:
    pass
if 10 > 20:
    pass
# 44. prime number using break
a = int(input('enter the number:'))
i = 2
while i < a:
    if a % i == 0:
        print('the entered number is not a prime number')
        break
    i +=1
else:
    print('the entered number is a prime number')
# 45.
a = ['steve', 'allen', 'mike', 'blake', 'miller']
# res = {'steve': 5, 'allen': 5, 'mike': 4, 'blake': 5, 'miller': 6}
res = {}
i = 0
while i < len(a):
    res[a[i]] = len(a[i])
    i += 1
print(res)

# 46.
a = ['steve', 'allen', 'mike', 'blake', 'miller']
# res = {'steve': ('steve', 5), 'allen': ('allen', 5), 'mike': ('mike', 4), 'blake': ('blake', 5), 'miller': ('miller', 6)}
res = {}
i = 0
while i < len(a):
    res[a[i]] = (a[i], len(a[i]))
    i += 1
print(res)


# 47.
a = ['steve', 'allen', 'mike', 'blake', 'miller']
# res = {'steve': ('steve', 5), 'allen': ('allen', 5), 'mike': (4, 'mike'), 'blake': ('blake', 5), 'miller': (6, 'miller')}
res = {}
i = 0
while i < len(a):
    if len(a[i]) % 2 == 0:
        res[a[i]] = (len(a[i]), a[i])
    else:
        res[a[i]] = (a[i], len(a[i]))
    i += 1
print(res)

# 48. WAP to count the no of times each character is repeated in the given string.
a = input('enter the string:')
# res = {'b': 1, 'a': 3, 'n': 2}
i = 0
res = {}
while i < len(a):
    if a[i] not in res:
        res[a[i]] = 1
    else:
        res[a[i]] += 1
    i += 1
print(res)
49.
a = 8179267926
# res = 'one two three'
d = {1:'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six',
     7:'seven', 8:'eight', 9:'nine', 0: 'zero'}
res = ''
while a > 0:
    res = d[a%10] + ' ' + res
    a //= 10

print(res)

# 50.
username = 'likith_1003'
password = '123445likith'
un = input('enter the username:')
if un == username:
    pw = input('enter the password:')
    if pw == password:
        print('logged in')
    else:
        print('invalid password')
else:
    print('user not found')


# 51.
c = [
    {'username': 'likith_1003', 'password': 'abcd1234'},
    {'username': 'ritesh', 'password': 'ritesh@123'},
    {'username': 'mickel', 'password': 'Mickel@jackson'},
    {'username': 'nick', 'password': 'nick1234'}

]
un = input('enter the username:')
i = 0
while i < len(c):
    if c[i]['username'] == un:
        pw = input('enter the passwordd:')
        if pw == c[i]['password']:
            print('User Logged in successfully')
        else:
            print('invalid Password')
        break
    i += 1

else:
    print('user Not Found')


# 52. WAP to group the given list of names WRT their length
a = ['mike', 'allen', 'steve', 'miller', 'anna', 'ritesh', 'jitesh',
         'hitesh', 'mukesh', 'yosho', 'akash', 'praveen', 'naveen',
         'vijay', 'anil']
res = {}
i= 0
while i < len(a):
    if len(a[i]) not in res:
        res[len(a[i])] = [a[i]]
    else:
        res[len(a[i])] += [a[i]]
    i += 1
print(res)
# 53. WAP to group the given list of names WRT their first charcater.
a = ['mike', 'allen', 'steve', 'miller', 'anna', 'ritesh', 'jitesh',
         'hitesh', 'mukesh', 'youso', 'akash', 'praveen', 'naveen',
         'vijay', 'anil']
res = defaultdict(list)
i= 0
while i < len(a):
    res[a[i][0]] += [a[i]]
    i += 1
print(res)

# 54. WAP to count the no of times each character is repeated in the given string.
a = input('enter the string:')
res = defaultdict(int)
i = 0
while i < len(a):
    res[a[i]] += 1
    i += 1
print(res)

# 55. WAP to find the missing vowel character in the given string.
a = 'python is easy'
res = ''
i = 0
v = 'aeiou'
while i < len(v):
    if v[i] not in a:
        res += v[i]
    i += 1
print(res)