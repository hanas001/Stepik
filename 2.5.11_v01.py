#lst = [4, 8, 0, 3, 4, 2, 0, 3]
lst = [int(i) for i in input().split()]

lstDouble = []
L = set(lst)
lstNew = list(set(L))
#lengthLst = len(lstNew)

for i in lstNew:
    x = lst.count(i)
    if x > 1:
        lstDouble.append(i)
        
for i in lstDouble:
    print (i, end = ' ')