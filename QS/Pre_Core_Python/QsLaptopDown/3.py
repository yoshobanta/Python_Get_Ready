#Wap to group the given list of names wrt their first character.
name = ['mike','sike','yosho','mana','manav','mia','lukash','layla']

res = {}
new_name =[]
i = 0
while i < len(name):
    key = name[i][0]
    if key not in res:
        res[key] = [name[i]]
    else:
        res[key] += [name[i]]
    i += 1
print(res)