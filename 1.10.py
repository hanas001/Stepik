# coding=utf-8
'''
A = int(input()) #recommended
B = int(input())    #not more then
H = int(input())    #current sleep time

if A <= H <= B:
    print ('Это нормально')
elif H < A:
    print ('Недосып')
elif H > B:
    print ('Пересып')
'''

y = int(input())

if y % 4 == 0 and y % 100 != 0:
    print ('Високосный')
elif y % 400 == 0:
    print ('Високосный')
else:
    print ('Обычный')