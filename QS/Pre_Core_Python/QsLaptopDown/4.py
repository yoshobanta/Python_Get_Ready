from collections import defaultdict

name = ['mike','sike','yosho','mana','manav','mia','lukash','layla']

res = defaultdict(list)    # for length with name
i = 0
while i < len(name):
    res[len(name[i])] += [name[i]]
    i += 1
print(res)

res2 = defaultdict(list)    # for first letter and name
i = 0
while i < len(name):
    res2[name[i][0]] += [name[i]]
    i += 1
print(res2)