#a, b = (int(i) for i in input().split())
a = int(input())
b = int(input())
#a = -5
#b = 12

av = 0
s = 0
k = 0
while (a % 3) != 0:
    a += 1
    #print (a)
for n in range(a, b + 1, 3):
        s += n
        k += 1
        #print (n)
av = float(s) / k

#print (s)
#print (k)
print (av)
#print (n)

#print (3 % 3)