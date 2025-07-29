# read
# readline
# readlines

# fo = open('test.txt', 'r')
# data = fo.read()
# print(data)

# fo.close()

# fo = open('test.txt', 'r')
# line = fo.readline()
# print(line)
# line = fo.readline()
# print(line)
# line = fo.readline()
# print(line)
# line = fo.readline()
# print(line)
# line = fo.readline()
# print(line)

# fo = open('test.txt', 'r')
# data = fo.readlines()
# fo.close()

# fo = open(r"C:\Users\lenovo\Desktop\sample.log")
# data = fo.readlines()
# print(data)
# fo.close()

# context manager.
# with open('sample.txt') as f:
#     for line in f:
#         print(line.replace(' ', '_'))
# from collections import  defaultdict
# ips = []
# with (open('access-log.txt') as f):
#     for i in f:
#         ip = i.split()[0]
#         if ip not in ips:
#             ips.append(ip)
#
#
# ips = []
# with (open('access-log.txt') as f):
#     for i in f:
#         ip = i.split()[0]
#         ips.append(ip)
#
# c = defaultdict(int)
# for i in ips:
#     c[i] += 1
# print(c)

# with open('sample.log') as f:
#     for i in f:
#         cleaned_line =i.strip()
#         if cleaned_line:
#             print(cleaned_line.split()[2])

# print(f)
###---------------------------------####
#### Write to a file/

# data1 = 'hiii\n'
# data2 = 'hello\n'
# data3 = 'python\n'
# data4 = 'java\n'
# data = [data1, data2, data3, data4]
# with open('test.txt', 'a') as f:
#     f.writelines(data)
# x = str(data)
# print(x)
#
# data = [10, 20, 30]
# enc = str(data)
#
# import json
# data = {'name': 'steve', 'age': 28, 'pay': 2588}
# enc_data = json.dumps(data)
# with open('myfile.txt', 'w') as f:
#     f.write(enc_data)
#
#
# with open('myfile.txt') as f:
#     data = f.read()
#     print(data)
#     print(type(data))
#     dec_data = json.loads(data)
#     print(dec_data)
#     print(type(dec_data))

import pickle
# data = {'name': 'steve', 'age': 28, 'pay': 2588}
# enc_data = pickle.dumps(data)
# with open('pickling.txt', 'wb') as f:
#     f.write(enc_data)

# with open('pickling.txt', "rb") as f:
#     data = f.read()
#     print(data)
#     print(type(data))
#     dec_data = pickle.loads(data)
#     print(dec_data)
#     print(type(dec_data))