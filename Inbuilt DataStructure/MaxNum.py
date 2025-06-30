
def max_in_lst(lst):
    if not lst:
        return None
    max_Value = lst[0]
    for i in range(1,len(lst)):     # or use for i in lst[1:]
        if max_Value < lst[i]:
            max_Value= lst[i]
        i +=1                       # if use for i in lst[1:] then no need of this 
    return max_Value

i = 0
size = int(input("Enter the size of the list"))
lst = []

while i < size:
    n = int(input("Enter a value"))
    lst += [n]
    i += 1

print(max_in_lst(lst))
    