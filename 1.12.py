'''
print ('Enter a, b, c')

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

p = (a + b + c)/2
s =  pow((p * (p - a) * (p - b) * (p - c)), 0.5)

print (s)
'''

n = int(input())

if -15 < n <= 12 or 14 < n < 17 or 19 <= n:
    print ('True')
else:
    print ('False')