# def div():
#     try:
#         a = eval(input('enter the number:'))
#         b = eval(input('enter the number:'))
#         return a / b
#     except ZeroDivisionError:
#         print('Please enter other than "0" as a second input')
#         return div()
#     except ValueError:
#         print('Please enter only numerical characters as a input')
#         return div()
#
#
# def func():
#     try:
#         a = eval(input('enter the number:'))
#         b = eval(input('enter the number:'))
#         return a / b
#     except Exception:
#         print('Exception Handelled Successfully')
#         return func()
#
# def demo():
#     try:
#         a = eval(input('enter the number:'))
#         b = eval(input('enter the number:'))
#         return a / b
#     except:
#         print('Exception Handeled Successfully')

#
# def sub():
#     a = int(input('enter the number:'))
#     b = int(input('enter the number:'))
#     if a > b:
#         return a - b
#     else:
#         raise ValueError('Enter fist number as a greatest')
#
# class MeraMarziException(Exception):
#     pass
#
# def sub():
#     a = int(input('enter the number:'))
#     b = int(input('enter the number:'))
#     if a > b:
#         return a - b
#     else:
#         raise MeraMarziException('Enter fist number as a greatest')

# iterators
def func():
    try:
        a = 'python'
        i = iter(a)
        while True:
            print(next(i))
    except StopIteration:
        pass


# a = 'python'
# for i in a:
#     print(i)

# # WAP to check whether the entered string are anagram or not
# a = 'listen'
# b = 'silent'
# if sorted(a) == sorted(b):
#     print('The entered strings are anagrams ')
# else:
#     print('the entered string are not anagrams')

names = ['steve jobs', 'mark henry', 'mickle jackson',
         'steve williomson', 'virat kohli', 'ms dhoni',
         'd likith', 'sundri shivani', 'bill gates']

ordered_names = sorted(names, reverse=True, key=lambda i:i.split()[-1])
# print(ordered_names)

details = [
    {'name': 'steve', 'age': 28, 'pay':2500},
    {'name': 'mike', 'age': 30, 'pay':3800},
    {'name': 'miller', 'age': 27, 'pay': 2450},
    {'name': 'allen', 'age': 25, 'pay':2400},
    {'name': 'bill', 'age': 35, 'pay':4000},
]
ordered_details = sorted(details, key=lambda i: i['pay'])
print(ordered_details)