# coding=utf-8
n = str('123456')
n = str(input())

d0 = int(n[0])
d1 = int(n[1])
d2 = int(n[2])
d3 = int(n[-3])
d4 = int(n[-2])
d5 = int(n[-1])

len1 = (d0 + d1 + d2)
len2 = (d3 + d4 + d5)

#print (len1),
#print (type(len1))
#print (len2),
#print (type(len2))
if len1 == len2:
    print ('Счастливый')
else:
    print ('Обычный')