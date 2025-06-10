### WAP to print "Hello World" for 5 time.
##i = 0
##while i < 5:
##    print('Hello World')
##    i += 1
##
### WAP to print all the numbers from 1 to 100
##i = 1
##while i <= 100:
##    print(i)
##    i += 1
##
### WAP to print the first n natural numbers.
##n = int(input('enter the number:'))
##i = 1
##while i <= n:
##    print(i)
##    i += 1
##
### WAP to print all the numbers in between the user entered limits.
##s = int(input('enter the string:'))
##e = int(input('enter tje ending:'))
##i = s
##while i <= e:
##    print(i)
##    i = i + 1     # i += 1
##
### WAP to print all the even numbers in between the user entered limits.
##s = int(input('enter the string:'))
##e = int(input('enter tje ending:'))
##i = s
##while i <= e:
##    if i % 2 == 0:
##        print(i)
##    i = i + 1     # i += 1

### WAP to print all the odd numbers in between the user entered limits.
##s = int(input('enter the number:'))
##e = int(input('enter the number:'))
##i = s
##while i <= e:
##    if i % 2 != 0:
##        print(i)
##    i += 1

### WAP to print all the numbers which are divisible by 7&9 in between the user entered limits
##
##s = int(input('enter the number:'))
##e = int(input('enter the number:'))
##i = s
##while i <= e:
##    if i % 7 == 0 and i % 9 == 0:
##        print(i)
##    i += 1

###-------------------------------String-----------------------------------------------
### WAP to print all the charcters from the given string.
##a = input('enter the string')
##i = 0
##while i < len(a):
##    print(a[i])
##    i += 1

### WAP to print only the uppercase alphabets from the given string.
##a = input('enter the string')
##i = 0
##while i < len(a):
##    if 'A' <= a[i] <= 'Z':
##        print(a[i])
##    i += 1

# WAP to print only the lowercase alphabets from the given string.
# WAP to print only the numerical characters from the given string.
# WAP to print only the Special characters from the given string.

### WAP to extract all the characters from one variable to another variable.
##a = input('enter the string:')
##res = ''
##i = 0
##while i < len(a):
##    res += a[i]
##    i += 1
##print(res)


### WAP to extract only the uppercase alphabets from the given string.
##a = input('enter the string:')
##res = ''
##i = 0
##while i < len(a):
##    if 'A' <= a[i] <= 'Z':
##        res += a[i]
##    i += 1
##print(res)
##
### WAP to Extract only the lowercase alphabets from the given string.
### WAP to Extract only the numerical characters from the given string.
### WAP to Extract only the Special characters from the given string.

### WAP to reverse a given string.
##a = input('enter the string:')
##i = -1
##res = ''
##while i >= -len(a):
##    res += a[i]
##    i -= 1
##print(res)
###===================== or ========================
##
##a = input('enter the string:')
##res = ''
##i = 0
##while i < len(a):
##    res = a[i] + res
##    i += 1
##print(res)

# WAP to check whether the entered string is palindrome or not.
a = input('enter the sring:')
if a[::-1] == a:
    print('the entered string is a palindrome')
else:
    print('the entered string is not a palindrome')




    

