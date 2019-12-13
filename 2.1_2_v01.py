a = int(input())
b = int(input())
i = max(a, b)
while i % b != 0 or i % a != 0:
    i += 1
print (i)