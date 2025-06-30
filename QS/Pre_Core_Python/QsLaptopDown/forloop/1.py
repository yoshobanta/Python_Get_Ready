#for loop
#wap to print all the ch of a given string
# a =input('enter a string - ')
# for i in a :
#     print(i)

#Wap to check if a string is palindrome or not.

# a= input("Enter a string -")
# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Wap to check if a string is palindrome or not.without slicing

# a=  input("Enter a string -")
# res =''
# for i in a:
#     res = i+res
# if a == res:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Wap to reverse a number.

# a = int(input("Enter a number -"))
# i = a
# res = 0
# while i > 0:
#     ld = i%10
#     res = res*10 + ld
#     i //=10

# print(res)

# now to do this in for loop we have no other options but to use type casting.
# a = int(input("Enter a number -"))
# res =''
# for i in str(a):
#     res = i + res

# print(res)


# wap for armstrong number.

a = int(input("Enter a number"))

res =0
for i in (str(a)):
    l = len(str(a))
    res += int(i) ** l

print(res)

