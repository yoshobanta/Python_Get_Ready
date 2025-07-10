# 1. Count how many palindromic numbers exist in a given range
s = int(input('enter the starting range'))
e = int(input('enter the ending range:'))
res = 0
x = []
for n in range(s, e+1):
    c = n
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n //= 10
    if rev == c:
        res += 1
        x.append(c)
print(f"The no of palindromic numbers in between the given range is {res}")
print(f"The palindromic numbers are: {x}")

# 2. Print a number in words (e.g., 123 → "One Two Three") using loops.
a = int(input('enter the number:'))
res = ''
while a > 0:
    ld = a % 10
    if ld == 1:
        res = 'One ' + res
    elif ld == 2:
        res = 'Two ' + res
    elif ld == 3:
        res = 'Three ' + res
    elif ld == 4:
        res = 'Four ' + res
    elif ld == 5:
        res = 'Five ' + res
    elif ld == 6:
        res = 'Six ' + res
    elif ld == 7:
        res = 'Seven ' + res
    elif ld == 8:
        res = 'Eight ' + res
    elif ld == 9:
        res = 'Nine ' + res
    elif ld == 0:
        res = 'Zero ' + res
    a //= 10
print(res)
#---------------------------or---------------------------
a = int(input('enter the number:'))
res = ''
d = {1: 'One ',2: 'Two ',3: 'Three ',4: 'Four ',5: 'Five ',6: 'Six ',7: 'Seven ',8: 'Eight ',9: 'Nine ',0:'Zero '}
while a > 0:
    ld = a%10
    res = d[ld]+res
    a//=10
print(res)

# 3. Write a function to return the count of words, characters, and lines in a string.
def demo(s):
    w = len(s.split())
    len(s)
    l = len(s.split('\\n'))
    return (w, c, l)
print(demo('steve is a great guy'))

# 4. Print all perfect squares between 1 and 1000.
res = []
i = 1
while i <= 1000:
    if i * i <= 1000:
        res += [i*i]
    else:
        break
    i += 1

print(res)
# 5. WAP to find the second largest number in the given list.
a = eval(input('enter the list:'))
great = a[0]
sg = 0
for i in a:
    if i > great:
        sg = great
        great = i
    elif i > sg:
        sg = i
print(great)
print(sg)

# 6. Find the nth Fibonacci number using recursion
n = int(input('enter the number:'))
i = 0
a, b = 0, 1
while i < n:
    print(a)
    c = a + b
    a, b = b, c
    i += 1

def fibo(n, i=1, a = 0, b = 1):
    if i < n:
        c = a + b
        a, b = b, c
        return fibo(n, i=i+1, a=a, b=b)
    else:
        return a
# 7. Remove adjacent duplicates in a string
# Input: "aaabbccddaa" → Output: "abcda"
a = "aaabbccddaabb"
res = 'abcd'
for i in a:
    if i not in res:
        res += i
    if res[-1] != i:
        res += i
print(res)

# 8. Find the first non-repeating character in a string
a = input('enter the string:')
for i in a:
    if a.count(i) == 1:
        print(i)
        break

# 9. Reverse each word in a sentence
# Input: "Hello World" → Output: "olleH dlroW"
Split and reverse in one pass (without using built in functions)
a = input('enter the string:')
res = ''
d = ''
for i in a:
    if i != ' ':
        res = i + res
    else:
        res = d+' '+ res
if d:
    res += d
print(res)

# 10. Check if two strings are anagrams
#
# "listen" vs "silent" → True
a = input('enter the string:')
b = input('enter the string:')
a = list(a)
b = list(b)
a.sort()
b.sort()
if a == b:
    print('the entered strings are anagrams')
else:
    print('the entered strings are not anagrams')

# 1. Check if two strings are anagrams
#
# "listen" vs "silent" → True
a = input('enter the string:')
b = input('enter the string:')
a = list(a)
b = list(b)
a.sort()
b.sort()
if a == b:
    print('the entered strings are anagrams')
else:
    print('the entered strings are not anagrams')

# 2. Find the second largest number in a list(without using any built in functions)
# 3. WAP to find the missing vowel character from the given string.
# 4. Compress a string using run-length encoding(without using built in functions)
# "aaabbc" → "a3b2c1"
x = input('enter the string:')
res = ''
for a in x:
    c = 0
    for i in x:
        if i == a:
            c += 1
    if a not in res:
        res += f"{a}{c}"
print(res)

# 5. Find the longest word in a string
a = input('enter the sting:')
x = a.split()
g = ''
for i in x:
    if len(i) > len(g):
        g = i
print(g)

# 6. Find the nth Fibonacci number using recursion

# 7. Print a number pyramid
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# 8. Find the first non-repeating character in a string
# 9. Reverse each word in a sentence
#
# Input: "Hello World" → Output: "olleH dlroW"
#
# Split and reverse in one pass (without using built in functions)
#
# 10. Remove adjacent duplicates in a string
#
# Input: "aaabbccddaa" → Output: "abcda"
