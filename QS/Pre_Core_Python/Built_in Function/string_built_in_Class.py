Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 'python is easy'
a.split()
['python', 'is', 'easy']
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
a = 'PyTHOn IS EasY To LeaRn'
res = ''
for i in a:
    if 'a' <= i <= 'z':
        res += chr(ord(i)-32)
pr
SyntaxError: invalid syntax
for i in a:
    if 'a' <= i <= 'z':
        res += chr(ord(i)-32)
print(res)
SyntaxError: invalid syntax
for i in a:
    if 'a' <= i <= 'z':
        res += chr(ord(i)-32)

res
'YNASOEAN'
for i in a:
    if 'a' <= i <= 'z':
        res += chr(ord(i)-32)
    else:
        res += i

        
res
'YNASOEANPYTHON IS EASY TO LEARN'
a
'PyTHOn IS EasY To LeaRn'
a.upper()
'PYTHON IS EASY TO LEARN'
a.lower()
'python is easy to learn'
b = 'python'
b.islower()
True
a.islower()
False
a = 'python is easy'
a.islower()
True
a = 'python_is_easy'
a.islower()
True
a.isupper()
False
a = 'PYTHON'
a.isupper()
True
a.isupper() or a.islower()
True
a = 'Steve @123'
a.isupper() or a.islower()
False
a.isalpha()
False
a.isnumeric()
False
a = '123'
a.isnumeric()
True
a = 'Steve @123'
a.isalpha() or a.isnumeric()
False
a = 'Steve123'
a.isalpha() or a.isnumeric()
False
a.isalpha()
False
a.isnumeric()
False
a.isalnum()
True
not(a.isalnum())
False
a = '!@#$%^&'
not(a.isalnum())
True
a = 'PyTHOn IS EasY To LeaRn'
a.swapcase()
'pYthoN is eASy tO lEArN'
a.capitalize()
'Python is easy to learn'
a.title()
'Python Is Easy To Learn'
a = 'Python Is Easy To Learn'
a.istitle()
True
a = 'banana'
res = {'b': 1, 'a': 3, 'n': 2}
a.count('b')
1
a.count('a')
3
a.count('n')
2
a = 'banana'
res = {}
for i in a:
    res[i] = a.count(i)

    
res
{'b': 1, 'a': 3, 'n': 2}
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

help(count)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    help(count)
NameError: name 'count' is not defined. Did you mean: 'round'?
help(str.count)
Help on method_descriptor:

count(self, sub[, start[, end]], /) unbound builtins.str method
    Return the number of non-overlapping occurrences of substring sub in string S[start:end].

    Optional arguments start and end are interpreted as in slice notation.

a = 'Banana'
a.count('a')
3
a.count('a', 0,3)
1
a.count('a', 0,1)
0
a.count('a', 0,2)
1
a.count('a', 0)
3
a.count('a', 3)
2
a.count('a', 4)
1
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> a
'Banana'
>>> a.startswith('A')
False
>>> a.endswith('a')
True
>>> a.startswith('Ban')
True
>>> a = 'PyTHOn IS EasY To LeaRn'
>>> a.split()
['PyTHOn', 'IS', 'EasY', 'To', 'LeaRn']
a.split('o')
['PyTHOn IS EasY T', ' LeaRn']
a.split('i')
['PyTHOn IS EasY To LeaRn']
a.split('I')
['PyTHOn ', 'S EasY To LeaRn']
a.split('n')
['PyTHO', ' IS EasY To LeaR', '']
a = 'PyTHOn IS EasY To LeaRn'
a.split(' ')
['PyTHOn', 'IS', 'EasY', 'To', 'LeaRn']
a.split(' ',2)
['PyTHOn', 'IS', 'EasY To LeaRn']
a.split(' ',2)
['PyTHOn', 'IS', 'EasY To LeaRn']
a.rsplit(' ',2)
['PyTHOn IS EasY', 'To', 'LeaRn']
a.split()
['PyTHOn', 'IS', 'EasY', 'To', 'LeaRn']
'_'.join(['PyTHOn', 'IS', 'EasY', 'To', 'LeaRn'])
'PyTHOn_IS_EasY_To_LeaRn'
''.join(['PyTHOn', 'IS', 'EasY', 'To', 'LeaRn'])
'PyTHOnISEasYToLeaRn'
a = 'PyTHOn IS EasY To LeaRn'
a.replace(' ', '_')
'PyTHOn_IS_EasY_To_LeaRn'
a.replace(' ', '_',2)
'PyTHOn_IS_EasY To LeaRn'
a = '                           steve                              '
len(a)
62
a.strip()
'steve'
a.rstrip()
'                           steve'
a.lstrip()
'steve                              '
a = '@@@@@@@@@@@@@@@steve@@@@@@@@@@@@@@@@'
a.strip
<built-in method strip of str object at 0x0000020E3282AFB0>
9
a.strip()
'@@@@@@@@@@@@@@@steve@@@@@@@@@@@@@@@@'
a.strip('@')
'steve'
a = 'steve'

a.zfill(10)
'00000steve'
help(str.zfill)
Help on method_descriptor:

zfill(self, width, /) unbound builtins.str method
    Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated.

a.zfill(width=10)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a.zfill(width=10)
TypeError: str.zfill() takes no keyword arguments
a.zfill(2)
'steve'
a = '                           steve                      '
a.strip(2)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.strip(2)
TypeError: strip arg must be None or str
a = '@@@@@@@@@@@@@@@steve@@@@@@@@@@@@@@@@'
a = '@@@@@@@@@@@@@@@ste@@@@@@@@@@@ve@@@@@@@@@@@@@@@@'
a.strip('@')
'ste@@@@@@@@@@@ve'
print(str)
<class 'str'>
print(len)
<built-in function len>
x = range(1, 11)
x.isprintable()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    x.isprintable()
AttributeError: 'range' object has no attribute 'isprintable'
a = 'banana'
a.index('a')
1
a.index('a',2)
3
a.index('a',4)
5
a.index('a',a.index('a')+1)
3
a.index('a', a.index('a',a.index('a')+1)+1)
5
a.index('a', a.index('a', a.index('a',a.index('a')+1)+1)+1)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a.index('a', a.index('a', a.index('a',a.index('a')+1)+1)+1)
ValueError: substring not found
a.index('x')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    a.index('x')
ValueError: substring not found
a.rindex('a')
5
a.rindex('a', a.rindex('a')-1)
5
a.rindex('a', 0,a.rindex('a')-1)
3
a.index('a')
1
a.find('a')
1
a.find('a', a.find('a')+1)
3
a.find('a', a.find('a', a.find('a')+1)+1)
5
a.find('a', a.find('a', a.find('a', a.find('a')+1)+1)+1)
-1
msg = 'Hello _____ Your Account _____ is debited with amount of rupees _____'
msg = 'Hello {} Your Account {} is debited with amount of rupees {}'
msg.format('steve', 1234, 19)
'Hello steve Your Account 1234 is debited with amount of rupees 19'
msg.format('allen', 1589, 566)
'Hello allen Your Account 1589 is debited with amount of rupees 566'
name = 'steve'
age = 28
pay=1895
f"Hello {name} you are {age} years of age and you get ${pay} as a pay"
'Hello steve you are 28 years of age and you get $1895 as a pay'
a = 'python\tis\teasy'
print(a)
python	is	easy
a.expandtabs(29)
'python                       is                           easy'
a = 'Hello steve Your Account 1234 is debited with amount of rupees 19'
a.title()
'Hello Steve Your Account 1234 Is Debited With Amount Of Rupees 19'
a = 'Hello Steve Your Account 1234 Is Debited With Amount Of Rupees 19'
a.istitle()
True
