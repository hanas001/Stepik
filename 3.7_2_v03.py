table = input()
codeTable = input()
line = input()
line2 = input()

dictCode = dict( zip( table , codeTable ) )  # makes pairs: table-code table
dictDeCode = {value:key for key, value in dictCode.items()}  # makes dictionary with inverted key/value items

lineCode = ''
lineDeCode = ''

for i in line:
    lineCode += dictCode[i]
print(*lineCode, sep='')

for i in line2:
    lineDeCode += dictDeCode[i]
print(*lineDeCode, sep='')