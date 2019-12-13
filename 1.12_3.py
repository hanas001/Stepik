# coding=utf-8
a = float(input())
b = float(input())
c = input()

if c == '+':
    r = a + b
    print (r)
elif c == '-':
    r = a - b
    print (r)
elif c == '*':
    r = a * b
    print (r)
elif c == '/':
    if b !=0:
        r = a / b
        print (r)
    else:
        print ('Деление на 0!')
elif c == 'mod':
    if b != 0:
        r = a % b
        print (r)
    else:
        print ('Деление на 0!')
elif c == 'pow':
    r = a ** b
    print (r)
elif c == 'div':
    if b != 0:
        r = a // b
        print (r)
    else:
        print ('Деление на 0!')