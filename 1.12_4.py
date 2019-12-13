# coding=utf-8
shape = raw_input()

if shape == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print float(s)
elif shape == 'круг':
    r = int(input())
    pi = 3.14
    s = pi * (r ** 2)
    print float(s)
elif shape == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    s = (p* (p - a) * (p - b) * (p - c)) ** 0.5
    print float(s)
else:
    pass