a = int(input())
b = int(input())
c = int(input())

n = a, b, c
mx = max(n)
mn = min(n)
rs = (a + b + c) - (mx + mn)

print (mx)
print (mn)
print (rs)