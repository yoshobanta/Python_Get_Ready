#wap to group the given list of names wrt their length
#o/p = {5 : ['yosho','steve']}...
name = ['mike','sike','yosho']
i = 0
res = {}
new_name =[]
while i < len(name):
    key = len(name[i])
    if key not in res:
        res[key] = [name[i]]
    else:
        new_name += [name[i]]
        res[key] += new_name
    i += 1
print(res)

