table = input()
codeTable = input()
line = input()
line2 = input()

dictCode = dict( zip( table , codeTable ) )  # makes pairs: table-code table
dictDeCode = {value:key for key, value in dictCode.items()}  # makes dictionary with inverted key/value items

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

if len(lineCode) == len(line):
    print(*lineCode, sep='')
elif  len(lineDeCode) == len(line):
    print(*lineDeCode, sep='')



lineCode2 = ''
lineDeCode2 = ''
c1 = 0
c2 = 0

for i in line2:
    if i in dictCode:
        c1 += 1
    elif i in dictDeCode :
        c2 += 1

if c1 > c2:
    for i in line2:
        lineCode2 += dictCode[i]
else:
    for i in line2:
        lineDeCode2 += dictDeCode[i]

if len(lineCode2) == len(line2):
    print(*lineCode2, sep='')
elif  len(lineDeCode2) == len(line2):
    print(*lineDeCode2, sep='')