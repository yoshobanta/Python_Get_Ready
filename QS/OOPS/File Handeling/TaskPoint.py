# x = []
# y = []
# z = []
# with open("points.txt") as f:
#     for i in f:
#         x.append(i.split()[0])
#         y.append(i.split()[1])
#         z.append(i.split()[2])
        
# print(x)
# print(y)
# print(z)

#Only x co-ordinates positive value
# x = []
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         if value > 0.0:
#             x.append(value)
            
# print(x)


# y = []
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         if value > 0.0:
#             y.append(value)
            
# print(y)

# z = []
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         if value > 0.0:
#             z.append(value)
            
# print(z)

#sum of x co-ordinates
# x = []
# res = 0
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         x.append(value)
#         res += value
            
        
# print(res)       
# print(sum(x))     #built-in
# print(x)

#sum of x co-ordinates but only negative values
# x = []
# res = 0
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         if value < 0.0:
#             x.append(value)
#             res += value
            
        
# print(res)       
# print(sum(x))     #built-in
# print(x)


# similarly for y and z sum and respective their +ve sum and -ve sum
# This is for z +ve
# z = []
# res = 0
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         if value > 0.0:
#             z.append(value)
#             res += value
            
        
# print(f"This is sum of all +ve z - co- ordinates using normal addition algo = {res}")       
# print(f"This is sum of all +ve z - co- ordinates using built-in sum  =        {sum(z)}")     #built-in


# Now average of x
# x = []
# with open("points.txt") as f:
#     for i in f:
#         value = float(i.split()[0])
#         if value > 0.0:
#             x.append(value)
            
# print(f"The avg is {sum(x)/len(x)}")

# Same avg code but Using list comprehension
# with open("points.txt") as f:
#     x = [ float(i.split()[0]) for i in f if float(i.split()[0]) > 0.0]

# print(f"The avg is {sum(x)/len(x)}")

# Now same code but using function naming i.e using lambda , map and filters

# with open("points.txt") as f:
    




