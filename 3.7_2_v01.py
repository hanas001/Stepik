'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
'''
table = input('Enter abc:')
codeTable = input('Enter code table:')
line = input('Enter message to code:')
line2 = input('Enter message to decode:')

# table = 'abcd'
# codeTable = '*d%#'
# # line = 'abacabadaba'
# line = '#*%*d*%'

# print('line:', line)
# print(len(line))

dictCode = dict( zip( table , codeTable ) )  # makes pairs: table-code table
dictDeCode = {value:key for key, value in dictCode.items()}  # makes dictionary with inverted key/value items
# print('dictCode:', dictCode)
# print('dictDeCode:',dictDeCode)

lineCode = ''
lineDeCode = ''

counter1 = 0
counter2 = 0

for i in line:
    if i in dictCode:
        counter1 += 1
    elif i in dictDeCode :
        counter2 += 1

if counter1 > counter2:
    for i in line:
        lineCode += dictCode[i]
else:
    for i in line :
        lineDeCode += dictDeCode[i]

# print('line Code:', lineCode)
# print(len(lineCode))
# print('line DeCode:', lineDeCode)
# print(len(lineDeCode))

if len(lineCode) == len(line):
    print('Decoded message:', *lineCode, sep='')
elif  len(lineDeCode) == len(line):
    print('Decoded message: ', *lineDeCode, sep='')



c1 = 0
c2 = 0

for i in line2:
    if i in dictCode:
        c1 += 1
    elif i in dictDeCode :
        c2 += 1

if c1 > c2:
    for i in line2:
        lineCode += dictCode[i]
else:
    for i in line2 :
        lineDeCode += dictDeCode[i]

if len(lineCode) == len(line2):
    print('Decoded message:', *lineCode, sep='')
elif  len(lineDeCode) == len(line2):
    print('Decoded message: ', *lineDeCode, sep='')