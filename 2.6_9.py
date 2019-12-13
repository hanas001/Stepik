#lst = [5, 8, 2, 7, 8, 8, 2, 4]
#x = 8
lst = [int(i) for i in input().split()]
x = int(input())

length = len(lst)
xLstPos = []

for i in range(length):
    if lst[i] == x:
        xLstPos.append(i)
if xLstPos:
    print (*xLstPos)
else:
    print ('Отсутствует')