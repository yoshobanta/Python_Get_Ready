# # for loop
# # WAp to print all the characters of a given string.
# a = input('enter the string:')
# for i in a:
#     print(i)

# # WAP to extract all the uppercase alphabets from the given string.
# a = input('enter the string:')
# res = ''
# for i in a:
#     if 'A' <= i <= 'Z':
#         res += i
# print(res)

# # 2. WAP to print all the numbers from 1 to 100
# for i in range(1, 101):
#     print(i)

# # WAP to extract all the even numbers in between the user entered limits.
# s = int(input('enter the number:'))
# e = int(input('enter the number:'))
# res = []
# for i in range(s, e+1):
#     if i % 2 == 0:
#         res += [i]
# print(res)

# # WAP to extract the divisors of a given number.
# n = int(input('enter the number:'))
# res = []
# for i in range(1, n//2+1):
#     if n % i == 0:
#         res += [i]
# print(res)

# # WAP to check whether the entered number is prime number or not.
# n = int(input('enter the number:'))
# for i in range(2, n//2+1):
#     if n % i == 0:
#         print('the entered number is not a prime number')
#         break
# else:
#     print('the entered number is a prime number')
# x = range(10, 201, 2)
# print(list(x))

# # WAP to extract all the odd index charcters of a string.
# a = input('enter the string:')
# res = ''
# for i in range(0, len(a)):
#     if i % 2 == 0:
#         res += a[i]
# print(res)

a = 'python'
for i, j in enumerate(a):
    if i % 2 == 0:
        print(j)
