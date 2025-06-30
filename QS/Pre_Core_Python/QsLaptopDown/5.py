# #Wap to find the missing vowel character in the given string.
a = 'python is easy'
res = ''            # 'u'
i = 0
v = 'aeiou'
while i < len(v):
    if v[i] not in a :
        res += v[i]
    i += 1
print(res)
